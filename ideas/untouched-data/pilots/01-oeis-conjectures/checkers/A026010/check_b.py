# A026010 method b: a(n) from the PARI binomial sum (Greubel). Compositions via generating function:
# odd-position part weight A = O(x) + y E(x), even-position part weight B = O(x) + E(x)/y, with
# O = x/(1-x^2), E = x^2/(1-x^2). G = (1 + A) / (1 - A B); answer = [x^(n+2) y^0] G. Laurent polys in y as dicts.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from math import comb
N = int(sys.argv[1]) if len(sys.argv) > 1 else 190
T, off = terms("A026010")
A_ = [sum(comb((n + k) // 2, k // 2) for k in range(n + 1)) for n in range(N + 1)]
assert A_[:len(T)] == T; print("terms OK", len(T))
M = N + 2
# series in x: list of dict{ydeg: coeff}
def ser(f): return [f(i) for i in range(M + 1)]
O = ser(lambda i: {0: 1} if i % 2 == 1 else {})
E = ser(lambda i: {0: 1} if i % 2 == 0 and i >= 2 else {})
def shift(s, e): return [{k + e: v for k, v in c.items()} for c in s]
def add(s, t):
    r = []
    for a, b in zip(s, t):
        c = dict(a)
        for k, v in b.items(): c[k] = c.get(k, 0) + v
        r.append(c)
    return r
def mul(s, t):
    r = [dict() for _ in range(M + 1)]
    for i, a in enumerate(s):
        if not a: continue
        for j in range(M + 1 - i):
            b = t[j]
            if not b: continue
            c = r[i + j]
            for k1, v1 in a.items():
                for k2, v2 in b.items(): c[k1 + k2] = c.get(k1 + k2, 0) + v1 * v2
    return r
A = add(O, shift(E, 1)); B = add(O, shift(E, -1)); AB = mul(A, B)
# 1/(1-AB) = sum (AB)^k ; AB has zero constant term
one = [{0: 1}] + [dict() for _ in range(M)]
inv = one; p = one
for _ in range(M):
    p = mul(p, AB); inv = add(inv, p)
G = mul(add(one, A), inv)
C = [g.get(0, 0) for g in G]
bad = next((n for n in range(0, N + 1) if C[n + 2] != A_[n]), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
