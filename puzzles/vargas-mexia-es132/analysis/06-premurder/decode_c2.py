"""Cipher 2 decoder (Vargas Mexía's Cipher 2, Jan–Mar 1578), from Tomokiyo's table (sources/keys/cipher2.tsv).

Notation (CIPHER2-GUIDE.md): a token is a base, then marks after, then marks above.
  base:  a number 1–23, or a letter-form (f, n, p, g, m, R, C, v, h, P, ...), or <rho>, <venus>, <sign:...>
  marks: + (-e), e (hook, -a), _ (dot below, -i), ^ (dot above, -o), . (dot at the right, -u), <bar> (null?:
         printed in parentheses)
Tomokiyo: 2=a, 3=b, ... 23=z (no j, k, v, w); clusters f=cr, n=pr, p=tr; the five marks give the vowel after the base.
Extensions are read from c2_extensions.tsv (base -> value); none are in the key. A base with no value prints as
[base] plus its vowel, and every unknown is listed. A vowel mark on a vowel base (e.g. 6^) prints both letters and is
flagged (Tomokiyo: "6 with diacritics" unresolved). Nothing is assigned by context.
    python3 decode_c2.py <transcription> [--syll]
"""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
KEY = HERE.parents[1] / "sources" / "keys" / "cipher2.tsv"
EXT = HERE / "c2_extensions.tsv"

VOWEL = {"+": "e", "e": "a", "_": "i", "^": "o", ".": "u"}
VOWELS = set("aeiou")


def load():
    base = {}
    for r in csv.DictReader(open(KEY, encoding="utf-8"), delimiter="\t"):
        s = r["symbol"].strip()
        if r["kind"] == "letter":
            base[s] = r["value"]
        elif r["kind"] == "cluster" and not s.startswith("(blank"):
            base[s.split()[0]] = r["value"]          # "f (under cr)" -> f
    ext = {}
    if EXT.exists():
        for r in csv.DictReader(open(EXT, encoding="utf-8"), delimiter="\t"):
            ext[r["base"]] = r["value"]
    return base, ext


TOK = re.compile(r"^(<rho>|<venus>|<sign:[^>]*>|\d+|[A-Za-z])((?:[+e_^.])*)((?:<[a-z]+>)*)(\?)?$")


def split(tok):
    """-> (base, marks_after, marks_above, uncertain) or None."""
    tok = tok.split("|")[0]                       # a|b: take the first reading
    m = TOK.match(tok)
    if not m:
        return None
    b, after, above, q = m.groups()
    if b.isdigit() and not (1 <= int(b) <= 23):
        return None
    return b, after, re.findall(r"<[a-z]+>", above), bool(q)


def decode_token(tok, base, ext, flags, where):
    s = split(tok)
    if s is None:
        flags.append(f"{where} unparsed '{tok}'")
        return f"[?{tok}]"
    b, after, above, q = s
    if "<bar>" in above:
        flags.append(f"{where} bar above (null?) '{tok}'")
    val = ext.get(b, base.get(b))
    vow = "".join(VOWEL[c] for c in after)
    if len(after) > 1:
        flags.append(f"{where} several marks after '{tok}'")
    if val is None:
        flags.append(f"{where} unvalued base '{b}' in '{tok}'")
        out = f"[{b}]{vow}"
    else:
        if val in VOWELS and vow:
            flags.append(f"{where} vowel mark on vowel '{tok}' -> {val}{vow}")
        out = val + vow
    if "<bar>" in above:
        out = f"({out})"                           # Tomokiyo: overbar = null?; shown, not dropped
    return out + ("?" if q else "")


def decode_line(line, lno, base, ext, flags, sep=""):
    out = []
    for chunk in re.split(r"(\[\[.*?\]\])", line):
        if chunk.startswith("[["):
            out.append(chunk); continue
        words = []
        for k, tok in enumerate(chunk.split(), 1):
            if tok in ("/", ",", "/.", "."):
                words.append(tok); continue
            words.append(decode_token(tok, base, ext, flags, f"{lno}:{k}"))
        out.append(sep.join(words) if sep else " ".join(words))
    return " ".join(x for x in out if x)


def main(path, syll=False):
    base, ext = load()
    flags = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        print(f"{lno:3d}  {decode_line(line, lno, base, ext, flags, '' if not syll else '-')}")
    print("\n# flags")
    for f in flags:
        print("#", f)
    unk = [f for f in flags if "unvalued" in f or "unparsed" in f]
    print(f"# {len(unk)} unknown/unparsed tokens; extensions in use: {ext or 'none'}")


if __name__ == "__main__":
    main(sys.argv[1], "--syll" in sys.argv)
