"""spelling.py - how the true decode and the printed text differ, as letter counts. HOLDS NO SIGN VALUES.

    python3 spelling.py [p1|full]
Decodes the cipher with the period key (sealed, through ../outside/decode.py), joins the letters, and matches
the string to the printed text with difflib. Reports: letters on each side, letters in equal blocks, the sizes
of the differing blocks, and the most frequent small differences as 'decode>print' letter strings. These are
facts of Italian spelling and of the abridgement, not values of signs.
"""
import collections, difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "outside"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "line"))
import decode, align  # noqa: E402

sub = sys.argv[1] if len(sys.argv) > 1 else "p1"
truth = decode.load_truth()
rows = decode.decode_file(os.path.join(HERE, "inputs", f"cipher-{sub}.txt"), truth)
D = "".join(decode.norm(it["value"] or "") for row in rows for it in row if it["type"] not in ("unread", "missing"))
P, _, _, _ = align.parse_plain(open(os.path.join(HERE, "inputs", f"plain-{sub}.txt"), encoding="utf-8").read())
sm = difflib.SequenceMatcher(None, D, P, autojunk=False)
eq, small, big = 0, collections.Counter(), []
for tag, a0, a1, b0, b1 in sm.get_opcodes():
    if tag == "equal":
        eq += a1 - a0
    elif a1 - a0 <= 4 and b1 - b0 <= 4:
        small[f"{D[a0:a1] or '-'}>{P[b0:b1] or '-'}"] += 1
    else:
        big.append((a1 - a0, b1 - b0))
print(f"decode letters {len(D)}, print letters {len(P)}, in equal blocks {eq}")
print(f"small differences {sum(small.values())} ({len(small)} kinds); large blocks {len(big)}: "
      f"decode letters {sum(a for a, b in big)}, print letters {sum(b for a, b in big)}")
print("large blocks (decode, print):", sorted(big, reverse=True)[:30])
for k, c in small.most_common(45):
    print(f"{c}\t{k}")
