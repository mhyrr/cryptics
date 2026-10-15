# A397315, method b: core-guided MaxSAT (PySAT RC2, Glucose backend): hard clauses "not every point of D is blacked out"
# for each inclusion-minimal symmetric difference D, soft unit clauses "point blacked out"; optimum = T(n,k).
# (Method a uses CP-SAT; a HiGHS MILP version was too slow to reproduce the data within the cap.)
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4")); sys.path.insert(0, os.path.dirname(__file__))
from oeisterms import terms
from common import edges
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
M = int(sys.argv[1]) if len(sys.argv) > 1 else 20
M0 = int(sys.argv[2]) if len(sys.argv) > 2 else 11
MODE = sys.argv[3] if len(sys.argv) > 3 else 'both'
def T(n, k):
    N, D = edges(n, k); w = WCNF()
    for d in D: w.append([-(i + 1) for i in d])
    for i in range(N): w.append([i + 1], weight=1)
    with RC2(w) as r:
        m = r.compute()
    S = {i for i in range(N) if m[i] > 0}
    assert all(not set(d) <= S for d in D)      # feasibility of the optimum, re-checked
    return len(S)
TT, off = terms("A397315")
if MODE in ('terms', 'both'):
    got = []; d = 4
    while len(got) < len(TT):
        for n in range(2, d - 1):
            got.append(T(n, d - n))
        d += 1
    assert got[:len(TT)] == TT; print("terms OK", len(TT))
if MODE == 'terms': sys.exit(0)
bad = []
for mm in range(M0, M + 1):
    t0 = time.time(); v = T(3, mm); print("T(3,%d) = %d  (%.1fs)" % (mm, v, time.time() - t0), flush=True)
    if v != mm + 2: bad.append(mm)
print("RESULT", "holds for 3<=m<=%d" % M if not bad else "COUNTEREXAMPLE m=%s" % bad)
