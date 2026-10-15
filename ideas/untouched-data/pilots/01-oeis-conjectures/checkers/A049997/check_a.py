# A049997 (numbers F(i)*F(j)). Sun: F(m)*F(n) with 2 < m < n is a perfect power only for (m,n) = (3,6) (2*8=16).
# Verified n <= 900.  Method a: exact Fibonacci by iteration, gmpy2.is_power on every product, 2 < m < n <= N.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
N = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
T, off = terms("A049997")
F = [gmpy2.mpz(0), gmpy2.mpz(1)]
while len(F) <= N: F.append(F[-1] + F[-2])
lim = T[-1]
S = sorted(set(int(F[i] * F[j]) for i in range(0, 40) for j in range(i, 40) if F[i] * F[j] <= lim))
assert S == T, (S[:20], T[:20]); print("terms OK", len(T))
hits = []
for n in range(4, N + 1):
    Fn = F[n]
    for m in range(3, n):
        if gmpy2.is_power(F[m] * Fn): hits.append((m, n))
print("perfect powers:", hits)
bad = [h for h in hits if h != (3, 6)]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE (m,n)=%s" % (bad[0],))
