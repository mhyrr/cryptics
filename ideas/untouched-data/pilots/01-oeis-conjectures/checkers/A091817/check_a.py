# A091817: (2*numerator(H(p-3)) - 3*denominator(H(p-3)))/p, p prime >= 3. Quet: always an integer (p < 3e4).
# Reduction used for the range (stated so it can be audited): den(H(p-3)) is coprime to p (all i <= p-3 < p), so
# p | 2*num - 3*den  <=>  2*H(p-3) == 3 (mod p), with H(p-3) computed as sum of modular inverses.
# Method a: exact Fractions for p < EXACT (literal definition), and inverses by batch inversion (one Fermat pow per p) for all p < N.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from fractions import Fraction
from sympy import primerange
import numba, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
EXACT = 3000
T, off = terms("A091817")
H = Fraction(0); m = 0; out = []; bad = None
for p in primerange(3, EXACT):
    while m < p - 3: m += 1; H += Fraction(1, m)
    v = 2 * H.numerator - 3 * H.denominator
    if v % p: bad = p
    out.append(v // p)
assert out[:len(T)] == T; print("terms OK", len(T), "exact check to", EXACT, "bad" if bad else "ok")
@numba.njit
def powmod(b, e, m):
    r = 1; b %= m
    while e:
        if e & 1: r = r * b % m
        b = b * b % m; e >>= 1
    return r
@numba.njit
def test(p):
    # batch inversion of 1..p-3 (prefix products, one Fermat inverse, back-substitution)
    m = p - 3
    pre = np.empty(m + 1, np.int64); pre[0] = 1
    for i in range(1, m + 1): pre[i] = pre[i - 1] * i % p
    inv_all = powmod(pre[m], p - 2, p); s = 0
    for i in range(m, 0, -1):
        s += inv_all * pre[i - 1] % p          # = 1/i
        inv_all = inv_all * i % p
    return (2 * (s % p) - 3) % p == 0
for p in primerange(5, N):
    if not test(p): bad = p; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE p=%d" % bad)
