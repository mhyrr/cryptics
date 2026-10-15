# A390118, method b: per n, all square roots of 1 mod n (sympy.sqrt_mod, all_roots), scan t = r + j*n in increasing
# order and take the first prime (gmpy2.is_prime); a(n) = (t^2-1)/n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy.ntheory import sqrt_mod
from gmpy2 import is_prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 120000
def a(n):
    if n == 1: return 3
    roots = sorted(sqrt_mod(1, n, all_roots=True))
    j = 0
    while True:
        for r in roots:
            t = r + j * n
            if t > 1 and is_prime(t): return (t * t - 1) // n
        j += 1
T, off = terms("A390118")
assert [a(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
bad = []; eq = 0
for n in range(2, N + 1):
    v = a(n)
    if v > (n + 5) * (n - 1): bad.append(n)
    eq += v == (n + 5) * (n - 1)
print("#equality cases:", eq)
print("RESULT", "holds for 2<=n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[:10])
