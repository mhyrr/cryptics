"""A297181 check_b (base 11): same certification with the MSB-first DP (see _k3/cayley_b.py); a(n) from the conjectured
g.f. denominator recurrence; first terms re-derived by BFS in the Cayley graph."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from oeisterms import terms
from cayley_b import L, maxL_below, digits, bfs_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
b = 11; k = b // 2
t, off = terms('A297181')
# g.f. x*(1+x+..+x^(k-1) - (b-1)x^k)/((1-x)(1-b x^k)): series coefficients
num = [0] + [1] * k + [-(b - 1)]
den = [0] * (k + 2); den[0] = 1; den[1] = -1; den[k] = -b; den[k + 1] = b   # (1-x)(1-b x^k)
a = [0] * (N + 1)
for n in range(N + 1):
    s = num[n] if n < len(num) else 0
    for j in range(1, min(n, k + 1) + 1): s -= den[j] * a[n - j]
    a[n] = s
assert a[1:len(t) + 1] == t, 'g.f. does not reproduce data'
bt = bfs_terms(b, 4 * 10**5, 12)
assert [x for x in bt if x is not None] == t[:len([x for x in bt if x is not None])]
print('terms ok', len(t), '(BFS for first', len([x for x in bt if x is not None]), ')')
bad = []
for n in range(1, N + 1):
    if not (L(a[n], b) == n and maxL_below(np.array(digits(a[n], b), np.int64), b) == n - 1): bad.append(n)
print('N', N, 'failures', bad[:10])
