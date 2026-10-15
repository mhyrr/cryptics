# A129011 checker b: values via gmpy2.iroot(n^4, 3); for each N <= X search a representation N = u + v with
# u <= v both in the set, scanning u upward (numba), boolean membership array.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, gmpy2, numba
from k2common import check_terms
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 7
f = lambda n: int(gmpy2.iroot(gmpy2.mpz(n) ** 4, 3)[0])
check_terms("A129011", f)
vals = []; n = 0
while f(n) <= X: vals.append(f(n)); n += 1
vals = np.array(vals, dtype=np.int64)
mem = np.zeros(X + 1, dtype=np.bool_); mem[vals] = True
@numba.njit(cache=True)
def scan(X, vals, mem):
    out = []
    for N in range(1, X + 1):
        ok = False
        for u in vals:
            if 2 * u > N: break
            if mem[N - u]: ok = True; break
        if not ok: out.append(N)
    return out
missing = scan(X, vals, mem)
print("X =", X, "#elements", len(vals), "positive N <= X not representable:", list(missing)[:20])
