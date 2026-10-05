"""H17 term scan over decoded letters (decode_c3_v2.py output). Finds the H17a terms in the decoded stream (cipher and
clear text joined, spaces removed, unknown tokens as '_') and prints each hit with context and the decoded line number.
A hit is a pointer for the reader of the decode, not a finding: H17a needs the passage read in full by both witnesses.
    python3 h17_scan.py f220_dec.txt [more ...]
Terms (fixed 2026-10-05, from the H17a definition): Pérez / Antonio; Éboli / princesa; Escobedo; secretario; prisión /
preso / arresto; papeles; cartas particulares; cifra; and Idiáquez (H17c context)."""
import re, sys

TERMS = {"perez": r"pe(r|l|\(r\|l\))e[zc]", "antonio": r"anton[i_]o", "eboli": r"e?bol[i_]", "princesa": r"prin[cs]esa",
         "escobedo": r"es[ck]o[bv]e[dt]o", "secretario": r"se[ck]reta", "prision": r"pri[sx][i_]on", "preso": r"(?<!m)pres[oa](?![nt])",
         "arresto": r"arrest", "papeles": r"pape[l_]es", "particular": r"particular", "cifra": r"[cz]if(r|\(r\|l\))a",
         "idiaquez": r"[iy]d[iy]a[qk]"}


def stream(path):
    out = []  # (char, line)
    for line in open(path, encoding="utf-8"):
        if line.startswith("## FLAGS"):
            break
        m = re.match(r"^\s*(\d+)\s\s(.*)$", line.rstrip("\n"))
        if not m:
            continue
        ln, txt = int(m.group(1)), m.group(2)
        txt = re.sub(r"⟨[^⟩]*⟩", "_", txt).replace("[[", "").replace("]]", "").lower()
        for ch in re.sub(r"[\s/,.]", "", txt):
            out.append((ch, ln))
    return out


for path in sys.argv[1:]:
    s = stream(path)
    text = "".join(c for c, _ in s)
    print(f"== {path}: {len(text)} chars")
    for name, rx in TERMS.items():
        for m in re.finditer(rx, text):
            a, b = max(0, m.start() - 30), min(len(text), m.end() + 30)
            print(f"  {name:10s} line {s[m.start()][1]:3d}  …{text[a:b]}…")
