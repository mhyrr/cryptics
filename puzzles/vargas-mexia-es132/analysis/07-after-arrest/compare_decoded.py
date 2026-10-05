"""Compare two decoded witnesses (decode_c3_v2.py output) on the decoded text, not on tokens. Readers differ in notation
(a sign written `d` by one and `6` by another decodes the same), so agreement is measured where it matters.
Letters only, lower case, unknowns dropped, clear text included. Reports the share of A's characters matched in order
(difflib, no autojunk) and, with --show, prints the decoded text of A with unmatched stretches in [brackets] and B's
reading after them, line-referenced, so a passage can be read in both witnesses at once.
    python3 compare_decoded.py A_dec.txt B_dec.txt [--show] [--from N --to M]   (N, M: A's decoded line numbers)"""
import re, sys, difflib


def stream(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("## FLAGS"):
            break
        m = re.match(r"^\s*(\d+)\s\s(.*)$", line.rstrip("\n"))
        if not m:
            continue
        txt = re.sub(r"⟨[^⟩]*⟩", "", m.group(2)).replace("(r|l)", "r").lower()
        for ch in re.sub(r"[^a-zñçáéíóú]", "", txt):
            out.append((ch, int(m.group(1))))
    return out


def main():
    args = sys.argv[1:]
    show = "--show" in args
    lo = int(args[args.index("--from") + 1]) if "--from" in args else 0
    hi = int(args[args.index("--to") + 1]) if "--to" in args else 10 ** 6
    A, B = stream(args[0]), stream(args[1])
    a, b = "".join(c for c, _ in A), "".join(c for c, _ in B)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    matched = sum(bl.size for bl in sm.get_matching_blocks())
    print(f"A {len(a)} chars, B {len(b)} chars, matched {matched} = {matched / max(1, len(a)):.0%} of A, "
          f"{matched / max(1, len(b)):.0%} of B")
    if not show:
        return
    out, cur = [], None
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if i1 < len(A) and not (lo <= A[i1][1] <= hi) and not (i2 > 0 and lo <= A[i2 - 1][1] <= hi):
            continue
        ln = A[i1][1] if i1 < len(A) else A[-1][1]
        if ln != cur:
            out.append(f"\n{ln:3d}  "); cur = ln
        if op == "equal":
            out.append(a[i1:i2])
        else:
            out.append(f"[{a[i1:i2]}|{b[j1:j2]}]")
    print("".join(out))


main()
