"""A332101 check_b: rigorous interval arithmetic (mpmath.iv, 20 digits / 45 terms, refined at 60 digits / 200 terms): enclose R_n(m) = sum_{j>=1} ((m-j)/m)^n using
power (not exp/log1p) for j < J and the tail bound sum_{j>=J} exp(-jn/m) <= exp(-Jn/m)/(1-exp(-n/m)); decide
R_n(c-1) < 1 <= R_n(c) for c = round(n/log 2)+2 (round decided in interval arithmetic too). Extra n as in check_a."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from mpmath import iv, mp
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
t, off = terms('A332101')
def a_pari(n):  # translation of the PARI: for(m=1,oo, s<m^n||return(m); s+=m^n)
    s = 0; m = 1
    while True:
        if not (s < m**n): return m
        s += m**n; m += 1
assert [a_pari(n) for n in range(len(t))] == t; print('terms ok', len(t))
def R_iv(n, m, J=90):
    s = iv.mpf(0); mm = iv.mpf(m)
    for j in range(1, min(J, m)):
        s += ((mm - j) / mm) ** n
    if J < m:
        q = iv.exp(-iv.mpf(n) / mm)
        s += iv.mpf([0, (q ** J / (1 - q)).b])
    return s
def decide(n, dps, J):
    iv.dps = dps
    x = iv.mpf(n) / iv.log(2)
    fl = int(mp.floor(x.a)); fr = x - fl
    if fr.b < 0.5: r = fl
    elif fr.a > 0.5: r = fl + 1
    else: return None
    c = r + 2
    r1 = R_iv(n, c - 1, J); r2 = R_iv(n, c, J)
    if r1.b < 1 and r2.a >= 1: return True
    if r1.a >= 1 or r2.b < 1: return False
    return None
bad = []; undec = []
for n in range(2, N + 1):
    d = decide(n, 20, 45)
    if d is None: d = decide(n, 60, 200)
    if d is None: undec.append(n)
    elif not d: bad.append(n)
print('N', N, 'mismatches', bad[:10], 'undecided', undec[:10])
n = 777451915729368
iv.dps = 100
x = iv.mpf(n) / iv.log(2); r = int(mp.floor(x.a))
fr = x - r
print('n=%d: frac(n/log2) in [%s, %s]' % (n, mp.nstr(mp.mpf(fr.a), 30), mp.nstr(mp.mpf(fr.b), 30)))
for m in (r + 1, r + 2):
    R = R_iv(n, m, J=400)
    print('  R(%d) - 1 in [%s, %s]' % (m, mp.nstr(mp.mpf((R - 1).a), 8), mp.nstr(mp.mpf((R - 1).b), 8)))
