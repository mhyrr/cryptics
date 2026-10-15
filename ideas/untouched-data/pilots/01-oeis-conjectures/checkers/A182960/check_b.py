# A182960 checker b: A(x^2) = F(x)F(-x), F(x) = Sum C(3n,n)/(2n+1) x^n (ternary trees, A001764), exact via flint
# fmpz_poly; b(p) = [x^p] A^p computed exactly (fmpz_poly pow_trunc, no modular reduction) then reduced mod p^3.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from math import comb
from flint import fmpz_poly
from sympy import primerange
from k2common import check_terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1010
M = PMAX + 1
F = [comb(3 * n, n) // (2 * n + 1) for n in range(2 * M + 2)]
Fp = fmpz_poly(F); Fm = fmpz_poly([(-1) ** n * x for n, x in enumerate(F)])
Q = Fp.mul_low(Fm, 2 * M + 1)
for i in range(1, 2 * M + 1, 2): assert Q[i] == 0
a = [int(Q[2 * i]) for i in range(M + 1)]
check_terms("A182960", lambda n: a[n])
A = fmpz_poly(a)
bseq = [1, 5, 215, 10463, 537287, 28435880, 1534398353, 83920389642]
for n in range(1, 8): assert int(A.pow_trunc(n, n + 1)[n]) == bseq[n]
print("b(1..7) from the %F line reproduced")
bad = []; cnt = 0
for p in primerange(5, PMAX + 1):
    r = int(fmpz_poly(a[:p + 1]).pow_trunc(p, p + 1)[p]) % p ** 3; cnt += 1
    if r != 5 % p ** 3: bad.append((p, r))
print("primes 5 <= p <=", PMAX, "tested:", cnt, "violations:", bad)
