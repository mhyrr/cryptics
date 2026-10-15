# A359930, method b: practical numbers via the recursion n = m*p^a (p = largest prime factor): n practical iff m practical
# and p <= sigma(m)+1 (lpf + sigma sieves, numba); list cross-checked against the subset-sum definition for n<=3000;
# comparison P(n+1)^(1/(n+1)) < P(n)^(1/n) done with mpmath at 50 digits.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
import mpmath; mpmath.mp.dps = 50
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 99910
X = 3_000_000
@njit(cache=True)
def practical(X):
    lpf = np.zeros(X + 1, np.int64); sig = np.ones(X + 1, np.int64)
    for i in range(2, X + 1):
        if lpf[i] == 0:
            for j in range(i, X + 1, i): lpf[j] = i
    for d in range(2, X + 1):
        for j in range(d, X + 1, d): sig[j] += d
    pr = np.zeros(X + 1, np.bool_); pr[1] = True
    for n in range(2, X + 1):
        p = lpf[n]; m = n
        while m % p == 0: m //= p
        pr[n] = pr[m] and p <= sig[m] + 1
    return pr
pr = practical(X)
def brute(n):
    divs = [d for d in range(1, n + 1) if n % d == 0]; reach = 1
    for d in divs: reach |= reach << d
    return all((reach >> m) & 1 for m in range(1, n + 1))
assert all(bool(pr[n]) == brute(n) for n in range(1, 3001)); print("practical list matches definition for n<=3000")
P = [int(v) for v in np.nonzero(pr)[0][:NMAX + 2]]
def cnt(n):
    p = mpmath.mpf(P[n - 1]); hi = p ** (1 + mpmath.mpf(1) / n); return sum(1 for q in P[n:n + 200] if p < q < hi)
T, off = terms("A359930")
assert [cnt(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
bad = []; minmargin = None
for n in range(3, NMAX + 1):
    d = mpmath.log(P[n - 1]) / n - mpmath.log(P[n]) / (n + 1)   # want > 0
    if d <= 0: bad.append(n)
    if minmargin is None or d < minmargin[0]: minmargin = (d, n)
print("smallest margin ln P(n)/n - ln P(n+1)/(n+1) = %s at n=%d" % (mpmath.nstr(minmargin[0], 6), minmargin[1]))
print("RESULT", "holds for 3<=n<=%d" % NMAX if not bad else "COUNTEREXAMPLE n=%s" % bad[:5])
