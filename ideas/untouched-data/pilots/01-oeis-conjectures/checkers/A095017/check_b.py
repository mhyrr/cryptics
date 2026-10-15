# A095017 checker b: different method.
# Part 1: reproduce data terms n<=24 with a pure-python bytearray sieve.
# Part 2: for each n <= N find the LARGEST lesser twin p <= 2^(n+1) (descending search, p+2 may exceed 2^(n+1)
#         by definition only p must lie in the range), primality by sympy.isprime (BPSW).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from sympy import isprime
from k2common import terms
NREP = 24; N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
T = [None] + terms("A095017")
M = 2 ** (NREP + 1) + 3
s = bytearray([1]) * M; s[0] = s[1] = 0
for p in range(2, int(M ** 0.5) + 1):
    if s[p]: s[p * p::p] = bytearray(len(range(p * p, M, p)))
for n in range(1, NREP + 1):
    c = sum(1 for p in range(2 ** n + 1, 2 ** (n + 1) + 1) if s[p] and s[p + 2])
    assert c == T[n], (n, c, T[n])
print(f"reproduced data terms n=1..{NREP}")
from sympy import primerange
small = list(primerange(5, 2000))
def last_twin(n):
    lo = 2 ** n
    p = 2 ** (n + 1)
    p -= (p - 5) % 6 if n >= 3 else 0
    step = 6 if n >= 3 else 1
    while p > lo:
        if n < 3 or all((p % q) and ((p + 2) % q) for q in small if q < p):
            if isprime(p) and isprime(p + 2): return p
        p -= step
    return None
bad = []
for n in range(1, N + 1):
    p = last_twin(n)
    if p is None: bad.append(n); print("NO TWIN for n =", n)
    if n % 100 == 0: print(n, "first twin below 2^(n+1) at distance", None if p is None else 2 ** (n + 1) - p, flush=True)
print("N =", N, "failures:", bad)
