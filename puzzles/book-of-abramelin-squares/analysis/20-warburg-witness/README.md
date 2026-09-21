# 20 — The Warburg print as a third witness, read once

**Result.** End state B by the original frozen rule; a stricter gate written by a
parallel session before the read fails on the print's uneven row lists (see
"Two gates"). On 349 interior
cells that are blank in Mathers and lettered in the Warburg print, the best
frozen letter model is right on 23 %; the vowel/consonant class is right on
83 %. On the print's own numbering, caption k selects the seed of square k:
17 hits against a within-chapter control of 3.5, and none at neighbouring
numbers.

Protocol, predictions and scorer were committed in `a4e2ad6` before any
subagent saw a square ([PROTOCOL.md](PROTOCOL.md)). Two independent Opus
readers per page read square-only masked pages. The main thread saw no
Warburg square before `score.py` ran, and ran it once.

PRIMARY — [Warburg Institute digitization](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
Book IV, PDF pages 324 to 378; page per square in `readings-A.json`.

## Two gates, and they disagree

Two legibility gates were written before the read. They give opposite answers,
and both are reported.

- **The original frozen gate** (`score.py`, commit `a4e2ad6`): agreed cells
  over lettered cells in regularly shaped squares. 3,887 of 3,976, 97.8 %.
  Passes. Every score in this README comes from this run.
- **The audited gate** (`score_checked.py`, written by a parallel session in
  `b8ed565`, also before the read; see [PREFLIGHT.md](PREFLIGHT.md)): it adds
  every printed position of a ragged item to the denominator as not agreed.
  3,887 of 10,083, 38.6 %. **Fails**, and by its rule no historical score is
  reported (`results-checked.json`). Its other correction, counting cells both
  readers marked `?`, changes nothing here: there are none.

Post hoc, `ragged_diagnostic.py` asks what the ragged items are. 123 of 132
are ragged in both readings; 110 have the same shape in both; on those 4,843
positions the readers agree on 95.8 %. The raggedness is how the print sets
partly filled squares, not a failure to read. Counting those agreed positions,
the audited denominator gives 8,527 of 10,083, 84.6 %.

How to hold this: the audited gate was fixed in advance and it failed, so the
Warburg scores cannot be called a clean pre-registered pass. The reason it
failed is a format assumption, not legibility, and the diagnostic that shows
this was run after the scores were seen. End state B does not rest on this
witness alone: experiment 16 and the Dehn scores of experiment 13 carry it, and
the Warburg numbers point the same way on every measure.

Exposure, from the audit: chapter 4 moon and water rows were seen in earlier
work and chapter 5 captions were development data, so not every cell is blind.
Cell counts include symmetry-related cells and are not independent trials.
The post hoc Greek reading of experiment 17 is not in this scorer.

## Reading quality

251 squares read by both readers. 119 have a regular shape in both readings
and are scored cell by cell; 132 are ragged (row words of unequal length, as
the print sets them, or read with different lengths) and count only through
their top row. On the 119, the readers agree on 3,887 of 3,976 lettered cells
(97.8 %). Disagreed cells are `?` in `warburg-squares.json` and are never scored.

## Cells blank in Mathers, lettered in Warburg (33 squares aligned by number)

| Model, frozen | Zone | Correct | Wrong | Abstain |
|---|---|---:|---:|---:|
| transpose plus half-turn (experiment 01) | border | 101 | 19 | 38 |
| same | interior | 15 | 12 | 322 |
| vowel/consonant checkerboard | interior | 288 | 61 | 0 |
| letter: class mode, A or R | interior | 81 | 268 | 0 |
| letter: chapter model (experiment 16 M1) | interior | 62 | 287 | 0 |
| letter: most common, A | interior | 58 | 291 | 0 |

Post hoc realignment inside chapters (experiment 13's code, 92 squares) gives
the same picture: symmetry 256 of 313 on borders, class 641 of 742, class mode
201 of 742, chapter model 152 of 742. The chapter habit of experiment 16 does
not transfer: it scores below the plain class mode.

## Witness disagreement, Mathers against Warburg

| Zone | Differ / cells |
|---|---:|
| top row | 27 / 193 |
| other border | 45 / 259 |
| interior | 40 / 183 |

Interior disagreements 40 against 28.6 expected when each square's own error
rate is held fixed (p 0.002; realigned 96 against 69.0, p 0.0002). Experiment
16 did not find this excess between Mathers and Dehn (p 0.13). Here it is
clear: copies drift most where neither symmetry nor a known word lets a
copyist check a letter. Where Mathers and Dehn differ, the Warburg letter
sides with Dehn 29 times, with Mathers 13, with neither 23.

## Seeds

205 top rows agreed by both readers. 39 equal an OCR transliteration of the
dictionary (control 6.8); 111 lie within one letter (control 45.6). The
expectation written beforehand, that the German print would match at or above
Mathers's 24 %, was **not met**: 19 %. Only 27 of 193 same-number pairs have
the same top row as Mathers, so the two witnesses number and spell
differently, and the print is a careless one (see the ragged rows).

## Caption to seed, per square, on the print's numbering

| Test | Observed | Control mean | Control maximum |
|---|---:|---:|---:|
| skeleton tier | 17 | 3.5 | 8 |
| skeleton, without chapter 5 | 16 | 3.4 | 10 |
| exact | 11 | 2.1 | 7 |

Offsets: caption k against square k + d gives 0, 1, **17**, 0, 0 for d from
−2 to 2. Experiment 18's spread over offsets was Mathers's renumbering, not a
loose link. Hits: 5/5 RACAB, 8/1 CANAMAL, 8/2 SAGRIR, 10/4 HORAH, 15/2 BASAR,
18/3 BUAH, 19/1 CALLAH, 19/13 BETULAH, 19/16 GEBHIR, 19/17 SARAH, 21/3 BACUR,
26/4 SEGOR, 27/8 SELEG, 27/12 IAGEB, 27/26 ANAKIM, 28/1 SEGOR, 29/2 MAHARACAH.
17 of 205 is a floor: the lookup sees about half of the printed
transliterations (experiment 19) and a third of the nominations find no entry.

## Limits

One low-resolution scan (about 100 ppi). The readers name systematic doubts:
C against E, long s against f, b against d, I and J share a glyph (mapped to I
before scoring; recorded in the protocol). Agreement between two readers of
the same model is not independence from shared bias. The first reader runs
died twice on the account spend limit and were resumed from saved files; one
first-run reader mentioned using symmetry to settle a ligature, and the
restart brief forbade it. That bias would favour the symmetry score, not the
letter models. The Warburg print belongs to the German tradition Dehn used,
so it is not independent of Dehn. It is unseen, not untouched.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/20-warburg-witness
python3 predict.py --check
python3 score.py            # rewrites results.json and warburg-squares.json from the checked-in readings
python3 test_preflight.py
python3 score_checked.py . --check   # the audited gate; reproduces results-checked.json
python3 ragged_diagnostic.py
```
