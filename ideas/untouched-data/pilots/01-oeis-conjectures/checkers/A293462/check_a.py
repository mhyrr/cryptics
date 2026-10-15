"""A293462 check_a: for each n <= N build A_n directly (perfect-power test by integer roots), compute all eigenvalues
with LAPACK (numpy eigvalsh) and the distance to phi and 1-phi. Distances > 1e-6 => not an eigenvalue (backward error
of eigvalsh is ~1e-13 * ||A||). Near hits are tested exactly: det(A_n^2 - A_n - I) mod three primes (nonzero mod any prime => not an eigenvalue;
zero mod all three reported as confirmed)."""
import os; os.environ.setdefault("OPENBLAS_NUM_THREADS", "1"); os.environ.setdefault("OMP_NUM_THREADS", "1")
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from math import isqrt
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

def iroot(x, k):
    r = int(round(x ** (1.0 / k)))
    for c in (r - 1, r, r + 1):
        if c >= 1 and c**k == x: return True
    return False
def is_pp(x):
    if x == 1: return True
    k = 2
    while 2**k <= x:
        if iroot(x, k): return True
        k += 1
    return False
PP = np.array([is_pp(x) if x >= 1 else False for x in range(2 * N + 3)], dtype=float)
A = np.array([[PP[i + j] for j in range(1, N + 1)] for i in range(1, N + 1)])
t, off = terms('A293462'); assert [int(A[:n, :n].sum()) for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
phi = (1 + 5 ** 0.5) / 2
near = []; mind = 1e9
for n in range(1, N + 1):
    ev = np.linalg.eigvalsh(A[:n, :n])
    d = min(np.min(np.abs(ev - phi)), np.min(np.abs(ev - (1 - phi))))
    if d < 1e-4: near.append(n)
    else: mind = min(mind, d)
def detmod(M, p):
    M = M % p; n = len(M); d = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r, c]), None)
        if piv is None: return 0
        if piv != c: M[[c, piv]] = M[[piv, c]]; d = -d
        d = d * int(M[c, c]) % p; inv = pow(int(M[c, c]), -1, p)
        f = (M[c + 1:, c] * inv) % p
        M[c + 1:, c:] = (M[c + 1:, c:] - (f[:, None] * M[c, c:][None, :]) % p) % p
    return d % p
exact = []
for n in near:   # phi eigenvalue <=> det(A^2 - A - I) == 0; nonzero mod any prime disproves
    Ai = A[:n, :n].astype(np.int64); B = Ai @ Ai - Ai - np.eye(n, dtype=np.int64)
    if all(detmod(B.copy(), p) == 0 for p in (1000003, 998244353, 2147483629)): exact.append(n)
print('N', N, 'near-hits', near, 'exactly confirmed', exact, 'min distance among others %.2e' % mind)
