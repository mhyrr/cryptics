# Shared hypergraph construction for A397315 checkers (rectangles with lattice corners, incl. tilted; edges = symmetric
# differences of corner sets of distinct rectangles, reduced to inclusion-minimal ones).
from itertools import combinations
def rectangles(n, k):
    P = [(x, y) for x in range(k) for y in range(n)]; S = set(P); R = set()
    for A, B, C in combinations(P, 3):
        for a, b, c in ((A, B, C), (B, A, C), (A, C, B)):
            if (a[0]-b[0])*(c[0]-b[0]) + (a[1]-b[1])*(c[1]-b[1]) == 0:
                d = (a[0]+c[0]-b[0], a[1]+c[1]-b[1])
                if d in S: R.add(frozenset((a, b, c, d)))
    return P, list(R)
def edges(n, k):
    P, R = rectangles(n, k); idx = {p: i for i, p in enumerate(P)}
    D = set()
    for r1, r2 in combinations(R, 2):
        D.add(frozenset(idx[p] for p in r1 ^ r2))
    D = sorted(D, key=len); minimal = []
    bysize = {}
    for d in D:
        if any(m <= d for m in minimal if len(m) < len(d)): continue
        minimal.append(d)
    return len(P), minimal
