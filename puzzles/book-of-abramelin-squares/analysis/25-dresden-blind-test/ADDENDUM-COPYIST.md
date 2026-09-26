# Addendum — the copyist's corrections. Frozen before any reading is opened

Date: 2026-09-26, after the locator inventory (`702450b`) and while the
readers run. The main thread has seen grid positions, headings and row
counts, no letters. This file and `copyist.py` are committed before any file
under `readings/` is opened.

## What the locators found

The Dresden copyist copied five squares twice: once as he found them in his
exemplar ("in libro", "ex libro legi", "Hoc infra sequens ita stetit in
libro quia sic non comparatum putavi…") and once as he thought they should
be ("Correctio mea", "mea corectio", "Sed puto fortasse sic sese habere
debere"). PRIMARY — Mscr.Dresd.N.111, pages below.

| Square | Correction | Exemplar | Shapes (rows × letters) |
|---|---|---|---|
| IV.11.3 | `p251-c2-g2` | `p251-c2-g1` | 7×7 against 5×7 |
| IV.12.4 | `p252-c1-g2` | `p252-c1-g3` | 9×9 against 8×9 |
| IV.18.3 | `p257-c3-g2` | `p257-c3-g3` | 8×8 against 7×8 |
| IV.19.6 | `p259-c2-g1` | `p259-c2-g2` | 6×6 against 6×6 |
| IV.26.2 | `p265-c3-g2` | `p265-c3-g3` | 5×5 against 5×5 |

In 11.3 the unnumbered grid carries the "I think it should be thus" note, so
it is the correction. In 26.2 the numbered grid is taken as the correction by
position; it has no "correctio" label. Already visible without letters: every
correction is square; three exemplars lack rows.

## H28

The copyist corrected squares by their symmetry: he restored missing rows
and conflicting cells so that the square reads the same across and down.

## Tests (consensus letters only: cells where readers A and B agree)

- **C1, transpose agreement.** For a grid, over pairs of cells (i, j), (j, i)
  with i < j that both exist and are read: the share that are equal. Primary:
  in how many pairs is the correction's share strictly higher than the
  exemplar's; one-sided exact sign test over pairs with a strict difference.
- **C2, how missing rows were made.** For each exemplar with fewer rows than
  its correction, align the correction's rows to the exemplar's by exact row
  identity where possible; rows of the correction with no identical exemplar
  row are *added rows*. Report the share of added-row cells equal to their
  transpose partner in the correction. Forecast: at least 0.8.
- **C3, exploratory.** Letters agreeing with Mathers (same id), on cells
  lettered in both, for correction and exemplar. No direction declared.

Five pairs cannot give a strong p (all five in one direction gives 1/32).
The result is a described historical practice with a count, not a rate.

## What would not follow

A symmetry-restoring copyist shows that a 17th-century reader perceived the
symmetry. It does not show that he knew the author's original letters; his
corrections are conjectures, like any modern editor's. For the blind test
these squares are the copyist's versions, and are reported separately in the
README.
