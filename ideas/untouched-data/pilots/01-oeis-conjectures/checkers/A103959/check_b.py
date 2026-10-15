# A103959 checker b: primes from a numpy sieve; for each p scan sieve-listed primes q, test p*q-2 with sympy.isprime;
# also directly checks only q <= p (conjecture <=> some prime q <= p works).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np
from sympy import isprime
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
M = 20_000_000
s = np.ones(M, dtype=bool); s[:2] = False
for i in range(2, int(M ** .5) + 1):
    if s[i]: s[i * i::i] = False
PR = np.nonzero(s)[0].tolist()
assert len(PR) >= N
def a_of_p(p):
    for q in PR:
        if isprime(p * q - 2): return q
check_terms("A103959", lambda n: a_of_p(PR[n - 1]))
bad = []
for n in range(1, N + 1):
    p = PR[n - 1]
    ok = False
    for q in PR:
        if q > p: break
        if isprime(p * q - 2): ok = True; break
    if not ok: bad.append((n, p))
print("N =", N, "violations:", bad[:10])
