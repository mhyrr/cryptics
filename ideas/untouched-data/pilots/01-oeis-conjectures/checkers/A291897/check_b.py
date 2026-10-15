"""A291897 check_b: E(m,0) for m=2n-1 from tangent numbers, E(2n-1,0) = (-1)^n T_n / 2^(2n-1). T_n from PARI's bernvec
via T_n = (-1)^(n-1) 2^(2n)(2^(2n)-1) B_(2n)/(2n), cross-checked against the Brent-Harvey integer recurrence for
n <= 1500; alternating power sum mod m^2 in numba. Terms via sympy euler()."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
t, off = terms('A291897')
from sympy import euler
assert [euler(2 * n - 1, n).p for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
NB = 1500
T = [0] * (NB + 1); T[1] = 1
for k in range(2, NB + 1): T[k] = (k - 1) * T[k - 1]
for k in range(2, NB + 1):
    for j in range(k, NB + 1): T[j] = (j - k) * T[j - 1] + (j - k + 2) * T[j]
assert T[1:6] == [1, 2, 16, 272, 7936]
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
pari('w = bernvec(%d)' % N)
def Tn(n):
    num = int(pari('numerator(w[%d+1])' % n)); den = int(pari('denominator(w[%d+1])' % n))
    v = (-1)**(n - 1) * 2**(2*n) * (2**(2*n) - 1) * num; d = den * 2 * n
    assert v % d == 0; return v // d
assert all(Tn(n) == T[n] for n in range(1, NB + 1))

@nb.njit(cache=True)
def mm(a, b, m):
    q = np.int64(float(a) * float(b) / float(m)); r = a * b - q * m
    while r < 0: r += m
    while r >= m: r -= m
    return r
@nb.njit(cache=True)
def pw(b, e, m):
    r = 1 % m; b %= m
    while e:
        if e & 1: r = mm(r, b, m)
        b = mm(b, b, m); e >>= 1
    return r
@nb.njit(cache=True)
def altsum(n, m, M):
    s = 0
    for j in range(1, n):
        v = pw(j, m, M)
        if (n - 1 - j) % 2: s -= v
        else: s += v
        s %= M
    return s

bad = []
for n in range(1, N + 1):
    m = 2 * n - 1; M = m * m
    if M == 1: continue
    e0 = (-1)**n * (Tn(n) % M) * pow(pow(2, m, M), -1, M)
    if ((-1)**n * e0 + 2 * altsum(n, m, M)) % M: bad.append(n)
print('N', N, 'violations', bad[:10])
