# A049997 method b: PARI fibonacci() and ispower() on every product F(m)F(n), 2 < m < n <= N.
# Terms from a translation of Greathouse's PARI list().
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(10**9)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
T, off = terms("A049997")
pari("list(lim)=my(phi=(1+sqrt(5))/2, v=vector(log(lim*sqrt(5))\\log(phi), i, fibonacci(i+1)), u=List([0]),t); for(i=1,#v,for(j=i,#v,t=v[i]*v[j];if(t>lim,break,listput(u,t)))); vecsort(Vec(u),,8)")
assert [int(x) for x in pari("list(%d)" % T[-1])] == T; print("terms OK", len(T))
F = [pari.fibonacci(i) for i in range(N + 1)]
isp = pari.ispower
hits = []; last = 3
for n in range(4, N + 1):
    if time.time() - T0 > 270: N = last; print("deadline hit"); break
    last = n
    Fn = F[n]
    for m in range(3, n):
        if isp(F[m] * Fn): hits.append((m, n))
print("perfect powers:", hits)
bad = [h for h in hits if h != (3, 6)]
print("RESULT", "holds to %d" % N if not bad else "COUNTEREXAMPLE (m,n)=%s" % (bad[0],))
