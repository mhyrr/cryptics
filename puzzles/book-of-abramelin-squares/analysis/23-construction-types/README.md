# 23 — Are there construction types?

**Result.** No seed-closed type. By the rule frozen in
[PROTOCOL.md](PROTOCOL.md) before the run (commit `56f0c57`), H26 is
**weakened**: Mathers shows no excess of squares whose interior letters come
from their own top row, and the Warburg print does not replicate one. The
square that prompted the test, Dresden APPARET, is unremarkable once its
common letters are allowed for.

## Question

Experiment 16 found interior letters reuse seed letters at the chance rate on
average. Could a small subset of squares be built from their seed's letters
and hide inside that average? Dresden IV.4.3 (APPARET) draws 8 of its 9
interior orbits from the seed; IV.4.2 (ETHANIM) draws 6 of 9.

## Frozen run

Per square: z of the observed closure against the square's closure under every
other seed of its size. D = Σ z² measures spread; U counts squares at z ≥ 2.
Null: seeds permuted within size class, 5,000 times. Motivating squares out.

| Corpus | Squares | D (null mean) | p | U (null mean) | p | Rule |
|---|---:|---:|---:|---:|---:|---|
| M, Mathers | 129 | 158.0 (130.0) | 0.051 | 5 (3.7) | 0.31 | weakened |
| W, Warburg print | 101 | 105.6 | 0.40 | 4 | 0.45 | not replicated |
| D, Dehn | 50 | 69.3 | 0.030 | 2 | 0.49 | — |

Excess closed squares in M: 1.3, 95 % interval −3 to 4.

Secondary, all within chance: closure against checkerboard conformity
ρ = −0.02 (p 0.83); dictionary seeds against the rest, mean z −0.34 (p 0.17).
Stratifying references by seed alphabet size (S2): D p 0.19, U p 0.16.

Dresden, descriptive against Mathers references: APPARET z 1.94 (8 of 9,
expected 3.9); ETHANIM z 1.29. APPARET's letters A, P, R, E, T are among the
commonest in the corpus, so any interior shares many of them.

The five Mathers squares at z ≥ 2 are listed in `results.json`
(`named_M_z_ge_2`): HOLOP, ORIMEL, QELADIM (two visible orbits), ARITON,
ROGAMOS. They have near-perfect checkerboard conformity, the opposite of the
APPARET pattern.

Calibration as frozen: planted closure in 19 squares is found (p 0.001 on
both D and U); homogeneous fill never reaches the supported rule (0 of 20).

## Estimator correction, 2026-09-26, after the run

P0 also shows 7 of 20 homogeneous replicates at p(D) < 0.05, where about one
is expected. Cause: the observed z standardises against references that
exclude the square's own seed, while a permuted seed usually lies inside
them, so observed z is wider than null z. D is anti-conservative. The frozen
verdict survives, because the bias favours support and support still failed.

[`corrected.py`](corrected.py) is post hoc. It uses every seed of the size,
the own seed included, so the moments do not depend on the assignment and the
permutation is exact. P0 then gives 1 of 20 at p(D) < 0.05.

| Corpus | D p | U p | Vowel orbits D p | Consonant orbits D p |
|---|---:|---:|---:|---:|
| M | 0.23 | 0.31 | 0.08 | 0.08 |
| W | 0.82 | 0.96 | 0.012 | 0.99 |
| D | 0.34 | 0.80 | 0.15 | 0.87 |

The frozen S3 vowel result (D p 0.003) was the estimator's bias. One of six
split tests at 0.012, in one witness only, is not a finding.

## Reading

The squares do not split by seed closure. Seed letters enter the interior
at the rate their frequency predicts, square by square, not only on average.
APPARET looked like a type because an eye counts matches without asking how
many a random interior would share with A, P, R, E, T.

## Limits

Discovery data, seen before the test. Squares with fewer than two visible
interior orbits are out, so Mathers contributes 129 of 232. W and D repeat
authored squares; they test transmission and reading, not new compositions.
Other typologies (Kollatsch's symmetry per frame, lexical centre rows) are
not tested here. A null result does not establish free choice.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/23-construction-types
python3 test_run.py        # 8 synthetic checks
python3 run.py --check     # frozen run, about 6 seconds
python3 corrected.py --check
```
