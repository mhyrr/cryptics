# A183527: a(n)=n for n<=4; a(n) = least number > a(n-1) that is a unique sum of 4 distinct earlier terms.
# Conjecture: the g.f. in the %F line (rational, denominator -(1-x)(1-x^73)), verified for n<=1000.
# Method a: numpy arrays r1..r4 of representation counts capped at 2 (capping commutes with the monotone updates).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np
from k2common import check_terms
from gf183527 import gf_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
G = gf_terms(N)
MAXV = G[-1] + 10   # if the sequence ever exceeded the g.f. value we would detect divergence before this
r = [None] + [np.zeros(MAXV + 1, dtype=np.int8) for _ in range(4)]
seq = []
def add(t):
    for k in (4, 3, 2):
        r[k][t:] = np.minimum(r[k][t:] + r[k - 1][:MAXV + 1 - t], 2)
    r[1][t] = min(r[1][t] + 1, 2)
for t in (1, 2, 3, 4): seq.append(t); add(t)
while len(seq) < N:
    cand = np.nonzero(r[4][seq[-1] + 1:] == 1)[0]
    if len(cand) == 0: print("ran out of range at n =", len(seq) + 1); break
    t = seq[-1] + 1 + int(cand[0]); seq.append(t); add(t)
check_terms("A183527", lambda n: seq[n - 1])
bad = [n for n in range(1, len(seq) + 1) if seq[n - 1] != G[n - 1]]
print("N =", len(seq), "first mismatch vs conjectured g.f.:", bad[:5], "| a(N) =", seq[-1])
