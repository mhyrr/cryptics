# A399145 / A399147, method b: all proper crossings of P_n with P_m (m<n) found by brute interleaving test over all side
# pairs restricted by an angular window, coordinates from the polar line form x cos(mu)+y sin(mu)=cos(delta) (2x2 solve),
# then global 2-D near-duplicate search (sort by x, compare points within 1e-9 in x and y); candidates confirmed with mpmath.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
import mpmath; mpmath.mp.dps = 50
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1400
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
VAR = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(os.path.dirname(os.path.abspath(__file__)))
H = {"A399145": 0, "A399147": 1}[VAR]          # vertex j of P_m at angle 2pi*(2j+H)/(2m)
@njit(cache=True)
def pts(n, H, X, Y, M, I, J):
    k = 0
    for m in range(3, n):
        for i in range(n):              # side i of P_n: vertices i, i+1  (angles in units of 1/(2nm) turns: m*(2i+H))
            A1 = m * (2 * i + H); A2 = m * (2 * i + 2 + H); full = 2 * n * m
            jc = (i * m) // n
            lo = 0 if m < 8 else jc - 2
            hi = m if m < 8 else jc + 3
            for jr in range(lo, hi):    # side j of P_m, only those near the arc of side i (all of them when m<8)
                j = jr % m
                B1 = n * (2 * j + H); B2 = n * (2 * j + 2 + H)
                # interleaving on the circle, exact integer test (shared endpoints -> not proper)
                b1 = (B1 - A1) % full; b2 = (B2 - A1) % full; a2 = A2 - A1
                in1 = 0 < b1 < a2; in2 = 0 < b2 < a2
                out1 = b1 > a2; out2 = b2 > a2
                if (in1 and out2) or (in2 and out1):
                    mu1 = math.pi * (A1 + A2) / full; de1 = math.pi * (A2 - A1) / full
                    mu2 = math.pi * (B1 + B2) / full; de2 = math.pi * (B2 - B1) / full
                    c1, s1, c2, s2 = math.cos(mu1), math.sin(mu1), math.cos(mu2), math.sin(mu2)
                    det = c1 * s2 - s1 * c2
                    r1 = math.cos(de1); r2 = math.cos(de2)
                    X[k] = (r1 * s2 - s1 * r2) / det; Y[k] = (c1 * r2 - r1 * c2) / det
                    M[k] = m; I[k] = i; J[k] = j; k += 1
    return k
def exact(n, m, i, j):
    full = 2 * n * m
    A1 = m * (2 * i + H); A2 = m * (2 * i + 2 + H); B1 = n * (2 * j + H); B2 = n * (2 * j + 2 + H)
    mu1 = mpmath.pi * (A1 + A2) / full; de1 = mpmath.pi * (A2 - A1) / full
    mu2 = mpmath.pi * (B1 + B2) / full; de2 = mpmath.pi * (B2 - B1) / full
    c1, s1, c2, s2 = mpmath.cos(mu1), mpmath.sin(mu1), mpmath.cos(mu2), mpmath.sin(mu2)
    det = c1 * s2 - s1 * c2; r1 = mpmath.cos(de1); r2 = mpmath.cos(de2)
    return (r1 * s2 - s1 * r2) / det, (c1 * r2 - r1 * c2) / det
CAP = 4 * 10**6
X = np.zeros(CAP); Y = np.zeros(CAP); M = np.zeros(CAP, np.int64); I = np.zeros(CAP, np.int64); J = np.zeros(CAP, np.int64)
def triples(n):
    k = pts(n, H, X, Y, M, I, J); assert k < CAP
    x, y, mm, ii, jj = X[:k], Y[:k], M[:k], I[:k], J[:k]
    o = np.argsort(x, kind="stable"); x, y, mm, ii, jj = x[o], y[o], mm[o], ii[o], jj[o]
    hits = []; ncand = 0
    for lag in range(1, 4):
        cl = np.nonzero((np.abs(x[lag:] - x[:-lag]) < 1e-9) & (np.abs(y[lag:] - y[:-lag]) < 1e-9) & (mm[lag:] != mm[:-lag]))[0]
        for q in cl:
            ncand += 1
            p1 = exact(n, int(mm[q]), int(ii[q]), int(jj[q])); p2 = exact(n, int(mm[q + lag]), int(ii[q + lag]), int(jj[q + lag]))
            if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) < mpmath.mpf(10) ** -40: hits.append((int(mm[q]), int(mm[q + lag])))
    return k, hits, ncand
TT, off = terms(VAR)
tot = 0; got = []; extra = 0
for n in range(3, 3 + len(TT)):
    if n > 3:
        c, h, _ = triples(n); tot += c; extra += 2 * len(h)
    got.append(tot - extra)
assert got == TT, (got[:12], TT[:12]); print("terms OK", len(TT))
bad = []; nc = 0
for n in range(N0 + 1, N + 1):
    c, h, k = triples(n); nc += k
    if h: bad.append(n); print("TRIPLE", n, h[:3], flush=True)
print("near pairs re-examined with mpmath:", nc)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[0])
