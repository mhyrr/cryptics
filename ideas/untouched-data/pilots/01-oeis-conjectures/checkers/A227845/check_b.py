"""A227845 check_b: terms via the alternate g.f. sum_m x^m sum_k C(m,k)^2 sum_j C(k,j)^2 x^j (series expansion);
a(p-1) = U(p-1)*U(p-2) mod p^2 using van Hoeij's 2nd-order recurrence n^2 U(n) = 2(3n^2-3n+1)U(n-2) - (n-1)^2 U(n-4),
U(-1)=1, U(0)=1, U(1)=2, U(2)=7/2, with modular inverses of 1..p-1 mod p^2 from the table iv[i]=-(m//i)iv[m%i] (inv(2) by extended Euclid). Primes with -2 primitive root
found by testing (-2)^((p-1)/q) != 1 for all prime q | p-1."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from math import comb
from fractions import Fraction
from sympy import primefactors, isprime
from oeisterms import terms
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

t, off = terms('A227845'); L = len(t)
ser = [0] * L
for m in range(L):
    for k in range(m + 1):
        for j in range(k + 1):
            if m + j < L: ser[m + j] += comb(m, k)**2 * comb(k, j)**2
assert ser == t
U = {-1: Fraction(1), 0: Fraction(1), 1: Fraction(2), 2: Fraction(7, 2)}
for n in range(3, L):
    U[n] = (2*(3*n*n-3*n+1)*U[n-2] - (n-1)**2*U[n-4]) / (n*n)
assert [U[n]*U[n-1] for n in range(L)] == t; print('terms ok', L)

@nb.njit(cache=True)
def mulmod(a, b, m):
    # schoolbook split into 16-bit chunks of b (m < 2^40 so a*2^16 < 2^56)
    r = 0; aa = a % m; bb = b % m
    while bb > 0:
        r = (r + aa * (bb & 0xFFFF)) % m
        bb >>= 16
        aa = (aa << 16) % m
    return r

@nb.njit(cache=True)
def inv(a, m):
    g0, g1, x0, x1 = m, a % m, 0, 1
    while g1:
        q = g0 // g1
        g0, g1 = g1, g0 - q * g1
        x0, x1 = x1, x0 - q * x1
    return x0 % m

@nb.njit(cache=True)
def a_pm1(p):
    m = p * p; N = p - 1
    u = np.zeros(N + 2, dtype=np.int64)  # u[i] = U(i-1)
    u[0] = 1; u[1] = 1; u[2] = 2; u[3] = mulmod(7, inv(2, m), m)
    iv = np.zeros(N + 1, dtype=np.int64); iv[1] = 1
    for i in range(2, N + 1):   # inverses mod p^2 of i < p by iv[i] = -(m//i) * iv[m % i]
        iv[i] = (m - mulmod(m // i, iv[m % i], m)) % m
    for n in range(3, N + 1):
        v = mulmod((2 * (3 * n * n - 3 * n + 1)) % m, u[n - 1], m) - mulmod(((n - 1) * (n - 1)) % m, u[n - 3], m)
        v %= m
        u[n + 1] = mulmod(v, mulmod(iv[n], iv[n], m), m)
    return mulmod(u[N + 1], u[N], m)

def neg2_primroot(p):
    return all(pow(p - 2, (p - 1) // q, p) != 1 for q in primefactors(p - 1))
ps = []; p = 3
while len(ps) < NP:
    p += 2
    if isprime(p) and neg2_primroot(p): ps.append(p)
bad = [p for p in ps if p >= 5 and a_pm1(p) != 0]
print('A105874 primes tested', len(ps), 'max', ps[-1], 'violations', bad[:10])
