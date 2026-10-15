# A378252, method b: PARI via cypari2. Scan x = 2^n+1, 2^n+2, ...: x is a prime power iff ispseudoprime(x) or
# (ispower(x) gives base^k with ispseudoprime(base)). Small-prime pre-sieve only to skip obvious non-primes; every x is checked with ispower.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2 * 10**8)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1001
SP = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def least_pp(n):
    x = 2 ** n + 1
    while True:
        k = int(pari.ispower(x))
        if k >= 2:
            b = pari.sqrtnint(x, k)
            if pari.ispseudoprime(b): return x, False
        if (x < 50 or (x % 2 and all(x % p for p in SP))) and pari.ispseudoprime(x): return x, True
        x += 1
T, off = terms("A378252")
assert [least_pp(n)[0] for n in range(0, len(T))] == T; print("terms OK", len(T))
bad = [n for n in range(N0, N + 1) if not least_pp(n)[1]]
print("tested %d<=n<=%d" % (N0, N))
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad)
