# A140427 (defined by a(n)=0 for n<4, floor((n-4)^2/4)+1 for 4<=n<=7, a(n)=a(n-8)+4).
# Conjecture (Irvine): essentially partial sums of A169675 (lexicographically earliest binary de Bruijn sequence
# of order 3, periodic). Precisely tested: A140427(n) = Sum_{i=0..n-1} A169675(i).
# Method a: de Bruijn sequence built by the standard Lyndon-word (FKM) algorithm, repeated; A140427 by its recurrence.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
def debruijn(k, n):
    a = [0] * k * n; seq = []
    def db(t, p):
        if t > n:
            if n % p == 0: seq.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]; db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j; db(t + 1, t)
    db(1, 1); return seq
per = debruijn(2, 3)
D = [per[i % 8] for i in range(N + 1)]
check_terms("A169675", lambda n: D[n], " (FKM de Bruijn)")
A = []
for n in range(N + 1):
    A.append(0 if n < 4 else ((n - 4) ** 2 // 4 + 1 if n < 8 else A[n - 8] + 4))
check_terms("A140427", lambda n: A[n])
s = 0; bad = []
for n in range(N + 1):
    if A[n] != s: bad.append(n)
    s += D[n]
print("N =", N, "mismatches:", bad[:10], "(both sides satisfy f(n+8)=f(n)+4, so agreement on n<16 already proves it)")
