# A062319 method b: tau(n^n) by trial-division of n^n's exponents via sum_{d|n} n^omega(d) (Manyama's PARI);
# tuple count by inclusion over primes: a pairwise coprime tuple assigns each prime power p^e||n to at most
# one slot with exponent 1..e -> count = prod_p (1 + n*e)  computed here by DP over the prime list
# counting assignments slot-by-slot (transfer over slots, state = set of primes already used).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from sympy import factorint, divisors, primefactors
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
T, off = terms("A062319")
a = lambda n: 1 if n == 0 else sum(n ** len(primefactors(d)) for d in divisors(n))
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def count(n):
    f = factorint(n); ps = list(f); k = len(ps)
    # each slot chooses a divisor: for each prime either exponent 0 or 1..e; coprimality = each prime used once.
    # DP over slots with state mask of used primes; number of divisors with prime-support exactly S is prod_{p in S} e_p.
    from itertools import combinations
    ways = {}
    for m in range(1 << k):
        w = 1
        for i in range(k):
            if m >> i & 1: w *= f[ps[i]]
        ways[m] = w
    dp = {0: 1}
    for _ in range(n):
        nd = {}
        for used, c in dp.items():
            free = ((1 << k) - 1) & ~used
            sub = free
            while True:
                nd[used | sub] = nd.get(used | sub, 0) + c * ways[sub]
                if sub == 0: break
                sub = (sub - 1) & free
        dp = nd
    return sum(dp.values())
bad = None
for n in range(1, N + 1):
    if count(n) != a(n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
