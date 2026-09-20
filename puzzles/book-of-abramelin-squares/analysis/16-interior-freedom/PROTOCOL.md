# 16 — Is the interior letter free? Protocol, frozen before the run

Date: 2026-09-20. This file, `princes.json` and `run.py` are committed before
`run.py` is executed. The run writes `results.json`. Nothing here is edited
after the run; corrections go in the README under a dated heading.

## Question

H16's second clause says: inside the vowel or consonant class, the interior
letter is a free choice. NEXT.md makes this the fork between end state A (a
generator exists) and end state B (seeds, symmetry, free filler). Each test
below could refute the clause.

## Data

- `sources/mathers-squares.json`. Squares with n >= 4 and n rows of length n.
  Letters upper-cased; cells that are not A–Z are blank. Vowels are AEIOU.
- A square whose rows equal an earlier square's rows is dropped (duplicate).
- Interior cell: 0 < i < n-1 and 0 < j < n-1.
- Orbit: the set {(i,j), (j,i), (n-1-i,n-1-j), (n-1-j,n-1-i)}. Symmetry copies
  a letter around its orbit, so the orbit is the unit of choice. An orbit's
  letter is the letter of its first visible cell in sorted order; that cell is
  the orbit's representative. Orbits with no visible cell are skipped.
- Dehn pairs: `13-dehn-witness-test/dehn-readings.json`, with the frozen gate
  of experiment 13 (same id, same size, visible agreement at least half),
  through `score.agreement`. The post hoc realignment is a secondary run.

## Exposure

The main thread has seen all of Mathers and Dehn chapters 1 to 14. It knows
these figures already: letter filler 32 % against 25 %; 39 % of interior
letters occur in the top row; R at row two, column two in 14 of 35 complete
5 × 5 squares; raw disagreement 28/298, 53/567, 71/563. The tests are therefore
discovery tests with controls, not blind tests. The Warburg square letters are
unread.

## Tests. Random seed 20260920 throughout.

**T1 chapter preference.** Context = chapter. Statistic: leave-one-square-out
log loss (bits per orbit) of the context model defined below. Control: permute
chapter labels over squares, 1,000 times. p = share of permutations with loss
at or below the observed.

**T2 prince preference.** Context = prince group from `princes.json`. Same
statistic and control.

**T3 seed-letter reuse.** Statistic: share of interior orbit letters that
occur in their own square's top row (squares with a complete top row).
Control: exchange top rows among squares of the same size, 2,000 times.
Reported for all orbits, and separately for vowels and consonants.

**T4 AREPO.** 5 × 5 squares whose cell (row 2, column 2) is a visible
consonant. Statistic: how many have R there. Control: inside each square,
permute letters among the visible interior consonant orbit representatives,
2,000 times. Reported with and without squares whose row two is AREPO or
whose top row is SATOR or ROTAS.

**T5 witness disagreement.** Cells visible in both witnesses, zones top row,
other border, interior. Statistic: interior disagreements. Control: inside
each square pair, permute the disagreement flags over the visible cells, 5,000
times. This holds each square's own error rate fixed, so a badly aligned pair
cannot drive the result. Two variants: interior against all border cells, and
interior against top row only. One-sided p for interior excess. Secondary:
the same after `score.realign`.

## Entropy

Letter entropy per orbit, given the letter's own class.

- Plug-in H(letter | class) with the Miller–Madow correction, for interior
  orbits and, for reference, for top-row cells.
- Cross-validated log loss, leave one square out. Base model M0: class-level
  letter counts with 0.5 added per letter of the class (5 vowels, 21
  consonants). Context model: p = (count in context + 5 × M0) / (n in context
  + 5). The constant 5 is fixed here and not tuned.
- Contexts: M1 chapter; M2 prince; M3 seed weight (M0 multiplied by λ for
  letters in the square's top row, renormalised inside the class, λ chosen per
  fold from 0.5 to 5.0 in steps of 0.25 by training likelihood); M4 position
  (on main diagonal or not, ring one or deeper); M5 the letter above the
  representative; M6 the letter up-left of it; M7 square size.
- For every model: bits per orbit, top-one accuracy, and for M4 to M7 a
  permutation p (M4: positions permuted among same-class orbits inside the
  square; M5, M6: context values permuted among orbits of the same class; M7:
  labels permuted over squares), 500 permutations.

## Reading the result, fixed now

- The evidence **keeps A alive** if any model M1 to M7 reaches top-one
  accuracy of 0.50 or lowers cross-validated entropy by 1.0 bit per orbit
  against M0.
- The evidence **supports B** if every model lowers entropy by less than
  0.5 bit and stays under 0.40 top-one accuracy.
- Anything between is reported as undecided.
- A significant small effect is a tendency of the compiler. It goes into the
  frozen Warburg model if it lowers cross-validated loss. It does not make a
  generator.

T5 reads this way: an interior excess says copies drift more where neither
symmetry nor a known word lets a copyist check a letter. No excess says
nothing about freedom. Dehn is an edited text and may have corrected borders
by symmetry, which would move the border rate in either direction.
