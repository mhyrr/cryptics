# 20-nihilist-columns — the Nihilist transposition read by columns, n × n squares

**Question.** H4 lists Nihilist read by columns as open. In n × n squares read by columns, output column j holds
one plaintext column, with the square's rows in one order shared by every column. Rearranging each square turns the
ciphertext into the Nihilist rectangle read by rows, which `18`'s solver reads (controls 117/120 at 615). Is either
telegram a Nihilist transposition read by columns?

## Method (`nihcols.py`, `run20.py`)
From a preamble length p, every full square of n² letters is rearranged (grid row (s, i) = cipher letters
s·n² + j·n + i, j = 0 … n − 1) and solved by `18-periodic-solver/setsolve.solve` at offset 0, unchanged. Rows may be
in any order within a square, so the classic system (one key on rows and columns) is covered. The solver runs every
p in 0–20 and keeps the best. Letters before p and after the last full square are not scored.

## Plan (written 2026-10-17, before any control, noise or target run in this folder; committed before the run)
The steps below are the pre-registration. Results go under "Result"; this section is not edited afterwards.
- **Plants.** Held-out Spanish telegraph text; total 615 (T1) or 160 (T2) = p random letters + body + b random
  letters, p and b uniform 0–20. Full squares of the body encrypted as above (rows shuffled per square, key
  random); the partial last square left in clear. The solver gets the whole text and n.
- **Seeds.** "20-plant", "20-control-solver", "20-noise", "20-noise-solver", "20-target-solver" (T1 n = 5…24, then
  T2 n = 5…12). The code asserts the solver's first start at the true p is not the planted order.
- **Recovery.** At least 90% of within-row neighbour pairs at the chosen p are body neighbours
  (`setsolve.adjacency_acc` on the rearranged text).
- **Bands and pass rule.** T1: n 5–8, 9–12, 13–16, 17–20, 21–24. T2: n 5–8, 9–12. 10 plants per band; a band passes
  at ≥ 8/10. A band that fails is "not testable" and its target runs are not read.
- **Noise ceiling.** 3 shuffles of the telegram at each band's top n, same scan.
- **Threshold, per (telegram, band), fixed after controls and noise and before the target:** halfway between the
  band's highest noise score and the lowest solver score among its recovered plants; if they overlap, the noise
  maximum, and a target above it is checked by reading. Written to `thresholds.json` and here before the target.
- **Target.** T1 n 5–24, T2 n 5–12, in passing bands. **Candidate rule:** above its band's threshold, then the
  dive README's criteria.

### Not covered
- Preambles longer than 20 letters (the square grid would start later); n ≥ 25 (one incomplete square holds T1,
  and how a partial square is read is unknown); the whole-text rectangle read by columns with unequal columns.

### Amendment, 2026-10-17, during the controls and before any noise, threshold or target run
The plan let T2 plants at n = 12 have no full square: a 144-letter square does not fit 160 letters with a preamble
and tail of more than 16 (the solver crashed on a zero row count). The T2 band 9–12 becomes **9–11** (a 121-letter
square always fits), and the T2 target runs n 5–11. `solve_scan` skips offsets with no full square. T1 plants come
first in the "20-plant" stream, so they are unchanged, and no T1 offset lacks a full square (n ≤ 24, at least 595
letters), so the 43 T1 plants already finished stand. No plant of the old T2 9–12 band had finished.

## Run
```
python3 -I nihcols.py                 # self-test
python3 -I run20.py controls ; python3 -I run20.py noise ; python3 -I run20.py thresholds
python3 -I run20.py target ; python3 -I run20.py summary > result.txt
```

## Result
(pending)
