"""Meanders / binary curves of A194595 (m=3) and A197653 (m=4).
T(n,k) = #words S over {L,R} of length m(n+1), first letter L, with m(k+1) L's, such that every dir index
0..m-1 occurs exactly n+1 times, where the first letter has index 0 and each later letter moves the index
+1 (L after L), -1 (R after R) mod m, or keeps it (letter change).
Conjectured closed form (both entries): T(n,n)=1, T(n,k) = Sum_{j=0..m-1} C(n,k)^(m-j) C(n,n-1-k)^j for k<n.

method a: forward DP, state (counts c_0..c_{m-2} [c_{m-1} implied], index, last letter, #L); additions only,
          modulo 5 primes < 2^62, CRT.
method b: forward DP WITHOUT the #L coordinate, each L step weighted by y; run for y = 0..m(n+1) modulo primes
          < 2^31 (products fit int64), recover the #L-polynomial by Lagrange interpolation mod p, then CRT.
brute(): exhaustive enumeration for small n (validates the reading of the definition against the data).
"""
import numpy as np, numba
from math import comb
from itertools import product

def closed(n, k, m):
    if k == n: return 1
    a, b = comb(n, k), comb(n, n - 1 - k)
    return sum(a ** (m - j) * b ** j for j in range(m))

def brute(n, m):
    Lt = m * (n + 1); out = [0] * (n + 1)
    for rest in product((0, 1), repeat=Lt - 1):
        S = (0,) + rest; c = [0] * m; i = 0; c[0] = 1
        for a, b in zip(S, S[1:]):
            if a == b: i = (i + (1 if b == 0 else -1)) % m
            c[i] += 1
        if all(x == n + 1 for x in c):
            nl = S.count(0)
            if nl % m == 0: out[nl // m - 1] += 1
    return out

@numba.njit(cache=True)
def _a3(n, p):
    K = n + 1; Lt = 3 * K
    cur = np.zeros((K + 1, K + 1, 3, 2, Lt + 1), dtype=np.int64)
    cur[1, 0, 0, 0, 1] = 1
    for pos in range(1, Lt):
        nxt = np.zeros_like(cur)
        for c0 in range(min(pos, K) + 1):
            for c1 in range(min(pos - c0, K) + 1):
                c2 = pos - c0 - c1
                if c2 > K: continue
                for idx in range(3):
                    for last in range(2):
                        for nl in range(pos + 1):
                            v = cur[c0, c1, idx, last, nl]
                            if v == 0: continue
                            for let in range(2):
                                if let == last: ni = (idx + 1) % 3 if let == 0 else (idx + 2) % 3
                                else: ni = idx
                                d0 = c0 + (ni == 0); d1 = c1 + (ni == 1); d2 = c2 + (ni == 2)
                                if d0 > K or d1 > K or d2 > K: continue
                                nn = nl + (let == 0)
                                w = nxt[d0, d1, ni, let, nn] + v
                                if w >= p: w -= p
                                nxt[d0, d1, ni, let, nn] = w
        cur = nxt
    out = np.zeros(n + 1, dtype=np.int64)
    for k in range(n + 1):
        s = 0
        for idx in range(3):
            for last in range(2):
                s = (s + cur[K, K, idx, last, 3 * (k + 1)]) % p
        out[k] = s
    return out

@numba.njit(cache=True)
def _a4(n, p):
    K = n + 1; Lt = 4 * K
    cur = np.zeros((K + 1, K + 1, K + 1, 4, 2, Lt + 1), dtype=np.int64)
    cur[1, 0, 0, 0, 0, 1] = 1
    for pos in range(1, Lt):
        nxt = np.zeros_like(cur)
        for c0 in range(min(pos, K) + 1):
            for c1 in range(min(pos - c0, K) + 1):
                for c2 in range(min(pos - c0 - c1, K) + 1):
                    c3 = pos - c0 - c1 - c2
                    if c3 > K: continue
                    for idx in range(4):
                        for last in range(2):
                            for nl in range(pos + 1):
                                v = cur[c0, c1, c2, idx, last, nl]
                                if v == 0: continue
                                for let in range(2):
                                    if let == last: ni = (idx + 1) % 4 if let == 0 else (idx + 3) % 4
                                    else: ni = idx
                                    d0 = c0 + (ni == 0); d1 = c1 + (ni == 1); d2 = c2 + (ni == 2); d3 = c3 + (ni == 3)
                                    if d0 > K or d1 > K or d2 > K or d3 > K: continue
                                    nn = nl + (let == 0)
                                    w = nxt[d0, d1, d2, ni, let, nn] + v
                                    if w >= p: w -= p
                                    nxt[d0, d1, d2, ni, let, nn] = w
        cur = nxt
    out = np.zeros(n + 1, dtype=np.int64)
    for k in range(n + 1):
        s = 0
        for idx in range(4):
            for last in range(2):
                s = (s + cur[K, K, K, idx, last, 4 * (k + 1)]) % p
        out[k] = s
    return out

@numba.njit(cache=True)
def _b(n, m, p, y):
    # counts state flattened: we keep a dict-free dense array over (c_0..c_{m-2}) with mixed radix K+1
    K = n + 1; Lt = m * K
    R = 1
    for _ in range(m - 1): R *= (K + 1)
    cur = np.zeros((R, m, 2), dtype=np.int64)
    cur[1, 0, 0] = y % p          # first letter L (weight y), index 0: c_0 = 1 -> flat index 1
    digits = np.zeros(m, dtype=np.int64)
    for pos in range(1, Lt):
        nxt = np.zeros_like(cur)
        for f in range(R):
            # decode counts
            t = f; s = 0
            for j in range(m - 1):
                digits[j] = t % (K + 1); t //= (K + 1); s += digits[j]
            cl = pos - s
            if cl < 0 or cl > K: continue
            for idx in range(m):
                for last in range(2):
                    v = cur[f, idx, last]
                    if v == 0: continue
                    for let in range(2):
                        if let == last: ni = (idx + 1) % m if let == 0 else (idx + m - 1) % m
                        else: ni = idx
                        if ni == m - 1:
                            if cl + 1 > K: continue
                            g = f
                        else:
                            if digits[ni] + 1 > K: continue
                            g = f
                            mul = 1
                            for j in range(ni): mul *= (K + 1)
                            g = f + mul
                        w = v * y % p if let == 0 else v
                        nxt[g, ni, last * 0 + let] = (nxt[g, ni, let] + w) % p
        cur = nxt
    full = 0; mul = 1
    for j in range(m - 1): full += K * mul; mul *= (K + 1)
    s = 0
    for idx in range(m):
        for last in range(2): s = (s + cur[full, idx, last]) % p
    return s

def _interp(vals, p):
    """values at y=0..D of a degree<=D polynomial mod p -> coefficients (Lagrange via Newton forward differences)."""
    D = len(vals) - 1
    # Newton divided differences on nodes 0..D
    c = list(vals)
    for j in range(1, D + 1):
        inv = pow(j, -1, p)
        for i in range(D, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) * inv % p
    # expand Newton form sum c_j prod_{i<j} (y - i)
    poly = [0] * (D + 1); basis = [1]
    for j in range(D + 1):
        for t, b in enumerate(basis): poly[t] = (poly[t] + c[j] * b) % p
        nb = [0] * (len(basis) + 1)
        for t, b in enumerate(basis):
            nb[t] = (nb[t] - j * b) % p; nb[t + 1] = (nb[t + 1] + b) % p
        basis = nb
    return poly

PA = [4611686018427387847, 4611686018427387817, 4611686018427387787, 4611686018427387761, 4611686018427387733]
def _primes31(cnt):
    from sympy import prevprime
    out = []; p = 2 ** 31
    while len(out) < cnt: p = prevprime(p); out.append(p)
    return out

def crt(res):
    x, M = 0, 1
    for r, p in res:
        t = ((r - x) * pow(M, -1, p)) % p; x += M * t; M *= p
    return x, M

def row(n, m, method):
    if method == "a":
        f = _a3 if m == 3 else _a4
        rows = [f(n, p) for p in PA]
        res = [crt([(int(rows[i][k]), PA[i]) for i in range(len(PA))]) for k in range(n + 1)]
    else:
        need = m * (n + 1) + 8
        PB = _primes31(need // 30 + 1)
        D = m * (n + 1)
        polys = []
        for p in PB:
            vals = [int(_b(n, m, p, y)) for y in range(D + 1)]
            polys.append(_interp(vals, p))
        res = [crt([(polys[i][m * (k + 1)], PB[i]) for i in range(len(PB))]) for k in range(n + 1)]
    out = []
    for x, M in res:
        assert 2 ** (m * (n + 1)) < M
        out.append(x)
    return out
