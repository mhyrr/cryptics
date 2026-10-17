# 11-one-or-two — one language, one convention, one system?

## Question
Do T1 and T2 come from the same language, the same writing convention and the same system? Their odd letters
differ: T1 has 6 X and 5 F; T2 has 0 X and 7 F (`08`). T1 was handed in at 11:31 and marked "als Chiffriert
aufgegeben" ("handed in as cipher"). T2 was handed in at 17:34 with a "Cde" stamp, which may mark code language.

## Pre-registered readings
Copied verbatim from the dispatch, before anything was run. Not edited after.

- If C1's global p ≥ 0.05 and no single letter survives the min-p calibration at 0.05, one language and one letter source explain both telegrams; the X/F difference is within sampling. Joint attacks (one key on both) keep their premise.
- If F alone survives (calibrated p < 0.05) while the global test passes, the difference is content or a T2-specific convention; it does not split the system.
- If the global p < 0.01, or C2 picks different languages, the telegrams differ in language or system, and joint attacks lose their premise.
- If C4 shows group-position structure (p < 0.01) in either telegram, that telegram is not a plain letter transposition at the group level (codewords, or nulls at fixed group positions). If p ≥ 0.05, group position carries nothing, as a transposition predicts.
- C5 alone cannot split the system: a clerk's class mark is not a cryptographic fact. It is reported as context.

## Method
One script, `one_or_two.py`, Python 3.11 standard library, fixed seeds (one `random.Random` per test). It reads the
two texts from `sources/`, and for C2 and C3 imports `plaintext.telegram` from `01-solver` (held-out books,
telegraph style), as `08/fit.py` does. These definitions were fixed before the first run.

- **C1, homogeneity.** Pearson chi-square of the 2 × 26 table of letter counts, T1 against T2, with expected counts
  from the margins. W (0 in both) has no expected count and drops out, so 25 letters enter. Null: 20,000 random
  splits of the pooled 775 letters into 615 and 160 (seed 11001). p = (null ≥ observed + 1) / 20,001. Per letter:
  the two-sided hypergeometric (Fisher) p of T2's count, given the letter's pooled count; two-sided means the sum of
  every outcome no more probable than the observed one. Min-p calibration: for each split, the smallest per-letter p
  over the 26 letters; a letter's calibrated p is the share of splits whose min-p is at or below its own p.
- **C2, same language.** References built as `08` builds them: 40 chunks of 10,000 letters per language from
  `plaintext.telegram(…, style="telegraph")` (seed 12001), letter frequencies with add-0.5 smoothing so no letter has
  zero probability. The log-likelihood of a telegram's counts under language L is Σ n_c ln f_L(c) (the multinomial
  coefficient is the same for all three and drops out). Reported: each language's LL, the ranking, and
  LLR = LL(best) − LL(second). Null: 1,000 plants of each language at each telegram's length (seed 12002). For each
  plant language: the share of plants that pick each language first; the share that give the telegram's full
  ranking; and the share that pick the telegram's best language with an LLR at least the telegram's.
- **C3, same convention.** Binomial: P(0 X in 160 letters) at T1's X rate 6/615; P(≤ 5 F in 615 letters) at T2's
  F rate 7/160. Plants: 2,000 Spanish telegraph plants at 160 and 2,000 at 615 (seed 13001). From them: P(0 X at
  160), P(≤ 5 F at 615), and for the excess itself P(≥ 6 X at 615) and P(≥ 7 F at 160).
- **C4, group structure.** Group position = letter index mod 5 (1–5); 615 = 123 × 5 and 160 = 32 × 5, so every group
  is full. (a) Pearson chi-square of letter class (vowels AEIOU; frequent consonants NRSTLCDMP; rare consonants, the
  other twelve) by position, a 3 × 5 table. (b) Pearson chi-square of {X, F, K, Z, Q, Y, J} against all other letters
  by position, a 2 × 5 table. Null for each: 10,000 shuffles of the telegram's own letters (seeds 14001, 14002;
  p = (null ≥ observed + 1) / 10,001). The counts of each of the seven letters by position are printed as
  description, with no test.
- **C5, paperwork.** Quoted from `sources/headers.md`, not computed. The script does only the arithmetic: charge per
  charged word for each telegram and the ratio between them.

## Run
From this folder: `python3 -I one_or_two.py > result.txt` (about 2 minutes, nearly all of it the C4 controls).
Seed check for C1: `python3 -I one_or_two.py --seeds > seeds.txt` (about 8 s). Before the controls were added,
two runs gave byte-identical `result.txt`. Adding them left everything before the controls section unchanged.

## Result
All numbers are from `result.txt` and `seeds.txt`.

**C1, homogeneity.** χ² = 29.1 on 25 letters; split null median 23.2, 95th percentile 36.4.
**Global p = 0.212** (seeds 11001–11005: 0.212–0.220).

| letter | T1 | T2 | T2 expected (pooled) | Fisher p | min-p calibrated p |
|---|---|---|---|---|---|
| **F** | 5 | 7 | 2.48 | 0.0044 | **0.056** (five seeds: 0.056–0.060) |
| A | 58 | 23 | 16.72 | 0.081 | 0.75 |
| P | 35 | 4 | 8.05 | 0.108 | 0.86 |
| O | 69 | 11 | 16.52 | 0.143 | 0.93 |
| **X** | 6 | 0 | 1.24 | 0.355 | **1.00** |

Every other letter has Fisher p ≥ 0.22. The min-p null's 5th percentile is 0.0037. In 5.6% of random splits
some letter is at least as extreme as F.

**C2, same language** (log-likelihood in natural log; 1,000 plants per language per length).

| | LL es | LL it | LL pt | ranking | LLR best vs second |
|---|---|---|---|---|---|
| T1 (615) | −1759.10 | −1792.29 | −1763.02 | es > pt > it | 3.92 |
| T2 (160) | −454.89 | −457.02 | −455.34 | es > pt > it | 0.44 |

How often plants of each language give the telegram's outcome:

| plants | at | pick es | pick it | pick pt | same ranking | pick es with LLR ≥ telegram's | median LLR |
|---|---|---|---|---|---|---|---|
| es | 615 | 0.992 | 0.000 | 0.008 | 0.987 | 0.965 | 17.40 |
| it | 615 | 0.000 | 0.997 | 0.003 | 0.000 | 0.000 | 23.05 |
| pt | 615 | 0.015 | 0.006 | 0.979 | 0.015 | 0.005 | 16.05 |
| es | 160 | 0.900 | 0.016 | 0.084 | 0.858 | 0.877 | 4.54 |
| it | 160 | 0.018 | 0.944 | 0.038 | 0.009 | 0.014 | 5.56 |
| pt | 160 | 0.062 | 0.038 | 0.900 | 0.059 | 0.042 | 3.81 |

Both telegrams pick Spanish, with the same full ranking.

**C3, same convention.**

| quantity | value |
|---|---|
| P(0 X in 160) at T1's X rate 6/615 (binomial) | 0.208 |
| P(≤ 5 F in 615) at T2's F rate 7/160 (binomial; 26.9 expected) | 2.0 × 10⁻⁷ |
| Spanish plants: P(0 X at 160) | 0.853 (mean 0.17 X) |
| Spanish plants: P(≤ 5 F at 615) | 0.690 (mean 4.71 F) |
| Spanish plants: P(≥ 6 X at 615) | 0.0020 (mean 0.67 X) |
| Spanish plants: P(≥ 7 F at 160) | 0.0050 (mean 1.24 F) |

**C4, group structure** (10,000 shuffles each).

| telegram | (a) class × position | (b) {X F K Z Q Y J} × position |
|---|---|---|
| T1 | χ² 4.15, p = 0.85 | χ² 2.08, p = 0.80 |
| T2 | χ² 3.10, p = 0.94 | χ² 5.18, p = 0.32 |

By position 1–5: T1's X fall 1 1 1 0 3 and its F 2 0 1 2 0; T2's F fall 2 1 4 0 0. Full tables in `result.txt`.

**C4 controls (added after the first result).** The coordinator asked for these after the C4 result above was in,
so they are not pre-registered. They measure how often C4's two tests reject on plants of known structure.
`c4_controls()` in the same script builds 200 plants per family at 615 and 200 at 160 letters (seeds 17000+, 18000+):
- **Code.** Each word of telegraph Spanish (a word-level twin of `plaintext.telegram`, 123 or 32 words) is replaced
  by one five-letter codeword from a per-plant codebook, so a repeated word repeats its codeword. The codewords
  come in three kinds: uniform random letters; CVCVC (vowels AEIOU, consonants the other 21, uniform); and CVCVC
  or VCVCV, chosen 50/50 per codeword.
- **Nulls.** Spanish telegraph plaintext goes through a forward double columnar (widths 8–25, random keys). A
  uniform random null letter then goes at group position 3, either of every group or of groups 1, 3, 5, … The
  615-letter plants carry 492 and 553 real letters; the 160-letter plants carry 128 and 144.
- **Negative control.** The same double columnar with no nulls.

The plants' null distribution is the same relabelling null as above. It is drawn faster, by sampling positions for
every class but the largest, with up to 1,000 draws. A plant stops once 51 null values reach its statistic, which
leaves the decisions at 0.01 and 0.05 unchanged. On the telegrams this null (10,000 draws) gives T1 0.849 / 0.788
and T2 0.937 / 0.313, against 0.848 / 0.799 and 0.941 / 0.322 from the shuffles.

Share of plants rejected; (a) class × position, (b) {X F K Z Q Y J} × position:

| family | n | (a) p < .01 | (a) p < .05 | (b) p < .01 | (b) p < .05 | either p < .01 |
|---|---|---|---|---|---|---|
| code, uniform random codewords | 615 | 0.505 | 0.675 | 0.320 | 0.485 | 0.615 |
| | 160 | 0.085 | 0.260 | 0.070 | 0.165 | 0.130 |
| code, CVCVC | 615 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| | 160 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| code, CVCVC or VCVCV per codeword | 615 | 0.450 | 0.575 | 0.320 | 0.485 | 0.525 |
| | 160 | 0.185 | 0.275 | 0.075 | 0.160 | 0.200 |
| DC + null at position 3, every group | 615 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| | 160 | 0.910 | 0.980 | 0.725 | 0.850 | 0.925 |
| DC + null at position 3, every 2nd group | 615 | 0.960 | 0.995 | 0.915 | 0.955 | 0.985 |
| | 160 | 0.280 | 0.485 | 0.195 | 0.395 | 0.350 |
| DC, no nulls (negative control) | 615 | 0.010 | 0.045 | 0.015 | 0.035 | 0.020 |
| | 160 | 0.005 | 0.050 | 0.005 | 0.030 | 0.010 |

The negative control rejects at about the nominal rate, so the tests are calibrated. Random and mixed codewords
are caught only through repetition: a repeated word puts the same letters at the same positions.

**C5, paperwork** (quoted from `sources/headers.md`, our readings of the forms).
- T1 is on the printed form. Its stamp reads `II A* 49.90z` and its word box `125`. The left margin carries
  "als Chiffriert aufgegeben" ("handed in as cipher").
- T2 is on a plain sheet. Its stamp reads `I A* 14.00z`, with a separate `Cde` stamp and "14 fr" in pencil. The
  reverse reads `47 × 34 = 188 + 141 = 15.98`, then `16.60`. Its 34 words are 32 groups plus the 2 address words.
- T1's reverse carries partly legible sums, among them `47.–`, `9.40`, `49.90` and `59.05 (?)`.

| arithmetic | value |
|---|---|
| T1: 49.90 / 125 | 0.3992 per word |
| T2: 14.00 / 34 (stamped) | 0.4118 per word |
| T2: 15.98 / 34 (pencilled) | 0.4700 per word |
| ratio T2 / T1 per word | 1.032 stamped; 1.177 pencilled |
| T2 stamped / pencilled, 14.00 / 15.98 | 0.876 |
| 0.47 × 125 | 58.75; 49.90 / 58.75 = 0.849 |
| 0.47 × 100; 0.47 × 20 | 47.00; 9.40 (both figures appear on T1's reverse) |

## Reading (script author's reading; the main thread judges)
- **Pre-registered reading 1 applies.** The global p is 0.21, and no letter survives the min-p calibration at
  0.05. One language and one letter source explain both telegrams' counts, and joint attacks keep their premise.
- F is the near miss. Its calibrated p is 0.056–0.060 over five seeds, so it misses reading 2's threshold
  consistently, but not by much. X's difference is plain sampling: T2 would expect only 1.2 X at the pooled rate.
- Against Spanish plants each telegram has its own one-letter excess: X in T1 (P = 0.002) and F in T2
  (P = 0.005). T1's F count and T2's lack of X are ordinary Spanish (0.69, 0.85). So C3's 2 × 10⁻⁷ comes from
  T2's own F rate, which is itself the anomaly. It does not show a different convention.
- C2 does not split them. Both rank es > pt > it. T2's pick is weak (LLR 0.44 against a Spanish-plant median of
  4.5), but 86% of Spanish plants give its ranking, against 6% of Portuguese and 1% of Italian plants.
- T1 is Spanish but unusually close to Portuguese. Its 3.9-nat margin is lower than 96.5% of Spanish plants. This
  is the same marginal fit `08` found.
- **C4: group position carries nothing in either telegram** (all four p ≥ 0.32). This is what a transposition
  predicts, and it is the pre-registered reading for p ≥ 0.05.
- The controls say how much that null result excludes. For T1 it rules out CVCVC codewords and a fixed-position
  null in every group or every second group (power 0.985–1.0 at p < 0.01). It only half rules out random or mixed
  codewords (0.53–0.62). For T2 it rules out CVCVC codewords (1.0) and an every-group null (0.93). It says little
  against random or mixed codewords (0.13–0.20) or an every-second-group null (0.35). A code with
  random-letter codewords therefore stays open for T2, the telegram with the `Cde` stamp.
- C5 is context only (reading 5). The stamped charges per word differ by 3%, with T2's the higher. The 0.47 rate
  pencilled on T2 also reproduces two figures on T1's reverse. **Unverified interpretation:** both telegrams may
  first have been priced at 0.47 per word, then charged less by different factors (0.849, 0.876). If so, the
  charges by themselves do not show T2 at a separate code rate. The class marks (I, II), the routing and any
  surcharges are not understood.

## Caveats
- C1 and the binomials in C3 treat letters as independent. Real text clumps: one repeated word or name can carry
  several F's. That makes these tests anti-conservative, which strengthens the "no split" reading. The plants carry
  real clumping; the binomials do not.
- Letter counts survive transposition, so C1 and C2 speak to the plaintext's letter source, not to the key.
  "Same system" here means only that nothing in the counts requires two systems. A different key, or a different
  transposition family, under the same letter source would pass.
- At 160 letters C2 picks a plant's true language 90–94% of the time, so T2's pick has limited power.
- References and plants come from the same held-out books, as in `08`. Plants therefore fit the reference a
  little better than an independent Spanish text would.
- The plants do not model X as a stop sign, code words, nulls or proper names.
- The C4 controls were added after the first result and were not pre-registered. Their code plants are stylised.
  Real 1930s codebooks were not modelled; their codeword rules (letter differences, pronounceability) were not
  looked up. A code whose codewords stand for phrases rather than single words repeats less, so these plants
  overstate power against it. Any system whose output does not align with fixed group slots also gives
  p ≥ 0.05, so C4 is consistent with transposition but does not single it out.
- C4 runs four tests, two per telegram. None is near 0.01, so the multiplicity does not matter here.
- C5 rests on our handwriting readings in `headers.md` (two T1 figures marked "?"). The meaning of `Cde`, `I A*`
  and `II A*` is unverified. Rates and classes under the 1932 Madrid regulations were not looked up.
