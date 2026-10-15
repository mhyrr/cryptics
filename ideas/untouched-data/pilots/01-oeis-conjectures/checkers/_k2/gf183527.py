"""Parse the conjectured g.f. of A183527 from its %F line and expand it to N terms (offset 1)."""
import os, re
from k2common import OEIS
def gf_terms(N):
    line = [l for l in open(os.path.join(OEIS, "seq/A183/A183527.seq")) if l.startswith("%F A183527 Conjectured")][0]
    expr = line.split("G.f.: ", 1)[1].split("(This has been")[0].strip()
    num_s, den_s = re.match(r"\((.*)\)\s*/\s*\((.*)\)\.?$", expr).groups()
    def poly(s):
        s = s.replace(" ", "")
        c = {}
        for sign, coef, pw in re.findall(r"([+-]?)(\d*)\*?x(?:\^(\d+))?", s):
            e = int(pw) if pw else 1; v = int(coef) if coef else 1
            c[e] = c.get(e, 0) + (-v if sign == "-" else v)
        # constant terms
        for sign, k in re.findall(r"(?:^|(?<=[+-]))([+-]?)(\d+)(?=[+-]|$)", s.replace("x^", "X")):
            pass
        rest = re.sub(r"[+-]?\d*\*?x(\^\d+)?", "", s)
        if rest: c[0] = c.get(0, 0) + int(rest)
        return c
    num, den = poly(num_s), poly(den_s)
    d0 = den[0]
    out = []
    for n in range(N + 1):
        v = num.get(n, 0) - sum(den[j] * out[n - j] for j in den if 0 < j <= n)
        assert v % d0 == 0; out.append(v // d0)
    return out[1:]   # a(1..N)
