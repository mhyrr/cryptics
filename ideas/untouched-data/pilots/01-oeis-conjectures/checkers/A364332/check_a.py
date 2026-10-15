# A364332: f(2)=0, f(p)=1+max{f(q): q prime, q|p-1}. Conjecture: the least prime p with f(p)=m is A082449(m) (verified m<=13).
# Method a: one Eratosthenes pass in numba: arr[n] = 1+max f(q) over primes q|n seen so far; when the pass reaches a prime p
# (arr[p]==0), f(p) = arr[p-1] (p>2), then propagate to multiples. Records the least prime for each f value up to X.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
X = int(sys.argv[1]) if len(sys.argv) > 1 else 1432349099
A082449, _ = terms("A082449")
@njit(cache=True)
def run(X, nfirst):
    arr = np.zeros(X + 1, np.uint8)
    least = np.zeros(64, np.int64); firstf = np.zeros(nfirst, np.int64); cnt = 0
    for n in range(2, X + 1):
        if arr[n] == 0:
            f = 0 if n == 2 else arr[n - 1]
            if least[f] == 0: least[f] = n
            if cnt < nfirst: firstf[cnt] = f; cnt += 1
            v = np.uint8(f + 1); arr[n] = v
            for j in range(2 * n, X + 1, n):
                if arr[j] < v: arr[j] = v
    return least, firstf
least, firstf = run(X, 200)
T, off = terms("A364332")
assert list(firstf[:len(T)]) == T; print("terms OK", len(T))
bad = []
for m in range(0, 30):
    if least[m]: print("m=%d least prime %d  A082449(m)=%s" % (m, least[m], A082449[m] if m < len(A082449) else "?"))
# conjecture for m: least prime with f=m equals A082449(m); decidable within X iff A082449(m) <= X
ms = [m for m in range(len(A082449)) if A082449[m] <= X]
bad = [m for m in ms if least[m] != A082449[m]]
print("decided for m <=", max(ms))
print("RESULT", "holds for m<=%d" % max(ms) if not bad else "COUNTEREXAMPLE m=%s (least p=%d vs A082449=%d)" % (bad[0], least[bad[0]], A082449[bad[0]]))
