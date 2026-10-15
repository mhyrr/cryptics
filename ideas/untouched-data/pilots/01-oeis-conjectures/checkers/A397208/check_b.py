# A397208, method b: enumerate r prime with p/4 < r < p/2 and test q = 4r - p prime (q<p, q>0). Primality via sympy.isprime.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import isprime, primerange, prime
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
def a(p, first=False):
    c = 0
    for r in primerange(p // 4 + 1, (p + 1) // 2):
        q = 4 * r - p
        if 0 < q < p and isprime(q):
            c += 1
            if first: return 1
    return c
ps = list(primerange(2, prime(NN) + 1))
T, off = terms("A397208")
assert [a(p) for p in ps[:len(T)]] == T; print("terms OK", len(T))
zeros = [p for p in ps if a(p, True) == 0]
print("zeros among first", NN, "primes (p<=%d):" % ps[-1], zeros)
print("RESULT", "holds for n<=%d" % NN if zeros == [2, 3, 11, 19, 43, 67] else "COUNTEREXAMPLE p=%s" % zeros)
