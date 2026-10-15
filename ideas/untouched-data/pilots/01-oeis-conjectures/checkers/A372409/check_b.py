# A372409, method b: own Gaussian elimination modulo a 31-bit prime (numba), Legendre symbols by Euler's criterion,
# h(-p) from PARI qfbclassno. Same statements as check_a.py. Terms: PARI matdet over Z.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import primerange
import cypari2; pari = cypari2.Pari()
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2400
PMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
q = 2147483629   # prime < 2^31
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
        # inverse by Fermat
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
def jac(a, m): return int(pari.kronecker(a, m))
def mat_a(n, sym):
    m = 2 * n + 1; A = np.zeros((n - 1, n - 1), np.int64); A[0, :] = 1
    for i in range(2, n):
        for j in range(1, n): A[i - 1, j - 1] = sym(i - j, m)
    return A
def hank(p, lo):
    hi = (p - 3) // 2; k = hi - lo + 1; A = np.zeros((k, k), np.int64)
    for i in range(k):
        for j in range(k): A[i, j] = leg(i + j + 2 * lo, p)
    A[0, :] = 1; return A
T, off = terms("A372409")
assert [int(pari.matdet(pari.matrix(n - 1, n - 1, [int(v) for v in mat_a(n, jac).flatten()]))) for n in range(2, 2 + len(T))] == T; print("terms OK", len(T))
bad1, bad2 = [], []; cnt = 0
for p in primerange(max(5, PMIN), PMAX):
    n = (p - 1) // 2
    if p % 4 == 1: sg1 = (-1) ** ((p + 3) // 4); sg2 = sg1
    else: hh = int(pari.qfbclassno(-p)); sg1 = (-1) ** ((hh + 1) // 2); sg2 = (-1) ** ((hh - 1) // 2)
    if detmod(mat_a(n, leg), q) != (sg1 * ((p - 2) // 3)) % q: bad1.append(p); print("FAIL conj1", p, flush=True)
    target = sg2 * pow(2, (p - 5) // 2, q) % q
    if detmod(hank(p, 1), q) != target or detmod(hank(p, 0), q) != (-target) % q: bad2.append(p); print("FAIL conj2", p, flush=True)
    cnt += 1
print("tested %d primes in [%d,%d)" % (cnt, PMIN, PMAX))
print("RESULT", "holds (mod q) for p<%d" % PMAX if not (bad1 or bad2) else "COUNTEREXAMPLE conj1 p=%s conj2 p=%s" % (bad1[:3], bad2[:3]))
