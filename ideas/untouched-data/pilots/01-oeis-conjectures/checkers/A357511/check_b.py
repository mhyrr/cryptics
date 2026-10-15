# A357511, method b: denominators k<=p-1 are prime to p, so v_p(numerator) = v_p(sum);
# compute the sum mod p^4 with modular inverses. Terms reproduced with the PARI program translated (sympy).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import binomial, Rational, primerange
P = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def a(n): return sum((binomial(n,k)**2*binomial(n+k,k)**2/Rational(k) for k in range(1, n+1)), Rational(0)).p if n else 0
T, off = terms("A357511")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def smod(p):
    M = p**4; n = p - 1; s = 0; b1 = 1; b2 = 1
    for k in range(1, n + 1):
        ik = pow(k, -1, M)
        b1 = b1 * (n - k + 1) % M * ik % M; b2 = b2 * (n + k) % M * ik % M
        s = (s + b1 * b1 % M * b2 % M * b2 % M * ik) % M
    return s
pr = list(primerange(7, P)); bad = [p for p in pr if smod(p)]
print("tested primes", len(pr), "below", P)
print("RESULT", "holds for 7<=p<%d" % P if not bad else "COUNTEREXAMPLE p=%s" % bad)
