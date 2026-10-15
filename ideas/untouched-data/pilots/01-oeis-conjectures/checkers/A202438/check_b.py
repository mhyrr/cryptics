"""A202438 check_b: G = 1/F by series inversion, then solve A^3 = G coefficient by coefficient,
exact for listed terms, then modulo 175 = 25*7 with numpy for both conjectures."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np
from oeisterms import terms
N25 = int(sys.argv[1]) if len(sys.argv) > 1 else 500
N7 = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
M = 175

def Fcoef(L, mod=None):
    f = [0] * L; m = 0
    while m * (m + 1) // 2 < L:
        T = m * (m + 1) // 2; v = 9**m * (2 * m + 1) * (-1) ** (T % 2)
        f[T] = v % mod if mod else v; m += 1
    return f

def inv(f, L, mod=None):
    g = [1] + [0] * (L - 1); nz = [k for k in range(1, L) if f[k]]
    for n in range(1, L):
        s = -sum(f[k] * g[n - k] for k in nz if k <= n)
        g[n] = s % mod if mod else s
    return g

def cuberoot_exact(f, L):
    a = [1] + [0] * (L - 1); a2 = [1] + [0] * (L - 1)
    for n in range(1, L):
        a2p = sum(a[i] * a[n - i] for i in range(1, n))
        c = a2p + sum(a[i] * a2[n - i] for i in range(1, n))
        r = f[n] - c; assert r % 3 == 0
        a[n] = r // 3; a2[n] = 2 * a[n] + a2p
    return a

t, off = terms('A202438')
assert cuberoot_exact(inv(Fcoef(len(t)), len(t)), len(t)) == t, 'terms mismatch'
print('terms ok', len(t))
L = max(25 * N25 + 25, 7 * N7 + 6)
g = np.array(inv(Fcoef(L, M), L, M), dtype=np.int64)
a = np.zeros(L, dtype=np.int64); a2 = np.zeros(L, dtype=np.int64); a[0] = 1; a2[0] = 1
inv3 = pow(3, -1, M)
for n in range(1, L):
    if n > 1:
        a2p = int(np.dot(a[1:n], a[n-1:0:-1]) % M); c = (a2p + int(np.dot(a[1:n], a2[n-1:0:-1]) % M)) % M
    else:
        a2p = 0; c = 0
    a[n] = (g[n] - c) * inv3 % M; a2[n] = (2 * a[n] + a2p) % M
b25 = [n for n in range(N25 + 1) if a[25 * n + 24] % 25]
b7 = [n for n in range(N7 + 1) if a[7 * n + 5] % 7]
print('N25', N25, 'viol25', b25[:10], '| N7', N7, 'viol7', b7[:10])
