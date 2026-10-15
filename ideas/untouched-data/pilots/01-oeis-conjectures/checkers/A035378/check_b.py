# A035378 method b: Horner-nested evaluation S = 1 + f_1(1 + f_2(1 + ... (1 + f_K))) with f_j = 1-(x-1)^j,
# where (x-1)^j comes from a Pascal-triangle table; exact (object arrays) for the listed terms, modulo 25 with
# FFT convolution (products < 2^53, rounded) for the range.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from math import comb
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 499
T, off = terms("A035378")
import numpy as np
def fftmul(u, v, D, mod):
    L = 1 << (2 * D + 2).bit_length()
    r = np.rint(np.fft.irfft(np.fft.rfft(u.astype(float), L) * np.fft.rfft(v.astype(float), L), L)[: D + 1])
    return r.astype(np.int64) % mod
def series(D, mod):
    K = 2 * D + 1
    # Pascal table rows C(j, i) for i <= D (mod 'mod' or exact)
    rows = [None] * (K + 1)
    row = np.zeros(D + 1, dtype=object if mod is None else np.int64); row[0] = 1; rows[0] = row
    for j in range(1, K + 1):
        nr = row.copy(); nr[1:] = row[1:] + row[:-1]
        if mod is not None: nr %= mod
        rows[j] = row = nr
    sign = np.array([(-1) ** i for i in range(D + 1)], dtype=object if mod is None else np.int64)
    R = np.zeros(D + 1, dtype=object if mod is None else np.int64); R[0] = 1
    for j in range(K, 0, -1):
        # f = 1 - (x-1)^j = 1 - sum C(j,i) x^i (-1)^(j-i)
        f = -rows[j] * sign * (-1) ** j
        f[0] += 1
        if mod is None:
            R = np.convolve(f, R)[: D + 1]; R[0] += 1
        else:
            f %= mod; R = fftmul(f, R, D, mod); R[0] = (R[0] + 1) % mod
    return [int(x) for x in R]
ex = series(len(T) - 1, None)
assert ex == T, (ex, T); print("terms OK", len(T))
D = 5 * NN + 4
a = series(D, 25)
bad = None
for n in range(NN + 1):
    if a[5*n+3] % 5 or a[5*n+4] % 5 or (a[5*n+2] - 2*a[5*n+1]) % 5: bad = n; break
print("RESULT", "holds to n=%d" % NN if bad is None else "COUNTEREXAMPLE n=%d" % bad)
