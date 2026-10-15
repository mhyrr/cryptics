# A182132: conjecture "C(n) = product of [(30,-7),(90,-23),(300,-79)] (linear forms a*n+b) is a Carmichael number if all factors are prime".
# Method b, see _k2/carm_form.py. Default range n <= 1300 (10x the stated bound), override with argv[1].
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from carm_form import run
from k2common import terms, check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1300
run("A182132", [(30,-7),(90,-23),(300,-79)], 1, "b", N, terms, check_terms)
