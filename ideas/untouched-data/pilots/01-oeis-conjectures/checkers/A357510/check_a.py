# A357510: a(n) = Sum_{k=0..n} k*C(n,k)^2*C(n+k,k)^2. Conjecture: a(p-1) == 0 mod p^4, primes p>=5 (checked to 499).
# Method a: exact integer sum from the definition (gmpy2).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz, next_prime
P = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def a(n):
    s = mpz(0); b1 = mpz(1); b2 = mpz(1)
    for k in range(1, n + 1):
        b1 = b1 * (n - k + 1) // k; b2 = b2 * (n + k) // k
        s += k * (b1 * b2) ** 2
    return s
T, off = terms("A357510")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = []; p = mpz(5); cnt = 0
while p < P:
    if a(int(p) - 1) % p**4: bad.append(int(p)); print("FAIL", p)
    cnt += 1; p = next_prime(p)
print("tested primes", cnt, "below", P)
print("RESULT", "holds for 5<=p<%d" % P if not bad else "COUNTEREXAMPLE p=%s" % bad)
