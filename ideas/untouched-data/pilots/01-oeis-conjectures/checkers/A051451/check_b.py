# A051451 method b: PARI. a(n) via Winkler's PARI loop (lcm stepping until it changes); witness search over twin
# primes p (forprime) with ispseudoprime on a(n)+p, a(n)+p+2, n = 3.. until a deadline.
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(10**9)
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A051451")
pari("seqA(lim)=my(v=List([1]),i=1,j=1,a);while(#v<lim,until(a!=j,a=lcm(j,i+1);i++);j=a;listput(v,a));Vec(v)")
A = [None] + [int(x) for x in pari("seqA(%d)" % min(NMAX, 3000))]
assert A[1:len(T) + 1] == T; print("terms OK", len(T))
pari("w(A)=forprime(p=3,A,if(isprime(p+2)&&ispseudoprime(A+p)&&ispseudoprime(A+p+2),return(p)));0")
last = 2; bad = None; ws = {}
for n in range(3, len(A)):
    if time.time() - T0 > DEADLINE: break
    p = int(pari("w(%d)" % A[n]))
    if p == 0: bad = n; break
    ws[n] = p; last = n
print("witness p for n=6:", ws.get(6), " last few:", [(n, ws[n]) for n in list(ws)[-3:]])
print("RESULT", "holds to %d" % last if bad is None else "COUNTEREXAMPLE n=%d" % bad)
