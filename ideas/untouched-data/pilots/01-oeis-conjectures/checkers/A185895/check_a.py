# A185895: e.g.f. Prod_{k>=1} (1 - x^k/k!). Conjecture (Bala) 1): sign(a(n)) != sign(a(n-1)) iff n is triangular
# (checked to n=1225). Parts 2), 3) not tested. Method a: c_n = n![x^n] of the partial product, multiplying in
# one factor (1 - x^k/k!) at a time: c_n <- c_n - C(n,k) c_{n-k} (integers), gmpy2.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2, hashlib
sys.set_int_max_str_digits(0)
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5050
c = [gmpy2.mpz(0)] * (N + 1); c[0] = gmpy2.mpz(1)
for k in range(1, N + 1):
    for n in range(N, k - 1, -1):
        if c[n - k]: c[n] -= gmpy2.comb(n, k) * c[n - k]
check_terms("A185895", lambda n: int(c[n]))
tri = {m * (m + 1) // 2 for m in range(0, 200)}
zeros = [n for n in range(N + 1) if c[n] == 0]
bad = [n for n in range(1, N + 1) if ((c[n] > 0) != (c[n - 1] > 0)) != (n in tri)]
print("N =", N, "zeros:", zeros[:5], "violations:", bad[:10], "| md5:", hashlib.md5(str([int(x) for x in c]).encode()).hexdigest())
