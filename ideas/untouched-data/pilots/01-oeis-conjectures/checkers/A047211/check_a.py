# A047211: n == 2,4 (mod 5). Arndt's conjecture: these are exactly the n for which the charpoly of M(n) is
# irreducible over Q, where M(n) (n X n) has ones on and below the skew diagonal and on the skew line two above it.
# Method a: exact integer charpoly (flint fmpz_mat) and full factorisation over Z (flint). Tests n = START..N,
# stopping at a CPU deadline; prints the last n completed. (n = 1 gives x - 1, irreducible but not in the
# sequence: degree-1 edge case, reported separately, not counted.)
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import flint
START = int(sys.argv[1]) if len(sys.argv) > 1 else 2
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1770
DEADLINE = float(sys.argv[3]) if len(sys.argv) > 3 else 280
T, off = terms("A047211")
assert [(5 * n - 1) // 2 for n in range(1, len(T) + 1)] == T; print("terms OK", len(T))
def M(n):
    return flint.fmpz_mat([[1 if (c >= n + 1 - r or c == n - 1 - r) else 0 for c in range(1, n + 1)] for r in range(1, n + 1)])
assert str(M(7).charpoly()) == "x^7 + (-5)*x^6 + (-4)*x^5 + 15*x^4 + 5*x^3 + (-11)*x^2 + (-1)*x + 1"   # %e example
t0 = time.process_time(); bad = None; last = None
for n in range(START, N + 1):
    if time.process_time() - t0 > DEADLINE: break
    fac = M(n).charpoly().factor()[1]
    irred = len(fac) == 1 and fac[0][1] == 1
    if irred != (n % 5 in (2, 4)): bad = n; print("witness factor degrees", [(g.degree(), e) for g, e in fac]); break
    last = n
print("completed n =", START, "..", last)
print("RESULT", "holds to %d" % last if bad is None else "COUNTEREXAMPLE n=%d" % bad)
