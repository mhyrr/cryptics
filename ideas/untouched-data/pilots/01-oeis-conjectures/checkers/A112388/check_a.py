# A112388: a(n) = smallest prime p with p^n pandigital. Conjecture: a(n)=2 for all n>168, i.e. 2^n pandigital for n>168
# (and 2^168 is not, else a(168)=2 too). Method a: gmpy2 decimal conversion of each 2^n.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import gmpy2
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
def a(n):
    if n == 1: return 10123457689   # p^1 pandigital prime: hardcoded as in the entry's own programs
    p = gmpy2.mpz(2)
    while len(set(gmpy2.digits(p ** n))) < 10: p = gmpy2.next_prime(p)
    return int(p)
check_terms("A112388", a)
fails = [n for n in range(160, 169) if len(set(gmpy2.digits(gmpy2.mpz(2) ** n))) < 10]
print("non-pandigital 2^n for 160<=n<=168:", fails)
bad = []
x = gmpy2.mpz(2) ** 168
for n in range(169, N + 1):
    x *= 2
    if len(set(gmpy2.digits(x))) < 10: bad.append(n)
print("N =", N, "n>168 with 2^n not pandigital:", bad[:20])
