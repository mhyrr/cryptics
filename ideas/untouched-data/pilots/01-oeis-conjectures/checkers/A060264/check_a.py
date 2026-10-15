# A060264: a(n) = first prime after 2n. Conjecture (n>2): a(n) = least prime p with 1^2..n^2 distinct mod p.
# Method a: brute force. For each prime p compute M(p) = largest n with 1^2..n^2 distinct mod p
# (by inserting squares until the first collision); then least p with M(p) >= n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np, numba
from sympy import primerange, nextprime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
T, off = terms("A060264")
assert [nextprime(2 * n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
@numba.njit
def M(p):
    seen = np.zeros(p, np.uint8); i = 1
    while True:
        r = (i * i) % p
        if seen[r]: return i - 1
        seen[r] = 1; i += 1
primes = list(primerange(2, 2 * N + 200))
Ms = [M(p) for p in primes]
# least p with M(p) >= n, for n = 3..N
best = {}; j = 0; bad = None
for n in range(3, N + 1):
    while Ms[j] < n: j += 1
    # M not monotone in p in principle, so scan from the start is needed; we keep j as the min index since
    # M(p) >= n implies M(p) >= n-1, so the least index for n is >= least index for n-1.
    if primes[j] != nextprime(2 * n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
