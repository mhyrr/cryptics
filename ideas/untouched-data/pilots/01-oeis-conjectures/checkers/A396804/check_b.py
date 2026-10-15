# A396804, method b: functional equation (1.e) A^k = A^(k-1) * exp(A^(k+3)) on ordinary coefficients mod p:
# c_0 = x; e = exp(c_{k+3}) via n*e_n = Sum i*g_i*e_{n-i}; c_k = c_{k-1} * e. Then a(n) = n! * c_1[n] mod p,
# exact a(n) by CRT over 30-bit primes (a different prime set from method a).
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import prevprime
from gmpy2 import mpz
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
EXTRA = float(os.environ.get("EXTRA", "1.6"))
@njit(cache=True)
def pw(b, e, p):
    r = 1; b %= p
    while e:
        if e & 1: r = r * b % p
        b = b * b % p; e >>= 1
    return r
@njit(cache=True)
def run(N, p):
    K = 1 + 3 * (N - 1) + 4
    c = np.zeros((K + 1, N + 1), np.int64)    # c[k, n] = [x^n] A^k
    e = np.zeros((K + 1, N + 1), np.int64)    # e[k, n] = [x^n] exp(A^(k+3))
    inv = np.zeros(N + 2, np.int64)
    for i in range(1, N + 2): inv[i] = pw(i, p - 2, p)
    for k in range(K + 1): c[k, 1] = 1; e[k, 0] = 1
    c[0, 1] = 1
    for n in range(2, N + 1):
        Kn = 1 + 3 * (N - n)
        for k in range(1, Kn + 1):
            # e[k, n-1] from c[k+3, 1..n-1]
            m = n - 1; s = 0
            for i in range(1, m + 1): s = (s + i * c[k + 3, i] % p * e[k, m - i]) % p
            e[k, m] = s * inv[m] % p
            # c[k, n] = sum_{i=1..n} c[k-1, i] * e[k, n-i]
            s = 0
            for i in range(1, n + 1): s = (s + c[k - 1, i] * e[k, n - i]) % p
            c[k, n] = s
    out = np.zeros(N + 1, np.int64); f = 1
    for n in range(1, N + 1):
        f = f * n % p; out[n] = f * c[1, n] % p
    return out
T, off = terms("A396804")
digits = EXTRA * (math.lgamma(N + 1) / math.log(10) + N * math.log10(8)) + 30
primes = []; P = mpz(1); q = 2**30
while P < mpz(10) ** int(digits + 1):
    q = prevprime(q); primes.append(q); P *= q
res = [run(N, p) for p in primes]
def crt(ps, rs):
    out = [0] * (N + 1)
    for n in range(1, N + 1):
        x = mpz(0); M = mpz(1)
        for p, r in zip(ps, rs):
            t = (int(r[n]) - x) * pow(int(M % p), -1, p) % p
            x += M * t; M *= p
        out[n] = int(x if x <= M // 2 else x - M)
    return out
vals = crt(primes, res)
# stability: the same reconstruction from all but the last 4 primes must agree (else the bound was too small)
assert crt(primes[:-4], res[:-4]) == vals, "CRT not stable: raise EXTRA"
assert vals[1:1 + len(T)] == T; print("terms OK", len(T), "primes used", len(primes))
pat = [1, 2, 0, 1, 1, 0]
bad = [n for n in range(1, N + 1) if vals[n] % 3 != pat[(n - 1) % 6]]
other = os.path.join(os.path.dirname(__file__), "mod_a.txt")
if os.path.exists(other):
    mine = " ".join("%d:%d,%d,%d" % (n, vals[n] % 3, vals[n] % 4, vals[n] % 5) for n in range(1, N + 1))
    print("residues identical to method a's file:", open(other).read() == mine)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s a(n) mod 3=%d" % (bad[0], vals[bad[0]] % 3))
