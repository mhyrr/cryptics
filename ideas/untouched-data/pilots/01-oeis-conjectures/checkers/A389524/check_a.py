# A389524: T(1,1)=1, T(n,k) = [n>=k](1 + Sum_{i=1..k-1} T(n-i,k-1) - Sum_{i=1..n-1} T(n-i,k)).
# Conjecture 1: Sum_k T(n,k) = d(n) (verified n<=1000). Also tested: Conjecture 3, T(2n,n) = n - d(n) (verified n<=250).
# Method a: the recurrence literally, column by column (column k needs only column k-1), prefix sums, exact Python ints
# (entries exceed 2^63 near n~6500, so no fixed-width arithmetic).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
rows = [0] * (N + 1); diag = [0] * (N // 2 + 1); tri = {}
prevP = [0] * (N + 1); mx = 0
for k in range(1, N + 1):
    P = [0] * (N + 1); S = 0
    for n in range(k, N + 1):
        t = 1 - S if k == 1 else 1 + (prevP[n - 1] - prevP[n - k]) - S
        S += t; P[n] = S; rows[n] += t
        if n == 2 * k: diag[k] = t
        if n <= 15: tri[(n, k)] = t
        if t > mx or -t > mx: mx = abs(t)
    prevP = P
T, off = terms("A389524")
assert [tri[(n, k)] for n in range(1, 16) for k in range(1, n + 1)][:len(T)] == T; print("terms OK", len(T))
d = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i): d[j] += 1
b1 = [n for n in range(1, N + 1) if rows[n] != d[n]]
b3 = [n for n in range(1, N // 2 + 1) if diag[n] != n - d[n]]
print("max |T| has", len(str(mx)), "digits;  conj3 bad:", b3[:5])
print("RESULT", "holds for n<=%d" % N if not b1 else "COUNTEREXAMPLE n=%s" % b1[:5])
