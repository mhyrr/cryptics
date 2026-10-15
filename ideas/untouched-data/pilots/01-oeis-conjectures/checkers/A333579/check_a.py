"""A333579 check_a: a(n) = [x^n] ((1+x+x^2)/(1-x+x^2))^n, exactly, as sum_j A_j B_{n-j} with A = (1+x+x^2)^n and
B = (1-x+x^2)^(-n), each from the power recurrence j c_j = sum_{k=1,2} ((alpha+1)k - j) P_k c_{j-k}.
Conjecture: a(p) == 2 mod p^3 for primes p >= 5."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from sympy import primerange
from oeisterms import terms
P = int(sys.argv[1]) if len(sys.argv) > 1 else 4999
def powser(P1, P2, alpha, L):
    c = [1]
    for j in range(1, L + 1):
        s = ((alpha + 1) * 1 - j) * P1 * c[j - 1]
        if j >= 2: s += ((alpha + 1) * 2 - j) * P2 * c[j - 2]
        assert s % j == 0; c.append(s // j)
    return c
def a(n):
    A = powser(1, 1, n, n); B = powser(-1, 1, -n, n)
    return sum(A[j] * B[n - j] for j in range(n + 1))
t, off = terms('A333579'); assert [a(n) for n in range(len(t))] == t; print('terms ok', len(t))
bad = []; cnt = 0
for p in primerange(5, P + 1):
    cnt += 1
    if (a(p) - 2) % p**3: bad.append(p)
print('primes', cnt, 'up to', P, 'violations', bad[:10])
