"""A227845 check_a: a(n) = sum_{k} sum_{j=k..n-k} C(n-k,j)^2 C(j,k)^2 (definition formula, exact) for the listed terms;
then a(p-1) mod p^2 for primes p with -2 a primitive root (A105874), using the P-recursive recurrence
n^2 a(n) = 2(3n^2-3n+1)a(n-1) - 2(3n^2-9n+7)a(n-3) + (n-2)^2 a(n-4) with denominators cleared
(x_n = a_n * prod_{i<=n} i^2), so no modular division. numba, mulmod via float quotient."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from math import comb
from sympy import primerange, n_order
from oeisterms import terms
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 10000   # number of A105874 primes

t, off = terms('A227845')
def a_def(n): return sum(comb(n-k, j)**2 * comb(j, k)**2 for k in range(n//2+1) for j in range(k, n-k+1))
assert [a_def(n) for n in range(len(t))] == t; print('terms ok', len(t))

@nb.njit(cache=True)
def mm(a, b, m):
    q = np.int64(float(a) * float(b) / float(m))
    r = a * b - q * m
    while r < 0: r += m
    while r >= m: r -= m
    return r

@nb.njit(cache=True)
def x_last(N, m):  # returns x_N mod m
    x = np.zeros(N + 1, dtype=np.int64)
    a0 = np.array([1, 2, 7, 28], dtype=np.int64)
    d = 1
    for n in range(0, min(N, 3) + 1):
        if n > 0: d = mm(d, (n * n) % m, m)
        x[n] = mm(a0[n] % m, d, m)
    for n in range(4, N + 1):
        c1 = (2 * (3 * n * n - 3 * n + 1)) % m
        c3 = (2 * (3 * n * n - 9 * n + 7)) % m
        c4 = ((n - 2) * (n - 2)) % m
        s1 = (n - 1) * (n - 1) % m; s2 = (n - 2) * (n - 2) % m; s3 = (n - 3) * (n - 3) % m
        f3 = mm(s1, s2, m); f4 = mm(f3, s3, m)
        v = mm(c1, x[n - 1], m) - mm(c3, mm(x[n - 3], f3, m), m) + mm(c4, mm(x[n - 4], f4, m), m)
        v %= m
        if v < 0: v += m
        x[n] = v
    return x[N]

# sanity: x_n/prod i^2 reproduces terms mod a large prime
from math import prod
Q = 1000003
for n in range(4, len(t)):
    assert x_last(n, Q) == t[n] * prod(i*i for i in range(1, n+1)) % Q
ps = []; p = 3
for p in primerange(3, 10**8):
    if n_order(-2 % p, p) == p - 1:
        ps.append(p)
        if len(ps) == NP: break
bad = [p for p in ps if p >= 5 and x_last(p - 1, p * p) != 0]
print('A105874 primes tested', len(ps), 'max', ps[-1], 'violations', bad[:10])
