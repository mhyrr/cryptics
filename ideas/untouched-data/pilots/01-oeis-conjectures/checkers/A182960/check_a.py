# A182960: A(x) = exp(Sum_{n>=1} C(6n-1,2n-1) x^n/n). Conjecture (Bala): b(n) = [x^n] A(x)^n satisfies
# b(p) == b(1) (mod p^3) for primes p >= 5 (checked to p=101).
# Method a: a(n) from n*a(n) = Sum_{k=1..n} C(6k-1,2k-1) a(n-k) (A'/A = Sum C(6k-1,2k-1) x^(k-1)), exact;
# b(p) via flint nmod_poly pow_trunc modulo p^3.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from math import comb
from flint import nmod_poly
from sympy import primerange
from k2common import check_terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1010
M = PMAX + 1
c = [0] + [comb(6 * k - 1, 2 * k - 1) for k in range(1, M + 1)]
a = [1]
for n in range(1, M + 1):
    s = sum(c[k] * a[n - k] for k in range(1, n + 1)); assert s % n == 0; a.append(s // n)
check_terms("A182960", lambda n: a[n])
bseq = [1, 5, 215, 10463, 537287, 28435880, 1534398353, 83920389642]
for n in range(1, 8):
    mod = 10 ** 30
    assert int(nmod_poly([x % (2**61-1) for x in a[:n + 1]], 2**61-1).pow_trunc(n, n + 1)[n]) == bseq[n] % (2**61-1)
print("b(1..7) from the %F line reproduced")
b1 = 5; bad = []; cnt = 0
for p in primerange(5, PMAX + 1):
    m = p ** 3
    P = nmod_poly([x % m for x in a[:p + 1]], m)
    r = int(P.pow_trunc(p, p + 1)[p]); cnt += 1
    if r != b1 % m: bad.append((p, r))
print("primes 5 <= p <=", PMAX, "tested:", cnt, "violations:", bad)
