# 03 — Transfer fragments from other seed families

**Question:** can recurring letter sequences supply choices that symmetry leaves
free, without guessing a language or consulting the target's complete rows?

Training rows, columns and reversals supply fragments of lengths 3–5 and whole
rows. A candidate must match at least two visible letters. Each donor group has
one vote, split equally among its compatible target letters. At least three
donor groups and 90% agreement are required. Prefer more observed positions,
then longer context, then more donor groups; conflicting tied contexts abstain.
Copies of one sequence within a grid do not create independent evidence.

The five fixed folds exclude each target group from its donor vocabulary.
The second declared variant fills from experiment 02, then makes one fragment
pass. Its additional predictions are scored separately, including propagated
errors. Proposed changes to visible letters are never applied.

Run from the repository root after generating the shared manifest:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/stressbench/common.py
python3 puzzles/book-of-abramelin-squares/analysis/03-fragment-transfer/run.py
```

Shared controls and tests: [stressbench](../stressbench/README.md).
Scores: [RESULTS.md](RESULTS.md). Audit: [results.json](results.json).

**Result:** with whole symmetry orbits hidden, 2/10 predictions match, covering
1.2% of 841 hidden cells. Three folds make no predictions. The matched symmetric
subset gets 0/8; its orbit-shuffled control gets 4/4, all also matched by the
frequency baseline. That sparse result gives no reliable recovery method.

On scattered blanks, fragments alone get 4/16 right. Adding fragments after
frames supplies four extra guesses: two right and two wrong. On boundary-only
tasks it adds four guesses, all wrong. The standalone method recovers all
320 planted motif centers in 80 held-out synthetic grids. The composed method
misses one because the frame stage supplies a wrong letter that it retains.

**Decision:** weaken the present fragment-transfer hypothesis. There may be
words or names here, but a small corpus-derived inventory at these thresholds
does not recover them reliably. No multilingual dictionary, linguistic mapping,
caption information or period lexicon was supplied; those remain distinct tests.
