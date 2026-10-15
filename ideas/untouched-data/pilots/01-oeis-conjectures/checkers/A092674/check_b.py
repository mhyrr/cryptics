# A092674 via closed form derived by Moebius inversion of the defining recurrence:
#   sum_{d|n} c(d) = h(n), h(1)=0, h(2)=3, h(n)=n (n>=3)  =>  c = mu * h,
# computed here by a divisor-sum sieve (not the closed form) to stay independent of the derivation.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
h = [0] * (N + 1)
for n in range(1, N + 1): h[n] = n
h[1] = 0
if N >= 2: h[2] = 3
c = h[:]                       # Dirichlet-inverse sieve: c(n) = h(n) - sum_{d|n, d<n} c(d)
for d in range(1, N + 1):
    for m in range(2 * d, N + 1, d):
        c[m] -= c[d]
check_terms("A092674", lambda n: c[n])
neg = [n for n in range(1, N + 1) if c[n] < 0]
print("N =", N, "negatives:", neg[:10], "min =", min(c[1:]))
