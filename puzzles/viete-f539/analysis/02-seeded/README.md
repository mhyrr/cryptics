# 02 — seeded values: how much does a crib or key fragment have to supply?

**Frozen 2026-10-03, before any run.** Tests H6.

## Question
Experiment 01 showed that ciphertext-only annealing fails on an f. 539-shaped text
(344 tokens, 145 signs: median 0.093). Marmont was solved from 33 published values.
How many known values does an f. 539-shaped text need before the same solver recovers
the rest? And does a crib at the start of the text (where f. 539's cipher continues
"sinon que") supply enough?

## Method
- The solver, model, corpus, scoring, schedule (T0 12, 500k steps, 12 restarts) and
  control generator are those frozen in `../01-annealing/` (imported, unchanged), with one
  addition: a `fixed` map. Fixed signs start at their true letter and are never moved.
- Every control is N = 344 tokens, D = 145 signs, with 21 breaks, as in 01's PRIMARY cell.
  The control seeds are new (`7000 + …`), not 01's.
- **KEY cells** (key-fragment model): the k most frequent signs of the control are known,
  for k = 10, 20, 33, 50.
- **CRIB cells** (crib model): the plaintext of the first L tokens is known, so every sign
  occurring there is fixed, for L = 20, 40, 80. Position 0 matches f. 539, whose cipher
  begins straight after "sinon que".
- 3 seeds per cell. Seven cells, 21 runs.

## Measures and criterion
- **Accuracy on unseeded tokens:** the fraction of tokens whose sign was *not* fixed that get
  the true letter. Seeded tokens are excluded, so seeds cannot inflate the score.
- The coverage of the seeds (the fraction of tokens they cover) is reported per cell.
- **Pass:** median unseeded accuracy ≥ 0.80.
- **Reading:** the smallest passing k (or L) is how much a real key fragment (or crib) must
  supply. If no cell passes, seeded solving at this length is also out of reach, and the
  wall is "needs more text", not "needs a crib".

## Run
```
python3 seeded.py      # -> result.txt, runs.txt
```

## Result (2026-10-03; `result.txt`, `runs.txt`; secondary measure `overall.py` → `overall.txt`)
| Cell | Signs fixed | Token coverage | Unseeded accuracy (median) | Whole-text accuracy (median) | Verdict |
|---|---|---|---|---|---|
| KEY 10 | 10 | 0.15 | 0.229 | 0.345 | FAIL |
| KEY 20 | 20 | 0.29 | 0.339 | 0.531 | FAIL |
| KEY 33 | 33 | 0.43 | 0.585 | 0.763 | FAIL |
| KEY 50 | 50 | 0.58 | 0.555 | 0.813 | FAIL |
| CRIB 20 | ~20 | 0.20 | 0.315 | 0.466 | FAIL |
| CRIB 40 | ~34 | 0.34 | 0.475 | 0.659 | FAIL |
| CRIB 80 | ~62 | 0.54 | 0.484 | 0.757 | FAIL |

**No cell passes the frozen criterion.** At this length the solver cannot finish a key
from a fragment. Even the 50 most frequent signs (58% of tokens) leave it at about 55% on
the rest, because the remaining ~95 signs occur once or twice each and n-grams cannot pin
them.

Secondary reading (not the criterion, so it does not count as a pass): with 33–50 known
values, or an 80-letter crib, the whole text comes out 76–81% right. Outputs at that level
are near-readable ("muneetpopu|lai|res|ecrainsiqueetdesuerespourenxn" for "munsetpopulairesetlamusiqueetdesuersamoureux").
A human finishing from there, as Lasry did by hand on f. 555, becomes plausible, but not before.

Caveats:
- These controls assume every sign is a letter. F. 539 also has a marked series that is
  probably syllabic, and possibly nulls. The real case is harder than these cells.
- A crib of 80 letters at a known position is far more than the Rome news can supply
  verbatim. The candidate phrases (H8) are guesses at sense, not at wording.
