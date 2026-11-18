"""run.py - item 2351 from the readers' files. Every figure in README.md comes from here.

    python3 run.py prep      agreement of cipher readers, merged cipher text, plain texts: work/, results/prep.tsv
    python3 run.py build     four tables, one per plain reading: work/key-P?.tsv, results/build.tsv
    python3 run.py tables    pairwise agreement of the tables; key-v0.tsv if the bar is met: results/tables.tsv
"""
import csv, itertools, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LINE = os.path.join(HERE, "..", "..", "line")
sys.path.insert(0, LINE)
import align, compare, merge  # noqa: E402

R, W, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "work"), os.path.join(HERE, "results")
CIPHER, PLAIN = "ABC", ("PA", "PB", "PC", "PD")
MARKED = ("certain", "probable")
RENAME = {r["from"]: r["to"] for r in csv.DictReader(open(os.path.join(HERE, "names.tsv")), delimiter="\t")}


def rd(*p):
    return open(os.path.join(*p), encoding="utf-8").read()


def wr(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)


def rename(tok):
    """Map made-up base names; keep marks, '?' and '|'."""
    def one(t):
        q = "?" if t.endswith("?") and t != "?" else ""
        t = t[:-1] if q else t
        base, _, marks = t.partition("^")
        return RENAME.get(base, base) + ("^" + marks if marks else "") + q
    return "|".join(one(t) for t in tok.split("|"))


def cipher_rows(reader):
    """Rows that hold cipher signs, clear words removed, from the row where the cipher starts."""
    rows = []
    for ln in rd(R, reader, "A.txt").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        toks = [rename(t) for t in re.sub(r"\[\[.*?\]\]", " ", ln).split()]
        if toks:
            rows.append(toks)
    return rows


def join(tok):
    """base^mark -> base+mark: a base with its mark is one sign for the builder."""
    return tok.replace("^", "+")


def plain_words(text):
    text = re.sub(r"(?m)^#.*$", " ", text)
    text = re.sub(r"<struck>.*?</struck>", " ", text, flags=re.S)
    text = text.replace("[?]", " ").replace("^", " ")
    out = []
    for w in re.split(r"\s+", text):
        if re.match(r"\[(\.\.\.|…)\]", w):
            if not out or out[-1] != "[...]":
                out.append("[...]")
        else:
            n = align.norm_letters(w)
            if n:
                out.append(n)
    return out


def prep():
    rows = {r: cipher_rows(r) for r in CIPHER}
    out = ["reader\trows\tsigns"] + [f"{r}\t{len(rows[r])}\t{sum(map(len, rows[r]))}" for r in CIPHER]
    if len({len(v) for v in rows.values()}) != 1:
        raise SystemExit("\n".join(out) + "\nreaders differ in cipher rows")
    out.append("pair\tagreement\tagreement_bases_only")
    for a, b in itertools.combinations(CIPHER, 2):
        ta = "\n".join(" ".join(r) for r in rows[a])
        tb = "\n".join(" ".join(r) for r in rows[b])
        c = compare.compare_texts(ta, tb)
        strip = lambda t: re.sub(r"\^[^ |?\n]+", "", t)
        d = compare.compare_texts(strip(ta), strip(tb))
        out.append(f"{a},{b}\t{compare.ratio(c['tok_matched'], c['tokens_a'], c['tokens_b']):.3f}\t"
                   f"{compare.ratio(d['tok_matched'], d['tokens_a'], d['tokens_b']):.3f}")
    lines, tot = [], {}
    for k in range(len(rows["A"])):
        toks, st = merge.merge_line([rows[r][k] for r in CIPHER], 0.5)
        lines.append(" ".join(join(t) for t in toks))
        for x, y in st.items():
            tot[x] = tot.get(x, 0) + y
    wr(os.path.join(W, "A-merged.txt"), "# letter A, readers A B C merged\n" + "\n".join(lines) + "\n")
    signs = [t for ln in lines for t in ln.split() if t != "?"]
    out += [f"merged: columns {tot['columns']}, kept {tot['kept']}, unread {tot['unread']}, dropped "
            f"{tot['dropped']}, kept with every vote {tot['unanimous']}",
            f"merged: distinct signs {len(set(signs))}, seen 5 times or more "
            f"{sum(1 for s in set(signs) if signs.count(s) >= 5)}"]
    out.append("plain\twords\tholes\tletters\tfrom_word")
    for p in PLAIN:
        w = plain_words(rd(R, p, "p233.txt"))
        cut = next((i + 1 for i, x in enumerate(w[:60]) if x in ("sera", "lasera")), None)
        if cut is None:                        # the reader did not read "sera": start after the fortieth token
            cut = 40
            note = "no 'sera' read; cut at token 40"
        else:
            note = f"after 'sera' (token {cut})"
        w = w[cut:]
        wr(os.path.join(W, f"plain-{p}.txt"), " ".join(w) + "\n")
        out.append(f"{p}\t{sum(x != '[...]' for x in w)}\t{w.count('[...]')}\t"
                   f"{sum(len(x) for x in w if x != '[...]')}\t{note}")
    wr(os.path.join(RES, "prep.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def build():
    out = []
    procs = {p: subprocess.Popen([sys.executable, os.path.join(LINE, "align.py"), "build",
                                  os.path.join(W, "A-merged.txt"), os.path.join(W, f"plain-{p}.txt"), "--out",
                                  os.path.join(W, f"key-{p}.tsv"), "--abridged"], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True) for p in PLAIN}
    for p, pr in procs.items():
        so, se = pr.communicate()
        rows = align.read_key(os.path.join(W, f"key-{p}.tsv")) if pr.returncode == 0 else []
        st = {}
        for r in rows:
            st[r["status"]] = st.get(r["status"], 0) + 1
        out.append(f"{p}\texit {pr.returncode}\t{so.strip().splitlines()[-1] if so.strip() else se[-200:]}\t"
                   f"null share {align.null_share(rows):.3f}")
    wr(os.path.join(RES, "build.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def tables():
    t = {p: {r["unit"]: r["value"] for r in align.read_key(os.path.join(W, f"key-{p}.tsv"))
             if r["status"] in MARKED} if os.path.exists(os.path.join(W, f"key-{p}.tsv")) else {} for p in PLAIN}
    out, good = ["pair\tshared_marked\tsame\tshare"], 0
    for a, b in itertools.combinations(PLAIN, 2):
        sh = [s for s in t[a] if s in t[b]]
        same = sum(t[a][s] == t[b][s] for s in sh)
        ok = len(sh) >= 10 and same >= 0.8 * len(sh)
        good += ok
        out.append(f"{a},{b}\t{len(sh)}\t{same}\t{same / max(1, len(sh)):.3f}\t{'ok' if ok else ''}")
    out.append(f"marked rows per table\t{' '.join(f'{p}:{len(t[p])}' for p in PLAIN)}")
    out.append(f"pairs meeting the bar\t{good}")
    out.append(f"pass\t{good >= 2}")
    if good >= 2:
        rows = []
        for s in sorted({s for p in PLAIN for s in t[p]}):
            vals = [t[p][s] for p in PLAIN if s in t[p]]
            if len(vals) >= 2 and len(set(vals)) == 1:
                rows.append(dict(unit=s, value=vals[0], type=align.unit_type(vals[0]), support=len(vals),
                                 conflict=0, share=1.0, status="probable", alts="tables agreeing",
                                 positions=""))
        align.write_key(rows, os.path.join(HERE, "key-v0.tsv"))
        kinds = {}
        for r in rows:
            kinds[r["type"]] = kinds.get(r["type"], 0) + 1
        out.append(f"key-v0 rows\t{len(rows)}\t{kinds}")
    wr(os.path.join(RES, "tables.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def tied_build():
    out = []
    procs = {p: subprocess.Popen([sys.executable, os.path.join(HERE, "tied.py"), "build",
                                  os.path.join(W, "A-merged.txt"), os.path.join(W, f"plain-{p}.txt"),
                                  os.path.join(W, f"tied-{p}.tsv")], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True) for p in PLAIN}
    for p, pr in procs.items():
        so, se = pr.communicate()
        out.append(f"{p}\texit {pr.returncode}\t{so.strip() or se[-200:]}")
    wr(os.path.join(RES, "tied-build.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def tied_tables():
    t = {}
    for p in PLAIN:
        f = os.path.join(W, f"tied-{p}.tsv")
        t[p] = {r["unit"]: r["value"] for r in align.read_key(f) if r["status"] in MARKED} if os.path.exists(f) else {}
    out, good = ["pair\tshared_bases_and_marks\tsame\tshare\tshared_other\tsame_other"], 0
    for a, b in itertools.combinations(PLAIN, 2):
        sh = [s for s in t[a] if s in t[b] and s[0] in "BM"]
        same = sum(t[a][s] == t[b][s] for s in sh)
        so = [s for s in t[a] if s in t[b] and s[0] == "W"]
        ok = len(sh) >= 8 and same >= 0.8 * len(sh)
        good += ok
        out.append(f"{a},{b}\t{len(sh)}\t{same}\t{same / max(1, len(sh)):.3f}\t{len(so)}\t"
                   f"{sum(t[a][s] == t[b][s] for s in so)}\t{'ok' if ok else ''}")
    out.append("marked rows per table\t" + " ".join(
        f"{p}:{sum(k[0] in 'BM' for k in t[p])}+{sum(k[0] == 'W' for k in t[p])}" for p in PLAIN))
    out.append(f"pairs meeting the bar\t{good}")
    out.append(f"pass\t{good >= 2}")
    if good >= 2:
        rows = []
        for s in sorted({s for p in PLAIN for s in t[p]}):
            vals = [t[p][s] for p in PLAIN if s in t[p]]
            if len(vals) >= 2 and len(set(vals)) == 1:
                rows.append(dict(unit=s, value=vals[0], type=align.unit_type(vals[0]), support=len(vals),
                                 conflict=0, share=1.0, status="probable", alts="tables agreeing", positions=""))
        align.write_key(rows, os.path.join(HERE, "key-v0.tsv"))
        out.append(f"key-v0 entries\t{len(rows)}\tbases {sum(r['unit'][0] == 'B' for r in rows)}, marks "
                   f"{sum(r['unit'][0] == 'M' for r in rows)}, other signs {sum(r['unit'][0] == 'W' for r in rows)}")
        out.append("entries marked differently by two tables\t" + (" ".join(sorted(
            s for s in {s for p in PLAIN for s in t[p]} if len({t[p][s] for p in PLAIN if s in t[p]}) > 1)) or "-"))
    wr(os.path.join(RES, "tied-tables.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def solve_run():
    out = subprocess.run([sys.executable, os.path.join(HERE, "solve.py"), "run", os.path.join(W, "A-merged.txt"),
                          os.path.join(HERE, "key-s0.tsv"), "--restarts", "8", "--seed", "1"],
                         capture_output=True, text=True)
    wr(os.path.join(RES, "solve.txt"), out.stdout + out.stderr[-500:])
    print(out.stdout, out.stderr[-500:])


def solve_test():
    import collections, random
    import solve, tied
    units, _, _ = align.parse_cipher(rd(W, "A-merged.txt"))
    mk = tied.markable(units)
    seq, bases, mks, others = solve.setup(units, mk)
    t = {r["unit"]: r["value"] for r in align.read_key(os.path.join(HERE, "key-s0.tsv"))}
    kb, km, kw = [t["B:" + b] for b in bases], [t["M:" + m] for m in mks], [t.get("W:" + w, "") for w in others]
    seen = collections.Counter()
    for p in PLAIN:
        for w in set(plain_words(rd(R, p, "p233.txt"))):
            if len(w) >= 5 and w != "[...]":
                seen[w] += 1
    words = sorted(w for w, n in seen.items() if n >= 2)

    def count(kb, km, kw):
        s = "".join(p or "" if x is not None else "?" for p, x in zip(solve.decode(seq, kb, km, kw), seq))
        return sum(w in s for w in words), s
    true, dec = count(kb, km, kw)
    rng, sh = random.Random(1), []
    for _ in range(200):
        a, b, c = kb[:], km[:], kw[:]
        rng.shuffle(a)
        rng.shuffle(b)
        rng.shuffle(c)
        sh.append(count(a, b, c)[0])
    below = sum(x < true for x in sh)
    found = [w for w in words if w in dec]
    out = [f"words_in_list\t{len(words)}", f"found_in_decode\t{true}", f"shuffles_below\t{below} of 200",
           f"shuffle_mean\t{sum(sh) / len(sh):.2f}", f"shuffle_max\t{max(sh)}", f"pass_words\t{below >= 190}",
           "found\t" + " ".join(found)]
    wr(os.path.join(RES, "solve-test.tsv"), "\n".join(out) + "\n")
    wr(os.path.join(RES, "solve-decode-A.txt"), "\n".join(dec[k:k + 100] for k in range(0, len(dec), 100)) + "\n")
    print("\n".join(out))


def forms():
    jobs = {}
    for order in ("CV", "VC"):
        for bare in ("", "a", "e", "i", "o", "u"):
            env = dict(os.environ, H9_ORDER=order, H9_BARE=bare)
            out = os.path.join(W, f"key-form-{order}-{bare or 'none'}.tsv")
            jobs[(order, bare)] = subprocess.Popen(
                [sys.executable, os.path.join(HERE, "solve.py"), "run", os.path.join(W, "A-merged.txt"), out,
                 "--restarts", "3", "--seed", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    rows = ["order\tbare\tbest_per_letter\tletters\tmarks"]
    for (order, bare), pr in jobs.items():
        so, se = pr.communicate()
        per = [(float(m.group(2)), int(m.group(1))) for m in re.finditer(r"letters (\d+); per letter (-[\d.]+)", so)]
        mk = re.search(r"marks: (.*)", so)
        b = max(per) if per else (float("nan"), 0)
        rows.append(f"{order}\t{bare or 'none'}\t{b[0]:.3f}\t{b[1]}\t{mk.group(1) if mk else se[-100:]}")
    wr(os.path.join(RES, "forms.tsv"), "\n".join(rows) + "\n")
    print("\n".join(rows))


def pe():
    import collections, tied
    w = plain_words(rd(R, "PE", "p233.txt"))
    cut = next(i + 1 for i, x in enumerate(w[:80]) if x in ("sera", "lasera"))
    w = w[cut:]
    wr(os.path.join(W, "plain-PE.txt"), " ".join(w) + "\n")
    out = [f"PE plain: words {sum(x != '[...]' for x in w)}, holes {w.count('[...]')}, letters "
           f"{sum(len(x) for x in w if x != '[...]')}"]
    free, tiedf = os.path.join(HERE, "key-pe-free.tsv"), os.path.join(HERE, "key-pe-tied.tsv")
    a = subprocess.Popen([sys.executable, os.path.join(LINE, "align.py"), "build", os.path.join(W, "A-merged.txt"),
                          os.path.join(W, "plain-PE.txt"), "--out", free, "--abridged"], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, text=True)
    b = subprocess.Popen([sys.executable, os.path.join(HERE, "tied.py"), "build", os.path.join(W, "A-merged.txt"),
                          os.path.join(W, "plain-PE.txt"), tiedf], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sa, ea = a.communicate()
    sb, eb = b.communicate()
    out += ["free: " + (sa.strip().splitlines()[-1] if sa.strip() else ea[-300:]), "tied: " + (sb.strip() or eb[-300:])]
    rows = [r for r in align.read_key(free) if r["status"] in MARKED]
    out.append(f"free table marked rows\t{len(rows)}\tnull share {align.null_share(align.read_key(free)):.3f}")
    bm = [(r["unit"].split("+"), r["value"]) for r in rows if "+" in r["unit"] and r["unit"].split("+")[1] in tied.VMARKS]
    two = [(u, v) for u, v in bm if len(v) == 2]
    byv, byb = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    for (b_, m), v in two:
        byv[m][v[1]] += 1
        byb[b_][v[0]] += 1
    out.append(f"free rows for a base with a vowel mark\t{len(bm)}\ttwo-letter values\t{len(two)}")
    out.append(f"  of those, ending in their mark's commonest letter\t{sum(max(c.values()) for c in byv.values())}")
    out.append(f"  of those, beginning with their base's commonest letter\t{sum(max(c.values()) for c in byb.values())}")
    out.append("  marks: " + "; ".join(f"{m}: " + " ".join(f"{k}×{n}" for k, n in c.most_common()) for m, c in sorted(byv.items())))
    out.append("  value lengths of the marked sign rows: " + " ".join(f"{k}:{n}" for k, n in sorted(collections.Counter(len(v) for _, v in bm).items())))
    keep = len(rows) >= 30
    out.append(f"keep\t{keep}")
    if keep:
        align.write_key(rows, os.path.join(HERE, "key-v0.tsv"))
    wr(os.path.join(RES, "pe.tsv"), "\n".join(out) + "\n")
    print("\n".join(out))


def screen_decode(text, mk, bs, bare):
    out = []
    for ln in text.splitlines():
        if ln.startswith("#"):
            continue
        for t in ln.split():
            b, _, m = t.partition("+")
            if t in bare:
                out.append(bare[t])
            elif m and b in bs and m in mk:
                out.append(bs[b] + mk[m])
            elif not m and b in bs:
                out.append(bs[b])
            else:
                out.append("?")
    return out


def screen(cipher="A-merged.txt", tag="screen"):
    import random
    rows = list(csv.DictReader(open(os.path.join(HERE, "sources", "map-pandolfini.tsv")), delimiter="\t"))
    mk = {r["ours"]: r["value"] for r in rows if r["kind"] == "mark"}
    bs = {r["ours"]: r["value"] for r in rows if r["kind"] == "base"}
    bare = {r["ours"]: r["value"] for r in rows if r["kind"] == "bare"}
    text = rd(W, cipher)
    words = sorted({w for w in plain_words(rd(R, "PE", "p233.txt")) if len(w) >= 5 and w != "[...]"})

    def count(mk, bs, bare):
        s = "".join(screen_decode(text, mk, bs, bare))
        return sum(w in s for w in words), s
    true, dec = count(mk, bs, bare)
    rng, sh = random.Random(1), []
    for _ in range(200):
        a, b, c = list(mk.values()), list(bs.values()), list(bare.values())
        rng.shuffle(a)
        rng.shuffle(b)
        rng.shuffle(c)
        sh.append(count(dict(zip(mk, a)), dict(zip(bs, b)), dict(zip(bare, c)))[0])
    pieces = screen_decode(text, mk, bs, bare)
    out = [f"signs\t{len(pieces)}", f"valued\t{sum(p != '?' for p in pieces)}\t{sum(p != '?' for p in pieces) / len(pieces):.3f}",
           f"judge_words\t{len(words)}", f"found\t{true}", f"shuffles_below\t{sum(x < true for x in sh)} of 200",
           f"shuffle_mean\t{sum(sh) / len(sh):.2f}", f"shuffle_max\t{max(sh)}",
           f"pass\t{true > max(sh) and true >= 10}", "found_words\t" + " ".join(w for w in words if w in dec)]
    wr(os.path.join(RES, f"{tag}.tsv"), "\n".join(out) + "\n")
    wr(os.path.join(RES, f"{tag}-decode.txt"), "\n".join(dec[k:k + 110] for k in range(0, len(dec), 110)) + "\n")
    print("\n".join(out))
    print(dec[:700])


def marks():
    import collections
    toks = [t for ln in rd(W, "A-merged.txt").splitlines() if not ln.startswith("#") for t in ln.split() if t != "?"]
    mk, bs, bm = collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    for t in toks:
        b, _, m = t.partition("+")
        m = m or "-"
        mk[m] += 1
        bs[b] += 1
        bm[b][m] += 1
    out = [f"signs\t{len(toks)}", f"marked\t{sum(v for k, v in mk.items() if k != '-')}",
           "marks\t" + " ".join(f"{m}:{c}" for m, c in mk.most_common()), "base\ttotal\tby mark"]
    out += [f"{b}\t{n}\t" + " ".join(f"{m}:{c}" for m, c in bm[b].most_common()) for b, n in bs.most_common()]
    wr(os.path.join(RES, "marks.tsv"), "\n".join(out) + "\n")
    print("\n".join(out[:4]))


if __name__ == "__main__":
    {"prep": prep, "build": build, "tables": tables, "marks": marks, "screen": screen, "pe": pe, "forms": forms, "solve": solve_run, "solve-test": solve_test, "tied": tied_build, "tied-tables": tied_tables}[sys.argv[1]]()
