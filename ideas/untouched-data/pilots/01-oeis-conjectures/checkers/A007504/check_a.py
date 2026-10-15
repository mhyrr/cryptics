# A007504: a(n) = sum of first n primes. Conjecture: every n >= 5340 is a(i)+a(j)+2a(k), i,j,k>0.
# Method a: FFT convolution of indicator vectors: (S + S) then + 2S; report all non-representable n <= N.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import numpy as np
from sympy import primerange
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
T, off = terms("A007504")
s = [0]
for p in primerange(2, 10**7):
    s.append(s[-1] + p)
    if s[-1] > N: break
assert s[:len(T)] == T; print("terms OK", len(T))
S = [x for x in s[1:] if x <= N]
def conv(u, v):
    L = 1 << int(np.ceil(np.log2(len(u) + len(v))))
    r = np.fft.irfft(np.fft.rfft(u, L) * np.fft.rfft(v, L), L)[: N + 1]
    return (r > 0.5)
I = np.zeros(N + 1); I[S] = 1
I2 = np.zeros(N + 1); I2[[2 * x for x in S if 2 * x <= N]] = 1
SS = conv(I, I).astype(float)
R = conv(SS, I2)
miss = [n for n in range(1, N + 1) if not R[n]]
print("largest non-representable:", max(miss), "count", len(miss))
bad = [n for n in miss if n >= 5340]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE n=%d" % bad[0])
