# Hand re-check of the A074726 counterexamples: F(n) abundant but not Zumkeller.
# Prints the full factorization (each factor proven prime by PARI isprime), sigma(F)/F, and the dominance
# certificate: F = 144*Q, gcd = 1, sigma(144) = 403 odd, 403*(sigma(Q)-Q) < Q  =>  no equal-sum divisor split.
# Sanity check of the lemma: exhaustive divisor-split search agrees on 144*557 and 144*557*2417.
import sys
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
from sympy import divisors
from fractions import Fraction
def split_exists(u):
    ds = sorted(divisors(u), reverse=True); tot = sum(ds)
    if tot % 2: return False
    suf = [0] * (len(ds) + 1)
    for i in range(len(ds) - 1, -1, -1): suf[i] = suf[i + 1] + ds[i]
    stack = [(0, tot // 2)]
    while stack:
        i, r = stack.pop()
        if r == 0: return True
        if i == len(ds) or suf[i] < r: continue
        stack.append((i + 1, r))
        if ds[i] <= r: stack.append((i + 1, r - ds[i]))
    return False
print("lemma sanity: 144*557 split?", split_exists(144 * 557), " 144*557*2417 split?", split_exists(144 * 557 * 2417))
for n in [int(x) for x in sys.argv[1:]] or [372, 732, 876, 996]:
    F = int(pari.fibonacci(n)); M = pari.factor(F)
    fac = [(int(p), int(e)) for p, e in zip(M[0], M[1])]
    assert all(pari.isprime(p) for p, e in fac)
    sF = 1
    for p, e in fac: sF *= (p ** (e + 1) - 1) // (p - 1)
    u = 1
    for p, e in fac:
        if p in (2, 3): u *= p ** e
    Q = F // u; sQ = sF // ((2**5 - 1) * (3**3 - 1) // 2) if u == 144 else None
    su = 1
    for p, e in fac:
        if p in (2, 3): su *= (p ** (e + 1) - 1) // (p - 1)
    sQ = sF // su
    print("n=%d F(n)=%d" % (n, F))
    print("  factorization:", fac)
    print("  sigma(F)/F = %.6f (> 2: %s), sigma(F) even: %s" % (float(Fraction(sF, F)), 2 * F < sF, sF % 2 == 0))
    print("  u = %d, sigma(u) = %d (odd: %s), sigma(u)*(sigma(Q)-Q)/Q = %.6f (< 1: %s)" % (u, su, su % 2 == 1, float(Fraction(su * (sQ - Q), Q)), su * (sQ - Q) < Q))
