"""A277341 check_a: a(n) = round(p^q / q^p), p = prime(n), q = prime(n+1); A058077(n) = C(q, p).
Conjecture 4: a(n+1) > a(n) iff A058077(n+1) > A058077(n), for n <= N.
a compared via double-precision logs q*ln p - p*ln q (exact rational rounding when n <= 400 or when the log gap is
< 2/min(a) + 1e-6, the only case where rounding can change the comparison); binomials compared exactly as C(q, q-p) with math.comb."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from math import log, comb, exp
from fractions import Fraction
from sympy import prime, primerange
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
ps = list(primerange(2, 2 * 10**6)); assert len(ps) > N + 3
def a_exact(n):
    p, q = ps[n - 1], ps[n]
    fr = Fraction(p**q, q**p); return int(fr + Fraction(1, 2))   # round half up (no exact halves occur)
t, off = terms('A277341'); assert [a_exact(n) for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
def la(n): p, q = ps[n - 1], ps[n]; return q * log(p) - p * log(q)
def C(n): p, q = ps[n - 1], ps[n]; return comb(q, q - p)
bad = []; exact_used = 0
for n in range(1, N + 1):
    l1, l2 = la(n), la(n + 1)
    if n <= 400 or abs(l2 - l1) < 2 * exp(-min(l1, l2)) + 1e-6:
        exact_used += 1; up_a = a_exact(n + 1) > a_exact(n)
    else:
        up_a = la(n + 1) > la(n)
    up_c = C(n + 1) > C(n)
    if up_a != up_c: bad.append(n)
print('N', N, 'violations', bad[:10], 'exact comparisons', exact_used)
