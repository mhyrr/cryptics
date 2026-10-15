# A087716: base-2 Fermat pseudoprimes (composite N with 2^(N-1) == 1 mod N) of the form j*p(i)# -+ p(k) with
# p(i) < p(k) < p(i+1)^2 and 0 < j < p(i+1). Conjecture: only 5 terms (claimed checked for all i <= 150).
# Method a: gmpy2 powmod + is_prime, i = 1, 2, ... until a wall-clock deadline; prints the last complete i.
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
from sympy import prime, primerange
IMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A087716")
def psp2(N): return N > 2 and N % 2 == 1 and gmpy2.powmod(2, N - 1, N) == 1 and not gmpy2.is_prime(N)
found = set(); P = 1; last = 0
for i in range(1, IMAX + 1):
    if time.time() - T0 > DEADLINE: break
    p, q = prime(i), prime(i + 1); P *= p
    for r in primerange(q, q * q):            # p(i) < r < p(i+1)^2
        for j in range(1, q):
            for N in (j * P - r, j * P + r):
                if N > 0 and psp2(N): found.add(N)
    last = i
S = sorted(found)
print("found:", S[:20], "count", len(S))
assert S[:5] == T; print("terms OK", len(T))
print("RESULT", "holds to i=%d" % last if len(S) == 5 else "COUNTEREXAMPLE extra term %s" % S[5:])
