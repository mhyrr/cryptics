"""A226838 check_b: a(n) mod 6 via e.g.f. recurrence with numpy Pascal rows and exact g_k (see _k3/egf_b.py)."""
import sys; sys.path.insert(0, __file__.rsplit('/', 2)[0] + '/_k3')
from oeisterms import terms
from egf_b import run, exact_terms
N = int(sys.argv[1])
t, off = terms('A226838'); assert exact_terms('A226838', len(t)) == t
a = run('A226838', 6, N)
assert a[:len(t)] == [x % 6 for x in t]; print('terms ok (mod 6)', len(t))
bad = [n for n, v in enumerate(a) if v != 1 % 6]
print('N', N, 'violations', bad[:10])
