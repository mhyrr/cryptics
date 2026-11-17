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

**Result (2026-11-16): pass, with the third version of the aligner.** `result.tsv`, `key-v0.tsv`.

| Bar | Run 1 | Final run |
|---|---|---|
| R1 top value right, frequent types | 0 of 29 | 26 of 29 (0.90) |
| R2 wrong among `certain` / among marked | 23 of 23 / 25 of 25 | 0 of 13 / 1 of 29 |
| R3 held-out accuracy / ceiling / control | 0.00 / 0.51 / 0.00 | 0.83 / 0.79 / 0.28 (coverage 0.86) |

**What was wrong (run 1).** Every frequent sign was given the value null, and a few rare signs each took a
whole phrase ("puede assegurar muy", "amor y recibira"). The model let any sign emit a code-length span, and a
span seen once became near-certain on the next pass. The synthetic pair had not shown it.
**First fix, rejected.** Codes off for the first half of the passes, and one count taken off every code span.
This pair passed (same figures as the final run), but the synthetic pair then failed S1 and S2 on all five seeds:
code words were cut to their first syllable ("madre" → "mad").
**Final fix.** A code span counts only for the support it has beyond its single best place in the plaintext.
A span seen in one place is worth nothing; a code seen in several places keeps its support. Both calibrations
were then rerun. The bars were not changed.

**Reading the table.** The one marked value that differs from Cp.30 is `21` = "qu" (Cp.30: q); the clerk wrote
q for "qu", so the aligner's value is what the sign stands for in use. The reader's habit of writing the
z-shaped 25 as `1` shows up as `1` = u (16 of 24): the table records signs as this reader names them. `24` (t) is
left `unknown` at 0.56 share because the reader confuses 24, 21 and 22. Held-out accuracy can exceed the
true-key ceiling for that reason: the rebuilt table fits the reader, and the true table does not.

**Limits.** One reader, 885 units, one pair. The plain side is a minute, not a decipherment. Line extents used
for the folds come from the full alignment.
