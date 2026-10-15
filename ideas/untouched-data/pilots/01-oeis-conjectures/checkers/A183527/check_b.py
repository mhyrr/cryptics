# A183527 checker b: Python big-int bitsets. ONE_k = sums with >=1 representation as k distinct terms,
# TWO_k = sums with >=2; adding term t: TWO_k |= TWO_{k-1}<<t | (ONE_k & ONE_{k-1}<<t); ONE_k |= ONE_{k-1}<<t.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
from gf183527 import gf_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
G = gf_terms(N)
ONE = [1, 0, 0, 0, 0]; TWO = [0, 0, 0, 0, 0]   # ONE[0] = {0} (empty sum)
seq = []
def add(t):
    for k in (4, 3, 2, 1):
        sh1 = ONE[k - 1] << t; sh2 = TWO[k - 1] << t
        TWO[k] |= sh2 | (ONE[k] & sh1)
        ONE[k] |= sh1
for t in (1, 2, 3, 4): seq.append(t); add(t)
while len(seq) < N:
    uniq = (ONE[4] & ~TWO[4]) >> (seq[-1] + 1)
    t = seq[-1] + 1 + ((uniq & -uniq).bit_length() - 1)
    seq.append(t); add(t)
check_terms("A183527", lambda n: seq[n - 1])
bad = [n for n in range(1, N + 1) if seq[n - 1] != G[n - 1]]
print("N =", N, "first mismatch vs conjectured g.f.:", bad[:5], "| a(N) =", seq[-1])
