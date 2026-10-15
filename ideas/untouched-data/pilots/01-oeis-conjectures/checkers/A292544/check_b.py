"""A292544 check_b: brute force over every h <= X: phi(h) by sieve, test pow(2, phi(h), h) == phi(h) mod h directly
(numba powmod). Zumkeller test by exact subset-sum: WLOG h itself is in one half, so need a subset of the other
divisors summing to sigma(h)/2 - h (bitset DP)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from sympy import divisors, divisor_sigma
from oeisterms import terms
X = int(sys.argv[1]) if len(sys.argv) > 1 else 40000000

@nb.njit(cache=True)
def powmod(b, e, m):
    r = 1 % m; b %= m
    while e:
        if e & 1: r = r * b % m
        b = b * b % m; e >>= 1
    return r

@nb.njit(cache=True)
def scan(X):
    phi = np.arange(X + 1, dtype=np.int32)
    for p in range(2, X + 1):
        if phi[p] == p:
            for j in range(p, X + 1, p): phi[j] -= phi[j] // p
    out = []
    for h in range(1, X + 1):
        f = np.int64(phi[h])
        if powmod(2, f, h) == f % h: out.append(h)
    return out

hs = scan(X)
t, off = terms('A292544'); tt = [x for x in t if x <= X]; assert hs[:len(tt)] == tt; print('terms ok', len(tt))
def zum(n):
    s = int(divisor_sigma(n))
    if s % 2: return False
    T = s // 2 - n
    if T < 0: return False
    mask = (1 << (T + 1)) - 1; r = 1
    for d in divisors(n)[:-1]: r = (r | (r << d)) & mask
    return (r >> T) & 1 == 1
bad = [h for h in hs[1:] if not zum(h)]
print('X', X, 'terms (n>1) tested:', len(hs) - 1, 'largest', hs[-1], 'non-Zumkeller terms:', bad)
