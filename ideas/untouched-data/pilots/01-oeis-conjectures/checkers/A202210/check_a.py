"""A202210 check_a: exact integer coefficients of A = F^(1/3), F = sum 3^m(2m+1) x^(m(m+1)/2),
via the power-rule recurrence 3n a_n = sum_{k>=1} (4k-3n) F_k a_{n-k} (sparse F).
Tests conjecture a(5n+4) == 0 mod 5 for n <= N."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
L = 5 * N + 5
F = {}
m = 0
while m * (m + 1) // 2 <= L:
    F[m * (m + 1) // 2] = 3**m * (2 * m + 1); m += 1
Fk = sorted(k for k in F if k > 0)
a = [1]
for n in range(1, L):
    s = 0
    for k in Fk:
        if k > n: break
        s += (4 * k - 3 * n) * F[k] * a[n - k]
    assert s % (3 * n) == 0
    a.append(s // (3 * n))
t, off = terms('A202210')
assert a[:len(t)] == t, 'terms mismatch'
print('terms ok', len(t))
bad = [n for n in range(N + 1) if a[5 * n + 4] % 5]
print('N', N, 'violations', bad[:10])
