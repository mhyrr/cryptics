"""A226838 check_a: a(n) mod 6 via e.g.f. recurrence with Lucas binomials and valuation-based g_k (see _k3/egf_a.py).
Conjecture: a(n) == 1 (mod 6) for all n >= 0."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from egf_a import run, exact_terms
N = int(sys.argv[1])
t, off = terms('A226838'); assert exact_terms('A226838', len(t)) == t; print('terms ok', len(t))
a = run('A226838', 6, N)
assert a[:len(t)] == [x % 6 for x in t]
bad = [n for n, v in enumerate(a) if v != 1 % 6]
print('N', N, 'violations', bad[:10])
