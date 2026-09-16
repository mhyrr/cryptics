# 02 — Independent frame rules with copying-error costs

**Question:** do different rules for concentric frames recover cells that exact
whole-grid symmetry misses? Can the model identify artificial copying errors
without changing the undamaged digital reading?

Each frame independently chooses among the ten subgroups of square symmetry,
including identity. Its fixed cost is `log2(26)` per observed orbit symbol plus
`log2(25 × .95 / .05)` per substitution needed to fit that orbit. This is a
simplified symbol-plus-error description cost, with a fixed 5% substitution
channel. It is not an estimated historical error rate. Group labels have equal
cost. Unobserved orbit symbols do not contribute evidence or predictions.

An orbit's unique majority supplies its candidate letter. All equally cheap
models must agree before a cell is filled or a visible reading is flagged.
Ties and entirely unobserved orbits abstain. Suggested repairs never modify
source cells. Frames are fitted to visible cells in each target; only the
frequency baseline uses the other folds.

Run from the repository root after generating the shared manifest:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/stressbench/common.py
python3 puzzles/book-of-abramelin-squares/analysis/02-frame-model/run.py
```

Shared splits, masks, controls and tests: [stressbench](../stressbench/README.md).
Full scores: [RESULTS.md](RESULTS.md). Per-cell predictions, clean-reading flags
and injected-error audit: [results.json](results.json), using zero-based cells.

**Result:** 555/591 predictions correct on scattered blanks (79.6% coverage),
versus 456/463 for strict whole-grid symmetry (62.4% coverage). Exact task
recovery falls from 30/81 to 18/81. Entirely hidden symmetry orbits yield no
predictions. With only a top-left boundary, the frame model gets 99/106 right
at 5.0% coverage, well below the global rule's 615/696 at 32.6% coverage.

On 60 planted grids with different frame types, 413/415 predictions are correct.
With one artificial substitution in each of the 81 source grids, 48/62 proposed
repairs restore the original letter; 13 proposals change an uncorrupted cell.
On the unmodified export, 12 letters in eight grids are flagged. Those could
include old errors, but the model provides no evidence that they are errors.

**Decision:** retain as a candidate completion and inspection tool. Do not use
it to rewrite a transcription or claim recovery of independent inner letters.
The fixed error cost and synthetic substitution distribution are assumptions;
actual scribal confusions and original frame choices remain untested.
