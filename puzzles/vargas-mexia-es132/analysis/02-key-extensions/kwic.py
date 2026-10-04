"""Every occurrence of each candidate key extension, in both readers, with decoded context.
Decoding uses the frozen 01 decoder; the candidate is shown as {TOKEN} in place."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "01-decode-f198"))
import decode as d

CANDIDATES = {
    "q-dot (21.)": lambda t: re.fullmatch(r"21\.\??", t),
    "q-dot-below (21_)": lambda t: re.fullmatch(r"21_\??", t),
    "2H / 24 (A's reading of 2H)": lambda t: re.fullmatch(r"(2H|24)[+._^]*\??", t),
    "H / 4 with mark (A)": lambda t: re.fullmatch(r"(H|4)[+._^]*\??", t) and not re.fullmatch(r"4[._^]?\??", t),
    "Sigma / epsilon": lambda t: "Sigma" in t or t.startswith("ε"),
}

def tokens(path):
    out = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("#"):
            continue
        for chunk in re.split(r"(\[\[.*?\]\])", line.rstrip("\n")):
            if chunk.startswith("[["):
                out.append((lno, chunk, chunk)); continue
            for tok in chunk.split():
                out.append((lno, tok, d.decode_line(tok, lno, [])))
    return out

for R in "AB":
    toks = tokens(HERE.parent.parent / "sources" / "transcription" / f"reader-{R}" / "f198.txt")
    for name, pred in CANDIDATES.items():
        hits = [i for i, (_, t, _) in enumerate(toks) if not t.startswith("[[") and pred(t)]
        print(f"\n== reader {R} · {name} · {len(hits)} occurrences")
        for i in hits:
            left = " ".join(x[2] for x in toks[max(0, i - 6):i])
            right = " ".join(x[2] for x in toks[i + 1:i + 7])
            print(f"  l{toks[i][0]:>2}  …{left[-60:]:>60} {{{toks[i][1]}}} {right[:60]}…")
