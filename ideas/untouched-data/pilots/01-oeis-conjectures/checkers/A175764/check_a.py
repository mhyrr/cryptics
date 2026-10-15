# A175764: iterate k -> (k^2+4)/d, d = next-to-largest divisor of k^2+4, until 2, 5 or 29; a(n) = #steps.
# Conjectures tested (both parts of the %C line): (i) a(n)=1 for n>29 with n mod 10 in {0,1,2,4,6,8,9};
# (ii) a(n)=9 for n mod 130 in {3,23,55,75,107,127}. Method a: literal definition with sympy.divisors.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from sympy import divisors
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
def f(k):
    u = k * k + 4; ds = divisors(u)
    return u // ds[-2]
def a(n, cap=60):
    s = 0
    while n not in (2, 5, 29):
        n = f(n); s += 1
        if s > cap: return None
    return s
check_terms("A175764", a)
b1 = [n for n in range(30, N + 1) if n % 10 in (0, 1, 2, 4, 6, 8, 9) and a(n) != 1]
b2 = [n for n in range(1, N + 1) if n % 130 in (3, 23, 55, 75, 107, 127) and a(n) != 9]
print("N =", N, "part (i) failures:", b1[:10], " part (ii) failures:", b2[:10])
