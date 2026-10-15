"""A226839 check_a: a(n) mod 3 via e.g.f. recurrence with Lucas binomials and valuation-based g_k (see _k3/egf_a.py).
Conjecture: a(n) == 1 (mod 3) for all n >= 0."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from egf_a import run, exact_terms
N = int(sys.argv[1])
t, off = terms('A226839'); assert exact_terms('A226839', len(t)) == t; print('terms ok', len(t))
a = run('A226839', 3, N)
assert a[:len(t)] == [x % 3 for x in t]
bad = [n for n, v in enumerate(a) if v != 1 % 3]
print('N', N, 'violations', bad[:10])
