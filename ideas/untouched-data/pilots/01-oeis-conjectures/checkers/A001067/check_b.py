# A001067 method b: exact numerators a(n) = numerator(B(2n)/(2n)) from flint's exact Bernoulli numbers, for
# 2n <= PMAX; for every prime p with 2n+1 < p < PMAX dividing a(n), check p^2 does not divide a(n).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import flint, gmpy2
from sympy import primerange
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A001067")
num = lambda n: int((flint.fmpq.bernoulli(2 * n) / (2 * n)).p)
assert [num(n) for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
primes = list(primerange(5, PMAX))
pairs = 0; bad = None
for n in range(1, (PMAX - 3) // 2 + 1):
    a = gmpy2.mpz(abs(num(n)))
    ps = [p for p in primes if p > 2 * n + 1]
    if not ps: break
    M = 1
    for p in ps: M *= p
    g = gmpy2.gcd(a, M)                    # product of primes in range dividing a(n)
    if g > 1:
        for p in ps:
            if g % p == 0:
                pairs += 1
                if a % (p * p) == 0: bad = (p, 2 * n); break
    if bad: break
print("irregular pairs (p, 2n) with 2n <= p-3 found:", pairs)
print("RESULT", "holds for p < %d" % PMAX if bad is None else "COUNTEREXAMPLE p=%d 2n=%d" % bad)
