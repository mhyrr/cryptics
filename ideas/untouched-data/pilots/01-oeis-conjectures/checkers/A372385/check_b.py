# A372385, method b: same identities (see check_a.py) with PARI for the arithmetic (quadunit(p), qfbclassno(p); for p==1 mod 4
# prime the narrow and wide class numbers agree) and own numba Gaussian elimination modulo a 31-bit prime; Legendre symbols
# by Euler's criterion. Terms: PARI matdet over Z.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import primerange
import cypari2; pari = cypari2.Pari()
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2300
PMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 2001
q = 2147483629
@njit(cache=True)
def detmod(A, q):
    A = A.copy(); n = A.shape[0]; d = 1
    for c in range(n):
        piv = -1
        for r in range(c, n):
            if A[r, c] % q != 0: piv = r; break
        if piv < 0: return 0
        if piv != c:
            for k in range(n): A[c, k], A[piv, k] = A[piv, k], A[c, k]
            d = (q - d) % q
        pv = A[c, c] % q; d = d * pv % q
        inv = 1; b = pv; e = q - 2
        while e:
            if e & 1: inv = inv * b % q
            b = b * b % q; e >>= 1
        for r in range(c + 1, n):
            f = A[r, c] % q * inv % q
            if f:
                for k in range(c, n): A[r, k] = (A[r, k] - f * A[c, k]) % q
    return d
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def M(p, lo, hi, plus):
    k = hi - lo; A = np.zeros((k, k), np.int64)
    for i in range(k):
        for j in range(k): A[i, j] = leg((i + lo) + (j + lo) if plus else (i - j), p)
    return A
def lin(A):
    d0 = detmod(A, q); d1 = detmod(A + 1, q); return d0, (d1 - d0) % q
def eps_pow(p, e):   # quadunit(p)^e = u + v*w, w=(1+sqrt p)/2  ->  A + B sqrt p mod q
    z = pari.quadunit(p) ** e
    # write z = u + v*w with w = (1+sqrt(p))/2 : real(z)=u, imag(z)=v in PARI's quadratic notation
    u = int(pari.real(z)); v = int(pari.imag(z)); i2 = pow(2, -1, q)
    return (u + v * i2) % q, (v * i2) % q
T, off = terms("A372385")
got = [int(pari.matdet(pari.matrix(n - 1, n - 1, [int(pari.kronecker(i - j, 2 * n + 1)) for i in range(1, n) for j in range(1, n)]))) for n in range(2, 2 + len(T))]
assert got == T; print("terms OK", len(T))
bad = []; cnt = 0
for p in primerange(max(5, PMIN), PMAX):
    n = (p - 1) // 2; sg = 1 if (n // 2) % 2 == 0 else -1; tw = pow(2, n - 1, q)
    if p % 4 == 1:
        h = int(pari.qfbclassno(p))
        r, s = eps_pow(p, (2 - int(pari.kronecker(2, p))) * h); a, b = eps_pow(p, h)
        ok = lin(M(p, 1, n, False)) == ((r - 2 * s) % q, sg * (2 * r - p * s) % q)
        ok = ok and lin(M(p, 0, n + 1, False)) == ((-r) % q, sg * p * s % q)
        ok = ok and lin(M(p, 1, n, True)) == (sg * tw * b % q, (-sg * tw * a) % q)
        ok = ok and lin(M(p, 0, n, True)) == (sg * tw * (2 * b - a) % q, sg * tw * (p * b - 2 * a) % q)
    else:
        ok = lin(M(p, 1, n, True)) == (0, tw) and lin(M(p, 0, n, True)) == ((-tw) % q, (-2 * tw) % q)
    if not ok: bad.append(p); print("FAIL", p, flush=True)
    cnt += 1
print("tested %d primes in [%d,%d)" % (cnt, PMIN, PMAX))
print("RESULT", "holds (mod q) for p<%d" % PMAX if not bad else "COUNTEREXAMPLE p=%s" % bad[:5])
