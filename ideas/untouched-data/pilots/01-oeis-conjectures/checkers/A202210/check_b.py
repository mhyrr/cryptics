"""A202210 check_b: solve A^3 = F coefficient by coefficient ([x^n]A^3 = 3a_n + lower terms),
exact for the listed terms, then modulo 5 with numpy for the conjecture a(5n+4) == 0 mod 5."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
M = 5

def Fcoef(L, mod=None):
    f = [0] * L; m = 0
    while m * (m + 1) // 2 < L:
        v = 3**m * (2 * m + 1); f[m * (m + 1) // 2] = v % mod if mod else v; m += 1
    return f

def cuberoot_exact(f, L):
    a = [1] + [0] * (L - 1); a2 = [1] + [0] * (L - 1)
    for n in range(1, L):
        a2p = sum(a[i] * a[n - i] for i in range(1, n))
        c = a2p + sum(a[i] * a2[n - i] for i in range(1, n))
        r = f[n] - c; assert r % 3 == 0
        a[n] = r // 3; a2[n] = 2 * a[n] + a2p
    return a

t, off = terms('A202210')
ae = cuberoot_exact(Fcoef(len(t)), len(t))
assert ae == t, 'terms mismatch'
print('terms ok', len(t))
L = 5 * N + 5
f = np.array(Fcoef(L, M), dtype=np.int64)
a = np.zeros(L, dtype=np.int64); a2 = np.zeros(L, dtype=np.int64); a[0] = 1; a2[0] = 1
inv3 = pow(3, -1, M)
for n in range(1, L):
    a2p = int(np.dot(a[1:n], a[n-1:0:-1]) % M) if n > 1 else 0
    c = (a2p + (int(np.dot(a[1:n], a2[n-1:0:-1]) % M) if n > 1 else 0)) % M
    a[n] = (f[n] - c) * inv3 % M
    a2[n] = (2 * a[n] + a2p) % M
bad = [n for n in range(N + 1) if a[5 * n + 4] % 5]
print('N', N, 'violations', bad[:10])
