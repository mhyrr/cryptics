# A016777 (3n+1). Erdos-Sarkozy: a set of n positive integers with property P (for x, y, z in the set with z < x, y,
# z does not divide x+y) has an element >= 3n-2 (Greathouse: verified n <= 12; {2n-1..3n-2} attains it).
# x = y is allowed (z does not divide 2x): with x != y only, {2,3} would beat the bound at n = 2, so the
# entry's reading must include x = y.
# Method a: branch and bound, elements chosen in DEcreasing order; a new minimum z is admissible iff no two
# (not necessarily distinct) larger chosen x, y have x+y == 0 (mod z). Computes g(M) = max size of a P subset of [1, M] and
# checks g(3n-3) <= n-1.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 280
T, off = terms("A016777")
assert [3 * n + 1 for n in range(len(T))] == T; print("terms OK", len(T))
def exists(M, k):
    """is there a P subset of [1, M] of size k?"""
    found = [None]
    def rec(z, S, cnt):
        if cnt == k: found[0] = sorted(S); return True
        for x in range(z, 0, -1):
            if cnt + x < k: return False        # not enough numbers left
            ok = True
            for i in range(len(S)):
                a = S[i]
                for j in range(i, len(S)):
                    if (a + S[j]) % x == 0: ok = False; break
                if not ok: break
            if ok:
                S.append(x)
                if rec(x - 1, S, cnt + 1): return True
                S.pop()
        return False
    rec(M, [], 0)
    return found[0]
t0 = time.process_time(); last = None; bad = None
for n in range(2, NMAX + 1):
    if time.process_time() - t0 > DEADLINE: break
    w = exists(3 * n - 3, n)
    if w: bad = (n, w); break
    assert exists(3 * n - 2, n)                 # attained
    last = n; print("n=%d ok (%.0fs)" % (n, time.process_time() - t0), flush=True)
print("RESULT", "holds to %s" % last if bad is None else "COUNTEREXAMPLE n=%d set=%s" % bad)
