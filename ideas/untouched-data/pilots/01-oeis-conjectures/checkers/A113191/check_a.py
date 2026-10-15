# A113191 / Sun's conjecture: L(m)-L(n) (m>1, m>n>=0) is a perfect power (exponent>=2) but not a square
# only for (m,n)=(7,0),(5,2). Method a: gmpy2.is_power + is_square on every pair, m <= M.
# Data check: the sequence itself = sorted distinct values L(i)-L(j), reproduced up to the last data term.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2
from k2common import terms
M = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
L = [2, 1]
while len(L) <= M + 2: L.append(L[-1] + L[-2])
T = terms("A113191"); top = T[-1]
vals = sorted({L[i] - L[j] for i in range(40) for j in range(i) if 0 <= L[i] - L[j] <= top} | {0})
# note: the entry's Mathematica program uses j <= i-2 plus 0..; we reproduce its listed terms set-wise
assert [v for v in vals if v <= top] == T, (vals[:80], T)
print("reproduced all", len(T), "data terms")
hits = []
for m in range(2, M + 1):
    Lm = L[m]
    for n in range(m):
        d = gmpy2.mpz(Lm - L[n])
        if d > 1 and gmpy2.is_power(d) and not gmpy2.is_square(d):
            hits.append((m, n, int(d) if d < 10**12 else "big"))
    if m % 1000 == 0: print("m =", m, "hits so far", hits, flush=True)
print("M =", M, "non-square perfect powers:", hits)
