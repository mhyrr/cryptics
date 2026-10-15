# A361717: a(n) = Sum_{k=0..n-1} C(n-1,k)^2 C(n+k,k). Conj 1: a(p)==0 mod p^4 (p>=5). Conj 2: a(p-1)==1-2p-p^2 mod p^3 (p!=3). Both checked to 199.
# Method a: exact integer sum from the definition.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz, next_prime
P = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
def a(n):
    if n == 0: return mpz(0)
    s = mpz(0); b1 = mpz(1); b2 = mpz(1)
    for k in range(0, n):
        if k: b1 = b1 * (n - k) // k; b2 = b2 * (n + k) // k
        s += b1 * b1 * b2
    return s
T, off = terms("A361717")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
b1, b2 = [], []; p = mpz(2); cnt = 0
while p < P:
    if p >= 5 and a(p) % p**4: b1.append(int(p)); print("FAIL1", p)
    if p != 3 and (a(p - 1) - (1 - 2*p - p*p)) % p**3: b2.append(int(p)); print("FAIL2", p)
    cnt += 1; p = next_prime(p)
print("tested primes", cnt, "below", P)
print("RESULT", "holds (both) for p<%d" % P if not (b1 or b2) else "COUNTEREXAMPLE c1=%s c2=%s" % (b1, b2))
