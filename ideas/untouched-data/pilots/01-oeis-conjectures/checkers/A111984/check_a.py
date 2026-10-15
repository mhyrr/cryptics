# A111984: A(x) = (Sum_k (2k+1) 8^k x^(k(k+1)/2))^(1/3). Conjecture a(5n+4) == 0 mod 5. Method a (see _k2/cuberoot_congr.py).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from cuberoot_congr import run
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10004
run("A111984", lambda k: (2 * k + 1) * 8 ** k, +1, "a", N, [(5, 4)])
