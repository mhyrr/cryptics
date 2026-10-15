# A394678: a(n) = (n! - 1) mod n^2. Conjecture: excluding a(4)=7, a(n) prime => n prime and n^2-n-1 prime (verified n<=5e4).
# Method a: running factorial mod n^2 is impossible (modulus changes), so compute n! mod n^2 by a product loop per n (numba-free, gmpy2).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import is_prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500000
import numpy as np
from numba import njit
@njit(cache=True)
def fm(n):
    M = n * n; r = 1
    for i in range(2, n + 1):
        r = (r * i) % M   # M < 2^38 for n<=5e5, r*i < 2^57
        if r == 0: break
    return (r - 1) % M
T, off = terms("A394678")
assert [fm(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
bad = []
for n in range(1, N + 1):
    v = fm(n)
    if is_prime(v) and n != 4 and not (is_prime(n) and is_prime(n*n - n - 1)): bad.append(n)
print("tested n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
