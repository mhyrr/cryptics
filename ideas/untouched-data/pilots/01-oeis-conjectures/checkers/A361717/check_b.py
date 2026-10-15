# A361717, method b: entry's P-recurrence for exact terms (division asserted) to reproduce data;
# the congruences are evaluated by a separate modular sum mod p^4 via the alternative formula
# a(n) = Sum_{k=0..n-1} (-1)^k C(n-2,k) C(2n-2-k, n-1-k)^2 (Bala, Oct 2024) -- cross-checked against the recurrence values.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import primerange
from math import comb
P = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
a = [0, 1]
for n in range(2, P + 1):
    rhs = (55*n**3 - 187*n**2 + 190*n - 48)*a[n-1] + (n-1)*(n-3)*(5*n-2)*a[n-2]
    d = n*(n-1)*(5*n-7); q, r = divmod(rhs, d); assert r == 0, n; a.append(q)
T, off = terms("A361717")
assert a[:len(T)] == T; print("terms OK", len(T))
def alt(n): return sum((-1)**k * comb(n-2, k) * comb(2*n-2-k, n-1-k)**2 for k in range(0, n-1)) if n >= 2 else a[n]
assert all(alt(n) == a[n] for n in range(2, 60)), "alt formula mismatch"
b1, b2 = [], []; pr = list(primerange(2, P))
for p in pr:
    if p >= 5 and a[p] % p**4: b1.append(p)
    if p != 3 and (a[p-1] - (1 - 2*p - p*p)) % p**3: b2.append(p)
print("tested primes", len(pr), "below", P)
print("RESULT", "holds (both) for p<%d" % P if not (b1 or b2) else "COUNTEREXAMPLE c1=%s c2=%s" % (b1, b2))
