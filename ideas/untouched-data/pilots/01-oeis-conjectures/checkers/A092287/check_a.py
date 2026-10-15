# A092287: a(n) = prod_{j,k<=n} gcd(j,k). Conjecture (Kaydalov): f(n,m) = prod_{j<=n,k<=m} gcd(j,k) has
# v_p(f(n,m)) = sum_i floor(n/p^i)*floor(m/p^i).  Method a: numpy grid of v_p(gcd(j,k)) computed with math.gcd
# on multiples of p only, 2-D cumulative sum, compare against the formula for all 1<=m<=n<=N.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from math import gcd, prod
import numpy as np
from sympy import primerange
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
T, off = terms("A092287")
f = lambda n, m: prod(gcd(j, k) for j in range(1, n + 1) for k in range(1, m + 1))
assert [f(n, n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def vp(x, p):
    c = 0
    while x % p == 0: x //= p; c += 1
    return c
bad = None
for p in primerange(2, N + 1):
    K = N // p
    g = np.zeros((K + 1, K + 1), np.int64)
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            g[a, b] = vp(gcd(a * p, b * p), p)
    C = g.cumsum(0).cumsum(1)
    n = np.arange(N + 1)
    form = np.zeros((N + 1, N + 1), np.int64); q = p
    while q <= N:
        form += np.outer(n // q, n // q); q *= p
    V = C[n // p][:, n // p]          # v_p(f(n,m)) = sum over multiples of p
    diff = np.argwhere(np.tril(V != form)[1:, 1:])
    if len(diff): bad = (p, tuple(diff[0] + 1)); break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE %s" % (bad,))
