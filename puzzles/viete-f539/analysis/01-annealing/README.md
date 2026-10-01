# 01 — homophonic annealing: pre-registration and matched control

**Frozen 2026-10-01, before any control or target run.** Changes after this commit
get a dated note below; they do not overwrite this section.

## Question
Can a homophonic annealer recover the key of a text shaped like f. 539? Only if it
can does a run on f. 539 mean anything.

## Why this experiment, after Bourdeau
Bourdeau's 2026-09-16 controls attacked only the 234 unmarked tokens, with the
marked signs as wildcards. They reached 1–18% key recovery. This experiment tests
the **most favourable** reading of the target instead: every non-numeric sign is a
single-letter homophone. If the solver fails under that assumption, every less
favourable structure (syllables, nulls, a nomenclator) is harder still, and the
wall is firm.

## Frozen choices
- **Solver:** `solver.py`, simulated annealing over sign→letter keys. Moves are
  reassign one sign (p = 0.5) or swap two signs. Temperature falls linearly from 12.0
  to 0 over 500,000 steps per restart, with 12 restarts in every cell. The highest final
  score across restarts is kept.
- **Alphabet:** 22 letters `abcdefghilmnopqrstuxyz` (j→i, v→u, k→c, w dropped, accents
  stripped, long s→s). No spaces: the cipher shows no word breaks (both blind readers).
- **Scoring:** the sum, over every 5-gram lying wholly inside a segment, of the 5-gram's
  joint log-frequency in training (unseen: log(0.1 / total)). Segments are split at
  numbers, which are treated as name codes of unknown length. The penalty is
  3 × N × KL(decrypted letter distribution ‖ training unigram distribution).
- **Corpus:** `fetch_corpus.py`. Brantôme, *Vies des dames galantes* (Gutenberg
  #39220), plus Montaigne, *Essais* I–III (Wikisource, the Bordeaux copy of 1595). The
  first 90% after normalization trains the model. The last 10% is held out and is the
  only source of control plaintext.
- **Controls:** held-out plaintext windows enciphered with D homophones allotted to
  letters in proportion to frequency, at least one each. Each token picks uniformly
  among its letter's homophones. Breaks are inserted at 21 random positions per 344
  tokens, matching the target's 19 Arabic and 2 Roman numbers.
- **Accuracy:** the fraction of cipher tokens whose recovered letter equals the true
  letter. Chance is about 0.06–0.15 depending on what the solver collapses to.

## Cells and criteria
| Cell | N tokens | D signs | Seeds | Role |
|---|---|---|---|---|
| PRIMARY f539-matched | 344 | 145 | 5 | **gate**: reader A's counts (the lower blind N and the smaller D) |
| POSITIVE marmont-shaped | 1300 | 155 | 3 | **solver validity**: must pass, or the solver is broken and nothing below counts |
| ladder N=700 / 1400 / 2800 | 700–2800 | 145 | 3 each | the length that would breach the wall in the same key |
| merge D=80 / D=40 | 344 | 80, 40 | 3 each | whether heavy merging of variant signs could rescue a short text |

- **Pass:** median accuracy ≥ 0.80 across the cell's seeds.
- **Decision rule:**
  - If POSITIVE fails, the solver is invalid. Fix it, re-register, rerun.
  - If PRIMARY fails, do not run the target. Record the short-text wall. The ladder
    names the breach: the smallest N that passes is how much same-key text, or the
    equivalent in known values, would be needed.
  - If PRIMARY passes, run the target on reader A's and reader B's transcriptions
    separately (12 restarts × 5 seeds each). A target result counts only if the seeds
    agree on ≥ 80% of tokens within each reading, and the two readings' decryptions
    agree with each other. Then judge it against README criteria 1–6.

## Tuning done before the freeze (off-protocol seeds, Marmont-shaped 1300 / 155 only)
Tuning used seeds that the protocol does not use (control seeds `k × 9973`); the
script was a scratch file in `out/`.
1. Conditional 5-gram scoring (add-k, with 4-gram interpolation) converged to junk
   ("zqx…", 0.06): unseen contexts scored better than real contexts with a wrong letter.
   It was replaced by joint log-frequencies.
2. Joint scoring alone collapsed to frequent letters ("esesete…", 0.33). The KL penalty
   was added. Weights 1, 3 and 6 were tried; 3 was kept.
3. At T0 = 8 with 4 restarts × 180k steps, 3 of 6 seeds solved. At T0 = 8 with 12 × 180k,
   2 of 4. At T0 = 12 with 12 × 500k, 6 of 6 solved (0.942, 0.965, 0.974, 0.978, 0.996, 0.997).
   That configuration is frozen. No tuning was run at N = 344 or on f. 539.

## How to run
```
python3 fetch_corpus.py          # out/corpus_raw.txt; 2026-10-01 SHA-256 a5319c5769cdcbc0a634a7b5209ba1ea1f9e7f5f21459ad571466f324aae93de
python3 solver.py model          # out/model.bin
python3 solver.py control        # control_result.txt (checked in)
```

## Result (2026-10-01; `control_result.txt`, per-seed lines in `control_runs.txt`)
| Cell | N | D | Accuracy by seed | Median | Verdict |
|---|---|---|---|---|---|
| POSITIVE marmont-shaped | 1300 | 155 | 0.985, 0.986, 0.993 | 0.986 | PASS: the solver is valid |
| **PRIMARY f539-matched** | **344** | **145** | 0.061, 0.064, 0.093, 0.142, 0.169 | **0.093** | **FAIL** |
| ladder | 700 | 145 | 0.26, 0.34, 0.694 | 0.340 | FAIL |
| ladder | 1400 | 145 | 0.986, 0.994, 0.999 | 0.994 | PASS |
| ladder | 2800 | 145 | 0.998, 0.998, 1.0 | 0.998 | PASS |
| merge | 344 | 80 | 0.224, 0.273, 0.343 | 0.273 | FAIL |
| merge | 344 | 40 | 0.994, 0.997, 1.0 | 0.997 | PASS |

**Decision (by the frozen rule):** PRIMARY fails, so the target is not run. Short-text wall.

What the numbers say:
- The same solver that recovers a Marmont-shaped key at 98.6% recovers 6–17% of a key shaped
  like f. 539. That holds even when every sign is assumed to be a plain letter homophone, which
  is more favourable than any structure the readers see.
- The failed control outputs read as fluent French ("…ementquestetdelamesentencontenno…",
  "…laplusestileseroit…") at 6–9% accuracy. A fluent-looking run on f. 539 would therefore be
  no evidence. This is the false-solution signature Bourdeau reported on the target itself.
- Breach by length: with about 145 signs, the passing point lies between 700 and 1,400 tokens of
  same-key text. F. 539 has 344, so it needs 2 to 4 times its own length.
- Breach by merging: only at about 40 signs does 344 tokens suffice; 80 still fails. The blind
  readers' *unmarked* inventories alone are 105 (A) and 128 (B) labels, and Bourdeau's are 79.
  Merging variant shapes cannot bring the inventory near 40.
- Not measured: crib-seeded or known-value-seeded solving (Marmont started from Tant's 33
  values). That is the next control to run if a crib or partial key turns up.
