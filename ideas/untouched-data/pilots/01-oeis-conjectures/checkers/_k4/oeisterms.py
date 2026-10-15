"""Read %S/%T/%U data terms of an OEIS entry from the local oeisdata checkout (batch K=1 helper)."""
import os
OEIS = os.environ.get("OEIS", "/tmp/claude-0/-home-user-cryptics/c65ae72a-6e03-5f50-a653-43bbdec9a35a/scratchpad/oeis_dl/oeisdata")

def terms(anum):
    path = os.path.join(OEIS, "seq", anum[:4], anum + ".seq")
    s = ""
    off = None
    for line in open(path, encoding="utf-8"):
        if line[:2] in ("%S", "%T", "%U"):
            s += line.split(None, 2)[2].strip()
        if line.startswith("%O"):
            off = int(line.split()[2].split(",")[0])
    return [int(x) for x in s.split(",") if x], off
