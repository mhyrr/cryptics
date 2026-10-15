"""A295431 check_a: a(n) = (12n)! n! / ((6n)! (4n)! (3n)!). Using Legendre's formula for v_p, test for n <= N:
(i) 5*7*11*a(n)/(n+1), (ii) 5*a(n)/(2n+1), (iii) a(n)/(3n+1), (iv) 2*5*7*11*a(n)/((n+1)(2n+1)(3n+1)) are integers."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from math import factorial
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
t, off = terms('A295431')
assert [factorial(12*n)*factorial(n)//(factorial(6*n)*factorial(4*n)*factorial(3*n)) for n in range(len(t))] == t
print('terms ok', len(t))
M = 3 * N + 2
spf = list(range(M + 1))
for i in range(2, int(M**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def fac(x):
    f = {}
    while x > 1: p = spf[x]; f[p] = f.get(p, 0) + 1; x //= p
    return f
def leg(m, p):
    v = 0
    while m: m //= p; v += m
    return v
def va(n, p): return leg(12*n, p) + leg(n, p) - leg(6*n, p) - leg(4*n, p) - leg(3*n, p)
def ok(n, c, ds):
    need = {}
    for d in ds:
        for p, e in fac(d).items(): need[p] = need.get(p, 0) + e
    cf = fac(c)
    return all(va(n, p) + cf.get(p, 0) >= e for p, e in need.items())
bad = {1: [], 2: [], 3: [], 4: []}
for n in range(0, N + 1):
    if not ok(n, 385, [n + 1]): bad[1].append(n)
    if not ok(n, 5, [2 * n + 1]): bad[2].append(n)
    if not ok(n, 1, [3 * n + 1]): bad[3].append(n)
    if not ok(n, 770, [n + 1, 2 * n + 1, 3 * n + 1]): bad[4].append(n)
print('N', N, 'failures (i)-(iv):', {k: v[:10] for k, v in bad.items()})
