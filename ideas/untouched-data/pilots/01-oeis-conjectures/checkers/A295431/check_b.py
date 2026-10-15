"""A295431 check_b: exact a(n) via the hypergeometric term ratio a(n)/a(n-1) = 24(12n-1)(12n-5)(12n-7)(12n-11)/
(n(2n-1)(3n-1)(3n-2)) and direct divisibility for n <= NE; for NE < n <= N, p-adic valuations from Legendre's
digit-sum form v_p(m!) = (m - s_p(m))/(p-1), primes of the divisors found by trial division."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
NE = 2000
t, off = terms('A295431')
a = [1]
for n in range(1, max(NE, len(t)) + 1):
    num = a[-1] * 24 * (12*n-1) * (12*n-5) * (12*n-7) * (12*n-11); den = n * (2*n-1) * (3*n-1) * (3*n-2)
    assert num % den == 0; a.append(num // den)
assert a[:len(t)] == t; print('terms ok', len(t))
conds = {1: (385, lambda n: n + 1), 2: (5, lambda n: 2*n + 1), 3: (1, lambda n: 3*n + 1),
         4: (770, lambda n: (n + 1) * (2*n + 1) * (3*n + 1))}
bad = {k: [] for k in conds}
for n in range(NE + 1):
    for k, (c, D) in conds.items():
        if (c * a[n]) % D(n): bad[k].append(n)
def sp(m, p):
    s = 0
    while m: s += m % p; m //= p
    return s
def vf(m, p): return (m - sp(m, p)) // (p - 1)
def primes_of(x):
    out = {}; d = 2
    while d * d <= x:
        while x % d == 0: out[d] = out.get(d, 0) + 1; x //= d
        d += 1 if d == 2 else 2
    if x > 1: out[x] = out.get(x, 0) + 1
    return out
for n in range(NE + 1, N + 1):
    fs = {1: primes_of(n + 1), 2: primes_of(2*n + 1), 3: primes_of(3*n + 1)}
    f4 = {}
    for f in fs.values():
        for p, e in f.items(): f4[p] = f4.get(p, 0) + e
    fs[4] = f4
    for k, (c, D) in conds.items():
        for p, e in fs[k].items():
            v = vf(12*n, p) + vf(n, p) - vf(6*n, p) - vf(4*n, p) - vf(3*n, p)
            cc = c; vc = 0
            while cc % p == 0: cc //= p; vc += 1
            if v + vc < e: bad[k].append(n); break
print('N', N, 'failures (i)-(iv):', {k: v[:10] for k, v in bad.items()})
