# A389148: composite e>6 with no 1<=a<b<c<d<e such that a!b!c!d!e! is a square.
# Wu's conjecture (Sep 2025, "true for e<=9469"), read as: for every e that has a solution, some solution has c < P := A151799(e)
# (largest prime < e).  Parity of v_P forces d >= P, and c >= P forces b >= P ("high" solutions: b,c,d in [P,e)).
# So the conjecture can only fail at e having a high solution and no solution with c<P.
# Method a: Zobrist hashing of the squarefree class of m! (XOR of random 64-bit keys over primes with odd exponent), numba.
#  - terms: exhaustive search for e<=2771 with a pair table (min b per class of a!b!);
#  - conjecture: for each composite e in (E0, E], find high solutions by enumerating b<c<d in [P,e); if any, search
#    d in [P,e), c<P descending, b<c descending, lookup a; budget per e, undecided e reported.
# Every solution found is re-verified exactly in Python (prime exponents of a!b!c!d!e!).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
from sympy import isprime, prevprime, primerange
E = int(sys.argv[1]) if len(sys.argv) > 1 else 94690
E0 = int(sys.argv[2]) if len(sys.argv) > 2 else 9469
BUDGET = int(sys.argv[3]) if len(sys.argv) > 3 else 2 * 10**8
rng = np.random.default_rng(389148)
@njit(cache=True)
def build(E, keys):
    spf = np.zeros(E + 1, np.int64)
    for i in range(2, E + 1):
        if spf[i] == 0:
            for j in range(i, E + 1, i):
                if spf[j] == 0: spf[j] = i
    v = np.zeros(E + 1, np.uint64)
    for m in range(2, E + 1):
        s = np.uint64(0); t = m
        while t > 1:
            p = spf[t]; e = 0
            while t % p == 0: t //= p; e += 1
            if e & 1: s ^= keys[p]
        v[m] = v[m - 1] ^ s
    return spf, v
keys = rng.integers(1, 2**63, size=E + 1, dtype=np.int64).astype(np.uint64)
spf, v = build(E, keys)
# single table: class of a! -> min a (a>=1)
order = np.lexsort((np.arange(1, E + 1), v[1:])); sv = v[1:][order]; sa = (np.arange(1, E + 1))[order]
first = np.ones(len(sv), np.bool_); first[1:] = sv[1:] != sv[:-1]
SV = sv[first].copy(); SA = sa[first].astype(np.int64).copy()
@njit(cache=True)
def mina(SV, SA, h):
    i = np.searchsorted(SV, h)
    if i < len(SV) and SV[i] == h: return SA[i]
    return 1 << 62
@njit(cache=True)
def high(e, P, v, SV, SA):
    for b in range(P, e):
        for c in range(b + 1, e):
            for d in range(c + 1, e):
                a = mina(SV, SA, v[b] ^ v[c] ^ v[d] ^ v[e])
                if a < b: return a, b, c, d
    return 0, 0, 0, 0
@njit(cache=True)
def low(e, P, v, SV, SA, budget):
    it = 0
    for d in range(e - 1, P - 1, -1):
        w = v[d] ^ v[e]
        for c in range(P - 1, 2, -1):
            wc = w ^ v[c]
            for b in range(c - 1, 1, -1):
                it += 1
                if it > budget: return -1, 0, 0, 0, it
                a = mina(SV, SA, wc ^ v[b])
                if a < b: return a, b, c, d, it
    return 0, 0, 0, 0, it
def verify(a, b, c, d, e):
    def leg(n, p):
        t = 0
        while n: n //= p; t += n
        return t
    return 1 <= a < b < c < d < e and all(sum(leg(m, p) for m in (a, b, c, d, e)) % 2 == 0 for p in primerange(2, e + 1))
# ---- terms: exhaustive for e <= TT using a pair table
TT = 2771
pa = []; pb = []; ph = []
for b in range(2, TT):
    aa = np.arange(1, b); pa.append(aa); pb.append(np.full(b - 1, b)); ph.append(v[1:b] ^ v[b])
ph = np.concatenate(ph); pb = np.concatenate(pb)
o = np.lexsort((pb, ph)); ph = ph[o]; pb = pb[o]
f = np.ones(len(ph), np.bool_); f[1:] = ph[1:] != ph[:-1]; PH = ph[f].copy(); PB = pb[f].astype(np.int64).copy()
@njit(cache=True)
def any_solution(e, P, v, PH, PB, SV, SA):
    for d in range(P, e):
        w = v[d] ^ v[e]
        for c in range(3, P):
            h = w ^ v[c]
            i = np.searchsorted(PH, h)
            if i < len(PH) and PH[i] == h and PB[i] < c: return True
    a, b, c, d = high(e, P, v, SV, SA)
    return a > 0
seq = [e for e in range(7, TT + 1) if not isprime(e) and not any_solution(e, prevprime(e), v, PH, PB, SV, SA)]
T, off = terms("A389148")
assert seq == T, (seq[:10], T[:10]); print("terms OK", len(T))
# ---- conjecture
nhigh = 0; undecided = []; bad = []; maxit = 0
for e in range(E0 + 1, E + 1):
    if isprime(e): continue
    P = prevprime(e)
    a, b, c, d = high(e, P, v, SV, SA)
    if a == 0: continue
    nhigh += 1
    assert verify(a, b, c, d, e)
    a, b, c, d, it = low(e, P, v, SV, SA, BUDGET); maxit = max(maxit, it)
    if a == -1: undecided.append(e); print("UNDECIDED", e, flush=True); continue
    if a == 0: bad.append(e); print("NO LOW SOLUTION", e, flush=True); continue
    assert verify(a, b, c, d, e), (a, b, c, d, e)
print("composite e in (%d,%d] with a high solution: %d; max low-search iterations %d" % (E0, E, nhigh, maxit))
print("RESULT", ("holds for e<=%d" % E if not undecided else "undecided e=%s" % undecided[:10]) if not bad else "COUNTEREXAMPLE e=%s" % bad)
