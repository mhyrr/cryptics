# A060432: partial sums of A002024. Conjecture (Gupta & Irvine): a(n) = minimum diameter of an (n+1)-element set of
# integers in which no nonzero d has more than d representations as a difference (pairs x > y with x - y = d).
# Known true for n <= 16.  Method a: numba iterative DFS over sets {0 = s0 < s1 < ...} inside [0, Dmax]
# (translation-normalised), maintaining difference counts; decides existence of an (n+1)-set with diameter <= Dmax.
# For each n: no set with diameter <= a(n)-1, and some set with diameter a(n).
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np, numba
from math import isqrt
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A060432")
A002024 = lambda k: (isqrt(8 * k) + 1) // 2      # floor(1/2 + sqrt(2k))
a = lambda n: sum(A002024(k) for k in range(1, n + 1))
assert [a(n) for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
@numba.njit(cache=False)
def exists(k, Dmax):
    # k = number of elements (n+1); returns 1 if a valid set inside [0, Dmax] containing 0 exists
    el = np.zeros(k, np.int64); r = np.zeros(Dmax + 1, np.int64)
    nxt = np.zeros(k, np.int64)
    el[0] = 0; t = 1; nxt[1] = 1
    while t >= 1:
        if t == k: return 1
        x = nxt[t]
        placed = False
        while x <= Dmax - (k - 1 - t):
            ok = True; i = 0
            while i < t:
                d = x - el[i]; r[d] += 1
                if r[d] > d: ok = False; i += 1; break
                i += 1
            if ok:
                el[t] = x; nxt[t] = x + 1; t += 1
                if t < k: nxt[t] = x + 1
                placed = True; break
            for j in range(i): r[x - el[j]] -= 1
            x += 1
        if not placed:
            t -= 1
            if t >= 1:
                y = el[t]
                for j in range(t): r[y - el[j]] -= 1
                # nxt[t] already y+1
    return 0
last = None; bad = None
for n in range(1, NMAX + 1):
    if time.time() - T0 > DEADLINE: break
    if exists(n + 1, a(n) - 1): bad = (n, "smaller diameter exists"); break
    if not exists(n + 1, a(n)): bad = (n, "no set of diameter a(n)"); break
    last = n; print("n=%d ok (%.0fs)" % (n, time.time() - T0), flush=True)
print("RESULT", "holds to %s" % last if bad is None else "COUNTEREXAMPLE n=%d (%s)" % bad)
