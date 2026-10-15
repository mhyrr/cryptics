# A074987: a(n) = least m != n with phi(m) = phi(n). Conjecture: a(n) <= 2n.
# Method a: numpy totient sieve to 2N; for each n look for m <= 2n, m != n, with phi(m) = phi(n) via sorted classes.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
T, off = terms("A074987")
M = 2 * N + 10
phi = np.arange(M + 1, dtype=np.int64)
for p in range(2, M + 1):
    if phi[p] == p:
        phi[p::p] -= phi[p::p] // p
order = np.lexsort((np.arange(M + 1), phi))       # sort by phi then by m
sp = phi[order]
first = {}
# smallest two m in each phi class
starts = np.flatnonzero(np.r_[True, sp[1:] != sp[:-1]])
two = {}
for s in starts:
    v = int(sp[s]); m1 = int(order[s]); m2 = int(order[s + 1]) if s + 1 <= M and sp[s + 1] == sp[s] else None
    two[v] = (m1, m2)
def a(n):
    m1, m2 = two[int(phi[n])]
    if m1 == 0: m1, m2 = m2, None  # index 0 has phi 0 only
    return m1 if m1 != n else m2
calc = [a(n) for n in range(1, len(T) + 1)]
assert calc == T, (calc[:20], T[:20]); print("terms OK", len(T))
bad = None
for n in range(1, N + 1):
    m = a(n)
    if m is None or m > 2 * n: bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
