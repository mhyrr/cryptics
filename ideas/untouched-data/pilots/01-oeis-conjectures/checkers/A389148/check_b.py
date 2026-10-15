# A389148, method b. Terms: C. W. Wu's generator from the entry (second Python program), first len(data) terms.
# Conjecture (see check_a.py): squarefree classes of m! hashed by a 128-bit linear (XOR) key pair with a different seed and
# key generator from method a (linear hashing cannot miss a true equality; every hit is verified exactly with Legendre's
# formula in Python, so conclusions are exact). For composite e in (E0,E]: high solutions (b,c,d in [P,e)) enumerated with
# d outermost; if one exists, search for c<P with d descending and (b,c) pairs ordered by gap c-b (method a: c then b).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from math import prod
from itertools import count, islice
from sympy import factorint, isprime, prevprime, primerange
E = int(sys.argv[1]) if len(sys.argv) > 1 else 94690
E0 = int(sys.argv[2]) if len(sys.argv) > 2 else 9469
def A389148_gen(): # generator of terms (Chai Wah Wu, from the entry)
    g, p, r = [set()], 0, {}
    for c in count(2):
        f = factorint(c)
        d = g[-1]^set(i for i, j in f.items() if j&1)
        for h in g:
            if (t:=prod(d^h)) not in r:
                r[t] = c-1
        g.append(d)
        if isprime(c):
            p = c-2
        elif any(not c%q for q in (2,3,5,7,11)):
            continue
        elif max(f.values())>1:
            continue
        else:
            for b in range(c-2,p,-1):
                u = d^g[b]
                for a in range(b-1,1,-1):
                    e = prod(u^g[a])
                    if e in r and r[e]<a:
                        break
                else:
                    continue
                break
            else:
                yield c
T, off = terms("A389148")
import time; _t = time.time()
assert list(islice(A389148_gen(), len(T))) == T; print("terms OK", len(T), "(%.0fs)" % (time.time() - _t), flush=True)
import numpy as np
from numba import njit
rng = np.random.default_rng(20251006)
k1 = rng.integers(0, 2**64 - 1, size=E + 1, dtype=np.uint64, endpoint=True)
k2 = rng.integers(0, 2**64 - 1, size=E + 1, dtype=np.uint64, endpoint=True)
@njit(cache=True)
def build(E, k1, k2):
    v1 = np.zeros(E + 1, np.uint64); v2 = np.zeros(E + 1, np.uint64)
    for m in range(2, E + 1):
        s1 = np.uint64(0); s2 = np.uint64(0); t = m; p = 2
        while p * p <= t:
            e = 0
            while t % p == 0: t //= p; e += 1
            if e & 1: s1 ^= k1[p]; s2 ^= k2[p]
            p += 1
        if t > 1: s1 ^= k1[t]; s2 ^= k2[t]
        v1[m] = v1[m - 1] ^ s1; v2[m] = v2[m - 1] ^ s2
    return v1, v2
v1, v2 = build(E, k1, k2)
idx = np.arange(1, E + 1)
o = np.lexsort((idx, v2[1:], v1[1:])); H1 = v1[1:][o]; H2 = v2[1:][o]; AA = idx[o]
keep = np.ones(len(H1), np.bool_); keep[1:] = (H1[1:] != H1[:-1]) | (H2[1:] != H2[:-1])
H1 = H1[keep].copy(); H2 = H2[keep].copy(); AA = AA[keep].astype(np.int64).copy()
@njit(cache=True)
def mina(h1, h2, H1, H2, AA):
    i = np.searchsorted(H1, h1)
    while i < len(H1) and H1[i] == h1:
        if H2[i] == h2: return AA[i]
        i += 1
    return 1 << 62
@njit(cache=True)
def high(e, P, v1, v2, H1, H2, AA):
    for d in range(P, e):
        for c in range(P, d):
            for b in range(P, c):
                a = mina(v1[b] ^ v1[c] ^ v1[d] ^ v1[e], v2[b] ^ v2[c] ^ v2[d] ^ v2[e], H1, H2, AA)
                if a < b: return a, b, c, d
    return 0, 0, 0, 0
@njit(cache=True)
def low(e, P, v1, v2, H1, H2, AA, maxit):
    # d descending; pairs (b,c) with c<P enumerated by gap L=c-b ascending, c descending within a gap (method a: c then b)
    it = 0
    for d in range(e - 1, P - 1, -1):
        w1 = v1[d] ^ v1[e]; w2 = v2[d] ^ v2[e]
        for L in range(1, P - 2):
            for c in range(P - 1, L + 1, -1):
                b = c - L
                it += 1
                if it > maxit: return -1, 0, 0, 0, it
                a = mina(w1 ^ v1[c] ^ v1[b], w2 ^ v2[c] ^ v2[b], H1, H2, AA)
                if a < b: return a, b, c, d, it
    return 0, 0, 0, 0, it
def verify(a, b, c, d, e):
    def leg(n, p):
        t = 0
        while n: n //= p; t += n
        return t
    return 1 <= a < b < c < d < e and all(sum(leg(m, p) for m in (a, b, c, d, e)) % 2 == 0 for p in primerange(2, e + 1))
nhigh = 0; bad = []; maxit = 0; und = []
for e in range(E0 + 1, E + 1):
    if isprime(e): continue
    P = prevprime(e)
    a, b, c, d = high(e, P, v1, v2, H1, H2, AA)
    if a == 0: continue
    assert verify(a, b, c, d, e); nhigh += 1
    a, b, c, d, it = low(e, P, v1, v2, H1, H2, AA, 3 * 10**9); maxit = max(maxit, it)
    if a == -1: und.append(e); print('UNDECIDED', e, flush=True); continue
    if a == 0: bad.append(e); print("NO LOW SOLUTION", e, flush=True); continue
    assert verify(a, b, c, d, e), (a, b, c, d, e)
print("composite e in (%d,%d] with a high solution: %d; max low-search iterations %d" % (E0, E, nhigh, maxit))
print("RESULT", ("holds for e<=%d" % E if not und else "undecided e=%s" % und) if not bad else "COUNTEREXAMPLE e=%s" % bad)
