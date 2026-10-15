"""check_a engine for A197654 (m=5) / A197655 (m=6): meanders = closed walks on the m-cycle (L: h->h+1 labelled h+1,
R: h->h-1 labelled h) starting with L, each edge label used n+1 times, m(k+1) L's. Count by the BEST theorem:
#Eulerian circuits = t_0 * prod (outdeg-1)!, arborescence count t_0 from the Kirchhoff determinant (exact Fractions),
times a (first arc forward) / (a!^m b!^m) (parallel arcs indistinguishable), a = k+1, b = n-k.
Compared with the conjectured closed formula sum_j C(n,k)^(m-j) C(n,n-1-k)^j and the recursive formula."""
from fractions import Fraction
from math import comb, factorial

def det(M):
    M = [[Fraction(x) for x in r] for r in M]; n = len(M); d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None: return Fraction(0)
        if p != c: M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            if f:
                for w in range(c, n): M[r][w] -= f * M[c][w]
    return d

def best(m, n, k):
    if k == n: return 1
    a, b = k + 1, n - k
    # Laplacian for in-arborescences rooted at 0: L = D_out - A
    Lap = [[0] * m for _ in range(m)]
    for v in range(m):
        Lap[v][v] += a + b
        Lap[v][(v + 1) % m] -= a
        Lap[v][(v - 1) % m] -= b
    t0 = det([row[1:] for row in Lap[1:]])
    val = t0 * Fraction(factorial(n)) ** m * a / (Fraction(factorial(a)) ** m * Fraction(factorial(b)) ** m)
    assert val.denominator == 1
    return int(val)

def closed(m, n, k):
    if k == n: return 1
    return sum(comb(n, k) ** (m - j) * comb(n, n - 1 - k) ** j for j in range(m))

def recursive(m, n, k):
    if k == n: return 1
    if m == 1: return comb(n, k)
    return comb(n, k) ** m + comb(n, k) * recursive(m - 1, n, n - 1 - k)
