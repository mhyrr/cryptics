"""A237593 check_b: translation of Michel Marcus's PARI heights()/isabove() (full column-height vectors, O(n) per n),
rows from the Indranil Ghosh/A237591 formula using floating ceil replaced by exact rational ceil."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import numpy as np, numba as nb
from fractions import Fraction
from math import ceil, isqrt
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000

def T_py(n):
    j = (isqrt(8 * n + 1) - 1) // 2
    s = lambda k: ceil(Fraction(n + 1, k) - Fraction(k + 1, 2)) - ceil(Fraction(n + 1, k + 1) - Fraction(k + 2, 2))
    return [s(k) if k <= j else s(2 * j + 1 - k) for k in range(1, 2 * j + 1)]
t, off = terms('A237593'); flat = []; n = 1
while len(flat) < len(t): flat += T_py(n); n += 1
assert flat[:len(t)] == t; print('terms ok', len(t))

@nb.njit(cache=True)
def run(N):
    ha = np.zeros(N + 2, np.int64); hb = np.zeros(N + 2, np.int64); r = np.zeros(5000, np.int64)
    ha[0] = 1; ha[1] = 0   # heights(row(1)) = [1], then append 0
    bad = 0; first = -1
    for n in range(2, N + 1):
        # 2j(j+1) <= ... j = floor((sqrt(8n+1)-1)/2)
        j = int((np.sqrt(8.0 * n + 1) - 1) / 2)
        while (j + 1) * (j + 2) // 2 <= n: j += 1
        while j * (j + 1) // 2 > n: j -= 1
        for k in range(1, j + 1):
            # ceil(p/q) for rationals: ceil((2n+2-k(k+1))/(2k))
            a1 = 2 * n + 2 - k * (k + 1); b1 = 2 * k
            a2 = 2 * n + 2 - (k + 1) * (k + 2); b2 = 2 * (k + 1)
            r[k - 1] = (-((-a1) // b1)) - (-((-a2) // b2))
        for k in range(j): r[2 * j - 1 - k] = r[k]
        h = n; iv = 0
        for i in range(2 * j):
            if i % 2 == 0:
                for q in range(r[i]): hb[iv] = h; iv += 1
            else:
                h -= r[i]
        for i in range(n):
            if hb[i] < ha[i]:
                bad += 1
                if first < 0: first = n
                break
        for i in range(n): ha[i] = hb[i]
        ha[n] = 0
    return bad, first

print('N', N, 'result (nbad, first crossing n):', run(N))
