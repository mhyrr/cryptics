# A397434, method b: ANF coefficients from Pascal's triangle mod 2 held as bitsets (row_d = row_{d-1} ^ row_{d-1}<<1),
# coefficient = parity of the first t bits of row d; binomials C(n,d) from additive Pascal rows (Python ints).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
rows2 = [1]
for d in range(1, N + 2): r = rows2[-1]; rows2.append(r ^ (r << 1))
vals = [None]; row = [1]
for n in range(1, N + 2):
    row = [1] + [row[i - 1] + row[i] for i in range(1, n)] + [1]
    t = (n + 1) // 2; mask = (1 << t) - 1
    vals.append(sum(row[d] for d in range(1, n + 1) if bin(rows2[d] & mask).count("1") & 1))
T, off = terms("A397434")
assert vals[1:1 + len(T)] == T; print("terms OK", len(T))
bad = [n for n in range(1, N + 1) if (vals[n] == vals[n + 1]) != (n % 4 == 2)]
print("tested 1<=n<=", N)
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[:5])
