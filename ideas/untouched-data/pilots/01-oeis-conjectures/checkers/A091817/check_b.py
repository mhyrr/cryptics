# A091817 method b: same reduction (den(H(p-3)) coprime to p, so integrality <=> 2*H(p-3) == 3 mod p), but
# H(p-3) mod p from the linear-time inverse table inv[i] = -(p//i)*inv[p%i]; terms via PARI translation.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numba, numpy as np, cypari2; pari = cypari2.Pari()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
T, off = terms("A091817")
pari("H(n)=sum(i=1,n,1/i)")
calc = [int(pari("(2*numerator(H(%d))-3*denominator(H(%d)))/%d" % (p - 3, p - 3, p))) for p in pari("primes([3,200])")]
assert calc[:len(T)] == T; print("terms OK", len(T))
@numba.njit
def test(p):
    inv = np.zeros(p, np.int64); inv[1] = 1; s = 1
    for i in range(2, p - 2):
        inv[i] = (p - (p // i) * inv[p % i] % p) % p
        s += inv[i]
    return (2 * (s % p) - 3) % p == 0
bad = None
for p in pari("primes([5,%d])" % N):
    if not test(int(p)): bad = int(p); break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE p=%d" % bad)
