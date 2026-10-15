# A092674: direct translation of the definition: s[1]=x, s[i]=binomial(i+1,2)-sum_{j<i} s[j]*floor(i/j);
# a(n) = constant term. Track constant parts with numpy int64 (values stay small).
# Conjecture tested: a(n) >= 0 for n <= N.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
c = np.zeros(N + 1, dtype=np.int64)  # constant terms
c[1] = 0
for i in range(2, N + 1):
    j = np.arange(1, i, dtype=np.int64)
    c[i] = i * (i + 1) // 2 - int(np.dot(c[1:i], i // j))
check_terms("A092674", lambda n: int(c[n]))
neg = np.nonzero(c[1:] < 0)[0]
print("N =", N, "negatives:", (neg + 1).tolist()[:10], "min =", int(c[1:].min()))
