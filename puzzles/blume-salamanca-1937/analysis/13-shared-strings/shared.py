"""Is the T1 x T2 shared-string excess robust to the choice of n and statistic?

E1 counts strings shared by T1 and T2 in four modes, n = 3-8:
  fwd  exact, T1 against T2 (as 02)
  rev  exact, T1 against reverse(T2)
  ham  at most one mismatch (Hamming distance <= 1), n >= 4
  gap  at most one interior insertion or deletion (an n-letter string against n+1 letters with one interior
       letter skipped, either side; exact matches included), n >= 5
For each mode and n: distinct shared pairs of strings (for fwd and rev, distinct shared n-grams), and
independent runs (matches merged when they overlap in both telegrams on the same diagonal, or on diagonals
one apart for gap). Per mode: the longest shared run.
E2 nulls: (i) independent letter shuffles; (ii) bigram-preserving shuffles (Altschul-Erickson Euler path,
Wilson's algorithm for the last-exit tree); (iii) two independent held-out Spanish telegraph texts
(01-solver/plaintext.py, telegram()) of 615 and 160 letters, each under its own random transposition.
E3 min-p family-wise test over the battery (distinct counts per mode x n, longest run per mode).
E4 post hoc positional checks (seen before the test was written).
Positions are 0-based, as in 02.
Usage (from this folder): python3 -I shared.py > result.txt
"""
import argparse, bisect, json, math, multiprocessing as mp, os, random, sys, time
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER); os.chdir(SOLVER)
import plaintext

def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
T1, T2 = load("../../sources/telegram-1.txt"), load("../../sources/telegram-2.txt")
SEED = 20261016
NULL_ID = {"i": 1, "ii": 2, "iii": 3}
NF, NH, NG = range(3, 9), range(4, 9), range(5, 9)

# ---------------------------------------------------------------- matching
def grams(s, n):
    d = {}
    for i in range(len(s) - n + 1):
        d.setdefault(s[i:i + n], []).append(i)
    return d

def exact(gx, y, n):
    return [(i, n, j, n) for j in range(len(y) - n + 1) for i in gx.get(y[j:j + n], ())]

def ham1(x, y, n):
    keys = {}
    for i in range(len(x) - n + 1):
        w = x[i:i + n]
        for k in range(n):
            keys.setdefault(w[:k] + "." + w[k + 1:], []).append(i)
    found = set()
    for j in range(len(y) - n + 1):
        w = y[j:j + n]
        for k in range(n):
            for i in keys.get(w[:k] + "." + w[k + 1:], ()):
                found.add((i, n, j, n))
    return list(found)

def gap1(x, y, n, gx=None, gy=None):
    gx = gx or grams(x, n); gy = gy or grams(y, n)
    found = set(exact(gx, y, n))
    for j in range(len(y) - n):
        w = y[j:j + n + 1]
        for k in range(1, n):
            for i in gx.get(w[:k] + w[k + 1:], ()):
                found.add((i, n, j, n + 1))
    for i in range(len(x) - n):
        w = x[i:i + n + 1]
        for k in range(1, n):
            for j in gy.get(w[:k] + w[k + 1:], ()):
                found.add((i, n + 1, j, n))
    return list(found)

def distinct(x, y, ms):
    return len({(x[i:i + a], y[j:j + b]) for i, a, j, b in ms})

def merge_runs(ms, tol):
    """Merge matches that overlap in both texts on diagonals within tol. Returns [(i0, i1, j0, j1)]."""
    ms = sorted(ms); par = list(range(len(ms)))
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for a in range(len(ms)):
        i, li, j, lj = ms[a]
        for b in range(a + 1, len(ms)):
            i2, li2, j2, lj2 = ms[b]
            if i2 >= i + li:
                break
            if j2 < j + lj and j < j2 + lj2 and abs((j2 - i2) - (j - i)) <= tol:
                ra, rb = find(a), find(b)
                if ra != rb: par[ra] = rb
    spans = {}
    for a, (i, li, j, lj) in enumerate(ms):
        r = find(a); s = spans.get(r)
        spans[r] = (i, i + li, j, j + lj) if s is None else \
            (min(s[0], i), max(s[1], i + li), min(s[2], j), max(s[3], j + lj))
    return sorted(spans.values())

def longest(fn, have):
    """Longest n with a match, given {n: nonempty} on a contiguous range; matches are monotone in n."""
    ns = sorted(have); hit = [n for n in ns if have[n]]
    if not hit:
        n = ns[0] - 1
        while n >= 1 and not fn(n): n -= 1
        return n
    if hit[-1] < ns[-1]:
        return hit[-1]
    n = ns[-1] + 1
    while fn(n): n += 1
    return n - 1

def selfrep(s, n): return sum(v > 1 for v in Counter(s[i:i + n] for i in range(len(s) - n + 1)).values())

def groups(s): return [s[k:k + 5] for k in range(0, len(s), 5)]

# ---------------------------------------------------------------- one replicate's statistics
BATTERY = ([f"fwd_d{n}" for n in NF] + [f"rev_d{n}" for n in NF] + [f"ham_d{n}" for n in NH] +
           [f"gap_d{n}" for n in NG] + ["fwd_L", "rev_L", "ham_L", "gap_L"])
RUNS = ([f"fwd_r{n}" for n in NF] + [f"rev_r{n}" for n in NF] + [f"ham_r{n}" for n in NH] +
        [f"gap_r{n}" for n in NG])
SELF = [f"{t}_self{n}" for t in ("T1", "T2") for n in (2, 3, 4)]
E4 = ["e4a_final3", "e4a_al8", "e4a_al64", "e4b_first12", "e4b_scan12"]
COLS = BATTERY + RUNS + SELF + E4

def analyse(x, y, detail=None):
    st = {}; yr = y[::-1]
    gx = {n: grams(x, n) for n in NF}
    for mode, yy in (("fwd", y), ("rev", yr)):
        have = {}
        for n in NF:
            ms = exact(gx[n], yy, n); have[n] = bool(ms)
            st[f"{mode}_d{n}"] = distinct(x, yy, ms)
            runs = merge_runs(ms, 0); st[f"{mode}_r{n}"] = len(runs)
            if detail is not None: detail[(mode, n)] = (ms, runs)
            if mode == "fwd" and n == 4:
                starts = sorted(r[2] for r in runs)
                st["e4b_first12"] = sum(s <= 11 for s in starts)
                st["e4b_scan12"] = max([bisect.bisect_right(starts, s + 11) - k for k, s in enumerate(starts)],
                                       default=0)
        st[f"{mode}_L"] = longest(lambda n, yy=yy: bool(exact(grams(x, n), yy, n)), have)
    have = {}
    for n in NH:
        ms = ham1(x, y, n); have[n] = bool(ms)
        st[f"ham_d{n}"] = distinct(x, y, ms)
        runs = merge_runs(ms, 0); st[f"ham_r{n}"] = len(runs)
        if detail is not None: detail[("ham", n)] = (ms, runs)
    st["ham_L"] = longest(lambda n: bool(ham1(x, y, n)), have)
    have = {}
    for n in NG:
        ms = gap1(x, y, n, gx[n], grams(y, n)); have[n] = bool(ms)
        st[f"gap_d{n}"] = distinct(x, y, ms)
        runs = merge_runs(ms, 1); st[f"gap_r{n}"] = len(runs)
        if detail is not None: detail[("gap", n)] = (ms, runs)
    st["gap_L"] = longest(lambda n: bool(gap1(x, y, n)), have)
    for t, s in (("T1", x), ("T2", y)):
        for n in (2, 3, 4): st[f"{t}_self{n}"] = selfrep(s, n)
    gx5, gy5 = groups(x), groups(y)
    px, py = gx5[:4] + gx5[-4:], gy5[:4] + gy5[-4:]
    agree = lambda a, b: sum(p == q for p, q in zip(a, b))
    st["e4a_final3"] = int(x[-5:-2] == y[-5:-2])
    st["e4a_al8"] = sum(agree(a, b) >= 3 for a, b in zip(px, py))
    st["e4a_al64"] = sum(agree(a, b) >= 3 for a in px for b in py)
    return st

# ---------------------------------------------------------------- nulls
def shuf(s, rnd):
    l = list(s); rnd.shuffle(l); return "".join(l)

def euler(s, rnd):
    """Uniform random sequence with the same bigram counts (hence same first and last letter)."""
    first, last = s[0], s[-1]
    succ = {}
    for a, b in zip(s, s[1:]): succ.setdefault(a, []).append(b)
    intree, nxt = {last: True}, {}
    for v in succ:                                   # Wilson: random last-exit tree rooted at `last`
        u = v
        while not intree.get(u):
            nxt[u] = rnd.choice(succ[u]); u = nxt[u]
        u = v
        while not intree.get(u):
            intree[u] = True; u = nxt[u]
    order = {}
    for v, l in succ.items():
        l = l[:]
        if v != last:
            l.remove(nxt[v]); rnd.shuffle(l); l.append(nxt[v])
        else:
            rnd.shuffle(l)
        order[v] = l
    ptr = dict.fromkeys(order, 0); out = [first]; u = first
    for _ in range(len(s) - 1):
        b = order[u][ptr[u]]; ptr[u] += 1; out.append(b); u = b
    return "".join(out)

def bigrams(s): return Counter(zip(s, s[1:]))

def replicate(job):
    null, r = job
    rnd = random.Random(SEED + 1_000_000 * NULL_ID[null] + r)
    if null == "i":
        x, y = shuf(T1, rnd), shuf(T2, rnd)
    elif null == "ii":
        x, y = euler(T1, rnd), euler(T2, rnd)
        assert bigrams(x) == bigrams(T1) and bigrams(y) == bigrams(T2)
    else:
        x = shuf(plaintext.telegram(len(T1), rnd), rnd); y = shuf(plaintext.telegram(len(T2), rnd), rnd)
        assert len(x) == len(T1) and len(y) == len(T2)
    st = analyse(x, y)
    return [st[c] for c in COLS]

def replicate_custom(job):
    """Null (ii) on a supplied pair (E2b ablation)."""
    tag, r, x0, y0 = job
    rnd = random.Random(SEED + 1_000_000 * tag + r)
    st = analyse(euler(x0, rnd), euler(y0, rnd))
    return [st[c] for c in COLS]

def run_null(null, reps, workers):
    path = os.path.join(here, "out", f"null_{null}.json")
    if os.path.exists(path):
        d = json.load(open(path))
        if d["cols"] == COLS and d["reps"] == reps:
            return d["rows"], d["cpu_s"]
    t = time.time()
    jobs = [(null, r) for r in range(reps)]
    if workers > 1:
        with mp.get_context("spawn").Pool(workers) as pool:
            rows = pool.map(replicate, jobs, chunksize=50)
    else:
        rows = [replicate(j) for j in jobs]
    wall = time.time() - t
    json.dump({"cols": COLS, "reps": reps, "cpu_s": wall * workers, "rows": rows}, open(path, "w"))
    return rows, wall * workers

# ---------------------------------------------------------------- p values
def pvalues(obs, rows, names):
    """Pool = null rows + observed (exchangeable under H0). Upper-tail counts as integers."""
    idx = [COLS.index(k) for k in names]; pool = rows + [obs]; N1 = len(pool)
    srt = [sorted(r[c] for r in pool) for c in idx]
    cnt = lambda k, v: N1 - bisect.bisect_left(srt[k], v)
    p_obs = {k: cnt(a, obs[c]) / N1 for a, (k, c) in enumerate(zip(names, idx))}
    minc = [min(cnt(a, r[c]) for a, c in enumerate(idx)) for r in pool]
    m_obs = minc[-1]
    fwp = sum(m <= m_obs for m in minc) / N1
    argmin = [k for a, (k, c) in enumerate(zip(names, idx)) if cnt(a, obs[c]) == m_obs]
    return p_obs, fwp, m_obs / N1, argmin

def binom_tail(n, p, k): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, nargs=3, default=[5000, 5000, 2000])
    ap.add_argument("--workers", type=int, default=max(1, min(8, (os.cpu_count() or 2) - 1)))
    a = ap.parse_args()
    os.makedirs(os.path.join(here, "out"), exist_ok=True)
    det = {}; ost = analyse(T1, T2, det); obs = [ost[c] for c in COLS]
    reps = dict(zip(("i", "ii", "iii"), a.reps))
    print(f"T1 {len(T1)} letters, T2 {len(T2)} letters. Positions 0-based. Seed {SEED}.")
    print(f"Replicates: (i) {reps['i']}, (ii) {reps['ii']}, (iii) {reps['iii']}.\n")

    print("== E1 observed counts (distinct shared / independent runs)")
    print(" n   fwd      rev      ham<=1   gap<=1")
    for n in NF:
        cell = lambda m: f"{ost[f'{m}_d{n}']:>3} / {ost[f'{m}_r{n}']:<3}" if f"{m}_d{n}" in ost else "   -    "
        print(f" {n}  {cell('fwd')}  {cell('rev')}  {cell('ham')}  {cell('gap')}")
    print(" longest run: " + ", ".join(f"{m} {ost[m + '_L']}" for m in ("fwd", "rev", "ham", "gap")))
    print("\nForward runs, n >= 4 (T1 span, T2 span, string):")
    for i0, i1, j0, j1 in det[("fwd", 4)][1]:
        print(f"  T1[{i0}:{i1}] T2[{j0}:{j1}] {T1[i0:i1]}")
    print("Reversed runs, n >= 4 (T1 span = reverse of T2 span; T2 positions in T2's own order):")
    for i0, i1, j0, j1 in det[("rev", 4)][1]:
        print(f"  T1[{i0}:{i1}] {T1[i0:i1]} = reverse T2[{len(T2) - j1}:{len(T2) - j0}] {T2[len(T2) - j1:len(T2) - j0]}")
    print("Reversed runs, n = 3: " + str(ost["rev_r3"]))
    for mode in ("ham", "gap"):
        for n in (6, 5) if mode == "gap" else (7, 6):
            ms = det[(mode, n)][0]
            print(f"{mode} matches, n = {n} ({len(ms)}):")
            for i, li, j, lj in sorted(ms):
                print(f"  T1[{i}:{i + li}] {T1[i:i + li]:<9} T2[{j}:{j + lj}] {T2[j:j + lj]}")

    res = {}; cpu = 0.0
    for null in ("i", "ii", "iii"):
        rows, c = run_null(null, reps[null], a.workers); res[null] = rows; cpu += c
    mean = {nl: {c: sum(r[k] for r in res[nl]) / len(res[nl]) for k, c in enumerate(COLS)} for nl in res}

    print("\n== E2 self-repeats (distinct n-grams occurring twice or more within one telegram)")
    print(" stat       obs   mean (i)  mean (ii)  mean (iii)   P(ii >= obs)  P(ii <= obs)")
    for c in SELF:
        k = COLS.index(c); v = [r[k] for r in res["ii"]]
        ge = sum(x >= ost[c] for x in v) / len(v); le = sum(x <= ost[c] for x in v) / len(v)
        print(f" {c:<9} {ost[c]:>4}   {mean['i'][c]:7.2f}   {mean['ii'][c]:7.2f}    {mean['iii'][c]:7.2f}"
              f"      {ge:6.3f}        {le:6.3f}")

    print("\n== E3 per-statistic p (upper tail; (1 + count) / (N + 1))")
    pv = {nl: pvalues(obs, res[nl], BATTERY + RUNS) for nl in res}
    print(" stat      obs |  mean (i)  p (i)  |  mean (ii)  p (ii) | mean (iii) p (iii)")
    for c in BATTERY + RUNS:
        print(f" {c:<8} {ost[c]:>4} | " + " | ".join(f"{mean[nl][c]:8.2f} {pv[nl][0][c]:7.4f}" for nl in res))
    print("\nFamily-wise p (min-p over the battery; each replicate's p against the same pooled null sample)")
    fams = {"A primary: distinct counts (mode x n) + longest run per mode, 25 stats": BATTERY,
            "B sensitivity: A + independent-run counts, 46 stats": BATTERY + RUNS,
            "C 02's own family: fwd distinct n = 3-6, 4 stats": [f"fwd_d{n}" for n in range(3, 7)],
            "D forward only: fwd distinct n = 3-8 + fwd_L, 7 stats": [f"fwd_d{n}" for n in NF] + ["fwd_L"],
            "E reversed only: rev distinct n = 3-8 + rev_L, 7 stats": [f"rev_d{n}" for n in NF] + ["rev_L"]}
    for name, fam in fams.items():
        print(f" {name}")
        for nl in res:
            _, fwp, mp_, am = pvalues(obs, res[nl], fam)
            print(f"   null ({nl:>3}): family-wise p = {fwp:.4f}; observed min p = {mp_:.4f} at {', '.join(am)}")

    print("\n== E4 post hoc (patterns seen before the test; leads, not findings)")
    c1, c2, N1, N2 = Counter(T1), Counter(T2), len(T1), len(T2); L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def p3(c, N, a, b, d):
        return c[a] * (c[b] - (a == b)) * (c[d] - (a == d) - (b == d)) / (N * (N - 1) * (N - 2))
    pex = sum(p3(c1, N1, a, b, d) * p3(c2, N2, a, b, d) for a in L for b in L for d in L)
    col = lambda nl, c: [r[COLS.index(c)] for r in res[nl]]
    tail = lambda nl, c, v: (1 + sum(x >= v for x in col(nl, c))) / (len(res[nl]) + 1)
    print(f"(a) final groups {T1[-5:]} / {T2[-5:]}: share first three letters = {ost['e4a_final3']}")
    print(f"    P(final groups share first 3 letters | null i), exact = {pex:.5f} (1 in {1 / pex:.0f});"
          f" Monte Carlo {sum(col('i', 'e4a_final3')) / len(res['i']):.5f}")
    for c, what in (("e4a_al8", "8 rank-aligned group pairs (first 4 from start, last 4 from end)"),
                    ("e4a_al64", "64 group pairs among the first 4 and last 4 groups of each")):
        dist = Counter(col("i", c))
        print(f"    {what}: pairs with >= 3 aligned letters agreeing, observed {ost[c]};"
              f" p (i) = {tail('i', c, ost[c]):.4f}, p (iii) = {tail('iii', c, ost[c]):.4f};"
              f" null (i) distribution {dict(sorted(dist.items()))}")
    R = ost["fwd_r4"]; k = ost["e4b_first12"]; starts = sorted(r[2] for r in det[("fwd", 4)][1])
    print(f"(b) forward 4+-letter runs: {R}; T2 starts {starts}; starts in T2[0:12]: {k}")
    print(f"    given {R} runs, starts uniform on 0-156: P(>= {k} in 0-11) = {binom_tail(R, 12 / 157, k):.5f} (binomial)")
    rnd = random.Random(SEED + 99); M = 200000; hit = 0
    for _ in range(M):
        s = sorted(rnd.randrange(157) for _ in range(R))
        if max(bisect.bisect_right(s, v + 11) - q for q, v in enumerate(s)) >= k: hit += 1
    print(f"    scan version (any 12-letter window of T2 holding >= {k} starts), {M} draws: P = {hit / M:.4f};"
          f" observed max in any window {ost['e4b_scan12']}")
    for nl in ("i", "iii"):
        print(f"    null ({nl}) directly: P(>= {k} run starts in T2[0:12]) = {tail(nl, 'e4b_first12', k):.4f};"
              f" P(any 12-window >= {k}) = {tail(nl, 'e4b_scan12', k):.4f}")
    cpu += ablation(obs, det, res, a.workers)
    print(f"\nNull CPU about {cpu / 60:.1f} min (wall x workers; cached nulls count the run that built them).")

def ablation(obs, det, res, workers, reps=4000):
    """E2b, added after the E3 result (not pre-registered): does null (ii) absorb the signal?"""
    print("\n== E2b (added after seeing E3; not pre-registered): does null (ii) carry the shared strings?")
    b1, b2 = bigrams(T1), bigrams(T2)
    sim = lambda p, q: sum(v * q[k] for k, v in p.items())
    rnd = random.Random(SEED + 77); S = []; D = []
    for _ in range(20000):
        p, q = bigrams(shuf(T1, rnd)), bigrams(shuf(T2, rnd)); S.append(sim(p, q)); D.append(len(p.keys() & q.keys()))
    so, do = sim(b1, b2), len(b1.keys() & b2.keys())
    print(f" T1 x T2 bigram overlap, sum c1(b) c2(b): observed {so}, null (i) mean {sum(S) / len(S):.1f},"
          f" p = {(1 + sum(s >= so for s in S)) / (len(S) + 1):.4f}")
    print(f" distinct bigrams shared: observed {do}, null (i) mean {sum(D) / len(D):.1f},"
          f" p = {(1 + sum(d >= do for d in D)) / (len(D) + 1):.4f}  (null (ii) fixes both at the observed)")
    c1, c2 = Counter(T1), Counter(T2)
    ex = lambda c, N, a, b: c[a] * (c[b] - (a == b)) / N          # E[count of bigram ab] under a shuffle
    contrib = sorted(((b1[k] * b2[k] - ex(c1, len(T1), *k) * ex(c2, len(T2), *k), "".join(k), b1[k], b2[k])
                      for k in set(b1) | set(b2)), reverse=True)
    print(" largest contributions to the excess (c1 c2 - shuffle expectation): " +
          ", ".join(f"{s} {d:+.0f} ({x}x{y})" for d, s, x, y in contrib[:8]))
    dbl = lambda s: sum(p == q for p, q in zip(s, s[1:]))
    print(f" doubled letters: T1 {dbl(T1)} (shuffle expectation {sum(ex(c1, len(T1), a, a) for a in c1):.1f}),"
          f" T2 {dbl(T2)} (expectation {sum(ex(c2, len(T2), a, a) for a in c2):.1f})")
    runpos = sorted({j for _, _, j0, j1 in det[("fwd", 4)][1] for j in range(j0, j1)})
    others = [j for j in range(len(T2)) if j not in runpos]
    print(f" T2 positions in the 7 forward runs: {len(runpos)}. Variant T2s permute the letters among those"
          f" positions ('runs broken'), or among as many random other positions ('control'). {reps} null (ii)"
          f" replicates each; observed statistics unchanged.")
    print(" variant            T2 bigram sim  mean fwd_d3  mean fwd_d4  p(fwd_d4 = 9)  family-wise p (A)")
    base = res["ii"]; m = lambda rows, c: sum(r[COLS.index(c)] for r in rows) / len(rows)
    print(f" original T2         {so:>6}       {m(base, 'fwd_d3'):7.2f}      {m(base, 'fwd_d4'):6.2f}"
          f"       {pvalues(obs, base, ['fwd_d4'])[0]['fwd_d4']:.4f}         {pvalues(obs, base, BATTERY)[1]:.4f}")
    t = time.time(); cpu = 0.0
    for tag, (kind, k) in enumerate([("runs broken", s) for s in range(3)] + [("control", s) for s in range(3)], 10):
        vr = random.Random(SEED + 500 + tag)
        pos = runpos if kind == "runs broken" else sorted(vr.sample(others, len(runpos)))
        y = list(T2); lets = [y[j] for j in pos]; vr.shuffle(lets)
        for j, c in zip(pos, lets): y[j] = c
        y = "".join(y)
        jobs = [(tag, r, T1, y) for r in range(reps)]
        with mp.get_context("spawn").Pool(workers) as pool:
            rows = pool.map(replicate_custom, jobs, chunksize=50)
        print(f" {kind:<12} {k}      {sim(b1, bigrams(y)):>6}       {m(rows, 'fwd_d3'):7.2f}      {m(rows, 'fwd_d4'):6.2f}"
              f"       {pvalues(obs, rows, ['fwd_d4'])[0]['fwd_d4']:.4f}         {pvalues(obs, rows, BATTERY)[1]:.4f}")
    return (time.time() - t) * workers

if __name__ == "__main__":
    main()
