# A005157 method b: Stembridge's triple product a(n) = prod_{1<=i<=j<=k<=n} (i+j+k-1)/(i+j+k-2).
# Multiplicity e(s) of i+j+k = s is a coefficient of q^3 [n+2 choose 3]_q (Gaussian binomial), computed by
# polynomial multiply/divide in python ints. Residue mod p^2 with valuation tracking. Terms via PARI translation.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari()
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10090
T, off = terms("A005157")
pari("A005157(n)=prod(i=1,n,prod(j=i,n,(i+j+n-1)/(i+2*j-2)))")
assert [int(pari("A005157(%d)" % n)) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def gauss3(n):
    # coefficients of [n+2 choose 3]_q = prod_{r=0..2} (1-q^(n+r)) / (1-q^(r+1))
    D = 3 * (n - 1)
    c = np.zeros(D + 3 * n + 10, dtype=np.int64); c[0] = 1
    for r in range(3):
        k = n + r                       # multiply by (1 - q^k)
        c[k:] = c[k:] - c[:-k].copy()
    for r in range(1, 4):               # divide by (1 - q^r): prefix sums with stride r
        for j in range(r): c[j::r] = np.cumsum(c[j::r])
    return c[: D + 1]
def amod(p):
    g = gauss3(p); m = p * p; v = 0; r = 1
    for d, e in enumerate(g):
        e = int(e)
        if e == 0: continue
        s = d + 3                       # i+j+k
        for val, sg in ((s - 1, 1), (s - 2, -1)):
            if val == 0: continue
            while val % p == 0: val //= p; v += sg * e
            r = r * pow(val, sg * e, m) % m
    return v, r
for n in range(1, 9):
    g = gauss3(n); x = 1
    from fractions import Fraction
    q = Fraction(1)
    for d, e in enumerate(g): q *= Fraction(d + 2, d + 1) ** int(e)
    assert q == int(pari("A005157(%d)" % n)), n
bad = None; cnt = 0
for p in pari("primes([5,%d])" % N):
    p = int(p); v, r = amod(p); cnt += 1
    target = pow(2, (p + 5) // 6 if p % 6 == 1 else (p + 1) // 6, p * p)
    if v != 0 or r != target: bad = (p, v, r, target); break
print("primes tested:", cnt)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE p=%d (v=%d r=%d target=%d)" % bad)
