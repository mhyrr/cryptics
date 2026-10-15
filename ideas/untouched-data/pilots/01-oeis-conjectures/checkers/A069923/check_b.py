# A069923 method b: PARI. Scan i = 2^n, 2^n+1, ... with ispseudoprime (BPSW) until a prime or past 2^n+prime(n).
# (interval pre-sieved by small primes). Terms by the PARI program with isprime -> ispseudoprime (speed).
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(10**9)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
T, off = terms("A069923")
assert [int(pari("sum(i=2^%d,2^%d+prime(%d),ispseudoprime(i))" % (n, n, n))) for n in range(1, len(T) + 1)] == T
print("terms OK", len(T))
# interval sieved by primes < 2^16 (2^n mod p by pow), survivors tested in order by PARI ispseudoprime
small = [int(x) for x in pari("primes(6542)")]
def first_gap(n):
    b = 1 << n; P = int(pari.prime(n)); alive = bytearray([1]) * (P + 1)
    for p in small:
        if p * p > b + P: break
        r = (-pow(2, n, p)) % p          # offset i with b+i == 0 mod p
        for i in range(r, P + 1, p):
            if b + i != p: alive[i] = 0
    for i in range(P + 1):
        if alive[i] and pari.ispseudoprime(b + i): return i
    return -1
import time; DEADLINE = 270; last = 0
bad = None; mx = (0, 0)
for n in range(1, N + 1):
    if time.time() - T0 > DEADLINE: N = last; print("deadline hit"); break
    last = n
    g = first_gap(n)
    if g < 0: bad = n; break
    mx = max(mx, (g / int(pari.prime(n)), n))
print("max (gap/prime(n), n):", mx, "last n", N)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
