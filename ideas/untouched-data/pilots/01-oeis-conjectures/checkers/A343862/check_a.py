# A340274 / A343862: a(n) = #{x+y+z=n, x,y,z>=1 : A*x^2y^2 + B*y^2z^2 + C*z^2x^2 is a square}.
# Conjecture 1: a(n)>0 for n>2 (Ehrenstein: all n<2^15). Since the form is homogeneous of degree 4,
# a(p)>0 for odd primes p and a(4)>0 imply a(n)>0 for all n>2 (scale a witness by n/p). So we test primes.
# Method a: numba search, x outer / y inner, float sqrt + exact check mod 2^64; every witness re-verified in Python.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import primerange
ANUM = os.environ.get("ANUM", "A343862")
A, B, C = {"A340274": (3, 5, 8), "A343862": (1, 5, 10)}[ANUM]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 327680
def count(n):
    return sum(1 for x in range(1, n - 1) for y in range(1, n - x) if (lambda v: math.isqrt(v) ** 2 == v)(A*x*x*y*y + B*y*y*(n-x-y)**2 + C*(n-x-y)**2*x*x))
T, off = terms(ANUM)
assert [count(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
@njit(cache=True)
def find(n, A, B, C):
    for x in range(1, n - 1):
        for y in range(1, n - x):
            z = n - x - y
            vf = A * float(x)**2 * float(y)**2 + B * float(y)**2 * float(z)**2 + C * float(z)**2 * float(x)**2
            s0 = np.uint64(math.sqrt(vf))
            X = np.uint64(x); Y = np.uint64(y); Z = np.uint64(z)
            v = np.uint64(A) * X*X*Y*Y + np.uint64(B) * Y*Y*Z*Z + np.uint64(C) * Z*Z*X*X  # mod 2^64
            for d in range(3):
                s = s0 + np.uint64(d) - np.uint64(1)
                if s * s == v:
                    return x, y
    return 0, 0
ps = [4] + list(primerange(3, N + 1)); bad = []
for p in ps:
    x, y = find(p, A, B, C)
    if x == 0: bad.append(p); print("NO WITNESS", p); continue
    z = p - x - y; v = A*x*x*y*y + B*y*y*z*z + C*z*z*x*x
    assert math.isqrt(v) ** 2 == v and x > 0 and y > 0 and z > 0, (p, x, y)
print("tested", len(ps), "values (4 and odd primes) up to", N)
print("RESULT", "holds for 3<=n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
