# 12-type-diagnostics — which cipher type do the statistics point to?

## Question
Is "plaintext letters in a new order" still the best reading of these texts, against the other cipher types of the
period, at these lengths? And what do the lengths allow?

## Pre-registered readings
Copied verbatim from the dispatch, before anything was run. Not edited later.

- If the transposition types (1–3) rank first for both telegrams, every statistic of T1 and T2 lies inside the 5–95% band of at least one transposition type, and leave-one-out accuracy for "transposition (1–3) vs everything else" is at least 95% at each length, then "plaintext letters in a new order" stands.
- If T1 or T2 falls outside every transposition band on some statistic but inside another type's band, that type rises in stage 2 and the statistic is named.
- Types 1, 2 and 3 are expected to be confusable with each other at these lengths. Report their mutual confusion instead of naming a winner among them, unless one statistic separates them at ≥ 90% leave-one-out accuracy.
- A type is excluded by these diagnostics only if T1 (or T2) lies outside its 1–99% band on at least one statistic AND the classifier puts it below the best type by more than 10 log-likelihood units.

## Method
`diagnose.py`. Plaintext is telegraph-style held-out Spanish from `01-solver/plaintext.py` (articles dropped, PUNTO
for stops, spelled quantities). Each plant is made at the telegram's length, 615 or 160 letters, and scored with the
same code as the telegrams. 500 plants per variant per length, 22 variants, 22,000 plants in all. Seeds are fixed
per variant and length. Every cipher has a round-trip self-test, and bifid and Playfair also pass hand-worked
textbook examples. "DC" means double columnar, forward convention, two random keys of width 8–25 (`01-solver/transpo.py`).

### Types and variants
| type | variant | what the plant is |
|---|---|---|
| 1 transposition | 1a | random permutation of the letters (stands for well-mixed double columnar) |
| | 1b | single columnar, random key, width 5–30 |
| | 1c | DC |
| 2 transposition + nulls | 2a / 2b | uniform random letters at 3% / 8% of positions, inserted before DC |
| | 2c | X at 1% of positions (6 in 615, 2 in 160), then DC |
| 3 transposition of mixed text | 3 | each word token replaced with probability 0.10 by a five-letter uniform random codeword (fixed per word), then DC |
| 4 monoalphabetic | 4 | random 26-letter key (calibration) |
| 5 Vigenère | 5 | random key, period 3–12, letter output (calibration) |
| 6 bifid | 6a–6d | random 5 × 5 square without W (plaintext W → V), period 5, 7, 10, unperiodic |
| 7 ADFGX / ADFGVX | 7a / 7b | 5 × 5 square (no W) with ADFGX, or 6 × 6 (letters and digits) with ADFGVX, then single columnar width 10–25 |
| 8 Playfair | 8 | random 25-letter square without W; doubled pair letters split with X (XX with Q); odd end padded with X |
| 9 homophonic | 9 | 26 output letters shared out by largest remainder of 26 × Spanish frequency: A3 E3 O3 I2 N2 R2 S2 T2, and 1 each for B C D L M P U. The 11 letters with k = 0 (F G H J K Q V W X Y Z) borrow the homophone set of a random letter. Homophone chosen uniformly per occurrence |
| 10 nomenclator | 10 | monoalphabetic, and each word token replaced with probability 0.15 by a 2- or 3-letter uniform random code group (fixed per word) |
| 11 codebook | 11a / 11b | every word becomes a five-letter codeword (fixed per word): uniform random letters, or CVCVC / VCVCV from vowels AEIOU and the 21 other letters |
| 12 jargon code | 12a / 12b | every word replaced, by a fixed random map, with a word drawn uniformly from the 11,450 held-out word types seen at least 5 times; as is, or then DC |

Types 7 and 8 produce even lengths only. For T1 they are planted at 614 letters, and their bands are compared with
T1's 615. Both are impossible at 615 in any case (see Length constraints).

### Statistics
Names follow the ACA / BION set as documented by CryptoCrack, which cites BION's "Reference Statistics", *The
Cryptogram*, May–June 2005 (https://www.sites.google.com/site/cryptocrackprogram/user-guide/tools-tab/identify-cipher,
`SECONDARY`). Operational forms follow the NCID code where it agrees with BION's wording (github.com/ernstleierzopf/ncid,
`cipherTypeDetection/textLine2CipherStatisticsDataset.py`, `SECONDARY`). Spanish tables replace the English ones.
N is the text length and t_i its letters.
- **IC** = 1000 · Σ n_x(n_x − 1) / (N(N − 1)).
- **MIC** = 1000 · max over periods p = 2–15 of the mean IC of the p columns t_j, t_{j+p}, … (BION uses 1–15.)
- **MKA** = 1000 · max over shifts s = 1–15 of #{i : t_i = t_{i+s}} / (N − s).
- **DIC** = 10000 · digraphic IC over all N − 1 overlapping pairs.
- **EDI** = 10000 · digraphic IC over the ⌊N/2⌋ pairs (t_0 t_1), (t_2 t_3), ….
- **LR** = 1000 · √R3 / N, where R3 is the number of distinct trigrams that occur at least twice. This is our
  reading of BION's "square root of the percentage of 3 symbol repeats".
- **ROD** = share of odd distances j − i among all pairs i < j whose digraphs t_i t_{i+1} and t_j t_{j+1} match
  (0.5 if there are none).
- **LDI** = mean over the N − 1 adjacent pairs of log10 P_es(ab), from `01-solver/out/lm_es_2.bin`.
- **SDD** = mean over adjacent pairs of log10 [P_es(ab) / (P_es(a) P_es(b))], with marginals from the same table.
  BION's English table keeps only positive discrepancies on a 0–9 scale. This version is unclipped.
- **CHI** = Σ_x (n_x − N f_x)² / (N f_x + 0.5), with f from 40 chunks of 10,000 telegraph-style letters, as in `08`.
- **NDL** = number of distinct letters.
- **DBL** = share of adjacent pairs that are doubled letters. **DBLE** = number of doubled letters at even-aligned
  pairs (t_{2k} = t_{2k+1}), which Playfair forbids.

### Bands, classifier, leave-one-out
- Bands are linearly interpolated quantiles of the plants. A type's band pools the plants of all its variants. A
  telegram's percentile is the mid-rank: % of plants below, plus half the % equal.
- Classifier: a diagonal Gaussian per variant (mean and sd of each statistic over its plants). Each sd is floored at
  0.5 for the integer statistics (NDL, DBLE) and at 0.1 × the median variant sd for the others, so that a constant
  such as Playfair's DBLE = 0 does not give an infinite penalty. A type's log-likelihood is the log of the equal-weight
  mixture of its variants. Units are natural logs.
- Leave-one-out: each plant is classified with its own variant's mean and sd recomputed without it. The binary test
  counts a plant as right when true and predicted type are both in {1, 2, 3} or both outside it.

## Run
`python3 -I diagnose.py > result.txt` takes about 40 s on one core. `--quick` runs 40 plants per variant. The
per-plant statistics go to `out/plants_615.tsv` and `out/plants_160.tsv`, which are gitignored.

## Result
All numbers come from `result.txt`.

### The telegrams
| | IC | MIC | MKA | DIC | EDI | LR | ROD | LDI | SDD | CHI | NDL | DBL | DBLE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 (615) | 69.5 | 70.6 | 86.9 | 51.5 | 54.5 | 10.91 | 0.491 | −2.864 | −0.355 | 58 | 25 | 0.073 | 23 |
| T2 (160) | 71.0 | 77.3 | 131.0 | 55.7 | 50.6 | 10.83 | 0.514 | −2.770 | −0.287 | 35 | 21 | 0.075 | 4 |

T1's MKA peaks at shift 5 and its MIC at period 3. T2's MKA peaks at shift 15, the end of the range, with 19
coincidences in 145 pairs. T1 has 45 doubled letters: 23 at even-aligned pairs and 22 at odd-aligned pairs. T2 has
12: 4 even-aligned and 8 odd-aligned.

### Classifier ranking (log-likelihood minus the best type)
| rank | T1 | Δ | T2 | Δ |
|---|---|---|---|---|
| 1 | 2 transposition + nulls | 0.0 | 1 transposition | 0.0 |
| 2 | 3 transposition of mixed text | −3.0 | 12 jargon code | −0.3 |
| 3 | 1 transposition | −3.7 | 2 transposition + nulls | −0.9 |
| 4 | 12 jargon code | −8.2 | 3 transposition of mixed text | −4.2 |
| 5 | 6 bifid | −69.3 | 10 nomenclator | −40.1 |
| 6 | 5 Vigenère | −96.2 | 4 monoalphabetic | −42.9 |
| 7 | 10 nomenclator | −105.0 | 6 bifid | −53.6 |
| 8 | 4 monoalphabetic | −121.4 | 11 codebook | −58.0 |
| 9 | 11 codebook | −124.9 | 8 Playfair | −80.8 |
| 10 | 9 homophonic | −349.7 | 5 Vigenère | −85.4 |
| 11 | 7 ADFGX/ADFGVX | −974.1 | 9 homophonic | −203.8 |
| 12 | 8 Playfair | −1136.7 | 7 ADFGX/ADFGVX | −699.8 |

By variant: for T1, 2a 0.0, 2c −0.9, 2b −0.9, 3 −3.5, 1a −3.6, 1c −4.7, 1b −4.9, 12b −8.1. For T2, 12b 0.0, 1a −0.3,
1b −0.4, 1c −0.4, 2c −0.9, 2a −0.9, 2b −3.4, 3 −4.6. T1's largest deviations from the nearest plain-transposition
variant (1a) are MIC z −1.8, LR −1.5 and IC −1.4. From 2a they are MIC −1.3, LR −1.1 and IC −0.7.

### Telegram percentile within each type's plants
`*` marks a value outside the 5–95% band, `**` outside the 1–99% band. T1 is scored against the 615 plants (614 for
types 7 and 8), T2 against the 160 plants.

T1:

| type | IC | MIC | MKA | DIC | EDI | LR | ROD | LDI | SDD | CHI | NDL | DBL | DBLE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 transposition | 5* | 2* | 22 | 27 | 57 | 6 | 29 | 9 | 32 | 93 | 88 | 51 | 56 |
| 2 transposition + nulls | 38 | 22 | 41 | 65 | 82 | 20 | 27 | 38 | 47 | 69 | 47 | 62 | 62 |
| 3 transposition of mixed text | 83 | 62 | 59 | 94 | 97* | 52 | 24 | 80 | 66 | 46 | 15 | 69 | 71 |
| 4 monoalphabetic | 5 | 2* | 17 | 0** | 0** | 0** | 22 | 100** | 99** | 0** | 88 | 100** | 100** |
| 5 Vigenere | 100** | 14 | 78 | 99* | 94 | 53 | 65 | 100** | 100** | 0** | 1* | 100** | 100** |
| 6 bifid | 100** | 99** | 95* | 98* | 98* | 87 | 34 | 100** | 100** | 0** | 51 | 99* | 97* |
| 7 ADFGX/ADFGVX | 0** | 0** | 0** | 0** | 0** | 0** | 15 | 100** | 100** | 0** | 100** | 0** | 0** |
| 8 Playfair | 100** | 99** | 95* | 70 | 0** | 0** | 100** | 100** | 100** | 0** | 58 | 100** | 100** |
| 9 homophonic | 100** | 100** | 99** | 95* | 96* | 60 | 33 | 100** | 100** | 0** | 0** | 100** | 100** |
| 10 nomenclator | 75 | 48 | 50 | 0** | 0** | 0** | 26 | 100** | 99** | 0** | 20 | 100** | 100** |
| 11 codebook | 96* | 54 | 54 | 47 | 55 | 5 | 30 | 100** | 50 | 0** | 0** | 100** | 99** |
| 12 jargon code | 3* | 1** | 14 | 7 | 19 | 2* | 27 | 3* | 11 | 25 | 89 | 71 | 77 |

T2:

| type | IC | MIC | MKA | DIC | EDI | LR | ROD | LDI | SDD | CHI | NDL | DBL | DBLE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 transposition | 37 | 17 | 91 | 65 | 47 | 26 | 53 | 55 | 78 | 93 | 55 | 56 | 24 |
| 2 transposition + nulls | 64 | 33 | 96* | 80 | 61 | 36 | 52 | 82 | 86 | 86 | 27 | 64 | 27 |
| 3 transposition of mixed text | 81 | 56 | 95* | 86 | 69 | 46 | 54 | 91 | 90 | 69 | 15 | 70 | 33 |
| 4 monoalphabetic | 37 | 9 | 84 | 1** | 3* | 0** | 56 | 100** | 100** | 0** | 55 | 100** | 97* |
| 5 Vigenere | 100** | 62 | 97* | 98* | 83 | 41 | 71 | 100** | 100** | 0** | 0** | 97* | 71 |
| 6 bifid | 100** | 97* | 98* | 98* | 95 | 65 | 50 | 100** | 100** | 0** | 0** | 93 | 57 |
| 7 ADFGX/ADFGVX | 0** | 0** | 0** | 0** | 0** | 0** | 64 | 100** | 100** | 0** | 100** | 0** | 0** |
| 8 Playfair | 100** | 90 | 97* | 78 | 1* | 13 | 100** | 100** | 100** | 0** | 1* | 100** | 100** |
| 9 homophonic | 100** | 100** | 100** | 96* | 92 | 38 | 53 | 100** | 100** | 0** | 0** | 100** | 98* |
| 10 nomenclator | 75 | 35 | 90 | 6 | 6 | 0** | 55 | 100** | 100** | 0** | 15 | 100** | 96 |
| 11 codebook | 96* | 59 | 86 | 63 | 55 | 2* | 53 | 100** | 51 | 0** | 0** | 98* | 85 |
| 12 jargon code | 26 | 9 | 84 | 27 | 22 | 12 | 52 | 26 | 37 | 72 | 65 | 78 | 58 |

### Plant median [5%, 95%] by type
At 615 (T1 in the first row):

| type | IC | MIC | MKA | DIC | EDI | LR | ROD | LDI | SDD | CHI | NDL | DBL | DBLE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | 69.5 | 70.6 | 86.9 | 51.5 | 54.5 | 10.91 | 0.491 | -2.864 | -0.355 | 58 | 25 | 0.073 | 23 |
| 1 transposition | 73.2 [69.5, 77.2] | 76.1 [71.6, 80.7] | 91.8 [82.2, 105.1] | 53.7 [47.6, 60.2] | 53.7 [45.8, 62.2] | 12.17 [10.91, 13.41] | 0.501 [0.472, 0.528] | -2.781 [-2.925, -2.710] | -0.339 [-0.396, -0.286] | 26 [14, 133] | 24 [23, 25] | 0.073 [0.057, 0.093] | 22 [15, 31] |
| 2 transposition + nulls | 70.5 [65.4, 75.0] | 73.2 [67.7, 78.4] | 88.4 [78.4, 100.7] | 49.6 [42.4, 57.5] | 49.4 [41.3, 58.5] | 11.61 [10.15, 12.91] | 0.503 [0.473, 0.528] | -2.843 [-2.997, -2.759] | -0.352 [-0.412, -0.299] | 48 [20, 156] | 25 [24, 26] | 0.070 [0.054, 0.090] | 21 [14, 29] |
| 3 transposition of mixed text | 66.9 [62.3, 71.8] | 69.6 [64.7, 74.9] | 85.0 [74.5, 97.9] | 44.6 [37.6, 51.7] | 44.1 [36.6, 52.8] | 10.91 [9.34, 12.17] | 0.504 [0.472, 0.528] | -2.925 [-3.070, -2.824] | -0.373 [-0.438, -0.313] | 62 [27, 156] | 26 [25, 26] | 0.067 [0.049, 0.086] | 21 [14, 28] |
| 4 monoalphabetic | 73.1 [69.4, 77.1] | 76.6 [72.0, 82.1] | 94.0 [82.2, 108.9] | 92.6 [79.3, 122.9] | 92.9 [76.2, 123.9] | 16.90 [15.68, 18.11] | 0.501 [0.474, 0.521] | -4.271 [-4.864, -3.612] | -0.768 [-1.130, -0.462] | 4503 [1785, 10535] | 24 [23, 25] | 0.016 [0.008, 0.026] | 5 [2, 9] |
| 5 Vigenere | 42.9 [39.9, 51.0] | 73.9 [69.1, 78.7] | 77.4 [57.8, 96.7] | 25.5 [20.0, 43.7] | 30.9 [20.2, 55.8] | 10.79 [8.29, 13.70] | 0.423 [0.205, 0.533] | -4.314 [-4.560, -3.971] | -0.790 [-0.921, -0.632] | 2803 [1523, 4906] | 26 [26, 26] | 0.037 [0.024, 0.055] | 12 [6, 19] |
| 6 bifid | 46.6 [42.1, 55.0] | 53.2 [45.6, 64.5] | 67.1 [54.8, 86.8] | 25.3 [19.4, 39.4] | 25.5 [18.7, 40.7] | 9.05 [6.70, 11.84] | 0.502 [0.454, 0.540] | -3.910 [-4.193, -3.542] | -0.703 [-0.858, -0.534] | 1524 [819, 2638] | 25 [25, 25] | 0.047 [0.029, 0.067] | 14 [8, 22] |
| 7 ADFGX/ADFGVX | 203.8 [172.6, 226.7] | 208.2 [176.6, 231.4] | 242.6 [208.0, 276.2] | 418.0 [303.8, 516.1] | 418.3 [304.4, 516.3] | 17.69 [16.37, 20.28] | 0.501 [0.483, 0.510] | -4.481 [-4.953, -4.040] | -0.758 [-0.971, -0.576] | 17949 [9178, 33516] | 6 [5, 6] | 0.201 [0.150, 0.250] | 62 [44, 79] |
| 8 Playfair | 53.3 [48.3, 61.0] | 57.6 [51.6, 66.0] | 70.0 [59.5, 85.4] | 48.1 [40.0, 70.2] | 94.7 [77.9, 135.2] | 13.72 [12.18, 15.28] | 0.299 [0.197, 0.362] | -4.151 [-4.647, -3.693] | -0.801 [-1.055, -0.550] | 2482 [1291, 4499] | 25 [24, 25] | 0.020 [0.010, 0.031] | 0 [0, 0] |
| 9 homophonic | 40.3 [39.0, 43.4] | 42.8 [40.8, 46.8] | 54.7 [47.4, 67.7] | 30.3 [25.1, 49.2] | 30.4 [23.8, 48.9] | 10.66 [9.05, 12.49] | 0.502 [0.459, 0.534] | -4.292 [-4.492, -4.070] | -0.779 [-0.913, -0.659] | 2683 [1807, 3962] | 26 [26, 26] | 0.013 [0.005, 0.024] | 4 [1, 8] |
| 10 nomenclator | 67.6 [63.6, 72.0] | 70.8 [66.5, 76.5] | 86.9 [75.7, 103.2] | 80.0 [68.3, 114.7] | 78.8 [65.6, 118.7] | 15.93 [14.45, 17.13] | 0.502 [0.466, 0.524] | -4.281 [-4.944, -3.677] | -0.776 [-1.183, -0.477] | 4160 [1467, 10235] | 26 [24, 26] | 0.018 [0.008, 0.028] | 5 [2, 9] |
| 11 codebook | 58.5 [39.3, 68.6] | 68.8 [46.5, 97.5] | 83.7 [51.1, 137.0] | 52.7 [28.2, 105.1] | 52.5 [27.5, 106.5] | 13.70 [10.91, 15.77] | 0.504 [0.450, 0.540] | -3.627 [-4.487, -2.973] | -0.432 [-0.891, -0.046] | 1840 [757, 3790] | 26 [26, 26] | 0.021 [0.007, 0.054] | 6 [1, 17] |
| 12 jargon code | 75.0 [70.2, 81.2] | 78.3 [72.9, 85.6] | 94.6 [83.2, 112.8] | 75.4 [50.3, 117.7] | 76.0 [49.2, 120.3] | 14.86 [11.38, 18.03] | 0.502 [0.470, 0.525] | -2.537 [-2.846, -2.242] | -0.073 [-0.371, 0.185] | 75 [43, 148] | 24 [22, 25] | 0.046 [0.010, 0.091] | 13 [2, 30] |

At 160 (T2 in the first row):

| type | IC | MIC | MKA | DIC | EDI | LR | ROD | LDI | SDD | CHI | NDL | DBL | DBLE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T2 | 71.0 | 77.3 | 131.0 | 55.7 | 50.6 | 10.83 | 0.514 | -2.770 | -0.287 | 35 | 21 | 0.075 | 4 |
| 1 transposition | 72.4 [66.0, 80.7] | 83.8 [73.3, 98.2] | 110.3 [89.7, 138.4] | 52.5 [39.8, 69.3] | 50.6 [31.6, 79.1] | 12.50 [6.25, 17.68] | 0.508 [0.390, 0.609] | -2.781 [-2.947, -2.650] | -0.337 [-0.441, -0.237] | 19 [10, 39] | 21 [18, 23] | 0.069 [0.038, 0.107] | 6 [2, 10] |
| 2 transposition + nulls | 69.3 [61.9, 77.9] | 80.2 [70.0, 94.2] | 105.3 [86.7, 130.2] | 47.8 [34.2, 64.5] | 47.5 [28.5, 72.8] | 12.50 [6.25, 17.68] | 0.510 [0.383, 0.612] | -2.853 [-3.037, -2.710] | -0.354 [-0.456, -0.255] | 23 [13, 52] | 22 [20, 24] | 0.069 [0.038, 0.101] | 5 [2, 9] |
| 3 transposition of mixed text | 65.7 [57.5, 75.7] | 76.3 [65.3, 91.6] | 101.3 [82.2, 130.7] | 43.0 [29.5, 60.5] | 41.1 [25.3, 66.5] | 10.83 [0.00, 16.54] | 0.509 [0.389, 0.605] | -2.923 [-3.175, -2.733] | -0.372 [-0.487, -0.262] | 27 [14, 65] | 23 [20, 25] | 0.063 [0.031, 0.101] | 5 [2, 10] |
| 4 monoalphabetic | 72.3 [65.6, 80.4] | 85.8 [76.2, 102.4] | 111.8 [90.9, 152.4] | 91.6 [66.9, 157.2] | 94.9 [57.0, 161.6] | 23.39 [17.68, 30.01] | 0.505 [0.386, 0.585] | -4.290 [-4.963, -3.563] | -0.773 [-1.138, -0.418] | 721 [316, 1372] | 21 [19, 23] | 0.013 [0.000, 0.038] | 1 [0, 3] |
| 5 Vigenere | 43.4 [38.8, 51.3] | 74.7 [62.1, 91.9] | 85.0 [61.2, 124.2] | 27.1 [15.9, 48.6] | 31.6 [12.7, 72.8] | 12.50 [0.00, 22.53] | 0.415 [0.135, 0.632] | -4.311 [-4.693, -3.898] | -0.785 [-1.006, -0.583] | 440 [276, 752] | 26 [24, 26] | 0.038 [0.013, 0.069] | 3 [0, 6] |
| 6 bifid | 46.5 [41.0, 56.5] | 58.9 [48.3, 74.8] | 82.8 [62.1, 115.6] | 25.5 [15.9, 45.4] | 25.3 [9.5, 50.6] | 8.84 [0.00, 18.75] | 0.515 [0.333, 0.667] | -3.917 [-4.293, -3.501] | -0.707 [-0.933, -0.506] | 286 [160, 491] | 25 [23, 25] | 0.044 [0.019, 0.082] | 4 [1, 7] |
| 7 ADFGX/ADFGVX | 201.5 [169.2, 230.1] | 218.2 [181.3, 251.7] | 261.1 [217.9, 311.7] | 406.0 [289.8, 531.0] | 401.9 [278.5, 535.1] | 39.53 [35.90, 43.30] | 0.506 [0.455, 0.539] | -4.470 [-4.927, -3.975] | -0.760 [-0.996, -0.551] | 2645 [1658, 4469] | 5 [5, 6] | 0.201 [0.132, 0.264] | 16 [10, 23] |
| 8 Playfair | 53.1 [45.8, 63.1] | 65.6 [54.5, 82.2] | 86.7 [68.0, 118.5] | 47.0 [32.6, 72.6] | 91.8 [63.1, 158.4] | 16.54 [8.84, 24.21] | 0.298 [0.127, 0.424] | -4.183 [-4.644, -3.609] | -0.807 [-1.110, -0.534] | 453 [238, 795] | 24 [22, 25] | 0.019 [0.000, 0.038] | 0 [0, 0] |
| 9 homophonic | 39.7 [36.9, 44.7] | 50.0 [42.9, 59.7] | 71.0 [53.3, 93.4] | 28.7 [19.1, 50.2] | 28.5 [12.7, 60.1] | 12.50 [6.25, 19.76] | 0.500 [0.353, 0.655] | -4.297 [-4.601, -3.974] | -0.782 [-0.959, -0.597] | 407 [271, 656] | 26 [25, 26] | 0.013 [0.000, 0.031] | 1 [0, 3] |
| 10 nomenclator | 67.5 [59.3, 75.5] | 80.8 [68.9, 96.5] | 106.0 [85.5, 141.9] | 78.8 [54.9, 121.9] | 79.1 [47.5, 129.9] | 21.65 [15.31, 27.95] | 0.505 [0.394, 0.596] | -4.319 [-4.989, -3.645] | -0.807 [-1.170, -0.483] | 673 [319, 1287] | 23 [20, 25] | 0.019 [0.000, 0.038] | 1 [0, 4] |
| 11 codebook | 55.9 [37.7, 70.5] | 72.5 [46.8, 118.1] | 96.6 [58.8, 158.2] | 48.6 [21.5, 112.4] | 47.5 [15.8, 120.3] | 20.73 [12.50, 27.95] | 0.508 [0.305, 0.672] | -3.545 [-4.552, -2.906] | -0.395 [-0.926, -0.011] | 291 [130, 588] | 26 [24, 26] | 0.019 [0.000, 0.063] | 2 [0, 6] |
| 12 jargon code | 73.9 [66.1, 82.8] | 87.0 [75.4, 103.8] | 114.1 [94.0, 143.9] | 68.9 [43.0, 122.6] | 69.6 [38.0, 132.9] | 18.75 [8.84, 31.25] | 0.512 [0.386, 0.598] | -2.528 [-2.882, -2.226] | -0.056 [-0.402, 0.198] | 29 [16, 52] | 20 [18, 23] | 0.038 [0.006, 0.101] | 3 [0, 9] |

Per-variant bands are in `result.txt`.

### Leave-one-out
Rows give the true type and columns the predicted type.

At 615. Overall accuracy is 82.9%. **Binary accuracy (1–3 vs the rest) is 95.18%.**
| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 940 | 325 | 29 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 205 |
| 2 | 327 | 866 | 258 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 48 |
| 3 | 5 | 185 | 304 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| 4 | 0 | 0 | 0 | 472 | 0 | 0 | 0 | 0 | 0 | 28 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 483 | 2 | 0 | 1 | 0 | 3 | 11 | 0 |
| 6 | 0 | 0 | 1 | 0 | 10 | 1954 | 0 | 0 | 1 | 1 | 33 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 1000 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 500 | 0 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 477 | 0 | 22 | 0 |
| 10 | 0 | 0 | 0 | 45 | 0 | 0 | 0 | 0 | 0 | 455 | 0 | 0 |
| 11 | 0 | 0 | 0 | 0 | 3 | 17 | 0 | 0 | 41 | 0 | 939 | 0 |
| 12 | 197 | 69 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 730 |

At 160. Overall accuracy is 72.3%. **Binary accuracy is 93.90%.**
| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 861 | 357 | 74 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 208 |
| 2 | 413 | 643 | 335 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 109 |
| 3 | 72 | 152 | 253 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 18 |
| 4 | 0 | 0 | 0 | 360 | 0 | 0 | 0 | 0 | 0 | 140 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 402 | 41 | 0 | 13 | 25 | 6 | 13 | 0 |
| 6 | 0 | 0 | 7 | 0 | 92 | 1757 | 0 | 11 | 98 | 19 | 16 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 | 0 | 1000 | 0 | 0 | 0 | 0 | 0 |
| 8 | 0 | 0 | 0 | 3 | 3 | 3 | 0 | 471 | 5 | 15 | 0 | 0 |
| 9 | 0 | 0 | 0 | 0 | 9 | 7 | 0 | 2 | 460 | 3 | 19 | 0 |
| 10 | 0 | 0 | 0 | 137 | 1 | 5 | 0 | 16 | 0 | 341 | 0 | 0 |
| 11 | 0 | 0 | 0 | 6 | 62 | 16 | 0 | 1 | 171 | 10 | 734 | 0 |
| 12 | 213 | 92 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 676 |

The binary errors are almost all between types 1–3 and type 12. At 615: 1→12 205, 12→1 197, 12→2 69, 2→12 48, and
11 others. At 160: 12→1 213, 1→12 208, 2→12 109, 12→2 92, 12→3 19, 3→12 18, and 12 involving bifid. With the
type-12 plants left out, binary accuracy would be 97.38% and 96.53%. That figure is supplementary, not the
pre-registered test.

### Mutual confusion of types 1, 2 and 3
| true \ predicted, 615 | 1 | 2 | 3 | | true \ predicted, 160 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|
| 1 | 940 | 325 | 29 | | 1 | 861 | 357 | 74 |
| 2 | 327 | 866 | 258 | | 2 | 413 | 643 | 335 |
| 3 | 5 | 185 | 304 | | 3 | 72 | 152 | 253 |

Plants of types 1–3 that land in types 1–3 sit on the diagonal 65.1% of the time at 615 and 55.6% at 160. Chance
is about 33%. Single-statistic three-way leave-one-out accuracy among 1–3 peaks at 62.1% (CHI) at 615 and 53.8%
(LDI) at 160. One pairwise split reaches 90%: IC separates type 1 from type 3 at 90.7% at 615. On that split, T1's IC
favours type 3 by 0.60 log units. The variant-level confusion is in `result.txt`.

### Pre-registered checks
| check | T1 (615) | T2 (160) |
|---|---|---|
| a transposition type (1–3) ranks first | yes (2) | yes (1) |
| every statistic inside the 5–95% band of at least one of types 1–3 | yes | yes |
| one transposition type holds every statistic in its 5–95% band | type 2 | type 1 |
| LOO binary accuracy ≥ 95% | **95.18%, yes** | **93.90%, no** |
| statistic outside every transposition band but inside another type's | none | none |
| single statistic separating 1/2/3 at ≥ 90% (three-way) | no (best 62.1%) | no (best 53.8%) |
| excluded (outside a 1–99% band and > 10 below the best) | 4, 5, 6, 7, 8, 9, 10, 11 | 4, 5, 6, 7, 8, 9, 10, 11 |
| not excluded | 1, 2, 3, 12 | 1, 2, 3, 12 |

**First pre-registered reading: not met.** It fails on one condition, LOO binary accuracy at 160.

The statistics each excluded type fails at the 1–99% level, with its Δ:
- T1: 4 [DIC EDI LR LDI SDD CHI DBL DBLE; −121], 5 [IC LDI SDD CHI DBL DBLE; −96], 6 [IC MIC LDI SDD CHI; −69],
  7 [all but ROD; −974], 8 [IC MIC EDI LR ROD LDI SDD CHI DBL DBLE; −1137], 9 [IC MIC MKA LDI SDD CHI NDL DBL DBLE;
  −350], 10 [DIC EDI LR LDI SDD CHI DBL DBLE; −105], 11 [LDI CHI NDL DBL DBLE; −125].
- T2: 4 [DIC LR LDI SDD CHI DBL; −43], 5 [IC LDI SDD CHI NDL; −85], 6 [IC LDI SDD CHI NDL; −54], 7 [all but ROD;
  −700], 8 [IC ROD LDI SDD CHI DBL DBLE; −81], 9 [IC MIC MKA LDI SDD CHI NDL DBL; −204], 10 [LR LDI SDD CHI DBL; −40],
  11 [LDI CHI NDL; −58].

### Supplementary (not pre-registered)
- The exclusion rule applied per variant excludes 4, 5, 6a–6d, 7a, 7b, 8, 9, 10, 11a, 11b **and 12a** for both
  telegrams. It does not exclude 1a–1c, 2a–2c, 3 or **12b**. Jargon survives only when transposed.
- How often plants pass the band condition of the first reading (every statistic inside some 1–3 band): at 615,
  types 1 / 2 / 3 pass 59% / 73% / 67%, types 4–11 pass 0%, and type 12 passes 20%. At 160 the figures are 59% /
  67% / 62%, 0%, and 30%.
- With prose-style Spanish instead of telegraphese, a random permutation gives IC 75.7 [70.5, 80.5] at 615, where
  T1 is at the 4th percentile. MIC puts T1 at the 3rd percentile, LR at the 5th, LDI at the 5th and CHI at the 71st.
  At 160, T2 is at the 20th percentile for IC. Prose raises the IC, so T1's low IC is not an artefact of the
  telegraph transform.

## Length constraints
From the script's `LENGTH CONSTRAINTS` block.

| | T1 | T2 |
|---|---|---|
| N | 615 = 3 · 5 · 41 | 160 = 2⁵ · 5 |
| N − 1, N + 1 | 614 = 2 · 307; 616 = 2³ · 7 · 11 | 159 = 3 · 53; 161 = 7 · 23 |
| form words − 2 address words | 125 − 2 = 123 = N/5 | 34 − 2 = 32 = N/5 |
| even (Playfair, ADFGX/ADFGVX, any digraph output) | **no** | yes (80 pairs) |
| multiple of 25 | no (615 mod 25 = 15) | no (160 mod 25 = 10) |
| complete turning grille | **none** for any n from 2 to 25 | 2 × 2 × 40; 3 × 3 without centre × 20; 4 × 4 × 10; 9 × 9 without centre × 2 |
| complete single-columnar widths 2–45 | 3, 5, 15, 41 | 2, 4, 5, 8, 10, 16, 20, 32, 40 |
| complete double columnar | both widths from {3, 5, 15, 41} | both widths from the list above |
| bifid / Vigenère periods 2–15 with complete blocks | 3, 5, 15 | 2, 4, 5, 8, 10 |
| codeword lengths 2–10 that divide N | 3, 5 | 2, 4, 5, 8, 10 |
| ADFGX/ADFGVX plaintext letters | 307.5, impossible | 80 |

Each type's requirement:
- Transposition (1–3), Vigenère, bifid, homophonic, nomenclator and jargon: none. Incomplete rectangles and blocks
  are allowed, and the lists above show where they would be complete.
- Playfair and ADFGX/ADFGVX: even length. T1 fails as a whole message, and a one-letter loss or addition would be
  needed. Playfair also fails on content. T1 has doubled letters at 23 even-aligned and 22 odd-aligned pairs, so
  it fails under either alignment. T2 has 4 and 8.
- Turning grille: a multiple of n², or of n² − 1 for odd n with the centre unused. No grille size fits T1. T2 fits
  4 × 4 (tested in `06`) and, untested, 3 × 3 and 9 × 9 without centre.
- Five-letter codewords: N a multiple of 5, which both are. The form counts (123 + 2, 32 + 2) show the clerk counted
  one word per five-letter group. That fits a cipher counted at five letters per word and five-letter codewords
  equally, so the word count does not separate code from cipher.

## Reading (script author's reading; the main thread judges)
1. **Everything except "letters in a new order" is excluded at both lengths.** Types 4–11 are excluded under the
   rule for both telegrams by 40 to 1,137 log units. So is jargon without transposition (12a), at variant level.
   Each fails several statistics at once. The common pattern is Spanish single letters at face value (CHI inside
   transposition bands) with non-Spanish letter pairs (LDI and SDD inside the transposition bands, far below
   jargon text as is, 12a, whose LDI median at 615 is −2.29 against T1's −2.86). No type that keeps
   plaintext pairs or substitutes letters reproduces it. Only types whose last step reorders Spanish-like letters do.
2. **The first pre-registered reading is not met**, on one condition only: LOO binary accuracy at 160 is 93.90%,
   below 95%. At 615 it passes at 95.18%. The misses are transpositions of Spanish confused with transpositions of
   Spanish jargon words (12b), and back. These diagnostics cannot tell whether the letters that were reordered were
   plain Spanish or Spanish code words, at either length. "Letters in a new order" survives every test here. "Plain
   Spanish in a new order" is not separable from "Spanish-word jargon in a new order".
3. **The second reading is not triggered.** No statistic of either telegram falls outside every transposition band.
4. **Types 1, 2 and 3 are confusable, as expected**, with diagonals of 65% and 56%. No statistic separates the
   three at 90%. The one pairwise split that reaches 90% (IC, 1 against 3, at 615) favours type 3 by only 0.6 log
   units. No winner is named.
5. **A weak lean in T1, not in T2.** T1 sits low against plain transposition of Spanish: IC at the 5th percentile,
   MIC at the 2nd, LR at the 6th, and lower still against prose. That is why types 2 and 3 edge out type 1, by 3–4
   log units. These statistics share one cause, letters slightly flatter than Spanish, so the diagonal model counts
   it several times. As one fact, it is roughly a 1-in-20 event under plain transposition. It is consistent with
   `08`'s marginal letter fit (X 6 against 1 expected). A few percent of non-Spanish letters, such as nulls, code
   groups, names or numbers, would produce it. T2 shows no lean (IC at the 37th percentile of type 1).

## Caveats
- The diagonal Gaussian ignores correlations. IC, MIC, LR, DIC and LDI all respond to the same flatness. Treat the
  differences of under 10 log units among types 1, 2, 3 and 12 as a tie, not a ranking.
- The plaintext is a model. Telegraph style is from `01`, and a prose check moves the bands up, not down. A real 1937
  business telegram with names, places, figures or foreign words is not modelled, and it would flatten the letters
  the way nulls do.
- Variant parameters are our choices: null rates, the codeword share, the homophone allocation (11 letters borrow),
  code-group lengths, the jargon vocabulary and the ADFGVX widths. Other choices would move the bands. The
  exclusions (types 4–11, by 40 or more log units on several statistics at once) should not hinge on them. The
  order among the survivors does.
- Types not planted: substitution followed by transposition, Nihilist number ciphers, long-period or running-key
  polyalphabetics (Enigma, strip ciphers), and any system with digit output (the Réglette's output was two-digit
  numbers, `sources/key-type-survey.md`). Their statistics are not computed here.
- Statistic definitions are adapted. MIC uses periods 2–15. LR and ROD are our reading of BION's one-line
  definitions; NCID's code computes LR differently. LDI and SDD use Spanish tables from the `01` training corpus, and
  SDD is unclipped. Rankings within this experiment are self-consistent. Its numbers are not comparable with English
  BION tables.
- At 160 letters every band is wide, so T2's diagnostics are weaker than T1's, as the LOO accuracy shows.
- No solved case (AGENTS rule 7) was run through this classifier. The solved cases in the catalog are symbol
  ciphers or too long to compare directly.

## Unverified claims
- That our LR and ROD match the definitions in BION's article (*The Cryptogram*, May–June 2005). We read only the
  CryptoCrack summary and the NCID code, not the article.
