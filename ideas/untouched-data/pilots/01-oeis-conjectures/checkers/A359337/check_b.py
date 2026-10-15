# A359337, method b: float64 shift-and-add convolution in numba (all terms positive, so relative rounding error per
# coefficient is <= ~n*k*eps, < 1e-10 for n<=1000). While coefficients are < 2^50 they are exact integers (exact ties);
# afterwards renormalised each step, a row is "unique" when the second-largest coefficient is < (1 - 1e-8) * max;
# anything closer is resolved by running the same product modulo 2^61-1 (different residues => the integers differ) and
# trusting the float order when the relative gap exceeds 1e-11; otherwise undecided.
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
Q = (1 << 61) - 1
@njit(cache=True)
def stepq(Rq, deg, ps, n, q):
    out = np.zeros(deg + ps[n - 1] + 1, np.int64)
    for i in range(n):
        p = ps[i]
        for j in range(deg + 1):
            v = out[j + p] + Rq[j]
            out[j + p] = v - q if v >= q else v
    return out
Rq = np.ones(1, np.int64); undecided = []; ties = []
R = np.ones(1); deg = 0; rows = [[0]]; near = []; mingap = 1.0; scaled = False
for n in range(1, N + 1):
    Rq = stepq(Rq, deg, ps, n, Q)
    R, deg = step(R, deg, ps, n)
    m = R.max()
    if m > 2.0 ** 50 or scaled:          # values are exact integers in float64 until we start rescaling
        R /= m; scaled = True; m = 1.0
    top = np.nonzero(R >= m * (1 - 1e-8))[0]
    if scaled:
        srt = np.partition(R, -2)[-2]; mingap = min(mingap, 1 - srt / m)
        jm = int(np.argmax(R))
        if len(top) > 1:
            # exact check of each candidate against the float argmax: different residues mod 2^61-1 => different integers;
            # then the float order is trustworthy if the relative gap exceeds 1e-11 (accumulated error <= n^2/2 * eps ~ 1e-11 at n=400)
            for j in top:
                if j == jm: continue
                if Rq[j] == Rq[jm]: undecided.append(n); print("EQUAL MOD Q (possible tie)", n, j, jm); continue
                if (R[jm] - R[j]) / m < 1e-11: undecided.append(n); print("UNRESOLVED", n, j, jm)
            near.append(n)
        rows.append([jm])
    else:
        rows.append([int(j) for j in np.nonzero(R == m)[0]])
        if len(rows[-1]) > 1 and n not in (2, 5, 6): ties.append(n); print("EXACT TIE", n, rows[-1])
T, off = terms("A359337")
flat = [j for r in rows for j in r]
assert flat[:len(T)] == T, (rows[:12], T[:15]); print("terms OK", len(T))
print("smallest relative gap between the top two coefficients after rescaling began: %.3e" % mingap)
print("near-ties resolved by exact residue + float order:", len(near))
print("RESULT", ("holds for n<=%d" % N if not undecided else "UNDECIDED n=%s" % undecided) if not ties else "COUNTEREXAMPLE n=%s" % ties)
