"""A291897 check_a: a(n) = numerator(E(2n-1, n)), Euler polynomial. Since (2n-1) is odd and E has 2-power denominators,
(2n-1)^2 | a(n) iff E(m,n) == 0 mod M, m=2n-1, M=m^2. Uses E(m,x)+E(m,x+1)=2x^m:
E(m,n) = (-1)^n E(m,0) + 2 sum_{j<n} (-1)^(n-1-j) j^m, with E(m,0) = -2(2^(m+1)-1) B_{m+1}/(m+1) from FLINT Bernoulli."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import flint
from fractions import Fraction
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
flint.fmpq.bernoulli(2 * N, cache=True)
def E0(m):
    b = flint.fmpq.bernoulli(m + 1)
    return Fraction(-2 * (2**(m + 1) - 1) * int(b.p), int(b.q) * (m + 1))
t, off = terms('A291897')
ex = []
for n in range(1, len(t) + 1):
    m = 2 * n - 1
    v = (-1)**n * E0(m) + 2 * sum((-1)**(n - 1 - j) * j**m for j in range(n))
    ex.append(v.numerator)
assert ex == t; print('terms ok', len(t))
bad = []
for n in range(1, N + 1):
    m = 2 * n - 1; M = m * m
    e0 = E0(m); assert e0.denominator & (e0.denominator - 1) == 0
    v = (-1)**n * e0.numerator * pow(e0.denominator, -1, M) if M > 1 else 0
    s = 0
    for j in range(1, n):
        s += (-1)**(n - 1 - j) * pow(j, m, M)
    if (v + 2 * s) % M if M > 1 else 0: bad.append(n)
print('N', N, 'violations', bad[:10])
