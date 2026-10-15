# A395102, method b: M. S. Branicky's case-based generator from the entry, instrumented to report k in case 3.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from itertools import count
from sympy import isprime, nextprime, sieve
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
an, nextp, seen = 3, 5, set(); out = [3]; ks = []
while len(out) < N:
    seen.add(an)
    while nextp in seen: nextp = nextprime(nextp)
    if nextp < an: an = nextp
    elif an + 2 not in seen and isprime(an + 2): an += 2
    else:
        done = False
        for k in count(1):
            for p in sieve.primerange(3, an):
                m = 2 * k * an + p
                if m not in seen and isprime(m):
                    ks.append((len(out) + 1, k)); an = m; done = True; break
            if done: break
    out.append(an)
T, off = terms("A395102")
assert out[:len(T)] == T; print("terms OK", len(T))
bad = [(n, k) for n, k in ks if k != 1]
print("n<=%d: case-3 steps" % N, len(ks), "max a =", max(out))
print("RESULT", "holds for n<=%d" % N if not bad else "COUNTEREXAMPLE n=%s k=%s" % bad[0])
