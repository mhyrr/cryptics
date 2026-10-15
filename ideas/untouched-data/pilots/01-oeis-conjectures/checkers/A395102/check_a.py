# A395102: a(1)=3; a(n) = least odd prime not used earlier with (a(n) mod a(n-1)) prime.
# Conjecture: in the "third case" (every odd prime < a(n-1) used and a(n-1)+2 not available) a(n) = 2*1*a(n-1)+p, p prime < a(n-1),
# i.e. 2a(n-1) < a(n) < 3a(n-1). Confirmed to n=10000.
# Method a: literal definition in numba (scan unused primes upward from the least unused one), then classify each step.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
L = 60_000_000
@njit(cache=True)
def run(N, L):
    isp = np.ones(L, np.bool_); isp[:2] = False
    for i in range(2, int(L ** 0.5) + 1):
        if isp[i]:
            for j in range(i * i, L, i): isp[j] = False
    used = np.zeros(L, np.bool_)
    a = np.zeros(N + 1, np.int64); a[1] = 3; used[3] = True
    case = np.zeros(N + 1, np.int64)
    lo = 5
    for n in range(2, N + 1):
        while used[lo] or not isp[lo]: lo += 2
        prev = a[n - 1]
        # classify which case applies (before choosing)
        if lo < prev: c = 1
        elif isp[prev + 2] and not used[prev + 2]: c = 2
        else: c = 3
        q = lo
        while True:
            if q >= L: return a, case, -1
            if isp[q] and not used[q] and isp[q % prev]: break
            q += 2
        a[n] = q; used[q] = True; case[n] = c
    return a, case, 0
a, case, err = run(N, L)
assert err == 0, "sieve too small"
T, off = terms("A395102")
assert list(a[1:1 + len(T)]) == T; print("terms OK", len(T))
bad = [n for n in range(2, N + 1) if case[n] == 3 and not (2 * a[n-1] < a[n] < 3 * a[n-1])]
print("n<=%d: case counts" % N, {c: int((case == c).sum()) for c in (1, 2, 3)}, "max a =", a.max())
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s (a(n-1)=%d, a(n)=%d)" % (bad[0], a[bad[0]-1], a[bad[0]]))
