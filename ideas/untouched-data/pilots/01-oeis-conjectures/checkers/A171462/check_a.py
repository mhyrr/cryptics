# A171462: a(1)=0, a(n) = n - n/P(n) (P = largest prime factor; the %C characterization; the bartender
# definition itself is not computed). Conjecture (Granvik): for n>1, a(n) = -n * min_{k=1..n} T(n,k)/k with
# T = A191898: T(n,1)=T(1,k)=1, T(n,k) = -Sum_{i=1..k-1} T(n-i,k) (n>=k), -Sum_{i=1..n-1} T(k-i,n) (n<k).
# Method a: column k of T is k-periodic (window sums of length k vanish), so only the first period
# P_k[r]=T(r,k), r=1..k is stored: P_k[r] = T(k,r) = P_r[(k-1)%r+1] for r<k, P_k[k] = -Sum_{r<k} P_k[r].
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, numba
from sympy import primefactors
from k2common import check_terms, terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 14000
@numba.njit(cache=True)
def build(N):
    off = np.zeros(N + 2, dtype=np.int64)
    for k in range(1, N + 1): off[k + 1] = off[k] + k
    P = np.zeros(off[N + 1], dtype=np.int32)    # P[off[k] + r - 1] = T(r,k)
    for k in range(1, N + 1):
        s = 0
        for r in range(1, k):
            v = P[off[r] + ((k - 1) % r)]        # T(k,r) = T((k-1)%r + 1, r)
            P[off[k] + r - 1] = v; s += v
        P[off[k] + k - 1] = 1 if k == 1 else -s
    return P, off
@numba.njit(cache=True)
def lhs(N, P, off):
    out = np.zeros(N + 1, dtype=np.int64)
    for n in range(2, N + 1):
        # min over k of T(n,k)/k as an exact fraction (num, den)
        bn, bd = 1, 1
        for k in range(1, n + 1):
            t = P[off[k] + ((n - 1) % k)]
            if t * bd < bn * k: bn, bd = t, k
        # -n * bn/bd must be an integer for the conjecture to make sense; return -1e18 sentinel if not
        if (n * bn) % bd != 0: out[n] = -10 ** 18
        else: out[n] = -(n * bn) // bd
    return out
P, off = build(N)
T191898 = terms("A191898")   # antidiagonals of symmetric array
idx = 0; d = 2
ok = True
while idx < len(T191898):
    for n in range(1, d):
        k = d - n
        if idx < len(T191898):
            if P[off[max(n, k)] + min(n, k) - 1] != T191898[idx]: ok = False
            idx += 1
    d += 1
print("A191898 data terms reproduced:", ok, len(T191898))
A = [0, 0] + [n - n // max(primefactors(n)) for n in range(2, N + 1)]
check_terms("A171462", lambda n: A[n])
L = lhs(N, P, off)
bad = [n for n in range(2, N + 1) if L[n] != A[n]]
print("N =", N, "mismatches:", bad[:10])
