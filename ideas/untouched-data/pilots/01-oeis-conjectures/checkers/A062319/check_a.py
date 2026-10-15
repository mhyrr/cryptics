# A062319: a(n) = tau(n^n). Conjecture: tau(n^n) = #ordered n-tuples of divisors of n that are pairwise coprime.
# Method a: tau(n^n) by factoring n (sympy); tuple count by exhaustive enumeration over tuples for small n
# (backtracking: extend a partial tuple only with divisors coprime to all chosen so far).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from math import gcd, prod
from sympy import factorint, divisors
from functools import lru_cache
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
T, off = terms("A062319")
tau_nn = lambda n: 1 if n == 0 else prod(n * e + 1 for e in factorint(n).values())
assert [tau_nn(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def count(n):
    ds = divisors(n)
    @lru_cache(None)
    def f(k, used):          # k slots left, 'used' = product of primes-support used so far (as radical)
        if k == 0: return 1
        return sum(f(k - 1, used * d // gcd(used, d) if d > 1 else used) for d in ds if gcd(d, used) == 1)
    return f(n, 1)
bad = None
for n in range(1, N + 1):
    if count(n) != tau_nn(n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
