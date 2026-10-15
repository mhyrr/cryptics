"""A325945 check_a: for every composite squarefree p < PMAX find the least q = k*D(p)+1 (D(x) = lambda(x)/gcd(lambda(x),x-1))
with gcd(p,q)=1, q squarefree, D(q) != 1 (q neither prime nor Carmichael) and p == 1 mod D(q) (Fagin's criterion for an
idempotent factorization pq with lambda(pq) | (p-1)(q-1)); numba with a smallest-prime-factor sieve up to QMAX.
Conjecture: such q exists for every composite squarefree p. Writes witnesses to witnesses.npy for check_b."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from oeisterms import terms
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 327680
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20000000

@nb.njit(cache=True)
def sieve(n):
    spf = np.zeros(n + 1, np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0: spf[j] = i
    return spf

@nb.njit(cache=True)
def gcd(a, b):
    while b: a, b = b, a % b
    return a

@nb.njit(cache=True)
def lam_sf(x, spf):
    # returns (lambda(x), squarefree flag, number of prime factors) for x <= len(spf)-1
    l = 1; sf = True; w = 0
    while x > 1:
        p = spf[x]; x //= p; w += 1
        if x % p == 0: sf = False
        l = l // gcd(l, p - 1) * (p - 1)
    return l, sf, w

@nb.njit(cache=True)
def lam_sf_big(x, spf, primes):
    # trial division by primes (for x > len(spf)-1), finishing with spf when small
    l = 1; sf = True; w = 0; n = len(spf) - 1
    for p in primes:
        if x <= n or p * p > x: break
        if x % p == 0:
            x //= p; w += 1
            if x % p == 0: sf = False
            l = l // gcd(l, p - 1) * (p - 1)
    if x > n:   # remaining x is prime
        w += 1; l = l // gcd(l, x - 1) * (x - 1)
    elif x > 1:
        l2, sf2, w2 = lam_sf(x, spf)
        # combine (x coprime to removed part unless repeated prime already flagged)
        if l2 > 0:
            l = l // gcd(l, l2) * l2
        w += w2; sf = sf and sf2
        if sf:
            # check repeated prime across the split
            pass
    return l, sf, w

@nb.njit(cache=True)
def D(x, spf):
    l, sf, w = lam_sf(x, spf)
    return l // gcd(l, x - 1)

@nb.njit(cache=True)
def run(PMAX, QMAX, spf, primes):
    out = np.zeros(PMAX, np.int64)  # out[p] = q, -1 if none <= QMAX, 0 if p not composite squarefree
    for p in range(4, PMAX):
        l, sf, w = lam_sf(p, spf)
        if not sf or w < 2: continue
        DP = l // gcd(l, p - 1)
        q = DP + 1; found = -1
        while q <= QMAX:
            if gcd(p, q) == 1:
                if q < len(spf): lq, sq, wq = lam_sf(q, spf)
                else: lq, sq, wq = lam_sf_big(q, spf, primes)
                if sq and wq >= 2:
                    DQ = lq // gcd(lq, q - 1)
                    if DQ != 1 and p % DQ == 1:
                        found = q; break
            q += DP
        out[p] = found
    return out

spf = sieve(QMAX)
QHARD = 4 * 10**12
primes = np.array([i for i in range(2, 2 * 10**6) if spf[i] == i], dtype=np.int64)
out = run(PMAX, QHARD, spf, primes)
ps = [p for p in range(4, PMAX) if out[p] != 0]
from sympy import factorint
from math import gcd as pgcd, lcm
def Dpy(x, f):
    l = 1
    for r in f: l = lcm(l, r - 1)
    return l // pgcd(l, x - 1)
for p in ps:
    if out[p] != -1: continue
    fp = factorint(p); DP = Dpy(p, fp); k = QMAX // DP
    while True:
        k += 1; q = k * DP + 1
        if pgcd(p, q) != 1: continue
        fq = factorint(q)
        if any(e > 1 for e in fq.values()) or len(fq) < 2: continue
        DQ = Dpy(q, fq)
        if DQ != 1 and p % DQ == 1: out[p] = q; break
    print('  fallback beyond QMAX: p', p, 'q', q, flush=True)
t, off = terms('A325945'); mism = [(p, int(out[p]), x) for p, x in zip(ps, t) if int(out[p]) != x]
print('terms: %d listed, mismatches (p, computed q, listed q):' % len(t), mism)
none = [p for p in ps if out[p] == -1]
np.save(__file__.rsplit('/', 1)[0] + '/witnesses.npy', np.array([[p, out[p]] for p in ps], dtype=np.int64))
print('PMAX', PMAX, 'composite squarefree p tested', len(ps), 'max least q', int(max(out[p] for p in ps)), 'p with no q <= QMAX:', none[:10])
