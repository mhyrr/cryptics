# A172572 checker b: variable-elimination DP. With e1=e1'+x, e2=e2'+x*e1',
#   f_m(a,b) := [x1^n..xm^n] e1^a e2^b = Sum_j C(a,n-j) C(b,j) f_{m-1}(a-n+2j, b-j),  f_0 = [a=b=0],
# and a(n) = f_6(0,3n). Since a+2b = m*n the state is b alone. Exact (Python ints) for the data terms,
# mod p^2 (numba, int64) for the congruence test.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, numba
from math import comb
from sympy import primerange
from k2common import check_terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 730
def exact(n):
    f = {0: 1}                         # level 0: b=0 (a=0)
    for m in range(1, 7):
        g = {}
        for b in range(0, m * n // 2 + 1):
            a = m * n - 2 * b
            s = 0
            for j in range(0, n + 1):
                a2, b2 = a - n + 2 * j, b - j
                if b2 < 0 or a2 < 0 or n - j > a: continue
                v = f.get(b2, 0)
                if v: s += comb(a, n - j) * comb(b, j) * v
            g[b] = s
        f = g
    return f[3 * n]
check_terms("A172572", exact)
@numba.njit(cache=True)
def modp2(n, M):
    A = 6 * n
    C = np.zeros((A + 1, n + 1), dtype=np.int64)
    for a in range(A + 1):
        C[a, 0] = 1
        for i in range(1, min(a, n) + 1):
            C[a, i] = (C[a - 1, i - 1] + (C[a - 1, i] if i <= a - 1 else 0)) % M
    f = np.zeros(3 * n + 1, dtype=np.int64); f[0] = 1
    for m in range(1, 7):
        g = np.zeros(3 * n + 1, dtype=np.int64)
        for b in range(0, m * n // 2 + 1):
            a = m * n - 2 * b
            s = 0
            for j in range(0, n + 1):
                a2 = a - n + 2 * j; b2 = b - j
                if b2 < 0 or a2 < 0 or n - j > a or b2 > (m - 1) * n // 2: continue
                if (m - 1) * n - 2 * b2 != a2: continue
                if j > b: continue
                s = (s + C[a, n - j] * (C[b, j] if j <= n else 0) % M * f[b2]) % M
            g[b] = s
        f = g
    return f[3 * n]
for n in range(1, 8): assert modp2(n, 10 ** 9 + 7) == exact(n) % (10 ** 9 + 7)
bad = []; cnt = 0
for p in primerange(2, PMAX + 1):
    r = modp2(p, p * p); cnt += 1
    if r != 90 % (p * p): bad.append((p, int(r)))
print("primes p <=", PMAX, "tested:", cnt, "violations (p, a(p) mod p^2):", bad)
