# 16-run-geometry — do the seven shared runs fit one single-columnar geometry?

## Question

`07` found one model that turns a shared phrase into the excess of shared 4-grams: single columnar
transposition, one key on both telegrams. Bourdeau excluded single columnar at the full lengths (615 and 160).
With untransposed letters at either end, it was not excluded. Do the seven shared runs of `02`/`13` sit
where that system would put them?

## Candidate and prediction

**K3.** One forward single columnar transposition: write rows of width w, read columns in key order, incomplete
last row allowed. One key serves both telegrams, and both carry a shared plaintext phrase. Each body may be
shorter than 615 or 160 by 0–20 untransposed letters at either end.

**Prediction.** Under K3 a true shared run is a same-row segment of the same column in both telegrams. So the
runs must fit one geometry: one width w, body starts s1 and s2, end trims e1 and e2, and one column order. The
column of rank k starts at S(k) = s + k·h + (long columns among ranks < k), with h = L′ // w and L′ % w long
columns. Under one key the same plaintext columns are long-eligible in both telegrams; only the count differs. A run at
rank k, row r sits at S1(k) + r + Δr in T1 and S2(k) + r in T2. Δr is one row offset for all runs: the phrase may
start at different rows when its plaintext offsets agree mod w. Chance runs fit no common geometry.

The seven runs (0-based; `02`, `13`): NOCU (T2 0, T1 17), APMOEP (T2 5, T1 263), OEPM (T2 8, T1 42),
LNDN (T2 38, T1 569), TRSP (T2 87, T1 274), RAEA (T2 128, T1 164), ISEE (T2 138, T1 464). About 2 of 7 are
expected by chance.

## Pre-registered readings

Copied verbatim from the dispatch, before any code was run.

- If the observed best count exceeds the 99th percentile of null (i) and of null (ii), and the planted control recovers the true w in at least 80% of plants, K3 is supported. The best geometry (w, s1, s2, e1, e2) becomes the stage-4 target, and the shared runs become a crib.
- If the observed best count lies within the 95th percentile of both nulls and the control passes, K3 is refuted for w 5–60 with up to 20 untransposed letters at each end.
- If the control fails (below 80%), K3 is "not testable by run geometry" here.
- Separately: if K3 plants at every w produce many more shared runs than 7 (median ≥ 2 × 7) or many fewer, record the run count itself as evidence for or against K3, with the plant distribution.

## Method

Python standard library, `python3 -I`, fixed seeds (20261016 plus replicate index). This experiment computes
statistics on positions only. It runs no decipherment and no key search on the telegrams.

**The exact consistency check (`geom.py`).** Write c1(k) = s1 + n1(k) and c2(k) = s2 + n2(k), where n(k) counts
long columns among ranks < k. Each rank is one step of a lattice path. Its type is B (long in both telegrams),
O (long only in the telegram with more long columns) or N (short in both). With x1 ≥ x2 the steps are
B = (+1, +1), O = (+1, 0), N = (0, 0); with x2 ≥ x1, O = (0, +1). The type counts are fixed by x1 and x2,
and any order of them is realised by some key. So "the start sequences are realisable with the long/short rule
for some common key" is exactly "such a path exists". The path starts at (s1, s2) and ends at
(615 − e1 − h1·w, 160 − e2 − h2·w). The search lets x reach w (every column long). That is the same geometry as
(h + 1, x = 0), so no geometry is added or lost, and the start and end boxes become independent.

A run (a, b, len) placed at rank k, row r, with column type t, needs c2(k) = b − k·h2 − r and
c1(k) − c2(k) = (a − b) − k·(h1 − h2) − Δr. It also needs 0 ≤ r ≤ colLen2 − len and 0 ≤ r + Δr ≤ colLen1 − len:
the whole run lies inside both columns. Each (run, rank, type) is an event with an interval of c2 values.
For each (w, h1, h2, direction, Δr), a dynamic programme over events, in T2 order, keeps the longest chain for
each event and c2 value. Consecutive events must be joined by a feasible path segment whose first step is the
earlier event's column type. Two runs on one rank must share the column: same c1, c2 and type. The first event
must be reachable from the start box, and the end box from the last. The best count is the longest chain over
all passes. "Every geometry that reaches it" re-runs the programme from each single start point (s1, s2) and
lists the end points (e1, e2) reached by a best chain.

**Bottoms (shared closing).** A run may instead sit at the same distance from the column bottom in both
telegrams. A closing lands in the same column in both only if L1′ ≡ L2′ (mod w). Then no column is long in one
telegram and short in the other, and the row offset of a bottom run is h1 − h2. These passes use B and N steps
only, and each run takes offset Δr or h1 − h2.

**Exact pruning.** w runs 5–60 and h1, h2 over every value the trims allow. For each (w, h1, h2, direction) a
relaxation bounds the chain length. Its nodes are (run, rank) pairs that fit the T1 and T2 column bands for some
Δr in range. Its edges join runs in T2 order with rank non-decreasing. An edge needs the diagonal difference
Δ(a − b) to equal Δk·(h1 − h2) plus at most Δk O-steps of the right sign. It also needs the T2 offset difference
to fit the row slack of the two columns. Every chain the exact programme accepts satisfies these conditions, so
the longest DAG path is an upper bound. A pass whose bound cannot beat the best so far (or reach it, when
collecting geometries) skips the exact programme. Each run's candidate ranks follow arithmetically from its T1
and T2 positions, so there are few.

**Checks (`verify.py`).** (1) The step-range formulas match every step sequence of length 1–6, in all three
modes. (2) An independent brute force builds column starts from every distinct long/short pattern a key can
give, for every geometry in two small spaces (shorter telegrams, w 3–7, small trims and Δr). It gives the same
best count in 240/240 trials, and the same set of best geometries in 208/208, top and bottoms. (3) At full
scale, the pruned search equals the unpruned exact programme on the observed runs (every pass reaching the best),
on 100 null sets × 2 variants, and on 6 plants (w 5–30).

**G2, nulls.** (i) 10,000 sets of seven run pairs with the observed lengths (one 6, six 4). Positions are
uniform in T1 and T2; no two runs overlap in either telegram. (ii) 2,000 pairs of independent letter
shuffles of T1 and T2. Their shared runs are extracted as in `02`/`13` (maximal forward matches of four or more
letters). Replicates with five or more runs are kept. p is the share of null sets whose best count is at least
the observed one.

**G3, plants.** 520 plants, 20 at each w from 5 to 30. Each draws s1, e1, s2, e2 uniform in 0–20, and a phrase of R
rows (R uniform in 4–min(8, L2′ // w)). The phrase sits at T2 plaintext offset o2 (uniform) and T1 offset
o1 = o2 + q·w, with q uniform in −10..10 among offsets that fit. So the true Δr is q, inside the searched range by
construction. Plaintext is held-out Spanish telegraph text (`01-solver/plaintext.py`, book 27738 excluded). The key is
random, and `transpo.col_enc` enciphers both bodies. The end letters are shuffled telegraph letters. Runs are
extracted as in G2(ii) and G1 is run on them. Recovery: the true w is among the geometries reaching the best
count; the stricter version also needs s1, s2, e1, e2 each within ±1. Also recorded: whether the true w is the
only w reaching the best.

**Added after the pre-registered run (not pre-registered).** Δr −10..10 only covers phrases whose plaintext
offsets differ by at most 10 rows (50 letters at w 5). So the observed runs and the same 10,000 null (i) sets were
also searched with Δr −125..125, every possible row offset (top alignment only).

## Run

From this folder:

    python3 -I fit.py --workers 7 > result.txt    # fresh: about 2.5 min wall, 9 CPU min on 8 cores
    python3 -I verify.py > verify.txt             # about 3 min, 2.5 CPU min

Per-replicate rows are cached in `out/` (gitignored), with the full lists of best geometries
(`g1_geometries_top.txt`, `g1_geometries_bottoms.txt`). Delete the JSON files to recompute.

## Result

All numbers are from `result.txt`.

**G1, observed.**

| variant | best count | geometries reaching it | subsets reaching it |
|---|---|---|---|
| top only (Δr −10..10) | **2** | 12,896 | NOCU+OEPM (w 24–27, 47–50; 12,631), NOCU+TRSP (w 5; 265) |
| top or bottom | **2** | 13,640 | the same two pairs; NOCU+OEPM also at w 29–46 |
| top only, Δr −125..125 (added) | **2** | 318 passes | the same two pairs (checked pair by pair) |

No three runs fit any geometry. Of the 21 pairs, only those two fit, and both contain NOCU. NOCU sits at T2
position 0. With s2 = 0 that is the top of the first column, and T1 17 is row 17 − s1 of T1's first column. So
NOCU fits rank 0 at almost any width (s2 = 0, s1 7–17, Δr 0–10), and a pair needs only one more run to line up.

**G2, nulls** (best count ≥ 2 is the observed):

| null | sets | best-count distribution | 95th / 99th pct | p |
|---|---|---|---|---|
| (i) random pairs, top only | 10,000 | 0: 965, 1: 5,345, 2: 3,477, 3: 209, 4: 4 | 2 / 3 | 0.369 |
| (i) top or bottom | 10,000 | 0: 620, 1: 3,895, 2: 4,882, 3: 599, 4: 4 | 3 / 3 | 0.549 |
| (i) top only, Δr −125..125 (added) | 10,000 | 0: 447, 1: 4,793, 2: 4,468, 3: 288, 4: 4 | 2 / 3 | 0.476 |
| (ii) shuffle pairs ≥ 5 runs, top only | 109 of 2,000 | 0: 25, 1: 59, 2: 25 | 2 / 2 | 0.229 |
| (ii) top or bottom | 109 of 2,000 | 0: 19, 1: 48, 2: 41, 3: 1 | 2 / 2 | 0.385 |

The shuffle pairs had 0–8 shared runs (mean 2.1), so 109 of 2,000 qualified.

**G3, plants** (520):

| measure | result |
|---|---|
| true w among the best geometries | 518/520 = 0.996 |
| true w and s1, s2, e1, e2 each within ±1 | 513/520 = 0.987 |
| true w is the only w reaching the best | 357/520 = 0.687 |
| planted best count | 5 to 30; **never below 5** |
| runs per plant | median 20; 3.1% have ≤ 7; 74% have ≥ 14 |

Median shared runs by w (min–max): w 5: 8 (5–9), 6: 9 (6–11), 7: 9 (7–14), 8: 10, 9: 11, 10–12: 13, 13: 16,
15: 18, 20: 22, 25: 28, 30: 33. The median best count equals w up to w 23, and runs 1–2 below w for w 24–30.
A phrase of R ≥ 4 rows leaves an R-letter segment in every column, so a K3 plant has about w true runs plus about two by chance.
The two misses are a w-10 plant beaten by a w-20 geometry (11 against 10) and a w-6 plant beaten by w 18
(7 against 6). When another width ties the true one (161 plants), in 73 every other width is a multiple of w (w 5 plants also
fit 10, 15, 20); in 47 a width within 1 of w ties (w 30 plants often also fit 31).

## Reading (script author's reading)

The main thread judges. This is how the script author reads the result against the pre-registered readings.

- **Reading 2 applies: K3 is refuted for w 5–60 with up to 20 untransposed letters at each end.** The observed
  best count, 2, is at the 95th percentile of null (i) (2) and of null (ii) (2), not above it. p is 0.37 and
  0.23. The control passes: the true w is recovered in 99.6% of plants (98.7% with the trims within ±1).
- The bottoms variant (shared closing) gives the same: best count 2, p 0.55 and 0.39. So does the added search
  over every row offset: best count 2, p 0.48.
- The two fitting pairs both use NOCU at T2 position 0, which fits almost any geometry. The other six runs fit no
  common geometry even in pairs.
- **The run-count reading is not met as written.** At w 5–12 the median plant has 8–13 runs, within a factor of two
  of 7. From w 13 upward the median is 16 or more. The run count alone counts against K3 only for w ≥ 13.
- The best count separates more sharply than the run count. No K3 plant at any w had a best count below 5:
  every column of a K3 plant carries a run, and those runs fit the true geometry. The telegrams' seven runs give 2,
  which random runs reach 37% of the time.

## Caveats

- The control covers w 5–30, the dispatch's plant range. For w 31–60 the refutation rests on the search alone.
  Above w 40 a 4-row phrase does not fit in T2's 160 letters (4 × 40 = 160), and above w 53 no T2 column holds
  four letters. So in that range K3 cannot make 4-letter runs from column segments at all.
- The check is strict: a run must lie wholly inside both columns. A true segment extended by chance letters
  across a column boundary fails it. This happens when the phrase fills most of a short T2 column; it is why the
  median best count falls 1–2 below w at w 24–30. The control measures this loss and still recovers w in 99.6%.
- If the phrase's plaintext offsets differ mod w, the two copies of a segment fall in columns of different rank.
  G1 does not model that. Such a phrase still leaves one shared run in every column, about w runs, so the
  run-count evidence applies to it as well.
- A phrase shorter than four rows leaves no column segment of four letters. K3 with such a phrase cannot explain
  the excess; the runs would be chance by construction.
- The long-column convention does not matter. The model needs only that one telegram's long columns include the other's.
  "First L′ % w plaintext columns long" (as in `transpo.col_enc`) and "last L′ % w long" both give that.
  Padding to a full rectangle is the case x = 0.
- Null (ii) keeps only 109 replicates, so its 99th percentile is coarse. It is 2 either way.
- Null (i) rarely puts a run at T2 position 0, where NOCU sits and fits almost anything. That favours the
  observed. The observed is at chance anyway.
- The bottoms variant needs L1′ ≡ L2′ (mod w). A closing with other lengths lands in columns of different rank and
  is not modelled, as above.
- The plants place the phrase so that the true Δr lies in −10..10. The added Δr −125..125 search on the
  observed runs and null (i) was not pre-registered. It was run after seeing the main result.
