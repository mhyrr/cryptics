# A197653 (m=4 meanders). Conjecture: T(n,k) = A+B+C+D = Sum_{j=0..3} C(n,k)^(4-j) C(n,n-1-k)^j (DP-confirmed n<=43).
# Method a (see _k2/meander.py): forward DP with #L coordinate, additions mod 5 primes ~2^62, CRT.
# Rows n = N0..N1 from argv; data rows reproduced first.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from meander import row, closed
from k2common import terms
M = 4; ANUM = "A197653"; METHOD = "a"
T = terms(ANUM); i = 0; n = 0
while i < len(T):
    r = row(n, M, METHOD)
    for k in range(n + 1):
        if i < len(T): assert r[k] == T[i], (n, k, r[k], T[i]); i += 1
    n += 1
print("reproduced all", len(T), "data terms (rows 0..%d)" % (n - 1))
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
N1 = int(sys.argv[2]) if len(sys.argv) > 2 else 20
for n in range(N0, N1 + 1):
    t = time.time(); r = row(n, M, METHOD)
    bad = [k for k in range(n + 1) if r[k] != closed(n, k, M)]
    print("n =", n, "mismatching k:", bad, "%.1fs" % (time.time() - t), flush=True)
