# A112388 checker b: maintain 2^n as numpy array of base-10^4 limbs, doubling with carry propagation;
# pandigital test from the limbs' decimal digits (leading limb without zero padding). Data terms via sympy.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np
from sympy import nextprime
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
def a(n):
    if n == 1: return 10123457689
    p = 2
    while len(set(str(p ** n))) < 10: p = nextprime(p)
    return p
check_terms("A112388", a)
B = 10000
L = np.zeros(N // 13 + 10, dtype=np.int64); L[0] = 1; top = 1   # little-endian limbs
digs = np.array([[int(c) for c in f"{v:04d}"] for v in range(B)], dtype=np.int8)
def pandigital(L, top):
    present = np.zeros(10, dtype=bool)
    if top > 60:   # fast path: low 50 limbs (all full 4-digit limbs) usually already contain every digit
        present[np.unique(digs[L[:50]].ravel())] = True
        if present.all(): return True
    body = L[:top - 1]
    present[np.unique(digs[body].ravel())] = True
    for c in str(int(L[top - 1])): present[int(c)] = True
    return present.all()
bad = []
for n in range(1, N + 1):
    L[:top + 1] *= 2
    # carry: values < 2*B so single pass suffices (carry is 0/1, and limb+carry < 2B-1 < ... handled iteratively)
    c = L[:top + 1] >= B
    while c.any():
        L[:top + 1][c] -= B
        L[1:top + 2][c[:top + 1]] += 1
        c = L[:top + 1] >= B
    if L[top] != 0: top += 1
    if n > 168 and not pandigital(L, top): bad.append(n)
    if n == 168: print("2^168 pandigital?", pandigital(L, top))
print("N =", N, "n>168 with 2^n not pandigital:", bad[:20])
