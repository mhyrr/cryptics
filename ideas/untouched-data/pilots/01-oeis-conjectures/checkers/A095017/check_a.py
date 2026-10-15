# A095017: a(n) = #lesser twin primes p in (2^n, 2^(n+1)].
# Part 1: reproduce data terms for n <= NREP by a numpy sieve (full count).
# Part 2: conjecture a(n) > 0: for each n <= N find the smallest lesser twin prime in (2^n, 2^(n+1)]
#         (ascending search, small-prime presieve, gmpy2.is_prime = 25-round Miller-Rabin on both p, p+2).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np, gmpy2
from k2common import terms
NREP = 27; N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
T = [None] + terms("A095017")   # offset 1
M = 2 ** (NREP + 1) + 3
s = np.ones(M, dtype=bool); s[:2] = False
for p in range(2, int(M ** 0.5) + 1):
    if s[p]: s[p * p::p] = False
tw = np.nonzero(s[:-2] & s[2:])[0]
for n in range(1, NREP + 1):
    c = int(((tw > 2 ** n) & (tw <= 2 ** (n + 1))).sum())
    assert c == T[n], (n, c, T[n])
print(f"reproduced data terms n=1..{NREP} (of {len(T)} given; larger terms need a sieve to 2^40)")
small = [int(p) for p in np.nonzero(s[:20000])[0]]
def first_twin(n):
    lo = 2 ** n + 1
    if n <= 20:
        for p in range(lo, 2 ** (n + 1) + 1):
            if gmpy2.is_prime(p) and gmpy2.is_prime(p + 2): return p
        return None
    p = lo + ((5 - lo) % 6)   # lesser twins > 3 are 5 mod 6
    hi = 2 ** (n + 1)
    while p <= hi:
        if all((p % q) and ((p + 2) % q) for q in small[:300]):
            if gmpy2.is_prime(p, 25) and gmpy2.is_prime(p + 2, 25): return p
        p += 6
    return None
bad = []
for n in range(1, N + 1):
    p = first_twin(n)
    if p is None: bad.append(n); print("NO TWIN for n =", n)
    if n % 100 == 0: print(n, "offset of first twin above 2^n:", None if p is None else p - 2 ** n, flush=True)
print("N =", N, "failures:", bad)
