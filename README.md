# cryptics

A working repository for the class of historical texts that a human author
appears to have built to mean something, where substantial material survives,
and where no reconstruction of the intended meaning has yet convinced the
field. Not Linear A. Not the Indus script. Those wait for a bilingual. This
repo is for the Voynich, the Hypnerotomachia, the Derveni papyrus, *Wulf and
Eadwacer*: cases where a synthesis of textual history, source parallels,
symbolism, and computation could plausibly produce a new insight.

Two activities live here:

1. **The catalog.** A scored list of the greatest unsolved texts, built toward
   a "50 greatest" cut. Each candidate is one file in `catalog/entries/`, scored
   on the axes in `rubric/RUBRIC.md`. `scripts/rank.py` reads the entries and
   regenerates `catalog/INDEX.md`. Humans and LLMs write the entries; the script
   does the arithmetic.
2. **Deep dives.** One folder per puzzle under `puzzles/<slug>/`, designed to be
   worked across many sessions without losing state: what we believe now,
   how we learned it, which hypotheses are live, and what to do next.

Start with `AGENTS.md` for how to work here and `STRUCTURE.md` for where
things go. `NEXT-SESSION.md` says what is in flight.

## Quick commands

```
python3 scripts/validate.py          # check every catalog entry parses and scores are in range
python3 scripts/rank.py              # regenerate catalog/INDEX.md
python3 scripts/rank.py --top 50     # print the current top 50 by attackability
```

Python 3.11+ standard library only. Per-puzzle analysis that needs more
(numpy, an OCR model, a language model client) gets its own environment under
`puzzles/<slug>/analysis/` and says so in that folder's README.

## Slash commands

- `/catalog` — work the catalog: add, score, or re-score entries and rebuild the index.
- `/focus <slug>` — open a deep dive on one puzzle, creating the folder from the template if needed.
- `/session-close` — write the handoff before ending a session on a puzzle.
