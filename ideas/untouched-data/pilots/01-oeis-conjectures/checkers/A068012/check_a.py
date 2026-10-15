# A068012: number of subsets of {1..n} summing to 0 mod 6. Conjecture: a(n) = 2a(n-1) for n>2 with 3 !| (n-1).
# Method a: DP over residues mod 6 with exact integers.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
T, off = terms("A068012")
c = [1, 0, 0, 0, 0, 0]; A = [1]
for n in range(1, N + 1):
    c = [c[r] + c[(r - n) % 6] for r in range(6)]; A.append(c[0])
assert A[off:off + len(T)] == T; print("terms OK", len(T))
bad = next((n for n in range(3, N + 1) if (n - 1) % 3 and A[n] != 2 * A[n - 1]), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
