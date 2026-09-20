# 20 — The Warburg print as a third witness. Frozen before its squares are read

Date: 2026-09-20. This is the last cheap unseen witness. It is read once.
Everything below, `predict.py`, `predictions.json` and `score.py` are
committed before any subagent is shown a square. The main thread has not seen
a Warburg square page; layout was labelled by subagents that returned band
numbers only (experiment 18).

PRIMARY: [Warburg Institute digitization](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
catalogued Stuttgart 1853. The PDF's page images are about 300 × 465 pixels.
Legibility is the known risk, and the reading design answers it.

## Reading

Two Opus readers, independent, no nested agents. Each sees square crops only,
cut by code from the layout labels: no captions, no Mathers, no Dehn, no
models. Each writes rows with `.` for an empty cell and `?` for a letter it
cannot read. A cell is scored only when both readers give the same letter.
Reader agreement is reported by zone. If agreed cells are under half of all
lettered cells, the witness is declared unreadable at this resolution, that is
the named wall, and no score is reported as evidence.

## What is scored

Alignment to Mathers: same chapter and number, same size, agreement on at
least half of the cells visible in both (experiment 13's gate, its code).
Secondary: experiment 13's post hoc realignment inside the chapter.

1. **Blank in Mathers, lettered in Warburg** (the blind cells), by zone:
   - transpose plus half-turn fills (experiment 01, via experiment 13's frozen
     `predictions.json`, hash checked);
   - vowel/consonant checkerboard class;
   - letter: class mode (A or R), the experiment 13 filler;
   - letter: chapter model of experiment 16 (M1), trained on all Mathers
     interior orbits, frozen here in `predictions.json`;
   - baseline: most common letter A.
2. **End state.** Fixed now: A needs interior letter accuracy of 0.50 or more
   on at least 50 blind interior cells. B is confirmed if the best letter
   model stays under 0.40 while class accuracy is 0.70 or more. Fewer than 50
   blind interior cells: the witness cannot decide, and experiment 16 stands
   alone.
3. **Witness disagreement**, Mathers against Warburg, with experiment 16's
   T5 permutation (flags permuted inside each square pair).
4. **Seeds.** Warburg complete top rows against experiment 12's vocabulary,
   exact and near, with the `cv_shuffle` control. Expectation stated now: a
   German witness is closer to the compiler than Mathers's French source, so
   its exact rate should be at or above Mathers's 56 of 232 (24 %).
5. **Caption to seed, per square.** The Warburg print numbers captions and
   squares alike. Experiment 18's frozen German nominations, looked up by
   experiment 14's unchanged `lookup.py`, are compared with the top row of the
   Warburg square of the same chapter and number (skeleton tier). Control:
   captions permuted inside the chapter, 2,000 draws; and the by-chapter score
   for comparison with experiment 14. Chapter 5 is development data and is
   reported separately.

Nothing is tuned after the read. Post hoc looks are allowed only under a
heading that says so.

## Amendment before the read: the print's format (2026-09-20, still frozen)

The layout subagents report that only chapters 1 to 3 are ruled grids. From
chapter 4 the print gives each square as a list of row words under its
caption. Fixed now, before any reader runs:

- A reader writes each group of letters as printed, upper case, `.` for a
  printed placeholder or empty cell, `?` for an unreadable letter.
- A row list becomes a square of size n = length of its first group, its
  groups taken as rows 1, 2, … from the top. If any group has another length,
  or there are more than n groups, the item is `ragged` and is not scored
  against Mathers cell by cell. Its first group still counts as a top row.
- Rows the print does not give are blank.
- Descriptive, not a test: on cells where Mathers and Dehn differ, whether the
  Warburg letter sides with Mathers, with Dehn, or with neither.
