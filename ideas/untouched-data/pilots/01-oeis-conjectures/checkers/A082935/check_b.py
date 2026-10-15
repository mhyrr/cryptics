# A082935 method b: per length L, the palindrome is its first half; a suffix DP of reachable digit sums over the
# free half-positions (sets) drives a lexicographically smallest construction. Admissible first-stage sums s are
# those whose digital-root chain hits n (computed recursively, memoised). The smallest palindrome over all
# admissible s is found by scanning lengths L = len(n).. and, within a length, all admissible s.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from functools import lru_cache
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
T, off = terms("A082935")
@lru_cache(None)
def chain(s):
    out = {s}
    if s >= 10: out |= chain(sum(int(c) for c in str(s)))
    return frozenset(out)
def best_of_length(P, L, n):
    k = len(P); h = (L + 1) // 2
    half = [None] * h
    full = [None] * L
    for i, c in enumerate(P):
        for pos in (i, L - 1 - i):
            if full[pos] is not None and full[pos] != int(c): return None
            full[pos] = int(c)
    for i in range(h):
        j = L - 1 - i
        if full[i] is not None and full[j] is not None and full[i] != full[j]: return None
        half[i] = full[i] if full[i] is not None else full[j]
    w = [1 if i == L - 1 - i else 2 for i in range(h)]
    # reach[i] = set of sums achievable by positions i..h-1
    reach = [set() for _ in range(h + 1)]; reach[h] = {0}
    for i in range(h - 1, -1, -1):
        opts = [half[i]] if half[i] is not None else range(10)
        reach[i] = {w[i] * d + r for d in opts for r in reach[i + 1]}
    targets = sorted(s for s in reach[0] if n in chain(s))
    best = None
    for s in targets:
        dig = []; R = s
        for i in range(h):
            opts = [half[i]] if half[i] is not None else range(10)
            for d in opts:
                if R - w[i] * d in reach[i + 1]: dig.append(d); R -= w[i] * d; break
        x = int("".join(map(str, dig + dig[: L // 2][::-1])))
        if best is None or x < best[0]: best = (x, s)
    return best
def a(n):
    P = str(n); L = len(P)
    while True:
        b = best_of_length(P, L, n)
        if b: return b
        L += 1
res = {n: a(n) for n in range(1, N + 1)}
assert [res[n][0] for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
exc = [(n, res[n][1]) for n in range(1, N + 1) if res[n][1] != n]
print("n whose minimal palindrome needs a later stage (n, first-stage sum):", exc)
bad = [n for n, _ in exc if n != 19]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d (a(n)=%d, first-stage sum %d)" % (bad[0], res[bad[0]][0], res[bad[0]][1]))
