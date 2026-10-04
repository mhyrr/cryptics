"""Align two readers' transcriptions token by token and list every disagreement.
    python3 align.py A.txt B.txt > diffs.txt
Clear text [[...]] is reduced to one token per word, prefixed '=' so it aligns too. Notation is
normalised first ('<cross above>' -> '<crossabove>'). Output: summary counts, then each non-equal
block with A line:token and B line:token positions. No decoding; safe for blind reconcilers.
"""
import re, sys, difflib


def stream(path):
    toks = []
    for lno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n").replace("<cross above>", "<crossabove>")
        if not line.strip() or line.startswith("#"):
            continue
        k = 0
        for chunk in re.split(r"(\[\[.*?\]\])", line):
            if chunk.startswith("[["):
                for w in chunk[2:-2].split():
                    k += 1; toks.append(("=" + w.lower(), lno, k))
            else:
                for t in chunk.split():
                    k += 1; toks.append((t, lno, k))
    return toks


def main(a, b):
    A, B = stream(a), stream(b)
    sm = difflib.SequenceMatcher(None, [t[0] for t in A], [t[0] for t in B], autojunk=False)
    eq = sum(i2 - i1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == "equal")
    ca = sum(1 for t in A if not t[0].startswith("=")); cb = sum(1 for t in B if not t[0].startswith("="))
    print(f"# A: {len(A)} tokens ({ca} cipher); B: {len(B)} tokens ({cb} cipher); equal-aligned: {eq}")
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        n += 1
        pa = f"A {A[i1][1]}:{A[i1][2]}" if i1 < len(A) else "A end"
        pb = f"B {B[j1][1]}:{B[j1][2]}" if j1 < len(B) else "B end"
        ctx = " ".join(t[0] for t in A[max(0, i1 - 3):i1])
        print(f"{n:4d} {op:8s} {pa:10s} {pb:10s} | ctx: {ctx} | A: {' '.join(t[0] for t in A[i1:i2]) or '-'} | B: {' '.join(t[0] for t in B[j1:j2]) or '-'}")
    print(f"# {n} disagreement blocks")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
