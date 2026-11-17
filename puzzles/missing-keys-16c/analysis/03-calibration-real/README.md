# 03 — real calibration of the aligner

**Question.** On a real pair (a blind reader's sign transcription and an independent period plaintext), does
`line/align.py` rebuild a key we hold?

**Why not Saint-Goard.** `PIPELINE.md` names Saint-Goard's letter of 23 Dec 1579 and its decipherment. That pair
cannot test the aligner: its cipher side (`vargas-mexia-es132/analysis/10-saint-goard/reader*/`) was written as
letter values read with the key, so the signs are gone, and Tomokiyo's Longlée table exists here only as an image.
Using it would need a new blind transcription of seven pages that es. 132 measured as hard to read. Substitute:

**The pair.** Philip II to Vargas Mexía, Guadalupe, 28 Mar 1580, BnF es. 132 f. 255, in Cp.30. Cipher side: the
blind transcription `vargas-mexia-es132/sources/transcription/f255/` (one reader, no key), text rows 11–34.
Plain side: the Simancas minute of the same passage, printed by Teulet (vol. 5, 1862, pp. 213–214). The minute is
not the letter: it says "Su Majestad le tiene" where the letter has "yo le tengo", and the es. 132 decode matched
it at 77–82%. That is the kind of plain side a class A item gives. Truth: Cp.30 (`cipher3.tsv`).
It is small: about 900 letters. `prep.py` writes `cipher.txt`, `plain.txt`, `truth.tsv`.

**Pass bars (written 2026-11-16, before `run.py` was run; nothing from this pair had been aligned).**
- **R1.** Of the unit types that occur five times or more and have a value in Cp.30, at least 80% get the true
  value as their top value.
- **R2.** At most 5% of `certain` entries and at most 10% of all marked entries have a wrong value.
- **R3.** Held-out accuracy is within 10 points of the ceiling (the true Cp.30 table scored on the same lines by
  the same scorer), and the shuffled control is at least 25 points below the held-out accuracy.
  The stage 4 bar of 0.85 is not used here: the minute differs from the letter, so the true key cannot reach it.

**Run.** `python3 prep.py && python3 run.py`.

**Result.** Not run yet.
