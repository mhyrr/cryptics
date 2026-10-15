# A363482: a(n) = denominator of 1/(2-3/(3-4/(4-5/(...(n-1)-n/(-5))))). Conjecture: except 49, every term is 1 or prime (to n=10000).
# Method a: exact continued fraction. Generalized CF b0=0, a1=1, b_j=j+1, a_j=-(j+1) (j>=2), with the last partial
# quotient replaced by (a=-n, b=-5): value = (-5A_{n-2} - n A_{n-3}) / (-5B_{n-2} - n B_{n-3}); reduce by exact gcd.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import mpz, gcd, is_prime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
A = {-1: mpz(1), 0: mpz(0)}; B = {-1: mpz(0), 0: mpz(1)}
A[1] = 2 * A[0] + 1 * A[-1]; B[1] = 2 * B[0] + 1 * B[-1]
def a(n):
    num = -5 * A[n - 2] - n * A[n - 3]; den = -5 * B[n - 2] - n * B[n - 3]
    return abs(den) // gcd(num, den)
out = {}
for n in range(3, N + 1):
    j = n - 2
    if j >= 2 and j not in A:
        A[j] = (j + 1) * A[j - 1] - (j + 1) * A[j - 2]; B[j] = (j + 1) * B[j - 1] - (j + 1) * B[j - 2]
    out[n] = a(n)
    A.pop(n - 5, None); B.pop(n - 5, None)
T, off = terms("A363482")
assert [out[n] for n in range(3, 3 + len(T))] == T; print("terms OK", len(T))
bad = [n for n in range(3, N + 1) if out[n] != 1 and not is_prime(out[n]) and out[n] != 49]
print("n with a(n)=49:", [n for n in out if out[n] == 49])
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s a=%s" % (bad[0], out[bad[0]]))
