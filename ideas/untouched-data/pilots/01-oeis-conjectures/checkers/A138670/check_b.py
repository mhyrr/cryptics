# A138670 checker b: zero set from the closed form {k*3^(m+1) + (3^m-1)/2 : k>=0, m>=0} (%F line, corrected m>=0) via a sieve,
# A106036 generated lazily as a fixed point (read position i of the word, emit image of letter i), no list re-expansion.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_k2"))
from k2common import check_terms
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
LIM = 3 * N + 10
mark = bytearray(LIM); m = 0   # NOTE: the %F line says m>=1, but m=0 (multiples of 3) is needed: a(3n)=0 and 0,3,6 are data terms
while 3 ** m // 3 <= LIM:
    st, step = (3 ** m - 1) // 2, 3 ** (m + 1)
    if st < LIM: mark[st::step] = b"\x01" * len(range(st, LIM, step))
    m += 1
Z = [k for k in range(LIM) if mark[k]][:N + 1]
check_terms("A138670", lambda n: Z[n])
img = {1: (1, 2), 2: (1, 2, 3), 3: (1, 2, 3, 3)}
w = [1, 2]; i = 1               # fixed point starts 1,2 (image of 1); expand letter i onward
while len(w) < N + 1:
    w.extend(img[w[i]]); i += 1
check_terms("A106036", lambda n: w[n], " (fixed point)")
bad = []; s = 0
for n in range(N + 1):
    if Z[n] != s: bad.append(n)
    s += w[n]
print("N =", N, "mismatches:", bad[:10])
