---
description: Work the catalog of unsolved texts — add, score, re-score, or review entries, then rebuild the index. Use for any catalog work that is not a deep dive on one puzzle.
argument-hint: [what to do — e.g. "add the Rök runestone", "second-pass the top 20", "re-score compute across ciphers"]
---

# Catalog work

**Input:** $ARGUMENTS

Cataloging, not solving. If you catch yourself testing a reading, stop and
open a deep dive with `/focus` instead (AGENTS.md rule 9).

## Orient
1. `AGENTS.md` rules 1–4 and 7. `rubric/RUBRIC.md` in full.
2. `catalog/INDEX.md` for where things stand. `catalog/EXCLUDED.md` so you do
   not re-propose a rejected candidate.
3. If the task names an entry, read it.

## Adding an entry
Copy `catalog/TEMPLATE.md` to `catalog/entries/<slug>.md`. Web search or fetch
every load-bearing fact; tier every source. Write "What a solution would have
to do" before scoring. Score all six axes; write one "Why the scores" line per
axis. Set `confidence` honestly.

## Re-scoring an entry
Change the scores in place. Add or extend a `## Revisions` section at the
bottom: date, which axes moved, from what to what, and why. Never rewrite the
old "Why the scores" line silently; append the new reasoning.

## Batch work (second pass, category sweep)
Fan out one subagent per entry or per category. Each dispatch points at
`AGENTS.md`, `rubric/RUBRIC.md`, and the entry; it does not re-brief. Read
the results on the main thread and make the judgment calls yourself.

## Finish
```
python3 scripts/validate.py && python3 scripts/rank.py
```
Commit the changed entries together with `catalog/INDEX.md`, staged by name.
Report what moved in the top 50 and why, in a short table.
