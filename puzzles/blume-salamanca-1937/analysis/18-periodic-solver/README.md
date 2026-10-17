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

### Target (`target.jsonl`, `result.txt`)
**No candidate.** Every target score is below its band's threshold. Best per band:

| telegram | band | best (n) | threshold | margin |
|---|---|---|---|---|
| T1 | 8–10 | −6.38 (10) | −5.30 | −1.08 |
| T1 | 11–15 | −6.09 (15) | −5.26 | −0.83 |
| T1 | 16–20 | −5.93 (20) | −5.15 | −0.78 |
| T1 | 21–30 | −5.65 (30) | −5.08 | −0.57 |
| T1 | 31–40 | −5.44 (39) | −4.91 | −0.53 |
| T1 | 41–50 | −5.19 (49) | −4.80 | −0.39 |
| T2 | 8–10 | −5.83 (10) | −5.36 | −0.47 |
| T2 | 11–15 | −5.37 (15) | −5.01 | −0.36 |

Target scores rise with n as the noise ceiling does (a longer key fits noise better); recovered plants sit
between −4.4 and −3.9 at every n. No reading shows Spanish.

**What is excluded now (controls pass, any preamble and any tail, since every offset was scanned and letters
outside full rows are not scored):**
- Letters permuted within sets of n, for T1 at n 8–50 and T2 at n 8–15.
- The Nihilist rectangle read by rows (any row order, so n × n squares under one key included), for T1 at n 8–50
  and T2 at n 8–15.
- Either family with one key on both telegrams, at n ≤ 50: T1 alone would have read.

**Not covered:** T2 at n 16–30 (controls fail: at 160 letters a wrong key outscores the right one); n > 50;
Nihilist squares whose partial last row moves into the middle; Nihilist read by columns.

### Post hoc check, written 2026-10-17 after the target and before this check ran (`excess.py`)
**Seen after looking:** at n = 15, 20, 30 and 50 the target scores 0.07–0.12 above all three noise shuffles
(far below every threshold). Three shuffles cannot price this. Long-key double columnar (K1, the top-ranked
family) should look like a shuffle to this solver, so an excess over shuffles could also weigh against K1.
**Check:** at n = 20 and 30, the same solver on 20 more shuffles of T1 ("18x-shuffle") and on 20 K1 plants
(forward CC, w1 and w2 uniform 16–25, 615 letters of held-out Spanish telegraph text, "18x-plant"); solver seeds
"18x-solver". The target values are the ones already in `target.jsonl`.
**Reading, fixed now:** (1) if the target lies inside the central 90% of the K1 plants at both n, the excess is
what K1 gives and says nothing new; (2) if it lies above the 95th percentile of both the shuffles and the K1 plants
at both n, it is a lead to be named in `NEXT.md`, not a finding (post hoc, and the two n were picked after
looking); (3) otherwise it is noise, recorded here.

**Result of the check** (`excess.jsonl`, `excess.txt`):

| n | T1 | 20 T1 shuffles: median, max; T1 above | 20 K1 plants: 5th pct, median, 95th pct; T1 above |
|---|---|---|---|
| 20 | −5.934 | −6.038, −5.969; 20/20 | −5.955, −5.815, −5.709; 3/20 |
| 30 | −5.648 | −5.765, −5.695; 20/20 | −5.709, −5.570, −5.446; 4/20 |

By the reading fixed above this is case (1): T1 lies inside the central 90% of the K1 plants at both n. Two points
the reading did not foresee. First, T1 is above all 20 of its own shuffles at both n, so its order carries
something this solver finds and a random order of the same letters lacks. Second, the comparison with K1 plants
mixes order with letter content. The plants are held-out Spanish, and T1's letters fit Spanish poorly (`08`), so a
plant can outscore T1 on its letters alone. The check therefore does not show that K1 produces T1's excess.

### Second post hoc check, written 2026-10-17 before it ran (`excess2.py`)
**Question.** Does a K1 plant exceed its own shuffles by as much as T1 exceeds its own? This removes letter content.
**Check:** n = 20. 20 K1 plants as in `excess.py` (stream "18y-plant"), each with 3 shuffles of its own letters
("18y-shuffle"); solver seeds "18y-solver". Excess = score − mean of its shuffles' scores. T1's excess uses the 20
T1 shuffles in `excess.jsonl`: −5.934 − mean(those 20).
**Reading, fixed now:** (1) T1's excess inside the central 90% of the K1 plants' excesses: T1's order fits K1 here.
(2) T1's excess above the 95th percentile of the K1 excesses: a lead against K1, named in `NEXT.md` (post hoc).
(3) Below the 5th percentile: T1 has less of this order than K1 gives, also named.

**Result of check 2** (`excess2.jsonl`, `excess2.txt`): T1's excess over its own shuffles at n = 20 is +0.106. The
20 K1 plants' excesses over their own shuffles run from −0.096 to +0.085 (median +0.013); T1 is above all 20.
By the reading fixed above this is case (2), a lead against K1 (post hoc, p ≈ 0.05).

**Follow-up.** `19-lag-profile` finds no letter-pair association at any lag in T1 or T2, and multi-lag sums inside
200 K1 plants. So pairs do not carry the excess. The offsets do: for n ≥ 15, T1's best offset leaves 15 or more
letters at the end out of the scored rows at 31 of 36 widths (17 expected if offsets were uniform), while shuffles
leave out tails of every length. T1's last 20 letters are the rare-letter-rich end `09` found (H6). A shuffle
spreads those letters through every row, so no offset helps it.

### Third post hoc check, written 2026-10-17 before it ran (`excess3.py`)
**Check:** n = 20. The solver on T1[0:595] (the last 20 letters removed) and on 20 shuffles of T1[0:595]'s letters
("18z-shuffle"; solver seeds "18z-solver"). **Reading, fixed now:** if T1[0:595] lies inside the central 90% of its
own shuffles, the excess in checks 1 and 2 was T1's rare-letter tail seen through the offset scan, and the lead
against K1 is withdrawn. If T1[0:595] is still above all 20, the lead stands and is named in `NEXT.md`.
