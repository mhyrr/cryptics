# A334886, method b: p-adic modular computation. For n=p-1, T = p*S is p-integral
# (only i=p in H(n+k) has p in the denominator); v_p(S)>=2 iff T == 0 mod p^3.
# T computed mod p^4 using modular inverses of j<p only. Terms reproduced via the PARI program translated (sympy Rational).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import Rational, binomial, primerange
P = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def H(n): return sum((Rational(1, k) for k in range(1, n + 1)), Rational(0))
def a(n): return (2 * sum(binomial(n, k)**2 * binomial(n + k, k)**2 * (H(n + k) - H(n - k)) for k in range(n + 1))).p
T, off = terms("A334886")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def Tmod(p):
    M = p ** 4; n = p - 1
    invs = {i: pow(i, -1, M) for i in range(1, 2 * p - 1) if i != p}
    tot = 0; b1 = 1; b2 = 1; hs = 0  # b1 = C(n,k) mod M, b2 = C(n+k,k) mod M
    for k in range(1, n + 1):
        b1 = b1 * (n - k + 1) % M * invs[k] % M
        b2 = b2 * (n + k) % M * invs[k] % M
        hs = (hs + invs[n - k + 1] + (invs[n + k] if n + k != p else 0)) % M  # sum 1/i, n-k<i<=n+k, i!=p
        tot = (tot + b1 * b1 % M * b2 % M * b2 % M * (1 + p * hs)) % M
    return 2 * tot % M
bad = []; cnt = 0
for p in primerange(5, P):
    t = Tmod(p); cnt += 1
    if t % p**3: bad.append(p); print("FAIL p=", p, t % p**3)
print("tested primes", cnt, "up to", P)
print("RESULT", "holds for 5<=p<%d" % P if not bad else "COUNTEREXAMPLE p=%s" % bad)
