---
description: Open or resume a multi-session deep dive on one puzzle. Creates puzzles/<slug>/ from the template if it does not exist, otherwise loads the handoff and continues.
argument-hint: <slug> [optional: what to do this session]
---

# Focus on one puzzle

**Input:** $ARGUMENTS

The first word is the slug (must match `catalog/entries/<slug>.md`). The rest,
if present, is the session's goal.

## If `puzzles/<slug>/` does not exist
1. Read the catalog entry. If there is none, write it first (`/catalog`), then
   come back. A dive without an entry has no admission test and no
   falsifiability clause.
2. `cp -r puzzles/_template puzzles/<slug>` and fill `README.md`: brief,
   status line, and the "What a solution would have to do" criteria copied
   from the entry and sharpened into numbered, testable conditions.
3. Seed `canon.md` from the entry's established facts, each with source and
   confidence. Seed `hypotheses.md` with the field's existing hypotheses
   (from "Prior attempts") so we start from the literature, not from zero.
4. Under `sources/`, pull the best machine-readable transcription if one
   exists; record it in `PROVENANCE.md`. If none exists, that is finding #1:
   write it in `NEXT.md` as the first wall.
5. Add the slug to `NEXT-SESSION.md` under Active dives. Create a HIVE ticket
   tagged with the slug if one does not exist.

## If it exists
Read in this order and nothing else first: `NEXT.md`, `README.md`,
`canon.md`, `hypotheses.md`. Search `research.md` rather than reading it end
to end. State in two lines where the dive stands and what this session will
do, then do it.

## While working
- A finding lands in the right file as it happens. True → `canon.md`.
  How learned → `research.md` (dated, newest first). Suspect → `hypotheses.md`.
- Any statistic or match comes from a script in `analysis/NN-name/` with a
  README and a checked-in result. Never from impression (AGENTS.md rule 6).
- One hypothesis test per subagent when fanning out. Synthesis stays here.
- Judge every hypothesis against the numbered criteria in `README.md`.
- When you hit a wall, name it exactly and what would breach it. Stop there.

## Finish
Run `/session-close`. Do not end a session without it.
