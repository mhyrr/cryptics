# A074987 method b: totients from PARI (cypari2 eulerphi), terms by the PARI brute-force translation;
# conjecture by scanning, for each n, the list of m in n's phi-class built incrementally in increasing m.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
T, off = terms("A074987")
def brute(n):
    t = int(pari.eulerphi(n)); m = 1
    while int(pari.eulerphi(m)) != t or m == n: m += 1
    return m
assert [brute(n) for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
phi = [0] + [int(x) for x in pari("vector(%d,k,eulerphi(k))" % (2 * N))]
cls = {}
for m in range(1, 2 * N + 1): cls.setdefault(phi[m], []).append(m)
bad = None
for n in range(1, N + 1):
    if not any(m != n for m in cls[phi[n]] if m <= 2 * n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
