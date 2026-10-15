"""A321766 check_b: independent verification of the certificate chain.json written by check_a: chain (m_i, F_i) with
m_1 = 154, m_{i+1} <= F_i, and for every link all of 3^m_i + 3^k - 1 (1 <= k < F_i) proven composite here by trial
division (primes < 1000) or a failed base-2 Fermat test (gmpy2.powmod); then every n in [154, F_last - 1] has a witness m.
Terms a(n) re-derived as permanents by Ryser's formula (n <= 16) and a column-ordered matching DP (all listed n)."""
import sys, json, gmpy2; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from functools import lru_cache
from itertools import combinations
from sympy import isprime, primerange
from oeisterms import terms
t, off = terms('A321766')
NT = int(sys.argv[1]) if len(sys.argv) > 1 else len(t)
def mat(n): return [[1 if isprime(3**i + 3**j - 1) else 0 for j in range(1, n + 1)] for i in range(1, n + 1)]
def ryser(A):
    n = len(A); tot = 0
    for r in range(1, n + 1):
        for S in combinations(range(n), r):
            p = 1
            for row in A:
                p *= sum(row[j] for j in S)
                if not p: break
            tot += (-1)**r * p
    return (-1)**n * tot
def colperm(A):
    n = len(A); cols = [[i for i in range(n) if A[i][j]] for j in range(n)]
    @lru_cache(maxsize=None)
    def go(c, mask):
        if c == n: return 1
        return sum(go(c + 1, mask | 1 << i) for i in cols[c] if not mask >> i & 1)
    return go(0, 0)
for n in range(1, NT + 1):
    A = mat(n); v = colperm(A)
    if n <= 16: assert ryser(A) == v
    assert v == t[n - 1], n
print('terms ok', NT, flush=True)
chain = json.load(open(__file__.rsplit('/', 1)[0] + '/chain.json'))
SP = list(primerange(5, 1000))
assert chain[0][0] == 154
ok = True; prev = None
for m, F in chain:
    if prev is not None and not (m <= prev): ok = False; print('link order broken', m, prev)
    base = 3**m - 1
    for k in range(1, F):
        N = base + 3**k
        if any(N % q == 0 and N != q for q in SP): continue
        if gmpy2.powmod(2, N - 1, N) != 1: continue
        ok = False; print('could not prove composite: m', m, 'k', k); break
    prev = F
    print(' link', m, F, 'verified', flush=True)
print('chain verified:', ok, '-> covered n in [154, %d]' % (chain[-1][1] - 1))
