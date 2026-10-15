"""A321766 check_a. Conjecture (R. Israel): for each n >= 154 there is m <= n with 3^m+3^k-1 composite for all k=1..n.
Let f(m) = least k >= 1 with 3^m+3^k-1 prime. Build a chain m_1=154, m_{i+1} <= f(m_i) with f(m_{i+1}) > f(m_i):
then every n in [154, f(m_last)-1] is covered. Compositeness is proven (sieve factor < 3000 or failed gmpy2 BPSW),
so the chain is rigorous; f(m) itself uses BPSW-probable primes (an error could only shorten the chain).
Candidates m are tried in increasing order of sieve-survivor count among k <= current bound.
Terms a(n) (permanents) reproduced by memoized row DP over column masks."""
import sys, time; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, gmpy2
from functools import lru_cache
from sympy import isprime, primerange
from oeisterms import terms
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 26350
TLIM = float(sys.argv[2]) if len(sys.argv) > 2 else 280
t0 = time.time()
t, off = terms('A321766')
def perm(n):
    rows = [[j for j in range(1, n + 1) if isprime(3**i + 3**j - 1)] for i in range(1, n + 1)]
    order = sorted(range(n), key=lambda i: len(rows[i]))
    @lru_cache(maxsize=None)
    def go(r, mask):
        if r == n: return 1
        return sum(go(r + 1, mask | (1 << j)) for j in rows[order[r]] if not mask >> j & 1)
    v = go(0, 0); go.cache_clear(); return v
NT = int(sys.argv[3]) if len(sys.argv) > 3 else len(t)
assert [perm(n) for n in range(1, NT + 1)] == t[:NT]; print('terms ok', NT, '%.0fs' % (time.time() - t0), flush=True)
SP = list(primerange(5, 10**5))
def sieve_k(m, K):
    """alive[k] for 1<=k<=K: no prime factor <= 1e5 found (factor must be a proper factor)."""
    alive = np.ones(K + 1, bool); alive[0] = False
    for q in SP:
        tq = (1 - pow(3, m, q)) % q
        if tq == 0: continue
        x = 1; k0 = None
        for k in range(1, q):
            x = x * 3 % q
            if k0 is None and x == tq: k0 = k
            if x == 1: o = k; break
        if k0 is None: continue
        alive[k0::o] = False
    return alive
# cache discrete-log data per q to speed sieve: precompute 3^k tables lazily
dl = {}
SP = list(primerange(5, 3000))   # sieve primes (discrete-log tables kept small)
for q in SP:
    x = 1; tab = {}; 
    for k in range(1, q):
        x = x * 3 % q; 
        if x not in tab: tab[x] = k
        if x == 1: break
    dl[q] = (tab, k)
def sieve_fast(m, K):
    alive = np.ones(K + 1, bool); alive[0] = False
    for q in SP:
        tq = (1 - pow(3, m, q)) % q
        tab, o = dl[q]
        k0 = tab.get(tq)
        if k0 is not None: alive[k0::o] = False
    return alive
def f_from(m, lo, hi, alive):
    """least k in [lo, hi] with 3^m+3^k-1 BPSW-prime (sieve survivors only); None if none."""
    base = gmpy2.mpz(3)**m - 1
    for k in range(lo, hi + 1):
        if alive[k] and gmpy2.is_bpsw_prp(base + gmpy2.mpz(3)**k): return k
    return None
KMAX = 4 * TARGET
chain = []
m = 154; al = sieve_fast(m, KMAX); F = f_from(m, 1, KMAX, al); chain.append((m, F))
print('m=154 f=', F, flush=True)
dead = set()
while F is not None and F <= TARGET and time.time() - t0 < TLIM:
    n = F   # first uncovered n
    cands = []
    for mm in range(155, n + 1):
        if mm in dead: continue
        a = sieve_fast(mm, n)
        cands.append((int(a.sum()), mm))
    cands.sort()
    found = None
    for _, mm in cands:
        if time.time() - t0 > TLIM: break
        a = sieve_fast(mm, KMAX)
        k = f_from(mm, 1, n, a)
        if k is not None: dead.add(mm); continue
        k = f_from(mm, n + 1, KMAX, a)
        found = (mm, k if k is not None else float('inf')); break
    if found is None: break
    chain.append(found); F = found[1]
    print('chain', found, '%.0fs' % (time.time() - t0), flush=True)
covered = min(F - 1, 10**12) if F is not None else None
print('chain', chain)
import json; json.dump([[a, (b if b != float('inf') else -1)] for a, b in chain], open(__file__.rsplit('/', 1)[0] + '/chain.json', 'w'))
print('covered n in [154, %s] (target %d)' % (covered, TARGET))
