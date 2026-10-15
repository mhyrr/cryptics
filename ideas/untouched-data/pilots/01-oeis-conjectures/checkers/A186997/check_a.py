# A186997: G.f. A = 1 + x A^3 + x^2 A^4. Conjectures (Bala, both tested): for n>=0 v2(a(2n+1)) = v2(Catalan(2n+1));
# for n>=2 v2(a(2n)) = 3 + v2(Catalan(n-2)). (Checked to n=100.)  Method a: Kruchinin's sum
# a(n) = Sum_{k} C(k,n-k) C(n+2k,n+k)/(n+k+1), cross-checked against the functional equation for small n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from math import comb
from k2common import check_terms
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 1000     # n range of the conjecture; indices up to 2NN+1
def a(n):
    if n == 0: return 1
    s = 0
    for k in range((n + 1) // 2, n + 1):
        t = comb(k, n - k) * comb(n + 2 * k, n + k); assert t % (n + k + 1) == 0; s += t // (n + k + 1)
    return s
check_terms("A186997", a)
# functional equation check, first 60 coefficients
M = 60; A = [a(i) for i in range(M)]
def mul(p, q): return [sum(p[i] * q[n - i] for i in range(n + 1)) for n in range(M)]
A2 = mul(A, A); A3 = mul(A2, A); A4 = mul(A3, A)
assert all(A[n] == (n == 0) + (A3[n - 1] if n >= 1 else 0) + (A4[n - 2] if n >= 2 else 0) for n in range(M))
v2 = lambda m: (m & -m).bit_length() - 1
cat = lambda n: comb(2 * n, n) // (n + 1)
vals = [a(i) for i in range(2 * NN + 2)]
b1 = [n for n in range(0, NN + 1) if v2(vals[2 * n + 1]) != v2(cat(2 * n + 1))]
b2 = [n for n in range(2, NN + 1) if v2(vals[2 * n]) != 3 + v2(cat(n - 2))]
print("n <=", NN, "conj 1 failures:", b1[:10], "conj 2 failures:", b2[:10])
