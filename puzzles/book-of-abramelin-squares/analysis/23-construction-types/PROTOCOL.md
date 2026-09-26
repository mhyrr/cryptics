# 23 — Are there construction types? Protocol, frozen before the run

Date: 2026-09-26. This file, `run.py` and `test_run.py` are committed before
`run.py` is executed on the historical corpora. The run writes `results.json`.
Nothing here is edited after the run; corrections go in the README under a
dated heading.

## Question

H26: the squares are not one population. A subset draws its interior letters
from the letters of its own top row (the seed) beyond chance. Call such a
square *seed-closed*.

Experiment 16's T3 found the corpus-wide seed-reuse rate at chance (35.9 %
against 35.4 %). An average at chance does not exclude a small closed subset
balanced by the rest. This test looks at the spread across squares, not the mean.

## Data

- **M, Mathers.** `16-interior-freedom/run.py:load()`, unchanged: squares with
  n ≥ 4 and n rows of length n, letters upper-cased, cells outside A–Z blank,
  duplicate grids dropped.
- **W, Warburg print.** `20-warburg-witness/warburg-squares.json`, records with
  a `grid` of n ≥ 4 rows of length n. `?` and every other non A–Z cell is
  blank. Duplicate grids dropped. Identifier `chapter/number`.
- **D, Dehn.** `13-dehn-witness-test/dehn-readings.json`, records whose rows
  form an n × n grid with n ≥ 4. First record per identifier; duplicate grids
  dropped. Same blank rule.
- **Dresden.** `22-dresden-witness-pilot/posthoc-collation.json`, reader A
  rows where both readers agree on every row; descriptive only (see below).

Orbit and representative: experiment 16's `orbits()`, unchanged. The orbit is
the set of cells that transpose plus half-turn map onto each other; its letter
is the letter of its first visible cell in sorted order.

**Eligible square:** a top row with every cell in A–Z and at least two visible
interior orbits.

## Motivating squares, excluded from the primary statistics

The hypothesis was formed after reading Dresden IV.4.3 (top row APPARET,
caption "In der Lufft", centre row AEREREA) beside IV.4.2 (ETHANIM). Every
square in any corpus whose top row is APPARET or ETHANIM, and Mathers 4/2 and
4/3, is excluded from the primary statistics. Sensitivity run S1 restores them.

## Statistic

For an eligible square s with seed σ and interior orbit letters ℓ₁…ℓₘ:

- k(s, r) = number of ℓᵢ that occur in the letter set of string r.
- kₛ = k(s, σ), the observed closure.
- References Rₛ: the distinct top-row strings of the other eligible squares of
  the same corpus and the same n, excluding strings equal to σ. A square with
  fewer than 5 references, or zero variance of k over its references, is
  excluded and listed.
- Eₛ, Vₛ: mean and population variance of k(s, r) over r ∈ Rₛ.
- zₛ = (kₛ − Eₛ) / √Vₛ.

Corpus statistics: **D** = Σ zₛ² (spread), **U** = #{zₛ ≥ 2} (closed tail),
**L** = #{zₛ ≤ −2} (avoiding tail), **S** = Σ zₛ (mean shift; the T3 analogue).

## Null

Within each size class, permute the assignment of seeds to eligible squares.
Each square keeps its interior letters, Eₛ and Vₛ; only kₛ is recomputed with
the assigned seed. The permutation keeps the seed-length and seed-alphabet
distribution of each size class and the shared use of seeds across squares.
5,000 permutations, random seed 20260926. One-sided p = (1 + #{null ≥ observed})
/ (1 + 5,000) for D, U, L and S.

## Decision rule (corpus M, primary)

- **H26 supported:** p(D) < 0.01 and p(U) < 0.01.
- **H26 weakened:** p(D) ≥ 0.05 and p(U) ≥ 0.05.
- Otherwise **open**.
- **Replicated:** the same two conditions at 0.05 in W. W shares its authored
  squares with M, so this is a second transmission and a second reading, not
  new squares. D is reported the same way; it has fewer squares and less power.

Size estimate: the excess closed tail U − mean(U under the null), with the
2.5 and 97.5 percentiles of U − U_null.

## Secondary tests (reported, not decisive)

- **A1, closure against alternation.** Checkerboard conformity cₛ: the share
  of visible interior orbits whose class equals experiment 13's rule at the
  representative cell (class V if the top-row letter of that column is a
  vowel XOR the row index is odd). Spearman ρ(zₛ, cₛ) over squares with
  m ≥ 3; 5,000 permutations of c; two-sided p. Expected sign, fixed now: ρ < 0.
- **A2, closure against dictionary seed.** Mathers squares whose top row is an
  exact hit in `12-dictionary-index/rows-in-dictionary.json` against the rest.
  Statistic: difference in mean z; 5,000 label permutations; two-sided p.
  Suspected sign, fixed now: dictionary seeds lower.
- **S1** includes the motivating squares. **S2** restricts Rₛ to references with
  the same number of distinct letters as σ where at least 5 exist, else the
  same-size set. **S3** repeats D, U, S separately over vowel and over
  consonant orbits. Each with 5,000 permutations.
- **Named list.** Every M square with z ≥ 2: seed, interior rows, k/m, E, z,
  and the z of the W and D square with the same top row where eligible.
- **Dresden, descriptive.** z for each agreed Dresden grid against the M
  references of its size. Two grids are exposed; no inference.

## Power and calibration, fixed before the run

- **P1, planted closure.** In corpus M, choose 15 % of eligible squares at
  random. In each, replace each interior orbit letter with probability 0.9 by
  a uniformly chosen seed letter of the same class, if the seed has one. Run
  the primary test with 1,000 permutations. The test must report supported.
- **P0, homogeneous fill.** Replace every interior orbit letter in M by a draw
  from the pooled M interior letter frequency of its class. 20 replicates,
  1,000 permutations each. Report how many reach the supported rule and how
  many reach p(D) < 0.05. More than 2 supported in 20 means the test is
  miscalibrated; the historical verdict is then withheld.

## Exposure

The main thread has read all of Mathers, Dehn chapters 1–14, the Warburg
readings and the Dresden three-page packet. It knows experiment 16's T3 mean
result. It has not computed per-square closure or its spread in any corpus.
This is a discovery test with controls on seen data, not a blind test.
Kollatsch's symmetry draft (CLAIMANT, pp. 22–23) already states the
vowel/consonant alternation qualitatively; A1 is a quantitative relation to
it, not a new observation of alternation.

## What would not follow

Support for H26 would not say how the closed squares were built. APPARET's
centre row AEREREA contains Latin *aere*, "air", beside the caption "In der
Lufft"; closure may be a side effect of a second word sharing letters with
the seed. A null result would not establish free choice (H16).
