# A339669: a(n) = number of Fibonacci numbers dividing Lucas(n)^2+1 (distinct values; 1 counted once).
# Conj 1: a(6n+3)=1; Conj 2: a(6n+1)=a(6n+5)=2; verified for n<156 (index < 156).
# Method a: Lucas via L(n)=L(n-1)+L(n-2); test every distinct Fibonacci number <= L^2+1 for divisibility.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k4"))
from oeisterms import terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1560
L = [2, 1]
while len(L) <= N: L.append(L[-1] + L[-2])
F = [1, 2]
while F[-1] <= L[N] ** 2 + 1: F.append(F[-1] + F[-2])
def a(n):
    v = L[n] ** 2 + 1
    return sum(1 for f in F if f <= v and v % f == 0)
T, off = terms("A339669")
assert [a(n) for n in range(off, off + len(T))] == T; print("terms OK", len(T))
bad = []
for n in range(N):
    r = n % 6; v = None
    if r == 3 and a(n) != 1: bad.append(n)
    if r in (1, 5) and a(n) != 2: bad.append(n)
print("tested indices 0..", N - 1)
print("RESULT", "holds for index<%d" % N if not bad else "COUNTEREXAMPLE n=%s" % bad[:10])
