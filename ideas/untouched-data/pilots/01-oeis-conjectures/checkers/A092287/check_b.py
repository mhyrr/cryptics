# A092287 method b: v_p(gcd(j,k)) = min(v_p(j), v_p(k)); accumulate row by row:
# V(n,m) = V(n-1,m) + sum_{k<=m} min(v_p(n), v_p(k)), with prefix sums over k.  Formula side via a loop
# over p^i computed independently (Legendre-like).  Also recomputes a(n) by the PARI h(n,p) translation.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from sympy import primerange
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
T, off = terms("A092287")
def h(n, p): return 0 if n < p else h(n // p, p) + (n // p) ** 2
def a(n):
    r = 1
    for p in primerange(2, n + 1): r *= p ** h(n, p)
    return r
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = None
for p in primerange(2, N + 1):
    v = [0] * (N + 1)
    for k in range(p, N + 1, p):
        x, c = k, 0
        while x % p == 0: x //= p; c += 1
        v[k] = c
    row = [0] * (N + 1)
    for n in range(1, N + 1):
        vn = v[n]
        if vn:
            s = 0
            for m in range(1, N + 1):
                s += min(vn, v[m]); row[m] += s
        # compare for m <= n
        if n % p == 0 or n == N:
            pass
        for m in (range(1, n + 1) if (n % p == 0 or n == N or n < 50) else ()):
            q, fm = p, 0
            while q <= n: fm += (n // q) * (m // q); q *= p
            if fm != row[m]: bad = (p, n, m); break
        if bad: break
    if bad: break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE %s" % (bad,))
