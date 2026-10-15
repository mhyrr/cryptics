# A127752: conjecture a(n) mod 2 = A035263(n+1) (1 iff 2-adic valuation of n+1 is even). Method a (prefix sums).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import hashlib
from rowsum_inv import method_a as M
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2 ** 20
r = M(3, N)
check_terms("A127752", lambda n: r[n])
def v2(m): return (m & -m).bit_length() - 1
bad = [n for n in range(N + 1) if r[n] % 2 != (1 if v2(n + 1) % 2 == 0 else 0)]
print("N =", N, "failures:", bad[:10], "| md5 of a(0..N):", hashlib.md5(str(r).encode()).hexdigest())
