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

## Result
(pending)
