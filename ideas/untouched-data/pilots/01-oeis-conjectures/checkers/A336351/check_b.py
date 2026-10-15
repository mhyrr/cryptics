# A336351, method b: exhaustive DFS over the "power-of-two difference" graph (Lemma in the entry: neighbours differ by
# a power of 2), testing the AP condition of each new triple explicitly by sorting; different candidate generation from a.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 150
KMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 120
NT = int(sys.argv[3]) if len(sys.argv) > 3 else 14
@njit(cache=True)
def isap(a, b, c):
    lo = min(a, min(b, c)); hi = max(a, max(b, c)); mid = a + b + c - lo - hi
    return mid - lo == hi - mid
@njit(cache=True)
def count(k):
    # neighbour lists: j with |i-j| a power of two
    nb = np.zeros((k + 1, 64), np.int64); nn = np.zeros(k + 1, np.int64)
    for i in range(1, k + 1):
        d = 1
        while d < k:
            for j in (i - d, i + d):
                if 1 <= j <= k: nb[i, nn[i]] = j; nn[i] += 1
            d *= 2
    v = np.zeros(k + 1, np.int64); used = np.zeros(k + 2, np.bool_); idx = np.zeros(k + 1, np.int64)
    v[0] = 1; used[1] = True; total = 0
    pos = 1; idx[1] = 0
    while pos >= 1:
        prev = v[pos - 1]
        if idx[pos] >= nn[prev]:
            pos -= 1
            if pos >= 1: used[v[pos]] = False; idx[pos] += 1
            continue
        z = nb[prev, idx[pos]]
        if used[z] or (pos >= 2 and not isap(v[pos - 2], prev, z)):
            idx[pos] += 1; continue
        if pos == k - 1:
            if isap(prev, z, v[0]) and isap(z, v[0], v[1]): total += 1
            idx[pos] += 1; continue
        v[pos] = z; used[z] = True; pos += 1; idx[pos] = 0
    return total
T, off = terms("A336351")
got = [count(6 * n - 3) // 2 for n in range(1, NT + 1)]
print("terms a(1..%d):" % NT, got)
assert got == T[:NT], (got, T[:NT]); print("terms OK", NT)
bad = []
for k in range(KMIN, KMAX + 1, 6):
    t = time.time(); c = count(k); print("k=%d arrangements=%d (%.1fs)" % (k, c, time.time() - t), flush=True)
    if c: bad.append(k)
print("RESULT", "holds for k<=%d" % KMAX if not bad else "COUNTEREXAMPLE k=%s" % bad)
