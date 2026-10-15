# A113191 checker b: Lucas numbers by the doubling-free closed recurrence via sympy.lucas, perfect-power test by
# sympy.perfect_power (independent implementation from gmpy2.is_power); non-square <=> exponent part odd.
import sys, os; os.environ["SYMPY_GROUND_TYPES"] = "python"   # flint ground types break math.log on huge ints inside perfect_power
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from sympy import perfect_power, lucas
from sympy.core.numbers import igcd
from k2common import terms
M = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
L = [int(lucas(i)) for i in range(M + 1)]
T = terms("A113191"); top = T[-1]
vals = {0} | {L[i] - L[j] for i in range(1, 40) for j in range(i - 1) if L[i] - L[j] <= top} | {L[i] - L[i-1] for i in range(1, 40)}
vals = sorted(v for v in vals if 0 <= v <= top)
assert vals == T, vals[:70]
print("reproduced all", len(T), "data terms")
hits = []
for m in range(2, M + 1):
    for n in range(m):
        d = L[m] - L[n]
        if d <= 1: continue
        r = perfect_power(d)          # (base, e) with maximal e, or False
        if r and r[1] % 2 == 1:       # maximal exponent odd => not a square
            hits.append((m, n, d if d < 10**12 else "big"))
    if m % 500 == 0: print("m =", m, "hits", hits, flush=True)
print("M =", M, "non-square perfect powers:", hits)
