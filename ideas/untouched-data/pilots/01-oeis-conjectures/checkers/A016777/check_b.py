# A016777 method b: same statement (x = y allowed), different search: elements chosen in INcreasing order.
# Adding a new maximum x to S is admissible iff for every y in S u {x} and every z in S with z < y,
# z does not divide x + y. Exhaustive DFS for an n-subset of [1, 3n-3]; also confirms {2n-1..3n-2} has P.
import sys, os, time; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 280
T, off = terms("A016777")
assert T == list(range(1, 3 * len(T) + 1, 3)); print("terms OK", len(T))
def hasP(S):
    S = sorted(S)
    return all((x + y) % z for i, z in enumerate(S) for j, x in enumerate(S) if j > i for y in S[j:])
def exists(M, k):
    S = []
    def rec(lo):
        if len(S) == k: return True
        for x in range(lo, M + 1):
            if len(S) + (M - x + 1) < k: return False
            ok = True
            for y in S + [x]:
                for z in S:
                    if z >= y: break
                    if (x + y) % z == 0: ok = False; break
                if not ok: break
            if ok:
                S.append(x)
                if rec(x + 1): return True
                S.pop()
        return False
    return sorted(S) if rec(1) else None
t0 = time.process_time(); last = None; bad = None
for n in range(2, NMAX + 1):
    if time.process_time() - t0 > DEADLINE: break
    assert hasP(range(2 * n - 1, 3 * n - 1))
    w = exists(3 * n - 3, n)
    if w: bad = (n, w); break
    last = n; print("n=%d ok (%.0fs)" % (n, time.process_time() - t0), flush=True)
print("RESULT", "holds to %s" % last if bad is None else "COUNTEREXAMPLE n=%d set=%s" % bad)
