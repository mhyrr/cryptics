# A397315: T(n,k) = max #grid points of an n X k grid that can be blacked out so that every lattice rectangle (tilted ones
# included) is determined by its visible corners. Equivalently the blackout set S may contain no set C(R1) xor C(R2).
# Conjecture: T(3,m) = m+2 for m>=3 (verified 3<=m<=10).
# Method a: CP-SAT (OR-tools): maximize |S| subject to |S cap D| <= |D|-1 for every inclusion-minimal symmetric difference D;
# status must be OPTIMAL. (Hypergraph built in common.py from the definition, same as the entry's program.)
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4")); sys.path.insert(0, os.path.dirname(__file__))
from oeisterms import terms
from common import edges
from ortools.sat.python import cp_model
M = int(sys.argv[1]) if len(sys.argv) > 1 else 20
M0 = int(sys.argv[2]) if len(sys.argv) > 2 else 11
MODE = sys.argv[3] if len(sys.argv) > 3 else 'both'   # 'terms', 'conj' or 'both' (separate runs keep each under the 5-min cap)
def T(n, k):
    N, D = edges(n, k)
    m = cp_model.CpModel(); x = [m.NewBoolVar("x%d" % i) for i in range(N)]
    for d in D: m.Add(sum(x[i] for i in d) <= len(d) - 1)
    m.Maximize(sum(x)); s = cp_model.CpSolver(); s.parameters.num_workers = 1; s.parameters.max_time_in_seconds = 240
    st = s.Solve(m)
    assert st == cp_model.OPTIMAL, (n, k, s.StatusName(st))
    return int(round(s.ObjectiveValue()))
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
