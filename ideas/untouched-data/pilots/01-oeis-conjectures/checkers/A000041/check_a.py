# A000041 (partition numbers). Sun's conjecture: every n > 2, n != 6, is a sum of distinct numbers of the form
# p(k)+2 (k>0) with no summand dividing another.  Method a: per-target DFS from the largest element down,
# with suffix-sum pruning and a forbidden set (divisors/multiples of chosen elements). Prints a witness sample.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 71400
T, off = terms("A000041")
def parts(m):                       # partition numbers by Euler's pentagonal recurrence
    p = [1] + [0] * m
    for n in range(1, m + 1):
        s, k = 0, 1
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > n: break
            sg = 1 if k % 2 else -1
            s += sg * p[n - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= n: s += sg * p[n - g2]
            k += 1
        p[n] = s
    return p
p = parts(400)
assert p[:len(T)] == T; print("terms OK", len(T))
B = sorted(set(p[k] + 2 for k in range(1, 400) if p[k] + 2 <= N))
sys.setrecursionlimit(10000)
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
print("witness 7140:", solve(7140), " witness N:", solve(N))
bad = [n for n in fails if n > 2 and n != 6]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
