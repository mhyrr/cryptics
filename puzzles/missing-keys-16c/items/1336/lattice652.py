"""lattice652.py - F 46 inf. n. 275, c. 652r read from four readers at once with key-v2.tsv (README, "Sixth stage").

    python3 lattice652.py test     results/c652-test.tsv
    python3 lattice652.py read     results/c652-read.txt   (run only after the test)
As lattice.py, over seven lines. `[[clear]]` in a reader's row marks a stretch of clear words: a column where
half the readers or more have it ends a cipher run, and the letter model starts afresh after it.
"""
import math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "line"))
import align, merge  # noqa: E402
import lattice  # noqa: E402

R, RES = os.path.join(HERE, "readers"), os.path.join(HERE, "results")
READERS = ("J", "K", "L", "M")
CLR = "[[clear]]"
ANY, NONE, ALPHA, EPS = lattice.ANY, lattice.NONE, lattice.ALPHA, lattice.EPS


def rows(reader):
    return [ln.split() for ln in open(os.path.join(R, reader, "c652.txt"), encoding="utf-8").read().splitlines()
            if ln.strip() and not ln.startswith("#")]


def columns():
    """-> list of lines; a line is a list of columns {reader index: token}."""
    files = [rows(r) for r in READERS]
    if len({len(f) for f in files}) != 1:
        raise SystemExit(f"readers differ in rows: {[len(f) for f in files]}")
    return [merge.columns([f[k] for f in files], lattice.RENAME) for k in range(len(files[0]))]


def candidates(col, kmap):
    n = float(len(READERS))
    c = {}
    for r in range(len(READERS)):
        tok = col.get(r)
        if tok is None:
            c[NONE] = c.get(NONE, 0) + 1.0
        elif tok == CLR:
            c[CLR] = c.get(CLR, 0) + 1.0
        else:
            for s, w in lattice.votes(tok):
                v = kmap.get(s) if s else None
                c[v if v else ANY] = c.get(v if v else ANY, 0) + w
    return {k: v / n for k, v in c.items()}


def best(lines, kmap, lp):
    """-> (score, path). path: per line, per column: (candidate, emitted, share) or ('CLR', '', share)."""
    total, out = 0.0, []
    for cols in lines:
        states = {("^", "^"): (0.0, None)}
        for col in cols:
            cand = candidates(col, kmap)
            if cand.get(CLR, 0) >= 0.5:
                sc, hist = max(states.values(), key=lambda v: v[0])
                states = {("^", "^"): (sc, (hist, "CLR", "", cand[CLR]))}
                continue
            cand.pop(CLR, None)
            new = {}
            for (a, b), (sc, hist) in states.items():
                for k, share in cand.items():
                    base = sc + math.log(max(share, EPS))
                    for o in ([NONE] if k == NONE else list(ALPHA) if k == ANY else [k]):
                        x, y, add = a, b, 0.0
                        for ch in o:
                            if x != "^":
                                add += lp(x, y, ch)
                            x, y = y, ch
                        tot = base + add - (math.log(len(ALPHA)) if k == ANY else 0.0)
                        if (x, y) not in new or tot > new[(x, y)][0]:
                            new[(x, y)] = (tot, (hist, k, o, share))
            states = new
        sc, hist = max(states.values(), key=lambda v: v[0])
        path = []
        while hist is not None:
            path.append(hist[1:])
            hist = hist[0]
        path.reverse()
        out.append(path)
        total += sc
    return total, out


def table():
    return align.key_map(align.read_key(os.path.join(HERE, "key-v2.tsv")))


def test():
    lp, held, ntrain = lattice.model()
    lines, kmap = columns(), table()
    sc, path = best(lines, kmap, lp)
    shown = [k for ln in path for k, o, s in ln if k not in ("CLR", NONE)]
    rng, signs, vals, sh = random.Random(1), list(kmap), [kmap[k] for k in kmap], []
    for _ in range(200):
        v = vals[:]
        rng.shuffle(v)
        sh.append(best(lines, dict(zip(signs, v)), lp)[0])
    below = sum(x < sc for x in sh)
    out = [f"readers\t{' '.join(READERS)}", f"lines\t{len(lines)}", f"columns\t{sum(len(c) for c in lines)}",
           f"table_values\t{len(kmap)}", f"places with a supported letter\t{sum(k != ANY for k in shown)}",
           f"places open\t{sum(k == ANY for k in shown)}", f"true_score\t{sc:.2f}",
           f"shuffles_below_true\t{below} of 200", f"shuffle_score_mean\t{sum(sh) / len(sh):.2f}",
           f"shuffle_score_max\t{max(sh):.2f}", f"pass\t{below >= 190}"]
    open(os.path.join(RES, "c652-test.tsv"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


def read():
    lp, held, ntrain = lattice.model()
    lines, kmap = columns(), table()
    sc, path = best(lines, kmap, lp)
    out = []
    for n, (cols, p) in enumerate(zip(lines, path), 1):
        sup, full, votes4 = [], [], []
        for k, o, share in p:
            if k == "CLR":
                sup.append(" | ")
                full.append(" | ")
                votes4.append(" | ")
            elif k == NONE:
                continue
            else:
                s = "?" if k == ANY else o
                sup.append(s)
                full.append(o.upper() if k == ANY else o)
                votes4.append(s if share >= 0.99 else "." * len(s))
        out += [f"row {n}", "  supported:  " + "".join(sup), "  with fill:  " + "".join(full),
                "  all four:   " + "".join(votes4)]
        out += ["  " + " ".join(f"{'/'.join((col.get(r) or '-') for r in range(len(READERS)))}" for col in cols)]
    out += ["", "supported: letters some reader's sign has a value for; ? = none. with fill: the letter model's",
            "guess at ? in capitals (not evidence). all four: letters every reader's sign supports. | = clear words."]
    open(os.path.join(RES, "c652-read.txt"), "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    {"test": test, "read": read}[sys.argv[1]]()
