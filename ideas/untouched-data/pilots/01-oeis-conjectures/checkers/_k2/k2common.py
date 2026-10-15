"""Shared helper for batch-2 checkers: read %S/%T/%U terms of an OEIS entry."""
import os
OEIS = os.environ.get("OEIS", "/tmp/claude-0/-home-user-cryptics/c65ae72a-6e03-5f50-a653-43bbdec9a35a/scratchpad/oeis_dl/oeisdata")

def terms(anum):
    p = os.path.join(OEIS, "seq", anum[:4], anum + ".seq")
    s = ""
    for line in open(p, encoding="utf-8"):
        if line[:2] in ("%S", "%T", "%U"):
            s += line.split(" ", 2)[2].strip()
    return [int(x) for x in s.split(",") if x]

def offset(anum):
    p = os.path.join(OEIS, "seq", anum[:4], anum + ".seq")
    for line in open(p, encoding="utf-8"):
        if line.startswith("%O"):
            return int(line.split()[2].split(",")[0])

def check_terms(anum, f, label=""):
    """f(n) -> value; compare with all data terms. Raises on mismatch."""
    t = terms(anum); o = offset(anum)
    for i, v in enumerate(t):
        got = f(o + i)
        if got != v:
            raise SystemExit(f"{anum}{label}: term mismatch at n={o+i}: got {got}, OEIS {v}")
    print(f"{anum}{label}: reproduced all {len(t)} data terms (n={o}..{o+len(t)-1})")
    return len(t)
