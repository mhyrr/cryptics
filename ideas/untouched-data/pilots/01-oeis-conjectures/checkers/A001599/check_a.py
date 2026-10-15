# A001599: harmonic (Ore) numbers: k with n*tau(n)/sigma(n) an integer. Ianakiev: all terms > 1 are Zumkeller
# (divisors split into two parts of equal sum). Verified for n <= 50 (term index).
# Method a: numba segmented sieve of sigma and tau up to X; each harmonic number is tested by a greedy
# descending-divisor partition of sigma/2 (with DFS fallback), and the witness half is re-verified.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np, numba
from sympy import divisors, primerange
X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
T, off = terms("A001599")
primes = np.array(list(primerange(2, int(X ** 0.5) + 2)), dtype=np.int64)
@numba.njit
def segment(L, S, primes):
    rem = np.arange(L, L + S, dtype=np.int64)
    sig = np.ones(S, np.int64); tau = np.ones(S, np.int64)
    for p in primes:
        if p * p > L + S: break
        st = ((L + p - 1) // p) * p
        for m in range(st, L + S, p):
            i = m - L; e = 0; pk = 1; s = 1
            while rem[i] % p == 0:
                rem[i] //= p; e += 1; pk *= p; s += pk
            sig[i] *= s; tau[i] *= e + 1
    out = []
    for i in range(S):
        if rem[i] > 1: sig[i] *= rem[i] + 1; tau[i] *= 2
        n = L + i
        if n >= 1 and (n * tau[i]) % sig[i] == 0: out.append(n)
    return out
t0 = time.time(); H = []; L = 1; S = 1 << 22
while L <= X:
    H += list(segment(L, min(S, X - L + 1), primes)); L += S
print("harmonic numbers <= %g: %d  (%.0fs)" % (X, len(H), time.time() - t0))
assert H[:len(T)] == T[:len(H)] and len(H) >= len(T) or H == [t for t in T if t <= X]; print("terms OK", min(len(T), len(H)))
def zumkeller_witness(n):
    ds = sorted(divisors(n), reverse=True); s = sum(ds)
    if s % 2: return None
    tgt = s // 2; pick = []; r = tgt
    for d in ds:
        if d <= r: pick.append(d); r -= d
    if r == 0: return pick
    suf = [0] * (len(ds) + 1)
    for i in range(len(ds) - 1, -1, -1): suf[i] = suf[i + 1] + ds[i]
    pick = []
    def dfs(i, r):
        if r == 0: return True
        if i == len(ds) or suf[i] < r: return False
        if ds[i] <= r:
            pick.append(ds[i])
            if dfs(i + 1, r - ds[i]): return True
            pick.pop()
        return dfs(i + 1, r)
    return pick if dfs(0, tgt) else None
bad = None
for n in H[1:]:
    w = zumkeller_witness(n)
    if w is None or sum(w) * 2 != sum(divisors(n)) or len(set(w)) != len(w) or any(n % d for d in w):
        bad = n; break
print("RESULT", "holds for all %d terms <= %g (index %d)" % (len(H), X, len(H)) if bad is None else "COUNTEREXAMPLE n=%d" % bad)
