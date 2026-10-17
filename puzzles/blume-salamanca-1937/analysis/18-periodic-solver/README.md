# 18-periodic-solver — sets of n ≥ 11 and Nihilist read by rows, with a solver that passes controls

**Question.** `15` found that `05`'s controls started the solver at the planted key. With independent seeds the old
hill climb recovers sets of 20 in 1/20 plants and Nihilist rows at n = 8 in 14/20, so sets of n ≥ 11 and Nihilist
read by rows are untested, not excluded (H4, H5). Does a solver built for the structure of these families pass
independently seeded controls, and if so, does either telegram read under them?

## Method (`setsolve.py`)
Both families write the plaintext in rows of n and permute the columns by one key. Sets of n read the rows in
order. The Nihilist rectangle read by rows also reorders the rows (any order; n × n squares with the same key on
rows and columns are a special case). In both, cipher position a + r·n + j is row r, cipher column j. So the columns
are known without search, and two columns that are neighbours in the plaintext make a plaintext bigram in every
row, whatever the row order. The key is the heaviest path through the n × n table of column-pair bigram scores.

1. **Stage 1.** Simulated annealing on that table (Spanish bigram log10, summed over the full rows). A move cuts a
   segment of the path and inserts it elsewhere; half the segments are short, half of any length. 8 restarts of
   4,000·n steps; the 3 best distinct paths go on.
2. **Stage 2.** Hill climb on the within-row Spanish quadgram score (log10 per quadgram; quadgrams that cross a row
   boundary are left out, so the score does not depend on row order), from each stage-1 path, patience 60·n, then
   every rotation of the row. The best is kept.
3. **Offsets.** An untransposed preamble of p letters leaves the sets starting at offset p mod n (with junk rows
   first if p ≥ n). The solver runs every offset a in [0, n) and keeps the best score. Letters before a and after
   the last full row are not scored, so any handling of a partial last set is covered.

The solver does not know the family. One target run per (telegram, n) covers both.

**Development (before this plan; seed streams "18-dev", "18-devscan", not reused).** `dev.py`, `dev_scan.py`.
At offset 0 and 615 letters: n 11–40 recovered 30/30 plants, both families, in 0.4–2.3 s. n 50: 6/6 after
segment lengths were widened and the rotation check added. n 60: 0/6 at this budget and 2/6 at double the
budget, every failure scoring below its own true key. With the offset scan and random preamble and tail of 0–20
letters: 20/20 plants at n 9, 14, 22, 33, 47 found the true offset; within-row neighbour accuracy 0.91–1.00.
Cost: about 0.09·n s per offset, so 200 s for one text at n = 47.

## Plan (written 2026-10-17, before any control, noise or target run in this folder; committed before the run)
The steps below are the pre-registration. Results go under "Result"; this section is not edited afterwards.

**Plants.** Held-out Spanish telegraph text (`01-solver/plaintext.py`, glossary book excluded). Total length 615
(T1) or 160 (T2) = p random letters + body + b random letters, with p and b drawn uniformly from 0–20. The body is
encrypted as sets of n (rows in order) or as the Nihilist rectangle read by rows (rows shuffled), key random.
The solver gets the whole 615 or 160 letters and n, never p or b.

**Seeds.** Separate string-keyed streams: "18-plant" (plant parameters and plant seeds), "18-control-solver",
"18-noise" (shuffles), "18-noise-solver", "18-target-solver" (drawn in a fixed order: T1 n = 8…50, then T2
n = 8…30). The control code asserts that the solver's first stage-1 start at the true offset is not the
planted order.

**Recovery.** A plant is recovered if, at the offset the solver chose, at least 90% of within-row neighbour pairs
in the decryption are neighbours in the body (`setsolve.adjacency_acc`; pairs with a preamble or tail letter left
out). This measure is free of row order and of the row's starting column, but for one pair per row.

**Bands and pass rule.** T1: n 8–10, 11–15, 16–20, 21–30, 31–40, 41–50. T2: n 8–10, 11–15, 16–20, 21–30. For each
(telegram, family, band), 10 plants with n uniform in the band. A band passes if at least 8 of its 10 plants are
recovered in **both** families. A band that fails is "not testable" and its target runs are not read.

**Noise ceiling.** The same solver, offset scan included, on 3 shuffles of T1 at n = 10, 15, 20, 30, 40, 50 (each
band's top n, where a longer key fits noise best) and 3 shuffles of T2 at n = 10, 15, 20, 30.

**Threshold, per (telegram, band), fixed after controls and noise and before the target:** halfway between the
band's highest noise score and the lowest solver score among the band's recovered plants (both families). If the
two overlap, the threshold is the noise maximum, and a target score above it is checked against the dive's
criteria by reading. Written to `thresholds.json` and into this README before the target runs; `run.py target`
refuses to run without it.

**Target.** T1 at every n 8–50, T2 at every n 8–30, in passing bands. Record the best score, offset and order per n,
with the first 80 letters of the decryption.

**Candidate rule.** A target score above its band's threshold is a candidate. A candidate goes to the dive README's
criteria (whole text reads under one stated system; T2 under the same system; independent re-decrypt). For the
Nihilist reading, row order is recovered after the key, by a separate step written then.

### Not covered, and why
- **n > 50 for T1.** Development shows the method fails at n = 60 (10 rows). A key of more than 50 places is beyond
  any documented hand system.
- **One key on both telegrams.** If T1 alone is excluded at n, a shared key adds nothing at n. Joint search would add
  power only where T1 alone fails (n > 50).
- **Nihilist squares whose partial last row the row key moves into the middle.** The rows after it are offset
  differently from those before. Not modelled; the offset scan would see only the larger aligned part.
- **Nihilist read by columns.** Ciphertext columns there are also at known positions when the squares are complete,
  so the same method applies. Not run here.

## Run
```
python3 -I setsolve.py                 # self-test
python3 -I run.py controls             # -> controls.jsonl
python3 -I run.py noise                # -> noise.jsonl
python3 -I run.py thresholds           # -> thresholds.json (from the two files above)
python3 -I run.py target               # -> target.jsonl (refuses without thresholds.json)
python3 -I run.py summary > result.txt
```

## Result

### Controls, noise and thresholds (2026-10-17, fixed before any target run)
`controls.jsonl` (200 plants), `noise.jsonl` (30 runs), `thresholds.json`. Recovered / 10 per family:

| telegram | band | sets | Nihilist rows | recovered plants' scores | noise max | threshold | verdict |
|---|---|---|---|---|---|---|---|
| T1 | 8–10 | 10/10 | 10/10 | −4.32 to −4.11 | −6.28 | −5.30 | pass |
| T1 | 11–15 | 10/10 | 10/10 | −4.36 to −4.08 | −6.16 | −5.26 | pass |
| T1 | 16–20 | 10/10 | 10/10 | −4.30 to −4.07 | −6.00 | −5.15 | pass |
| T1 | 21–30 | 10/10 | 10/10 | −4.39 to −3.94 | −5.77 | −5.08 | pass |
| T1 | 31–40 | 9/10 | 10/10 | −4.35 to −4.02 | −5.48 | −4.91 | pass |
| T1 | 41–50 | 8/10 | 10/10 | −4.26 to −3.97 | −5.34 | −4.80 | pass |
| T2 | 8–10 | 9/10 | 9/10 | −5.08 to −4.06 | −5.65 | −5.36 | pass |
| T2 | 11–15 | 9/10 | 8/10 | −4.93 to −4.04 | −5.09 | −5.01 | pass |
| T2 | 16–20 | 3/10 | 4/10 | — | −4.95 | — | not testable |
| T2 | 21–30 | 3/10 | 1/10 | — | −4.53 | — | not testable |

Every T1 failure (3 of 120, all sets of n at n 40–50) scores below its own true key and reads 79–89% of
neighbours. At 160 letters and n ≥ 16 most failures score **above** their own true key (rows of 5–10 letters let
a wrong key fit better than the right one), so no search budget would fix those bands. T2's 11–15 margin is
narrow (noise −5.09, lowest recovered −4.93).
