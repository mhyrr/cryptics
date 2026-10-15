# A076449: least number whose digits can be used to form exactly n different primes (some or all digits).
# Keith's conjecture: a(n) exists for every n (checked n <= 66).
# Key fact used: the count depends only on the digit multiset M of the number: c(M) = #{primes p : digits(p) is a
# sub-multiset of M} (a prime written with a leading zero is the same prime formed from fewer digits).
# Method a: numpy sieve to 10^D, f(S) = #primes with digit multiset exactly S, superset-sum (zeta transform) over
# all multisets of size <= D, then a(n) = least number realising a multiset with c = n (smallest nonzero digit,
# then zeros, then ascending). Reports the largest N such that every n <= N is realised with <= D digits.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np
from itertools import combinations_with_replacement
D = int(sys.argv[1]) if len(sys.argv) > 1 else 8
T, off = terms("A076449")
lim = 10 ** D
sv = np.ones(lim, bool); sv[:2] = False
for i in range(2, int(lim ** 0.5) + 1):
    if sv[i]: sv[i * i::i] = False
f = {}
for p in np.flatnonzero(sv):
    s = str(p); key = tuple(s.count(c) for c in "0123456789")
    f[key] = f.get(key, 0) + 1
Ms = []
for k in range(1, D + 1):
    for comb in combinations_with_replacement(range(10), k):
        Ms.append(tuple(comb.count(d) for d in range(10)))
g = {M: f.get(M, 0) for M in Ms}
g[(0,) * 10] = 0
for d in range(10):                               # zeta transform along digit d
    for M in sorted(g, key=lambda M: M[d]):
        if M[d] > 0:
            P = M[:d] + (M[d] - 1,) + M[d + 1:]
            g[M] += g[P]
def least(M):
    nz = [d for d in range(1, 10) if M[d]]
    if not nz: return None                        # all zeros: not a valid number (except 0)
    d0 = nz[0]; rest = list(M); rest[d0] -= 1
    return int(str(d0) + "".join(str(d) * rest[d] for d in range(10)))
best = {}
for M in Ms:
    x = least(M)
    if x is None: continue
    c = g[M]
    if c not in best or x < best[c]: best[c] = x
best.setdefault(0, 1)
calc = [best.get(n) for n in range(0, len(T))]
assert calc == T, [(n, calc[n], T[n]) for n in range(len(T)) if calc[n] != T[n]][:5]; print("terms OK", len(T))
Nmax = 0
while Nmax + 1 in best: Nmax += 1
print("max count with <= %d digits: %d; first missing n: %d" % (D, max(best), Nmax + 1))
print("RESULT", "holds to %d (exists with <= %d digits for all n <= %d)" % (Nmax, D, Nmax))
