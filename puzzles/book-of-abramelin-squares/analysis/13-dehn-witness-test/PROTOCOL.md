# 13 — Protocol: score frozen interior predictions against the Dehn readings

Written 2026-09-20, before the Dehn readings were parsed. See EXPOSURE below
for the two readings seen by accident before this file existed.

## The witness

Peterson's web edition of Mathers (the project's pinned source, cached at
`sources/cache/e2/mathers.html`) prints variant readings in its note column,
marked `D:`. His foreword says they come from Georg Dehn's edition of the
German text. A regular-expression count finds 46 notes of the form
`D: WORD, WORD, ...`. They often give every row of a square that Mathers
leaves mostly blank. The project record has not used them before.

Tier: edited PRIMARY at two removes (German manuscripts, then Dehn, then
Peterson). Dehn compared several German witnesses and may have corrected or
reconstructed. So this is a test against a modern German-based edition, not
against an untouched manuscript. Hypothesis H5 already warns about this.

## Question

Mathers leaves 151 squares incomplete. Where a Dehn reading supplies letters
for cells that are blank in Mathers, how many of those letters do models that
never saw them predict?

## Models, frozen before parsing

All models see only the Mathers export (`sources/mathers-squares.json`).

1. `sym_TA`: experiment 01's forced fills under transpose plus half-turn,
   `analysis/01-mathers-structure/predictions.json`, committed in `998f90d` on
   2026-09-16. Used as committed.
2. `sym_T`: transpose only. A blank cell (i, j) takes the visible letter at (j, i).
3. `class_checkerboard`: predicts vowel or consonant, not a letter. Cell (i, j),
   zero-indexed, is a vowel when the top-row letter at column j is a vowel and
   i is even, or that letter is a consonant and i is odd. Vowels are A E I O U.
   Needs a visible top-row letter in column j.
4. `letter_filler`: the checkerboard class, then the most frequent interior
   letter of that class in the 81 complete Mathers squares. Development
   leave-one-out accuracy on those squares: class 1,046/1,413 (74 %), letter
   332/1,413 (23 %), against 233 for the single most frequent letter.
5. `letter_global`: the single most frequent interior letter. Baseline.

Predictions for every blank cell of every analyzable incomplete square are
written to `predictions.json` and hashed in `prediction-freeze.json` before
`parse_dehn.py` is run for the first time.

## Scoring

A scored cell is blank in Mathers, inside the square's shape, and a letter in
the Dehn reading of the same square id with the same dimensions. Squares whose
Dehn reading has a different shape are listed and not scored. Report per model:
predicted, correct, wrong, abstained, split into border cells and strict
interior cells. Report separately how often Mathers and Dehn disagree on cells
visible in both, split into top row, other border, and interior.

Also reported, as description and not as a model score: how many complete Dehn
squares satisfy T and TA exactly, and the share of interior cells that follow
the checkerboard class.

## What would count

`sym_TA` precision above 90 % on border cells supports H4 historically for the
first time. Checkerboard class accuracy near the development 74 % on unseen
interiors supports the filler description. Letter accuracy near 23 % says the
interior letters carry little recoverable signal beyond class. None of this
can establish a generator.

## Exposure

Before this protocol was written, a context dump of the cached HTML around
chapter 5 displayed the full Dehn reading for 5/1 and the first rows of the
Dehn reading printed beside 5/2, plus Dehn's caption order for chapter 5.
Squares 5/1 and 5/2 are scored but flagged `seen_before_freeze`. No model
here was tuned on them: the filler statistics come from Mathers complete
squares only.
