# A127750: conjecture a(n) mod 2 = A036987(n) (1 iff n = 2^m - 1). Method a (prefix sums), see _k2/rowsum_inv.py
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import hashlib
from rowsum_inv import method_a as M
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2 ** 20
r = M(2, N)
check_terms("A127750", lambda n: r[n])
bad = [n for n in range(N + 1) if r[n] % 2 != (1 if (n + 1) & n == 0 else 0)]
print("N =", N, "failures:", bad[:10], "| md5 of a(0..N):", hashlib.md5(str(r).encode()).hexdigest())
