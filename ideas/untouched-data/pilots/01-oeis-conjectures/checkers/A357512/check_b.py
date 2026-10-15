# A357512, method b: the entry's P-recurrence (exact division asserted), reduce mod n^4.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
a = [mpz(0), mpz(4), mpz(1188), mpz(126144)]
for n in range(4, N + 1):
    rhs = ((n-3)*(2*n-1)*(n+1)*(105*n**7 - 879*n**6 + 2981*n**5 - 5124*n**4 + 4376*n**3 - 1236*n**2 - 442*n + 195)*(n-2)**3*a[n-1]
          - n**3*(n-3)*(2*n-3)*(n+1)*(105*n**7 - 591*n**6 + 1253*n**5 - 1346*n**4 + 784*n**3 - 124*n**2 - 90*n + 33)*a[n-2]
          + n**3*(2*n-1)*(n+1)*(3*n**4 - 6*n**3 + 4*n**2 - n - 1)*(n-1)**4*a[n-3])
    d = (n-3)*(2*n-3)*(3*n**4 - 18*n**3 + 40*n**2 - 39*n + 13)*(n-2)**3*(n-1)**4
    q, r = divmod(rhs, d); assert r == 0, n
    a.append(q)
T, off = terms("A357512")
assert a[:len(T)] == T; print("terms OK", len(T))
ns = [n for n in range(1, N + 1) if n % 6 in (1, 5)]
bad = [n for n in ns if a[n-1] % n**4]
print("tested", len(ns), "values n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
