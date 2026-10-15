"""A226890 check_b: a(n) mod 30 via e.g.f. recurrence with numpy Pascal rows and exact g_k (see _k3/egf_b.py)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from egf_b import run, exact_terms
N = int(sys.argv[1])
t, off = terms('A226890'); assert exact_terms('A226890', len(t)) == t
a = run('A226890', 30, N)
assert a[:len(t)] == [x % 30 for x in t]; print('terms ok (mod 30)', len(t))
bad = [n for n, v in enumerate(a) if v != 1 % 30]
print('N', N, 'violations', bad[:10])
