"""lattice.py - the bare line on F 131 inf. c. 14r read from four readers at once (README, "Fourth test").

    python3 lattice.py test     results/lattice-test.tsv
    python3 lattice.py read     results/lattice-read.txt   (run only after the test)
Columns: readers F, A, B lined up on reader E's row. Each column holds the readers' votes. The best path
through the columns is found by log vote share plus letter-trigram log probability. The letter model may
choose only among candidates some reader supports; an unread or unvalued vote is "any one letter" and prints
as '?'. Control: the same with the table's values shuffled among its signs.
"""
import difflib, math, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align  # noqa: E402

R, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "results")
CORPUS = os.path.join(HERE, "..", "2911", "print", "leoperediniccol03milagoog_djvu.txt")
RENAME = {"n-a": "a", "n-slong": "slong", "n-ess": "slong"}     # earlier readers' names for listed signs
ANY, NONE = "*", ""
ALPHA = "abcdefghilmnopqrstuz"
K = 0.1
EPS = 0.02                                                     # floor on a candidate's vote share


def votes(tok):
    """-> [(sign or None for unread, weight)] for one token."""
    if tok == "?":
        return [(None, 1.0)]
    if "|" in tok:
        parts = [p.rstrip("?") for p in tok.split("|")]
        return [(RENAME.get(p, p) or None, 1.0 / len(parts)) for p in parts]
    if tok.endswith("?"):
        s = tok[:-1]
        return [(RENAME.get(s, s), 0.7), (None, 0.3)]
    return [(RENAME.get(tok, tok), 1.0)]


def row(reader):
    t = open(os.path.join(R, reader, "c14.txt"), encoding="utf-8").read()
    return [x for ln in t.splitlines() if not ln.startswith("#") for x in ln.split()]


def first(tok):
    return votes(tok)[0][0] or "?"


def columns(readers=("E", "F", "A", "B"), rows=None):
    """-> list of columns; a column is {reader: token}. Reader 0 is the frame; a stretch another reader has
    and the frame lacks becomes columns of its own."""
    rows = rows or {r: row(r) for r in readers}
    cols = [{readers[0]: t} for t in rows[readers[0]]]
    for rd in readers[1:]:
        idx = [i for i, c in enumerate(cols) if readers[0] in c]
        a = [first(cols[i][readers[0]]) for i in idx]
        toks = rows[rd]
        b = [first(t) for t in toks]
        extra = []                                   # (insert before cols index, token)
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            n = min(i2 - i1, j2 - j1) if op in ("equal", "replace") else 0
            for k in range(n):
                cols[idx[i1 + k]][rd] = toks[j1 + k]
            at = idx[i1 + n] if i1 + n < len(idx) else len(cols)
            extra += [(at, t) for t in toks[j1 + n:j2]]
        for at, t in sorted(extra, key=lambda e: -e[0]):
            # another reader's lone column just before this place takes it, if this reader has no vote there
            if at > 0 and readers[0] not in cols[at - 1] and rd not in cols[at - 1]:
                cols[at - 1][rd] = t
            else:
                cols.insert(at, {rd: t})
    return cols, readers


def candidates(col, readers, kmap):
    """-> {candidate: share}. candidate: a value string, ANY, or NONE."""
    c = {}
    for rd in readers:
        tok = col.get(rd)
        if tok is None:
            c[NONE] = c.get(NONE, 0) + 1.0
            continue
        for s, w in votes(tok):
            v = kmap.get(s) if s else None
            key = v if v else ANY
            c[key] = c.get(key, 0) + w
    n = float(len(readers))
    return {k: v / n for k, v in c.items()}


def letters_of(path):
    return open(path, encoding="utf-8", errors="replace").read()


def model():
    words = [align.norm_letters(w) for w in re.split(r"[^A-Za-zàèéìòùÀÈÉÌÒÙ]+", letters_of(CORPUS))]
    text = "".join(w for w in words if w and all(ch in ALPHA for ch in w))
    cut = int(len(text) * 0.9)
    train, held = text[:cut], text[cut:]
    tri, bi = {}, {}
    for i in range(len(train) - 2):
        tri[train[i:i + 3]] = tri.get(train[i:i + 3], 0) + 1
        bi[train[i:i + 2]] = bi.get(train[i:i + 2], 0) + 1
    V = len(ALPHA)

    def lp(a, b, c):
        return math.log((tri.get(a + b + c, 0) + K) / (bi.get(a + b, 0) + K * V))
    return lp, held, len(train)


def best(cols, readers, kmap, lp):
    """-> (score, lm score, letters emitted, path). path: [(candidate, emitted, share)] per column."""
    states = {("^", "^"): (0.0, 0.0, None)}          # (last two letters) -> (score, lm, history)
    for col in cols:
        cand = candidates(col, readers, kmap)
        new = {}
        for (a, b), (sc, lm, hist) in states.items():
            for k, share in cand.items():
                base = sc + math.log(max(share, EPS))
                outs = [NONE] if k == NONE else list(ALPHA) if k == ANY else [k]
                for o in outs:
                    x, y, l2 = a, b, lm
                    for ch in o:
                        if x != "^":
                            l2 += lp(x, y, ch)
                        x, y = y, ch
                    tot = base + (l2 - lm) - (math.log(len(ALPHA)) if k == ANY else 0.0)
                    st = (x, y)
                    if st not in new or tot > new[st][0]:
                        new[st] = (tot, l2, (hist, k, o, share))
        states = new
    sc, lm, hist = max(states.values(), key=lambda v: v[0])
    path = []
    while hist is not None:
        path.append(hist[1:])
        hist = hist[0]
    path.reverse()
    return sc, lm, sum(len(o) for _, o, _ in path), path


def table():
    p = os.path.join(HERE, "key-v1.tsv")
    return align.key_map(align.read_key(p))


def test():
    lp, held, ntrain = model()
    cols, readers = columns()
    kmap = table()
    sc, lm, n, path = best(cols, readers, kmap, lp)
    rng, signs, vals = random.Random(1), list(kmap), [kmap[k] for k in kmap]
    sh, shlm = [], []
    for _ in range(200):
        v = vals[:]
        rng.shuffle(v)
        s2, l2, n2, _ = best(cols, readers, dict(zip(signs, v)), lp)
        sh.append(s2)
        shlm.append(l2 / max(1, n2 - 2))
    below = sum(1 for x in sh if x < sc)
    win = []
    for i in range(0, len(held) - n, n):
        w = held[i:i + n]
        win.append(sum(lp(w[j], w[j + 1], w[j + 2]) for j in range(n - 2)) / (n - 2))
    win.sort()
    per = lm / max(1, n - 2)
    out = [f"columns\t{len(cols)}", f"readers\t{' '.join(readers)}", f"table_values\t{len(kmap)}",
           f"train_letters\t{ntrain}", f"path_letters\t{n}", f"true_score\t{sc:.2f}",
           f"shuffles_below_true\t{below} of 200", f"shuffle_score_mean\t{sum(sh) / len(sh):.2f}",
           f"shuffle_score_max\t{max(sh):.2f}", f"pass\t{below >= 190}",
           f"true_lm_per_letter\t{per:.3f}", f"shuffle_lm_per_letter_mean\t{sum(shlm) / len(shlm):.3f}",
           f"shuffle_lm_per_letter_max\t{max(shlm):.3f}",
           f"heldout_italian_windows\t{len(win)}",
           f"heldout_lm_per_letter_p05_p50_p95\t{win[len(win) // 20]:.3f} {win[len(win) // 2]:.3f} "
           f"{win[19 * len(win) // 20]:.3f}",
           f"heldout_windows_below_true\t{sum(1 for x in win if x < per) / len(win):.3f}"]
    open(os.path.join(RES, "lattice-test.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def read():
    lp, held, ntrain = model()
    cols, readers = columns()
    kmap = table()
    sc, lm, n, path = best(cols, readers, kmap, lp)
    out = ["col\t" + "\t".join(readers) + "\tcandidates\tchosen\tshare"]
    line, fill = [], []
    for i, (col, (k, o, share)) in enumerate(zip(cols, path), 1):
        cand = candidates(col, readers, kmap)
        cs = " ".join(f"{'none' if c == NONE else 'any' if c == ANY else c}:{w:.2f}"
                      for c, w in sorted(cand.items(), key=lambda e: -e[1]))
        shown = "" if k == NONE else "?" if k == ANY else o
        out.append(f"{i}\t" + "\t".join(col.get(r) or "-" for r in readers) + f"\t{cs}\t{shown or '(none)'}\t{share:.2f}")
        line.append(shown)
        fill.append(o.upper() if k == ANY else o)
    out += ["", "supported letters ('?' = no reader's sign has a value there):", "".join(line),
            "with the letter model's fill in capitals (not evidence):", "".join(fill),
            "letters chosen with all four votes: " + "".join(s if sh >= 0.99 else "." * max(1, len(s))
                                                              for s, (k, o, sh) in zip(line, path) if s)]
    open(os.path.join(RES, "lattice-read.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def selftest():
    """Planted lines: 20 windows of held-out Italian and 20 of random letters, each enciphered with the real
    table's signs, then read by four noisy readers (15% of signs wrong, 8% unread, 3% dropped, 25% of the
    table's signs treated as unvalued). Reports how often the test passes (50 shuffles, bar 48) and the share
    of supported letters that are right."""
    lp, held, _ = model()
    kmap = table()
    rng = random.Random(7)
    by = {}
    for s_, v in kmap.items():
        by.setdefault(v, []).append(s_)
    signs = list(kmap)
    out = ["kind\tpassed_of_20\tsupported_letters_right"]
    for kind in ("italian", "random"):
        passed = right = total = 0
        for t in range(20):
            if kind == "italian":
                i = rng.randrange(len(held) - 40)
                plain = "".join(ch for ch in held[i:i + 40] if ch in by)[:36]
            else:
                plain = "".join(rng.choice(list(by)) for _ in range(36))
            true = [rng.choice(by[ch]) for ch in plain]
            hidden = set(rng.sample(signs, len(signs) // 4))
            km = {k: v for k, v in kmap.items() if k not in hidden}
            rows = {}
            for rd in "EFAB":
                r_ = []
                for s_ in true:
                    x = rng.random()
                    if x < 0.03:
                        continue
                    r_.append("?" if x < 0.11 else rng.choice(signs) if x < 0.26 else s_)
                rows[rd] = r_
            cols, readers = columns(rows=rows)
            sc, lm, n, path = best(cols, readers, km, lp)
            ks, vs, below = list(km), [km[k] for k in km], 0
            for _ in range(50):
                v = vs[:]
                rng.shuffle(v)
                below += best(cols, readers, dict(zip(ks, v)), lp)[0] < sc
            passed += below >= 48
            got = "".join("?" if k == ANY else o for k, o, _ in path)
            sm = difflib.SequenceMatcher(None, got, plain, autojunk=False)
            total += sum(1 for ch in got if ch != "?")
            right += sum(b_.size for b_ in sm.get_matching_blocks())
        out.append(f"{kind}\t{passed}\t{right}/{total}")
    open(os.path.join(RES, "lattice-selftest.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    {"test": test, "read": read, "selftest": selftest}[sys.argv[1]]()
