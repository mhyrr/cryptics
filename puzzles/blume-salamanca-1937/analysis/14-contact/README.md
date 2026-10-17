# 14-contact — does vowel/consonant contact rule out long-key double columnar?

## Question

K1, the residual of H1/H2, cannot be attacked at these lengths. It still makes a prediction. Does either telegram
show vowel/consonant structure that K1 cannot produce? And does the T1 × T2 bigram overlap found by `13` exceed
what K1 produces?

## Candidate and its prediction

**K1:** forward double columnar transposition (CC, `01-solver/transpo.py`) of the whole text, with long keys
(w1 or w2 ≥ 16).

Under K1, ciphertext neighbours are plaintext letters about w1·w2 apart, when the first-stage columns are taller
than w2. Plaintext vowel/consonant alternation lives at distances of 1–10 letters. So K1 predicts:

- vowel/consonant class carries no short-lag structure in the ciphertext (V1a);
- the two telegrams' bigram profiles overlap only at chance (V1b);
- segments do not differ in vowel density beyond chance (V1c).

`13` found, after looking, that the bigram profiles overlap more than shuffles allow (Σ c1(b)·c2(b) = 541 against
470.9, p = 0.0013), carried by vowel pairs EE, EA, OA. This experiment tests K1's prediction in a pre-registered way.

## Pre-registered readings

Copied verbatim from the dispatch, before anything was run. Not edited later.

- If T1 or T2 gives V1a or V1c calibrated p < 0.01 under the K1 plants (null b), and the positive controls reach p < 0.01 in at least 50% of plants, K1 is refuted as a whole-text system for that telegram. The lag or window length that carries the signal is recorded as a constraint on the system.
- If V1b is < 0.01 under null (b) while V1a and V1c are at chance (p ≥ 0.05), the cross-telegram overlap is a phenomenon K1 does not produce. K1 is weakened, not refuted, because the statistic was found on this data.
- If every p is ≥ 0.05 under null (b), K1 survives this test. The vowel-pair overlap is then treated as chance, and 13's family-wise p under the bigram-preserving null is read as the artefact side.
- If the positive controls reach p < 0.01 in fewer than 50% of plants, V1a/V1c have no power here and refute nothing.

## Method

`contact.py`, Python 3.11+ standard library, fixed seeds. Vowels are A E I O U; every other letter is a consonant.
x_i = 1 if letter i is a vowel, else 0. N is the text length, p̂ its vowel share. Positions are 0-based.

These choices were fixed in this file before the first run.

**V1a, class contact.** Lag-1 counts VV, VC, CV, CC. Class autocorrelation
r(k) = Σ_{i<N−k} (x_i − p̂)(x_{i+k} − p̂) / (N p̂ (1 − p̂)), for k = 1–40 (T1) and 1–20 (T2). Each lag gets a
two-sided p, min(1, 2 · min(upper tail, lower tail)). The V1a statistic is the minimum p over lags. The calibrated
p is the share of the reference set whose own minimum p is at or below the telegram's. Given the letter counts, VV
is a linear function of r(1), so the lag-1 counts are reported but not tested separately.

**V1b, cross-telegram overlap.** S_all = Σ_b c1(b)·c2(b) over all 676 bigrams b, where c(b) counts b among a
telegram's overlapping adjacent pairs (614 in T1, 159 in T2). This is `13`'s statistic. S_VV is the same sum over
the 25 vowel–vowel bigrams. Upper tail. The V1b p used in the readings is 2 × min(p_all, p_VV), capped at 1
(Bonferroni over the two statistics). V1b was found on this data. It can weaken K1, never refute it.

**V1c, vowel-density heterogeneity.** Cut the text into consecutive non-overlapping windows of length m, from
position 0, and drop the remainder. m ∈ {5, 10, 15, 20, 25, 30, 41} (T1) and {5, 8, 10, 16, 20} (T2). Statistic:
dispersion D_m = (variance of the windows' vowel counts) / (m p̂ (1 − p̂)). D_m is two-sided. Plaintext
vowel/consonant alternation makes windows *more* even than chance, so a system that keeps short distances can show
up in either tail. The V1c statistic is the minimum p over m, calibrated as for V1a. The Wald–Wolfowitz runs test on
the x sequence (z from the counts) is reported beside it, two-sided. It does not enter the V1c minimum, because
runs = 1 + VC + CV is the lag-1 contact again.

**Nulls.** Each p is computed under two reference sets, with the same code.
- (a) 20,000 letter shuffles of each telegram. For V1b, shuffle j of T1 is paired with shuffle j of T2.
- (b) K1 plants. Telegraph-style held-out Spanish from `01-solver/plaintext.py` `telegram()`, at 615 and
  160 letters. Forward CC, w1 and w2 drawn independently and uniformly from 16–25, keys uniform random permutations.
  10,000 plants per length (the floor is 2,000). For V1b two versions:
  - (b1) plant 615-j paired with plant 160-j, independent keys and plaintexts (10,000 pairs);
  - (b2) 2,000 pairs under one key pair on both, whose plaintexts both start with the same phrase of 40–100
    letters (length uniform), drawn from `telegram()` (the floor is 1,000).
  K1 includes both. The V1b reading uses the larger of the (b1) and (b2) p values.

Per-statistic p values against a reference set of M texts are (1 + #ref ≥ obs) / (M + 1) and the same for ≤.
Each reference text's own per-statistic and minimum p are computed against the same set.

**Positive controls (power).** Systems that keep short plaintext distances, on the same plaintext source:
- letters permuted within sets of n = 5–12 (one key for every full set, the last partial set left in place;
  as `04`'s `block_inner`);
- row routes: write rows of width w = 5–15, read the rows in a random order (as `04`'s `row_perm`).

500 plants per family per length, parameter drawn uniformly. Each control is calibrated against the K1 plants (b),
exactly as a telegram is. Under (a) each control is calibrated against 1,000 shuffles of its own letters. Power is
the share of controls, both families pooled, with calibrated p < 0.01, per statistic, per length, under (b). Each
family's share and the (a) shares are reported as well.

**Diagnostics (do not enter the readings).**
- Plaintext distance between ciphertext neighbours in the K1 plants: the share of adjacent ciphertext pairs whose
  plaintext letters are ≤ 10 apart, by length.
- Excess overlap: S minus its expectation given each text's letter counts,
  E[c(ab)] = n_a n_b / N (a ≠ b) and n_a (n_a − 1) / N (a = b). Under (a) this is S shifted by a constant. Under (b)
  it removes the plants' letter-count spread.
- The bigrams that carry S (c1·c2 minus expectation).

**Changed after the smoke run, before the full run (diagnostics only).** The plant split moved from "stage-1
column height h1 > w2" to "share of neighbours ≤ 10 apart above 0.05", because at 615 almost every plant has
h1 > w2. The controls' V1c hits now report their tail.

**Added after the first full run (no randomness used, every other number unchanged).** Standard deviations for
V1b, the spread of E[S | counts] among the plants, and the plants' plaintext r(1–5) and D_5 before transposition.

## Run

`python3 -I contact.py > result.txt` from this folder. It takes 1–2 minutes wall on 7 workers, about 6 CPU minutes.
`--quick` runs a small smoke test. Per-replicate rows go to `out/full.json` (gitignored). `out/result-first.txt`
is the first full run, kept for the diff against `result.txt`.

## Result

All numbers are from `result.txt`. Replicates: 20,000 shuffles per telegram (a); 10,000 K1 plants per length (b);
2,000 shared-key pairs (b2); 500 controls per family per length. No count was cut.

**Lag-1 contact.** Neither telegram alternates. Spanish plaintext does, strongly.

| | VV | VC | CV | CC | r(1) | r(2) |
|---|---|---|---|---|---|---|
| T1 observed | 111 | 148 | 148 | 207 | +0.012 | −0.063 |
| T1 expected under shuffle | 108.7 | 149.9 | 149.9 | 205.5 | −0.002 | −0.001 |
| T2 observed | 33 | 38 | 38 | 50 | +0.033 | +0.126 |
| T2 expected under shuffle | 31.1 | 39.5 | 39.5 | 49.0 | −0.006 | −0.006 |
| plants' plaintext, before transposition (mean) | | | | | −0.544 | +0.125 |

The plaintext's mean D_5 is 0.28: its 5-letter windows are far more even than chance.

**V1a and V1c** (calibrated p; the lag or window that gives the minimum in brackets).

| telegram | statistic | null (a) shuffles | null (b) K1 plants |
|---|---|---|---|
| T1 | V1a, r(1–40) | 0.49 [k = 10, r = −0.097] | 0.56 [k = 10] |
| T1 | V1c, D_m | 0.88 [m = 15, D = 1.17] | 0.87 [m = 41, D = 1.23] |
| T1 | runs test, z = −0.32 | 0.78 | 0.78 |
| T2 | V1a, r(1–20) | 0.86 [k = 2, r = +0.126] | 0.84 [k = 2] |
| T2 | V1c, D_m | 0.14 [m = 16, D = 1.90] | 0.17 [m = 16] |
| T2 | runs test, z = −0.48 | 0.69 | 0.65 |

The smallest single-lag p is T1 r(10), 0.018 (a) and 0.021 (b). The smallest single-window p is T2 D_16, 0.047 (a)
and 0.054 (b), in the upper tail (too uneven).

**V1b** (upper tail; mean ± sd of the null).

| statistic | observed | null (a) | null (b1) independent | null (b2) shared keys and phrase |
|---|---|---|---|---|
| S_all | 541 | 471.2 ± 22.1, p 0.0008 | 519.0 ± 42.3, p 0.30 | 524.7 ± 43.3, p 0.35 |
| S_VV | 228 | 164.6 ± 24.3, p 0.0068 | 198.6 ± 36.3, p 0.20 | 200.5 ± 37.5, p 0.22 |
| **V1b = 2 × min** | | **0.0016** | **0.41** | **0.45** |
| *diagnostic:* S_all − E[S \| counts] | +69.9 | +0.1 ± 22.1, p 0.0008 | −0.1 ± 24.0, p 0.0028 | −0.3 ± 23.8, p 0.0035 |
| *diagnostic:* S_VV − E[S \| counts] | +63.3 | −0.1 ± 24.3, p 0.0068 | +0.0 ± 28.8, p 0.019 | +0.4 ± 29.0, p 0.021 |

E[S_all | counts] is 471.1 for the telegrams. For the plant pairs it is 519.1 ± 34.6, and only 7.6% of pairs are as
low as the telegrams. The bigrams that carry the excess are as in `13`: EE +51.7 (14 × 5), EA +26.2, OA +16.7,
NO +14.3, AI +8.6.

**Positive controls** (share of controls with calibrated p < 0.01).

| family | N | V1a (b) | V1c (b) | V1a (a) | V1c (a) |
|---|---|---|---|---|---|
| letters permuted within sets of 5–12 | 615 | 0.56 | 0.97 | 0.85 | 0.97 |
| rows of width 5–15, read in a random order | 615 | 1.00 | 1.00 | 1.00 | 1.00 |
| **pooled (power)** | **615** | **0.78** | **0.98** | 0.93 | 0.99 |
| letters permuted within sets of 5–12 | 160 | 0.15 | 0.43 | 0.30 | 0.48 |
| rows of width 5–15, read in a random order | 160 | 1.00 | 0.85 | 1.00 | 0.88 |
| **pooled (power)** | **160** | **0.57** | **0.64** | 0.65 | 0.68 |

Every control V1c hit is in the lower tail (windows too even): 1,624 of 1,624. The row routes are found at lag 1
and m = 5. Sets of n are found mostly at lags 1–3 and m = 5–15. At 160, V1c finds them well only for n = 5 (62 of 64)
and n = 8 (50 of 66), and half the time for n = 10.

**K1 plant diagnostics.**

| N | neighbours ≤ 10 plaintext letters apart: median / 90th pct / max | plants at p < 0.01 against the telegram's shuffles, V1a / V1c |
|---|---|---|
| 615 | 0.000 / 0.003 / 0.60 | 1.4% / 1.1% (share ≤ 0.05, n 1,950); 0.0% / 2.0% (share > 0.05, n 50; keys 24–25 × 24–25) |
| 160 | 0.025 / 0.40 / 0.91 | 1.2% / 1.9% (share ≤ 0.05, n 1,235); 1.6% / 2.2% (share > 0.05, n 765) |

## Reading (script author's reading)

The main thread judges. This is how the script author reads the result against the pre-registered readings.

- **Refutation: not met.** No V1a or V1c p under null (b) is below 0.05. The lowest is T2 V1c, 0.17. No lag or
  window carries a signal, so no constraint is recorded.
- **No power: does not apply.** Pooled power is 0.78 and 0.98 at 615, and 0.57 and 0.64 at 160, all at or above
  50%. One family is weak at T2's length: letters permuted within sets, 0.15 (V1a) and 0.43 (V1c). `05` already
  excludes it.
- **V1b below 0.01 under (b): not met.** The pre-registered V1b is 0.41 (b1) and 0.45 (b2).
- **Survival applies.** Every p under null (b) is ≥ 0.05. K1 survives this test. As pre-registered, the vowel-pair
  overlap is treated as chance, and `13`'s family-wise p under the bigram-preserving null (0.052) is read as the
  artefact side.
- **A flag on that reading.** Under null (b), raw S mostly measures letter counts, not overlap. The plants' letters
  are more concentrated than the telegrams', so their expected S is 519 ± 35 against the telegrams' 471. That
  spread (sd 42) swamps the telegrams' +70 excess. Measured against its count-based expectation (the excess
  diagnostic, declared in Method before the run but outside the readings), the overlap is rare under K1:
  p = 0.0028 (b1) and 0.0035 (b2) for S_all, 0.019 and 0.021 for S_VV, 0.0056 and 0.0070 after the same
  Bonferroni. A shared opening phrase under shared keys adds no excess (mean −0.3). With the excess statistic,
  the second reading (K1 weakened, not refuted) would apply instead. The pre-registered statistic governs. Whether
  the survival reading still stands, given that V1b had no power under (b), is the main thread's call.

## Caveats

- V1b was found on this data (`13`, E2b). Under null (a) it reproduces `13` (541 against 471.2), so it is not new
  evidence. No p here is a fresh test of the overlap.
- The readings set a power criterion for V1a and V1c only. Raw V1b under null (b) has little power, because K1
  plants let the letter counts vary.
- The plants' plaintext is `plaintext.telegram()`, a proxy. Its vowel share is 0.45, against 0.42 (T1) and
  0.44 (T2). It does not model the X and F excesses of `08`, and its letters are more concentrated than the
  telegrams'. V1a and V1c are normalised by p̂, so this matters little for them. It matters a lot for raw V1b.
- At T2's length the stated mechanism does not hold. The stage-1 columns are 6–10 letters tall, shorter than w2,
  so neighbours are not w1·w2 apart. In a median plant 2.5% of neighbours are ≤ 10 letters apart (90th percentile
  40%). The plants still show no class structure, because the short distances are mixed and their r(d) values
  cancel. The null (b) calibration stands. The "w1·w2 apart" account fits T1 only.
- K1 plants draw both keys from 16–25. K1 also covers one short key with one long key (for example w1 ≤ 15,
  w2 ≥ 16). That case was not planted.
- Each calibrated p corrects for the choice of lag or window within its family. It does not correct across the
  eight tests (V1a, V1c and runs on two telegrams, plus V1b). The lowest V1a/V1c p is 0.14, so no correction is
  needed for the reading.
- T2's largest departure (D_16 = 1.90) is in the upper tail. Every positive control departs in the lower tail.
- At 160 letters, V1a power (0.57) is close to the 50% line. It rests on the row-route family.
- This experiment tests no key and attempts no reading.
