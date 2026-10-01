"""Gate measures for f. 539 across three readings (see README.md). Standard library only.

Usage: python3 measure.py > result.txt
"""
import re, urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent.parent / "sources" / "transcription"
BOURDEAU = ("https://raw.githubusercontent.com/dbourdeau/cyphersolver/"
            "9226922ffb0663b1d9b95f4ef898d093efd74ef2/targets/joyeuse/ct_f539.txt")

ARABIC = re.compile(r"^\d+\??$")
ROMAN = {"xiiij", "xvj", "xij"}           # Roman numerals as read; bare "xi" is ambiguous, kept as a sign

def lines_from(text, sep_bar=False):
    out = []
    for ln in text.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        out.append([t for t in ln.replace("|", " ").split()] if sep_bar else ln.split())
    return out

# Each reader's own mark convention (from its marks.tsv, or Bourdeau's header).
def marked_A(t): return bool(re.search(r"[+#.:|]$|[+#.:]\|$", t.rstrip("?")))
def marked_B(t): return bool(re.search(r"_(d|dd|x|h|S|f|hat)$", t.rstrip("?")))
def marked_D(t): return bool(re.search(r"[.:+#^_]+$", t.rstrip("?")))

def measure(name, lines, is_marked):
    toks = [t for l in lines for t in l]
    arab = [t for t in toks if ARABIC.match(t)]
    rom = [t for t in toks if t in ROMAN]
    signs = [t for t in toks if not ARABIC.match(t) and t not in ROMAN]
    unq = [t for t in signs if "?" in t]
    marked = [t for t in signs if is_marked(t)]
    unmarked = [t for t in signs if not is_marked(t)]
    D = len(set(signs))
    print(f"== {name}")
    print(f"  tokens per line: {[len(l) for l in lines]}  total {len(toks)}")
    print(f"  arabic numbers ({len(arab)}): {' '.join(arab)}")
    print(f"  roman numerals ({len(rom)}): {' '.join(rom)}")
    print(f"  sign tokens N={len(signs)}  distinct D={D}  N/D={len(signs)/D:.2f}  hapax={sum(1 for c in Counter(signs).values() if c==1)}  flagged '?'={len(unq)}")
    print(f"  marked {len(marked)} over {len(set(marked))} labels; unmarked {len(unmarked)} over {len(set(unmarked))} labels")
    return len(signs)

A = lines_from((SRC / "reader-A" / "transcription.txt").read_text())
B = lines_from((SRC / "reader-B" / "transcription.txt").read_text())
D = lines_from(urllib.request.urlopen(BOURDEAU, timeout=60).read().decode(), sep_bar=True)
nA = measure("reader A (blind)", A, marked_A)
nB = measure("reader B (blind)", B, marked_B)
nD = measure("Bourdeau 2026-09-16 (single reader)", D, marked_D)
N = min(nA, nB)
print(f"\nG1: lower blind count N = {N}; threshold 300 -> {'PASS' if N >= 300 else 'FAIL'}")
print("Reference ratios: Marmont ~1300/155 = 8.4 (Church); f. 555 858/86 = 10.0 (Lasry, via breach research)")
