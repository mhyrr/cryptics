# A003592: numbers 2^i*5^j. Sun's conjecture: every n >= 1 not in {1,4,12} is a sum of distinct numbers
# 2^a*5^b + 1 (a,b >= 0) with no summand dividing another.  Method a: per-target DFS (largest first) with
# suffix-sum pruning and pairwise divisibility check. Prints witnesses.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 37000
T, off = terms("A003592")
seq = sorted(2**i * 5**j for i in range(80) for j in range(40) if 2**i * 5**j <= 10**18)
assert seq[:len(T)] == T; print("terms OK", len(T))
B = sorted(set(x + 1 for x in seq if x + 1 <= N))
def solve(n):
    els = [b for b in B if b <= n][::-1]
    suf = [0] * (len(els) + 1)
    for i in range(len(els) - 1, -1, -1): suf[i] = suf[i + 1] + els[i]
    chosen = []
    def dfs(i, r):
        if r == 0: return True
        if i == len(els) or suf[i] < r: return False
        x = els[i]
        if x <= r and all(c % x and x % c for c in chosen):
            chosen.append(x)
            if dfs(i + 1, r - x): return True
            chosen.pop()
        return dfs(i + 1, r)
    return list(chosen) if dfs(0, n) else None
fails = [n for n in range(1, N + 1) if solve(n) is None]
print("non-representable n:", fails)
print("witness 3700:", solve(3700), " witness N:", solve(N))
bad = [n for n in fails if n not in (1, 4, 12)]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
