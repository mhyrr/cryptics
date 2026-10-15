"""A219562 check_a: a(n)=sum_{k=0..n} C(n+k,k)^4. Reproduce terms exactly; then for primes 7<=p<=P
compute a(p-1) mod p^5 with binomials updated mod p^5 using modular inverses of k (k<p)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from math import comb
from sympy import primerange
from oeisterms import terms
P = int(sys.argv[1]) if len(sys.argv) > 1 else 4999
t, off = terms('A219562')
assert [sum(comb(n + k, k)**4 for k in range(n + 1)) for n in range(len(t))] == t
print('terms ok', len(t))
bad = []; cnt = 0
for p in primerange(7, P + 1):
    M = p**5; c = 1; s = 1
    for k in range(1, p):
        c = c * (p - 1 + k) % M * pow(k, -1, M) % M
        s = (s + pow(c, 4, M)) % M
    cnt += 1
    if s != 1: bad.append((p, s))
print('primes tested', cnt, 'up to', P, 'violations', bad[:5])
