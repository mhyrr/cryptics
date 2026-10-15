# A334886: a(n) = numerator of 2*Sum_{k=0..n} C(n,k)^2 C(n+k,k)^2 (H(n+k)-H(n-k)).
# Conjecture (Bala): a(p-1) == 0 (mod p^2) for primes p >= 5 (checked to p=499).
# Method a: exact rational arithmetic (gmpy2 mpq) straight from the definition.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpq, mpz, comb, is_prime, next_prime
P = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def S(n):
    H = [mpq(0)]
    for i in range(1, 2 * n + 1): H.append(H[-1] + mpq(1, i))
    return 2 * sum(comb(n, k) ** 2 * comb(n + k, k) ** 2 * (H[n + k] - H[n - k]) for k in range(n + 1))
T, off = terms("A334886")
assert [S(n).numerator for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = []; p = mpz(5); cnt = 0
while p < P:
    num = S(int(p) - 1).numerator
    if num % (p * p): bad.append(int(p)); print("FAIL p=", p, "num mod p^2 =", num % (p * p))
    cnt += 1; p = next_prime(p)
print("tested primes", cnt, "up to", P)
print("RESULT", "holds for 5<=p<%d" % P if not bad else "COUNTEREXAMPLE p=%s" % bad)
