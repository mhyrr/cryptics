# A175764 checker b: f(k) = smallest prime factor of k^2+4 (u / (u / spf(u)), as in the entry's alternative PARI f),
# spf by trial division over a prime list; a(n) by iteration.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from sympy import isprime, primerange
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
PR = list(primerange(2, 200000))
def spf(u):
    if isprime(u): return u
    for p in PR:
        if u % p == 0: return p
    raise RuntimeError("spf beyond trial bound")
def a(n, cap=60):
    s = 0
    while n not in (2, 5, 29):
        u = n * n + 4; n = u // (u // spf(u)); s += 1
        if s > cap: return None
    return s
check_terms("A175764", a)
b1 = [n for n in range(30, N + 1) if n % 10 in (0, 1, 2, 4, 6, 8, 9) and a(n) != 1]
b2 = [n for n in range(1, N + 1) if n % 130 in (3, 23, 55, 75, 107, 127) and a(n) != 9]
print("N =", N, "part (i) failures:", b1[:10], " part (ii) failures:", b2[:10])
