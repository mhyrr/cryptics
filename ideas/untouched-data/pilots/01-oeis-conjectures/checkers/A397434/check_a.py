# A397434: a(n) = #monomials in the ANF of the threshold function [weight >= t], t = ceil(n/2), n variables.
# ANF coefficient of a degree-d monomial = parity of #{k < t : k submask of d} (Lucas), and a(n) = Sum_{d: coef=1} C(n,d).
# Conjecture: a(n) = a(n+1) iff n == 2 (mod 4) (verified n<=998).
# Method a: digit-DP for the submask count, exact binomials by incremental product (Python ints).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
def coef(d, t):
    res = 0
    for i in range(max(t.bit_length(), d.bit_length()), -1, -1):
        if (t >> i) & 1:
            res += 1 << bin(d & ((1 << i) - 1)).count("1")
            if not (d >> i) & 1: return res & 1
    return res & 1
def a(n):
    t = (n + 1) // 2; s = 0; b = 1
    for d in range(1, n + 1):
        b = b * (n - d + 1) // d
        if coef(d, t): s += b
    return s
# brute check of coef against the ANF definition for small n
from itertools import combinations
for n in range(1, 9):
    t = (n + 1) // 2
    for d in range(1, n + 1):
        anf = sum(1 for kk in range(d + 1) for _ in combinations(range(d), kk) if kk >= t) & 1   # Moebius sum over subsets of a d-set
        assert anf == coef(d, t), (n, d)
T, off = terms("A397434")
assert [a(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
vals = [None] + [a(n) for n in range(1, N + 2)]
bad = [n for n in range(1, N + 1) if (vals[n] == vals[n + 1]) != (n % 4 == 2)]
print("tested 1<=n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[:5])
