# A003592 method b: profile DP with big-int bitsets (state = chosen elements that divide a later element).
# Elements generated as 2^a*5^b+1 by a heap-free double loop (translation of the PARI list()).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 37000
T, off = terms("A003592")
def lst(lim):
    v = []; n5 = 1
    while n5 <= lim:
        m = n5
        while m <= lim: v.append(m); m <<= 1
        n5 *= 5
    return sorted(v)
assert lst(T[-1]) == T; print("terms OK", len(T))
B = sorted(set(x + 1 for x in lst(N)))
mask = (1 << (N + 1)) - 1
S0 = set(x for x in B if any(y % x == 0 for y in B if y > x))
states = {(): 1}
for x in B:
    new = dict(states)
    for st, bs in states.items():
        if any(x % c == 0 for c in st): continue
        nst = tuple(sorted(st + (x,))) if x in S0 else st
        new[nst] = new.get(nst, 0) | ((bs << x) & mask)
    states = new
reach = 0
for bs in states.values(): reach |= bs
fails = [n for n in range(1, N + 1) if not (reach >> n) & 1]
print("non-representable n:", fails, " #states", len(states))
bad = [n for n in fails if n not in (1, 4, 12)]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
