"""Exp 08 diagnostic (exploratory, written after scoring; not a test). For each base sign, what plaintext the
1579 decipherment has where the sign stands, using score.py's alignment. Tokens with no matched letters get the
plaintext gap between their matched neighbours.
    python3 diag.py <merged transcription> plain_p34.txt [base ...]"""
import sys, difflib, re
from collections import defaultdict, Counter
sys.argv, args = sys.argv[:1], sys.argv[1:]
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("score_mod", Path(__file__).with_name("score.py"))
src = Path(__file__).with_name("score.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": str(Path(__file__).with_name("score.py"))}
exec(compile(src, "score.py", "exec"), ns)
cipher, plain = ns["read_cipher"](args[0]), ns["read_plain"](args[1])
want = set(args[2:])
seen = defaultdict(Counter)
for p in cipher:
    toks = cipher[p]; stream, owner = [], []
    for i, (_, _, d) in enumerate(toks):
        for c in ns["norm"](d):
            stream.append(c); owner.append(i)
    a, b = "".join(stream), ns["norm"](plain.get(p, ""))
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    amap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
    for i, (lno, t, d) in enumerate(toks):
        before = [amap[k] for k in amap if owner[k] < i]; after = [amap[k] for k in amap if owner[k] > i]
        lo = max(before) + 1 if before else 0; hi = min(after) if after else len(b)
        seg = b[lo:hi]
        base = ns["base_of"](t)
        if not want or base in want:
            seen[base][f"{t} -> {ns['norm'](d) or d} | pt '{seg}'"] += 1
for base in sorted(seen, key=lambda k: -sum(seen[k].values())):
    print(f"== {base}")
    for k, n in seen[base].most_common():
        print(f"  {n}x {k}")
