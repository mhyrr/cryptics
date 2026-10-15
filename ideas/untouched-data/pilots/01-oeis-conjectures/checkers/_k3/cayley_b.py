"""check_b engine for A297180/1/2 (base b): MSB-first formulation. g_c = min cost of the digits from here upward given
carry c into this position; g'_c = min(d+c+g_0, b-d-c+g_1); above the top g = (0, 1); L(x) = g_0 after the last digit.
max over 0 <= x < X with a tight/free flag (MSB-first), state delta = g1-g0, value max g0. Terms also reproduced by
BFS over a window of integers."""
import numpy as np, numba as nb

def L(x, b):
    g0, g1 = 0, 1
    for d in reversed(digits(x, b)):
        g0, g1 = min(d + g0, b - d + g1), min(d + 1 + g0, b - d - 1 + g1)
    return g0

def digits(x, b):
    out = []
    while x: x, d = divmod(x, b); out.append(d)
    return out

@nb.njit(cache=True)
def maxL_below(dig, b):
    OFF = 2 * b + 2; W = 2 * OFF + 1; NEG = -10**9
    best = np.full((W, 2), NEG, np.int64)    # flag 0: free (already smaller), 1: tight
    best[1 + OFF, 1] = 0                      # g0=0, g1=1
    for i in range(len(dig) - 1, -1, -1):
        Xi = dig[i]
        nb_ = np.full((W, 2), NEG, np.int64)
        for di in range(W):
            for fl in range(2):
                v = best[di, fl]
                if v == NEG: continue
                g0 = v; g1 = v + di - OFF
                top = b - 1 if fl == 0 else Xi
                for d in range(top + 1):
                    if fl == 1 and d == Xi: nfl = 1
                    else: nfl = 0
                    h0 = min(d + g0, b - d + g1); h1 = min(d + 1 + g0, b - d - 1 + g1)
                    nd = h1 - h0
                    if nd > OFF: nd = OFF
                    if nd < -OFF: nd = -OFF
                    if h0 > nb_[nd + OFF, nfl]: nb_[nd + OFF, nfl] = h0
        best = nb_
    m = NEG
    for di in range(W):
        if best[di, 0] > m: m = best[di, 0]   # strictly less than X
    return m

def bfs_terms(b, limit, count):
    # BFS distances on integers in [-limit, limit] with generators +-b^k (paths may leave the window; window chosen big)
    from collections import deque
    gens = []; p = 1
    while p <= 2 * limit: gens += [p, -p]; p *= b
    dist = {0: 0}; q = deque([0]); first = {}
    while q:
        x = q.popleft()
        for g in gens:
            y = x + g
            if -limit <= y <= limit and y not in dist:
                dist[y] = dist[x] + 1; q.append(y)
    res = []
    for n in range(1, count + 1):
        c = [x for x, d in dist.items() if d == n and x > 0]
        res.append(min(c) if c else None)
    return res
