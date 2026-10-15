# A082935: smallest palindrome beginning with (the digits of) n whose iterated digit sum equals n at some stage.
# Conjecture (%C): except n = 19, the digit sum at the first stage is already n. Checked to n = 100.
# Method a: for each admissible first-stage sum s (iterating digit sums from s hits n), the smallest palindrome with
# prefix n and digit sum s is built greedily per length (closed-form feasibility of the remaining sum);
# the overall minimum is compared with the s = n candidate.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
T, off = terms("A082935")
ds = lambda x: sum(map(int, str(x)))
def hits(s, n):          # does s, ds(s), ds(ds(s)), ... contain n?
    while True:
        if s == n: return True
        if s < 10 or s < n: return False
        s = ds(s)
def minpal(P, s):
    P = [int(c) for c in P]; k = len(P)
    for L in range(1, 2 * k + s + 3):
        if L < k: continue
        dig = [None] * L; ok = True
        for i, d in enumerate(P):
            for pos in (i, L - 1 - i):
                if dig[pos] is not None and dig[pos] != d: ok = False
                dig[pos] = d
        if not ok: continue
        groups = []                               # free groups (index, weight)
        for i in range((L + 1) // 2):
            if dig[i] is None: groups.append((i, 1 if i == L - 1 - i else 2))
        R = s - sum(d for d in dig if d is not None)
        def feas(R, gs):
            w2 = sum(1 for _, w in gs if w == 2); w1 = sum(1 for _, w in gs if w == 1)
            return 0 <= R <= 18 * w2 + 9 * w1 and (w1 > 0 or R % 2 == 0)
        if not feas(R, groups): continue
        for gi, (i, w) in enumerate(groups):
            for d in range(10):
                if feas(R - w * d, groups[gi + 1:]):
                    dig[i] = dig[L - 1 - i] = d; R -= w * d; break
        return int("".join(map(str, dig)))
    return None
def a(n):
    P = str(n); best = minpal(P, n); best_s = n if best is not None else None
    s = n + 1
    while best is None or s <= 9 * len(str(best)):
        if hits(s, n):
            c = minpal(P, s)
            if c is not None and (best is None or c < best): best, best_s = c, s
        s += 1
    return best, best_s
res = {n: a(n) for n in range(1, N + 1)}
assert [res[n][0] for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
exc = [(n, res[n][1]) for n in range(1, N + 1) if res[n][1] != n]
print("n whose minimal palindrome needs a later stage (n, first-stage sum):", exc)
bad = [n for n, _ in exc if n != 19]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d (a(n)=%d, first-stage sum %d)" % (bad[0], res[bad[0]][0], res[bad[0]][1]))
