"""Score a v2 decode of f. 83 against Tomokiyo's aligned syllable labels (SECONDARY:
cryptiana spanish3Dduplicates.png, f. 83 panel, transcribed 2026-10-04 from the image; his "?" kept as "?").
    python3 calibrate.py f83_cal_v2.txt
Syllables are compared after lower-casing, u/v and i/y merged; difflib alignment.
"""
import re, sys, difflib
REF = ("cri vis cer ca de la sa li da del du que de ? a lan con de sse que y no pa ra yr a los pa "
       "y sses ba xos y lo que vos so bre e llo ha vi a de s pa ssa da con el re y y su ma dre").split()


def norm(s):
    return s.lower().replace("v", "u").replace("y", "i")


def main(path):
    hyp = []
    for line in open(path, encoding="utf-8"):
        if re.match(r"^\s*\d+\s", line):
            body = re.sub(r"\[\[.*?\]\]", " ", line.split(None, 1)[1])
            hyp += body.split()
    # start at the first reference syllable, stop after "dre"
    hyp = hyp[[norm(h) for h in hyp].index("cri"):]
    hyp = hyp[:[norm(h) for h in hyp].index("dre") + 1]
    sm = difflib.SequenceMatcher(None, [norm(x) for x in REF], [norm(x) for x in hyp], autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    print(f"reference syllables {len(REF)}, decoded tokens {len(hyp)}, matched {m} ({m/len(REF):.0%} of reference)")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"  {op:8s} ref: {' '.join(REF[i1:i2]) or '-':22s} ours: {' '.join(hyp[j1:j2]) or '-'}")


if __name__ == "__main__":
    main(sys.argv[1])
