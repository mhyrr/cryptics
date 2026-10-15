# A193236: A(x) = (Sum_k (-3)^k (2k+1) x^(k(k+1)/2))^(-1/3). Conjectures a(5n+4)==0 mod 5, a(7n+5)==0 mod 7. Method a.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from cuberoot_congr import run
N = int(sys.argv[1]) if len(sys.argv) > 1 else 14005
run("A193236", lambda k: (-3) ** k * (2 * k + 1), -1, "a", N, [(5, 4), (7, 5)])
