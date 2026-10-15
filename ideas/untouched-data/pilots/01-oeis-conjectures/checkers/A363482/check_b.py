# A363482, method b: the entry's formula (Marcus PARI translation) evaluated mod M = n^2+3n-5:
# a(n) = M / gcd(M, 5 f(n-3) + n f(n-4)), f(m) = (m+2)*lf(m+1)/2, lf(m) = Sum_{k<m} k!  (M odd so 2 is invertible). numba.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from gmpy2 import is_prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
@njit(cache=True)
def gcd(a, b):
    while b: a, b = b, a % b
    return a
@njit(cache=True)
def mm(a, b, M):
    # (a*b) mod M for 0<=a,b<M<2^50 without 128-bit ints: float quotient estimate, wrapping int64 remainder, then correction
    q = np.int64(float(a) * float(b) / float(M))
    r = np.int64(np.uint64(a) * np.uint64(b) - np.uint64(q) * np.uint64(M))
    while r < 0: r += M
    while r >= M: r -= M
    return r
@njit(cache=True)
def run(N):
    out = np.zeros(N + 1, np.int64)
    for n in range(3, N + 1):
        M = n * n + 3 * n - 5
        inv2 = (M + 1) // 2
        # lf(m) for m = n-3 and n-2 (needed for f(n-4) and f(n-3)); lf(m) = sum_{k=0}^{m-1} k!
        fac = 1; lf = 0; lfs = np.zeros(n + 1, np.int64)
        for k in range(0, n - 1):
            if k > 0: fac = mm(fac, k % M, M)
            lf = (lf + fac) % M; lfs[k + 1] = lf
        def_f3 = mm(mm((n - 1) % M, lfs[n - 2], M), inv2, M)      # f(n-3) = (n-1) lf(n-2) / 2
        f4 = mm(mm((n - 2) % M, lfs[n - 3], M), inv2, M) if n >= 4 else 0  # f(n-4) = (n-2) lf(n-3)/2
        if n == 3: f4 = 0   # f(-1) = 1*lf(0)/2 = 0
        X = (mm(5, def_f3, M) + mm(n % M, f4, M)) % M
        out[n] = M // gcd(M, X)
    return out
out = run(N)
T, off = terms("A363482")
assert [int(out[n]) for n in range(3, 3 + len(T))] == T; print("terms OK", len(T))
bad = [n for n in range(3, N + 1) if out[n] != 1 and out[n] != 49 and not is_prime(int(out[n]))]
print("n with a(n)=49:", [n for n in range(3, N + 1) if out[n] == 49])
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s a=%s" % (bad[0], out[bad[0]]))
