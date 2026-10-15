"""A261524 check_a. Conjecture 1: Zs(d,2,1) (Zsigmondy number: largest divisor of 2^d-1 coprime to 2^k-1, k<d) is a term
(odd n with gcd(1+x^n, 1+(1+x)^n) nontrivial over GF(2)) iff d is odd and d != 1, 15, 21.
For m = Zs(d) (> 1), ord_m(2) = d, so by Song's criterion m is a term iff the order-m subgroup H of GF(2^d)^* contains h
with h+1 in H. numba GF(2^d) arithmetic (d <= 62): walk h = y, y^2, ... (y a generator of H) and test (h+1)^m == 1.
A hit is a certificate of membership. Exhaustive walks (all of H) are done when m <= EXH, proving non-membership.
Even d: non-membership also follows since H lies in the norm-1 group of GF(2^(d/2)), and h, h+1 both of norm 1 forces
h^2+h+1 = 0, i.e. 3 | m (only d = 2)."""
import sys, time; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from math import gcd
from sympy import divisors, factorint
import cypari2
pari = cypari2.Pari()
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 62
BUDGET = int(sys.argv[2]) if len(sys.argv) > 2 else 3 * 10**6
EXH = int(sys.argv[3]) if len(sys.argv) > 3 else 3 * 10**7

def Zs(d):
    x = 2**d - 1
    for k in divisors(d)[:-1]:
        g = gcd(x, 2**k - 1)
        while g > 1: x //= g; g = gcd(x, 2**k - 1)
    return x

@nb.njit(cache=True)
def mul(a0, b0, poly, top):
    a = np.uint64(a0); b = np.uint64(b0); r = np.uint64(0); one = np.uint64(1)
    while b != np.uint64(0):
        if (b & one) != np.uint64(0): r = r ^ a
        b = b >> one; a = a << one
        if (a & top) != np.uint64(0): a = a ^ poly ^ top
    return r

@nb.njit(cache=True)
def pw(a0, e0, poly, top):
    r = np.uint64(1); a = np.uint64(a0); e = np.int64(e0)
    while e > 0:
        if e & 1: r = mul(r, a, poly, top)
        a = mul(a, a, poly, top); e = e >> 1
    return r

@nb.njit(cache=True)
def walk(y, m, steps, poly, top):
    h = np.uint64(y); one = np.uint64(1)
    for i in range(1, steps + 1):
        if h != one:
            if pw(h ^ one, m, poly, top) == one: return i
        h = mul(h, y, poly, top)
    return -1

res = {}; wit = {}
for d in range(1, DMAX + 1):
    m = Zs(d)
    if m == 1: res[d] = ('not-term (m=1)', 0); continue
    pol = pari('ffinit(2,%d)' % d); co = [int(c) for c in pari('Vecrev(lift(%s))' % pol)]
    poly = np.uint64(sum(c << i for i, c in enumerate(co)) & ((1 << d) - 1)); top = np.uint64(1 << d)  # x^d reduced away
    k = (2**d - 1) // m; fm = factorint(m)
    rng = np.random.default_rng(d)
    while True:   # generator of H: x^k with exact order m
        x = np.uint64(int(rng.integers(2, 2**min(d, 62))) & ((1 << d) - 1) or 2)
        y = pw(x, k, poly, top)
        if all(pw(y, int(m // int(r)), poly, top) != np.uint64(1) for r in fm): break
    steps = m if m <= EXH else BUDGET
    i = walk(y, m, steps, poly, top)
    if i > 0:
        res[d] = ('TERM (witness h=y^%d)' % i, m); h = pw(y, i, poly, top); wit[d] = [co, int(h), str(m)]
    elif m <= EXH: res[d] = ('not-term (exhaustive)', m)
    else: res[d] = ('undecided', m)
pred = lambda d: d % 2 == 1 and d not in (1, 15, 21)
bad = [d for d in res if (res[d][0].startswith('TERM') and not pred(d)) or (res[d][0].startswith('not') and pred(d))]
und = [d for d in res if res[d][0] == 'undecided']
import json; json.dump({'DMAX': DMAX, 'EXH': EXH, 'res': {d: [r[0], str(r[1])] for d, r in res.items()}, 'wit': wit}, open(__file__.rsplit('/', 1)[0] + '/witnesses.json', 'w'))
for d in res: print(d, res[d][0], 'm=%d' % res[d][1])
print('DMAX', DMAX, 'contradictions', bad, 'undecided', und)
