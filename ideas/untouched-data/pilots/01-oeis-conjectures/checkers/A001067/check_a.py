# A001067: numerator of B(2n)/(2n). Manyama: if a prime p > 2n+1 divides a(n), then p^2 does not (claimed for
# p < 12 million). For p > 2n+1, p is absent from the denominator, so the test is B(2n) mod p^2 != 0 whenever
# B(2n) == 0 mod p (irregular pairs).
# Method a: for each prime p < PMAX, B_0..B_{p-2} mod p^2 from the power series x/(e^x - 1) inverted mod p^2
# (flint nmod_poly), k! times coefficient.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import flint
from sympy import primerange
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A001067")
assert [flint.fmpq.bernoulli(2 * n) / (2 * n) for n in range(1, len(T) + 1)] and \
       [int((flint.fmpq.bernoulli(2 * n) / (2 * n)).p) for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
pairs = 0; bad = None
for p in primerange(5, PMAX):
    m = p * p
    inv = [0] * (p - 1); f = 1
    for k in range(p - 1):               # 1/(k+1)! mod p^2
        f = f * (k + 1) % m; inv[k] = pow(f, -1, m)
    g = flint.nmod_poly(inv, m).inverse_series_trunc(p - 1)
    fact = 1
    for k in range(1, p - 2):
        fact = fact * k % m
        if k % 2 == 0 and k <= p - 3:
            b = int(g[k]) * fact % m
            if b % p == 0:
                pairs += 1
                if b == 0: bad = (p, k); break
    if bad: break
print("irregular pairs (p, 2n) with 2n <= p-3 found:", pairs)
print("RESULT", "holds for p < %d" % PMAX if bad is None else "COUNTEREXAMPLE p=%d 2n=%d" % bad)
