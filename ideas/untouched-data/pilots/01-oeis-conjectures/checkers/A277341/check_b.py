"""A277341 check_b: same comparison with mpmath (30 digits): log a ~ q log p - p log q (exact big-int rounding when
the values are tiny or closer than ~1, the only cases where rounding can matter), log C(q,p) = lgamma(q+1)-lgamma(p+1)-lgamma(q-p+1);
ties within 1e-20 resolved exactly."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import mpmath as mp
from math import comb
from sympy import nextprime
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
mp.mp.dps = 30
ps = [2]
while len(ps) < N + 3: ps.append(nextprime(ps[-1]))
def a_exact(n):
    p, q = ps[n - 1], ps[n]; num, den = p**q, q**p
    return (2 * num + den) // (2 * den)
t, off = terms('A277341'); assert [a_exact(n) for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
def la(n): p, q = ps[n - 1], ps[n]; return q * mp.log(p) - p * mp.log(q)
def lc(n): p, q = ps[n - 1], ps[n]; return mp.loggamma(q + 1) - mp.loggamma(p + 1) - mp.loggamma(q - p + 1)
bad = []
LA = [None] + [la(n) for n in range(1, N + 2)]; LC = [None] + [lc(n) for n in range(1, N + 2)]
for n in range(1, N + 1):
    if min(LA[n], LA[n + 1]) < 3 or abs(LA[n + 1] - LA[n]) < 2 * mp.exp(-min(LA[n], LA[n + 1])) + mp.mpf(10)**-20:
        up_a = a_exact(n + 1) > a_exact(n)
    else: up_a = LA[n + 1] > LA[n]
    if abs(LC[n + 1] - LC[n]) < 1e-20:
        up_c = comb(ps[n + 1], ps[n]) > comb(ps[n], ps[n - 1])
    else: up_c = LC[n + 1] > LC[n]
    if up_a != up_c: bad.append(n)
print('N', N, 'violations', bad[:10])
