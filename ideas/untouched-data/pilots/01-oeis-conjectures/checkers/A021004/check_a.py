# A021004: Pisot sequence P(4,10): a(0)=4, a(1)=10, a(n) = ceil(a(n-1)^2/a(n-2) - 1/2) (exact integer arithmetic).
# Conjecture: a(n) = 2a(n-1) + a(n-2) + a(n-3) - a(n-4) - a(n-6).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A021004")
a = [4, 10]
for n in range(2, N + 1):
    num, den = 2 * a[-1] ** 2 - a[-2], 2 * a[-2]     # ceil(num/den)
    a.append(-((-num) // den))
assert a[:len(T)] == T; print("terms OK", len(T))
bad = next((n for n in range(6, N + 1) if a[n] != 2*a[n-1] + a[n-2] + a[n-3] - a[n-4] - a[n-6]), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
