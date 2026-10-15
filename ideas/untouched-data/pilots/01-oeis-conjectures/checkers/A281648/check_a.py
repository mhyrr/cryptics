"""A281648 check_a: a(n) = numerator(B_{2n}) mod n via FLINT (python-flint, cached Bernoulli numbers).
Conjecture: a(n) == n-1 iff n in {6, 10} or n = 2^k."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
import flint
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10240
flint.fmpq.bernoulli(2 * N, cache=True)
a = {n: int(flint.fmpq.bernoulli(2 * n).p % n) for n in range(1, N + 1)}
t, off = terms('A281648'); assert [a[n] for n in range(1, len(t) + 1)] == t; print('terms ok', len(t))
S = sorted(n for n in a if a[n] == n - 1)
pred = sorted({6, 10} | {2**k for k in range(0, 40) if 2**k <= N})
print('N', N, 'set == predicted:', S == pred, 'extra:', sorted(set(S) - set(pred)), 'missing:', sorted(set(pred) - set(S)))
