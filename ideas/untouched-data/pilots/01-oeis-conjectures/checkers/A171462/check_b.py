# A171462 checker b: A191898 by its literal recurrence, column by column with a sliding window sum
# (T(m,k) = -(T(m-1,k)+...+T(m-k+1,k)) for m >= k; entries above the diagonal read from the lower triangle by symmetry,
# which is how the n<k branch of the definition reads). a(n) = n*(1-1/P) computed from a smallest-prime-factor sieve.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, numba
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 14000
@numba.njit(cache=True)
def build(N):
    off = np.zeros(N + 2, dtype=np.int64)            # row m holds T(m,1..m) at off[m]..off[m]+m-1
    for m in range(1, N + 1): off[m + 1] = off[m] + m
    L = np.zeros(off[N + 1], dtype=np.int32)
    for m in range(1, N + 1): L[off[m]] = 1          # T(m,1)=1
    for k in range(2, N + 1):
        # window holds T(m-1,k), ..., T(m-k+1,k); initial m=k: T(1..k-1, k) = T(k, 1..k-1) (computed columns < k)
        s = 0
        for r in range(1, k): s += L[off[k] + r - 1]
        for m in range(k, N + 1):
            v = -s
            L[off[m] + k - 1] = v
            # slide: add T(m,k), drop T(m-k+1,k)
            j = m - k + 1
            drop = L[off[k] + j - 1] if j < k else L[off[j] + k - 1]
            s += v - drop
    return L, off
@numba.njit(cache=True)
def lhs(N, L, off):
    out = np.zeros(N + 1, dtype=np.int64)
    for n in range(2, N + 1):
        bn, bd = 1, 1
        for k in range(1, n + 1):
            t = L[off[n] + k - 1]
            if t * bd < bn * k: bn, bd = t, k
        out[n] = -(n * bn) // bd if (n * bn) % bd == 0 else -10 ** 18
    return out
L, off = build(N)
from k2common import terms
T191898 = terms("A191898"); idx = 0; d = 2; ok = True
while idx < len(T191898):
    for n in range(1, d):
        k = d - n
        if idx < len(T191898):
            if L[off[max(n, k)] + min(n, k) - 1] != T191898[idx]: ok = False
            idx += 1
    d += 1
print("A191898 data terms reproduced:", ok, len(T191898))
spf = list(range(N + 1))
for i in range(2, int(N ** .5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j: spf[j] = i
def gpf(n):
    g = 1
    while n > 1: g = max(g, spf[n]); n //= spf[n]
    return g
A = [0, 0] + [n - n // gpf(n) for n in range(2, N + 1)]
check_terms("A171462", lambda n: A[n])
Lh = lhs(N, L, off)
bad = [n for n in range(2, N + 1) if Lh[n] != A[n]]
print("N =", N, "mismatches:", bad[:10])
