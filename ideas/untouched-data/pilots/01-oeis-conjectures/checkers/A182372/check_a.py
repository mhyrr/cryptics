# A182372: number of sets S of nonnegative integers with perimeter n (perimeter = sum of elements whose predecessor
# and successor are not both in S). Conjecture (Arndt): a(n) = A227134(n) + A227135(n).
# Method a: A182372 by a DP over maximal runs [a,b] of S (a run contributes a+b, or a if a=b; runs separated by a gap);
# A227134/A227135 from their definitions (partitions with parts used at most twice, a repeated pair allowed only when
# the index of its first copy, parts ascending from index 1, is odd / even) by a knapsack over part values.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, hashlib
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 12000
def zeros(): return np.array([0] * (N + 1), dtype=object)
def shift(X, c):
    Y = zeros()
    if c <= N: Y[c:] = X[:N + 1 - c]
    return Y
empty = zeros(); empty[0] = 1
Gm2, Gm1 = empty.copy(), empty.copy()   # G[b-2], G[b-1] (G[x] = empty + sets whose last run ends <= x)
H = zeros()                              # H[b-1] = Sum_{a=0..b-1} shift(G[a-2], a)
for b in range(0, N + 1):
    F = shift(Gm2, b) + shift(H, b)      # singleton run {b} + runs [a,b], a<b
    Gb = Gm1 + F
    H = H + shift(Gm2, b)                # now H[b]
    Gm2, Gm1 = Gm1, Gb
A = Gm1
check_terms("A182372", lambda n: int(A[n]))
def part(rule_odd):
    E = zeros(); O = zeros(); E[0] = 1   # E/O: number of parts so far even/odd
    for v in range(1, N + 1):
        nE = E + shift(O, v); nO = O + shift(E, v)
        if rule_odd: nE = nE + shift(E, 2 * v)   # pair starts at index count+1, odd <=> count even
        else:        nO = nO + shift(O, 2 * v)   # even index <=> count odd
        E, O = nE, nO
    return E + O
P134 = part(True); P135 = part(False)
check_terms("A227134", lambda n: int(P134[n])); check_terms("A227135", lambda n: int(P135[n]))
bad = [n for n in range(N + 1) if A[n] != P134[n] + P135[n]]
print("N =", N, "mismatches:", bad[:10], "| md5 A182372(0..N):", hashlib.md5(str(list(A)).encode()).hexdigest())
