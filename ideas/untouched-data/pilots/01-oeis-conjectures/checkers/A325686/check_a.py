"""A325686 check_a: a(n) = #{(x,y,z) distinct positive, x+y+z=n, x+y!=z, x!=y+z}. For each x count admissible y in
O(1) by removing the (at most 4) excluded y values; brute O(n^2) for small n as cross-check. Conjecture (Barker):
a(n) = a(n-2)+a(n-3)+a(n-4)-a(n-5)-a(n-6)-a(n-7)+a(n-9) for n>9 (equivalently the g.f.)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000

@nb.njit(cache=True)
def count(n):
    c = 0
    for x in range(1, n - 1):
        if 2 * x == n: continue           # x = y+z for every y
        m = n - x - 1                      # y in 1..m, z = n-x-y >= 1
        ex = np.empty(4, np.int64); k = 0
        ex[k] = x; k += 1                   # y = x
        ex[k] = n - 2 * x; k += 1           # z = x
        if (n - x) % 2 == 0: ex[k] = (n - x) // 2; k += 1        # z = y
        if (n - 2 * x) % 2 == 0: ex[k] = (n - 2 * x) // 2; k += 1  # x + y = z
        bad = 0
        for i in range(k):
            v = ex[i]
            if v < 1 or v > m: continue
            dup = False
            for j in range(i):
                if ex[j] == v: dup = True
            if not dup: bad += 1
        c += m - bad
    return c

@nb.njit(cache=True)
def brute(n):
    c = 0
    for x in range(1, n):
        for y in range(1, n - x):
            z = n - x - y
            if x != y and y != z and x != z and x + y != z and x != y + z: c += 1
    return c

@nb.njit(cache=True)
def allcounts(N):
    a = np.zeros(N + 1, np.int64)
    for n in range(N + 1): a[n] = count(n)
    return a
a = allcounts(N)
assert all(a[n] == brute(n) for n in range(300))
t, off = terms('A325686'); assert list(a[0:len(t)]) == t; print('terms ok', len(t))
bad = [n for n in range(10, N + 1) if a[n] != a[n-2]+a[n-3]+a[n-4]-a[n-5]-a[n-6]-a[n-7]+a[n-9]]
print('N', N, 'recurrence failures', bad[:10])
