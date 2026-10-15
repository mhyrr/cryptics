# A000041 method b: profile DP with big-int bitsets. Process the elements p(k)+2 in increasing order; the state
# is the set of chosen elements that divide some later element (only those can create conflicts later);
# an element may be added only if no chosen element in the state divides it. p(k) from sympy's partition().
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from sympy.functions.combinatorial.numbers import partition
N = int(sys.argv[1]) if len(sys.argv) > 1 else 71400
T, off = terms("A000041")
assert [int(partition(n)) for n in range(len(T))] == T; print("terms OK", len(T))
B = []; k = 1
while int(partition(k)) + 2 <= N: B.append(int(partition(k)) + 2); k += 1
B = sorted(set(B))
mask = (1 << (N + 1)) - 1
S0 = [x for x in B if any(y % x == 0 for y in B if y > x)]
states = {(): 1}            # frozen tuple of chosen S0 elements -> bitset of reachable sums
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
bad = [n for n in fails if n > 2 and n != 6]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
