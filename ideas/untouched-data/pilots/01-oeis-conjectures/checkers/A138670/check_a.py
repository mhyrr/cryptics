# A138670 = indices of 0's in Stewart's choral sequence A116178 (a(3n)=0, a(3n-1)=1, a(3n+1)=a(n), offset 0).
# Conjecture (Irvine): essentially partial sums of A106036 (trajectory of 1 under 1->12, 2->123, 3->1233),
# precisely A138670(n) = Sum_{i=0..n-1} A106036(i). Method a: choral sequence by its recursive definition,
# A106036 by iterating the morphism on a list.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
LIM = 3 * N + 10
ch = [0] * LIM
for k in range(1, LIM):
    if k % 3 == 0: ch[k] = 0
    elif k % 3 == 2: ch[k] = 1
    else: ch[k] = ch[(k - 1) // 3]
Z = [k for k in range(LIM) if ch[k] == 0][:N + 1]
assert len(Z) == N + 1
check_terms("A138670", lambda n: Z[n])
w = [1]
while len(w) < N + 1:
    w = [x for c in w for x in {1: (1, 2), 2: (1, 2, 3), 3: (1, 2, 3, 3)}[c]]
check_terms("A106036", lambda n: w[n], " (morphism)")
s = 0; bad = []
for n in range(N + 1):
    if Z[n] != s: bad.append(n)
    s += w[n]
print("N =", N, "mismatches A138670(n) vs Sum_{i<n} A106036(i):", bad[:10])
