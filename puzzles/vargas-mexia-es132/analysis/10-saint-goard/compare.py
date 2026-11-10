"""Align each pair of readers' glyph-token streams for each page and score their agreement.

Input : readerA|B|C/<page>.txt  (rows "Lnn | tokens | French", see GUIDE.md)
Output: results/agreement.tsv (one row per page) and results/aligned-<page>-<pair>.txt (side-by-side blocks)
Method: nulls (·) and CLEAR rows are dropped; tokens are lower-cased; the two streams of a page are aligned
with difflib.SequenceMatcher (no line numbers are trusted). "agree" = tokens in matching blocks;
agreement = 2*agree / (len A + len B). A token "(a/o)" matches either value. "?" never matches.
Agreement between two readers is not accuracy: both can share an error.
"""
import os, re, difflib, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["363r", "363v", "364r", "364v", "365r", "365v", "366r"]

def tokens(path):
    out = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\s*L\d+\w?\s*\|(.*?)\|(.*)", line)
        if not m or "CLEAR" in m.group(1):
            continue
        for t in m.group(1).split():
            t = t.strip().lower()
            if t in ("·", ".", "•", "") :
                continue
            out.append(t)
    return out

def norm(t):
    m = re.match(r"\((\w+)/(\w+)\)", t)
    return m.group(1) if m else t

os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
rows = ["page\tpair\ttokens_1\ttokens_2\tunknown_1\tunknown_2\tagree\tagreement"]
for p in PAGES:
    for r1, r2 in (("A", "B"), ("A", "C"), ("B", "C")):
        f1, f2 = (os.path.join(HERE, "reader" + r, p + ".txt") for r in (r1, r2))
        if not (os.path.exists(f1) and os.path.exists(f2)):
            continue
        a, b = tokens(f1), tokens(f2)
        na = [norm(t) if t != "?" else "?1" for t in a]
        nb = [norm(t) if t != "?" else "?2" for t in b]
        sm = difflib.SequenceMatcher(None, na, nb, autojunk=False)
        agree = sum(bl.size for bl in sm.get_matching_blocks())
        rows.append(f"{p}\t{r1}{r2}\t{len(a)}\t{len(b)}\t{a.count('?')}\t{b.count('?')}\t{agree}\t{2*agree/max(1,len(a)+len(b)):.3f}")
        with open(os.path.join(HERE, "results", f"aligned-{p}-{r1}{r2}.txt"), "w", encoding="utf-8") as f:
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag == "equal":
                    f.write("= " + "".join(x if len(x) == 1 else f"[{x}]" for x in a[i1:i2]) + "\n")
                else:
                    f.write(f"{r1} {' '.join(a[i1:i2])}\n{r2} {' '.join(b[j1:j2])}\n")
open(os.path.join(HERE, "results", "agreement.tsv"), "w").write("\n".join(rows) + "\n")
print("\n".join(rows))
