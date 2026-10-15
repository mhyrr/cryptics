# A172572: a(n) = #(3n x 6) 0/1 matrices with row sums 2 and column sums n = [x1^n...x6^n] e2(x1..x6)^(3n).
# Conjecture (Bala) part 1: a(p) == 90 (mod p^2) for all primes p (checked to p=73). Part 2 not tested.
# Method a (exact): e2 = (p1^2 - p2)/2 gives
#   a(n) = N!/(2^N (n!)^6) * Sum_k (-1)^k (2N-2k)!/(N-k)! * [t^k] G(t)^6,  N=3n,  G(t)=Sum_b n!/(b!(n-2b)!) t^b,
# evaluated with python-flint exact integers; then reduced mod p^2.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from flint import fmpz_poly, fmpz
from math import factorial
from sympy import primerange
from k2common import check_terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 730
def a(n):
    N = 3 * n
    G = fmpz_poly([factorial(n) // (factorial(b) * factorial(n - 2 * b)) for b in range(n // 2 + 1)])
    G6 = G ** 6
    s = fmpz(0)
    for k in range(0, min(N, G6.degree()) + 1):
        term = factorial(2 * N - 2 * k) // factorial(N - k) * int(G6[k])
        s += -term if k % 2 else term
    num = factorial(N) * int(s); den = 2 ** N * factorial(n) ** 6
    assert num % den == 0
    return num // den
check_terms("A172572", a)
bad = []; cnt = 0
for p in primerange(2, PMAX + 1):
    r = a(p) % (p * p); cnt += 1
    if r != 90 % (p * p): bad.append((p, r))
print("primes p <=", PMAX, "tested:", cnt, "violations (p, a(p) mod p^2):", bad)
