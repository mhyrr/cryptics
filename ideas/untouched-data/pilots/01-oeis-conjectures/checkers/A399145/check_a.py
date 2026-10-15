# A399145 (vertex-aligned, vertices at 2*pi*j/m) and A399147 (side-midpoint-aligned, vertices at 2*pi*(j+1/2)/m):
# regular polygons P_3..P_n inscribed in one circle. Conjecture: no three sides of distinct polygons meet at a proper
# crossing point (verified n<=1000), so a(n) = #pairwise proper crossings.
# Method a: incremental. A triple point whose largest polygon is P_n lies on a side s of P_n. Each side s of P_n (arc of
# length 2pi/n) is crossed by P_m (m<n) exactly at the two sides of P_m incident to the (at most one) vertex of P_m strictly
# inside the arc of s. Positions along s are sorted per side; neighbours (lag<=3) closer than 1e-5 side lengths are recomputed in
# long double, and those within 1e-8 decided with mpmath (50 digits): a triple point only if equal to 1e-40.
# Usage: check_a.py N [N0] [variant]   tests n in (N0, N]; terms reproduced from n=3..len(terms).
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
import mpmath; mpmath.mp.dps = 50
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1400
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
VAR = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(os.path.dirname(os.path.abspath(__file__)))
OFF = {"A399145": 0.0, "A399147": 0.5}[VAR]
def crossings(n):
    """for P_n vs all P_m, m<n: arrays side index of P_n, parameter t along that side, m, vertex index of P_m."""
    S = []; Tt = []; Ms = []; Vs = []
    for m in range(3, n):
        j = np.arange(m)
        ang = 2 * np.pi * (j + OFF) / m
        u = ang / (2 * np.pi / n) - OFF          # position in units of P_n sides
        s = np.floor(u).astype(np.int64)
        frac = u - s
        inside = (frac > 1e-9) & (frac < 1 - 1e-9)   # vertices of P_m strictly inside an arc of P_n
        # exact check of shared vertices: (j+OFF)/m == (i+OFF)/n  <=>  n*(2j+2OFF) == m*(2i+2OFF) handled by tolerance;
        # with integer arithmetic: shared iff n*(2j+2*OFF) is divisible by m and the quotient has the right parity
        jj = j[inside]; ss = s[inside] % n
        for nb in (-1, 1):
            S.append(ss); Ms.append(np.full(len(jj), m)); Vs.append(jj * 2 + (nb > 0))
            # chord of P_m from vertex jj to jj+nb, chord of P_n side ss: compute parameter t along side ss
            a1 = 2 * np.pi * (ss + OFF) / n; a2 = 2 * np.pi * (ss + 1 + OFF) / n
            b1 = 2 * np.pi * (jj + OFF) / m; b2 = 2 * np.pi * (jj + nb + OFF) / m
            P1 = np.stack([np.cos(a1), np.sin(a1)]); P2 = np.stack([np.cos(a2), np.sin(a2)])
            Q1 = np.stack([np.cos(b1), np.sin(b1)]); Q2 = np.stack([np.cos(b2), np.sin(b2)])
            d1 = P2 - P1; d2 = Q2 - Q1; w = Q1 - P1
            den = d1[0] * d2[1] - d1[1] * d2[0]
            t = (w[0] * d2[1] - w[1] * d2[0]) / den
            Tt.append(t)
    return np.concatenate(S), np.concatenate(Tt), np.concatenate(Ms), np.concatenate(Vs)
def exact_t(n, s, m, v):
    jj, nb = v // 2, (1 if v % 2 else -1)
    a1 = 2 * mpmath.pi * (s + OFF) / n; a2 = 2 * mpmath.pi * (s + 1 + OFF) / n
    b1 = 2 * mpmath.pi * (jj + OFF) / m; b2 = 2 * mpmath.pi * (jj + nb + OFF) / m
    p1 = (mpmath.cos(a1), mpmath.sin(a1)); p2 = (mpmath.cos(a2), mpmath.sin(a2))
    q1 = (mpmath.cos(b1), mpmath.sin(b1)); q2 = (mpmath.cos(b2), mpmath.sin(b2))
    d1 = (p2[0]-p1[0], p2[1]-p1[1]); d2 = (q2[0]-q1[0], q2[1]-q1[1]); w = (q1[0]-p1[0], q1[1]-p1[1])
    return (w[0]*d2[1] - w[1]*d2[0]) / (d1[0]*d2[1] - d1[1]*d2[0])
PI_LD = 4 * np.arctan(np.longdouble(1))
def t_ld(n, s, m, v):   # vectorised recomputation in 80-bit long double
    s = s.astype(np.longdouble); m = m.astype(np.longdouble); jj = (v // 2).astype(np.longdouble); nb = np.where(v % 2 == 1, 1, -1).astype(np.longdouble)
    off = np.longdouble(OFF); nn = np.longdouble(n)
    a1 = 2 * PI_LD * (s + off) / nn; a2 = 2 * PI_LD * (s + 1 + off) / nn
    b1 = 2 * PI_LD * (jj + off) / m; b2 = 2 * PI_LD * (jj + nb + off) / m
    p1x, p1y, p2x, p2y = np.cos(a1), np.sin(a1), np.cos(a2), np.sin(a2)
    q1x, q1y, q2x, q2y = np.cos(b1), np.sin(b1), np.cos(b2), np.sin(b2)
    d1x, d1y, d2x, d2y = p2x - p1x, p2y - p1y, q2x - q1x, q2y - q1y; wx, wy = q1x - p1x, q1y - p1y
    return (wx * d2y - wy * d2x) / (d1x * d2y - d1y * d2x)
def triples(n):
    # float64 error of t is < ~3e-7 (side directions of P_n, P_m differ by >= pi/(nm)); screen at 1e-5, refine in long double
    # (error < ~1e-10) at 1e-8, then decide with mpmath at 50 digits.
    S, Tt, Ms, Vs = crossings(n)
    assert np.all((Tt > 0) & (Tt < 1))
    o = np.lexsort((Tt, S)); S, Tt, Ms, Vs = S[o], Tt[o], Ms[o], Vs[o]
    hits = []; ncand = 0
    for lag in (1, 2, 3):
        cl = np.nonzero((S[lag:] == S[:-lag]) & (np.abs(Tt[lag:] - Tt[:-lag]) < 1e-5) & (Ms[lag:] != Ms[:-lag]))[0]
        if len(cl) == 0: continue
        ta = t_ld(n, S[cl], Ms[cl], Vs[cl]); tb = t_ld(n, S[cl + lag], Ms[cl + lag], Vs[cl + lag])
        for i in cl[np.abs(ta - tb) < 1e-8]:
            ncand += 1
            if abs(exact_t(n, int(S[i]), int(Ms[i]), int(Vs[i])) - exact_t(n, int(S[i + lag]), int(Ms[i + lag]), int(Vs[i + lag]))) < mpmath.mpf(10) ** -40:
                hits.append((int(S[i]), int(Ms[i]), int(Ms[i + lag])))
    return len(S), hits, ncand
TT, off = terms(VAR)
tot = 0; got = []; extra = 0
for n in range(3, 3 + len(TT)):
    if n > 3:
        c, h, _ = triples(n); tot += c; extra += 2 * len(h)
    got.append(tot - extra)   # a triple point = 3 pair crossings, 1 point
assert got == TT, (got[:12], TT[:12]); print("terms OK", len(TT))
bad = []; nclose = 0
for n in range(N0 + 1, N + 1):
    c, h, k = triples(n); nclose += k
    if h: bad.append((n, h[:3])); print("TRIPLE", n, h[:3], flush=True)
print("near pairs sent to mpmath:", nclose)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[0][0])
