# A051451: a(n) = lcm(1..x), x = n-th prime power. Winkler: for every n > 2 there is a twin pair [p, p+2], p < a(n),
# with a(n)+p, a(n)+p+2 also prime. Claimed verified 3 <= n <= 1000.
# Method a: gmpy2.is_prime (BPSW-type probable prime), smallest such p, n = 3.. until a deadline.
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
from sympy import primerange, factorint
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A051451")
pp = [1] + [m for m in range(2, 200000) if len(factorint(m)) == 1]
a = [None]; L = 1
for x in pp[:NMAX + 1]:
    L = L * x // gmpy2.gcd(L, x); a.append(L)
assert [int(v) for v in a[1:len(T) + 1]] == T; print("terms OK", len(T))
def witness(A):
    p = 3
    while p < A:
        if gmpy2.is_prime(p + 2) and gmpy2.is_prime(A + p) and gmpy2.is_prime(A + p + 2) and gmpy2.is_prime(p): return p
        p = int(gmpy2.next_prime(p))
    return None
last = 2; bad = None; ws = {}
for n in range(3, NMAX + 1):
    if time.time() - T0 > DEADLINE: break
    w = witness(a[n])
    if w is None: bad = n; break
    ws[n] = w; last = n
print("witness p for n=6:", ws.get(6), " last few:", [(n, ws[n]) for n in list(ws)[-3:]])
print("RESULT", "holds to %d" % last if bad is None else "COUNTEREXAMPLE n=%d" % bad)
