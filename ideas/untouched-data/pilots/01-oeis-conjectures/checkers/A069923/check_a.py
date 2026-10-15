# A069923: number of primes p with 2^n <= p <= 2^n + prime(n). Question/conjecture: always >= 1 (checked n<=250).
# Method a: terms by counting with sympy.isprime; conjecture via gmpy2.next_prime(2^n - 1) <= 2^n + prime(n).
# (gmpy2/GMP next_prime is a probable-prime test; a false positive could only hide a counterexample if the
#  returned value is composite, which check_b's PARI BPSW scan cross-checks.)
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
from sympy import isprime, prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
T, off = terms("A069923")
assert [sum(isprime(i) for i in range(2**n, 2**n + prime(n) + 1)) for n in range(1, len(T) + 1)] == T
print("terms OK", len(T))
from sympy import sieve
pr = list(sieve.primerange(2, 10**6))
bad = None; maxratio = (0, 0)
for n in range(1, N + 1):
    g = int(gmpy2.next_prime(gmpy2.mpz(2) ** n - 1)) - 2 ** n
    if g > pr[n - 1]: bad = n; break
    maxratio = max(maxratio, (g / pr[n - 1], n))
print("max (gap/prime(n), n):", maxratio)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
