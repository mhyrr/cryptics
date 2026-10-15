# A371113, method b: M. F. Hasler's Python program from the entry (membership via a set for speed; logic unchanged).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
K = int(sys.argv[1]) if len(sys.argv) > 1 else 33330
T = []; S = set(); least_unused = 0
while len(T) < 3 * (K + 1):
    if len(T) % 3 < 2:
        x = least_unused; T.append(x); S.add(x)
        while x + 1 in S: x += 1
        least_unused = x + 1
    else:
        suffix = (str(T[-2]) + str(T[-1]))[::-1]
        for i in range(1, len(suffix) + 1):
            if suffix[-i] != '0' and (s := suffix[:-i-1:-1] + suffix) == s[::-1] and (x := int(suffix[-i:])) not in S: break
        else:
            x = int('1' + suffix); assert x not in S
        T.append(x); S.add(x); assert x > least_unused
TT, off = terms("A371113")
assert T[:len(TT)] == TT; print("terms OK", len(TT))
bad = [k for k in range(K + 1) if T[3*k+1] - T[3*k] not in (1, 2)]
print("tested k = 0..", K, " #k with diff 2:", sum(T[3*k+1]-T[3*k] == 2 for k in range(K+1)))
print("RESULT", "holds for k<=%d" % K if not bad else "COUNTEREXAMPLE k=%s" % bad[:5])
