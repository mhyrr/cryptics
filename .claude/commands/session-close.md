---
description: Write the handoff before ending a session — rewrite the puzzle's NEXT.md, update NEXT-SESSION.md, verify nothing is stranded, stage by name.
argument-hint: [optional: slug of the puzzle in focus]
---

# Session close

**Input:** $ARGUMENTS

A session without a handoff loses its value to the next one. Do these in
order.

1. **Findings are filed.** Anything learned this session is in `canon.md`,
   `research.md` (dated entry, newest first), or `hypotheses.md`. Nothing is
   only in the conversation. Every hypothesis touched has a current status.
2. **Analysis is reproducible.** Each `analysis/NN-*/` touched has a README
   with question, method, run command, result. Outputs summarized and checked
   in.
3. **Rewrite `puzzles/<slug>/NEXT.md`** (if a puzzle was in focus): last
   session date, where it stopped, the first thing to do next, open questions,
   the named wall if any. Rewrite, do not append.
4. **Update `NEXT-SESSION.md`** at the repo root: which dives are active,
   one status line each, and what the next session should pick up.
5. **Catalog touched?** `python3 scripts/validate.py && python3 scripts/rank.py`.
6. **HIVE.** Add a ticket note on the puzzle's ticket with the session's
   outcome in two or three lines. Write a HIVE memory for any decision or
   durable fact the files alone would not make obvious.
7. **Git.** `git status`. Stage changed files by name. Commit with a message
   that says what moved. Do not push unless asked.

Close with a three-line recap: what was found, what was filed, what is next.
