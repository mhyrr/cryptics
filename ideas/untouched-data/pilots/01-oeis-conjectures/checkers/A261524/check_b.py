"""A261524 check_b: (1) Song's PARI isA261524 (loop over H in GF(2^d) via ffgen/ffprimroot) run directly for every d
whose m = Zs(d) <= LIM; (2) every membership witness h of check_a (witnesses.json) re-verified in PARI: h != 1,
h^m == 1 and (h+1)^m == 1 in GF(2)[x]/(f) with f irreducible of degree d; (3) gcd(1+x^m, 1+(1+x)^m) over GF(2) computed
directly (the definition) for m <= 3000. Zs(d) from A064078's definition via gcds."""
import sys, json; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import cypari2
from math import gcd
from sympy import divisors
pari = cypari2.Pari(); pari.allocatemem(10**9)
LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
W = json.load(open(__file__.rsplit('/', 1)[0] + '/witnesses.json'))
DMAX = W['DMAX']
pari('isA261524(n,p=2) = my(d=znorder(Mod(p,n)), c=ffgen(p^d,\'c), g=ffprimroot(c)); forstep(e=0, p^d-2, (p^d-1)/n, if((g^e+1)^n==1, return(1))); return(0)')
pari('W(n)=my(e=Mod(1,2)); poldegree(gcd(e*(1+x^n), e*(1+(1+x)^n))) > 1')
def Zs(d):
    x = 2**d - 1
    for k in range(1, d):
        if d % k == 0:
            g = gcd(x, 2**k - 1)
            while g > 1: x //= g; g = gcd(x, 2**k - 1)
    return x
out = {}
for d in range(1, DMAX + 1):
    m = Zs(d); r = None
    if m == 1: r = False
    elif m <= LIM: r = bool(int(pari('isA261524(%d)' % m)))
    if m > 1 and m <= 3000: assert r == bool(int(pari('W(%d)' % m))), d
    w = W['wit'].get(str(d))
    if w is not None:
        co, h, ms = w; assert int(ms) == m
        f = 'Mod(1,2)*(' + '+'.join('x^%d' % i for i, c in enumerate(co) if c) + ')'
        assert int(pari('polisirreducible(%s)' % f)) == 1 and int(pari('poldegree(%s)' % f)) == d
        hp = 'Mod(Mod(1,2)*(' + ('+'.join('x^%d' % i for i in range(d) if h >> i & 1) or '0') + '), %s)' % f
        ok = int(pari('my(h=%s); h!=Mod(Mod(1,2),%s) && h^%d==1 && (h+1)^%d==1' % (hp, f, m, m)))
        assert ok == 1, ('witness fails', d)
        if r is False: print('CONFLICT d', d)
        r = True
    out[d] = r
pred = lambda d: d % 2 == 1 and d not in (1, 15, 21)
bad = [d for d, r in out.items() if r is not None and r != pred(d)]
und = [d for d, r in out.items() if r is None]
print('DMAX', DMAX, 'decided', len(out) - len(und), 'contradictions with conjecture', bad, 'undecided', und)
