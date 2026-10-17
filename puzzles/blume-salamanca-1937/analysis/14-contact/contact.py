"""14-contact: does vowel/consonant contact rule out K1 (forward double columnar, long keys)?

V1a  class autocorrelation r(k), k = 1-40 (T1) / 1-20 (T2), two-sided, min p over lags, calibrated.
V1b  cross-telegram bigram overlap S = sum_b c1(b) c2(b), all bigrams and vowel-vowel only, upper tail.
V1c  vowel-count dispersion D_m in non-overlapping windows, two-sided, min p over m, calibrated; runs test beside it.
Nulls: (a) letter shuffles of each telegram; (b) K1 plants (Spanish telegraph plaintext, forward CC, w1, w2 in 16-25).
Positive controls: letters permuted within sets of 5-12; rows of width 5-15 read in a random order.
Usage (from this folder): python3 -I contact.py > result.txt      (--quick for a small smoke run)
"""
import bisect, json, math, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
from operator import add

here = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(here, "..", "01-solver")
sys.path.insert(0, SOLVER)
os.chdir(SOLVER)  # plaintext.py reads its corpus by relative path
import plaintext, transpo

SEED = 20261016
VOW = frozenset("AEIOU")
VV_SET = frozenset(a + b for a in "AEIOU" for b in "AEIOU")
CFG = {615: dict(lags=40, ms=(5, 10, 15, 20, 25, 30, 41)), 160: dict(lags=20, ms=(5, 8, 10, 16, 20))}
W_LONG = range(16, 26)
EPS = 1e-12
QUICK = "--quick" in sys.argv
N_SHUF = 2000 if QUICK else 20000       # null (a), per telegram
N_PLANT = 1000 if QUICK else 10000      # null (b), per length (floor 2,000)
N_SHARED = 200 if QUICK else 2000       # null (b2) pairs (floor 1,000)
N_CTRL = 50 if QUICK else 500           # positive controls per family per length (floor 300)
N_CTRL_SHUF = 200 if QUICK else 1000    # own shuffles per control, for null (a)
WORKERS = 7

# ---------- statistics ----------
def vbits(t):
    """Bit i of the result is 1 iff letter i is a vowel."""
    return int("".join("1" if c in VOW else "0" for c in reversed(t)), 2)

def class_stats(t):
    """Lag-1 contact counts, r(1..K), D_m for each m, runs z. t is a string of length 615 or 160."""
    N = len(t); X = vbits(t); nv = X.bit_count(); p = nv / N; npq = N * p * (1 - p); cfg = CFG[N]
    r = []
    for k in range(1, cfg["lags"] + 1):
        A = (X & (X >> k)).bit_count()                 # sum x_i x_{i+k}
        St = (X >> k).bit_count()                      # sum_{i >= k} x_i
        Sh = (X & ((1 << (N - k)) - 1)).bit_count()    # sum_{i < N-k} x_i
        r.append((A - p * (Sh + St) + (N - k) * p * p) / npq)
    D = []
    for m in cfg["ms"]:
        W, mask = N // m, (1 << m) - 1
        c = [((X >> (j * m)) & mask).bit_count() for j in range(W)]
        mu = sum(c) / W
        D.append(sum((v - mu) ** 2 for v in c) / W / (m * p * (1 - p)))
    A1 = (X & (X >> 1)).bit_count()
    VV, VC, CV = A1, (X & ((1 << (N - 1)) - 1)).bit_count() - A1, (X >> 1).bit_count() - A1
    CC = N - 1 - VV - VC - CV
    R, n1, n0 = 1 + VC + CV, nv, N - nv
    ER, VR = 1 + 2 * n1 * n0 / N, 2 * n1 * n0 * (2 * n1 * n0 - N) / (N * N * (N - 1))
    return (VV, VC, CV, CC), r, D, (R - ER) / math.sqrt(VR)

def bigram_counts(t): return Counter(map(add, t, t[1:]))

def overlap(c1, c2):
    s_all = s_vv = 0
    for b, v in c2.items():
        u = c1.get(b, 0) * v
        s_all += u
        if b in VV_SET: s_vv += u
    return s_all, s_vv

def expected_overlap(t1, t2):
    """E[S | letter counts] under independent shuffles: E c(ab) = n_a n_b / N (a != b), n_a (n_a - 1) / N (a = b)."""
    n1, n2, N1, N2 = Counter(t1), Counter(t2), len(t1), len(t2)
    out = []
    for letters in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "AEIOU"):
        u = [n1[a] * n2[a] for a in letters]
        same = sum(n1[a] * (n1[a] - 1) * n2[a] * (n2[a] - 1) for a in letters)
        out.append((sum(u) ** 2 - sum(x * x for x in u) + same) / (N1 * N2))
    return out

# ---------- calibration ----------
class Ref:
    """Reference set of statistic vectors. Per-statistic p (two-sided or upper), min p over the vector, calibrated."""
    def __init__(self, rows, two_sided=True):
        self.M, self.two = len(rows), two_sided
        self.cols = [sorted(col) for col in zip(*rows)]
        self.minp_sorted = sorted(self.minp(r, internal=True)[0] for r in rows)
    def p(self, l, v, internal=False):
        s, M = self.cols[l], self.M
        ge, le = M - bisect.bisect_left(s, v - EPS), bisect.bisect_right(s, v + EPS)
        if internal: d = M
        else: ge, le, d = ge + 1, le + 1, M + 1
        return min(1.0, 2 * min(ge, le) / d) if self.two else ge / d
    def minp(self, vec, internal=False):
        ps = [self.p(l, v, internal) for l, v in enumerate(vec)]
        m = min(ps); return m, ps.index(m), ps
    def calibrated(self, vec):
        m, arg, ps = self.minp(vec)
        return (1 + bisect.bisect_right(self.minp_sorted, m + EPS)) / (self.M + 1), m, arg, ps
    def mean(self, l): return sum(self.cols[l]) / self.M
    def sd(self, l):
        mu = self.mean(l); return math.sqrt(sum((v - mu) ** 2 for v in self.cols[l]) / (self.M - 1))

def upper_p(ref_vals, obs):
    return (1 + sum(v >= obs - EPS for v in ref_vals)) / (len(ref_vals) + 1)

def two_p(ref_vals, obs):
    ge = sum(v >= obs - EPS for v in ref_vals); le = sum(v <= obs + EPS for v in ref_vals); M = len(ref_vals)
    return min(1.0, 2 * min(ge + 1, le + 1) / (M + 1))

# ---------- systems ----------
def k1_plant(pt, rnd):
    w1, w2 = rnd.choice(W_LONG), rnd.choice(W_LONG)
    k1, k2 = rnd.sample(range(w1), w1), rnd.sample(range(w2), w2)
    return transpo.double_enc(pt, k1, k2, "CC"), w1, w2, k1, k2

def neighbour_dist(N, k1, k2):
    """Plaintext distances between ciphertext neighbours under these keys (diagnostic)."""
    idx = "".join(chr(0x4E00 + i) for i in range(N))
    c = [ord(x) - 0x4E00 for x in transpo.double_enc(idx, k1, k2, "CC")]
    return [abs(c[i + 1] - c[i]) for i in range(N - 1)]

def block_inner(pt, rnd, n):  # as 04-run-keeping/runs.py: one key for every full set; last partial set in place
    k = rnd.sample(range(n), n)
    return "".join("".join(b[j] for j in k) if len(b) == n else b for b in (pt[i:i + n] for i in range(0, len(pt), n)))

def row_perm(pt, rnd, w):     # as 04-run-keeping/runs.py: rows of width w, read in a random order
    r = [pt[i:i + w] for i in range(0, len(pt), w)]; rnd.shuffle(r); return "".join(r)

CONTROLS = [("letters permuted within sets of n", block_inner, range(5, 13)),
            ("rows of width w read in a random order", row_perm, range(5, 16))]

# ---------- worker: own-shuffle calibration of one control (null a) ----------
def own_shuffle_cal(args):
    t, seed, n = args
    rnd, L, ra, rc = random.Random(seed), list(t), [], []
    for _ in range(n):
        rnd.shuffle(L); _, r, D, _ = class_stats("".join(L)); ra.append(r); rc.append(D)
    _, r, D, _ = class_stats(t)
    return Ref(ra).calibrated(r)[0], Ref(rc).calibrated(D)[0]

# ---------- main ----------
def main():
    t0 = time.time()
    transpo._tests()
    def load(p): return "".join(c for c in open(os.path.join(here, p)).read().upper() if c.isalpha())
    tel = {"T1": load("../../sources/telegram-1.txt"), "T2": load("../../sources/telegram-2.txt")}
    assert (len(tel["T1"]), len(tel["T2"])) == (615, 160)
    obs = {k: class_stats(t) for k, t in tel.items()}
    obs_S = overlap(bigram_counts(tel["T1"]), bigram_counts(tel["T2"]))
    obs_E = expected_overlap(tel["T1"], tel["T2"])
    out = {}

    print(f"T1 {len(tel['T1'])} letters, T2 {len(tel['T2'])} letters. Vowels AEIOU. Seed {SEED}.")
    print(f"Null (a): {N_SHUF} shuffles per telegram. Null (b): {N_PLANT} K1 plants per length (forward CC, "
          f"w1, w2 uniform 16-25); (b2) {N_SHARED} shared-key, shared-phrase pairs.")
    print(f"Controls: {N_CTRL} per family per length; null (a) for controls uses {N_CTRL_SHUF} own shuffles each.\n")

    # ----- null (a): shuffles -----
    sh = {k: [] for k in tel}; shS = []
    rA = {"T1": random.Random(SEED + 11), "T2": random.Random(SEED + 12)}
    L = {k: list(t) for k, t in tel.items()}
    for _ in range(N_SHUF):
        bc = {}
        for k in tel:
            rA[k].shuffle(L[k]); s = "".join(L[k]); sh[k].append(class_stats(s)); bc[k] = bigram_counts(s)
        shS.append(overlap(bc["T1"], bc["T2"]))
    print(f"[null (a) done, {time.time() - t0:.0f} s]", file=sys.stderr)

    # ----- null (b): K1 plants, and (b1) pairs -----
    pl = {615: [], 160: []}; plS1, plE1, plW, nd = [], [], {615: [], 160: []}, {615: [], 160: []}
    ptst = {615: [], 160: []}  # the plants' plaintexts, for reference (no randomness used)
    rB = {615: random.Random(SEED + 21), 160: random.Random(SEED + 22)}
    for j in range(N_PLANT):
        ct = {}
        for N in (615, 160):
            pt = plaintext.telegram(N, rB[N]); c, w1, w2, k1, k2 = k1_plant(pt, rB[N])
            assert sorted(c) == sorted(pt) and len(c) == N
            ct[N] = c; pl[N].append(class_stats(c)); plW[N].append((w1, w2))
            if j < 2000:
                ptst[N].append(class_stats(pt))
                d = neighbour_dist(N, k1, k2); nd[N].append((sum(x <= 10 for x in d) / (N - 1), sum(x <= 3 for x in d) / (N - 1)))
        plS1.append(overlap(bigram_counts(ct[615]), bigram_counts(ct[160])))
        plE1.append(expected_overlap(ct[615], ct[160]))
    print(f"[null (b) done, {time.time() - t0:.0f} s]", file=sys.stderr)

    # ----- null (b2): shared keys, shared opening phrase -----
    plS2, plE2, phl = [], [], []
    r2 = random.Random(SEED + 23)
    for _ in range(N_SHARED):
        Lp = r2.randint(40, 100); phrase = plaintext.telegram(Lp, r2)
        p1, p2 = phrase + plaintext.telegram(615 - Lp, r2), phrase + plaintext.telegram(160 - Lp, r2)
        w1, w2 = r2.choice(W_LONG), r2.choice(W_LONG); k1, k2 = r2.sample(range(w1), w1), r2.sample(range(w2), w2)
        c1, c2 = transpo.double_enc(p1, k1, k2, "CC"), transpo.double_enc(p2, k1, k2, "CC")
        assert len(c1) == 615 and len(c2) == 160
        plS2.append(overlap(bigram_counts(c1), bigram_counts(c2))); plE2.append(expected_overlap(c1, c2)); phl.append(Lp)
    print(f"[null (b2) done, {time.time() - t0:.0f} s]", file=sys.stderr)

    # ----- reference sets -----
    REF = {}
    for k, N in (("T1", 615), ("T2", 160)):
        REF[k, "a", "r"] = Ref([s[1] for s in sh[k]]); REF[k, "a", "D"] = Ref([s[2] for s in sh[k]])
        REF[k, "b", "r"] = Ref([s[1] for s in pl[N]]); REF[k, "b", "D"] = Ref([s[2] for s in pl[N]])
    print(f"[references built, {time.time() - t0:.0f} s]", file=sys.stderr)

    # ----- V1a / V1c on the telegrams -----
    summary = {}
    for k, N in (("T1", 615), ("T2", 160)):
        (VV, VC, CV, CC), r, D, z = obs[k]; t = tel[k]; nv = sum(c in VOW for c in t); nc = N - nv
        print(f"== {k}: {nv} vowels of {N} (share {nv / N:.3f})")
        print(f"V1a lag-1 contact (observed; expected under shuffle):")
        print(f"   VV {VV} ({nv * (nv - 1) / N:.1f})  VC {VC} ({nv * nc / N:.1f})  CV {CV} ({nv * nc / N:.1f})  "
              f"CC {CC} ({nc * (nc - 1) / N:.1f})")
        print(f"V1a class autocorrelation r(k):")
        print(f"   {'k':>3} {'r obs':>8} | {'mean (a)':>8} {'sd (a)':>7} {'z (a)':>6} {'p (a)':>7} | {'mean (b)':>8} {'sd (b)':>7} {'p (b)':>7}")
        Ra, Rb = REF[k, "a", "r"], REF[k, "b", "r"]
        cal_a, mp_a, arg_a, ps_a = Ra.calibrated(r); cal_b, mp_b, arg_b, ps_b = Rb.calibrated(r)
        for l, v in enumerate(r):
            za = (v - Ra.mean(l)) / Ra.sd(l)
            print(f"   {l + 1:>3} {v:+8.4f} | {Ra.mean(l):+8.4f} {Ra.sd(l):7.4f} {za:+6.2f} {ps_a[l]:7.4f} | "
                  f"{Rb.mean(l):+8.4f} {Rb.sd(l):7.4f} {ps_b[l]:7.4f}")
        print(f"   V1a min p over lags: (a) {mp_a:.4f} at k = {arg_a + 1}, calibrated p = {cal_a:.4f}; "
              f"(b) {mp_b:.4f} at k = {arg_b + 1}, calibrated p = {cal_b:.4f}")
        Da, Db = REF[k, "a", "D"], REF[k, "b", "D"]
        dca, dma, darga, dpa = Da.calibrated(D); dcb, dmb, dargb, dpb = Db.calibrated(D)
        print(f"V1c vowel-count dispersion D_m (two-sided p; upper-tail p for information):")
        print(f"   {'m':>3} {'win':>4} {'D obs':>7} | {'mean (a)':>8} {'p (a)':>7} {'up (a)':>7} | {'mean (b)':>8} {'p (b)':>7} {'up (b)':>7}")
        for l, m in enumerate(CFG[N]["ms"]):
            ua = upper_p(Da.cols[l], D[l]); ub = upper_p(Db.cols[l], D[l])
            print(f"   {m:>3} {N // m:>4} {D[l]:7.3f} | {Da.mean(l):8.3f} {dpa[l]:7.4f} {ua:7.4f} | {Db.mean(l):8.3f} {dpb[l]:7.4f} {ub:7.4f}")
        print(f"   V1c min p over m: (a) {dma:.4f} at m = {CFG[N]['ms'][darga]}, calibrated p = {dca:.4f}; "
              f"(b) {dmb:.4f} at m = {CFG[N]['ms'][dargb]}, calibrated p = {dcb:.4f}")
        za_runs = [s[3] for s in sh[k]]; zb_runs = [s[3] for s in pl[N]]
        p_norm = math.erfc(abs(z) / math.sqrt(2))
        print(f"Runs test: runs {1 + VC + CV}, z = {z:+.3f} (normal two-sided p {p_norm:.4f}); "
              f"p (a) {two_p(za_runs, z):.4f}; p (b) {two_p(zb_runs, z):.4f}\n")
        summary[k] = dict(V1a_a=cal_a, V1a_b=cal_b, V1a_lag_a=arg_a + 1, V1a_lag_b=arg_b + 1,
                          V1c_a=dca, V1c_b=dcb, V1c_m_a=CFG[N]["ms"][darga], V1c_m_b=CFG[N]["ms"][dargb],
                          runs_a=two_p(za_runs, z), runs_b=two_p(zb_runs, z), runs_z=z)

    # ----- V1b -----
    print("== V1b cross-telegram bigram overlap (upper tail)")
    print(f"   {'stat':>6} {'obs':>5} {'E|counts':>8} | {'mean (a)':>8} {'sd':>5} {'p (a)':>7} | {'mean (b1)':>9} {'sd':>5} {'p (b1)':>7} | {'mean (b2)':>9} {'sd':>5} {'p (b2)':>7}")
    def sd(v): mu = sum(v) / len(v); return math.sqrt(sum((x - mu) ** 2 for x in v) / (len(v) - 1))
    v1b = {}
    for i, name in enumerate(("S_all", "S_VV")):
        a = [s[i] for s in shS]; b1 = [s[i] for s in plS1]; b2 = [s[i] for s in plS2]
        pa, pb1, pb2 = upper_p(a, obs_S[i]), upper_p(b1, obs_S[i]), upper_p(b2, obs_S[i])
        v1b[name] = (pa, pb1, pb2)
        print(f"   {name:>6} {obs_S[i]:>5} {obs_E[i]:8.1f} | {sum(a) / len(a):8.1f} {sd(a):5.1f} {pa:7.4f} | "
              f"{sum(b1) / len(b1):9.1f} {sd(b1):5.1f} {pb1:7.4f} | {sum(b2) / len(b2):9.1f} {sd(b2):5.1f} {pb2:7.4f}")
    print("   Excess S - E[S | letter counts] (diagnostic; under (a) identical to S):")
    for i, name in enumerate(("S_all", "S_VV")):
        xo = obs_S[i] - obs_E[i]
        x1 = [s[i] - e[i] for s, e in zip(plS1, plE1)]; x2 = [s[i] - e[i] for s, e in zip(plS2, plE2)]
        xa = [s[i] - obs_E[i] for s in shS]
        print(f"   {name:>6} excess {xo:+7.1f} | (a) mean {sum(xa) / len(xa):+6.1f} sd {sd(xa):4.1f} p {upper_p(xa, xo):.4f} | "
              f"(b1) mean {sum(x1) / len(x1):+6.1f} sd {sd(x1):4.1f} p {upper_p(x1, xo):.4f} | "
              f"(b2) mean {sum(x2) / len(x2):+6.1f} sd {sd(x2):4.1f} p {upper_p(x2, xo):.4f}")
    e1 = [e[0] for e in plE1]
    print(f"   E[S_all | letter counts]: telegrams {obs_E[0]:.1f}; (b1) plants mean {sum(e1) / len(e1):.1f}, sd {sd(e1):.1f}, "
          f"share at or below the telegrams' {sum(x <= obs_E[0] for x in e1) / len(e1):.4f}")
    bon = {nl: min(1.0, 2 * min(v1b["S_all"][j], v1b["S_VV"][j])) for j, nl in enumerate(("a", "b1", "b2"))}
    print(f"   V1b p = 2 x min(p_all, p_VV): (a) {bon['a']:.4f}; (b1) {bon['b1']:.4f}; (b2) {bon['b2']:.4f}; "
          f"reading uses max(b1, b2) = {max(bon['b1'], bon['b2']):.4f}")
    c1, c2 = bigram_counts(tel["T1"]), bigram_counts(tel["T2"]); n1, n2 = Counter(tel["T1"]), Counter(tel["T2"])
    def e(n, N, b): return n[b[0]] * (n[b[1]] - (b[0] == b[1])) / N
    contrib = sorted(((c1.get(b, 0) * v - e(n1, 615, b) * e(n2, 160, b), b, c1.get(b, 0), v) for b, v in c2.items()), reverse=True)
    print("   Largest contributions c1 x c2 - E1 x E2: " +
          ", ".join(f"{b} {x:+.1f} ({u}x{v})" for x, b, u, v in contrib[:8]) + "\n")

    # ----- K1 plant diagnostics -----
    print("== K1 plant diagnostics (first 2,000 plants per length)")
    for N in (615, 160):
        P = ptst[N]; M = len(P)
        rr = [sum(x[1][k] for x in P) / M for k in range(5)]; d5 = sum(x[2][0] for x in P) / M
        print(f"   {N}: the plants' plaintexts before transposition: mean r(1..5) " + " ".join(f"{v:+.3f}" for v in rr) +
              f"; mean D_5 {d5:.3f}; mean vowel share {sum(x[0][0] + x[0][1] for x in P) / M / (N - 1):.3f}")
    for N in (615, 160):
        a10 = sorted(x[0] for x in nd[N]); a3 = sorted(x[1] for x in nd[N]); M = len(a10)
        print(f"   {N}: share of ciphertext neighbours <= 10 plaintext letters apart: median {a10[M // 2]:.3f}, "
              f"90th pct {a10[int(0.9 * M)]:.3f}, max {a10[-1]:.3f}; <= 3 apart: median {a3[M // 2]:.3f}, max {a3[-1]:.3f}")
    for k, N in (("T1", 615), ("T2", 160)):
        # How shuffle-like are K1 plants? Calibrate each plant against the telegram's shuffles (null a),
        # split by the share of ciphertext neighbours that are <= 10 plaintext letters apart.
        Ra, Da = REF[k, "a", "r"], REF[k, "a", "D"]
        grp = {}; keys_hi = Counter()
        for s_, (w1, w2), (f10, _) in zip(pl[N], plW[N], nd[N]):
            g = "short-neighbour share > 0.05" if f10 > 0.05 else "short-neighbour share <= 0.05"
            grp.setdefault(g, []).append((Ra.calibrated(s_[1])[0], Da.calibrated(s_[2])[0]))
            if f10 > 0.05: keys_hi[w1, w2] += 1
        for g, v in sorted(grp.items()):
            print(f"   {k}-length plants against {k}'s shuffles (null a), {g}: n {len(v)}, "
                  f"V1a p < 0.01 in {sum(x[0] < 0.01 for x in v) / len(v):.3f}, V1c p < 0.01 in {sum(x[1] < 0.01 for x in v) / len(v):.3f}")
        print(f"      commonest (w1, w2) with share > 0.05: " + ", ".join(f"{a}x{b} ({n})" for (a, b), n in keys_hi.most_common(8)))
    print()

    # ----- positive controls -----
    print("== Positive controls (calibrated p < 0.01)")
    print(f"   {'family':<40} {'N':>4} {'V1a (b)':>8} {'V1c (b)':>8} {'V1a (a)':>8} {'V1c (a)':>8}")
    ctrl_rows, jobs = [], []
    rC = random.Random(SEED + 31)
    for fi, (name, fn, prm) in enumerate(CONTROLS):
        for k, N in (("T1", 615), ("T2", 160)):
            for i in range(N_CTRL):
                par = rC.choice(list(prm)); c = fn(plaintext.telegram(N, rC), rC, par)
                assert len(c) == N
                _, r, D, _ = class_stats(c)
                pa_b = REF[k, "b", "r"].calibrated(r); pc_b = REF[k, "b", "D"].calibrated(D)
                l = pc_b[2]; lowtail = D[l] < REF[k, "b", "D"].cols[l][REF[k, "b", "D"].M // 2]
                ctrl_rows.append(dict(family=fi, N=N, par=par, V1a_b=pa_b[0], V1c_b=pc_b[0],
                                      V1a_lag=pa_b[2] + 1, V1c_m=CFG[N]["ms"][l], V1c_low=lowtail))
                jobs.append((c, SEED * 1000 + len(jobs), N_CTRL_SHUF))
    with Pool(WORKERS) as pool:
        for row, (pa, pc) in zip(ctrl_rows, pool.map(own_shuffle_cal, jobs, chunksize=8)):
            row["V1a_a"], row["V1c_a"] = pa, pc
    print(f"[controls done, {time.time() - t0:.0f} s]", file=sys.stderr)
    power = {}
    for N in (615, 160):
        for fi in (0, 1, None):
            rows = [x for x in ctrl_rows if x["N"] == N and (fi is None or x["family"] == fi)]
            sh_ = {s: sum(x[s] < 0.01 for x in rows) / len(rows) for s in ("V1a_b", "V1c_b", "V1a_a", "V1c_a")}
            label = CONTROLS[fi][0] if fi is not None else "POOLED (both families)"
            print(f"   {label:<40} {N:>4} {sh_['V1a_b']:8.3f} {sh_['V1c_b']:8.3f} {sh_['V1a_a']:8.3f} {sh_['V1c_a']:8.3f}")
            if fi is None: power[N] = sh_
    # where the controls' signal sits
    for N in (615, 160):
        for fi, (name, _, prm) in enumerate(CONTROLS):
            rows = [x for x in ctrl_rows if x["N"] == N and x["family"] == fi]
            byp = {}
            for x in rows: byp.setdefault(x["par"], []).append(x)
            s = ", ".join(f"{p}: {sum(x['V1a_b'] < 0.01 for x in v)}/{sum(x['V1c_b'] < 0.01 for x in v)}/{len(v)}" for p, v in sorted(byp.items()))
            lags = Counter(x["V1a_lag"] for x in rows if x["V1a_b"] < 0.01).most_common(3)
            ms = Counter(x["V1c_m"] for x in rows if x["V1c_b"] < 0.01).most_common(3)
            print(f"   {N} {name}: by parameter (V1a hits / V1c hits / n, null b): {s}")
            low = sum(x["V1c_low"] for x in rows if x["V1c_b"] < 0.01)
            print(f"      commonest carrying lag {lags}; window {ms}; V1c hits in the lower tail (too even) {low}")
    print()

    # ----- summary -----
    print("== Summary (calibrated p)")
    for k, N in (("T1", 615), ("T2", 160)):
        s = summary[k]
        print(f"   {k}: V1a (a) {s['V1a_a']:.4f} [k={s['V1a_lag_a']}], (b) {s['V1a_b']:.4f} [k={s['V1a_lag_b']}]; "
              f"V1c (a) {s['V1c_a']:.4f} [m={s['V1c_m_a']}], (b) {s['V1c_b']:.4f} [m={s['V1c_m_b']}]; "
              f"runs (a) {s['runs_a']:.4f}, (b) {s['runs_b']:.4f}; power (b) V1a {power[N]['V1a_b']:.3f}, V1c {power[N]['V1c_b']:.3f}")
    print(f"   V1b: (a) {bon['a']:.4f}; (b1) {bon['b1']:.4f}; (b2) {bon['b2']:.4f}")
    print(f"   Run time {time.time() - t0:.0f} s wall.")

    os.makedirs(os.path.join(here, "out"), exist_ok=True)
    tag = "quick" if QUICK else "full"
    json.dump(dict(summary=summary, v1b=v1b, bonferroni=bon, power={str(k): v for k, v in power.items()},
                   controls=ctrl_rows, plant_keys={str(k): v for k, v in plW.items()},
                   plant_S1=plS1, plant_S2=plS2, plant_E1=plE1, plant_E2=plE2, phrase_len=phl, shuffle_S=shS),
              open(os.path.join(here, "out", f"{tag}.json"), "w"))

if __name__ == "__main__":
    main()
