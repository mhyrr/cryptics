# A378252: least prime power > 2^n. Conjecture: all terms except 9 (n=3) are prime (confirmed to n=1000).
# Method a: q = gmpy2.next_prime(2^n) (BPSW probable prime); for each exponent k>=2, the least k-th power above 2^n
# is b^k with b = iroot(2^n,k)+1; the least prime k-th power is (least prime >= b)^k. Conjecture fails at n iff one is < q.
# Usage: check_a.py N [N0]  (tests N0 <= n <= N; terms always reproduced).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz, next_prime, iroot, is_prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1001
def least_pp(n):
    x = mpz(2) ** n; q = next_prime(x); best = q
    for k in range(2, n + 1):
        b = iroot(x, k)[0] + 1
        if b ** k >= best: continue
        p = b if is_prime(b) else next_prime(b)
        if p ** k < best: best = p ** k
    return best, q
T, off = terms("A378252")
assert [int(least_pp(n)[0]) for n in range(0, len(T))] == T; print("terms OK", len(T))
bad = []
for n in range(N0, N + 1):
    v, q = least_pp(n)
    if v != q: bad.append(n); print("NONPRIME", n, v)
print("tested %d<=n<=%d" % (N0, N))
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
