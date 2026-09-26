# 25 — Blind test of the frozen construction recipe on Dresden N 111. Pre-registration

Frozen 2026-09-26, before any of physical pages 246–297 is downloaded or
viewed by anyone in this project. Greg approved the full remaining Book IV.
This file and `access.py` are committed before acquisition. The locator
inventory, the crops manifest and `score.py` are each committed before the
step that depends on them. Nothing here is edited after a step runs;
corrections go in the README under a dated heading.

## The claim under test

The recipe: a seed word in the top row; a frame and interior completed by
transpose plus half-turn symmetry; interior cells alternating vowel and
consonant (the checkerboard of experiment 13); and inside its class, a letter
that no tested context predicts (experiments 16, 23, 24). The predictions
below were computed from Mathers alone and frozen in earlier commits, before
these pages existed in the project:

| File | sha256 | Frozen in |
|---|---|---|
| `13-dehn-witness-test/predictions.json` (sym_TA, class_checkerboard, letter_filler, letter_global) | `3cbf9b90…ec0c` | experiment 13 |
| `20-warburg-witness/predictions.json` (letter_chapter) | `97fb0cad…cfe8` | `a4e2ad6` |
| `24-square-palette/predictions.json` (class_mode, palette) | `32ef3c0c…f5` | `27b8aba` |

The full hashes are pinned in `freeze.json`. The scorer refuses to run if
any differs.

## Cohort

Physical images **246–297** of Mscr.Dresd.N.111 (METS labels 243–294), all
remaining pages of Book IV as far as the METS sequence shows, taken whole.
Pages 243–245 (experiment 22) are not reused. Pages without letter grids are
recorded as such. PRIMARY — [SLUB record](https://digital.slub-dresden.de/id364474017),
image URLs from the pinned `sources/dresden-n111/page-index.json`.

## Procedure

1. **Acquisition.** `access.py --fetch` downloads the 52 original JPEGs to
   the ignored cache and writes `image-manifest.json` with sizes and hashes.
   The main thread does not view them.
2. **Locator pass.** Fresh Opus agents see only page images, the preceding
   page for context, and `LOCATOR-INSTRUCTIONS.md`. They transcribe no grid
   letters. Per grid: stable id `pPPP-cC-gG` (column left to right, grid top
   to bottom), book, chapter, item number as written, the short heading as
   written, a coarse normalized bounding box, and the number of rows and
   columns. Traversal runs down each column, then right. The merged inventory
   is checked for chapter/item continuity and committed before any reader runs.
   Chapter numbers are never inferred from letters.
3. **Crops.** `crop.py` cuts each located grid from the native image with
   5 % padding using macOS `sips`; hashes go to `crops-manifest.json`.
4. **Reading.** For each page batch, two fresh Opus agents (A and B) read the
   same crops against the same locator worklist, isolated from each other,
   from every other witness and from all predictions, following
   `READER-INSTRUCTIONS.md`. Literal transcription: uppercase Latin letters,
   `?` uncertain, `.` explicitly empty cell. J and I, U and V as written. No
   repair by symmetry, words, memory of any edition or of Abramelin itself.
   Uneven rows are kept.
5. **Scorer freeze.** `score.py` and its synthetic tests are committed before
   reader outputs are opened by the main thread.

## Consensus and alignment

- A cell is read when readers A and B give the same letter. Conflicts and `?`
  stay unknown and are never resolved by a model.
- A grid enters scoring only if both readers give the same row-length vector
  and it is n × n with n ≥ 4.
- **Primary join:** Dresden book IV chapter c item k ↔ Mathers `c/k`, with
  experiment 20's frozen gate: same n, letters agree on at least half of the
  cells lettered in both.
- **Secondary join, declared now:** experiment 13's `realign` rule (same
  chapter, unique best agreement on Mathers-visible cells, at least half).
  It uses no Mathers-blank cell.

## Targets and measures

Target = a Mathers-blank cell (as in each prediction file) whose Dresden
consensus is a letter, in a joined grid. Border and interior as in experiment 13.

- **M1** symmetry (sym_TA) precision on border targets; abstentions reported.
- **M2** checkerboard class accuracy on interior targets.
- **M3** top-one letter accuracy on interior targets for class-mode
  (letter_filler), chapter (letter_chapter), global, and palette (experiment
  24, with the checkerboard class; and given the true class).

Cells in one square are not independent. Intervals are percentile intervals
from 2,000 bootstrap resamples of joined squares, random seed 20260926.
Orbit-level counts are reported beside cell counts.

## Decision rule (primary join)

Minimum: 50 interior and 30 border targets, else **too few targets**.

- **Frame fails** if M1 < 0.70. **Class fails** if M2 < 0.60.
- **Generator signal** if any letter model reaches M3 ≥ 0.50
  (experiment 20's rule A).
- **Recipe holds** if M1 ≥ 0.80, M2 ≥ 0.70 and every letter model M3 < 0.40
  (experiment 20's rule B plus the frame).
- Otherwise **undecided**.

Forecasts, stated so they can miss: M1 0.85 (0.75–0.95); M2 0.80
(0.70–0.88); class-mode letter 0.25 (0.18–0.35). These are forecasts from
the Dehn and Warburg scores; the pilot's two grids gave class 27/50.

## Secondary, declared now

- **S1 seed alternation** (Kollatsch's observation, quantified): M2 is higher
  in squares whose Mathers top row alternates vowel and consonant at every
  step than in the rest. One-sided permutation of the label over joined
  squares, 5,000 draws.
- **S2 palette against class mode**, given the true class: exact sign test on
  discordant interior target orbits, as in experiment 24.
- **S3 transmission** (H24): Mathers against Dresden disagreement on cells
  lettered in both, by zone; interior excess with flags permuted inside each
  square pair, 5,000 draws, as in experiment 16 T5.
- **S4** the secondary join, M1–M3 again.
- **S5** reader agreement: shapes, letters, conflicts, unknowns.
- **S6** J→I normalized copy of M1–M3.

## Exposure and independence

The main thread has read all of Mathers, Dehn chapters 1–14, the Warburg
readings and Dresden pages 243–245. It has not seen pages 246–297. The
prediction files were written before this cohort was acquired, so no
prediction can have been fitted to these pages. The readers are Opus models
whose training may include printed editions of Abramelin; they are told to
transcribe literally, and model-memory contamination remains a limit.
Dresden shares the German tradition with Warburg and Dehn's sources;
agreement with them is not historical independence. Readers are one model
family; their agreement is not an adjudicated edition.

## What would not follow

Recipe holds: the construction is characterized to its residue, not proven
to be free choice. Generator signal: a context predicts letters, and a new
dive into that context opens; it is not yet a rule.
