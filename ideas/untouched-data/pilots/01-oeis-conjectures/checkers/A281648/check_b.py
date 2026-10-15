"""A281648 check_b: PARI (cypari2) bernvec, i.e. the entry's own PARI numerator(bernfrac(2n))%n via a different
Bernoulli routine; sanity-cross-checked on a sample with bernfrac and with the entry's Ruby (Akiyama-Tanigawa) algorithm."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import cypari2
from fractions import Fraction
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10240
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
pari('w = bernvec(%d)' % N)
a = {n: int(pari('numerator(w[%d+1]) %% %d' % (n, n))) for n in range(1, N + 1)}
for n in list(range(1, 60)) + [N // 3, N // 2, N]:
    assert a[n] == int(pari('numerator(bernfrac(%d))%%%d' % (2 * n, n)))
def akiyama(m):  # B_0..B_m (B_1=+1/2 convention irrelevant for even index)
    A = []; out = []
    for i in range(m + 1):
        A.append(Fraction(1, i + 1))
        for j in range(i, 0, -1): A[j - 1] = j * (A[j - 1] - A[j])
        out.append(A[0])
    return out
B = akiyama(240)
assert all(B[2 * n].numerator % n == a[n] for n in range(1, 121))
t, off = terms('A281648'); assert [a[n] for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
S = sorted(n for n in a if a[n] == n - 1)
pred = sorted({6, 10} | {2**k for k in range(0, 40) if 2**k <= N})
print('N', N, 'set == predicted:', S == pred, 'extra:', sorted(set(S) - set(pred)), 'missing:', sorted(set(pred) - set(S)))
