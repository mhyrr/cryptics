# A081113: king paths of length n-1 from one side of an n X n board to the opposite (one cell per row,
# column moves -1/0/+1). Conjecture: (n+3)a(n+4) = 27n a(n) + 27a(n+1) - 9(2n+5)a(n+2) + (8n+21)a(n+3).
# Method a: direct transfer DP over columns. Exact (python ints) for n <= 60 (terms); for the range test the
# same DP is run vectorised in numpy modulo two ~2^61 primes (exact counts are ~3^n, too slow to DP exactly).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1800
T, off = terms("A081113")
def exact(n):
    v = [1] * n
    for _ in range(n - 1):
        v = [v[i] + (v[i - 1] if i else 0) + (v[i + 1] if i + 1 < n else 0) for i in range(n)]
    return sum(v)
assert [exact(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def modvals(p):
    out = [0]
    for n in range(1, N + 1):
        v = np.ones(n, dtype=np.int64)
        for _ in range(n - 1):
            w = v.copy(); w[1:] += v[:-1]; w[:-1] += v[1:]; v = w % p
        out.append(sum(int(x) for x in v) % p)   # python-int sum: avoid int64 overflow
    return out
bad = None
primes = [576460752303423433, 576460752303423263]   # < 2^59 so 3 additions cannot overflow int64
for p in primes:
    a = modvals(p)
    for n in range(1, N - 3):
        lhs = (n + 3) * a[n + 4] % p
        rhs = (27 * n * a[n] + 27 * a[n + 1] - 9 * (2 * n + 5) * a[n + 2] + (8 * n + 21) * a[n + 3]) % p
        if lhs != rhs: bad = (n, p); break
    if bad: break
print("RESULT", "holds (mod 2 primes) to n=%d" % (N - 4) if bad is None else "COUNTEREXAMPLE n=%d (mod %d)" % bad)
