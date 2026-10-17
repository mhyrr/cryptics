"""Experiment 16: do the shared runs of T1 and T2 fit one single-columnar geometry (K3)?

G1  fit the seven observed runs: best count over w 5-60, s1 s2 e1 e2 0-20, dr -10..10, every
    geometry reaching it; then the same with shared-closing (bottom) runs allowed.
G2  nulls: (i) 10,000 sets of 7 random run pairs (observed lengths, uniform, no overlaps);
    (ii) shared-run sets of 2,000 independent shuffle pairs of the telegrams, kept if >= 5 runs.
G3  K3 plants: Spanish telegraph plaintext, one random key, w 5-30 (stratified), a shared phrase of
    4-8 rows at the same plaintext offset mod w (row offset q in -10..10), 0-20 untransposed letters
    at each end; runs extracted as in 02; recovery of the true w (and trims within +-1).
Usage (from this folder): python3 -I fit.py [--workers 7] > result.txt
Per-replicate rows are cached in out/*.json (gitignored); delete them to recompute.
"""
import itertools, json, os, random, sys, time
from collections import Counter
from multiprocessing import Pool

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import geom
SOLVER = os.path.join(here, "..", "01-solver")
OUT = os.path.join(here, "out")
SEED = 20261016


def load(p):
    return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())


T1, T2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
OBS_LIST = [("NOCU", 0, 17), ("APMOEP", 5, 263), ("OEPM", 8, 42), ("LNDN", 38, 569),
            ("TRSP", 87, 274), ("RAEA", 128, 164), ("ISEE", 138, 464)]


def shared_runs(x, y, n=4):
    """Maximal forward runs of >= n letters shared by x and y: [(pos in x, pos in y, length)].
    Same as 13's 'fwd' runs (n-gram matches merged when they overlap on one diagonal)."""
    idx = {}
    for i in range(len(x) - n + 1):
        idx.setdefault(x[i:i + n], []).append(i)
    out = []
    for j in range(len(y) - n + 1):
        for i in idx.get(y[j:j + n], ()):
            if i > 0 and j > 0 and x[i - 1] == y[j - 1]:
                continue
            L = n
            while i + L < len(x) and j + L < len(y) and x[i + L] == y[j + L]:
                L += 1
            out.append((i, j, L))
    return sorted(out, key=lambda r: (r[1], r[0]))


def name(runs, idxs):
    return "+".join(T2[runs[i][1]:runs[i][1] + runs[i][2]] for i in idxs)


# ------------------------------------------------------------------ workers
def gen_null_i(rep):
    rnd = random.Random(SEED * 10 + 1_000_000 + rep)
    lens = [L for _, _, L in OBS]
    runs, u1, u2 = [], set(), set()
    for L in lens:
        while True:
            a, b = rnd.randrange(geom.N1 - L + 1), rnd.randrange(geom.N2 - L + 1)
            s1, s2 = set(range(a, a + L)), set(range(b, b + L))
            if not (s1 & u1) and not (s2 & u2):
                break
        runs.append((a, b, L)); u1 |= s1; u2 |= s2
    runs.sort(key=lambda r: (r[1], r[0]))
    return runs


def job_null_i(rep):
    runs = gen_null_i(rep)
    return [rep, len(runs), geom.search(runs)[0], geom.search(runs, bottoms=True)[0]]


WIDE = (-125, 125)   # every row offset: h1 <= 615 // 5 = 123


def job_null_i_wide(rep):
    return [rep, geom.search(gen_null_i(rep), DR=WIDE)[0]]


def job_null_ii(rep):
    rnd = random.Random(SEED * 10 + 2_000_000 + rep)
    a, b = list(T1), list(T2)
    rnd.shuffle(a); rnd.shuffle(b)
    runs = shared_runs("".join(a), "".join(b))
    if len(runs) < 5:
        return [rep, len(runs), None, None]
    return [rep, len(runs), geom.search(runs)[0], geom.search(runs, bottoms=True)[0]]


_PT = None


def _plaintext():
    global _PT
    if _PT is None:
        sys.path.insert(0, SOLVER)
        cwd = os.getcwd(); os.chdir(SOLVER)
        import plaintext, transpo
        plaintext.heldout_words("es")
        os.chdir(cwd)
        _PT = (plaintext, transpo)
    return _PT


def make_plant(rep):
    plaintext, transpo = _plaintext()
    rnd = random.Random(SEED * 10 + 3_000_000 + rep)
    w = 5 + rep % 26
    s1, e1, s2, e2 = (rnd.randint(0, 20) for _ in range(4))
    L1, L2 = geom.N1 - s1 - e1, geom.N2 - s2 - e2
    R = rnd.randint(4, min(8, L2 // w))
    M = R * w
    o2 = rnd.randint(0, L2 - M)
    qs = [q for q in range(-10, 11) if 0 <= o2 + q * w <= L1 - M]
    q = rnd.choice(qs); o1 = o2 + q * w
    p2 = plaintext.telegram(L2, rnd)
    phrase = p2[o2:o2 + M]
    p1 = plaintext.telegram(L1, rnd)
    p1 = p1[:o1] + phrase + p1[o1 + M:]
    key = rnd.sample(range(w), w)
    fill = list(plaintext.telegram(s1 + e1 + s2 + e2 + 1, rnd)); rnd.shuffle(fill)
    fill = "".join(fill)
    c1 = fill[:s1] + transpo.col_enc(p1, key) + fill[s1:s1 + e1]
    c2 = fill[s1 + e1:s1 + e1 + s2] + transpo.col_enc(p2, key) + fill[s1 + e1 + s2:s1 + e1 + s2 + e2]
    assert len(c1) == geom.N1 and len(c2) == geom.N2
    return dict(rep=rep, w=w, s1=s1, e1=e1, s2=s2, e2=e2, R=R, q=q, o1=o1, o2=o2), c1, c2


def job_plant(rep):
    t0 = time.process_time()
    g, c1, c2 = make_plant(rep)
    runs = shared_runs(c1, c2)
    g["n_runs"] = len(runs)
    best, hits = geom.search(runs, collect=True)
    wset = sorted({h[0] for h in hits})
    box = lambda v: (max(0, v - 1), min(20, v + 1))
    near, _ = geom.search(runs, W=(g["w"], g["w"]), S1=box(g["s1"]), S2=box(g["s2"]),
                          E1=box(g["e1"]), E2=box(g["e2"]))
    exact, _ = geom.search(runs, W=(g["w"], g["w"]), S1=(g["s1"],) * 2, S2=(g["s2"],) * 2,
                           E1=(g["e1"],) * 2, E2=(g["e2"],) * 2, DR=(g["q"], g["q"]))
    g.update(best=best, w_best=wset, true_w=g["w"] in wset, near=near == best, unique_w=wset == [g["w"]],
             n_true_geom=exact, cpu=round(time.process_time() - t0, 3))
    return g


# ------------------------------------------------------------------ helpers
def cached(path, fn, reps, workers):
    path = os.path.join(OUT, path)
    rows = json.load(open(path)) if os.path.exists(path) else []
    done = len(rows)
    if done < reps:
        with Pool(workers) as pool:
            rows += pool.map(fn, range(done, reps), chunksize=20)
        os.makedirs(OUT, exist_ok=True)
        json.dump(rows, open(path, "w"))
    return rows[:reps]


def pct(vals, q):
    s = sorted(vals)
    return s[min(len(s) - 1, int(q * len(s)))] if s else None


def describe(vals):
    c = Counter(vals)
    return ", ".join(f"{k}: {c[k]}" for k in sorted(c))


def main():
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 7
    cpu0 = time.process_time(); wall0 = time.time()
    print(f"T1 {len(T1)} letters, T2 {len(T2)} letters. Positions 0-based. Seed {SEED}.")
    print("Search space: w 5-60, s1 s2 e1 e2 0-20, dr -10..10, single columnar forward, one key.\n")

    # ---------------------------------------------------------- G1
    print("== G1 observed runs")
    for nm, b, a in OBS_LIST:
        print(f"  {nm:7} T2 {b:3}  T1 {a:3}  diagonal T1-T2 {a - b}")
    for bottoms in (False, True):
        label = "top only (shared phrase, one row offset dr)" if not bottoms else \
            "top or bottom (shared closing allowed: equal distance from the column bottom, L1 = L2 mod w)"
        best, hits = geom.search(OBS, bottoms=bottoms, collect=True)
        per_hit = [geom.geometries(OBS, h, best) for h in hits]
        geo = set().union(*per_hit) if per_hit else set()
        print(f"\n-- {label}")
        print(f"best count: {best}")
        print(f"passes (w, h1, h2, mode, dr) reaching it: {len(hits)}; distinct geometries (w, s1, s2, e1, e2, dr): {len(geo)}")
        # every subset of size `best` that reaches it on its own, with its geometries (exhaustive)
        allsub = set()
        for sub in itertools.combinations(range(len(OBS)), best):
            rs = [OBS[i] for i in sub]
            b2, h2s = geom.search(rs, bottoms=bottoms, collect=True)
            if b2 < best:
                continue
            gs = set().union(*[geom.geometries(rs, h, best) for h in h2s])
            allsub |= gs
            ws = Counter(g[0] for g in gs); drs = sorted({g[5] for g in gs})
            print(f"  subset {name(OBS, sub)}: {len(gs)} geometries; w: "
                  f"{', '.join(f'{w} ({n})' for w, n in sorted(ws.items()))}; dr {drs[0]}..{drs[-1]}")
        assert allsub == geo, "subset geometries differ from full-set geometries"
        print("  by w (all best geometries): " + ", ".join(f"{w}: {n}" for w, n in sorted(Counter(g[0] for g in geo).items())))
        tag = "bottoms" if bottoms else "top"
        with open(os.path.join(OUT, f"g1_geometries_{tag}.txt"), "w") as f:
            f.write("w s1 s2 e1 e2 dr\n")
            for g in sorted(geo):
                f.write(" ".join(map(str, g)) + "\n")
        dist = sorted(geo)
        print("  examples: " + "; ".join(f"w {g[0]} s1 {g[1]} s2 {g[2]} e1 {g[3]} e2 {g[4]} dr {g[5]}" for g in dist[:3]))
        if bottoms is False:
            obs_top = best
        else:
            obs_bot = best

    print("\n-- added after the pre-registered run (not pre-registered): every row offset, dr -125..125, top only")
    best_w, hits_w = geom.search(OBS, DR=WIDE, collect=True)
    fits = [name(OBS, s) for s in itertools.combinations(range(len(OBS)), best_w)
            if geom.search([OBS[i] for i in s], DR=WIDE)[0] >= best_w]
    print(f"best count: {best_w}; passes reaching it: {len(hits_w)}; w: {sorted({h[0] for h in hits_w})}")
    print(f"  subsets of size {best_w} that fit on their own (exhaustive): {', '.join(fits)}")

    # ---------------------------------------------------------- G2
    print("\n== G2 nulls (p = share of null sets with best count >= observed)")
    ri = cached("null_i.json", job_null_i, 10000, workers)
    for col, obs, lab in ((2, obs_top, "top only"), (3, obs_bot, "top or bottom")):
        v = [r[col] for r in ri]
        p = sum(x >= obs for x in v) / len(v)
        print(f"(i) random run pairs, {len(v)} sets, {lab}: best-count distribution {{{describe(v)}}}; "
              f"95th pct {pct(v, .95)}, 99th pct {pct(v, .99)}; observed {obs}; p = {p:.4f}")
    rw = cached("null_i_wide.json", job_null_i_wide, 10000, workers)
    v = [r[1] for r in rw]
    print(f"(i) same sets, dr -125..125 (not pre-registered): {{{describe(v)}}}; 95th pct {pct(v, .95)}, "
          f"99th pct {pct(v, .99)}; observed {best_w}; p = {sum(x >= best_w for x in v) / len(v):.4f}")
    rii = cached("null_ii.json", job_null_ii, 2000, workers)
    kept = [r for r in rii if r[2] is not None]
    print(f"(ii) shuffle pairs: {len(rii)} drawn; run counts {{{describe([r[1] for r in rii])}}}; "
          f"kept (>= 5 runs): {len(kept)}")
    for col, obs, lab in ((2, obs_top, "top only"), (3, obs_bot, "top or bottom")):
        v = [r[col] for r in kept]
        if v:
            p = sum(x >= obs for x in v) / len(v)
            print(f"(ii) {lab}: best-count distribution {{{describe(v)}}}; 95th pct {pct(v, .95)}, "
                  f"99th pct {pct(v, .99)}; observed {obs}; p = {p:.4f}")
    v7 = [r[2] for r in kept if r[1] == 7]
    if v7:
        print(f"(ii) top only, replicates with exactly 7 runs ({len(v7)}): {{{describe(v7)}}}")

    # ---------------------------------------------------------- G3
    print("\n== G3 K3 plants (w 5-30, 20 per w; phrase 4-8 rows; 0-20 untransposed letters each end)")
    rows = cached("plants.json", job_plant, 520, workers)
    n = len(rows)
    tw = sum(r["true_w"] for r in rows); nr = sum(r["near"] for r in rows); un = sum(r["unique_w"] for r in rows)
    print(f"plants: {n}")
    print(f"best geometry includes the true w: {tw}/{n} = {tw / n:.3f}")
    print(f"best geometry includes the true w with s1 s2 e1 e2 each within +-1: {nr}/{n} = {nr / n:.3f}")
    print(f"true w is the only w reaching the best count: {un}/{n} = {un / n:.3f}")
    ties = [r for r in rows if r["true_w"] and not r["unique_w"]]
    mult = sum(all(w % r["w"] == 0 for w in r["w_best"]) for r in ties)
    near = sum(any(abs(w - r["w"]) == 1 for w in r["w_best"]) for r in ties)
    print(f"  of the {len(ties)} ties: every other w a multiple of the true w in {mult}; "
          f"some w within 1 of the true w in {near}")
    print(f"planted best-count distribution: {{{describe([r['best'] for r in rows])}}}")
    print(f"runs consistent with the exact true geometry, minus best count: {{{describe([r['n_true_geom'] - r['best'] for r in rows])}}}")
    print("\nby w: runs (median, min-max) | best count (median) | true w | true w and trims +-1 | unique w")
    for w in range(5, 31):
        rs = [r for r in rows if r["w"] == w]
        nrun = sorted(r["n_runs"] for r in rs); bc = sorted(r["best"] for r in rs)
        print(f"  w {w:2}: runs {nrun[len(nrun) // 2]:3} ({nrun[0]}-{nrun[-1]}) | best {bc[len(bc) // 2]:3} | "
              f"{sum(r['true_w'] for r in rs):2}/{len(rs)} | {sum(r['near'] for r in rs):2}/{len(rs)} | "
              f"{sum(r['unique_w'] for r in rs):2}/{len(rs)}")
    allruns = [r["n_runs"] for r in rows]
    print(f"\nplant run counts overall: median {sorted(allruns)[n // 2]}; share with <= 7 runs "
          f"{sum(x <= 7 for x in allruns) / n:.3f}; share with >= 14 runs {sum(x >= 14 for x in allruns) / n:.3f}")
    print("target: 7 runs")
    fails = [r for r in rows if not r["true_w"]]
    if fails:
        print("plants where the true w does not reach the best (w, R, runs, best, runs on true geometry, w reaching best):")
        for r in fails[:15]:
            print(f"  rep {r['rep']}: w {r['w']} R {r['R']} q {r['q']} runs {r['n_runs']} best {r['best']} "
                  f"true-geom {r['n_true_geom']} w_best {r['w_best'][:8]}")
    print(f"\nCPU this run: {time.process_time() - cpu0:.0f} s main process; plant CPU (workers) "
          f"{sum(r['cpu'] for r in rows):.0f} s; wall {time.time() - wall0:.0f} s")


OBS = [(a, b, len(nm)) for nm, b, a in OBS_LIST]
OBS.sort(key=lambda r: (r[1], r[0]))

if __name__ == "__main__":
    got = shared_runs(T1, T2)
    assert got == sorted(OBS, key=lambda r: (r[1], r[0])), got
    os.makedirs(OUT, exist_ok=True)
    main()
