"""A197654 check_a: T(n,k) (m=5) by the BEST theorem (see _k3/meander_a.py) vs the conjectured closed and recursive formulas,
for 0 <= k <= n <= N. Terms reproduced from the BEST count."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from meander_a import best, closed, recursive
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 * 29
m = 5
t, off = terms('A197654'); flat = []; n = 0
while len(flat) < len(t): flat += [best(m, n, k) for k in range(n + 1)]; n += 1
assert flat[:len(t)] == t; print('terms ok', len(t))
bad = [(n, k) for n in range(N + 1) for k in range(n + 1) if not (best(m, n, k) == closed(m, n, k) == recursive(m, n, k))]
print('N', N, 'mismatches', bad[:10])
