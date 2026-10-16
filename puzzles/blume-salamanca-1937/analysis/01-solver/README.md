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
