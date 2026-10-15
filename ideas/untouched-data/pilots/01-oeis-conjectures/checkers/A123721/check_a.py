# A123721(n) = A123249(n) - 2n, A123249(1)=1, A123249(n) = n + (least k >= n not among earlier terms).
# Conjecture: for k>1 the least n with A123721(n)=k is 2^k+2^(k-1)-k. Method a: numba, boolean "used" array.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, numba
from k2common import check_terms
K = int(sys.argv[1]) if len(sys.argv) > 1 else 27
N = 2 ** (K + 1) + 2 ** K + 10   # covers A123720(K+1)
@numba.njit(cache=True)
def run(N, K):
    w = np.zeros(2 * N + 1000, dtype=np.bool_)
    first = np.full(K + 2, -1, dtype=np.int64)
    small = np.zeros(200, dtype=np.int64)
    w[1] = True; small[1] = 1   # A123721(1)=1 per the entry's PARI program
    for n in range(2, N + 1):
        k = n
        while w[k]: k += 1
        a = n + k; w[a] = True
        v = a - 2 * n
        if n < 200: small[n] = v
        if v <= K + 1 and first[v] == -1: first[v] = n
    return first, small
first, small = run(N, K)
check_terms("A123721", lambda n: int(small[n]))
A720 = lambda k: 2 ** k + 2 ** (k - 1) - k
lit = [(k, int(first[k]), A720(k)) for k in range(2, K + 1) if first[k] != A720(k)]
sh = [(k, int(first[k]), A720(k + 1)) for k in range(2, K + 1) if first[k] != A720(k + 1)]
print("K =", K, "(n up to", N, ")")
print("  literal form first{a(n)=k} == A123720(k): mismatches (k, first, A123720(k)):", lit[:5], "...", len(lit))
print("  shifted form first{a(n)=k} == A123720(k+1): mismatches:", sh)
