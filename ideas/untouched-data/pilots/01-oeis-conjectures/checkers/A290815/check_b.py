"""A290815 check_b: harmonic sums over units via batch modular inversion (prefix products + one extended-Euclid
inverse per m), unit test by gcd; e = v_m(numerator S1) found by reducing S1 mod m^3 and testing m | , m^2 |, m^3 |.
Conjecture: m^(e-1) | numerator(sum' 1/k^2)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

@nb.njit(cache=True)
def mulmod(a, b, m):  # a,b < m < 2^50: quotient from float, remainder fixed up in wrapping int64
    q = np.int64(float(a) * float(b) / float(m))
    r = a * b - q * m
    while r < 0: r += m
    while r >= m: r -= m
    return r

@nb.njit(cache=True)
def egcd_inv(a, m):
    g0, g1, x0, x1 = m, a % m, 0, 1
    while g1:
        q = g0 // g1
        g0, g1 = g1, g0 - q * g1
        x0, x1 = x1, x0 - q * x1
    return x0 % m

@nb.njit(cache=True)
def gcd(a, b):
    while b: a, b = b, a % b
    return a

@nb.njit(cache=True)
def inv_sum(m, M, power):
    ks = np.empty(m, np.int64); c = 0
    for k in range(1, m + 1):
        if gcd(k, m) == 1:
            v = k % M
            if power == 2: v = mulmod(v, v, M)
            ks[c] = v; c += 1
    pre = np.empty(c + 1, np.int64); pre[0] = 1
    for i in range(c): pre[i + 1] = mulmod(pre[i], ks[i], M)
    inv = egcd_inv(pre[c], M)
    s = 0
    for i in range(c - 1, -1, -1):
        s = (s + mulmod(inv, pre[i], M)) % M     # inverse of ks[i]
        inv = mulmod(inv, ks[i], M)
    return s

@nb.njit(cache=True)
def scan(N):
    out = np.zeros((N + 1, 2), np.int64)
    for m in range(2, N + 1):
        s = inv_sum(m, m * m * m, 1)
        e = 0
        if s % m == 0: e = 1
        if s % (m * m) == 0: e = 2
        if s == 0: e = 3
        out[m, 0] = e
        out[m, 1] = 1
        if e >= 2:
            out[m, 1] = 1 if inv_sum(m, m ** (e - 1), 2) == 0 else 0
    return out

out = scan(N)
seq = [1] + [m for m in range(2, N + 1) if out[m, 0] == 3]
t, off = terms('A290815'); t = [x for x in t if x <= N]; assert seq[:len(t)] == t; print('terms ok (those <= N)', len(t))
bad = [m for m in range(2, N + 1) if out[m, 1] == 0]
print('N', N, '#terms (m^3|num)', len(seq), 'conjecture failures:', bad[:10])
