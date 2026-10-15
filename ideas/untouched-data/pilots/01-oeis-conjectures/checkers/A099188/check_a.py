# A099188: a(n) = 2*ceil(n/sqrt 2). Conjecture: a(n) = length of a shortest polygonal path from (0,0) to (n,n)
# with integer vertices and integer edge lengths (tested to n=10000).
# Lower bound is a proof (recorded here, also asserted numerically): an integer vector (x,y) of integer length c has
# c == x+y (mod 2), so the total length is == 2n == 0 (mod 2); and it is > n*sqrt2 (no lattice vector along the
# diagonal has integer length), hence >= 2*ceil(n/sqrt2). So the conjecture <=> a path of length E=2*ceil(n/sqrt2) exists.
# Method a: explicit witness by DFS over edge types (u=x+y, c) of the near-diagonal Pythagorean vectors with
# |x-y| = 1: (0,1,1),(3,4,5),(20,21,29),(119,120,169),... (u odd, so the count is even and the x-y offsets
# can be cancelled by orienting half of them each way). Each witness path is rebuilt and checked exactly.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from math import isqrt
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
def E(n): return 0 if n == 0 else 2 * (isqrt((n * n - 1) // 2) + 1)
check_terms("A099188", E)
# Pell-type vectors (x, x+1, c) with x^2+(x+1)^2=c^2
types = [(0, 1, 1)]
x, y, c = 3, 4, 5
while x + y <= 2 * N + 2:
    types.append((x, y, c)); x, y, c = 3 * x + 2 * c + 1, 3 * x + 2 * c + 2, 4 * x + 3 * c + 2
types.sort(key=lambda t: -(t[0] + t[1]))
U = [t[0] + t[1] for t in types]; C = [t[2] for t in types]
import sys as _s; _s.setrecursionlimit(10000)
def dfs(i, u, c, acc):
    if u == 0 and c == 0: return acc
    if i == len(types) or u <= 0 or c <= 0: return None
    if c > u or 2 * c * c <= u * u: return None        # each type has u/sqrt2 < c <= u
    if i == len(types) - 2:                             # last two types (3,4,5) and (0,1,1): solve directly
        # x7*7 + x1 = u ; x7*5 + x1 = c
        if (u - c) % 2: return None
        x7 = (u - c) // 2; x1 = u - 7 * x7
        if x7 < 0 or x1 < 0: return None
        return acc + [(types[i], x7), (types[i + 1], x1)]
    hi = u // U[i]
    for k in range(hi, -1, -1):
        r = dfs(i + 1, u - k * U[i], c - k * C[i], acc + ([(types[i], k)] if k else []))
        if r is not None: return r
    return None
def verify(n, w):
    vecs = []
    for (x, y, c), k in w: vecs += [(x, y, c)] * k
    # orient: alternate (x,y) and (y,x) so that the x-y offsets cancel (count is even since every u is odd)
    assert len(vecs) % 2 == 0
    px = py = L = 0
    for j, (x, y, c) in enumerate(vecs):
        if j % 2: x, y = y, x
        assert x * x + y * y == c * c
        px += x; py += y; L += c
    return (px, py, L) == (n, n, E(n))
fail = []
for n in range(1, N + 1):
    w = dfs(0, 2 * n, E(n), [])
    if w is None or not verify(n, w): fail.append(n)
    if n % 20000 == 0: print("n =", n, "failures so far:", fail[:10], flush=True)
print("N =", N, "n without a length-E witness from this family:", fail[:20], "count", len(fail))
