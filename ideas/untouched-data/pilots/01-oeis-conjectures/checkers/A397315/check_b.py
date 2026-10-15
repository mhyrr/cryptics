# A397315, method b: complementary formulation solved by a different engine: minimum hitting set
# (every minimal symmetric difference D must contain a visible point) as a 0/1 MILP with scipy/HiGHS; T = nk - min.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4")); sys.path.insert(0, os.path.dirname(__file__))
from oeisterms import terms
from common import edges
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
M = int(sys.argv[1]) if len(sys.argv) > 1 else 20
M0 = int(sys.argv[2]) if len(sys.argv) > 2 else 11
def T(n, k):
    N, D = edges(n, k)
    A = lil_matrix((len(D), N))
    for r, d in enumerate(D):
        for i in d: A[r, i] = 1
    res = milp(c=np.ones(N), constraints=LinearConstraint(A.tocsr(), lb=np.ones(len(D)), ub=np.inf),
               integrality=np.ones(N), bounds=Bounds(0, 1), options={"time_limit": 240, "mip_rel_gap": 0})
    assert res.status == 0, (n, k, res.message)
    return N - int(round(res.fun))
TT, off = terms("A397315")
got = []; d = 4
while len(got) < len(TT):
    for n in range(2, d - 1):
        got.append(T(n, d - n))
    d += 1
assert got[:len(TT)] == TT; print("terms OK", len(TT))
bad = []
for mm in range(M0, M + 1):
    t0 = time.time(); v = T(3, mm); print("T(3,%d) = %d  (%.1fs)" % (mm, v, time.time() - t0), flush=True)
    if v != mm + 2: bad.append(mm)
print("RESULT", "holds for 3<=m<=%d" % M if not bad else "COUNTEREXAMPLE m=%s" % bad)
