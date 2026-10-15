# A185895 checker b: e.g.f. = exp(G), G = -Sum_{k,j>=1} x^(jk)/(j (k!)^j) (Gutkovskiy). g_m = m![x^m]G
#   = -Sum_{jk=m} m!/(j (k!)^j) is an integer; then a(n) = Sum_{m=1..n} C(n-1,m-1) g_m a(n-m).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2, hashlib
sys.set_int_max_str_digits(0)
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5050
fact = [gmpy2.mpz(1)]
for i in range(1, N + 1): fact.append(fact[-1] * i)
g = [gmpy2.mpz(0)] * (N + 1)
for m in range(1, N + 1):
    s = gmpy2.mpz(0)
    for k in range(1, m + 1):
        if m % k == 0:
            j = m // k
            q, r = gmpy2.f_divmod(fact[m], j * fact[k] ** j); assert r == 0
            s += q
    g[m] = -s
a = [gmpy2.mpz(1)]
for n in range(1, N + 1):
    s = gmpy2.mpz(0); b = gmpy2.mpz(1)          # b = C(n-1, m-1)
    for m in range(1, n + 1):
        s += b * g[m] * a[n - m]
        b = b * (n - m) // m
    a.append(s)
check_terms("A185895", lambda n: int(a[n]))
tri = {m * (m + 1) // 2 for m in range(0, 200)}
zeros = [n for n in range(N + 1) if a[n] == 0]
bad = [n for n in range(1, N + 1) if ((a[n] > 0) != (a[n - 1] > 0)) != (n in tri)]
print("N =", N, "zeros:", zeros[:5], "violations:", bad[:10], "| md5:", hashlib.md5(str([int(x) for x in a]).encode()).hexdigest())
