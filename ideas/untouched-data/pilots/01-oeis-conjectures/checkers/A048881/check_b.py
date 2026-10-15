# A048881 method b: a(n) = v2(C(2n,n)/(n+1)) via Legendre (v2(m!) = m - wt(m)), translating Somos's PARI;
# A076478 built as a flat bit stream (vectors of each length in numerical order), then cut into words.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
T, off = terms("A048881")
v2f = lambda m: m - bin(m).count("1")
a = lambda n: v2f(2 * n) - v2f(n) - v2f(n + 1)
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
stream = []; L = 1; total = 0; lengths = []
while total < N:
    for v in range(2 ** L):
        stream.extend((v >> (L - 1 - i)) & 1 for i in range(L)); lengths.append(L); total += 1
        if total >= N: break
    L += 1
pos = 0; bad = None
for n in range(1, N + 1):
    L = lengths[n - 1]; s = sum(stream[pos:pos + L]); pos += L
    if s != a(n): bad = n; break
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
