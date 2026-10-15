# Third check, main thread: is numerator(B_{2n}) == -1 (mod n) at n = 3330? Two libraries.
import sys, sympy, flint
n = int(sys.argv[1])
b1 = sympy.bernoulli(2*n); r1 = b1.p % n
b2 = flint.fmpq.bernoulli(2*n); r2 = int(b2.p) % n
print("n", n, "sympy", r1, "flint", r2, "n-1", n-1, "den", b1.q, "match", r1 == r2 == n-1)
