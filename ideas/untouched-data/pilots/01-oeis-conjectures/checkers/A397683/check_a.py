# A397683: f(m) = #{1<=x<m : gcd(x,m)=gcd(x+1,m)=1, ord_m(x)=ord_m(x+1)}; a(n)=f(2n-1).
# Conjecture: for odd m, f(m)=0 iff m is a power of 3 or of 7 (m>1) (verified m<20000).
# Method a: numba; order via Carmichael lambda from an spf sieve; existence search for each odd m, full count for 3^k,7^k.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
@njit(cache=True)
def spf_sieve(N):
    s = np.zeros(N + 1, np.int64)
    for i in range(2, N + 1):
        if s[i] == 0:
            for j in range(i, N + 1, i):
                if s[j] == 0: s[j] = i
    return s
@njit(cache=True)
def gcd(a, b):
    while b: a, b = b, a % b
    return a
@njit(cache=True)
def pw(b, e, m):
    r = 1; b %= m
    while e:
        if e & 1: r = r * b % m
        b = b * b % m; e >>= 1
    return r
@njit(cache=True)
def lam_and_primes(m, spf):
    lam = 1; mm = m
    while mm > 1:
        p = spf[mm]; e = 0
        while mm % p == 0: mm //= p; e += 1
        l = (p - 1) * p ** (e - 1)
        if p == 2 and e >= 3: l //= 2
        lam = lam * l // gcd(lam, l)
    qs = np.zeros(20, np.int64); nq = 0; t = lam
    while t > 1:
        q = spf[t]; qs[nq] = q; nq += 1
        while t % q == 0: t //= q
    return lam, qs[:nq]
@njit(cache=True)
def order(x, m, lam, qs):
    o = lam
    for q in qs:
        while o % q == 0 and pw(x, o // q, m) == 1: o //= q
    return o
@njit(cache=True)
def f(m, spf, first):
    if m == 1: return 1
    lam, qs = lam_and_primes(m, spf); c = 0
    for x in range(1, m):
        if gcd(x, m) == 1 and gcd(x + 1, m) == 1 and order(x, m, lam, qs) == order(x + 1, m, lam, qs):
            c += 1
            if first: return 1
    return c
spf = spf_sieve(N + 1)
T, off = terms("A397683")
assert [f(2 * n - 1, spf, False) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
def is37(m):
    for b in (3, 7):
        t = m
        while t % b == 0: t //= b
        if t == 1: return True
    return False
bad = []
for m in range(3, N + 1, 2):
    z = f(m, spf, not is37(m)) == 0
    if z != is37(m): bad.append(m); print("MISMATCH", m)
print("tested odd 3<=m<=", N)
print("RESULT", "holds for m<=%d" % N if not bad else "COUNTEREXAMPLE m=%s" % bad[:10])
