# 04 — Learned nonlinear local recurrences

**Question:** does a shared transition rule generate the interiors of new seed
families, as opposed to recognizing isolated local patterns?

Encode A–Z as 0–25. Fit lookup tables for `C = N + f(W)`, `C = W + f(N)` or
`C = f(N,W)` modulo 26, where N and W are the preceding row and column cells.
Four corner traversals give 12 configurations. Within each outer training fold,
hold out a deterministic quarter of its groups to select the configuration
with most correct one-step predictions. Refit the winner on all outer training
groups. Outer targets never select a rule.

Modal prediction uses the most frequent training outcome for a context, with a
fixed alphabetic tie-break. Confident prediction also requires 90% observation
agreement and support from at least three training groups. Unseen contexts
abstain. Recursive rollout uses visible cells and earlier predictions only;
one-step **teacher forcing** supplies the true neighbours and is explicitly
an oracle diagnostic. It cannot establish generation.

In addition to the common masks, a separate boundary test supplies the two
edges required by the traversal selected from training data. Keep this separate
from the common top-row/left-column mask: different corners have different
target cells. Changing which boundary is supplied does not consult target letters.

Run from the repository root after generating the shared manifest:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/stressbench/common.py
python3 puzzles/book-of-abramelin-squares/analysis/04-local-recurrence/run.py
```

Shared controls and tests: [stressbench](../stressbench/README.md).
Scores: [RESULTS.md](RESULTS.md). Every inner selection and outer prediction:
[results.json](results.json).

**Result:** selected-corner rollout gets 301/1,429 letters right (21.1% accuracy,
66.9% coverage), versus 262 correct for the frequency baseline on those cells.
One fold loses to that baseline. No task is fully reconstructed. No confident
prediction is made on any of the original masks. All outer folds select the
unrestricted pair lookup, not either additive family. Teacher forcing gets
415/1,911 right; that cannot be substituted for the rollout result.

The matched 55-grid symmetric subset gets 146/689 right in boundary rollout,
below its baseline's 156. Orbit-shuffling that subset gives 107/930. Modest
local structure in the full sample is not a reliable shared generator.

The synthetic control uses a fixed, randomly constructed nonlinear `f` with
random boundaries. Nested selection recovers the planted family; all 3,920
interior letters in 80 held-out grids are generated correctly, including the
confident variant. This is our A–Z construction inspired by the local-rule
question. It does **not** implement or independently replicate Reeds's Soyga
algorithm or its historical alphabet.

**Decision:** weaken these shared recurrence families as Abramelin generators.
This does not exhaust other alphabets, seed-specific rules, larger neighbourhoods
or mixtures of construction types. Any expanded search needs a new declared
test and stronger data, not a tuned claim against these reused outer folds.
