# A081113 method b: exact, by the reflection principle. With L = n-1 and T(L,d) the trinomial coefficient
# [x^d](1+x+1/x)^L, walks in the strip [1,n] summed over start/end give
#   a(n) = sum_d (n-|d|) T(L,d) - 2 sum_{s=2}^{n-1} (s-1) T(L,s)
# (only one reflection on each wall matters since L < n+1). Then test the recurrence exactly.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
T, off = terms("A081113")
a = [0]; row = [1]          # row[d] = T(L, d) for d = 0..L (symmetric)
for n in range(1, N + 1):
    L = n - 1
    if L > 0:
        new = [0] * (L + 1)
        full = lambda d: row[abs(d)] if abs(d) <= L - 1 else 0
        for d in range(L + 1): new[d] = full(d - 1) + full(d) + full(d + 1)
        row = new
    s = n * row[0] + 2 * sum((n - d) * row[d] for d in range(1, L + 1))
    s -= 2 * sum((t - 1) * row[t] for t in range(2, n) if t <= L)
    a.append(s)
assert a[off:off + len(T)] == T; print("terms OK", len(T))
bad = None
for n in range(1, N - 3):
    if (n + 3) * a[n + 4] != 27 * n * a[n] + 27 * a[n + 1] - 9 * (2 * n + 5) * a[n + 2] + (8 * n + 21) * a[n + 3]:
        bad = n; break
print("RESULT", "holds (exact) to n=%d" % (N - 4) if bad is None else "COUNTEREXAMPLE n=%d" % bad)
