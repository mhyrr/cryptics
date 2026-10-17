# 09-odd-positions — where are the odd letters, and does their placement fit a transposition?

## Question
Where are the odd letters (X in T1, F in T2, and the other rare letters), and does their placement fit a
transposition of the whole text?

## Observation that came first
The main thread looked at the positions before this test was designed. These are the observations; they are
why the test exists, and the statistics below correct for having seen them (scan statistics over window length
and start, min-p over all windows and moduli, each calibrated).
- T1 has X at 0-based positions 362, 424, 440, 596, 609, 614; K at 289, 599; F at 133, 328, 535, 605, 612.
- T1's last 20 letters (595–614, `AXLNKIPLANFTULXREFLX`) hold 3 of 6 X, 1 of 2 K and 2 of 5 F.
- T2 has F at 12, 27, 32, 105, 126, 145, 157. Four of the seven sit at group position 3 (index mod 5 = 2).

## Pre-registered readings
Copied verbatim from the dispatch, before anything was run. Not edited afterwards.

- A1/A2: if the calibrated p for T1's end (A2) or scan (A1) is < 0.01 AND fewer than 1% of the A3 transposition plants reach it, the end of T1 is not part of the transposed body (an indicator, a separately enciphered tail, or nulls appended after transposition). The attack target then changes. If p ≥ 0.05, the rare letters sit where a transposition puts them and the end cluster is chance. 0.01–0.05 is suggestive only and changes nothing.
- A4/A5: if the X residue min-p (calibrated) is < 0.01 and only mechanism (b) reproduces it, X's are nulls at fixed places after transposition. If p ≥ 0.05, X's are indistinguishable from in-body letters, and position cannot separate X-as-stop from X-as-null-before-transposition; only counts can (another experiment does that). The same reading applies to T2's F.
- The same tests run on T2. Whatever T1 shows, a result that holds for one telegram and not the other is reported as such, not averaged.

## Method
Python 3 standard library, fixed seeds. `common.py` holds the shared pieces. It imports `01-solver` the way
`08-letter-fit/fit.py` does.

**Surprisal.** s(c) = −log10 p_es(c). The reference is the one `08` uses: 40 chunks of 10,000 letters from
`plaintext.telegram`, Spanish, telegraph style, with 08's seed (so the same 400,000 letters). Every count gets
+1, so W and K are finite. Rarest letters: W 3.50, X 3.04, K 2.80, Z 2.35, J 2.33, Q 2.25, F 2.15, Y 2.03,
H 2.02. Common letters sit near 1.0. Sums use round(1000 · s), so ties compare exactly.

**Null and calibration (`common.Null`).** For an observed statistic x, p = (1 + #{null ≥ x}) / (K + 1). Each
null row also gets its own p, leave-one-out. A family of statistics (all window lengths, all ends, all moduli)
is summarised by its min-p. The min-p is calibrated as the fraction of null rows whose own min-p is at least as
small. Ties count against the target, so every p is conservative.

**A1, A2 (`scan.py`).** A1: for each window length l ∈ {5, 10, 15, 20, 25, 30, 40, 50, 60}, the largest
summed surprisal over all start positions. A2: the summed surprisal of the first g and the last g groups,
g = 1–4. The null is 10,000 shuffles of the telegram's own letters.

**A3 (`scan.py`).** Plants of 615 and 160 letters. The plaintext is `plaintext.telegram`, Spanish, telegraph
style, under two letter conventions:
- `stop`: the stop word PUNTO is replaced by the letter, so the letter occurs in the body.
- `fill`: ordinary PUNTO stops, plus 1–4 copies of the letter appended before transposition.

Each plaintext is enciphered by single columnar (width 5–45, random key, incomplete last row allowed) or by
forward double columnar (widths 8–25, two random keys; `01-solver/transpo.py`). At 615 letters the letter is
X. At 160 letters it is X (as the brief says) and also F (T2's odd letter, and what A5 needs). That gives 500
plants per cell. Each plant gets its own calibrated A1 and A2 p from 1,000 shuffles. The shuffles are drawn
from a fixed bank of 4,000 random permutations, to save time. A plant "reaches" the target when its calibrated
p is ≤ the target's. The target is also rerun with the plant procedure (1,000 shuffles from the bank), for a
like-for-like comparison.

**A4 (`residues.py`).** The positions of one letter: X in T1, F in T2 (primary); F, K, and X+K+F together in
T1 (secondary, not pre-registered). There are three families of statistics, all integers:
- Residues: per modulus, the sum of squared residue counts. This is equivalent to chi-square against uniform
  for a fixed modulus and count. Moduli are 3, 5, 15, 41, 123, 205 for T1 and 2, 4, 5, 8, 10, 16, 20, 32, 40,
  80 for T2. All divide the length.
- Ends: the letter's count in the first and last g groups, g = 1–4.
- Scan: the letter's largest count in any window of length l (the A1 lengths). This family is not in the
  brief. It was added because the end cluster was seen first. An end test alone cannot correct for that; a
  search over every place can.

Each family's min-p is calibrated by placing the same number of letters at random positions, 50,000 trials
per (length, count). The brief asked for 10,000. The first run used 10,000 and gave T1's end calibrated
p = 0.0005, resting on 4 null events, so the count was raised. The first run's output is in
`out/result-residues-first-run-10k.txt`; it agrees.

**A5 (`residues.py`).** There are 1,000 plants per mechanism, at T1's length with X and at T2's length with F.
The statistics are computed on every occurrence of the letter in the plant, nulls and natural ones alike,
because the target shows no more than that.
- `a-single`, `a-double`: the letter is the stop, then single or double columnar (as A3).
- `b-every-k`: c nulls placed after transposition at o, o+k, …, with k from 5 to 120 (capped where c nulls
  must fit: 5–26 at T2's length) and o random. Here c is the target's count, 6 for T1 and 7 for T2.
- `b-grp-last`: c nulls at the last letter of every q-th group, starting at a random group.
- `b-grp-pos`: as `b-grp-last`, at a random fixed position (1–5) inside the group. This variant is not in the
  brief. It was added because T2's F lean to group position 3.
- `c-before-single`, `c-before-double`: 1–4 fillers before transposition (as A3 `fill`).
- `c-after`: 1–4 fillers appended after single columnar transposition, completing the last group.

The body of every `b` and `c-after` plant is Spanish telegraph plaintext with PUNTO stops, single columnar.
For each mechanism the table gives the fraction of plants at least as extreme as the target (calibrated
p ≤ target's) for residues (A4), ends, and the scan.

No key search and no decipherment were attempted.

**A3 at the target's resolution (`a3_summary.py`, `a3_floor.py`).** T1's A2 p sits at the floor of 10,000
shuffles. A plant's p cannot go below the floor of 1,000 shuffles (1/1001). So `scan.py`'s "A2 reach" column
for T1 is empty by construction. `a3_summary.py` compares plants with the target under the same 1,000-shuffle
procedure. `a3_floor.py` replays `scan.py`'s seeded plant stream and checks it against the stored rows. It then
recalibrates every T1 plant at the 1,000-shuffle floor with 10,000 fresh shuffles, as the target was.

## Run
From this folder, in this order:
```
python3 -I scan.py > result-scan.txt          # A1-A3, 9 min CPU; per-plant rows in out/a3_plants.jsonl
python3 -I a3_summary.py > a3-summary.txt     # reads out/a3_plants.jsonl and result-scan.txt; seconds
python3 -I a3_floor.py > a3-floor.txt         # replays scan.py's plants; 40 s CPU
python3 -I residues.py > result-residues.txt  # A4-A5, 4.5 min CPU
```
The total is about 15 minutes of CPU. Seeds are fixed in the scripts.

## Result
Files: `result-scan.txt`, `a3-summary.txt`, `a3-floor.txt`, `result-residues.txt`.

### A1, A2: rare letters anywhere, and at the ends (null: 10,000 shuffles)
| | T1 | T2 |
|---|---|---|
| A1 best window (min-p over l) | l = 20 at 595–614, p = 0.0042 | l = 40 at 10–49, p = 0.13 |
| **A1 calibrated p** | **0.019** | 0.38 |
| A2 best end (min-p over 8) | last 4 groups, p = 0.0001 | first 3 groups, p = 0.077 |
| **A2 calibrated p** | **0.0001** (the floor; 0 of 10,000 shuffles) | 0.32 |

In T1 the best window for every length from 5 to 60 lies in the last 60 letters. The scan found the end without
being told where to look. The last 20 letters `AXLNKIPLANFTULXREFLX` have a mean surprisal of 1.65, against
1.24 for the whole text. T1's ends, one by one:
- last group `REFLX`: p = 0.0063
- last 2 groups `FTULXREFLX`: p = 0.0002
- last 3 groups: p = 0.0008
- last 4 groups: p = 0.0001

T1's first four groups are unremarkable (p ≥ 0.15).

### A3: is the shuffle null fair, and do transposition plants reach the target?
Each cell has 500 plants. A plant reaches the target when its calibrated p is ≤ the target's.

| cell | A1 reach (target 0.019) | A1 ≤ 0.01 | A1 ≤ 0.05 | A2 ≤ 0.01 | A2 ≤ 0.05 |
|---|---|---|---|---|---|
| T1 single, X stop | 0.018 | 0.010 | 0.062 | 0.014 | 0.062 |
| T1 single, X fill | 0.020 | 0.010 | 0.046 | 0.010 | 0.070 |
| T1 double, X stop | 0.028 | 0.016 | 0.068 | 0.020 | 0.064 |
| T1 double, X fill | 0.004 | 0.004 | 0.046 | 0.010 | 0.064 |
| **T1 pooled (2,000)** | **0.018** | 0.010 | 0.056 | 0.013 | 0.065 |
| T2 pooled, X and F (4,000) | 0.377 (target 0.38) | 0.009 | 0.050 | 0.009 | 0.046 |

- **T1 A2 reach: 0 of 2,000 plants.** Like for like (both at 1,000 shuffles), the target is at the floor
  (0.0010), and 16 plants (0.8%) share that floor (`a3-summary.txt`). Recalibrated with 10,000 shuffles, those
  16 give p from 0.0008 to 0.024. None reaches the target's 0.0001 (`a3-floor.txt`).
- T1 A1 like for like (target 0.030 at 1,000 shuffles): 62 of 2,000 plants (3.1%) reach it.
- T2: plants reach A1 in 38% and A2 in 32% of cases, like for like.
- **Fairness.** Under transposition the shuffle p's are close to uniform for A1. For A2 they are slightly
  anti-conservative: 6.5% of T1 plants fall at ≤ 0.05, about 3 standard errors above 5%. T2 plants are on
  nominal.

### A4: residues, gaps, ends and scan of the odd letter (null: 50,000 random placements)
| | T1 X (6) | T2 F (7) |
|---|---|---|
| positions | 362, 424, 440, 596, 609, 614 | 12, 27, 32, 105, 126, 145, 157 |
| gaps | 62, 16, 156, 13, 5 | 15, 5, 73, 21, 19, 12 |
| best modulus | 3 (p = 0.38) | 5 (residue 2 four times; p = 0.097) |
| **residue calibrated p** | **0.73** | **0.28** |
| ends, best | last 4 groups hold 3 X; p = 0.0004 (exact hypergeometric 0.00055) | last 3 groups hold 2 F; p = 0.13 |
| ends calibrated p | 0.0006 | 0.26 |
| scan (any window), calibrated p | 0.070 (l = 20 at 596–615) | 0.93 |

Secondary rows (T1, not pre-registered):
| letter | residue calibrated | ends calibrated | scan calibrated |
|---|---|---|---|
| F (5) | 0.76 | 0.0031 | 0.35 |
| K (2) | 0.22 | 0.11 | 1.00 |
| X + K + F (13) | 0.85 | < 0.0001 | 0.0002 |

The X + K + F set was chosen after looking at the end, so its p's are descriptions, not tests.

### A5: which mechanism reproduces the placement? (1,000 plants each)
Each cell is the fraction of plants with calibrated p ≤ the target's. "Median c" is the median count of the
letter in the plant.

T1, letter X (targets: residues 0.73, ends 0.0006, scan 0.070)
| mechanism | median c | residues | ends | scan | residues ≤ 0.01 |
|---|---|---|---|---|---|
| a, X stop, single | 9 | 0.70 | 0.001 | 0.064 | 0.006 |
| a, X stop, double | 8 | 0.68 | 0.000 | 0.064 | 0.012 |
| b, every k-th letter | 6 | 0.51 | 0.001 | 0.10 | 0.38 |
| b, last letter of every q-th group | 6 | 1.00 | 0.001 | 0.12 | 0.96 |
| b, fixed group position | 6 | 1.00 | 0.002 | 0.12 | 0.96 |
| c, fillers before, single | 3 | 0.50 | 0.000 | 0.031 | 0.046 |
| c, fillers before, double | 3 | 0.53 | 0.002 | 0.071 | 0.005 |
| **c, fillers after (last group)** | 3 | 0.15 | **0.75** | 0.73 | 0.000 |

T2, letter F (targets: residues 0.28, ends 0.26, scan 0.93)
| mechanism | median c | residues | ends | scan | residues ≤ 0.01 |
|---|---|---|---|---|---|
| a, F stop, single | 3 | 0.23 | 0.24 | 0.72 | 0.007 |
| a, F stop, double | 3 | 0.22 | 0.22 | 0.74 | 0.008 |
| b, every k-th letter | 8 | 0.60 | 0.075 | 0.62 | 0.39 |
| b, last letter of every q-th group | 8 | 1.00 | 0.088 | 0.61 | 0.98 |
| b, fixed group position | 8 | 1.00 | 0.070 | 0.62 | 0.98 |
| c, fillers before, single | 4 | 0.28 | 0.26 | 0.76 | 0.046 |
| c, fillers before, double | 4 | 0.21 | 0.23 | 0.78 | 0.007 |
| c, fillers after (last group) | 4 | 0.086 | 1.00 | 0.84 | 0.000 |

## Reading (script author's reading)
The main thread judges. This is how the author reads the pre-registered rules against the numbers.

**T1, A1/A2.** A2's calibrated p is 0.0001, below 0.01. No transposition plant reaches it (0 of 2,000).
Taken literally, the first pre-registered reading therefore applies: the end of T1 is not part of the
transposed body, and the attack target changes.

One flag the main thread must weigh. A2 tests the ends, and the end is where the cluster was seen before the
test. The location-free test is A1. A1 gives 0.019, and 1.8% of plants reach it (3.1% like for like). By the
same rule that is "suggestive only, changes nothing". Two things count in A2's favour:
- The ends were a convention named in advance: indicators and fillers sit first or last.
- A1's scan, told nothing, put its best window at the end for every length.

Against that, the X-only scan is 0.070. The anomaly is a mix of rare letters, not X alone. In the last 20
letters, three X, one K and two F carry almost all the excess surprisal; the other 14 letters are near the
text's mean.

**T1, A4/A5.** The X residue min-p is calibrated at 0.73, so p ≥ 0.05. X's are indistinguishable from in-body
letters by residue, and nulls at fixed places (mechanism b) are not supported. Position cannot separate
X-as-stop from X-as-null-before-transposition; only counts can. The X end statistic (0.0006) is reproduced by
no in-body or fixed-place mechanism (≤ 0.2%). Only fillers added after transposition reproduce it (75%).

**T2.** Nothing is anomalous: A1 0.38, A2 0.32, F residues 0.28, F ends 0.26, F scan 0.93. The four F's at
group position 3 give p = 0.097 for modulus 5 alone, and 0.28 once all ten moduli are counted. By the
pre-registered readings, T2's rare letters sit where a transposition puts them, and its F's are
indistinguishable from in-body letters.

**The two telegrams differ.** T1 has an end anomaly and T2 does not. This is reported as two results, not
averaged.

## Caveats
- **The observation came first** (see above). A1 and the X-only scan correct for where the cluster is; A2 and
  the end columns of A4/A5 do not.
- **c-after reproduces the size of the end statistic, not its shape.** Fillers appended after transposition sit
  consecutively at the very end (`…XX`). T1's end X's are at 596, 609 and 614, with other letters between them.
  A tail that is enciphered separately, or an indicator, is a mechanism no plant here models.
- **Surprisal depends on the reference.** It is Spanish telegraph style with PUNTO stops. Under an X-stop
  reference, X would be less surprising, and A1/A2 would weaken for T1.
- **Floor plants only.** `a3_floor.py` recalibrates only plants at the 1,000-shuffle floor. A plant whose true
  p is about 0.0001 misses that floor about 10% of the time, so a reach of order 0.1% cannot be excluded. That
  is still far below 1%.
- **The plant generator's stop rate varies a lot.** Under X-as-stop the X count runs from 2 to 66 per 615
  letters. The median is 8–9, near T1's 6. The highest counts were not traced; the glossary below, whose
  entries end in full stops, is a likely source. Counts are another experiment's job.
- **The held-out Spanish corpus contains an English–Spanish glossary.** Book 27738 (*José*, a school edition)
  ends with a vocabulary (from line 7,499 of 16,381 in `01-solver/out/raw_es/27738.txt`), for example `=exasperado, --a=, exasperated, enraged, offended.`
  That is about 4% of the held-out letters (119,694 of 2,981,544). It feeds `plaintext.telegram`, so it feeds
  this folder's surprisal reference, `08`'s reference, and about 4% of plant starts. The calibrated p's here
  condition on each text's own letters, so the A3/A5 fractions should be robust. The surprisal weights and
  `08`'s expected counts move a little. Not fixed here: `01-solver` is not this folder's.
- **A3 shares one permutation bank.** Each plant draws 1,000 of the same 4,000 permutations, which correlates
  plant p's slightly. The target's own p's use independent shuffles.
- **The brief was extended in four places.** The extensions are an F convention for T2-length plants in A3,
  the X-only scan, a fixed-group-position null variant, and 50,000 instead of 10,000 placements. Each is labelled
  where it appears.
- **No key search, no decipherment.**
