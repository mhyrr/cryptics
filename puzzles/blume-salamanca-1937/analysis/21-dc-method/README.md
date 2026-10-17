# 21-dc-method — Lasry's double columnar figures against ours, and a passing control at w2 16–17

**Status: done for this session. Method research on plants only; no solver was run on T1 or T2.**

**In one paragraph.** No single factor explains Lasry's figures. Our IDP reproduces his own fitness-distance
curve (fig. 9.2) at his challenge geometry, and in his presumed setting (English, 599 letters) the K2 search
finds nothing at 18 × 19 or 19 × 20 (0 of 6). In every setting tried, the IDP brings a climb back to the true K2
only from within 2–4 swaps; completeness, alignment, length and language move that by about one swap at most,
while the share of keys inside it falls tenfold per unit of w2. The thesis does not state the length, budget or
trial count behind its 60% and 90%. What does work at 615 letters is spending evaluations: Lasry's full
neighbourhood climb with a budget of 50 M IDP evaluations per length pair passed two pre-registered controls,
**w1 2–15 × w2 16–17, 20 of 20**. w2 ≥ 18, and w1 ≥ 16 at w2 ≥ 16, remain behind a named wall (below).

## Question
`01-solver` recovers forward double columnar (CC) plants at 615 letters for w1 2–15 × w2 12–15 (30/30, 180 s) and
falls off a cliff at w2 ≈ 16. Lasry (thesis 2018, ch. 9.4.6) reports over 60% success at 19 × 20 and 90% at 18–19.
Which factor separates the two? Then either fix it, so that a method passes a planted control at w2 16–20 on
615 letters, or show the gap is real and name the wall.

## Sources read (2026-10-17)
- Lasry thesis, Kassel 2018, ch. 9.4.5–9.4.6 and fig. 9.2, full text via the Kobra DSpace API
  (handle 123456789/15274, bitstream `kup_9783737604598.pdf`), **SCHOLARLY**. Cached in `out/thesis/` (gitignored).
- Lasry's own IDP code, as ported to CrypTool 2 (`CrypPlugins/IDPAttack/IDPAnalyser.cs`, authors "George Lasry,
  Armin Krauß"), and his transformation set (`CrypPlugins/ADFGVXAnalyzer/common/TranspositionTransformations.cs`),
  https://github.com/CrypToolProject/CrypTool-2 (main, fetched 2026-10-17), **PRIMARY** for the implementation.
  Cached in `out/ct2/`.
- Schmeh's blog on the "Reloaded" challenges (2018), with Lasry's comment that his hill climbing "could not produce
  a solution" for keys longer than 27,
  https://scienceblogs.de/klausis-krypto-kolumne/2018/01/25/the-top-50-unsolved-encrypted-messages-13-double-column-transposition-reloaded/ ,
  **POPULAR**.

### What the thesis states, and what it does not
- States: the success figures ("over 60% for finding keys of length 19 and 20 for K1 and K2, respectively. For key
  lengths of 18 to 19 we even have a success probability of 90%"), the algorithm in five steps, the IDP
  definition, and a fitness-distance plot for K2 of length 23 (fig. 9.2).
- **Does not state** the ciphertext length, the language, the number of trials, or the time or iteration budget
  behind those figures, nor the subset sizes in steps 1–2. `research.md` (session 3) and `NEXT.md` say "simulations,
  599 letters, English". That is an inference from context (the challenge was 599 letters of English), not a quote.
  The only budget information is that the challenge itself was attacked by a server (i7, 8 cores, 20,000 IDP per
  second in all) left running over the 14 candidate length pairs during development.
- Fig. 9.2 (K2 = 23, 100,000 keys; length not stated): degradation D(x) reaches 46% of its plateau at one swap,
  70% at two, 84% at three, 90% at four, 95% at five. "3-partite swap" is not defined in the thesis; Lasry's CT2
  transformation set contains 3-cycles of single elements and cyclic rotations of three segments of length 1–3.

## Implementation, `01` against Lasry (thesis text and his CT2 code)
| item | Lasry | `01-solver` | matters? |
|---|---|---|---|
| IDP pair score | max over all start positions of both columns of the mean bigram log-frequency | same | — |
| IDP greedy | best pair first; no cycle until the last link; the last link closes the cycle (w1 links; CT2 code). The thesis prose says "until all columns have both neighbours" | same greedy, but stops at w1 − 1 links (no closing link) | tested (`idp=1`): no |
| K2 moves | full neighbourhood: cyclic segment slides, segment swaps, 3-partite swaps (≈ 1.1 w³ distinct moves: 5,727 at w = 18, 8,245 at 20) | random draw of one of four move types | tested (`climb=1`): basin about +1 swap from 1–2 swaps out |
| K2 climb | enumerate the neighbourhood, keep improvements, stop at a true local optimum | stochastic first improvement, **stop after 3 w² consecutive failures** (972 at w = 18, i.e. 17% of the neighbourhood) | tested: 2 hits against 1 per 6 runs at 13 × 17 |
| pre-pass | random keys → best subset → left-to-right swaps → best subset | 200 → 10 → left-to-right → 3 | sizes not stated by Lasry |
| K1 stage | trigrams | quadgrams | not tested (K2 is the cliff) |
| priors | key-phrase priors and fragment word-spotting (the challenge's two optimisations) | none | not used: unknowable for T1 |
| budget | not stated | 180–600 s per pair | yes, up to w2 = 17: 50 M evaluations passes; see section 4 |

## Method
`dcm.c` is a copy of `01`'s `dtsolve.c` with switches (header of `dcm.c`): `idp=0|1|2` (01's path / Lasry's
cycle / K1-consistent rescoring), `oracle=1` (probe only: the true K1 segment starts), `pmi=1` (PMI bigram table),
`climb=0|1` (01's stochastic climb / Lasry's full neighbourhood), `k1climb=0|1`, `space=0|1` (moves on the rank
array / the reading order; `space=1` was not used), and a budget counted in **IDP evaluations**, not seconds, so
that machine load does not change a result. Controls A and A2 ran on `out/dcm`, built from the source saved as
`out/dcm_ctlA_source.c` (hashes in `out/dcm_ctlA.sha256`); `idp=2` was added afterwards and built separately as
`out/dcm2` (`bin=dcm2`) so as not to touch the binary of a running control. The current `dcm.c` differs from the
control source only by the `idp=2` branch. Modes: `probe` (fitness-distance curve with Lasry's non-correcting swaps, random keys,
climb optima from random starts, and **basins**: the share of climbs started x swaps from the true K2 that
return to it), `k2` (the K2 stage alone; a hit is a K2 whose IDP reaches the true K2's), `solve` (the full method,
01's K1 stage), `k1` (the K1 stage given K2).

`run21.py` plants and drives. Spanish plants are `01`'s telegraph-style held-out text (`01-solver/plaintext.py`,
unchanged); English plants are prose from held-out books fetched by `fetch_en.py` (`en_manifest.json`,
`lm_en_summary.json`; 7.4 M training letters, Gutendex's author-year filter is loose). Plant keys and plaintext
offsets come from a SHA-256 stream keyed `plant|tag|i`; solver seeds from `solver|tag|i`. The solver aborts if a
random start equals the planted K2.

## How to run
```
python3 -I fetch_en.py                      # English corpus and tables; copies 01's Spanish tables to out/
cc -O3 -march=native -o out/dcm dcm.c -lm
python3 -I run21.py probe TAG LANG N W1 W2 TRIALS WORKERS climb=1 nclimb=10 nbasin=10 ptag=PLANTS
python3 -I run21.py k2    TAG LANG N "W1xW2" TRIALS WORKERS budget=... climb=1 ptag=PLANTS
python3 -I run21.py solve TAG LANG N "W1xW2" TRIALS WORKERS budget=... climb=1 idp=1
python3 -I summ21.py probe|k2|solve TAG ... out=NAME   # tables to results/NAME.md
python3 -I ballsize.py > results/ballsize.md
```
Outputs: `out/TAG.jsonl` (gitignored); summaries in `results/`. `chain2.sh`–`chain7.sh`, `ctlA.sh` and `ctlA2.sh`
are this session's runs in order (chain 6 was stopped after its first probe when `idp=2` failed). Chain 1 was
typed at the prompt:
```
python3 -I run21.py probe pr_es615_16x18_c0 es 615 16 18 3 3 ptag=P_es615_16x18 climb=0 idp=0 nclimb=10 nbasin=10
python3 -I run21.py probe pr_es615_16x18_c1 es 615 16 18 3 3 ptag=P_es615_16x18 climb=1 idp=0 nclimb=10 nbasin=10
python3 -I run21.py probe pr_en599_19x20_c1 en 599 19 20 3 3 ptag=P_en599_19x20 climb=1 nclimb=10 nbasin=10
python3 -I run21.py probe pr_en599_21x23_c1 en 599 21 23 3 3 ptag=P_en599_21x23 climb=1 nclimb=10 nbasin=10
``` Every run used at most 3 processes while experiment 17's tier 2 held 5 cores.

## Pre-registered control A (written 2026-10-17 15:04 EDT, before any control run)
Chosen from the pilots (`results/k2-pilots.md`): Lasry's climb with the closing link (`climb=1 idp=1`) gave 3 K2
hits in 9 runs at 13 × 17 against 1 in 6 for 01's climb on the same plants; w2 ≥ 18 is out of reach of any
budget this session can afford (10 × 20: 1 hit in 15 runs of 8 M evaluations).
- **Band:** w1 2–15 × w2 16–17, forward CC, 615 letters, Spanish telegraph-style held-out plaintext (`01`'s
  `plaintext.py`), Spanish model. Lengths drawn uniformly from the band by the plant stream, tag `ctlA`.
- **Method:** `dcm solve`, `climb=1 idp=1 k1climb=0`, `01`'s K1 stage and refinement, **budget 50,000,000 IDP
  evaluations per run**, one run per trial, the whole budget spent (no stop at a hit, as in a target run).
- **Trials:** 10.
- **Pass rule (`01`'s):** a trial is a full recovery if the final decryption matches the plaintext in at least 95%
  of positions, allowing a cyclic shift of up to 40. The band passes at ≥ 8 of 10.
- **Seeds:** plant stream `plant|ctlA|i`, solver stream `solver|ctlA|i`; the solver aborts if a random K2 start
  equals the planted K2.
- **Load:** the budget is counted in evaluations, so load does not change the result; wall time is reported only.
- Command: `python3 -I run21.py solve ctlA es 615 "2-15x16-17" 10 3 budget=50000000 climb=1 idp=1 k1climb=0`

## Pre-registered control A2 (written 2026-10-17 15:54 EDT, after A, before any A2 run)
A passed 10/10, but its draw put 8 of 10 trials at w2 = 16 and only one at w1 ≥ 13 (15 × 16, a complete K1
rectangle). A2 tests the hard corner of A's band on its own.
- **Band:** w1 12–15 × w2 17; otherwise exactly as A (615 letters, Spanish telegraph-style plants, Spanish model,
  `dcm solve climb=1 idp=1 k1climb=0`, the same binary as A, **50,000,000 IDP evaluations per run**, full budget).
- **Trials:** 10; plant stream `plant|ctlA2|i`, solver stream `solver|ctlA2|i`.
- **Pass rule:** `01`'s, as A: ≥ 95% of positions with a cyclic shift ≤ 40; the corner passes at ≥ 8 of 10.
- **What it decides:** if A2 fails, A's pass is reported as covering w1 2–12 × w2 16–17 only, with the corner
  recorded as not testable at this budget.
- Command: `python3 -I run21.py solve ctlA2 es 615 "12-15x17" 10 3 budget=50000000 climb=1 idp=1 k1climb=0`

## Results
Everything in sections 1–5 is a pilot (probes and K2-stage searches, not pre-registered); sections 6 and 7 are
the pre-registered controls. Tables: `results/probes.md`, `results/k2-pilots.md`, `results/ballsize.md`.

### 1. Our IDP reproduces Lasry's own fitness-distance curve
At his challenge geometry (English, 599 letters, 21 × 23, 3 plants), D(x) as a share of the random-key level is
0.43, 0.73, 0.86, 0.93 for x = 1–4 swaps. Fig. 9.2 reads 0.46, 0.70, 0.84, 0.90. The IDP is therefore implemented
equivalently, and the curve he calls "on average monotonic ... steeper as we get closer" is the same shape we see
at 615 letters of Spanish (16 × 18: 0.51, 0.81, 0.92, 0.96).

### 2. In every setting the climb returns to the true K2 only from 2–4 swaps away
"Basin" = climbs started x non-correcting swaps from the true K2 that end at it (full-neighbourhood climb unless
stated). Three plants per row; 8–10 climbs per plant and x.

| factor tested | setting | from 2 swaps | 3 | 4 | 5 |
|---|---|---|---|---|---|
| baseline, `01`'s climb | es 615, 16 × 18 | 14/30 | 3/30 | 1/30 | 0/30 |
| move set and climb (Lasry's full neighbourhood) | es 615, 16 × 18 | 20/30 | 4/30 | 0/30 | 0/30 |
| closing link (Lasry's CT2 IDP) | es 615, 16 × 18 | 10/24 | 2/24 | 0/24 | — |
| PMI bigram table | es 615, 16 × 18 | 13/24 | 5/24 | 1/24 | — |
| language | en 615, 16 × 18 | 14/24 | 3/24 | 0/24 | — |
| language and length (Lasry's presumed setting) | en 599, 19 × 20 | 19/30 | 4/30 | 0/30 | 0/30 |
| Lasry's challenge geometry (K2 rectangle 26 × 23 + 1) | en 599, 21 × 23 | 22/30 | 6/30 | 0/30 | 0/30 |
| K2 rectangle complete | es 612, 16 × 18 | 23/24 | 10/24 | 0/24 | — |
| K1 rectangle complete | es 608, 16 × 18 | 18/24 | 11/24 | 3/24 | — |
| alignment oracle (true K1 segment starts) | es 615, 16 × 18 | 16/24 | 9/24 | 4/24 | — |
| K1-consistent rescoring of the chain (`idp=2`, a practical stand-in for the oracle) | es 615, 16 × 18 | 9/24 | 0/24 | 0/24 | 0/24 |
| text length 1000 | en 1000, 19 × 20 | 24/24 | 18/24 | 4/24 | — |
| rows per K1 column: w1 = 13 | es 615, 13 × 17 | 19/24 | 8/24 | 1/24 | 0/24 |
| w1 = 10 | es 615, 10 × 20 | 18/24 | 7/24 | 2/24 | 0/24 |
| w1 = 6 | es 615, 6 × 20 | 18/24 | 14/24 | 9/24 | 2/24 |

Outside the basin there is no usable gradient: at four swaps D is 93–97% of the random-key level, with the
random keys' spread, and climbs from random starts end with 0–5 key elements right, mostly 0–2 (a random key has 1
on average). Completeness of either rectangle, knowing the alignment, 1000 letters instead of 600, and short K1
keys each add about one swap.
Language, the closing link and a PMI table add nothing. Fixing the segment starts from the K1 chain the IDP itself
implies (`idp=2`) reaches the oracle's value at the true key but collapses as soon as the chain is wrong, so its
basin is smaller, not larger.

### 3. Why a basin of 2–4 swaps is a cliff in w2
`ballsize.py` (exact counts): the share of all keys within 3 swaps of the true K2 is 10^-6.9 at w = 15,
10^-8.0 at 16, 10^-9.0 at 17, 10^-10.1 at 18, 10^-12.4 at 20 (within 4 swaps: 10^-5.7, -6.6, -7.6, -8.6, -10.8).
A search with no gradient outside the basin pays roughly the inverse of that share, so each unit of w2 costs about
a factor of 10, and a one-swap gain in basin buys only about two units of w2.

### 4. K2-stage hit rates (pilots, budget 8 M IDP evaluations per run, stop at the hit)
A hit is a K2 whose IDP reaches the true K2's; every hit was the exact K2. Failures ended 0.44–3.53 below the
true IDP: they are search failures, not selectivity failures.

| setting | runs | hits | rate per M evaluations |
|---|---|---|---|
| **Lasry's presumed setting, en 599, 18 × 19** | 3 | **0** | < 0.13 (95% bound) |
| **en 599, 19 × 20** | 3 | **0** | |
| es 615, 13 × 17, Lasry's climb | 9 | 3 | 0.057 |
| es 615, 13 × 17, `01`'s climb (same 6 plants as 6 of the 9) | 6 | 1 | 0.021 |
| es 615, 13 × 20 | 3 | 0 | |
| es 615, 10 × 18 | 6 | 1 | 0.024 |
| es 615, 10 × 20, both climbs | 15 | 1 | 0.009 |
| es 615, 6 × 20 | 3 | 1 | 0.055 |
| **es 615, 16 × 17** | 6 | **0** | < 0.06 (95% bound) |

8 M evaluations is about 400 s of Lasry's 2013 machine at his stated 20,000 IDP per second (8 cores). At the
measured rates (one to three hits per cell, so each rate is uncertain by a factor of about three), 80% of runs
would need about 30 M evaluations at 13 × 17, 70 M at 10 × 18 and 180 M at 10 × 20 (~1.3 h per length pair on one
core here). At w1 ≥ 16 no hit was seen at all: 16 × 17 ended 3.0–3.7 below the true IDP in all six runs.

### 5. Selectivity is not the problem
The true K2 sits 14–20 standard deviations above random keys at 599–615 letters (24–28 at 1000); the best of 2,000
random keys sits 3–4 above. A candidate list that contains the true K2, or a key within two swaps of it (D1 is
about half the gap, still ~8 sd clear), would expose it even among ~10^9 candidates.

### 6. Control A (pre-registered): **pass, 10 of 10**
`out/ctlA.jsonl`, `results/controls.md`. Every trial a full recovery (100% of positions, no shift needed); every
run's K2 search hit the true K2.

| trial | w1 × w2 | first ≥ 95% reading at (M IDP evaluations) | final score | CPU s for 50 M |
|---|---|---|---|---|
| 0 | 10 × 16 | 1.78 | −4.146 | 1348 |
| 1 | 11 × 16 | 4.82 | −4.110 | 819 |
| 2 | 7 × 16 | 0.51 | −4.099 | 436 |
| 3 | 2 × 16 | 0.04 | −4.128 | 76 |
| 4 | 15 × 16 | 0.42 | −4.047 | 809 |
| 5 | 12 × 16 | 0.89 | −4.104 | 1526 |
| 6 | 3 × 17 | 0.03 | −4.125 | 71 |
| 7 | 8 × 16 | 0.10 | −4.082 | 539 |
| 8 | 10 × 17 | 5.96 | −4.131 | 1334 |
| 9 | 4 × 16 | 0.14 | −4.178 | 206 |

Scores of recoveries −4.18 to −4.05, all above `01`'s candidate threshold of −5.10 (the same Spanish quadgram model
and per-letter score). The latest first recovery came at 6.0 M of the 50 M budget. Caveat on coverage: the draw put
8 trials at w2 = 16 and one at w1 ≥ 13, which is why A2 was registered.

### 7. Control A2, the corner w1 12–15 × w2 17 (pre-registered): **pass, 10 of 10**
`out/ctlA2.jsonl`, `results/controls.md`. Every trial a full recovery (100%, no shift); every K2 search hit.

| w1 × w2 | trials | first ≥ 95% reading at (M IDP evaluations) | final scores | CPU s for 50 M |
|---|---|---|---|---|
| 12 × 17 | 3 | 0.04, 0.11, 0.17 | −4.14 to −4.07 | 1518–1522 |
| 13 × 17 | 3 | 10.5, 15.4, 23.7 | −4.12 to −4.06 | 1805–1934 |
| 14 × 17 | 1 | 10.7 | −4.04 | 1140 |
| 15 × 17 | 3 | 0.64, 3.6, 6.2 | −4.14 to −4.02 | 801–806 |

The slowest recovery (13 × 17) came at 23.7 M of 50 M, so the budget has about a factor of two of margin in the
corner, not ten. With A, **20 of 20** planted trials recovered in w1 2–15 × w2 16–17 at 50 M evaluations per run.

### Answer: which factor separates Lasry's figures from ours
None of the candidate factors does. With the method as the thesis states it, in the setting the thesis implies
(English, 599 letters), our implementation reproduces his fitness-distance curve and finds no K2 at 18 × 19 or
19 × 20 (0 of 6). Rectangle completeness, language, 599 against 615, the IDP's closing link and the move set each
move the basin by at most one swap, and the cost of the K2 search grows tenfold per unit of w2 whatever the basin.
The 60% and 90% figures must rest on conditions the thesis does not state (text length, budget, number of trials,
how the simulated keys were made). They are not evidence that w2 ≈ 20 is reachable on 600 letters. Lasry himself
broke the challenge from a partial solution (a spotted word, then a known-plaintext search; thesis 9.4.6.2), not
from a converged hill climb, and in 2018 commented that his hill climbing could not produce a solution for the
Reloaded challenges, whose keys are longer than 27 (blog comment, POPULAR).

### Things in `01-solver` that look wrong or matter
1. **The K2 climb stops early.** `climb()` quits after 3·w2² consecutive failures (972 at w2 = 18), about 17% of
   Lasry's neighbourhood (5,727 distinct moves), so it often stops short of a local optimum. From one swap away it
   returned 24/30 times against 28/30 for a full-neighbourhood climb; from two, 14/30 against 20/30. Per
   evaluation at 13 × 17, on the same six plants: 1 hit against 2. It does not explain the cliff.
2. `01`'s README difference (i) says "the thesis assigns w1 links". Lasry's own code builds the same cycle-free
   greedy path and then adds the forced closing link. Tested (`idp=1`): no effect on the basin.
3. `dtsolve probe` draws swaps that can overlap or undo earlier ones (Lasry's protocol forbids it), so its D(x) at
   x ≥ 2 is slightly understated. The conclusions drawn from it stand.
4. `01` budgets are wall-clock seconds. During this session the load average was about 15 on 8 cores, so 180 s
   was not a fixed amount of search. `dcm` counts IDP evaluations.
5. `research.md` (session 3) and `NEXT.md` say Lasry's figures came from "simulations, 599 letters, English". The
   thesis states neither.
6. Not wrong, for the record: the IDP table is a joint log-probability (a PMI table made no difference), and the
   window may start only at a column's possible starts (Lasry's code also lets it end on a long column's last
   letter; negligible).

## Named wall (proposed wording for `NEXT.md`)
**Double columnar with w1 ≥ 16 and w2 ≥ 16, or w2 ≥ 18 at any w1, on 615 letters.** The IDP brings a climb back
to the true K2 only from within 2–4 swaps (2–3 at w1 ≥ 10); outside that it has no gradient. No IDP variant
(closing link, PMI table, K1-consistent starts), move set, language, length from 599 to 1000, rectangle shape or
alignment oracle widens that basin by more than about one swap, while the share of keys inside it falls about
tenfold per unit of w2. Measured: 16 × 17, no hit in 48 M evaluations; 10 × 18, one in 42 M; 10 × 20, one in
114 M. Lasry's 60% at 19 × 20 is not reproduced in his own presumed setting (0 of 6) and rests on conditions his
thesis does not state. **Breach:** K2 candidates from outside the search (a list of Spanish key phrases: the true
K2 sits 14–20 sd above random keys, so even 10^9 candidates stay selective, and a phrase within two swaps of the
key still stands out), a crib, more text under the same keys, or, for w1 ≤ 10 and w2 18–20 only, a budget of
roughly 70–200 M evaluations per length pair, which would need its own control first.

## Proposed target run (for the main thread to approve; not run)
Both controls passed (A 10/10, A2 10/10).
- **Family and text:** forward CC, telegram 1 at full length (615), Spanish model.
- **Region:** w1 2–15 × w2 16–17, 28 length pairs.
- **Method:** exactly control A: `out/dcm solve CT w1=.. w2=.. lang=es seed=S budget=50000000 climb=1 idp=1
  k1climb=0`, one run per pair, seeds from a string-keyed stream (e.g. `solver|target21|w1xw2`).
- **Candidate rule:** final per-letter quadgram score above −5.10 (`01`'s threshold; control recoveries −4.18 to
  −4.05). A candidate goes to `01`'s criteria (whole-text reading, telegram 2, independent re-decrypt).
- **Cost:** from the controls' CPU times (measured at 7, 8, 10–15 and 2–4; 5, 6 and 9 interpolated), about
  10,000 CPU s per value of w2 summed over w1 2–15, so about 5.7 CPU hours in all; the longest pair (13 × 17) takes
  about 32 min. Under an hour on 8 free cores. The budget is in evaluations, so load lengthens it but does not
  weaken it.
- **What an empty result would add:** with `01` (w1 2–15 × w2 12–15, 30/30) and Bourdeau (w2 ≤ 15), forward CC on
  T1 at full length would be excluded for w1 ≤ 15 and w2 ≤ 17, for Spanish (and, by `01`'s H3 control, probably
  Italian and Portuguese, though that control was not repeated at w2 16–17).
- **Scope of an exclusion:** full length only. `15` showed any full-length columnar exclusion is void if 5–20
  letters at an end are not transposed; covering that means repeating the run on `17`'s truncated bodies.

## Target run (accepted by the main thread 2026-10-17 18:10 EDT, before any run on T1)
The proposal above, unchanged: forward CC, T1 at full length (615), Spanish model, w1 2–15 × w2 16–17 (28 pairs),
`out/dcm solve ... budget=50000000 climb=1 idp=1 k1climb=0`, one run per pair, seed `solver|target21|w1xw2`.
Candidate: final per-letter score above −5.10. The binary is the one controls A and A2 used: `target21.py` refuses
to run unless `out/dcm` matches `dcm_ctlA.sha256`; its source is checked in as `dcm_ctlA.c` (the current `dcm.c`
adds only the failed `idp=2` branch). The control records are copied to `results/ctlA.jsonl` and
`results/ctlA2.jsonl`. Three workers while tier 2 of `17` runs (the budget is in evaluations, so load does not
change the search).
```
python3 -I target21.py run 3      # -> results/target21.jsonl
python3 -I target21.py summary > results/target21.md
```

### Target result (`results/target21.jsonl`, `results/target21.md`, 2026-10-17)
**No candidate.** All 28 pairs of w1 2–15 × w2 16–17 score −6.22 to −6.00 (best 15 × 17), against the threshold
−5.10 and control recoveries of −4.18 to −4.02. No reading shows Spanish. **Excluded:** forward double columnar CC on
T1 at full length, w1 2–15 × w2 16–17. With `01`/`03` (w2 12–15) and Bourdeau (w2 ≤ 11): forward CC on T1 at full
length is excluded for w1 ≤ 15 and w2 ≤ 17. Full length only (`15`); the truncated bodies at w2 16–17 are not run.
