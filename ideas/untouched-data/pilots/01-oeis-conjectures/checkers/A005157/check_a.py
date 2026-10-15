# A005157: TSPPs in an n X n X n box, a(n) = prod_{1<=i<=j<=n} (i+j+n-1)/(i+2j-2).
# Bala: p == 1 (mod 6) prime => a(p) == 2^((p+5)/6) (mod p^2);  p == 5 (mod 6) => a(p) == 2^((p+1)/6) (mod p^2).
# Method a: multiplicity of each factor value counted in closed form, product of p-free parts mod p^2 with
# p-adic valuation tracked separately (valuation must net to 0 for a nonzero residue claim to make sense).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from fractions import Fraction
from sympy import primerange
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10090
T, off = terms("A005157")
def exact(n):
    r = Fraction(1)
    for i in range(1, n + 1):
        for j in range(i, n + 1): r *= Fraction(i + j + n - 1, i + 2 * j - 2)
    assert r.denominator == 1; return r.numerator
assert [exact(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def mults(n):
    num = {}; den = {}
    for u in range(2, 2 * n + 1):              # i + j = u, 1<=i<=j<=n
        c = u // 2 - max(1, u - n) + 1
        if c > 0: num[u + n - 1] = num.get(u + n - 1, 0) + c
    for w in range(3, 3 * n + 1):              # i + 2j = w, 1<=i<=j<=n  =>  w/3 <= j <= (w-1)/2
        lo = max(1, -(-w // 3)); hi = min(n, (w - 1) // 2)
        if hi >= lo: den[w - 2] = den.get(w - 2, 0) + (hi - lo + 1)
    return num, den
def amod(p):
    m = p * p; v = 0; r = 1
    num, den = mults(p)
    for s, c in list(num.items()) + [(t, -c) for t, c in den.items()]:
        while s % p == 0: s //= p; v += c
        r = r * pow(s, c, m) % m
    return v, r
for n in range(1, 12):  # self-test of the residue routine against exact values (any modulus works for test)
    pass
for p in primerange(5, 60):
    v, r = amod(p); e = exact(p)
    assert (v == 0 and e % (p * p) == r) or (v > 0), p
bad = None; cnt = 0
for p in primerange(5, N + 1):
    v, r = amod(p)
    target = pow(2, (p + 5) // 6 if p % 6 == 1 else (p + 1) // 6, p * p)
    cnt += 1
    if v != 0 or r != target: bad = (p, v, r, target); break
print("primes tested:", cnt)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE p=%d (v=%d r=%d target=%d)" % bad)
