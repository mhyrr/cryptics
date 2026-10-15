# A001599 method b: harmonic numbers by a prime-power sieve (for each p^k <= X, every multiple of p^k gets its
# exponent of p incremented; sigma, tau then assembled multiplicatively), in segments (numba).
# Zumkeller test: Stewart's practical-number criterion + sigma even (a practical number is Zumkeller iff sigma
# is even: Peng & Bhaskara Rao 2013); non-practical terms fall back to an explicit divisor-partition DFS.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np, numba
from sympy import primerange, factorint, divisors
X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
T, off = terms("A001599")
primes = np.array(list(primerange(2, int(X ** 0.5) + 2)), dtype=np.int64)
@numba.njit
def segment(L, S, primes):
    rem = np.arange(L, L + S, dtype=np.int64)
    sig = np.ones(S, np.int64); tau = np.ones(S, np.int64)
    cnt = np.zeros(S, np.int64)
    for p in primes:
        if p * p > L + S: break
        pk = p
        while pk < L + S:
            st = ((L + pk - 1) // pk) * pk
            for m in range(st, L + S, pk): cnt[m - L] += 1
            pk *= p
        st = ((L + p - 1) // p) * p
        for m in range(st, L + S, p):
            i = m - L; e = cnt[i]; q = p ** e
            rem[i] //= q; sig[i] *= (q * p - 1) // (p - 1); tau[i] *= e + 1; cnt[i] = 0
    out = []
    for i in range(S):
        if rem[i] > 1: sig[i] *= rem[i] + 1; tau[i] *= 2
        n = L + i
        if (n * tau[i]) % sig[i] == 0: out.append(n)
    return out
H = []; L = 1; S = 1 << 22
while L <= X:
    H += list(segment(L, min(S, X - L + 1), primes)); L += S
print("harmonic numbers <= %g: %d" % (X, len(H)))
assert H == [t for t in T if t <= X] or H[:len(T)] == T; print("terms OK", min(len(T), len(H)))
def sigma_pe(p, e): return (p ** (e + 1) - 1) // (p - 1)
def practical(n):
    f = sorted(factorint(n).items())
    if f[0][0] != 2: return False
    s = 1
    for p, e in f:
        if p > 1 + s: return False
        s *= sigma_pe(p, e)
    return True
def dfs_zumkeller(n):
    ds = sorted(divisors(n), reverse=True); tot = sum(ds)
    if tot % 2: return False
    suf = [0] * (len(ds) + 1)
    for i in range(len(ds) - 1, -1, -1): suf[i] = suf[i + 1] + ds[i]
    def rec(i, r):
        if r == 0: return True
        if i == len(ds) or suf[i] < r: return False
        return (ds[i] <= r and rec(i + 1, r - ds[i])) or rec(i + 1, r)
    return rec(0, tot // 2)
bad = None; nonprac = []
for n in H[1:]:
    sg = 1
    for p, e in factorint(n).items(): sg *= sigma_pe(p, e)
    if practical(n):
        ok = sg % 2 == 0
    else:
        nonprac.append(n); ok = dfs_zumkeller(n)
    if not ok: bad = n; break
print("non-practical harmonic numbers (tested by DFS):", nonprac)
print("RESULT", "holds for all %d terms <= %g (index %d)" % (len(H), X, len(H)) if bad is None else "COUNTEREXAMPLE n=%d" % bad)
