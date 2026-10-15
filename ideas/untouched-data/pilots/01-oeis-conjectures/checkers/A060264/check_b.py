# A060264 method b: number theory. i^2 == j^2 (mod p), 1<=i<j<=n, iff p | (j-i) or p | (i+j).
# For each n, scan odd primes p upward and test the conditions p > n-1 and no s in [3,2n-1] with p | s
# (i.e. p > 2n-1) directly by looping over s, without using the closed form.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import gmpy2
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
T, off = terms("A060264")
def np_(m):  # first prime > m
    return int(gmpy2.next_prime(m))
assert [np_(2 * n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
def ok(p, n):
    if p == 2: return n <= 1
    if p <= n - 1: return False          # j - i = p is available
    # sums i+j range over 3..2n-1; a multiple of p in that range exists iff p <= 2n-1 (multiples p, 2p, ...)
    m = ((3 + p - 1) // p) * p
    return m > 2 * n - 1
bad = None
p = 2  # least valid p is nondecreasing in n (validity for n implies validity for n-1)
for n in range(3, N + 1):
    while not ok(p, n): p = np_(p)
    if p != np_(2 * n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
