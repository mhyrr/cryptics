"""Cross-check geom.py against a brute force that shares none of its reasoning.

The brute force takes every geometry (w, s1, s2, e1, e2, dr) in a small space and every distinct
long/short pattern a key can give (all orderings of the multiset of column types), builds the column
starts directly, and counts runs that sit in the same rank in both telegrams with row offset dr (or,
with bottoms, equal distance from the bottom when L1 = L2 mod w). The fast search must give the same
best count. Small telegram lengths (N1, N2) keep the brute force cheap.
Usage (from this folder): python3 -I verify.py > verify.txt
"""
import itertools, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geom


def patterns(w, x1, x2):
    lo, hi = min(x1, x2), max(x1, x2)
    ty = ["B"] * lo + ["O"] * (hi - lo) + ["N"] * (w - hi)
    for p in sorted(set(itertools.permutations(ty))):
        l1 = [1 if t == "B" or (t == "O" and x1 > x2) else 0 for t in p]
        l2 = [1 if t == "B" or (t == "O" and x2 > x1) else 0 for t in p]
        yield l1, l2


def brute(runs, N1, N2, W, S, E, DR, bottoms, geoms=None):
    best = 0
    for w in range(W[0], W[1] + 1):
        for s1, e1, s2, e2 in itertools.product(range(S[0], S[1] + 1), range(E[0], E[1] + 1),
                                                range(S[0], S[1] + 1), range(E[0], E[1] + 1)):
            L1, L2 = N1 - s1 - e1, N2 - s2 - e2
            h1, x1 = divmod(L1, w); h2, x2 = divmod(L2, w)
            for l1, l2 in patterns(w, x1, x2):
                st1, st2, len1, len2 = [], [], [], []
                p1, p2 = s1, s2
                for k in range(w):
                    st1.append(p1); st2.append(p2)
                    len1.append(h1 + l1[k]); len2.append(h2 + l2[k])
                    p1 += h1 + l1[k]; p2 += h2 + l2[k]
                for dr in range(DR[0], DR[1] + 1):
                    c = 0
                    for a, b, L in runs:
                        for k in range(w):
                            if st2[k] <= b < st2[k] + len2[k]:
                                break
                        else:
                            continue
                        r, rho = b - st2[k], a - st1[k]
                        if not (b + L <= st2[k] + len2[k] and 0 <= rho and rho + L <= len1[k]):
                            continue
                        if rho - r == dr:
                            c += 1
                        elif bottoms and x1 == x2 and len1[k] - L - rho == len2[k] - L - r:
                            c += 1
                    if geoms is not None and c > 0:
                        geoms.setdefault(c, set()).add((w, s1, s2, e1, e2, dr))
                    best = max(best, c)
    return best


def planted(rnd, N1, N2, W, S, E, DR, nrun, bottoms):
    """Runs placed on one random geometry (so high counts get tested), plus random runs."""
    w = rnd.randint(*W); s1, e1, s2, e2 = (rnd.randint(*S), rnd.randint(*E), rnd.randint(*S), rnd.randint(*E))
    L1, L2 = N1 - s1 - e1, N2 - s2 - e2
    h1, x1 = divmod(L1, w); h2, x2 = divmod(L2, w)
    l1, l2 = next(iter(patterns(w, x1, x2))) if rnd.random() < 0.3 else \
        rnd.choice(list(patterns(w, x1, x2)))
    st1 = [s1 + k * h1 + sum(l1[:k]) for k in range(w)]
    st2 = [s2 + k * h2 + sum(l2[:k]) for k in range(w)]
    dr = rnd.randint(*DR)
    runs = []
    for _ in range(nrun):
        L = rnd.randint(2, 3)
        k = rnd.randrange(w)
        c1, c2 = h1 + l1[k], h2 + l2[k]
        use_bottom = bottoms and x1 == x2 and rnd.random() < 0.5
        if use_bottom:
            u = rnd.randint(0, max(0, min(c1, c2) - L))
            a, b = st1[k] + c1 - L - u, st2[k] + c2 - L - u
        else:
            rs = [r for r in range(0, c2 - L + 1) if 0 <= r + dr <= c1 - L]
            if not rs:
                continue
            r = rnd.choice(rs); a, b = st1[k] + r + dr, st2[k] + r
        runs.append((a, b, L))
    for _ in range(rnd.randint(0, 3)):
        L = rnd.randint(2, 3)
        runs.append((rnd.randint(0, N1 - L), rnd.randint(0, N2 - L), L))
    return runs


def check_ranges():
    """d1_range and seg_range against all step sequences of length <= 6."""
    steps = {1: {"B": (1, 1), "O": (1, 0), "N": (0, 0)}, 2: {"B": (1, 1), "O": (0, 1), "N": (0, 0)},
             0: {"B": (1, 1), "N": (0, 0)}}
    for mode, st in steps.items():
        for dk in range(1, 7):
            reach = {}
            for seq in itertools.product(st, repeat=dk):
                d1 = sum(st[t][0] for t in seq); d2 = sum(st[t][1] for t in seq)
                reach.setdefault(None, set()).add((d1, d2))
                reach.setdefault(seq[0], set()).add((d1, d2))
            for t in (None,) + tuple(st):
                got = set()
                for d2 in range(-2, dk + 3):
                    r = geom.d1_range(mode, dk, d2, t)
                    if r:
                        got |= {(d1, d2) for d1 in range(r[0], r[1] + 1)}
                assert got == reach.get(t, set()), (mode, dk, t)
                got2 = set()
                for dd in range(-dk - 2, dk + 3):
                    r = geom.seg_range(mode, dk, dd, t)
                    if r:
                        got2 |= {(dd + d2, d2) for d2 in range(r[0], r[1] + 1)}
                assert got2 == reach.get(t, set()), ("seg", mode, dk, t)
    print("d1_range and seg_range match all step sequences (dk 1-6, three modes)")


def main():
    check_ranges()
    rnd = random.Random(16)
    for cfg in [(61, 29, (3, 6), (0, 2), (0, 2), (-2, 2), 160), (70, 24, (4, 7), (0, 1), (0, 2), (-3, 3), 80)]:
        run_cfg(rnd, *cfg)
    full_scale()


def full_scale():
    """At the real lengths and full ranges, the pruned search must equal the unpruned exact DP."""
    import fit
    geom.N1, geom.N2 = 615, 160
    for bottoms in (False, True):
        a = geom.search(fit.OBS, bottoms=bottoms, collect=True)
        b = geom.search(fit.OBS, bottoms=bottoms, collect=True, nobound=True)
        same = a[0] == b[0] and {h[:5] for h in a[1]} == {h[:5] for h in b[1]}
        print(f"full scale, observed runs, bottoms={bottoms}: pruned best {a[0]}, unpruned best {b[0]}; "
              f"passes reaching it identical: {same} ({len(a[1])})")
    agree = 0
    for rep in range(100):
        runs = random_null_i(rep)
        for bottoms in (False, True):
            agree += geom.search(runs, bottoms=bottoms)[0] == geom.search(runs, bottoms=bottoms, nobound=True)[0]
    print(f"full scale, 100 null (i) sets x 2 variants: pruned = unpruned best count in {agree}/200")
    agree = 0
    for rep in (0, 31, 62, 93, 124, 155):
        g, c1, c2 = fit.make_plant(rep)
        runs = fit.shared_runs(c1, c2)
        agree += geom.search(runs)[0] == geom.search(runs, nobound=True)[0]
    print(f"full scale, 6 K3 plants (w 5, 10, 15, 20, 25, 30): pruned = unpruned best count in {agree}/6")


def random_null_i(rep):
    import fit
    rnd = random.Random(rep)
    runs, u1, u2 = [], set(), set()
    for L in [4, 6, 4, 4, 4, 4, 4]:
        while True:
            a, b = rnd.randrange(615 - L + 1), rnd.randrange(160 - L + 1)
            s1, s2 = set(range(a, a + L)), set(range(b, b + L))
            if not (s1 & u1) and not (s2 & u2):
                break
        runs.append((a, b, L)); u1 |= s1; u2 |= s2
    return runs


def run_cfg(rnd, N1, N2, W, S, E, DR, ntrial):
    geom.N1, geom.N2 = N1, N2
    agree = 0; total = 0; dist = {}; gagree = 0; gtotal = 0
    for trial in range(ntrial):
        bottoms = trial % 2 == 1
        if trial % 4 < 2:
            runs = planted(rnd, N1, N2, W, S, E, DR, rnd.randint(2, 6), bottoms)
        else:
            runs = [(rnd.randint(0, N1 - 3), rnd.randint(0, N2 - 3), rnd.randint(2, 3)) for _ in range(rnd.randint(2, 7))]
        gb = {}
        bf = brute(runs, N1, N2, W, S, E, DR, bottoms, gb)
        fast, hits = geom.search(runs, W=W, S1=S, S2=S, E1=E, E2=E, DR=DR, bottoms=bottoms, collect=True)
        total += 1; agree += bf == fast; dist[bf] = dist.get(bf, 0) + 1
        if bf != fast:
            print("MISMATCH", trial, bottoms, runs, "brute", bf, "fast", fast)
        if bf > 0:
            gf = set()
            for h in hits:
                gf |= geom.geometries(runs, h, fast, S1=S, S2=S, E1=E, E2=E)
            gtotal += 1; gagree += gf == gb[bf]
            if gf != gb[bf]:
                print("GEOMETRY MISMATCH", trial, runs, len(gf), len(gb[bf]), sorted(gf ^ gb[bf])[:5])
    print(f"N1={N1} N2={N2} w {W} s {S} e {E} dr {DR}: best count, fast vs brute force: {agree}/{total} agree; "
          f"brute-force best counts {dict(sorted(dist.items()))}")
    print(f"    set of geometries reaching the best (top and bottoms trials): {gagree}/{gtotal} identical")


if __name__ == "__main__":
    main()
