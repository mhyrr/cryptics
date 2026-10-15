# A068012 method b: roots-of-unity filter a(n) = (1/6) sum_{k=0..5} prod_{j=1..n} (1 + w^(k j)), w = exp(2 pi i/6),
# computed exactly in Z[w] (elements x + y*w with w^2 = w - 1).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
T, off = terms("A068012")
def mul(a, b):  # (x1+y1 w)(x2+y2 w) = x1x2 + (x1y2+x2y1) w + y1y2 (w-1)
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] + a[1] * b[1])
pw = [(1, 0)]
for _ in range(5): pw.append(mul(pw[-1], (0, 1)))
P = [(1, 0)] * 6; A = [1]
for n in range(1, N + 1):
    P = [mul(P[k], (1 + pw[(k * n) % 6][0], pw[(k * n) % 6][1])) for k in range(6)]
    s = (sum(p[0] for p in P), sum(p[1] for p in P))
    assert s[1] == 0 and s[0] % 6 == 0
    A.append(s[0] // 6)
assert A[off:off + len(T)] == T; print("terms OK", len(T))
bad = next((n for n in range(3, N + 1) if (n - 1) % 3 and A[n] != 2 * A[n - 1]), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
