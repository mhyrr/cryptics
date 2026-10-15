# A079044: k with Sum_{j=0..k} sin(j/Pi) < 0. Conjecture: a(n) = floor(2*Pi^2*n).
# Method a: running float sum (math.fsum-style compensated) of sin(j/pi); any |S| < 1e-6 re-done in mpmath at 60 digits.
import sys, os, math; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import mpmath; mpmath.mp.dps = 60
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
T, off = terms("A079044")
K = int(2 * math.pi ** 2 * (N + 2)) + 10
s = 0.0; c = 0.0; seq = []; close = 0
for j in range(0, K + 1):
    y = math.sin(j / math.pi) - c; t = s + y; c = (t - s) - y; s = t
    neg = s < 0
    if abs(s) < 1e-6:
        close += 1; neg = mpmath.fsum(mpmath.sin(i / mpmath.pi) for i in range(j + 1)) < 0
    if neg: seq.append(j)
assert seq[:len(T)] == T; print("terms OK", len(T), "near-zero rechecks", close)
pi2 = 2 * mpmath.pi ** 2
bad = next((n for n in range(1, N + 1) if seq[n - 1] != int(mpmath.floor(pi2 * n))), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
