"""Score a blind Cipher 2 transcription of f. 11v against Tomokiyo's (tomokiyo_f11.txt, the f. 11v block).
Cipher tokens only (clear [[...]] and separators dropped); '?' and a|b alternatives reduced to the first reading.
Tomokiyo's text is partial (he cut lines and skipped some), so the score is the share of HIS tokens that the reader
matched exactly in an order-preserving alignment, plus the same with the base only (marks ignored).
    python3 calibrate_c2.py ../../sources/transcription/f11v-cal/transcription.txt
"""
import re, sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent


def toks(lines):
    out = []
    for line in lines:
        if not line.strip() or line.startswith("#"):
            continue
        line = re.sub(r"\[\[.*?\]\]", " ", line)
        for t in line.split():
            if t in ("/", ",", "/.", "."):
                continue
            out.append(t.split("|")[0].rstrip("?"))
    return out


def tomokiyo_11v():
    lines = open(HERE / "tomokiyo_f11.txt", encoding="utf-8").read().split("\n")
    a = lines.index("# (f.11v)"); b = lines.index("# (f.12)")
    return toks(lines[a + 1:b])


def base(t):
    m = re.match(r"^(<[^>]+>|\d+|[A-Za-z])", t)
    return m.group(1) if m else t


def score(ref, hyp, key=lambda t: t):
    sm = difflib.SequenceMatcher(None, [key(t) for t in ref], [key(t) for t in hyp], autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks())


def main(path):
    ref = tomokiyo_11v()
    hyp = toks(open(path, encoding="utf-8"))
    ex = score(ref, hyp); bs = score(ref, hyp, base)
    print(f"Tomokiyo f. 11v cipher tokens: {len(ref)}; reader tokens: {len(hyp)}")
    print(f"exact (base + marks): {ex}/{len(ref)} = {ex/len(ref):.0%}")
    print(f"base only:            {bs}/{len(ref)} = {bs/len(ref):.0%}")
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    print("\n# disagreements (Tomokiyo -> reader)")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"{op:8s} T[{i1}:{i2}] {' '.join(ref[i1:i2]) or '-':30s} -> {' '.join(hyp[j1:j2]) or '-'}")


if __name__ == "__main__":
    main(sys.argv[1])
