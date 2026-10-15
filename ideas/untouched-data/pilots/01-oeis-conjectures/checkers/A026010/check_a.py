# A026010: a(n) = number of Dyck-like walks... ; PARI: a(n) = sum_{k=0..n} binomial(floor((n+k)/2), floor(k/2)).
# Conjecture: a(n) = #compositions of n+2 in which even parts appear as often at even positions as at odd positions.
# Method a: definition of a(n) by counting walks s(0)=2, |s(i)-s(i-1)|=1, s(i)>=0 (DP); compositions by DP over
# (sum, parity of next position, #even parts at odd pos - #even parts at even pos).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 190
T, off = terms("A026010")
def walks(n):
    v = {2: 1}
    for _ in range(n):
        w = {}
        for s, c in v.items():
            for t in (s - 1, s + 1):
                if t >= 0: w[t] = w.get(t, 0) + c
        v = w
    return sum(v.values())
A = [walks(n) for n in range(N + 1)]
assert A[:len(T)] == T; print("terms OK", len(T))
M = N + 2
# dp[m][par][d]: compositions of m, next position parity par (0 -> next is odd position 1,3,..), balance d
from collections import defaultdict
dp = [defaultdict(int) for _ in range(M + 1)]; dp[0][(0, 0)] = 1
for m in range(M + 1):
    for (par, d), c in list(dp[m].items()):
        for k in range(1, M - m + 1):
            nd = d + ((1 if par == 0 else -1) if k % 2 == 0 else 0)
            dp[m + k][(1 - par, nd)] += c
C = [sum(c for (par, d), c in dp[m].items() if d == 0) for m in range(M + 1)]
bad = next((n for n in range(0, N + 1) if C[n + 2] != A[n]), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
