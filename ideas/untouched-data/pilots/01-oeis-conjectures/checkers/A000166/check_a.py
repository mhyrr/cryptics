# A000166 (derangements). Sun: for n > 2, a(n) is a perfect power only for n = 4 (a(4) = 9). Verified n <= 1000.
# Method a: a(n) = n a(n-1) + (-1)^n exactly; gmpy2.is_power (GMP mpz_perfect_power_p) for each n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A000166")
a = gmpy2.mpz(1); A = [1]
for n in range(1, N + 1):
    a = n * a + (-1) ** n; A.append(a)
assert [int(x) for x in A[:len(T)]] == T; print("terms OK", len(T))
hits = [n for n in range(3, N + 1) if gmpy2.is_power(A[n])]
print("perfect powers at n =", hits, [int(A[n]) for n in hits if n < 20])
bad = [n for n in hits if n != 4]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
