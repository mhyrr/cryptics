"""run.py - stages 2-5 of item 1336 from the readers' files. Every figure in README.md comes from here.

    python3 run.py prep       agreement, consensus files in work/, results/agreement.tsv
    python3 run.py build      key-v0.tsv from the F 47 pair (plain build), work/aligned.txt, results/build.tsv
    python3 run.py heldout    results/heldout.tsv (five folds on the pair)
    python3 run.py transfer   decode the c. 44r slip with key-v0.tsv, score against its note: results/transfer.tsv
    python3 run.py decode     results/decode-<passage>.txt for c269, c44, c14 (every unvalued sign shown as ?)
Plan B (README): b-build (key-c44-v0.tsv from the c. 44r pair), b-test (decode c. 269r, score against c. 270r),
b-decode (results/b-decode.txt: the bare line on c. 14r by each reader, and both slips).
Cipher consensus: tokens both readers agree on; a stretch of disagreement is one '?'. Plain consensus: words
both readers agree on (letters only, align.norm_letters); a stretch of disagreement is '[...]'.
"""
import difflib, os, random, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LINE = os.path.join(HERE, "..", "..", "line")
sys.path.insert(0, LINE)
import align, compare  # noqa: E402

R, W, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "work"), os.path.join(HERE, "results")
KEY = os.path.join(HERE, "key-v0.tsv")


def rd(*p):
    return open(os.path.join(*p), encoding="utf-8").read()


def wr(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)


def plain_words(text):
    text = re.sub(r"(?m)^#.*$", " ", text)
    text = re.sub(r"<struck>.*?</struck>", " ", text, flags=re.S)
    text = text.replace("[?]", " ").replace("^", " ")
    out = []
    for w in re.split(r"\s+", text):
        if re.match(r"\[(\.\.\.|…)\]", w):
            out.append("[...]")
        else:
            n = align.norm_letters(w)
            if n:
                out.append(n)
    return out


def plain_consensus(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out, same = [], 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            out += a[i1:i2]
            same += i2 - i1
        elif not out or out[-1] != "[...]":
            out.append("[...]")
    return out, 2 * same / max(1, len(a) + len(b))


def prep():
    rows = ["piece\ttokens_a\ttokens_b\tagreement\tconsensus_tokens\tconsensus_unread"]
    for p in ("c269", "c44", "c14"):
        ta, tb = rd(R, "A", p + ".txt"), rd(R, "B", p + ".txt")
        r = compare.compare_texts(ta, tb)
        compare.write_consensus(ta, tb, os.path.join(W, p + ".txt"))
        us, _, _ = align.parse_cipher(rd(W, p + ".txt"))
        rows.append(f"{p}\t{r['tokens_a']}\t{r['tokens_b']}\t{compare.ratio(r['tok_matched'], r['tokens_a'], r['tokens_b']):.3f}\t{len(us)}\t"
                    f"{sum(u.sym == '?' for u in us)}")
    for p in ("p270", "p44"):
        a, b = plain_words(rd(R, "PA", p + ".txt")), plain_words(rd(R, "PB", p + ".txt"))
        c, agr = plain_consensus(a, b)
        wr(os.path.join(W, p + ".txt"), " ".join(c) + "\n")
        wr(os.path.join(W, p + "-PA.txt"), " ".join(a) + "\n")
        rows.append(f"{p}\t{len(a)}\t{len(b)}\t{agr:.3f}\t{len(c)}\t{c.count('[...]')}")
    wr(os.path.join(RES, "agreement.tsv"), "\n".join(rows) + "\n")
    print("\n".join(rows))


def build(extra=()):
    out = subprocess.run([sys.executable, os.path.join(LINE, "align.py"), "build", os.path.join(W, "c269.txt"),
                          os.path.join(W, "p270.txt"), "--out", KEY, "--aligned", os.path.join(W, "aligned.txt"),
                          *extra], capture_output=True, text=True)
    rows = align.read_key(KEY) if os.path.exists(KEY) else []
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    msg = out.stdout.strip().splitlines()[-1:] + [f"exit {out.returncode}", f"rows {st}",
                                                  f"null share {align.null_share(rows):.3f}"]
    wr(os.path.join(RES, "build.tsv"), "\n".join(msg) + "\n")
    print("\n".join(msg), out.stderr[-400:] if out.returncode else "")


def heldout():
    units, P, wb, lac, pairs = align.load_pair(os.path.join(W, "c269.txt"), os.path.join(W, "p270.txt"))
    r = align.heldout(units, P, wb, lac, pairs)
    s = "".join(f"{k}\t{r[k]:.3f}\n" for k in ("accuracy", "recall", "coverage", "control"))
    s += f"units\t{r['units']}\nletters\t{r['letters']}\n"
    wr(os.path.join(RES, "heldout.tsv"), s)
    print(s)


def transfer():
    kmap = align.key_map(align.read_key(KEY))
    units, _, _ = align.parse_cipher(rd(W, "c44.txt"))
    signs = [u for u in units if u.kind == "sign"]
    rng = random.Random(1)
    rows = ["plain\tsigns\tvalued\taccuracy\trecall\tcontrol"]
    for name in ("p44", "p44-PA"):
        P, _, _, _ = align.parse_plain(rd(W, name + ".txt"))
        m, d, t = align.score(align.decode_units(units, kmap), P)
        cm = cd = 0
        for _ in range(20):
            a, b, _ = align.score(align.decode_units(units, align.permuted(kmap, rng)), P)
            cm, cd = cm + a, cd + b
        rows.append(f"{name}\t{len(signs)}\t{sum(u.sym in kmap for u in signs) / max(1, len(signs)):.3f}\t"
                    f"{m / max(1, d):.3f}\t{m / max(1, t):.3f}\t{cm / max(1, cd):.3f}")
    wr(os.path.join(RES, "transfer.tsv"), "\n".join(rows) + "\n")
    print("\n".join(rows))


def decode():
    kmap = align.key_map(align.read_key(KEY))
    for p in ("c269", "c44", "c14"):
        units, _, _ = align.parse_cipher(rd(W, p + ".txt"))
        s = "".join(f"{ln:3d}  {t}\n" for ln, t in align.render(units, align.decode_units(units, kmap)))
        wr(os.path.join(RES, f"decode-{p}.txt"), s)
        print(p)
        print(s)


# ---------------------------------------------------------------- plan B (README, "Plan B")
KEY44 = os.path.join(HERE, "key-c44-v0.tsv")


def provisional(rows):
    """Every row whose value holds at 60% of its places, whatever the count."""
    return {r["unit"]: r["value"] for r in rows if float(r["share"]) >= 0.6}


def b_build():
    """`b-build`: plain build (as registered). `b-build --abridged`: after the plain build stopped on its null
    check; no --aligned file in that mode."""
    extra = ["--abridged"] if "--abridged" in sys.argv else ["--aligned", os.path.join(W, "aligned-c44.txt")]
    out = subprocess.run([sys.executable, os.path.join(LINE, "align.py"), "build", os.path.join(W, "c44.txt"),
                          os.path.join(W, "p44.txt"), "--out", KEY44, *extra], capture_output=True, text=True)
    rows = align.read_key(KEY44)
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    prov = provisional(rows)
    kinds = {}
    for v in prov.values():
        kinds[align.unit_type(v)] = kinds.get(align.unit_type(v), 0) + 1
    msg = [out.stdout.strip(), f"exit {out.returncode}", f"rows {st}", f"provisional rows {len(prov)}: {kinds}",
           f"null share {align.null_share(rows):.3f}"]
    wr(os.path.join(RES, "b-build-abridged.tsv" if "--abridged" in sys.argv else "b-build.tsv"), "\n".join(msg) + "\n")
    print("\n".join(msg), out.stderr[-300:] if out.returncode else "")


def b_test():
    kmap = provisional(align.read_key(KEY44))
    compare.write_consensus(rd(R, "C", "c269.txt"), rd(R, "D", "c269.txt"), os.path.join(W, "c269-CD.txt"))
    P, _, _, _ = align.parse_plain(rd(W, "p270.txt"))
    rng = random.Random(1)
    rows = ["cipher\tsigns\tunread\tvalued_of_read\tdecoded_letters\taccuracy\trecall\tcontrol"]
    for name, text in (("c269 C+D consensus", rd(W, "c269-CD.txt")), ("c269 reader C", rd(R, "C", "c269.txt")),
                       ("c269 reader D", rd(R, "D", "c269.txt"))):
        units, _, _ = align.parse_cipher(text)
        signs = [u for u in units if u.kind == "sign" and u.sym != "?"]
        m, d, t = align.score(align.decode_units(units, kmap), P)
        cm = cd = 0
        for _ in range(20):
            a, b, _ = align.score(align.decode_units(units, align.permuted(kmap, rng)), P)
            cm, cd = cm + a, cd + b
        rows.append(f"{name}\t{len(units)}\t{len(units) - len(signs)}\t"
                    f"{sum(u.sym in kmap for u in signs) / max(1, len(signs)):.3f}\t{d}\t{m / max(1, d):.3f}\t"
                    f"{m / max(1, t):.3f}\t{cm / max(1, cd):.3f}")
    wr(os.path.join(RES, "b-test.tsv"), "\n".join(rows) + "\n")
    print("\n".join(rows))


def b_decode():
    kmap = provisional(align.read_key(KEY44))
    out = []
    for name, text in (("c14 reader A", rd(R, "A", "c14.txt")), ("c14 reader B", rd(R, "B", "c14.txt")),
                       ("c44 consensus", rd(W, "c44.txt")), ("c269 C+D consensus", rd(W, "c269-CD.txt"))):
        units, _, _ = align.parse_cipher(text)
        out.append(f"## {name}")
        if name.startswith("c14"):
            out.append(" ".join(f"{u.sym}={kmap.get(u.sym, '?') or '∅'}" for u in units))
        out += [f"{ln:3d}  {t}" for ln, t in align.render(units, align.decode_units(units, kmap))]
    wr(os.path.join(RES, "b-decode.txt"), "\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd = sys.argv[1]
    {"prep": prep, "build": lambda: build(sys.argv[2:]), "heldout": heldout, "transfer": transfer,
     "decode": decode, "b-build": b_build, "b-test": b_test, "b-decode": b_decode}[cmd]()
