"""A290408 check_a: solve z = (i+z)^(-i) (principal branch) by complex Newton in mpmath at D digits, starting off
the line Im z = -1/2; report |Im z + 1/2| and that Re z reproduces the listed digits."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import mpmath as mp
from oeisterms import terms
D = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
mp.mp.dps = D + 30
I = mp.mpc(0, 1)
f = lambda z: z - mp.power(I + z, -I)
fp = lambda z: 1 - (-I) * mp.power(I + z, -I - 1)
z = mp.mpc('1.3', '-0.3')
mp.mp.dps = 30
for _ in range(60): z = z - f(z) / fp(z)
prec = 25
while prec < D + 30:
    prec = min(2 * prec, D + 30); mp.mp.dps = prec
    z = z - f(z) / fp(z)
z = z - f(z) / fp(z)
mp.mp.dps = D + 30
res = abs(f(z)); dev = abs(z.imag + mp.mpf(1) / 2)
t, off = terms('A290408')
s = mp.nstr(z.real, len(t) + 10, strip_zeros=False).replace('.', '')
assert [int(c) for c in s[:len(t)]] == t; print('terms ok', len(t))
print('D', D, 'residual |f(z)| ~ 10^%s' % (int(mp.log10(res)) if res else '-inf'), '| |Im z + 1/2| ~ 10^%s' % (int(mp.log10(dev)) if dev else '-inf'))
print('Re z =', mp.nstr(z.real, 40))
