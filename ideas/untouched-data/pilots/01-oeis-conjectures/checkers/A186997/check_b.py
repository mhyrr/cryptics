# A186997 checker b: coefficients from Mathar's D-finite recurrence (entry %F line)
#   n(n+1)(2n+1)a(n) - n(28n^2-27n+8)a(n-1) + 6(11n^3-36n^2+32n-5)a(n-2) + 8(2n-5)(14n^2-52n+51)a(n-3)
#   + 32(2n-5)(2n-7)(n-3)a(n-4) = 0,
# seeded with a(0..3) obtained by iterating A = 1 + x A^3 + x^2 A^4 on truncated series; the first 60 terms are
# also checked against that functional equation. 2-adic valuations via gmpy2; v2(Catalan(n)) = s2(n+1)-1 (Kummer).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2
from k2common import check_terms
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
L = 2 * NN + 2
M = 60
def mul(p, q): return [sum(p[i] * q[n - i] for i in range(n + 1)) for n in range(M)]
A = [1] + [0] * (M - 1)
for _ in range(M):
    A3 = mul(mul(A, A), A); A4 = mul(A3, A)
    A = [(n == 0) + (A3[n - 1] if n else 0) + (A4[n - 2] if n > 1 else 0) for n in range(M)]
a = A[:4]
for n in range(4, L):
    s = (n * (28 * n * n - 27 * n + 8) * a[n - 1] - 6 * (11 * n ** 3 - 36 * n * n + 32 * n - 5) * a[n - 2]
         - 8 * (2 * n - 5) * (14 * n * n - 52 * n + 51) * a[n - 3] - 32 * (2 * n - 5) * (2 * n - 7) * (n - 3) * a[n - 4])
    d = n * (n + 1) * (2 * n + 1); assert s % d == 0; a.append(s // d)
assert a[:M] == A, "recurrence disagrees with functional equation"
check_terms("A186997", lambda n: a[n])
v2 = lambda m: int(gmpy2.bit_scan1(m))
vcat = lambda n: bin(n + 1).count("1") - 1
b1 = [n for n in range(0, NN + 1) if v2(a[2 * n + 1]) != vcat(2 * n + 1)]
b2 = [n for n in range(2, NN + 1) if v2(a[2 * n]) != 3 + vcat(n - 2)]
print("n <=", NN, "conj 1 failures:", b1[:10], "conj 2 failures:", b2[:10])
