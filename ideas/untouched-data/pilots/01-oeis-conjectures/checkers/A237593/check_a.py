"""A237593 check_a: Conjecture 2 (Dyck path n never crosses path n-1, i.e. its column heights dominate).
Rows from A237591 via s(n,k)=ceil((n+1)/k-(k+1)/2)-ceil((n+1)/(k+1)-(k+2)/2) in exact integer arithmetic;
paths compared as step functions by merging O(sqrt n) breakpoints. Also checks area(n)-area(n-1)=sigma(n)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000

@nb.njit(cache=True)
def cdiv(a, b):
    return -((-a) // b)

@nb.njit(cache=True)
def row(n, out):
    # A235791(n,k) = ceil((n+1)/k - (k+1)/2) = ceil((2n+2 - k(k+1)) / (2k)); returns length of full row (2j)
    j = 0
    while (j + 1) * (j + 2) // 2 <= n: j += 1
    for k in range(1, j + 1):
        out[k - 1] = cdiv(2 * n + 2 - k * (k + 1), 2 * k) - cdiv(2 * n + 2 - (k + 1) * (k + 2), 2 * (k + 1))
    for k in range(j):
        out[2 * j - 1 - k] = out[k]
    return 2 * j

@nb.njit(cache=True)
def segs(n, r, L, xs, hs):
    # horizontal segments: start x and height; returns count
    h = n; x = 0; c = 0
    for i in range(L):
        if i % 2 == 0:
            xs[c] = x; hs[c] = h; c += 1; x += r[i]
        else:
            h -= r[i]
    xs[c] = x; hs[c] = 0; c += 1   # beyond: height 0 (end at x=n)
    return c

@nb.njit(cache=True)
def run(N, sig):
    r = np.zeros(4000, np.int64); xa = np.zeros(4000, np.int64); ha = np.zeros(4000, np.int64)
    xb = np.zeros(4000, np.int64); hb = np.zeros(4000, np.int64)
    L = row(1, r); ca = segs(1, r, L, xa, ha)
    area_prev = 0
    for i in range(ca - 1): area_prev += (xa[i + 1] - xa[i]) * ha[i]
    nbad = 0; firstbad = -1; areabad = -1
    for n in range(2, N + 1):
        L = row(n, r); cb = segs(n, r, L, xb, hb)
        # compare step functions on [0, n): at every breakpoint of either
        i = 0; k = 0
        while i < cb - 1 or k < ca - 1:
            x = xb[i] if xb[i] > xa[k] else xa[k]
            while i + 1 < cb and xb[i + 1] <= x: i += 1
            while k + 1 < ca and xa[k + 1] <= x: k += 1
            if x < n and hb[i] < ha[k]:
                nbad += 1
                if firstbad < 0: firstbad = n
                break
            nx = n
            if i + 1 < cb and xb[i + 1] < nx: nx = xb[i + 1]
            if k + 1 < ca and xa[k + 1] < nx: nx = xa[k + 1]
            if nx >= n: break
            if i + 1 < cb and xb[i + 1] == nx: i += 1
            if k + 1 < ca and xa[k + 1] == nx: k += 1
            if hb[i] < ha[k]:
                nbad += 1
                if firstbad < 0: firstbad = n
                break
        area = 0
        for q in range(cb - 1): area += (xb[q + 1] - xb[q]) * hb[q]
        if area - area_prev != sig[n] and areabad < 0: areabad = n
        area_prev = area
        for q in range(cb): xa[q] = xb[q]; ha[q] = hb[q]
        ca = cb
    return nbad, firstbad, areabad

t, off = terms('A237593')
r = np.zeros(4000, np.int64); flat = []
n = 1
while len(flat) < len(t):
    L = row(n, r); flat += list(r[:L]); n += 1
assert flat[:len(t)] == t; print('terms ok', len(t))
sig = np.zeros(N + 1, np.int64)
for d in range(1, N + 1): sig[d::d] += d
print('N', N, 'result (nbad, first crossing n, first area mismatch n):', run(N, sig))
