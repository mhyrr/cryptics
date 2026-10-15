"""A290408 check_b: with x = z + i, z = x^(-i) and Im z = -1/2 means conj(x) = exp(-i Log x); writing Log x = L + i*theta
this holds iff L = theta. Solve the real equation (1/2)ln(a^2+1/4) = atan2(1/2, a) for a by mpmath findroot at D digits,
then check the complex fixed-point residual of z = a - i/2 directly, and compare a with the listed digits."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import mpmath as mp
from oeisterms import terms
D = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
mp.mp.dps = D + 30
g = lambda a: mp.log(a * a + mp.mpf(1) / 4) / 2 - mp.atan2(mp.mpf(1) / 2, a)
a = mp.findroot(g, mp.mpf('1.339'), tol=mp.mpf(10) ** (-(D + 20)))
z = mp.mpc(a, -mp.mpf(1) / 2); I = mp.mpc(0, 1)
res = abs(z - mp.power(I + z, -I))
t, off = terms('A290408')
s = mp.nstr(a, len(t) + 10, strip_zeros=False).replace('.', '')
assert [int(c) for c in s[:len(t)]] == t; print('terms ok', len(t))
print('D', D, 'fixed-point residual of a - i/2 ~ 10^%s' % (int(mp.log10(res)) if res else '-inf'))
print('a =', mp.nstr(a, 40))
