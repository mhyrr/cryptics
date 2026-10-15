"""A202438 check_a: exact integer coefficients of A = F^(-1/3), F = sum 9^m(2m+1)(-x)^(m(m+1)/2),
via power-rule recurrence 3n a_n = sum_{k>=1} (2k-3n) F_k a_{n-k} (sparse F).
Tests a(25n+24) == 0 mod 25 for n <= N25 and a(7n+5) == 0 mod 7 for n <= N7."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
N25 = int(sys.argv[1]) if len(sys.argv) > 1 else 500
N7 = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
L = max(25 * N25 + 25, 7 * N7 + 6)
F = {}; m = 0
while m * (m + 1) // 2 <= L:
    T = m * (m + 1) // 2; F[T] = 9**m * (2 * m + 1) * (-1) ** (T % 2); m += 1
Fk = sorted(k for k in F if k > 0)
a = [1]
for n in range(1, L):
    s = 0
    for k in Fk:
        if k > n: break
        s += (2 * k - 3 * n) * F[k] * a[n - k]
    assert s % (3 * n) == 0
    a.append(s // (3 * n))
t, off = terms('A202438')
assert a[:len(t)] == t, 'terms mismatch'
print('terms ok', len(t))
b25 = [n for n in range(N25 + 1) if a[25 * n + 24] % 25]
b7 = [n for n in range(N7 + 1) if a[7 * n + 5] % 7]
b5 = [n for n in range((L - 5) // 5) if a[5 * n + 4] % 5]
print('N25', N25, 'viol25', b25[:10], '| N7', N7, 'viol7', b7[:10], '| proven mod5 sanity viol', b5[:5])
