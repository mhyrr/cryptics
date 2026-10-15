"""A219562 check_b: exact big-integer binomials C(p-1+k,k) built incrementally (no modular inverses),
then sum of 4th powers reduced mod p^5. Terms reproduced via the PARI formula translated."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import gmpy2
from oeisterms import terms
P = int(sys.argv[1]) if len(sys.argv) > 1 else 4999
t, off = terms('A219562')
assert [sum(int(gmpy2.comb(n + k, k))**4 for k in range(n + 1)) for n in range(len(t))] == t
print('terms ok', len(t))
bad = []; cnt = 0
p = gmpy2.mpz(7)
while p <= P:
    M = p**5; c = gmpy2.mpz(1); s = gmpy2.mpz(1)
    for k in range(1, int(p)):
        c = c * (p - 1 + k) // k
        s += gmpy2.powmod(c % M, 4, M)
    cnt += 1
    if s % M != 1: bad.append(int(p))
    p = gmpy2.next_prime(p)
print('primes tested', cnt, 'up to', P, 'violations', bad[:5])
