"""Code-word concordance across Cipher 3 v2 transcriptions.
    python3 concordance.py ../../sources/transcription/<dir>/transcription.txt ... > concordance.txt
For every token that decode_c3_v2 renders as a code (⟨#…⟩: a cross above, or digits with no parse),
print the letter, line, raw token and ±6 decoded tokens of context. Then a count table by code.
"""
import re, sys, io, contextlib
from collections import defaultdict
from pathlib import Path
import decode_c3_v2 as dc


def decoded(path):
    ext, flags, rows = dc.load_ext(), [], []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        for chunk in re.split(r"(\[\[.*?\]\])", line):
            if chunk.startswith("[["):
                rows.append((lno, chunk, chunk)); continue
            for t in chunk.split():
                rows.append((lno, t, dc.tok(t, ext, flags, f"{lno}")))
    return rows


def main(paths):
    by = defaultdict(list)
    for p in paths:
        name = Path(p).parent.name
        rows = decoded(p)
        for i, (lno, raw, dec) in enumerate(rows):
            if dec.startswith("⟨#"):
                key = re.sub(r"<[^>]+>|[+.p?]", "", raw)
                left = " ".join(r[2] for r in rows[max(0, i - 6):i])
                right = " ".join(r[2] for r in rows[i + 1:i + 7])
                by[key].append(f"{name:10s} l.{lno:<3d} {raw:16s} | {left} [[{dec}]] {right}")
    for k in sorted(by, key=lambda k: (-len(by[k]), k)):
        print(f"\n## {k}  ({len(by[k])})")
        print("\n".join(by[k]))


if __name__ == "__main__":
    main(sys.argv[1:])
