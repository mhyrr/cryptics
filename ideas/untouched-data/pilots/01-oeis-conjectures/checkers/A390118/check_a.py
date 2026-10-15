# A390118: a(n) = least m>=1 with m*n+1 = p^2, p prime. Conjecture: a(n) <= (n+5)(n-1) for n>1 (verified n<=12000).
# a(n) = (p^2-1)/n for the least prime p with p^2 == 1 (mod n); the conjecture is p^2 <= n^3+4n^2-5n+1.
# Method a: sweep primes p upward to PMAX = sqrt(N^3+4N^2-5N+1); for each, enumerate divisors n<=N of (p-1)(p+1)
# (spf sieve) and set a(n) the first time n is hit.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
N = int(sys.argv[1]) if len(sys.argv) > 1 else 120000
PMAX = math.isqrt(N**3 + 4*N**2 - 5*N + 1) + 2
@njit(cache=True)
def run(N, PMAX):
    spf = np.zeros(PMAX + 2, np.int32)
    for i in range(2, PMAX + 2):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= PMAX + 1:
                for j in range(i * i, PMAX + 2, i):
                    if spf[j] == 0: spf[j] = i
    first = np.zeros(N + 1, np.int64)   # least prime p with p^2==1 mod n
    ps = np.zeros(64, np.int64); es = np.zeros(64, np.int64)
    divs = np.zeros(1 << 20, np.int64)
    for p in range(2, PMAX + 1):
        if spf[p] != p: continue
        # factor (p-1)(p+1)
        np_ = 0
        for t0 in (p - 1, p + 1):
            t = t0
            while t > 1:
                q = spf[t]; e = 0
                while t % q == 0: t //= q; e += 1
                found = False
                for i in range(np_):
                    if ps[i] == q: es[i] += e; found = True
                if not found: ps[np_] = q; es[np_] = e; np_ += 1
        nd = 1; divs[0] = 1
        for i in range(np_):
            cur = nd; pk = 1
            for e in range(es[i]):
                pk *= ps[i]
                for j in range(cur):
                    v = divs[j] * pk
                    if v <= N: divs[nd] = v; nd += 1
        for j in range(nd):
            d = divs[j]
            if first[d] == 0: first[d] = p
    return first
first = run(N, PMAX)
a = lambda n: (int(first[n]) ** 2 - 1) // n
T, off = terms("A390118")
assert [a(n) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
unset = [n for n in range(1, N + 1) if first[n] == 0]
bad = unset + [n for n in range(2, N + 1) if first[n] and a(n) > (n + 5) * (n - 1)]
mx = max(range(2, N + 1), key=lambda n: a(n) / ((n + 5) * (n - 1)) if first[n] else 9)
print("max ratio a(n)/((n+5)(n-1)) at n=%d: %.4f" % (mx, a(mx) / ((mx + 5) * (mx - 1))))
eq = [n for n in range(2, N + 1) if first[n] and a(n) == (n + 5) * (n - 1)]
print("#equality cases:", len(eq), eq[:15])
print("RESULT", "holds for 2<=n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % sorted(bad)[:10])
