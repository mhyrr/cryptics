# A394678, method b: closed form. Prime n: (n-1)! = -1 + kn (Wilson, k computed as ((n-1)! mod n^2 +1)/n) -> a(n) = n^2-n-1 checked;
# composite n: a(n) = n^2-1 iff n^2 | n! ; v_q(n!) via Legendre compared with 2 v_q(n) for every q|n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from sympy import factorint, isprime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500000
def leg(n, q):
    e = 0
    while n: n //= q; e += n
    return e
def a(n):
    if n == 1: return 0
    if isprime(n): return n*n - n - 1      # Wilson: n! == -n mod n^2
    if all(leg(n, q) >= 2*e for q, e in factorint(n).items()): return n*n - 1
    import math
    return (math.factorial(n) - 1) % (n*n)
T, off = terms("A394678")
assert [a(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
exc = [n for n in range(2, N + 1) if not isprime(n) and not all(leg(n, q) >= 2*e for q, e in factorint(n).items())]
print("composite n<=N with n^2 not dividing n!:", exc)
bad = []
for n in range(1, N + 1):
    v = a(n)
    if isprime(v) and n != 4 and not (isprime(n) and isprime(n*n-n-1)): bad.append(n)
print("tested n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
