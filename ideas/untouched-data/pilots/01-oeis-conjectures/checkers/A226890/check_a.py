"""A226890 check_a: a(n) mod 30 via e.g.f. recurrence with Lucas binomials and valuation-based g_k (see _k3/egf_a.py).
Conjecture: a(n) == 1 (mod 30) for all n >= 0."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from egf_a import run, exact_terms
N = int(sys.argv[1])
t, off = terms('A226890'); assert exact_terms('A226890', len(t)) == t; print('terms ok', len(t))
a = run('A226890', 30, N)
assert a[:len(t)] == [x % 30 for x in t]
bad = [n for n, v in enumerate(a) if v != 1 % 30]
print('N', N, 'violations', bad[:10])
