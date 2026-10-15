# A359337, method b: float64 shift-and-add convolution in numba (all terms positive, so relative rounding error per
# coefficient is <= ~n*k*eps, < 1e-10 for n<=1000), renormalised every step. A row is "unique" when the second-largest
# coefficient is < (1 - 1e-8) * max; anything closer is reported as a near-tie (undecided by this method).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
ps = np.array([prime(i) for i in range(1, N + 1)], np.int64)
@njit(cache=True)
def step(R, deg, ps, n):
    newdeg = deg + ps[n - 1]
    out = np.zeros(newdeg + 1)
    for i in range(n):
        p = ps[i]
        for j in range(deg + 1):
            out[j + p] += R[j]
    return out, newdeg
R = np.ones(1); deg = 0; rows = [[0]]; bad = []; near = []; mingap = 1.0
for n in range(1, N + 1):
    R, deg = step(R, deg, ps, n)
    m = R.max(); R /= m
    top = np.nonzero(R >= 1 - 1e-8)[0]
    if n > 40:   # exact small cases are integers in float; beyond, keep the relative gap
        srt = np.partition(R, -2)[-2]; mingap = min(mingap, 1 - srt)
    if len(top) == 1: rows.append([int(top[0])])
    else:
        exact = np.nonzero(R == 1.0)[0]
        rows.append([int(j) for j in exact])
        if n not in (2, 5, 6): near.append(n); print("NEAR-TIE", n, top)
T, off = terms("A359337")
flat = [j for r in rows for j in r]
assert flat[:len(T)] == T; print("terms OK", len(T))
print("smallest relative gap between top two coefficients for 40<n<=%d: %.3e" % (N, mingap))
print("RESULT", "holds for n<=%d" % N if not near else "UNDECIDED near-ties at n=%s" % near)
