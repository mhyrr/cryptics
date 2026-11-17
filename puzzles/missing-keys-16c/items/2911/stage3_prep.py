"""stage3_prep.py - make every input of stages 3 and 4 from the reader files (README, "Before the first alignment").

    python3 stage3_prep.py

Run from this directory. Writes work/:
  norm/<A|B>/<page>.txt     reader files with made-up names of one sign mapped by names.tsv (nothing else changed)
  consensus/<page>.txt      line/compare.py --consensus of the two readers, per page
  cipher-consensus.txt      the three pages joined, marks as written (base^mark): side run "separate units"
  cipher-primary.txt        the same through units.py (base+mark one unit): primary run
  plain-consensus.txt       both-plain-readers-agree text: primary run
  plain-A.txt               plain reader A alone, same clean-up: side run
  plain-print.txt           the printed text (print/opere6-...txt), cleaned: side run
  wordlist.txt              words of the printed text and words both plain readers agree on (for fluency.py)
and results/prep.tsv with the counts.
"""
import difflib, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LINE = os.path.join(HERE, "..", "..", "line")
sys.path.insert(0, LINE)
sys.path.insert(0, HERE)
import align, units  # noqa: E402

CPAGES = ["V140-1r", "V140-1v", "V140-2r"]
PPAGES = ["V139-1v", "V139-2r"]
W = os.path.join(HERE, "work")
counts = []


def rd(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


# ---- cipher side
names = dict(r.split("\t")[:2] for r in rd(os.path.join(HERE, "names.tsv")).splitlines()[1:] if r.strip())


def norm_token(tok):
    def one(t):
        q = "?" if t.endswith("?") and t != "?" else ""
        core = t[:-1] if q else t
        parts = core.split("^")
        parts[0] = names.get(parts[0], parts[0])
        return "^".join(parts) + q
    return "|".join(one(t) for t in tok.split("|"))


def norm_text(text):
    out, n = [], 0
    for row in text.splitlines():
        if not row.strip() or row.lstrip().startswith("#"):
            out.append(row)
            continue
        parts = []
        for part in re.split(r"(\[\[.*?\]\])", row):
            if part.startswith("[["):
                parts.append(part)
            else:
                toks = [norm_token(t) for t in part.split()]
                n += sum(a != b for a, b in zip(toks, part.split()))
                parts.append(" ".join(toks))
        out.append(" ".join(p for p in parts if p))
    return "\n".join(out) + "\n", n


joined = []
for page in CPAGES:
    for r in "AB":
        t, n = norm_text(rd(os.path.join(HERE, "readers", r, page + ".txt")))
        wr(os.path.join(W, "norm", r, page + ".txt"), t)
        counts.append(("names mapped, reader %s, %s" % (r, page), n))
    cons = os.path.join(W, "consensus", page + ".txt")
    os.makedirs(os.path.dirname(cons), exist_ok=True)
    subprocess.run([sys.executable, os.path.join(LINE, "compare.py"), os.path.join(W, "norm", "A", page + ".txt"),
                    os.path.join(W, "norm", "B", page + ".txt"), "--consensus", cons], check=True, stdout=subprocess.DEVNULL)
    body = [ln for ln in rd(cons).splitlines() if ln.strip() and not ln.startswith("#")]
    us, _, nl = align.parse_cipher("\n".join(body))
    signs = [u for u in us if u.kind == "sign"]
    toks = len({u.tok for u in signs})
    unread = sum(1 for u in signs if u.sym == "?")
    counts.append(("consensus lines, %s" % page, nl))
    counts.append(("consensus sign tokens, %s" % page, toks))
    counts.append(("consensus unread stretches (?), %s" % page, unread))
    joined.append("# page %s" % page)
    joined += body
cc = "\n".join(joined) + "\n"
wr(os.path.join(W, "cipher-consensus.txt"), cc)
wr(os.path.join(W, "cipher-primary.txt"), units.join_text(cc))
for name in ("cipher-consensus.txt", "cipher-primary.txt"):
    us, _, nl = align.parse_cipher(rd(os.path.join(W, name)))
    signs = [u for u in us if u.kind == "sign"]
    counts.append(("%s: lines" % name, nl))
    counts.append(("%s: sign units" % name, len(signs)))
    counts.append(("%s: unread units" % name, sum(1 for u in signs if u.sym == "?")))
    counts.append(("%s: distinct sign units" % name, len({u.sym for u in signs if u.sym != "?"})))
    counts.append(("%s: clear words" % name, sum(1 for u in us if u.kind == "clear")))


# ---- plain side
def clean_plain(text, drop_first_row):
    """-> list of rows, each a list of words as written (abbreviation brackets and [?] removed)."""
    text = re.sub(r"<del>.*?</del>", " ", text, flags=re.S)
    text = re.sub(r"</?ins>", " ", text)
    rows = [r for r in text.splitlines() if r.strip() and not r.lstrip().startswith("#")]
    if drop_first_row:
        rows = rows[1:]
    out = []
    for r in rows:
        r = r.replace("[?]", "").replace("[…]", " … ").replace("[...]", " … ")
        r = re.sub(r"[()]", "", r)
        out.append(r.split())
    return out


def key(w):
    return "…" if w == "…" else align.norm_letters(w)


def plain_consensus():
    out_rows, kept, lost_a, wa_total, la_total, lkept = [], 0, 0, 0, 0, 0
    for k, page in enumerate(PPAGES):
        ra = clean_plain(rd(os.path.join(HERE, "readers", "plain-A", page + ".txt")), k == 0)
        rb = clean_plain(rd(os.path.join(HERE, "readers", "plain-B", page + ".txt")), k == 0)
        wa = [(w, i) for i, row in enumerate(ra) for w in row if key(w)]
        wb = [w for row in rb for w in row if key(w)]
        ka, kb = [key(w) for w, _ in wa], [key(w) for w in wb]
        wa_total += sum(1 for x in ka if x != "…")
        la_total += sum(len(x) for x in ka if x != "…")
        rows = [[] for _ in ra]
        sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            same = op == "equal" or ("…" not in ka[i1:i2] + kb[j1:j2] and "".join(ka[i1:i2]) == "".join(kb[j1:j2]) and i2 > i1)
            if same:
                for w, i in wa[i1:i2]:
                    if key(w) == "…":
                        rows[i].append("[…]")
                    else:
                        rows[i].append(w)
                        kept += 1
                        lkept += len(key(w))
            else:
                row = wa[i1][1] if i2 > i1 else (wa[i1 - 1][1] if i1 else 0)
                rows[row].append("[…]")
                lost_a += sum(1 for x in ka[i1:i2] if x != "…")
        out_rows.append("# page %s" % page)
        out_rows += [" ".join(r) for r in rows]
    counts.append(("plain reader A: words (heading row left out)", wa_total))
    counts.append(("plain reader A: letters", la_total))
    counts.append(("plain consensus: words kept", kept))
    counts.append(("plain consensus: letters kept", lkept))
    counts.append(("plain consensus: reader A words gone to lacunae", lost_a))
    counts.append(("plain consensus: share of reader A words kept", round(kept / wa_total, 3)))
    counts.append(("plain consensus: share of reader A letters kept", round(lkept / la_total, 3)))
    text = "\n".join(out_rows) + "\n"
    text = re.sub(r"(\[…\] ?)+", "[…] ", text)
    counts.append(("plain consensus: lacuna marks", text.count("[…]")))
    return text


pc = plain_consensus()
wr(os.path.join(W, "plain-consensus.txt"), pc)
pa = []
for k, page in enumerate(PPAGES):
    pa.append("# page %s" % page)
    pa += [" ".join("[…]" if w == "…" else w for w in row)
           for row in clean_plain(rd(os.path.join(HERE, "readers", "plain-A", page + ".txt")), k == 0)]
wr(os.path.join(W, "plain-A.txt"), "\n".join(pa) + "\n")


def print_text():
    rows = [r[4:] for r in rd(os.path.join(HERE, "print", "opere6-niccolini-1510-08-05.txt")).splitlines()
            if re.match(r"P5[45]\|", r)]
    rows = [r for r in rows[1:] if not r.startswith("*")]          # heading row and the editors' sub-note left out
    text = ""
    for r in rows:
        r = r.replace("[?]", "").replace("(?)", "").replace("*", "")
        r = r.replace("⟨…⟩", " […] ").replace("⟨", "").replace("⟩", "").strip()
        if text.endswith("-"):
            if r.startswith("[…]"):
                text = text[:-1] + " " + r                          # the word's second half is lost
            else:
                text = text[:-1] + r
        else:
            text += ("\n" if text else "") + r
    return text + "\n"


pp = print_text()
wr(os.path.join(W, "plain-print.txt"), pp)
for name in ("plain-consensus.txt", "plain-A.txt", "plain-print.txt"):
    P, wbd, lac, _ = align.parse_plain(rd(os.path.join(W, name)))
    counts.append(("%s: letters" % name, len(P)))
    counts.append(("%s: lacuna marks" % name, sum(lac)))

words = set()
for w in re.findall(r"[^\W\d_]+", pp.replace("[…]", " ")):
    words.add(align.norm_letters(w))
for w in pc.replace("[…]", " ").split():
    if not w.startswith("#"):
        words.add(align.norm_letters(w))
words = sorted(w for w in words if w)
wr(os.path.join(W, "wordlist.txt"), "# words of the printed text and words both plain readers agree on; NOT independent of the pair\n" + "\n".join(words) + "\n")
counts.append(("wordlist: words", len(words)))
counts.append(("wordlist: words of 3 letters or more", sum(1 for w in words if len(w) >= 3)))

wr(os.path.join(HERE, "results", "prep.tsv"), "what\tcount\n" + "".join("%s\t%s\n" % c for c in counts))
print(rd(os.path.join(HERE, "results", "prep.tsv")), end="")
