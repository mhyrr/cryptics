# 24 — Does a square reuse its own interior letters? Protocol, frozen before the run

Date: 2026-09-26. This file, `run.py` and `test_run.py` are committed before
`run.py` is executed on historical data. The run writes `predictions.json`
(from Mathers only) and then `results.json`. Nothing here is edited after the
run; corrections go in the README under a dated heading.

## Question

H27: inside one square, interior orbits share letters with each other beyond
what the letter frequencies of the square's chapter and the square's
vowel/consonant pattern predict. The square has its own palette.

If true, a hidden interior letter is predictable from the square's other
interior letters. Experiment 16 tested chapter, prince, seed, position, size
and the neighbouring cell as contexts. It did not test the square's other
interior orbits. A palette that predicts witness letters would refute H16's
second clause in its strong form (the letter is free inside its class).

## Data

- **Mathers:** `16-interior-freedom/run.py:load()` and `orbits()`, unchanged.
  Chapter = the number before the slash. The orbit's cell set is the four
  images of its representative under transpose and half-turn.
- **Witnesses**, used only in part B:
  - **W:** `20-warburg-witness/warburg-squares.json` `grid`, id `chapter/number`,
    experiment 20's frozen gate: same n, n × n, letters agree on at least half
    of the cells lettered in both.
  - **D:** `13-dehn-witness-test/dehn-readings.json`, experiment 13's frozen gate
    (same id, n × n, every cell a letter, agreement at least half on
    Mathers-visible cells); first passing record per id.
  - **R, Dresden:** `22-dresden-witness-pilot/posthoc-collation.json`, a cell is
    read only where readers A and B agree; id `source_id`; experiment 20's gate.
- **Denominator check:** the extraction must reproduce the interior target
  cells of the earlier frozen scores: W 349, D 193, R 50. If it does not, the
  part B verdict is withheld and the difference is reported.

## Motivating squares

The idea came from experiment 23's named list: 17/3 HOLOP, 16/20 ORIMEL,
22/1 QELADIM, 16/19 ARITON, 18/10 ROGAMOS (for example KOROK, IRORA, ARORI).
These five are excluded from parts A and C. Sensitivity run S1 restores them.
Part B's targets are witness cells blank in Mathers; none of these five was
compared letter by letter with a witness in forming the idea.

## Part A — repetition inside squares (discovery, Mathers)

Items: squares with at least two visible interior orbits.
Statistic **Rep** = Σ over squares, Σ over letters, C(count, 2): the number of
same-letter pairs of interior orbits in the same square. **Rep_far** counts
only pairs whose orbits have no two cells that share an edge.

Primary null: within each chapter and class (vowel AEIOU, consonant), permute
orbit letters across the orbits of that chapter. Each square keeps its number
of orbits and its class pattern; each chapter keeps its letter counts.
5,000 permutations, random seed 20260926; one-sided p = (1 + #{null ≥ obs}) / 5,001.
Secondary nulls: within class only (corpus-wide); within chapter × size × class.

## Part C — how many bits (discovery, Mathers)

Leave one orbit out. For a held orbit of class c in square s: palette counts nₗ
over the other visible orbits of s in class c, N = Σ nₗ; base M0(ℓ | c) is
experiment 16's leave-one-square-out class distribution (`base_probs`).
P(ℓ) = (nₗ + K·M0(ℓ | c)) / (N + K). K is chosen from
{0.25, 0.5, 1, 2, 4, 8, 16, 32, 64} by lowest mean loss; K = ∞ is M0.
Report bits per orbit for M0 and the chosen K, top-one accuracy for both, and
the same gain on 200 within-chapter permuted corpora (primary null of part A)
with K chosen the same way. Gain = loss(M0) − loss(K).

## Part B — frozen prediction, scored on witnesses

Predictions for every Mathers-blank interior cell, from Mathers only:
- palette = visible interior orbits of the square in Mathers, excluding the
  target cell's own orbit;
- M0 = class letter counts over all visible Mathers interior orbits + 0.5;
- **class_mode**: argmax M0(ℓ | c); **palette**: argmax (nₗ + K·M0(ℓ | c)) with
  part C's K; ties to higher M0, then alphabetical;
- both are stored for c = V and c = C, and for the checkerboard class of
  experiment 13 where the column's top-row letter is visible.

Scoring. A target orbit is a Mathers interior orbit with at least one Mathers-blank
cell that the witness reads as a letter; its truth is the witness letter at the
first such cell in sorted order. Primary measure: top-one accuracy given the
truth letter's class, one vote per target orbit. Secondary: the same with the
checkerboard class, and cell-level counts comparable to experiments 13, 20, 22.

## Decision rule

- **H27 supported:** part A p(Rep) < 0.01 under the primary null, and in W the
  palette is right more often than class_mode on target orbits where their
  predictions differ, one-sided exact sign test p < 0.05.
- **H27 weakened:** part A p(Rep) ≥ 0.05.
- **Open:** otherwise. If W has fewer than 10 discordant target orbits, the
  witness half is reported as underpowered.
- D and R are reported with the same sign test; they share authored squares
  with W and are not independent confirmations.

## Power and calibration, fixed before the run

- **P1, planted palette.** In a random 30 % of part A's squares, redraw each
  interior orbit letter from two letters per class chosen at random from that
  square's chapter pool. Part A must give p < 0.01 with 1,000 permutations.
- **P0, homogeneous.** Redraw every orbit letter from its chapter-and-class
  pool. 20 replicates, 1,000 permutations each. Report counts at p < 0.01 and
  p < 0.05; more than 3 of 20 at p < 0.05 withholds the part A verdict.

## Exposure

The main thread has read all of Mathers, Dehn chapters 1–14, the Warburg
readings and the Dresden packet, and knows the earlier frozen scores. It has
not computed within-square repetition, palette predictions or their accuracy.
Discovery test with controls for A and C; B's predictions are a function of
Mathers only, frozen by this commit, then scored once against already-read
witnesses. B is therefore a frozen prediction on exposed readings, not a blind test.

## What would not follow

Support would not say why a composer reused letters (pronounceability,
syllable habits, a word list). A null would not establish free choice.
