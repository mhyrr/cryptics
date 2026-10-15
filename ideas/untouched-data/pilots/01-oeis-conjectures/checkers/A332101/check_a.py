"""A332101 check_a: a(n) = least m with m^n <= sum_{k<m} k^n, i.e. R_n(m) = sum_{j=1}^{m-1} (1-j/m)^n >= 1 (R_n increasing
in m). For each n <= N with c = round(n/log 2) + 2, test R_n(c-1) < 1 <= R_n(c) in double precision (numpy, terms
until < 1e-25); if |R-1| < 1e-9 recompute with mpmath at 60 digits. Terms reproduced exactly with integers.
Extra: the n = 777451915729368 flagged in the entry, at 120 digits."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, mpmath as mp
from math import log
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
t, off = terms('A332101')
def a_exact(n):
    s = 0; m = 1
    while True:
        if m**n <= s: return m
        s += m**n; m += 1
assert [a_exact(n) for n in range(len(t))] == t; print('terms ok', len(t))
J = np.arange(1, 200, dtype=float)
def R_float(n, m):
    jj = J[J < m]
    return float(np.sum(np.exp(n * np.log1p(-jj / m))))
def R_mp(n, m, dps=60):
    with mp.workdps(dps):
        s = mp.mpf(0); j = 1
        while j < m:
            tt = mp.exp(n * mp.log1p(-mp.mpf(j) / m)); s += tt
            if tt < mp.mpf(10) ** (-dps + 5): break
            j += 1
        return s
bad = []; refined = 0
for n in range(2, N + 1):
    c = round(n / log(2)) + 2
    if abs(n / log(2) - round(n / log(2))) > 0.4999: c = int(mp.nint(mp.mpf(n) / mp.log(2))) + 2
    r1 = R_float(n, c - 1); r2 = R_float(n, c)
    if abs(r1 - 1) < 1e-9 or abs(r2 - 1) < 1e-9:
        refined += 1; r1 = R_mp(n, c - 1); r2 = R_mp(n, c)
    if not (r1 < 1 <= r2): bad.append(n)
print('N', N, 'mismatches', bad[:10], 'refined with mpmath:', refined)
n = 777451915729368
with mp.workdps(120):
    x = mp.mpf(n) / mp.log(2); r = int(mp.nint(x))
    print('n=%d: n/log2 = %s' % (n, mp.nstr(x, 40)))
    for m in (r + 1, r + 2):
        print('  R(%d) - 1 = %s' % (m, mp.nstr(R_mp(n, m, 120) - 1, 10)))
