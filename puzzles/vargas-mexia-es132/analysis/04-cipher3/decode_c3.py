"""Cipher 3 (Devos Cp.30, per Tomokiyo) decoder. Frozen 2026-10-04 before reader A of f. 105 was read.
    python3 decode_c3.py <transcription> > out.txt
Rules (from ../../sources/keys/cipher3.tsv and keys/README.md):
- 1..29 letters (table); 9,3,14,19,26 second numbers for a,e,i,o,u; 30..37 clusters.
- Vowel marks after: '+' a, '.' e, 'p' (hook) o, 's'/'<sign:Sigma>' (curl) i [flagged], 'u'-suffix none.
- Marks above add a consonant: '<v>' r, '<hat>' n, '<bar>' s, '/' l (above), '\\' m.
- Numbers > 37 are codes: output ⟨#n⟩ and flagged (no values assigned).
- Digit runs > 37 that are not plausible codes are NOT split; they stay codes (frozen choice).
"""
import re, sys
L = {10: "a", 8: "b", 7: "c", 6: "d", 4: "e", 2: "f", 11: "g", 12: "h", 13: "i", 15: "l", 16: "m",
     17: "n", 18: "o", 20: "p", 21: "q", 22: "r", 23: "s", 24: "t", 25: "u", 27: "x", 28: "y", 29: "z",
     9: "a", 3: "e", 14: "i", 19: "o", 26: "u", 1: "?1", 5: "?5"}
CL = {30: "br", 31: "cr", 32: "dr", 33: "fr", 34: "gr", 35: "pl", 36: "tr", 37: "vr"}
V = {"+": "a", ".": "e", "p": "o", "s": "i"}
ABOVE = {"<v>": "r", "<hat>": "n", "<bar>": "s"}

def tok(t, flags, where):
    t0 = t
    t = t.rstrip("?")
    m = re.match(r"^(\d+)(.*)$", t)
    if not m:
        if t in ("/",):
            return "/"
        flags.append(f"{where} non-numeric '{t0}'")
        return f"⟨{t0}⟩"
    n, rest = int(m.group(1)), m.group(2)
    if n > 37:
        flags.append(f"{where} code {n}")
        base = f"⟨#{n}⟩"
    else:
        base = CL.get(n) or L.get(n, f"⟨{n}⟩")
    vow = ""; cons = ""
    for mk in re.findall(r"<[^>]+>|[+.ps!]", rest):
        if mk in V and not vow:
            vow = V[mk]
            if mk == "s": flags.append(f"{where} 's' read as -i curl in '{t0}'")
        elif mk in ABOVE:
            cons += ABOVE[mk]
        elif mk == "<crossabove>":
            flags.append(f"{where} cross above (code marker?) on '{t0}'")
            base = f"⟨{t0}⟩"
        else:
            flags.append(f"{where} unhandled mark '{mk}' in '{t0}'")
    return base + vow + cons

def main(path):
    flags = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip(): continue
        if line.startswith("#"): print(line); continue
        out = []
        for k, chunk in enumerate(re.split(r"(\[\[.*?\]\])", line)):
            if chunk.startswith("[["): out.append(chunk); continue
            for i, t in enumerate(chunk.split(), 1):
                out.append(tok(t, flags, f"{lno}:{i}"))
        print(f"{lno:3d}  {' '.join(out)}")
    print("\n## FLAGS"); print("\n".join(flags))

if __name__ == "__main__":
    main(sys.argv[1])
