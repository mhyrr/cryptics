"""Syllable agreement between two decoded outputs of the same letter (decode_c3_v2 or decode_v2 output).
    python3 agree.py a_dec.txt b_dec.txt
Clear text and line labels are dropped; u/v and i/y merged; difflib alignment over decoded syllables."""
import re, sys, difflib


def syl(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("## FLAGS"):
            break
        if re.match(r"^\s*\d+\s", line):
            body = re.sub(r"\[\[.*?\]\]", " ", line.split(None, 1)[1])
            out += [t.lower().replace("v", "u").replace("y", "i") for t in body.split()
                    if not re.match(r"^⟨\w+\.\w+⟩$|^⟨[rv]\d+⟩$|^⟨\d+[rv]⟩$", t)]
    return out


a, b = syl(sys.argv[1]), syl(sys.argv[2])
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
m = sum(x.size for x in sm.get_matching_blocks())
print(f"A {len(a)} syllables, B {len(b)}; matched {m}: {m/len(a):.0%} of A, {m/len(b):.0%} of B")
