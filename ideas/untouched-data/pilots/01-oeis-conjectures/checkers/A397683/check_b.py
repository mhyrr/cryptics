# A397683, method b: PARI znorder via cypari2 (independent order code), witness search per odd m, full scan for 3^k,7^k.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from math import gcd
import cypari2; pari = cypari2.Pari()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
def f(m, first=False):
    if m == 1: return 1
    c = 0; prev = None
    for x in range(1, m):
        if gcd(x, m) == 1 and gcd(x + 1, m) == 1:
            if pari.znorder(pari.Mod(x, m)) == pari.znorder(pari.Mod(x + 1, m)):
                c += 1
                if first: return 1
    return c
T, off = terms("A397683")
assert [f(2 * n - 1) for n in range(1, 1 + len(T))] == T; print("terms OK", len(T))
pw = set()
for b in (3, 7):
    t = b
    while t <= N: pw.add(t); t *= b
bad = [m for m in range(3, N + 1, 2) if (f(m, m not in pw) == 0) != (m in pw)]
print("tested odd 3<=m<=", N)
print("RESULT", "holds for m<=%d" % N if not bad else "COUNTEREXAMPLE m=%s" % bad[:10])
