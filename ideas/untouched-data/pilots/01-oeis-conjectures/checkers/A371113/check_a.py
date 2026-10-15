# A371113: triples (a(3k),a(3k+1),a(3k+2)); a(3k), a(3k+1) = least unused; a(3k+2) = least unused m such that
# digits of a(3k).a(3k+1).m form a palindrome. Conjecture 3: a(3k+1)-a(3k) in {1,2} for all k (verified to k=3333).
# Method a: own implementation; candidate m enumerated by length: for L<=|D| m=rev(D[:L]) if D[L:] palindromic,
# for L>|D| m = t + rev(D) with t a palindrome of length L-|D|; no leading zero.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
from itertools import product
K = int(sys.argv[1]) if len(sys.argv) > 1 else 33330
def pals(L):
    if L == 0: yield ""; return
    h = (L + 1) // 2
    for first in "123456789":
        for rest in product("0123456789", repeat=h - 1):
            left = first + "".join(rest)
            yield left + (left[::-1] if L % 2 == 0 else left[:-1][::-1])
used = set(); seq = []; least = 0
def take_least():
    global least
    while least in used: least += 1
    used.add(least); return least
def pal_m(D):
    for L in range(1, 10 ** 6):
        if L <= len(D):
            rest = D[L:]
            if rest == rest[::-1]:
                s = D[:L][::-1]
                if s[0] != "0" and int(s) not in used: return int(s)
        else:
            rD = D[::-1]
            for t in pals(L - len(D)):
                s = t + rD
                if s[0] != "0" and int(s) not in used: return int(s)
for k in range(K + 1):
    x = take_least(); y = take_least(); m = pal_m(str(x) + str(y)); used.add(m); seq += [x, y, m]
T, off = terms("A371113")
assert seq[:len(T)] == T; print("terms OK", len(T))
bad = [k for k in range(K + 1) if seq[3*k+1] - seq[3*k] not in (1, 2)]
print("tested k = 0..", K, " #k with diff 2:", sum(seq[3*k+1]-seq[3*k] == 2 for k in range(K+1)))
print("RESULT", "holds for k<=%d" % K if not bad else "COUNTEREXAMPLE k=%s" % bad[:5])
