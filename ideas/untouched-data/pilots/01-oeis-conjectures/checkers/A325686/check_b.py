"""A325686 check_b: O'Bryant's equivalent count: Sidon sets {0,u,v,n}, 0<u<v<n, i.e. the six differences
u, v, n, v-u, n-u, n-v all distinct; for each u count v with O(1) exclusions; brute force over (u,v) for small n.
Compared with the conjectured g.f. 2x^6(1+3x+3x^2+5x^3)/((1-x)^3(1+x)^2(1+x^2)(1+x+x^2)) expanded as a power series."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000

@nb.njit(cache=True)
def sidon(n):
    c = 0
    for u in range(1, n - 1):
        if 2 * u == n: continue          # u = n-u for every v
        # v-dependent coincidences among {u, v, n, v-u, n-u, n-v}: v=n-u (v=n-u, u=n-v), v=n/2 (v=n-v),
        # v=2u (v-u=u), v=(n+u)/2 (v-u=n-v); each candidate is re-tested with the full 6-difference test
        ex = np.empty(4, np.int64); k = 0
        ex[k] = n - u; k += 1
        ex[k] = 2 * u; k += 1
        if n % 2 == 0: ex[k] = n // 2; k += 1
        if (n + u) % 2 == 0: ex[k] = (n + u) // 2; k += 1
        bad = 0; seen = np.empty(4, np.int64); s = 0
        for i in range(k):
            v = ex[i]
            if v <= u or v >= n: continue
            dup = False
            for j in range(s):
                if seen[j] == v: dup = True
            if dup: continue
            seen[s] = v; s += 1
            d = np.array([u, v, n, v - u, n - u, n - v]); okk = True
            for p in range(6):
                for q in range(p):
                    if d[p] == d[q]: okk = False
            if not okk: bad += 1
        c += (n - 1 - u) - bad
    return c

@nb.njit(cache=True)
def brute(n):
    c = 0
    for u in range(1, n):
        for v in range(u + 1, n):
            d = np.array([u, v, n, v - u, n - u, n - v]); ok = True
            for p in range(6):
                for q in range(p):
                    if d[p] == d[q]: ok = False
            if ok: c += 1
    return c

@nb.njit(cache=True)
def allc(N):
    a = np.zeros(N + 1, np.int64)
    for n in range(1, N + 1): a[n] = sidon(n)
    return a
a = allc(N)
assert all(a[n] == brute(n) for n in range(1, 300))
t, off = terms('A325686'); assert list(a[0:len(t)]) == t; print('terms ok', len(t))
# g.f. series
num = [0] * 10; num[6] = 2; num[7] = 6; num[8] = 6; num[9] = 10
from numpy.polynomial import polynomial as Pl
den = [1]
for f in ([1, -1], [1, -1], [1, -1], [1, 1], [1, 1], [1, 0, 1], [1, 1, 1]): den = list(np.convolve(den, f))
den = [int(x) for x in den]
g = [0] * (N + 1)
for n in range(N + 1):
    s = num[n] if n < len(num) else 0
    for j in range(1, min(n, len(den) - 1) + 1): s -= den[j] * g[n - j]
    g[n] = s
bad = [n for n in range(1, N + 1) if g[n] != a[n]]
print('N', N, 'g.f. mismatches', bad[:10])
