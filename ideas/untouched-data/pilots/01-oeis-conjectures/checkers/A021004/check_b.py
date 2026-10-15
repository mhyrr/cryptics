# A021004 method b: generate b(n) from the conjectured linear recurrence (seeded with the first 6 Pisot terms
# computed by the PARI pisotP translation), then verify the Pisot rule b(n) = ceil(b(n-1)^2/b(n-2) - 1/2)
# via the integer inequality  -b(n-2) < 2*(b(n-1)^2 - b(n)*b(n-2)) <= b(n-2).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from fractions import Fraction
import math
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
T, off = terms("A021004")
seed = [4, 10]
for n in range(2, 6): seed.append(math.ceil(Fraction(seed[-1] ** 2, seed[-2]) - Fraction(1, 2)))
b = seed[:]
for n in range(6, N + 1): b.append(2*b[-1] + b[-2] + b[-3] - b[-4] - b[-6])
assert b[:len(T)] == T; print("terms OK", len(T))
bad = None
for n in range(2, N + 1):
    e = 2 * (b[n - 1] ** 2 - b[n] * b[n - 2])
    if not (-b[n - 2] < e <= b[n - 2]): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
