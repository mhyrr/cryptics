# 24 — Does a square reuse its own interior letters?

**Result.** No. By the rule frozen in [PROTOCOL.md](PROTOCOL.md) before the
run (commit `0baba37`), H27 is **weakened**. Interior orbits of one square
share letters slightly *less* often than chapter-matched chance. The square's
other letters add nothing to a hidden letter's prediction, in Mathers or on
three witnesses.

## Part A — repetition inside squares

135 Mathers squares with at least two visible interior orbits, 732 orbits, motivating squares out. Rep counts same-letter pairs of
interior orbits in one square; the null permutes letters within chapter and
class, 5,000 times.

| Null | Rep (null mean) | p, excess | Rep_far (null mean) | p |
|---|---:|---:|---:|---:|
| within chapter × class (primary) | 191 (206.1) | 0.91 | 175 (186.9) | 0.86 |
| within class, corpus-wide | 191 (189.7) | 0.46 | 175 (171.6) | 0.39 |
| within chapter × size × class | 191 (204.5) | 0.99 | 175 (184.2) | 0.95 |
| S1, motivating squares restored | 199 (214.5) | 0.91 | 183 (194.7) | 0.85 |

The protocol tests excess only. Observed repetition equals the corpus-wide
expectation and falls below the chapter-matched expectations; under the
chapter × size null the lower tail is about 0.01. That direction was not
declared and is an observation, not a finding. One reading: the chapter
preference of experiment 16 comes from squares within a chapter sharing
material with each other, not from each square concentrating its letters.

## Part C — bits

Leave one orbit out, 732 orbits. The palette model's best K is 32, which
almost ignores the palette: 2.921 bits against 2.931 for class frequency,
accuracy 29.5 % against 29.1 %. The gain, 0.010 bit, equals the mean gain on
200 permuted corpora (0.010); p 0.40.

## Part B — frozen predictions on witnesses

Predictions come from Mathers only. The extraction reproduces the earlier
interior denominators exactly: W 349, D 193, R 50, and the checkerboard
class-mode scores 81, 61, 11 of experiments 20, 13, 22.

| Witness | Target orbits | class mode | palette | discordant |
|---|---:|---:|---:|---:|
| W, Warburg | 153 | 48 | 48 | 0 |
| D, Dehn | 78 | 26 | 26 | 0 |
| R, Dresden | 18 | 6 | 6 | 0 |

With K = 32 the palette never overturns the class mode on a witness target.
Given the true class, class mode is right on 100 of 349 Warburg cells.

Calibration: a planted two-letter palette in 30 % of squares is found
(p 0.001); homogeneous fill gives p < 0.05 in 0 of 20 replicates.

## Reading

Interior letters do not cluster within a square. Together with experiment 16
(chapter, prince, seed, position, size, neighbours) and experiment 23 (seed
closure types), no tested context predicts the letter beyond its class. The
tested contexts now include the square's own other letters, not only its
chapter, seed and neighbours.

## Limits

Discovery data for A and C. B scores frozen predictions on readings the main
thread had seen. A rule keyed to material outside the square and chapter is
not excluded. A null result does not establish free choice (H16).

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/24-square-palette
python3 test_run.py        # 8 synthetic checks
python3 run.py --check     # about 16 seconds
```
