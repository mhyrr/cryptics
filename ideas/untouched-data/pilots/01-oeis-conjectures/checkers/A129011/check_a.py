# A129011: a(n)=floor(n^(4/3)). Churchhouse: every positive integer N is a(i)+a(j). Method a: values by exact integer
# cube root (Python int, Newton), sumset via numpy FFT convolution of the indicator vector.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
import numpy as np
from k2common import check_terms
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 7
def icbrt(m):
    x = int(round(m ** (1 / 3))) if m < 2 ** 1000 else 1 << (m.bit_length() // 3 + 1)
    while x ** 3 > m: x -= 1
    while (x + 1) ** 3 <= m: x += 1
    return x
f = lambda n: icbrt(n ** 4)
check_terms("A129011", f)
vals = []; n = 0
while True:
    v = f(n)
    if v > X: break
    vals.append(v); n += 1
ind = np.zeros(X + 1); ind[vals] = 1.0
L = 1 << (2 * X + 1).bit_length()
F = np.fft.rfft(ind, L)
cnt = np.rint(np.fft.irfft(F * F, L)[:X + 1])
missing = np.nonzero(cnt[1:] < 0.5)[0] + 1
print("X =", X, "#elements", len(vals), "positive N <= X not representable:", missing[:20].tolist())
