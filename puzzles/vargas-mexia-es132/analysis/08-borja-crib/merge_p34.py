"""Exp 08 amendment 2 (2026-10-16, after reader B, before reader A): P3 and P4 are scored as one passage, P34.
Reason: reader B's decode showed that the five full-width lines at the foot of f. 42v are decipherment, not clear
text. They continue the P3 margin note and run into the start of P4 (amendment 1, prep_plain.py, was wrong). Merging
avoids drawing the P3/P4 boundary by eye.
    python3 merge_p34.py cipher <transcription.txt> > X     (drops the P4 header: P4 tokens join P3)
    python3 merge_p34.py plain <C plaintext.txt> > Y         (keeps the full-width lines; drops the P4 header and
                                                               C's [sign] marker)"""
import re, sys
kind, path = sys.argv[1], sys.argv[2]
for line in open(path, encoding="utf-8"):
    line = line.rstrip("\n")
    if kind == "cipher" and re.match(r"^#\s*=+\s*P4\b", line):
        continue
    if kind == "plain":
        if line.startswith("# P4") or line.startswith("# --- full width"):
            continue
        line = line.replace("[sign]", "").strip()
    print(line)
