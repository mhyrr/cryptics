# A397208: a(n) = #{primes q < p=prime(n) : (p+q)/4 prime}. Conjecture: zeros only at p=2,3,11,19,43,67 (verified n<=10000).
# Method a: sieve; for each p scan primes q<p ascending, test (p+q)%4==0 and (p+q)/4 prime.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
from numba import njit
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 100000   # number of primes n
LIM = 2_000_000
s = np.ones(LIM, dtype=np.bool_); s[:2] = False
for i in range(2, int(LIM**0.5) + 1):
    if s[i]: s[i*i::i] = False
P = np.nonzero(s)[0]
assert len(P) >= NN
@njit(cache=True)
def cnt(i, P, s, stop_first):
    p = P[i]; c = 0
    for j in range(i):
        q = P[j]
        if (p + q) % 4 == 0 and s[(p + q) // 4]:
            c += 1
            if stop_first: return 1
    return c
T, off = terms("A397208")
assert [cnt(i, P, s, False) for i in range(len(T))] == T; print("terms OK", len(T))
zeros = [int(P[i]) for i in range(NN) if cnt(i, P, s, True) == 0]
print("zeros among first", NN, "primes (p<=%d):" % P[NN-1], zeros)
print("RESULT", "holds for n<=%d" % NN if zeros == [2, 3, 11, 19, 43, 67] else "COUNTEREXAMPLE p=%s" % zeros)
