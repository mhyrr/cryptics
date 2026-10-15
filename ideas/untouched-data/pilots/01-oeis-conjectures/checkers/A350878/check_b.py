# A350878, method b: per m, enumerate divisors d by trial division, and for each d sum d*p over primes p < m/d
# (prefix sums of primes) minus d*p for primes p | (m/d), p < m/d (direct, not convolution).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
N = int(sys.argv[1]) if len(sys.argv) > 1 else 150000
@njit(cache=True)
def term(m, dd, PS):
    k = m // dd; t = PS[k]; kk = k; p = 2
    while p * p <= kk:
        if kk % p == 0:
            if p < k: t -= p
            while kk % p == 0: kk //= p
        p += 1
    if kk > 1 and kk < k: t -= kk
    return dd * t
@njit(cache=True)
def sall(N):
    isp = np.ones(N + 1, np.bool_); isp[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            for j in range(i * i, N + 1, i): isp[j] = False
    PS = np.zeros(N + 2, np.int64)   # PS[k] = sum of primes < k
    for k in range(1, N + 2): PS[k] = PS[k - 1] + ((k - 1) if isp[k - 1] else 0)
    out = np.zeros(N + 1, np.int64)
    for m in range(1, N + 1):
        tot = 0; d = 1
        while d * d <= m:
            if m % d == 0:
                tot += term(m, d, PS)
                if d != m // d: tot += term(m, m // d, PS)
            d += 1
        out[m] = tot
    return out
s = sall(N)
T, off = terms("A350878")
found = [m for m in range(1, N + 1) if s[m] % m == 0]
assert found == [t for t in T if t <= N], found; print("terms OK", len(found), "(terms <= %d)" % N)
eq = [m for m in range(1, N + 1) if s[m] == m]
print("m<=%d with s(m)=m:" % N, eq)
print("RESULT", "holds for m<=%d" % N if eq == [5] else "COUNTEREXAMPLE m=%s" % eq)
