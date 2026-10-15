"""A333579 check_b: G = (1+x+x^2)/(1-x+x^2) mod x^(p+1) (denominator expanded by g_n = f_n + g_{n-1} - g_{n-2}),
then G^p by binary powering with truncated products in FLINT nmod_poly modulo p^3; compare [x^p] with 2.
Terms: the entry's triple-sum formula sum_{i,j,k} (-1)^(n-k-i-j) C(n,k)C(k,i)C(n+j-1,j)C(j,n-k-i-j)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import flint
from math import comb
from sympy import primerange
from oeisterms import terms
P = int(sys.argv[1]) if len(sys.argv) > 1 else 4999
def tri(n):
    s = 0
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                r = n - k - i - j
                if 0 <= r <= j: s += (-1)**(n - k - i - j) * comb(n, k) * comb(k, i) * comb(n + j - 1, j) * comb(j, r)
    return s
t, off = terms('A333579'); assert [1] + [tri(n) for n in range(1, len(t))] == t; print('terms ok', len(t))
bad = []; cnt = 0
for p in primerange(5, P + 1):
    cnt += 1; M = p**3; L = p + 1
    f = [1, 1, 1] + [0] * (L - 3); g = []
    for n in range(L):
        v = f[n] + (g[n - 1] if n >= 1 else 0) - (g[n - 2] if n >= 2 else 0); g.append(v)
    G = flint.nmod_poly([v % M for v in g], M)
    R = flint.nmod_poly([1], M); e = p
    while e:
        if e & 1: R = R.mul_low(G, L)
        G = G.mul_low(G, L); e >>= 1
    if int(R[p]) != 2 % M: bad.append(p)
print('primes', cnt, 'up to', P, 'violations', bad[:10])
