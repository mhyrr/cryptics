# A359930: a(n) = #practical numbers strictly between P(n) and P(n)^(1+1/n), P = A005153.
# Sun's conjecture: P(n)^(1/n) strictly decreasing for n>=3 (valid for n<=9991). Tested literally: P(n+1)^(1/(n+1)) < P(n)^(1/n).
# Method a: Stewart-Sierpinski criterion with an spf sieve (numba), then compare n*ln P(n+1) vs (n+1)*ln P(n) in double,
# falling back to exact integer powers when the margin is < 1e-6.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 99910
X = 3_000_000
@njit(cache=True)
def practical(X):
    spf = np.zeros(X + 1, np.int64)
    for i in range(2, X + 1):
        if spf[i] == 0:
            for j in range(i, X + 1, i):
                if spf[j] == 0: spf[j] = i
    pr = np.zeros(X + 1, np.bool_); pr[1] = True
    for n in range(2, X + 1, 2):
        m = n; sig = 1; ok = True
        while m > 1:
            p = spf[m]
            if p > sig + 1: ok = False; break
            pe = 1; s = 1
            while m % p == 0: m //= p; pe *= p; s += pe
            sig *= s
        pr[n] = ok
    return pr
pr = practical(X)
P = np.nonzero(pr)[0]
assert len(P) > NMAX + 1, len(P)
P = [int(v) for v in P[:NMAX + 2]]  # P[0] = P(1)
def cnt(n):
    p = P[n - 1]; hi = p ** (1 + 1 / n); return sum(1 for q in P[n:n + 200] if p < q < hi)
T, off = terms("A359930")
assert [cnt(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
bad = []; exact = 0
for n in range(3, NMAX + 1):
    a, b = P[n - 1], P[n]   # P(n), P(n+1)
    diff = n * math.log(b) - (n + 1) * math.log(a)   # want < 0
    if abs(diff) < 1e-6:
        exact += 1; ok = b ** n < a ** (n + 1)
    else: ok = diff < 0
    if not ok: bad.append(n)
print("exact fallbacks:", exact, " P(%d) = %d" % (NMAX + 1, P[NMAX]))
print("RESULT", "holds for 3<=n<=%d" % NMAX if not bad else "COUNTEREXAMPLE n=%s" % bad[:5])
