# A099188 checker b.
# (1) Exhaustive for n <= NS: Dijkstra over lattice points with ALL integer-length lattice vectors (any direction,
#     non-primitive included) of length <= 2n, i.e. the true minimum, compared to 2*ceil(n/sqrt2).
# (2) For n <= N: reachability DP (Python big-int bitsets) over (sum of x+y, total length) using every Pythagorean
#     vector with |x-y| <= 7 and length <= E(N) (both orientations), tracking the x-y offset too:
#     state = (length L, offset d) -> bitset over u = x+y. Conjecture holds at n iff state (E(n), 0) has bit 2n.
import sys, os, heapq; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from math import isqrt, ceil, sqrt
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 40
def E(n):
    m = 0
    while 2 * m * m < n * n: m += 1      # ceil(n/sqrt2) by exact search
    return 2 * m
check_terms("A099188", E)
# (1) exhaustive small n
def shortest(n):
    R = 2 * n + 2
    vecs = [(x, y, isqrt(x * x + y * y)) for x in range(-R, R + 1) for y in range(-R, R + 1)
            if (x or y) and isqrt(x * x + y * y) ** 2 == x * x + y * y and x * x + y * y <= (2 * n) ** 2]
    dist = {(0, 0): 0}; pq = [(0, 0, 0)]
    while pq:
        d, px, py = heapq.heappop(pq)
        if (px, py) == (n, n): return d
        if d > dist.get((px, py), 1 << 60): continue
        for x, y, c in vecs:
            q = (px + x, py + y)
            if -n <= q[0] <= 2 * n and -n <= q[1] <= 2 * n and d + c < dist.get(q, 1 << 60) and d + c <= 2 * n:
                dist[q] = d + c; heapq.heappush(pq, (d + c, q[0], q[1]))
bad_small = [n for n in range(1, NS + 1) if shortest(n) != E(n)]
print("exhaustive n <= %d mismatches:" % NS, bad_small)
# (2) bitset DP
LMAX = E(N); D = 7
types = []
for x in range(0, LMAX + 1):
    for y in range(max(0, x - D), x + D + 1):
        s = x * x + y * y; c = isqrt(s)
        if c * c == s and 0 < c <= LMAX: types.append((x + y, x - y, c))
types = sorted(set(types))
print("vector types used (u, d, c):", len(types))
reach = [dict() for _ in range(LMAX + 1)]   # reach[L][d] = bitset over u
reach[0][0] = 1
for L in range(1, LMAX + 1):
    cur = reach[L]
    for u, d, c in types:
        if c > L: continue
        for d0, bs in reach[L - c].items():
            nd = d0 + d
            if abs(nd) > D: continue
            cur[nd] = cur.get(nd, 0) | (bs << u)
    mask = (1 << (2 * N + 1)) - 1
    for k in cur: cur[k] &= mask
fail = [n for n in range(1, N + 1) if not (reach[E(n)].get(0, 0) >> (2 * n)) & 1]
print("N =", N, "n without a length-E path (this vector family):", fail[:20], "count", len(fail))
