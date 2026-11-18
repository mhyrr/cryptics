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


def b_test2():
    kmap = provisional(align.read_key(KEY44))
    units, _, _ = align.parse_cipher(rd(W, "c269-CD.txt"))
    P, _, lac, _ = align.parse_plain(rd(W, "p270.txt"))
    align.AB_BEAM = 1500

    def matches(k):
        score, tab, ops = align.beam_read(units, P, lac, None, k)
        return sum(1 for u, (kind, j0, j1) in zip(units, ops) if kind == "M" and u.sym in k), score
    true_m, true_s = matches(kmap)
    rng, sh = random.Random(1), []
    signs, vals = list(kmap), [kmap[s] for s in kmap]
    for _ in range(20):
        v = vals[:]
        rng.shuffle(v)
        sh.append(matches(dict(zip(signs, v)))[0])
    held = sum(1 for u in units if u.sym in kmap)
    out = (f"held_sign_places\t{held}\ntrue_matches\t{true_m}\ntrue_beam_score\t{true_s:.1f}\n"
           f"shuffle_matches\t{' '.join(map(str, sorted(sh)))}\nshuffle_mean\t{sum(sh) / len(sh):.1f}\n"
           f"shuffle_max\t{max(sh)}\nratio_to_mean\t{true_m / (sum(sh) / len(sh)):.2f}\n"
           f"pass\t{true_m > max(sh) and true_m >= 1.5 * sum(sh) / len(sh)}\n")
    wr(os.path.join(RES, "b-test2.tsv"), out)
    print(out)


# ---------------------------------------------------------------- third stage (README, "Third stage")
KEY269, KEY1 = os.path.join(HERE, "key-c269-v0.tsv"), os.path.join(HERE, "key-v1.tsv")
MARKED = ("certain", "probable")


def w_build():
    out = subprocess.run([sys.executable, os.path.join(LINE, "align.py"), "build", os.path.join(W, "c269-CD.txt"),
                          os.path.join(W, "p270.txt"), "--out", KEY269, "--abridged"], capture_output=True, text=True)
    rows = align.read_key(KEY269)
    st = {}
    for r in rows:
        st[r["status"]] = st.get(r["status"], 0) + 1
    msg = [out.stdout.strip(), f"exit {out.returncode}", f"rows {st}", f"null share {align.null_share(rows):.3f}"]
    wr(os.path.join(RES, "w-build.tsv"), "\n".join(msg) + "\n")
    print("\n".join(msg), out.stderr[-300:] if out.returncode else "")


def w_check():
    old = provisional(align.read_key(KEY44))
    new_rows = [r for r in align.read_key(KEY269) if r["status"] in MARKED]
    new = {r["unit"]: r["value"] for r in new_rows}
    shared = sorted(s for s in new if s in old)
    same = [s for s in shared if new[s] == old[s]]
    ok = len(shared) >= 8 and len(same) >= 0.8 * len(shared)
    out = [f"marked_new_rows\t{len(new)}", f"shared_signs\t{len(shared)}", f"same_value\t{len(same)}",
           f"differ\t{' '.join(f'{s}:{old[s]}/{new[s]}' for s in shared if new[s] != old[s]) or '-'}",
           f"pass\t{ok}"]
    if ok:
        add = [r for r in new_rows if r["unit"] not in old]
        sup = {r["unit"]: int(r["support"]) for r in align.read_key(KEY44)}
        swap = {r["unit"] for r in new_rows if r["unit"] in old and r["value"] != old[r["unit"]]
                and int(r["support"]) > sup[r["unit"]]}          # amended rule: more witnessed places stands
        rows = [dict(r, status="probable", alts="c44") for r in align.read_key(KEY44)
                if r["unit"] in old and r["unit"] not in swap]
        rows += [dict(r, alts="c269") for r in add]
        rows += [dict(r, alts="c269, differs from c44") for r in new_rows if r["unit"] in swap]
        out.append(f"c269_value_stands\t{' '.join(sorted(swap)) or '-'}")
        align.write_key(rows, KEY1)
        kinds = {}
        for r in add:
            kinds[r["type"]] = kinds.get(r["type"], 0) + 1
        out += [f"added_rows\t{len(add)}\t{kinds}", f"table_v1_rows\t{len(rows)}"]
    wr(os.path.join(RES, "w-check.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def c14_text():
    """-> list of (name, cipher text) the test runs on, and the E-F agreement."""
    te, tf = rd(R, "E", "c14.txt"), rd(R, "F", "c14.txt")
    c = compare.compare_texts(te, tf)
    agr = compare.ratio(c["tok_matched"], c["tokens_a"], c["tokens_b"])
    if agr >= 0.85:
        compare.write_consensus(te, tf, os.path.join(W, "c14-EF.txt"))
        return [("c14 E+F consensus", rd(W, "c14-EF.txt"))], agr, c
    return [("c14 reader E", te), ("c14 reader F", tf)], agr, c


def c14_prep():
    texts, agr, c = c14_text()
    rows = ["piece\ttokens_a\ttokens_b\tagreement", f"c14 E,F\t{c['tokens_a']}\t{c['tokens_b']}\t{agr:.3f}"]
    a, b = plain_words(rd(R, "PC", "p14.txt")), plain_words(rd(R, "PD", "p14.txt"))
    cons, pagr = plain_consensus(a, b)
    wr(os.path.join(W, "p14.txt"), " ".join(cons) + "\n")
    rows.append(f"p14 PC,PD\t{len(a)}\t{len(b)}\t{pagr:.3f}")
    rows.append(f"test_runs_on\t{'; '.join(n for n, _ in texts)}")
    wr(os.path.join(RES, "agreement-c14.tsv"), "\n".join(rows) + "\n")
    print("\n".join(rows))


def wordlist():
    words = set()
    for rdr, names in (("PA", ("p270", "p44")), ("PB", ("p270", "p44")), ("PC", ("p14",)), ("PD", ("p14",))):
        for n in names:
            words |= set(plain_words(rd(R, rdr, n + ".txt")))
    for w in re.split(r"[^a-z]+", rd(HERE, "..", "2911", "bench", "inputs", "plain-full.txt").lower()):
        words.add(align.norm_letters(w))
    return sorted(w for w in words if len(w) >= 4 and w != "[...]")


def cover(s, words):
    """Most letters of s covered by words laid without overlap; '?' is any one letter; a word counts only
    with >= 3 valued letters and >= 2/3 of its letters valued."""
    n = len(s)
    best = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        b = best[i + 1]
        for w in words:
            L = len(w)
            if i + L > n:
                continue
            seg = s[i:i + L]
            known = L - seg.count("?")
            if known < 3 or 3 * known < 2 * L:
                continue
            if all(c == "?" or c == d for c, d in zip(seg, w)):
                b = max(b, L + best[i + L])
        best[i] = b
    return best[0]


def c14_string(text, kmap):
    units, _, _ = align.parse_cipher(text)
    return "".join(kmap.get(u.sym) or "?" for u in units if u.kind == "sign"), units


def table_in_force():
    return align.key_map(align.read_key(KEY1)) if os.path.exists(KEY1) else provisional(align.read_key(KEY44))


def c14_test():
    kmap, words = table_in_force(), wordlist()
    texts, agr, _ = c14_text()
    out, ok_all = [f"table_values\t{len(kmap)}", f"wordlist\t{len(words)}", f"agreement_E_F\t{agr:.3f}"], True
    for name, text in texts:
        s, units = c14_string(text, kmap)
        true = cover(s, words)
        rng, signs, vals, sh = random.Random(1), list(kmap), [kmap[k] for k in kmap], []
        for _ in range(200):
            v = vals[:]
            rng.shuffle(v)
            sh.append(cover(c14_string(text, dict(zip(signs, v)))[0], words))
        below = sum(1 for x in sh if x < true)
        ok = below >= 190
        ok_all = ok_all and ok
        out += [f"## {name}", f"signs\t{len(s)}", f"valued\t{len(s) - s.count('?')}", f"covered_true\t{true}",
                f"shuffles_below_true\t{below} of 200", f"shuffle_mean\t{sum(sh) / len(sh):.1f}",
                f"shuffle_max\t{max(sh)}", f"pass\t{ok}"]
    out.append(f"pass_all\t{ok_all}")
    wr(os.path.join(RES, "c14-test.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def c14_decode():
    kmap = table_in_force()
    out = []
    for rdr in "EFAB":
        text = rd(R, rdr, "c14.txt")
        s, units = c14_string(text, kmap)
        out += [f"## c14 reader {rdr}", " ".join(f"{u.sym}={kmap.get(u.sym) or '?'}" for u in units), s]
    wr(os.path.join(RES, "c14-decode.txt"), "\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd = sys.argv[1]
    {"prep": prep, "build": lambda: build(sys.argv[2:]), "heldout": heldout, "transfer": transfer,
     "decode": decode, "b-build": b_build, "b-test": b_test, "b-decode": b_decode, "b-test2": b_test2,
     "w-build": w_build, "w-check": w_check,
     "c14-prep": c14_prep, "c14-test": c14_test, "c14-decode": c14_decode}[cmd]()
