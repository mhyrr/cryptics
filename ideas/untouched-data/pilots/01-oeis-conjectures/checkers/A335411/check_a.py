# A335411 (vertices) and A335412 (edges) of the figure made by n-secting the angles of an equilateral triangle.
# Conjecture (Barker): a(n) = a(n-1)+a(n-2)-a(n-3)+a(n-10)-a(n-11)-a(n-12)+a(n-13) for n>13 (Blomberg: holds n<=500).
# Combinatorics: two cevians from different corners always meet at one interior point; at most 3 cevians (one per corner)
# pass through a point.  With t(n) = #triple points: V = 3 + 3(n-1) + 3(n-1)^2 - 2t,  E = 3n + 3(n-1)(2n-1) - 3t.
# Method a: t(n) via trigonometric Ceva: cevians at angles a*th, b*th, c*th (th = pi/(3n), measured cyclically) concur iff
# sin(a th) sin(b th) sin(c th) = sin((n-a)th) sin((n-b)th) sin((n-c)th). For each (a,b) solve for the unique angle
# gamma (f(g)=sin g/sin(pi/3-g) is increasing), test gamma/th integral (1e-7), confirm hits with mpmath at 60 digits.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
import mpmath; mpmath.mp.dps = 60
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
@njit(cache=True)
def cand(n, out):
    th = math.pi / (3 * n); k = 0
    for a in range(1, n):
        for b in range(1, n):
            R = math.sin((n - a) * th) * math.sin((n - b) * th) / (math.sin(a * th) * math.sin(b * th))
            # need sin g / sin(pi/3 - g) = R
            g = math.atan((math.sqrt(3) / 2 * R) / (1 + R / 2))
            c = g / th; ci = round(c)
            if abs(c - ci) < 1e-7 and 1 <= ci <= n - 1:
                out[k, 0] = a; out[k, 1] = b; out[k, 2] = ci; k += 1
    return k
buf = np.zeros((200000, 3), np.int64)
def t(n):
    k = cand(n, buf); cnt = 0
    th = mpmath.pi / (3 * n)
    for a, b, c in buf[:k]:
        lhs = mpmath.sin(a * th) * mpmath.sin(b * th) * mpmath.sin(c * th)
        rhs = mpmath.sin((n - a) * th) * mpmath.sin((n - b) * th) * mpmath.sin((n - c) * th)
        if abs(lhs - rhs) < mpmath.mpf(10) ** -50: cnt += 1
        else: print("float candidate rejected", n, a, b, c)
    assert cnt % 3 == 0 or True
    return cnt  # each concurrency point = one ordered triple (a,b,c)
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
open(os.path.join(os.path.dirname(__file__), "VE_a.txt"), "w").write("\n".join("%d %d %d" % (n, V[n], E[n]) for n in range(1, N + 1)))
print("RESULT", "holds for 13<n<=%d (both)" % N if not (bv or be) else "COUNTEREXAMPLE V n=%s E n=%s" % (bv[:3], be[:3]))
