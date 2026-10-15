# A340274 / A343862, method b: z outer / x inner search (method a: x outer / y inner), float pre-test |round(sqrt(v))^2 - v|
# small, every candidate confirmed with exact math.isqrt in Python (false positives skipped, search resumed).
# Terms reproduced via a separate brute count with gmpy2.is_square.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from gmpy2 import is_square
from sympy import primerange
ANUM = os.environ.get("ANUM", "A340274")
A, B, C = {"A340274": (3, 5, 8), "A343862": (1, 5, 10)}[ANUM]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 327680
def count(n):
    c = 0
    for z in range(1, n - 1):
        for x in range(1, n - z):
            y = n - x - z
            c += is_square(A*x*x*y*y + B*y*y*z*z + C*z*z*x*x)
    return c
T, off = terms(ANUM)
assert [count(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
@njit(cache=True)
def nxt(n, z0, x0, A, B, C):
    x = x0
    for z in range(z0, n - 1):
        while x < n - z:
            y = n - x - z
            vf = A * float(x)**2 * float(y)**2 + B * float(y)**2 * float(z)**2 + C * float(z)**2 * float(x)**2
            s = math.floor(math.sqrt(vf) + 0.5)
            if abs(s * s - vf) <= 1e-13 * vf + 1.0:
                return z, x
            x += 1
        x = 1
    return 0, 0
ps = [4] + list(primerange(3, N + 1)); bad = []; calls = 0
for p in ps:
    z, x = 1, 1
    while True:
        z, x = nxt(p, z, x, A, B, C); calls += 1
        if z == 0: bad.append(p); print("NO WITNESS", p); break
        y = p - x - z; v = A*x*x*y*y + B*y*y*z*z + C*z*z*x*x
        if math.isqrt(v) ** 2 == v: break
        x += 1
print("tested", len(ps), "values (4 and odd primes) up to", N, "candidate calls", calls)
print("RESULT", "holds for 3<=n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
