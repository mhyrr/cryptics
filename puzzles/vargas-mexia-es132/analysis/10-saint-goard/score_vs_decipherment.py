"""Score each reader of the 23 Dec 1579 cipher letter against the court decipherment (fr. 16106 ff. 208r-209v).

Truth : ../../sources/fr16106-ff208-209-decipherment.md, section "## Text" (main-thread working transcription of the
        sixteenth-century decipherment; it has gaps and may have errors of its own).
Input : readerA|B|C/<page>.txt, column 2 (glyph tokens). Reader C did not read f. 366r; reader B's file is used there.
Method: both sides are reduced to letter strings: lower case, accents stripped, v->u, j->i, y->i, letters only.
        Word signs "[Roi]" become their letters; "(a/o)" takes the first value; "?" stays "?" and never matches;
        nulls are dropped; CLEAR rows are skipped. Bracketed editorial matter in the truth is removed, and words
        marked [?] are kept. The two strings are aligned with difflib.SequenceMatcher (autojunk off).
        precision = matched letters / reader letters; recall = matched letters / truth letters.
        Spelling differences between the cipher and the decipherer (and the transcriber's expansions) count as
        errors, so these figures are lower bounds on glyph accuracy.
Output: results/score_vs_decipherment.tsv
"""
import os, re, difflib, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["363r", "363v", "364r", "364v", "365r", "365v", "366r"]

def letters(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-z?]", "", s)

def truth():
    t = open(os.path.join(HERE, "..", "..", "sources", "fr16106-ff208-209-decipherment.md"), encoding="utf-8").read()
    t = t.split("## Text", 1)[1].split("## English summary", 1)[0]
    t = re.sub(r"\*\*f\. \d+[rv]\.\*\*", " ", t)
    t = re.sub(r"\[interlined:[^\]]*\]", " ", t)
    t = re.sub(r"\[…[^\]]*\]", " ", t)          # unread stretches and editorial notes starting with an ellipsis
    t = t.replace("[?]", "").replace("…", " ")
    t = re.sub(r"\[([^\]]*)\]", r"\1", t)        # supplied letters and doubtful words are kept
    return letters(t).replace("?", "")

def reader(r):
    out = []
    for p in PAGES:
        rr = r if os.path.exists(os.path.join(HERE, "reader" + r, p + ".txt")) else "B"
        for line in open(os.path.join(HERE, "reader" + rr, p + ".txt"), encoding="utf-8"):
            m = re.match(r"\s*L\d+\w?\s*\|(.*?)\|", line)
            if not m or "CLEAR" in m.group(1):
                continue
            for tok in m.group(1).split():
                if tok in ("·", ".", "•"):
                    continue
                if tok == "?":
                    out.append("?"); continue
                alt = re.match(r"\((\w+)/", tok)
                out.append(letters(alt.group(1) if alt else tok.strip("[]")))
    return "".join(out)

T = truth()
rows = ["reader\treader_letters\tunknown\ttruth_letters\tmatched\tprecision\trecall"]
for r in "ABC":
    s = reader(r)
    sm = difflib.SequenceMatcher(None, s, T, autojunk=False)
    m = sum(b.size for b in sm.get_matching_blocks())
    rows.append(f"{r}\t{len(s)}\t{s.count('?')}\t{len(T)}\t{m}\t{m/len(s):.3f}\t{m/len(T):.3f}")
os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
open(os.path.join(HERE, "results", "score_vs_decipherment.tsv"), "w").write("\n".join(rows) + "\n")
print("\n".join(rows))
