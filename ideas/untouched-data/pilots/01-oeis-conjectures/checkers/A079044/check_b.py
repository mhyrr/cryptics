# A079044 method b: closed form Sum_{j=0..k} sin(j x) = sin(k x/2) sin((k+1) x/2) / sin(x/2), x = 1/pi,
# evaluated in mpmath (40 digits) for every k; the sign is that of sin(k/(2pi)) * sin((k+1)/(2pi)).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import mpmath; mpmath.mp.dps = 40
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
T, off = terms("A079044")
K = int(2 * float(mpmath.pi) ** 2 * (N + 2)) + 10
h = 1 / (2 * mpmath.pi)
seq = []; prev = mpmath.sin(0 * h)
for k in range(0, K + 1):
    cur = mpmath.sin((k + 1) * h)
    if prev * cur < 0: seq.append(k)
    prev = cur
assert seq[:len(T)] == T; print("terms OK", len(T))
bad = next((n for n in range(1, N + 1) if seq[n - 1] != int(mpmath.floor(2 * mpmath.pi ** 2 * n))), None)
print("RESULT", "holds to %d" % N if bad is None else "COUNTEREXAMPLE n=%d" % bad)
