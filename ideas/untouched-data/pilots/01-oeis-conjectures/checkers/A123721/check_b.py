# A123721 checker b: pure Python. Earlier A123249 terms are increasing, so keep them in a FIFO queue and
# advance k past queued values (merge), instead of a boolean array. Asserts monotonicity as it goes.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from collections import deque
from k2common import check_terms
K = int(sys.argv[1]) if len(sys.argv) > 1 else 25
N = 2 ** (K + 1) + 2 ** K + 10   # covers A123720(K+1)
q = deque([1]); prev = 1
first = {}; small = {1: 1}   # A123721(1)=1 by the entry's program (prints a=1)
for n in range(2, N + 1):
    k = n
    while q and q[0] < n: q.popleft()          # values below n can never matter again
    i = 0
    while i < len(q) and q[i] <= k:            # queue is sorted: skip used values n, n+1, ...
        if q[i] == k: k += 1
        i += 1
    a = n + k
    assert a > prev; prev = a
    q.append(a)
    v = k - n
    if n < 200: small[n] = v
    if v not in first: first[v] = n
check_terms("A123721", lambda n: small[n])
A720 = lambda k: 2 ** k + 2 ** (k - 1) - k
lit = [(k, first.get(k), A720(k)) for k in range(2, K + 1) if first.get(k) != A720(k)]
sh = [(k, first.get(k), A720(k + 1)) for k in range(2, K + 1) if first.get(k) != A720(k + 1)]
print("K =", K, "(n up to", N, ") | max value seen:", max(first))
print("  literal form first{a(n)=k} == A123720(k): mismatches (k, first, A123720(k)):", lit[:5], "...", len(lit))
print("  shifted form first{a(n)=k} == A123720(k+1): mismatches:", sh)
