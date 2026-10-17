# 01-solver — double columnar solver after Lasry, Kopal and Wacker, with matched controls

**Question.** Can a divide-and-conquer IDP search recover the keys of a forward double columnar transposition of
615 letters of telegraph-style Spanish, and in which key-length bands? Only bands that pass go on to the target.

## Files
| file | role |
|---|---|
| `fetch_corpus.py`, `corpus_manifest.json` | Gutenberg books by language, train / held-out split (every 5th book held out) |
| `lm.py`, `lm_summary.json` | telegraph normalisation (A–Z, accents stripped, Ñ→N, digits spelled) and bigram/quadgram tables |
| `transpo.py` | reference transposition in pure Python, with hand-worked tests. Used to encrypt controls and for the independent re-decrypt |
| `dtsolve.c` | the solver (C). Modes `solve`, `idp`, `probe`, `bench`, `decrypt` |
| `test_engine.py` | C decryption == Python reference (300/300), and Python IDP speed |
| `plaintext.py` | telegraph-style control plaintext from held-out books |
| `control.py` | planted controls; results `controls/*.jsonl` |
| `probe.py` | fitness-distance probe of the IDP on a plant |

Build: `cc -O3 -march=native -o out/dtsolve dtsolve.c -lm`. Corpus: `python3 -I fetch_corpus.py es it pt && python3 -I lm.py`.

## Corpus
Project Gutenberg via the Gutendex API, authors alive 1860–1905 (the filter is loose and admits translations).
Two dictionaries and an English-language reader are excluded. Training letters: es 13.6 M, it 8.2 M, pt 6.0 M.
Book lists, splits and table hashes: `corpus_manifest.json`, `lm_summary.json`. Control plaintexts come only from
held-out books, transformed to telegraphese (`plaintext.py`: articles and QUE dropped at p = 0.7, PUNTO at
sentence ends, spelled quantities with units at p = 0.03 per word).

## Speed (measured)
Pure-Python IDP at w1 = 20: ~60 per second. C: 19,000 per second per core at 20 × 21, 42,000 at 13 × 13, 9,400 at
25 × 25. Lasry reports 20,000 per second on 8 cores. The inner loop is therefore in C, with a Python driver.

## Method, and where it differs from the thesis (Lasry 2018, ch. 9.4.5–9.4.6, read 2026-10-16)
Per iteration: (1) 200 random K2, keep the best 10 by IDP; (2) the left-to-right swap pre-pass on each, keep 3;
(3) hill climb each on IDP with swaps, segment slides, segment swaps and 3-partite swaps; (4a) K1 by hill climb on
quadgrams, seeded from the IDP's neighbour chain, plus 3 random restarts; (4b) alternate K2 and K1 climbs on the
full-decryption quadgram score until neither improves. Repeat until the time budget ends; keep the best.
Differences: (i) the greedy IDP assignment refuses links that close a cycle, so it yields one path of w1 − 1 links
(and a K1 seed); the thesis assigns w1 links. (ii) Climbs are stochastic first-improvement with a patience limit,
not full neighbourhood enumeration. (iii) Quadgrams, not trigrams, score K1 and the refinement. (iv) No key-phrase
priors and no fragment word-spotting (the thesis's two optimisations).

## Fitness-distance (probe.py, 2026-10-16)
On 615 letters the IDP is selective but a needle. Plant 16 × 18: true K2 −33.35; one random swap −35.67; two −36.96;
four −37.75; random keys −37.97; IDP climb optima −36.8 to −37.3 with 0–2 key elements right. Swaps restricted to
columns of equal length (no segment shifts) are barely smoother (−35.14, −36.52, −37.57 at 1, 2, 4). Plant 20 × 21:
the same shape. Lasry's challenge had K2 = 23 with 599 = 26 × 23 + 1, a nearly complete K2 rectangle, which may be
why his landscape was smoother. The method therefore needs to start within a few swaps of the true K2, which
caps its reach.

## Pre-registered pass rule (written before the band controls ran)
- A trial is a **full recovery** if the decryption matches the plaintext in at least 95% of positions, allowing a
  cyclic shift of up to 40 letters (an incomplete rectangle admits keys that read the right text displaced).
- A key-length band **passes** if at least 80% of its trials are full recoveries, with at least 10 trials,
  at the same per-length-pair time budget the target run will use.
- A band that fails is **not searched**; it is recorded as "not testable with this method".
- The **score threshold** for a target hit is set from the controls before the target run (next section).

## Band controls (615 letters, forward CC, Spanish model, 180 s per run, telegraph-style held-out plaintext)
Logs: `controls/*.jsonl`; table: `controls/summary.md` (from `summarize.py`).

| region | trials | full recoveries | verdict |
|---|---|---|---|
| w1 12–13 × w2 12–13 | 10 | 10 | **pass** |
| w1 14–15 × w2 14–15 | 10 | 10 | **pass** |
| w1 2–11 × w2 12–15 | 10 | 10 | **pass** |
| w1 16–17 × w2 16–17 | 10 | 0 | fail: not testable with this method |
| w1 8–15 × w2 16–17 | 10 | 7 (two more read 87–88%) | fail (below 80%): not testable with this method |
| asymmetric probes 13 × 20, 13 × 24, 20 × 13, 24 × 13 | 8 | 1 | fail: the K2 search fails at w2 ≥ 20; the K1 stage is unreliable at w1 ≥ 20 in 180 s |

Most recoveries in the passing region came within 10 s of a 180 s budget. The cliff at w2 ≈ 16 matches the
fitness-distance probe: the IDP has no usable gradient there at this length.

**Frozen target region for H1:** forward double columnar (CC), w1 2–15 × w2 12–15, Spanish model, 180 s per
(w1, w2) pair, one seed. Controls in this region: 30 of 30 recovered.

## Score threshold (fixed 2026-10-16, before any target run)
Per-letter quadgram score (Spanish model). In controls: full recoveries −4.89 to −3.98; partial readings (57–88%)
−4.89 to −4.85; noise failures −5.19 and lower. **A target run scoring above −5.10 is a candidate** and goes to the
README criteria (whole-text reading, telegram 2, independent re-decrypt). A run at or below −5.10 is noise. The
score alone never makes a hit: partial readings and full recoveries overlap near −4.87.

## Cross-language control (H3): Italian and Portuguese plants, Spanish model
`controls/xlang.jsonl`: 10 of 10 recovered (Italian 5/5, scores −4.68 to −4.88; Portuguese 5/5, −4.50 to −4.65),
region w1 2–15 × w2 12–15, 180 s. All above −5.10, so the H1 target run also tests Italian and Portuguese plaintext.

## Joint controls (H2): 615 + 160 letters under the same keys
`controls/joint16.jsonl`, `controls/joint16b.jsonl`. w1 8–15 × w2 16–17: **8 of 10** (one more read 88%) —
**passes** at exactly 80%. w1 8–15 × w2 18–20: 1 of 5 — fails, not searched. Telegram 2 moves the cliff by
about one key length.

**Frozen H2 target region (2026-10-16, before the run):** CC, both telegrams, shared keys, w1 8–15 × w2 16–17,
Spanish model, 180 s per pair, seed 1000, candidate threshold −5.10 (joint per-letter score).

## CR convention (stage 1 rows→columns, stage 2 columns→rows; Bourdeau's convention 3)
`controls/cr_band.jsonl`: w1 2–15 × w2 12–15, **8 of 10 — passes**. The two failures are both w1 = 2 and score the
same as their true plaintexts (−4.125 vs −4.126; −4.221 vs −4.231), so they are probably correct readings displaced
beyond the 40-letter shift tolerance. They are counted as failures, as the rule says.
**Frozen CR target region (before the run):** CR, telegram 1, w1 2–15 × w2 12–15, 180 s per pair, threshold −5.10.

## Note added 2026-10-17 (session 6, from `21-dc-method`)
- Difference (i) above misdescribes the thesis: Lasry's own code builds the same cycle-free greedy path, then adds
  the forced closing link. Tested in `21` (`idp=1`): no effect on the basin.
- The K2 climb stops after 3·w2² consecutive failures, about 17% of Lasry's full neighbourhood, so it often stops
  short of a local optimum (from two swaps away it returned 14/30 times, against 20/30 for a full-neighbourhood
  climb). This does not explain the cliff, and the band controls above measured this solver as it is, so `03`'s
  exclusions stand.
- `dtsolve probe` draws swaps that may overlap or undo earlier ones, so D(x) at x ≥ 2 is slightly understated.
- Budgets here are wall-clock seconds; under load (about 15 on 8 cores on 2026-10-17) 180 s is not a fixed amount of
  search. `21`'s `dcm` counts IDP evaluations.
- "Lasry's challenge ... may be why his landscape was smoother": `21` finds a complete rectangle widens the basin by
  at most about one swap.
