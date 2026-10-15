# A396804: e.g.f. A(x) = x*exp(A^4(x)), A^k = k-th functional iterate. Conjecture (Asaria): a(n) mod 3 = [1,2,0,1,1,0] repeating
# for n>=1 (holds through n=201).
# Method a: Manyama's recurrence a(1,k)=1, a(n,k) = 1/(n-1) Sum_{i=1..n-1} i*C(n,i)*a(n-i,k)*Sum_{j=1..k} a(i,j+3),
# computed mod many 31-bit primes in numba, then exact a(n) by CRT (product of primes > 10^(1.6*log10(n!*8^n)+30); the
# reconstruction is required to be unchanged when the last 4 primes are dropped).
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
    a = np.zeros((N + 1, K + 1), np.int64)     # a[m, k]
    S = np.zeros((N + 1, K + 1), np.int64)     # S[i, k] = sum_{j=1..k} a[i, j+3]
    C = np.zeros((N + 1, N + 1), np.int64)
    for n in range(N + 1):
        C[n, 0] = 1
        for i in range(1, n + 1): C[n, i] = (C[n - 1, i - 1] + (C[n - 1, i] if i <= n - 1 else 0)) % p
    for k in range(1, K + 1): a[1, k] = 1
    for n in range(1, N + 1):
        Kn = 1 + 3 * (N - n)
        if n >= 2:
            inv = pw(n - 1, p - 2, p)
            for k in range(1, Kn + 1):
                s = 0
                for i in range(1, n):
                    s = (s + i * C[n, i] % p * a[n - i, k] % p * S[i, k]) % p
                a[n, k] = s * inv % p
        # prefix sums for this level, needed by higher levels with k up to K(level)-3
        acc = 0
        for k in range(1, Kn - 2):
            acc = (acc + a[n, k + 3]) % p; S[n, k] = acc
    return a[:, 1].copy()
T, off = terms("A396804")
digits = EXTRA * (math.lgamma(N + 1) / math.log(10) + N * math.log10(8)) + 30
primes = []; P = mpz(1); q = 2**31
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
assert all(v > 0 for v in vals[1:])
pat = [1, 2, 0, 1, 1, 0]
bad = [n for n in range(1, N + 1) if vals[n] % 3 != pat[(n - 1) % 6]]
print("digits of a(N):", len(str(vals[N])), " log10(a(N)/N!) per n: %.3f" % ((math.log10(vals[N]) - math.lgamma(N + 1) / math.log(10)) / N), " CRT bound digits", int(digits))
print("other entry conjectures: odd iff n odd:", all((vals[n] % 2 == 1) == (n % 2 == 1) for n in range(1, N + 1)),
      " mod4 [1,2,3,0]:", all(vals[n] % 4 == [1, 2, 3, 0][(n - 1) % 4] for n in range(1, N + 1)),
      " mod5 never 3:", all(vals[n] % 5 != 3 for n in range(1, N + 1)))
open(os.path.join(os.path.dirname(__file__), "mod_a.txt"), "w").write(" ".join("%d:%d,%d,%d" % (n, vals[n] % 3, vals[n] % 4, vals[n] % 5) for n in range(1, N + 1)))
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s a(n) mod 3=%d" % (bad[0], vals[bad[0]] % 3))
