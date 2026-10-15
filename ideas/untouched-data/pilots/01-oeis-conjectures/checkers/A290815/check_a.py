"""A290815 check_a: for m<=N compute S1 = sum_{k<=m,(k,m)=1} 1/k and S2 = sum 1/k^2 modulo m^3 / m^2 as running
fractions num/den (den coprime to m, so m^e | numerator(S) iff num == 0 mod m^e). e = largest exponent with
m^e | numerator(S1) (e>=3 re-checked exactly mod m^4 in Python); general conjecture: m^(e-1) | numerator(S2).
Also reproduces the sequence terms (m^3 | numerator(S1))."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from fractions import Fraction
from math import gcd
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

@nb.njit(cache=True)
def mm(a, b, m):
    q = np.int64(float(a) * float(b) / float(m))
    r = a * b - q * m
    while r < 0: r += m
    while r >= m: r -= m
    return r

@nb.njit(cache=True)
def sums(m, M, sq):
    mask = np.zeros(m + 1, np.uint8)
    x = m; p = 2
    while p * p <= x:
        if x % p == 0:
            for j in range(p, m + 1, p): mask[j] = 1
            while x % p == 0: x //= p
        p += 1
    if x > 1:
        for j in range(x, m + 1, x): mask[j] = 1
    num = 0; den = 1
    for k in range(1, m + 1):
        if mask[k] == 0 or m == 1:
            kk = k % M
            if sq: kk = mm(kk, kk, M)
            num = (mm(num, kk, M) + den) % M
            den = mm(den, kk, M)
    return num

@nb.njit(cache=True)
def scan(N):
    out = np.zeros((N + 1, 2), np.int64)  # e (capped at 3), S2 ok flag
    for m in range(2, N + 1):
        M3 = m * m * m
        n1 = sums(m, M3, False)
        e = 0
        if n1 % m == 0: e = 1
        if n1 % (m * m) == 0: e = 2
        if n1 == 0: e = 3
        out[m, 0] = e
        if e >= 2:
            M = m ** (e - 1)
            out[m, 1] = 1 if sums(m, M, True) == 0 else 0
        else:
            out[m, 1] = 1
    return out

out = scan(N)
seq = [1] + [m for m in range(2, N + 1) if out[m, 0] == 3]
t, off = terms('A290815'); t = [x for x in t if x <= N]; assert seq[:len(t)] == t; print('terms ok (those <= N)', len(t))
# exact re-check of e>=3 cases mod m^4 (Python big ints)
e4 = []
for m in range(2, N + 1):
    if out[m, 0] == 3:
        M = m**4; num = 0; den = 1
        for k in range(1, m + 1):
            if gcd(k, m) == 1: num = (num * k + den) % M; den = den * k % M
        if num == 0: e4.append(m)
bad = [m for m in range(2, N + 1) if out[m, 1] == 0]
print('N', N, '#terms (m^3|num)', len(seq), 'm with m^4|num:', e4, 'conjecture failures (m^(e-1) !| num(S2)):', bad[:10])
