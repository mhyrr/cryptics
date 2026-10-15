# A350878: m such that m | s(m), s(m) = Sum over pairs (d|m, p prime) with d*p<m and d*p not dividing m of d*p.
# Conjecture: s(m) = m only for m = 5 (true for m<=15000).
# Method a: s = Dirichlet convolution id * g with g(k) = (sum of primes < k) - (sum of primes p<k with p|k),
# since for k=m/d the condition is p<k and p does not divide k. Harmonic-sum sieve in numba.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
N = int(sys.argv[1]) if len(sys.argv) > 1 else 150000
NT = int(sys.argv[2]) if len(sys.argv) > 2 else 65311881
@njit(cache=True)
def build(N):
    isp = np.ones(N + 1, np.bool_); isp[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            for j in range(i * i, N + 1, i): isp[j] = False
    sopf = np.zeros(N + 1, np.int64)
    for p in range(2, N + 1):
        if isp[p]:
            for j in range(2 * p, N + 1, p): sopf[j] += p   # primes p<k dividing k
    g = np.zeros(N + 1, np.int64); ps = 0
    for k in range(1, N + 1):
        g[k] = ps - sopf[k]        # ps = sum of primes < k
        if isp[k]: ps += k
    s = np.zeros(N + 1, np.int64)
    for d in range(1, N + 1):
        for k in range(1, N // d + 1):
            s[d * k] += d * g[k]
    return s
s = build(NT)
terms_found = [m for m in range(1, NT + 1) if s[m] % m == 0]
T, off = terms("A350878")
assert terms_found == T, (terms_found[:30], T); print("terms OK", len(T), "(all m <= %d)" % NT)
eq = [m for m in range(1, N + 1) if s[m] == m]
print("m<=%d with s(m)=m:" % N, eq)
print("RESULT", "holds for m<=%d" % N if eq == [5] else "COUNTEREXAMPLE m=%s" % eq)
