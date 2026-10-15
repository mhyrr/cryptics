"""Extract OEIS conjectures that state a finite checked range, and flag the open ones.

Usage: python3 -I extract.py <path-to-oeisdata> > candidates.tsv
Input: a clone of github.com/oeis/oeisdata (seq/Axxx/Axxxxxx.seq files).
A candidate is a %C or %F line that says "conjecture" and gives a checked bound
("verified for n <= N", "true for n < N", "checked up to N", "holds for all p < 10^6").
It is dropped if a LATER line of the same entry (by position) mentions a
counterexample, disproof, "is false", "fails", or "proved"/"proof", or if the
entry is keyword dead. Output columns are documented in the header row.
"""
import re, sys
from pathlib import Path

root = Path(sys.argv[1]) / "seq"
CONJ = re.compile(r"conjectur", re.I)
NUM = r"(\d+(?:\.\d+)?\s*\*\s*10\^\d+|10\^\d+|2\^\d+|\d[\d,]*)"
RANGE = re.compile(
    r"(?:verified|checked|true|holds|tested|confirmed|valid|searched)\b[^.;]{0,60}?"
    r"(?:<=|<|up to|through|below|less than|to|until|≤)\s*(?:n\s*=\s*|k\s*=\s*|p\s*=\s*)?" + NUM,
    re.I)
SETTLED = re.compile(r"counterexample|counter-example|disprove|is false|fails\b|\bfalse\b|\bproved\b|\bproof\b|\bproven\b", re.I)
BFILE = re.compile(r"Table of n, a\(n\) for n = (-?\d+)\.\.(\d+)")

def to_int(s):
    s = s.replace(",", "").replace(" ", "")
    try:
        if "*10^" in s:
            a, b = s.split("*10^"); return int(float(a) * 10 ** int(b))
        if s.startswith("10^"): return 10 ** int(s[3:])
        if s.startswith("2^"): return 2 ** int(s[2:])
        return int(float(s))
    except ValueError:
        return None

print("anum\tkeywords\tbound\tbfile_end\tedge\tprograms\tline")
n_entries = n_conj = 0
for f in sorted(root.glob("A*/A*.seq")):
    lines = f.read_text(errors="replace").splitlines()
    n_entries += 1
    kw = next((l.split(" ", 2)[2] for l in lines if l.startswith("%K")), "")
    if "dead" in kw.split(","):
        continue
    bend = None
    for l in lines:
        m = BFILE.search(l)
        if m: bend = int(m.group(2))
    progs = sorted({m.group(1) for l in lines if l.startswith("%o") for m in [re.match(r"%o A\d+ \((\w+)", l)] if m})
    if any(l.startswith("%p") for l in lines): progs.append("Maple")
    if any(l.startswith("%t") for l in lines): progs.append("Mathematica")
    for i, l in enumerate(lines):
        if not (l.startswith("%C") or l.startswith("%F")) or not CONJ.search(l):
            continue
        n_conj += 1
        m = RANGE.search(l)
        if not m:
            continue
        if SETTLED.search(l) or any(SETTLED.search(x) and CONJ.search(x) for x in lines[i+1:] if x[:2] in ("%C", "%F")):
            continue
        bound = to_int(m.group(1))
        if bound is None or bound < 10:
            continue
        edge = "Y" if bend and bound <= bend * 1.05 and bound >= bend * 0.5 else ""
        text = l.split(" ", 2)[2].replace("\t", " ")
        print(f"{f.stem}\t{kw}\t{bound}\t{bend or ''}\t{edge}\t{','.join(progs)}\t{text}")
print(f"# entries scanned {n_entries}; conjecture lines {n_conj}", file=sys.stderr)
