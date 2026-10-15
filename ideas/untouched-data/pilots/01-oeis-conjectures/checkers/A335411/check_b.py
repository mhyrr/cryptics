# A335411/A335412, method b: coordinate geometry. Triangle (0,0),(1,0),(1/2,sqrt3/2); cevian from corner i leaves at
# direction (side to next corner) + j*pi/(3n). Intersect each corner-0 cevian with each corner-1 cevian, compute the
# direction of the point from corner 2 and test whether it is a multiple of pi/(3n) (1e-7, then confirmed with mpmath,
# 60 digits, by recomputing the intersection). V, E from the same incidence counts as method a (see check_a.py header).
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
import mpmath; mpmath.mp.dps = 60
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
@njit(cache=True)
def cand(n, out):
    th = math.pi / (3 * n); k = 0
    x2 = 0.5; y2 = math.sqrt(3) / 2
    for a in range(1, n):
        da = a * th; ca = math.cos(da); sa = math.sin(da)
        for b in range(1, n):
            db = 2 * math.pi / 3 + b * th; cb = math.cos(db); sb = math.sin(db)
            # (0,0)+s(ca,sa) = (1,0)+u(cb,sb)  ->  s*ca - u*cb = 1, s*sa - u*sb = 0
            det = -ca * sb + cb * sa
            s = (-sb) / det
            X = s * ca; Y = s * sa
            phi = math.atan2(Y - y2, X - x2) - 4 * math.pi / 3
            while phi < 0: phi += 2 * math.pi
            c = phi / th; ci = round(c)
            if abs(c - ci) < 1e-7 and 1 <= ci <= n - 1:
                out[k, 0] = a; out[k, 1] = b; out[k, 2] = ci; k += 1
    return k
buf = np.zeros((200000, 3), np.int64)
def t(n):
    k = cand(n, buf); cnt = 0; th = mpmath.pi / (3 * n)
    for a, b, c in buf[:k]:
        da = a * th; db = 2 * mpmath.pi / 3 + b * th
        ca, sa, cb, sb = mpmath.cos(da), mpmath.sin(da), mpmath.cos(db), mpmath.sin(db)
        s = (-sb) / (-ca * sb + cb * sa); X = s * ca; Y = s * sa
        phi = mpmath.atan2(Y - mpmath.sqrt(3) / 2, X - mpmath.mpf(1) / 2) - 4 * mpmath.pi / 3
        if phi < 0: phi += 2 * mpmath.pi
        if abs(phi / th - c) < mpmath.mpf(10) ** -45: cnt += 1
        else: print("float candidate rejected", n, a, b, c)
    return cnt
V = [None]; E = [None]
for n in range(1, N + 1):
    tt = t(n) if n > 1 else 0
    V.append(3 + 3 * (n - 1) + 3 * (n - 1) ** 2 - 2 * tt); E.append(3 * n + 3 * (n - 1) * (2 * n - 1) - 3 * tt)
TV, _ = terms("A335411"); TE, _ = terms("A335412")
assert V[1:1 + len(TV)] == TV and E[1:1 + len(TE)] == TE; print("terms OK", len(TV), len(TE))
def rec_bad(a):
    return [n for n in range(14, N + 1) if a[n] != a[n-1] + a[n-2] - a[n-3] + a[n-10] - a[n-11] - a[n-12] + a[n-13]]
bv, be = rec_bad(V), rec_bad(E)
print("A335411 recurrence failures:", bv[:10]); print("A335412 recurrence failures:", be[:10])
fa = os.path.join(os.path.dirname(__file__), "VE_a.txt")
if os.path.exists(fa):
    mine = "\n".join("%d %d %d" % (n, V[n], E[n]) for n in range(1, N + 1))
    print("identical V,E to method a:", open(fa).read() == mine)
print("RESULT", "holds for 13<n<=%d (both)" % N if not (bv or be) else "COUNTEREXAMPLE V n=%s E n=%s" % (bv[:3], be[:3]))
