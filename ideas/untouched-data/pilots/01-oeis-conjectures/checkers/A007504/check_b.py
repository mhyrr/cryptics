# A007504 method b: a(n) from PARI vecsum(primes(n)); for each target n search k (2a(k) <= n) and i with
# n - 2a(k) - a(i) in the set of sums (hash-set lookups).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
T, off = terms("A007504")
assert [int(pari("vecsum(primes(%d))" % n)) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
S = []; n = 1
while True:
    v = int(pari("vecsum(primes(%d))" % n))
    if v > N: break
    S.append(v); n += 1
Sset = set(S)
def rep(n):
    for c in S:
        r = n - 2 * c
        if r < 2 * S[0]: return False
        for x in S:
            if x > r - x: break
            if (r - x) in Sset: return True
    return False
miss = [n for n in range(1, N + 1) if not rep(n)]
print("largest non-representable:", max(miss), "count", len(miss))
bad = [n for n in miss if n >= 5340]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
