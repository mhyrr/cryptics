# A339669, method b: translation of Corneth's PARI program: L(n)^2+1 = 5F(n)^2+4(-1)^n+1,
# walk Fibonacci numbers m (k,m) -> (m,m+k) counting divisors, plus 1 for the divisor 1.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from gmpy2 import fib, mpz
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1560
def a(n):
    l2 = 5 * fib(n) ** 2 + 4 * (-1) ** n + 1
    k, m, res = mpz(1), mpz(2), 1
    while m <= l2:
        if l2 % m == 0: res += 1
        k, m = m, m + k
    return res
T, off = terms("A339669")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = [n for n in range(N) if (n % 6 == 3 and a(n) != 1) or (n % 6 in (1, 5) and a(n) != 2)]
print("tested indices 0..", N - 1)
print("RESULT", "holds for index<%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[:10])
