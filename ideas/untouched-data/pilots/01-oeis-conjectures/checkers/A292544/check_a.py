"""A292544 check_a: terms h <= X of {h : 2^phi(h) == phi(h) mod h} generated structurally: h = m*2^e with m odd >= 3
(m = 1 and odd h > 1 impossible: see note), condition reduces to phi(m)*2^(e-1) == 1 mod m (phi(m) via sieve).
The reduction is re-verified on every generated term by pow(). Zumkeller test: practical numbers with even sigma are
Zumkeller (Peng & Bhaskara Rao 2013); non-practical terms fall back to a full subset-sum bitset DP.
Conjecture: every term > 1 is Zumkeller (A083207)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from sympy import factorint, divisors, totient, divisor_sigma
from oeisterms import terms
X = int(sys.argv[1]) if len(sys.argv) > 1 else 40000000

@nb.njit(cache=True)
def gen(X):
    H = X // 2
    phi = np.arange(H + 1, dtype=np.int32)
    for p in range(2, H + 1):
        if phi[p] == p:
            for j in range(p, H + 1, p): phi[j] -= phi[j] // p
    out = []
    for m in range(3, H + 1, 2):
        c = np.int64(phi[m]) % m; h = 2 * m
        while h <= X:
            if c == 1: out.append(h)
            c = 2 * c % m; h *= 2
    return out

hs = [1] + sorted(gen(X))
for h in hs: assert pow(2, int(totient(h)), h) == int(totient(h)) % h
t, off = terms('A292544'); tt = [x for x in t if x <= X]; assert hs[:len(tt)] == tt; print('terms ok', len(tt))

def practical(n):
    f = sorted(factorint(n).items()); s = 1
    for p, a in f:
        if p > 1 + s: return False
        s *= (p**(a + 1) - 1) // (p - 1)
    return True
def zum_dp(n):
    s = int(divisor_sigma(n))
    if s % 2: return False
    T = s // 2; mask = (1 << (T + 1)) - 1; r = 1
    for d in divisors(n): r = (r | (r << d)) & mask
    return (r >> T) & 1 == 1
bad = []; npr = 0
for h in hs[1:]:
    s = int(divisor_sigma(h))
    if s % 2 == 0 and practical(h): continue
    npr += 1
    if not zum_dp(h): bad.append(h)
print('X', X, 'terms (n>1) tested:', len(hs) - 1, 'largest', hs[-1], 'non-practical/odd-sigma handled by DP:', npr, 'non-Zumkeller terms:', bad)
