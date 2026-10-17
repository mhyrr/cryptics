# 13-shared-strings — is the T1 × T2 excess robust, or chosen after looking?

## Question

Is the excess of strings shared by T1 and T2 robust, or an artefact of choosing n and the statistic after looking?

`02` counted distinct shared 4-grams (9 against 2.2 from shuffles, p = 0.001). It picked n = 4 and the
"distinct shared n-gram" statistic after seeing the text. This experiment fixes a battery of statistics in
advance, runs it under three nulls, and corrects for the choice with a min-p family-wise test.

## Observation that came first (E4)

The main thread saw these patterns before this test was written:

- (a) Both final groups begin REF: T1 group 123 `REFLX`, T2 group 32 `REFUD`.
- (b) T2's first 12 letters `NOCUOAPMOEPM` hold three of the seven shared 4+-letter runs: NOCU (T1 position 17),
  OEPM (T1 42) and APMOEP (T1 263).

E4 tests them, but they were seen first. Their p values are leads, not findings.

## Pre-registered readings

Copied verbatim from the dispatch, before any code was run.

- If the family-wise p stays < 0.01 under nulls (i) and (ii), the excess is robust: a mechanism is required, and no tested family supplies one (07).
- If the family-wise p is 0.01–0.05, the excess is "suggestive, not established", and work aimed at the shared strings is demoted.
- If the family-wise p ≥ 0.05, the 02 result was an artefact of choosing n and statistic after looking; canon changes to "shared strings at chance after correction".
- If reversed matches are in excess and forward matches are not, a reversed-reading component is suggested; it conflicts with Bourdeau's exclusion of reversed systems, and the conflict is recorded rather than resolved.
- If null (iii) gives a materially higher family-wise p than null (i) (factor ≥ 3), the shuffle null is too strict for Spanish-skewed text and the realistic null governs.
- E4 results are leads, not findings, whatever their p, because the pattern was seen first. They can motivate a pre-registered test on new data only.

## Method

`shared.py`, Python 3.11 standard library, fixed seeds (20261016 plus null and replicate index, so results do not
depend on the worker count). Positions are 0-based, as in `02`.

**E1, the battery.** Four match modes, T1 against T2:
- `fwd`: exact, T1 against T2 (the `02` statistic), n = 3–8.
- `rev`: exact, T1 against reverse(T2), n = 3–8.
- `ham`: at most one mismatch (Hamming distance ≤ 1, exact matches included), n = 4–8.
- `gap`: at most one interior insertion or deletion, n = 5–8. An n-letter string of one telegram matches n + 1
  consecutive letters of the other with one interior letter skipped. Exact matches are included.

For each mode and n, the script counts distinct shared pairs of strings. For `fwd` and `rev` this is the number of
distinct shared n-grams. For each mode it also finds the longest shared run. It also counts independent runs: matches
that overlap in both telegrams on the same diagonal are merged into one run (for `gap`, diagonals one apart).
`fwd` runs at n = 4 are the seven runs of `02`'s note.

**E2, the nulls.**
- (i) Independent letter shuffles of each telegram (`02`'s null).
- (ii) Bigram-preserving shuffles of each telegram. The Altschul–Erickson Euler-path method draws a random
  last-exit tree with Wilson's algorithm, shuffles the other exits, and walks. Every replicate is checked to have
  exactly the telegram's bigram counts (so also its first and last letter and its 2-gram self-repeats).
- (iii) Two independent held-out Spanish telegraph texts from `01-solver/plaintext.py` `telegram()` (615 and
  160 letters), each under its own random transposition (a uniform random permutation of positions). This is a
  letter shuffle of a Spanish text. It frees the letter counts, which nulls (i) and (ii) fix at the observed ones.

Replicates: 20,000 for (i), 20,000 for (ii), 10,000 for (iii). The task floor was 5,000, 5,000 and 2,000.
The extra replicates were cheap (about 7 ms each).

**E3, look-elsewhere.** The primary battery (A) has 25 statistics: distinct counts for every mode × n, plus the
longest run in each of the four modes. Each p is an upper tail, (1 + count ≥ observed) / (N + 1). For the
family-wise p, the observed vector joins the N null replicates (they are exchangeable under the null). Each member's
p values are computed against that same pooled sample, and each member's minimum p over the battery is taken. The
family-wise p is the share of members whose minimum p is at or below the observed one. Secondary families: (B) A plus
the 21 independent-run counts; (C) `02`'s own four statistics (fwd distinct, n = 3–6); (D) forward only; (E) reversed
only.

**E4, post hoc.**
- (a) First, the exact probability under null (i) that the two final groups share their first three letters.
  The look-elsewhere version takes the first four and last four groups of each telegram. It counts group pairs with
  at least 3 of 5 aligned letters agreeing, two ways: the 8 rank-aligned pairs (group k with group k from the start,
  group −k with group −k from the end) and all 64 pairs among those groups. Both are calibrated by null (i).
- (b) The number of forward 4+-letter runs whose T2 start lies in T2[0:12]. It is compared with a binomial
  (observed run count, starts uniform on 0–156), with a scan version (any 12-letter window of T2), and with null (i)
  directly. Null (i) conditions on nothing, so it also carries the overall excess.

**E2b, added after seeing E3 (not pre-registered).** Null (ii) fixes each telegram's own bigram counts. If the
two telegrams' bigram profiles resemble each other, null (ii) carries that resemblance into every replicate.
E2b measures that overlap, Σ c1(b) c2(b) over bigrams b, against null (i). It then rebuilds null (ii) from altered
copies of T2 (4,000 replicates each) and keeps the observed statistics unchanged. In the 'runs broken' copies the
letters at the 27 T2 positions inside the seven forward runs are permuted among themselves. In the 'control' copies
the same is done at 27 random other positions. Three seeds each.

## Run

`python3 -I shared.py --reps 20000 20000 10000 > result.txt` from this folder. A fresh run takes about 1:45 wall
for the three nulls and 1:00 for E2b on 7 workers (8-core machine), about 15 CPU minutes in all. Per-replicate rows
are cached in `out/null_{i,ii,iii}.json` (gitignored), so a rerun only redoes E2b. Without `--reps` it runs the task
floor of 5,000 / 5,000 / 2,000 replicates.

## Result

All numbers are from `result.txt`. Positions are 0-based.

**E1, observed** (distinct shared / independent runs):

| n | fwd | rev | ham ≤ 1 | gap ≤ 1 |
|---|---|---|---|---|
| 3 | 37 / 37 | 23 / 24 | – | – |
| 4 | 9 / 7 | 4 / 3 | 134 / 84 | – |
| 5 | 2 / 1 | 1 / 1 | 21 / 13 | 5 / 4 |
| 6 | 1 / 1 | 0 / 0 | 3 / 1 | 1 / 1 |
| 7 | 0 | 0 | 2 / 1 | 0 |
| 8 | 0 | 0 | 0 | 0 |
| longest run | 6 (APMOEP) | 5 (ORAEA / AEARO) | 7 | 6 |

The forward counts reproduce `02` exactly (37, 9, 2, 1; seven runs). The 7-letter near-match is APMOEP plus one
flanking letter (EAPMOEP / OAPMOEP). Two of the five gapped 5-letter matches extend forward runs by one skipped
letter: RAEAT / RAEA·ET and ISEEN / ISEE·RN. A third is new, AFEEN / AF·HEEN.

**E3, family-wise p** (min-p over the battery):

| battery | null (i) shuffle | null (ii) bigram-preserving | null (iii) Spanish, transposed |
|---|---|---|---|
| **A primary, 25 stats** | **0.0076** | **0.052** | **0.020** |
| B, A + 21 run counts | 0.013 | 0.078 | 0.028 |
| C, `02`'s own (fwd distinct n 3–6) | 0.0029 | 0.017 | 0.0072 |
| E, reversed only | 0.24 | 0.35 | 0.29 |

The minimum p comes from the same statistic under every null: **fwd_d4**, distinct shared 4-grams. That is the
statistic `02` reported. Its single-statistic p is 0.0013 under (i), 0.0081 under (ii) and 0.0030 under (iii).
Monte Carlo standard errors on the A row are about 0.0006, 0.0016 and 0.0014. Null (iii)/(i) = 2.6.

**E3, selected single statistics** (observed; null mean, p):

| stat | obs | (i) | (ii) | (iii) |
|---|---|---|---|---|
| fwd_d3 | 37 | 26.1, 0.014 | 31.3, 0.11 | 28.4, 0.068 |
| fwd_d4 | 9 | 2.18, 0.0013 | 3.28, 0.0081 | 2.53, 0.0030 |
| fwd_d5 | 2 | 0.16, 0.020 | 0.27, 0.041 | 0.18, 0.023 |
| fwd_d6 / fwd_L | 1 / 6 | 0.011 | 0.021 | 0.012 |
| fwd_r4 (runs) | 7 | 2.07, 0.0058 | 3.15, 0.040 | 2.40, 0.015 |
| rev_d4 | 4 | 2.17, 0.19 | 2.90, 0.33 | 2.54, 0.26 |
| rev_d5 / rev_L | 1 / 5 | 0.13 | 0.19 | 0.16 |
| ham_d5 | 21 | 10.4, 0.016 | 14.5, 0.11 | 12.1, 0.058 |
| ham_d7 | 2 | 0.07, 0.014 | 0.12, 0.027 | 0.09, 0.017 |
| gap_d5 | 5 | 1.29, 0.029 | 2.02, 0.085 | 1.56, 0.048 |

**E2, self-repeats** (distinct n-grams seen twice or more within one telegram; observed, then null means):

| | obs | (i) | (ii) | (iii) | P(ii ≤ obs) |
|---|---|---|---|---|---|
| T1, 3-grams | 45 | 50.2 | 53.8 | 55.9 | 0.050 |
| T1, 4-grams | 3 | 4.25 | 5.12 | 5.21 | 0.25 |
| T2, 3-grams | 3 | 4.09 | 4.83 | 4.40 | 0.23 |
| T2, 4-grams | 0 | 0.30 | 0.39 | 0.34 | 0.68 |

Null (ii) keeps the 2-gram self-repeats exactly (139 and 29) by construction. It roughly keeps T2's 3- and
4-gram counts and T1's 4-gram count. It overstates T1's 3-gram self-repeats, 53.8 against 45 observed, at the lower
5% tail. Null (ii) text is clumpier than T1 itself.

**E2b, does null (ii) carry the shared strings?** (post hoc)

The two telegrams' bigram profiles overlap more than shuffles allow: Σ c1(b) c2(b) = 541 against 470.9 under (i),
p = 0.0013. The number of distinct shared bigrams is at chance (84 against 86.8). The excess sits in vowel pairs:
EE +52 (14 in T1 × 5 in T2), EA +26, OA +17, then NO +14, AI +9. Doubled letters overall are at chance (T1 45 against
42.7; T2 12 against 11.3).

| T2 variant used to build null (ii) | overlap | mean fwd_d4 | p(fwd_d4 = 9) | family-wise p (A) |
|---|---|---|---|---|
| original | 541 | 3.28 | 0.0081 | 0.052 |
| runs broken, 3 seeds | 503 / 526 / 521 | 2.58 / 2.96 / 2.92 | 0.002–0.005 | 0.014 / 0.030 / 0.027 |
| control, 3 seeds | 506 / 515 / 541 | 2.67 / 2.96 / 3.27 | 0.003–0.009 | 0.018 / 0.024 / 0.061 |

Breaking the runs moves null (ii) no more than permuting 27 random positions does. The overlap that inflates
null (ii) is spread across T2. It is not carried by the seven shared runs.

**E4, post hoc** (leads, not findings):

| check | observed | p |
|---|---|---|
| (a) final groups share first 3 letters (REFLX / REFUD), exact under (i) | yes | 0.00033 (1 in 2,991) |
| (a) 8 rank-aligned group pairs, first 4 and last 4 groups, with ≥ 3 aligned letters agreeing | 1 | 0.022 (i); 0.027 (iii) |
| (a) all 64 pairs among those groups | 1 | 0.17 (i); 0.20 (iii) |
| (b) run starts in T2[0:12], given 7 runs, uniform starts (binomial) | 3 of 7 | 0.012 |
| (b) any 12-letter window of T2 holding ≥ 3 of 7 starts (scan) | 3 | 0.35 |
| (b) ≥ 3 run starts in T2[0:12], null (i) directly | 3 | 0.0012 |
| (b) any 12-letter window with ≥ 3 run starts, null (i) directly | 3 | 0.028 |

The null (i) rows for (b) carry the overall excess of runs as well as their position.

## Reading (script author's reading)

The main thread judges. This is how the script author reads it against the pre-registered readings.

- **Robust (< 0.01 under (i) and (ii)): not met.** Null (i) gives 0.0076, but null (ii) gives 0.052.
- **The nulls straddle the 0.05 line.** Null (iii) gives 0.020, inside the "suggestive" band. Null (ii) gives
  0.052 ± 0.0016, just on the "artefact" side, and 0.078 with the run counts added (battery B). No null puts the
  family-wise p clearly at or above 0.05.
- **Null (iii) does not govern.** It is 2.6 times null (i), under the pre-registered factor of 3.
- **Reversed reading: does not apply.** Forward matches are in excess and reversed ones are not (family E,
  p 0.24–0.35). Nothing here conflicts with Bourdeau's exclusion of reversed systems.
- **One statistic carries the excess, the one `02` chose:** distinct shared 4-grams. Near-match modes add little
  that is independent. The 7-letter Hamming match is APMOEP with a flanking letter. Two of the five gapped matches
  extend existing runs.
- On balance this reads as the middle case: **"suggestive, not established."** The excess survives correction
  under the nulls that fix letter counts (i) or draw Spanish-like counts (iii). It fails under the bigram-preserving
  null by a hair.
- E2b says why null (ii) is harder. The telegrams share a diffuse excess of vowel pairs (EE, EA, OA). It is not the
  seven runs, and it is itself unusual under (i) (p = 0.0013, found after looking). One question decides between
  "suggestive" and "artefact": is that overlap a nuisance to condition on, or part of the same phenomenon? That
  question is the main thread's.
- E4 (a) and (b) look small only before look-elsewhere: REF at both ends is 1 in 2,991. Over the 64 group pairs
  the p is 0.17, and the scan for the T2 opening gives 0.35. They are leads for a test on new data, nothing more.

## Caveats

- Null (ii) is not a neutral, stricter null. It fixes each telegram's bigram counts, and those counts carry a
  cross-telegram vowel-pair overlap (E2b). Its texts are also clumpier than T1: 53.8 3-gram self-repeats against
  45 observed.
- The battery was fixed by the dispatch, which was written after `02`. The family-wise p corrects only within
  these 25 statistics. Other choices are not covered: n beyond 8, positional or alignment statistics, other
  definitions of near-match. The statistics are strongly correlated, so the correction is mild; Bonferroni would
  give 25 × 0.0013 = 0.033 under (i).
- Null (iii) uses the telegraphese proxy of `01-solver/plaintext.py`. It does not model the X and F excesses of
  `08`. A random transposition of a text is the same as a letter shuffle of it, so (iii) differs from (i) only in
  letting letter counts vary.
- `ham` and `gap` include exact matches by definition. `gap` allows only one interior skipped letter.
- p values pool the observed with the null replicates, which is conservative by 1/(N + 1). The longest-run
  statistics are coarse because they take few values.
- E2b and the vowel-pair overlap were found after seeing E3. E4 patterns were seen before the test. Both are leads.
- This experiment tests no mechanism, key or reading.
