# A389524, method b: derived recurrence. With C(n)=Sum_{m<=n}T(m,k) the definition gives C(n)=1+W(n), W(n)=Sum_{i=1..k-1}T(n-i,k-1),
# hence T(k,k)=1+Sum_{m<k}T(m,k-1) and T(n,k)=T(n-1,k-1)-T(n-k,k-1) for n>k. Vectorized numpy per column with dtype=object (exact Python ints).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
import numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
rows = np.zeros(N + 1, dtype=object); diag = {}; small = {}
col = np.zeros(N + 1, dtype=object); col[1] = 1          # column 1: T(n,1) = [n==1]
rows += col; mx = 1
for n in range(1, 16): small[(n, 1)] = int(col[n])
for k in range(2, N + 1):
    new = np.zeros(N + 1, dtype=object)
    new[k] = 1 + col[1:k].sum()
    if k < N: new[k + 1:] = col[k:N] - col[1:N + 1 - k]
    col = new; rows += col
    mx = max(mx, int(np.abs(col).max()))
    if 2 * k <= N: diag[k] = int(col[2 * k])
    if k <= 15:
        for n in range(k, 16): small[(n, k)] = int(col[n])
diag[1] = 0
print("max |T| has", len(str(mx)), "digits")
T, off = terms("A389524")
flat = [small[(n, k)] for n in range(1, 16) for k in range(1, n + 1)]
assert flat[:len(T)] == T; print("terms OK", len(T))
d = np.zeros(N + 1, np.int64)
for i in range(1, N + 1): d[i::i] += 1
b1 = [n for n in range(1, N + 1) if rows[n] != d[n]]
b3 = [n for n in range(1, N // 2 + 1) if diag[n] != n - d[n]]
print("max |T| =", mx, " conj3 bad:", b3[:5])
print("RESULT", "holds for n<=%d" % N if not b1 else "COUNTEREXAMPLE n=%s" % b1[:5])
