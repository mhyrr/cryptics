# A372409: a(n) = det of [Jacobi(i-j,2n+1)]_{0<i,j<n} with the first row replaced by 1's.
# Conj 1: p=2n+1 prime: a(n)/floor((p-2)/3) = (-1)^((p+3)/4) (p==1 mod 4), (-1)^((h(-p)+1)/2) (p==3 mod 4).
# Conj 2: p>3 prime, S(p)=[J(i+j,p)]_{1<=i,j<=(p-3)/2}, T(p)=[J(i+j,p)]_{0<=i,j<=(p-3)/2}, first rows -> 1:
#         det S = -det T = 2^((p-5)/2) s(p), s(p) = (-1)^((p+3)/4) (p==1 mod 4), (-1)^((h(-p)-1)/2) (p==3 mod 4).
# NOTE: as printed, '-det T' fails already at p=5 (det S=1, det T=-2); exact dets for all p<80 give det T = -2 det S.
# We therefore test det S = 2^((p-5)/2)s(p) and det T = -2^((p-3)/2)s(p) (misprint-corrected reading).
# Both verified for primes p<2000.
# Method a: determinants modulo a 62-bit prime with python-flint nmod_mat (a mismatch mod q is a proof of failure; agreement
# is evidence, error probability ~1/q per test); h(-p) by counting reduced forms of discriminant -p (own code).
# Terms: exact integer determinants (flint fmpz_mat) for n<=len(data).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import flint
from sympy import jacobi_symbol, primerange
from math import isqrt
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2400
PMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
q = (1 << 62) - 57
_tab = {}
def J(a, m):   # Jacobi symbol; for prime m a table of squares mod m (cached), else sympy
    t = _tab.get(m)
    if t is None:
        from sympy import isprime
        if isprime(m):
            t = [-1] * m; t[0] = 0
            for x in range(1, m): t[x * x % m] = 1
        else: t = [int(jacobi_symbol(r, m)) for r in range(m)]
        _tab[m] = t
    return t[a % m]
def mat_a(n):
    m = 2 * n + 1
    return [[1] * (n - 1)] + [[J(i - j, m) for j in range(1, n)] for i in range(2, n)]
def hank(p, lo):
    hi = (p - 3) // 2
    rows = [[J(i + j, p) for j in range(lo, hi + 1)] for i in range(lo, hi + 1)]
    rows[0] = [1] * len(rows[0]); return rows
def h_neg(p):   # class number of discriminant -p (p==3 mod 4, p>3): count reduced forms (a,b,c), b^2-4ac=-p
    D = -p; h = 0
    for a in range(1, isqrt(p // 3) + 1):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a: continue
            if c == a and b < 0: continue
            h += 1
    return h
T, off = terms("A372409")
assert [int(flint.fmpz_mat(mat_a(n)).det()) if n > 1 else None for n in range(2, 2 + len(T))] == T; print("terms OK", len(T))
def detq(rows): return int(flint.nmod_mat(rows, q).det())
bad1, bad2 = [], []; cnt = 0
for p in primerange(max(5, PMIN), PMAX):
    n = (p - 1) // 2
    if p % 4 == 1: sg1 = (-1) ** ((p + 3) // 4); sg2 = sg1
    else: hh = h_neg(p); sg1 = (-1) ** ((hh + 1) // 2); sg2 = (-1) ** ((hh - 1) // 2)
    if detq(mat_a(n)) != (sg1 * ((p - 2) // 3)) % q: bad1.append(p); print("FAIL conj1", p, flush=True)
    target = sg2 * pow(2, (p - 5) // 2, q) % q
    if detq(hank(p, 1)) != target or detq(hank(p, 0)) != (-2 * target) % q: bad2.append(p); print("FAIL conj2", p, flush=True)
    cnt += 1
print("tested %d primes in [%d,%d)" % (cnt, PMIN, PMAX))
print("RESULT", "holds (mod q) for p<%d" % PMAX if not (bad1 or bad2) else "COUNTEREXAMPLE conj1 p=%s conj2 p=%s" % (bad1[:3], bad2[:3]))
