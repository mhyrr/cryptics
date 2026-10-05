"""Cipher 1 decoder (16 Dec 1577, es. 132 ff. 3r–4r), from Tomokiyo's table after Devos 1950 p. 418
(sources/keys/cipher1.tsv). Frozen before any f. 3 transcription exists.

Input notation: sources/transcription/CIPHER1-GUIDE.md (neutral glyph labels; the mapping to letters is here, from the
key's glyph descriptions). Values:
  numbers 6–100: syllables (cipher1.tsv). 12, 21, 31 also have Devos's conflicting letter values a, e, u: printed as
  "co|a", "fu|e", "hu|u" and flagged, never chosen.
  glyphs: <tri> a, <wbar> b, <arc> c, <abar> d, <theta> e, <8sq> g, <W> h, <eps> o, <venus> p, <omega> u, <II> x,
  <Omega> y, <hash> z.
  after: + -l, <tail> -r, <curl> -s (key: -l "+", -r hooked stroke, -s hook/tail; the guide's two shapes are matched to
  the key's two drawings).
  above: <dot> -n, <2dot> -m, <acute> medial r, <x> medial l, <dothook> medial h, <om> medial u (inserted after the
  first consonant of the syllable), <arch> doubles the consonant, <2>/<tilde> null, <cross>/<bar> code element
  (61 paz, 85 qual, 93 rey; any other prints [code:N]), <loop> number (flagged).
  letter groups: {bis} reyno, {nos} V.M., {to} hermanos (Devos's monosyllables); any other {xx} prints as {xx}, flagged.
    python3 decode_c1.py <transcription>
"""
import csv, re, sys
from pathlib import Path
KEY = Path(__file__).resolve().parents[2] / "sources" / "keys" / "cipher1.tsv"
GLYPH = {"<tri>": "a", "<wbar>": "b", "<arc>": "c", "<abar>": "d", "<theta>": "e", "<8sq>": "g", "<W>": "h",
         "<eps>": "o", "<venus>": "p", "<omega>": "u", "<II>": "x", "<Omega>": "y", "<hash>": "z"}
AFTER = {"+": "l", "<tail>": "r", "<curl>": "s"}
FINAL = {"<dot>": "n", "<2dot>": "m"}
MEDIAL = {"<acute>": "r", "<x>": "l", "<dothook>": "h", "<om>": "u"}
CODES = {"61": "paz", "85": "qual", "93": "rey"}
WORDS = {"bis": "reyno", "nos": "V.M.", "to": "hermanos"}
DEVOS = {"12": "a", "21": "e", "31": "u"}


def load():
    syl = {}
    for r in csv.DictReader(open(KEY, encoding="utf-8"), delimiter="\t"):
        if r["kind"] == "cluster" and r["symbol"].strip().isdigit():
            syl[r["symbol"].strip()] = r["value"]
    return syl


TOK = re.compile(r"^(\d+|<[A-Za-z0-9]+>|\{[a-z]+\}|<sign:[^>]*>)((?:\+|<tail>|<curl>)*)((?:<[a-z0-9]+>)*)(\?)?$")


def insert_medial(s, c):
    m = re.match(r"^(qu|[^aeiou]*)(.*)$", s)
    return m.group(1) + c + m.group(2)


def decode_token(tok, syl, flags, where):
    t = tok.split("|")[0]
    m = TOK.match(t)
    if not m:
        flags.append(f"{where} unparsed '{tok}'"); return f"[?{tok}]"
    b, after, above, q = m.groups()
    above = re.findall(r"<[a-z0-9]+>", above)
    if b.startswith("{"):
        w = b[1:-1]
        if w in WORDS:
            return f"[{WORDS[w]}]"
        flags.append(f"{where} letter group {b}{''.join(above)}"); return b + "".join(above)
    if b.startswith("<sign"):
        flags.append(f"{where} unknown sign '{tok}'"); return f"[{b}]"
    if ("<cross>" in above or "<bar>" in above) and b.isdigit():
        if b in CODES and "<cross>" in above:
            return f"[{CODES[b]}]"
        flags.append(f"{where} code element '{tok}'"); return f"[code:{b}]"
    if b.isdigit():
        if b not in syl:
            flags.append(f"{where} number outside table '{tok}'"); return f"[{b}]"
        s = syl[b]
        if b in DEVOS:
            flags.append(f"{where} Devos conflict {b}: {s} | {DEVOS[b]}"); s = f"{s}|{DEVOS[b]}"
    else:
        if b not in GLYPH:
            flags.append(f"{where} unknown glyph '{tok}'"); return f"[{b}]"
        s = GLYPH[b]
    for a in above:
        if a in MEDIAL:
            s = insert_medial(s, MEDIAL[a])
        elif a == "<arch>":
            s = s[0] + s if s and s[0] not in "aeiou" else s
            flags.append(f"{where} arch doubles '{tok}' -> {s}")
    for a in re.findall(r"\+|<tail>|<curl>", after):
        s += AFTER[a]
    for a in above:
        if a in FINAL:
            s += FINAL[a]
        elif a in ("<2>", "<tilde>"):
            s = f"({s})"
        elif a not in MEDIAL and a != "<arch>":
            flags.append(f"{where} mark above {a} in '{tok}'")
    return s + ("?" if q else "")


def main(path):
    syl = load(); flags = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        out = []
        for chunk in re.split(r"(\[\[.*?\]\])", line):
            if chunk.startswith("[["):
                out.append(chunk); continue
            for k, tok in enumerate(chunk.split(), 1):
                out.append(tok if tok in ("/", ",") else decode_token(tok, syl, flags, f"{lno}:{k}"))
        print(f"{lno:3d}  {' '.join(out)}")
    print("\n# flags")
    for f in flags:
        print("#", f)


if __name__ == "__main__":
    main(sys.argv[1])
