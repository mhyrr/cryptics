# A357510, method b: the entry's 4-term P-recurrence (exact integer division asserted), then reduce mod p^4.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import primerange
P = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
N = P
a = [0, 4, 108]
for n in range(3, N + 1):
    rhs = ((2*n-1)*(105*n**5 - 576*n**4 + 1208*n**3 - 1195*n**2 + 556*n - 104)*a[n-1]
           - (2*n-3)*(105*n**5 - 474*n**4 + 800*n**3 - 629*n**2 + 240*n - 36)*a[n-2]
           + (n-1)*(2*n-1)*(3*n**2-3*n+1)*(n-2)**2*a[n-3])
    d = n**2*(n-1)*(2*n-3)*(3*n**2-9*n+7)
    q, r = divmod(rhs, d); assert r == 0, n
    a.append(q)
T, off = terms("A357510")
assert a[:len(T)] == T; print("terms OK", len(T))
bad = [p for p in primerange(5, P) if a[p-1] % p**4]
print("tested primes", len(list(primerange(5, P))), "below", P)
print("RESULT", "holds for 5<=p<%d" % P if not bad else "COUNTEREXAMPLE p=%s" % bad)
