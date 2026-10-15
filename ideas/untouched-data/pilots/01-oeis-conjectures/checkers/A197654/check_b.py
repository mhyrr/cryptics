"""A197654 check_b: direct DP over L/R words from the definition (see _k3/meander_b.py) vs the conjectured closed formula
(Luschny's PARI form h(n,k)*C(n,k)^5), for n <= N (small: state space grows fast)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from fractions import Fraction
from math import comb
from oeisterms import terms
from meander_b import dp_row
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
m = 5
def luschny(n, k):
    h = m if n == 1 + 2 * k else (1 + k) * (1 - Fraction(n - k, 1 + k) ** m) / (1 + 2 * k - n)
    v = h * comb(n, k) ** m; assert v.denominator == 1; return int(v)
t, off = terms('A197654'); flat = []; n = 0
while len(flat) < len(t): flat += [luschny(n, k) for k in range(n + 1)]; n += 1
assert flat[:len(t)] == t; print('terms ok (formula)', len(t))
bad = []
for n in range(N + 1):
    row = dp_row(m, n)
    if row != [luschny(n, k) for k in range(n + 1)]: bad.append(n)
    print(' n', n, 'DP row ok' if not bad or bad[-1] != n else 'MISMATCH', flush=True)
print('N', N, 'mismatches', bad)
