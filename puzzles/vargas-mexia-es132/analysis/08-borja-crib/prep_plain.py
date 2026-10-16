"""Exp 08: build the scoring plaintext from reader C's margin transcription. Fixed 2026-10-16 after C finished and
before any cipher reader output exists.
    python3 prep_plain.py ../../sources/transcription/fr15561-f42-margins/plaintext.txt > plain_scoring.txt
- Drops every line after `# --- full width ---` up to the next passage header: those lines (f. 42v foot,
  "Valiendome de todas las occasiones … si no se hazen otras") are the letter's clear main text, not decipherment.
  Text flow: f. 42v clear ends "…otras"; the f. 43r decipherment begins "mayores…"; the f. 43r clear text follows.
- Removes reader C's `[sign]` marker (the keying sign before the P1 note, not text)."""
import re, sys
skip = False
for line in open(sys.argv[1], encoding="utf-8"):
    if line.startswith("# P"):
        skip = False
    elif line.startswith("# --- full width"):
        skip = True; continue
    if not skip:
        print(line.rstrip("\n").replace("[sign]", "").strip())
