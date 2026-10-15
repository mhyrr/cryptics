# A047211 method b: modular certificates. Reducible side: exact det(M -/+ I) == 0 (flint fmpz_mat.det), i.e. +-1 is
# an eigenvalue. Irreducible side: charpoly mod several word primes (nmod_mat), factor degree patterns mod each
# squarefree prime; integer factor degrees must be subset sums of every pattern, so if the intersection of the
# subset-sum sets over primes contains nothing in [1, n-1], the charpoly is irreducible over Q.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import flint
START = int(sys.argv[1]) if len(sys.argv) > 1 else 2
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1770
T, off = terms("A047211")
assert [n for n in range(1, T[-1] + 1) if n % 5 in (2, 4)] == T; print("terms OK", len(T))
def rows(n): return [[1 if (c >= n + 1 - r or c == n - 1 - r) else 0 for c in range(1, n + 1)] for r in range(1, n + 1)]
from sympy import nextprime
PR = [1000003]
while len(PR) < 60: PR.append(nextprime(PR[-1]))
def irreducible_cert(n):
    R = rows(n); flat = [x for r in R for x in r]; allowed = (1 << (n + 1)) - 1
    for p in PR:
        cp = flint.nmod_mat(n, n, flat, p).charpoly()
        if cp.gcd(cp.derivative()).degree() > 0: continue
        sums = 1
        for g, e in cp.factor()[1]:
            for _ in range(e): sums |= sums << g.degree()
        allowed &= sums
        if allowed & ~1 & ~(1 << n) == 0: return True
    return False
def has_pm1_root(n):
    m = flint.fmpz_mat(rows(n)); I = flint.fmpz_mat([[int(i == j) for j in range(n)] for i in range(n)])
    return (m - I).det() == 0 or (m + I).det() == 0
bad = None; inconclusive = []
for n in range(START, N + 1):
    if n % 5 in (2, 4):
        if has_pm1_root(n): bad = n; break
        if not irreducible_cert(n): inconclusive.append(n)
    else:
        if not has_pm1_root(n): inconclusive.append(n)
print("inconclusive n:", inconclusive)
print("RESULT", ("holds to %d" % N if not inconclusive else "holds except inconclusive") if bad is None else "COUNTEREXAMPLE n=%d" % bad)
