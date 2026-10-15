# A087716 method b: PARI translation of Greathouse's lst(), with psp() replaced by an explicit Fermat base-2 test
# (Mod(2,N)^(N-1)==1) plus !ispseudoprime(N), looping i upward until a deadline.
import time; T0 = time.time()
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k1"))
from oeisterms import terms
import cypari2; pari = cypari2.Pari(); pari.allocatemem(10**9)
IMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
DEADLINE = float(sys.argv[2]) if len(sys.argv) > 2 else 270
T, off = terms("A087716")
pari("isf(N)=N>2&&N%2&&Mod(2,N)^(N-1)==1&&!ispseudoprime(N)")
pari("one(i)=my(P=prod(t=1,i,prime(t)),q=prime(i+1),v=List());forprime(r=q,q^2,for(j=1,q-1,if(j*P-r>0&&isf(j*P-r),listput(v,j*P-r));if(isf(j*P+r),listput(v,j*P+r))));Vec(v)")
found = set(); last = 0
for i in range(1, IMAX + 1):
    if time.time() - T0 > DEADLINE: break
    found |= set(int(x) for x in pari("one(%d)" % i)); last = i
    print("i=%d done, found so far %d (%.0fs)" % (i, len(found), time.time() - T0), flush=True)
S = sorted(found)
print("found:", S[:20], "count", len(S))
assert S[:5] == T; print("terms OK", len(T))
print("RESULT", "holds to i=%d" % last if len(S) == 5 else "COUNTEREXAMPLE extra term %s" % S[5:])
