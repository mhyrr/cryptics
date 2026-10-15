# A357512: a(n) = Sum_{k=0..n} k^5 C(n,k)^2 C(n+k,k)^2. Conjecture: a(n-1) == 0 mod n^4 for all n == 1,5 mod 6 (to 499).
# Method a: exact integer sum from the definition for each n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def a(n):
    s = mpz(0); b1 = mpz(1); b2 = mpz(1)
    for k in range(1, n + 1):
        b1 = b1 * (n - k + 1) // k; b2 = b2 * (n + k) // k
        s += k**5 * (b1 * b2) ** 2
    return s
T, off = terms("A357512")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = []; cnt = 0
for n in range(1, N + 1):
    if n % 6 in (1, 5):
        cnt += 1
        if a(n - 1) % n**4: bad.append(n); print("FAIL", n)
print("tested", cnt, "values n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
