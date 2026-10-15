# A048881: a(n) = wt(n+1)-1. Conjecture: a(n) = digit sum of n-th word of A076478 (n>=1).
# Method a: words generated as all binary vectors of length L=1,2,... in numerical order.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
T, off = terms("A048881")
a = lambda n: bin(n + 1).count("1") - 1
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
words = []
L = 1
while len(words) < N:
    for v in range(2 ** L):
        words.append(format(v, "0%db" % L))
        if len(words) >= N: break
    L += 1
bad = [n for n in range(1, N + 1) if sum(map(int, words[n - 1])) != a(n)]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
