# A182088: conjecture "C(n) = product of [(30,-29),(60,-59),(90,-89),(180,-179)] (linear forms a*n+b) is a Carmichael number if all factors are prime".
# Method b, see _k2/carm_form.py. Default range n <= 1500 (10x the stated bound), override with argv[1].
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from carm_form import run
from k2common import terms, check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
run("A182088", [(30,-29),(60,-59),(90,-89),(180,-179)], 2, "b", N, terms, check_terms)
