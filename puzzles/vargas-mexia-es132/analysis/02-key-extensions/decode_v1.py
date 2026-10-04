"""Decoder 01 plus the frozen extensions in extensions.tsv (applied before the 01 rules)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "01-decode-f198"))
import decode as d

EXT = [(re.compile(r"^21\.\??$"), "que"), (re.compile(r"^21_\??$"), "qui"),
       (re.compile(r"^2H[+._^]*\??$"), "que"), (re.compile(r"^H[+._^]*\??$"), "ne"),
       (re.compile(r"^(<sign:Sigma>|ε)"), "o")]
_orig = d.decode_line

def decode_line(line, lno, flags):
    out = []
    for chunk in re.split(r"(\[\[.*?\]\])", line):
        if chunk.startswith("[["):
            out.append(chunk); continue
        for tok in chunk.split():
            for rx, val in EXT:
                if rx.search(tok):
                    out.append(val.upper()); break      # upper case marks an extension value
            else:
                out.append(_orig(tok, lno, flags))
    return " ".join(out)

d.decode_line = decode_line
if __name__ == "__main__":
    d.main(sys.argv[1])
