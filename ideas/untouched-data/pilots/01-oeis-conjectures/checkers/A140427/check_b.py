# A140427 checker b: A169675 found by brute force as the lexicographically earliest length-8 cyclic binary word
# containing all 8 windows of length 3; A140427 by its g.f. x^4(x^4+x^3+x^2+1)/((x-1)^2(x+1)(x^2+1)(x^4+1)) via
# power-series division.
import sys, os, itertools; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
for w in itertools.product((0, 1), repeat=8):
    if len({(w[i], w[(i + 1) % 8], w[(i + 2) % 8]) for i in range(8)}) == 8: per = w; break
D = [per[i % 8] for i in range(N + 1)]
check_terms("A169675", lambda n: D[n], " (brute force)")
num = [0, 0, 0, 0, 1, 0, 1, 1, 1]
# denominator (x-1)^2 (x+1)(x^2+1)(x^4+1) expanded
def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): r[i + j] += x * y
    return r
den = mul(mul(mul([1, -1], [1, -1]), [1, 1]), mul([1, 0, 1], [1, 0, 0, 0, 1]))
A = []
for n in range(N + 1):
    v = (num[n] if n < len(num) else 0) - sum(den[j] * A[n - j] for j in range(1, len(den)) if j <= n)
    A.append(v // den[0] if den[0] == 1 else -v)
check_terms("A140427", lambda n: A[n])
s = 0; bad = []
for n in range(N + 1):
    if A[n] != s: bad.append(n)
    s += D[n]
print("N =", N, "mismatches:", bad[:10])
