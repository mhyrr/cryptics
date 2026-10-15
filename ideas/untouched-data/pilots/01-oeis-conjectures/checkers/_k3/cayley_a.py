"""check_a engine for A297180/1/2 (base b): word length L(x) in the Cayley graph of Z w.r.t. {+-b^k}.
L by the LSB-first carry DP: f0' = min(f0+d, f1+d+1), f1' = min(f0+b-d, f1+b-d-1); L = min(f0, f1+1).
M(X) = max_{0<=x<X} L(x) by a digit DP (LSB-first) over x with state (f1-f0, comparison flag of low parts), value max f0.
a(n) is certified as the least x>0 with L(x)=n when L(a(n)) = n and M(a(n)) = n-1."""
import numpy as np, numba as nb

def L(x, b):
    f0, f1 = 0, 10**9
    while x:
        x, d = divmod(x, b)
        f0, f1 = min(f0 + d, f1 + d + 1), min(f0 + b - d, f1 + b - d - 1)
    return min(f0, f1 + 1)

@nb.njit(cache=True)
def maxL_below(dig, b):
    # dig: base-b digits of X, least significant first. returns max L(x) over 0 <= x < X.
    OFF = 2 * b + 2; W = 2 * OFF + 1
    NEG = -10**9
    best = np.full((W, 3), NEG, np.int64)   # [delta+OFF, flag] flag 0: x_low < X_low, 1: equal, 2: greater
    # before any digit: f0 = 0, f1 = +inf  -> represent f1 as f0 + big: clip delta to OFF
    best[OFF + OFF, 1] = 0
    for i in range(len(dig)):
        Xi = dig[i]
        nb_ = np.full((W, 3), NEG, np.int64)
        for di in range(W):
            delta = di - OFF
            for fl in range(3):
                v = best[di, fl]
                if v == NEG: continue
                f0 = v; f1 = v + delta
                for d in range(b):
                    g0 = min(f0 + d, f1 + d + 1); g1 = min(f0 + b - d, f1 + b - d - 1)
                    nd = g1 - g0
                    if nd > OFF: nd = OFF
                    if nd < -OFF: nd = -OFF
                    if d < Xi: nfl = 0
                    elif d > Xi: nfl = 2
                    else: nfl = fl
                    if g0 > nb_[nd + OFF, nfl]: nb_[nd + OFF, nfl] = g0
        best = nb_
    m = NEG
    for di in range(W):
        v = best[di, 0]
        if v == NEG: continue
        val = min(v, v + (di - OFF) + 1)
        if val > m: m = val
    return m
