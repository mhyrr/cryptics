# A336351: number of cyclic arrangements of {1..6n-3} (up to rotation and reversal) in which every three cyclically
# consecutive entries can be reordered into an arithmetic progression.
# Conjecture: for k == 0 (mod 6) no such arrangement of {1..k} exists (verified k<=114).
# Method a: exhaustive DFS in numba; 1 fixed first, the third entry onward is one of 2y-x, (x+y)/2, 2x-y.
# Counts ordered cycles starting at 1 (each arrangement twice, once per direction).
# Usage: check_a.py KMAX [KMIN]  -> tests k = KMIN, KMIN+6, ..., <= KMAX (multiples of 6) and reproduces terms.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 150
KMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 120
NT = int(sys.argv[3]) if len(sys.argv) > 3 else 14
@njit(cache=True)
def ap(a, b, c):
    return 2 * a == b + c or 2 * b == a + c or 2 * c == a + b
@njit(cache=True)
def count(k):
    v = np.zeros(k + 1, np.int64); used = np.zeros(k + 2, np.bool_); ch = np.zeros(k + 1, np.int64)
    v[0] = 1; used[1] = True; total = 0
    for s in range(2, k + 1):
        v[1] = s; used[s] = True
        pos = 2; ch[2] = 0
        while pos >= 2:
            if ch[pos] >= 3:
                pos -= 1
                if pos >= 2:
                    used[v[pos]] = False; ch[pos] += 1
                continue
            x = v[pos - 2]; y = v[pos - 1]; c = ch[pos]
            if c == 0: z = 2 * y - x
            elif c == 1:
                z = (x + y) // 2 if (x + y) % 2 == 0 else -1
            else: z = 2 * x - y
            if z < 1 or z > k or used[z]:
                ch[pos] += 1; continue
            if pos == k - 1:
                if ap(y, z, v[0]) and ap(z, v[0], v[1]): total += 1
                ch[pos] += 1; continue
            v[pos] = z; used[z] = True; pos += 1; ch[pos] = 0
        used[s] = False
    return total
T, off = terms("A336351")
got = []
for n in range(1, NT + 1):
    c = count(6 * n - 3)
    got.append(c // 2 if 6 * n - 3 > 3 else c // 2)
print("terms a(1..%d):" % NT, got)
assert got == T[:NT], (got, T[:NT]); print("terms OK", NT)
bad = []
for k in range(KMIN, KMAX + 1, 6):
    t = time.time(); c = count(k); print("k=%d arrangements=%d (%.1fs)" % (k, c, time.time() - t), flush=True)
    if c: bad.append(k)
print("RESULT", "holds for k<=%d" % KMAX if not bad else "COUNTEREXAMPLE k=%s" % bad)
