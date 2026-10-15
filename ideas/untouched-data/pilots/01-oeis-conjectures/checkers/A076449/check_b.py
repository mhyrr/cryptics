# A076449 method b: primes from PARI (primes up to 10^D in chunks), f(S) per exact digit multiset; c(M) as an
# explicit sum of f over all sub-multisets of M (product of ranges), no zeta transform; least number per count.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
from itertools import product, combinations_with_replacement
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
D = int(sys.argv[1]) if len(sys.argv) > 1 else 8
T, off = terms("A076449")
f = {}
step = 10 ** 6
for lo in range(0, 10 ** D, step):
    for p in pari("primes([%d,%d])" % (lo, lo + step - 1)):
        s = str(int(p)); key = tuple(s.count(c) for c in "0123456789")
        f[key] = f.get(key, 0) + 1
best = {0: 1}
for k in range(1, D + 1):
    for comb in combinations_with_replacement(range(10), k):
        if comb[-1] == 0: continue
        M = [comb.count(d) for d in range(10)]
        c = sum(f.get(S, 0) for S in product(*[range(m + 1) for m in M]))
        d0 = next(d for d in range(1, 10) if M[d]); rest = M[:]; rest[d0] -= 1
        x = int(str(d0) + "".join(str(d) * rest[d] for d in range(10)))
        if c not in best or x < best[c]: best[c] = x
calc = [best.get(n) for n in range(0, len(T))]
assert calc == T, [(n, calc[n], T[n]) for n in range(len(T)) if calc[n] != T[n]][:5]; print("terms OK", len(T))
Nmax = 0
while Nmax + 1 in best: Nmax += 1
print("max count with <= %d digits: %d; first missing n: %d" % (D, max(best), Nmax + 1))
print("RESULT", "holds to %d (exists with <= %d digits for all n <= %d)" % (Nmax, D, Nmax))
