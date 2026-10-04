"""Extension tally on the v2 Cipher 4 texts (step 4 of the 2026-10-04 plan). Frozen rules: extensions.tsv
(02) plus cross-above doubling (decode_v2). For each extension, every occurrence with ±6 decoded tokens,
grouped by letter; counts per letter. Fit is judged by reading each line (recorded in tally-judged.md),
not by this script.
    python3 tally.py > tally.txt
"""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decode_v2 as v2
d = v2.d
ROOT = HERE.parent.parent / "sources" / "transcription"
LETTERS = {"f87": ROOT / "v2/f87.txt", "f123": ROOT / "v2/f123.txt", "f157": ROOT / "v2/f157.txt",
           "f179": ROOT / "v2/f179.txt", "f198": ROOT / "v2/f198.txt", "f154 (held-out)": ROOT / "f154/transcription.txt"}
EXT = {"21. = que": r"21\.\??", "21_ = qui": r"21_\??", "2H = que": r"2H[+._^]*\??",
       "H = ne": r"H[+._^]*\??", "Sigma = o": r"(<sign:Sigma>|ε).*", "cross above doubles": r".*<crossabove>.*"}


def toks(path):
    out = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("#"):
            continue
        line = line.rstrip("\n").replace("<cross above>", "<crossabove>")
        for chunk in re.split(r"(\[\[.*?\]\])", line):
            if chunk.startswith("[["):
                out.append((lno, chunk, chunk)); continue
            for t in chunk.split():
                out.append((lno, t, v2.decode_line(t, lno, [])))
    return out


counts = {}
for name, p in LETTERS.items():
    if not p.exists():
        print(f"# {name}: missing {p}"); continue
    T = toks(p)
    for ext, rx in EXT.items():
        hits = [i for i, (_, t, _) in enumerate(T) if not t.startswith("[[") and re.fullmatch(rx, t)]
        counts[(name, ext)] = len(hits)
        print(f"\n== {name} · {ext} · {len(hits)}")
        for i in hits:
            l = " ".join(x[2] for x in T[max(0, i - 6):i]); r = " ".join(x[2] for x in T[i + 1:i + 7])
            print(f"  l{T[i][0]:>3} …{l[-55:]:>55} {{{T[i][1]}→{T[i][2]}}} {r[:55]}…")
print("\n## Counts")
for ext in EXT:
    print(f"{ext:22s} " + "  ".join(f"{n}:{counts.get((n, ext), '-')}" for n in LETTERS))
