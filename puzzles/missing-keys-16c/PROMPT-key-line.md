# Prompt — run the key line (pilot, then batches)

Paste the block below into a fresh session in this repository.

---

Resume the dive `puzzles/missing-keys-16c`. Read, in this order: `CLAUDE.md`, the dive's `NEXT.md`, `README.md`,
`canon.md`, `hypotheses.md`, then `PIPELINE.md`. `PIPELINE.md` is the design; follow it. Where it and this prompt
differ, this prompt wins, and you note the difference in `research.md`.

**Goal.** Produce cipher keys nobody has written down, from class A items of Bourdeau's open catalogue: a cipher
letter with its period decipherment gives the key; the key is tested on held-out text; then it reads the bare
sibling letters. A key that fails its held-out test is recorded as failed. Applying someone else's published key
is not the result.

**Phase 0 — tools and calibration.** Do this yourself, on the main thread.
1. Build `line/` in the dive: `queue.py`, `ledger.tsv`, `align.py`, `compare.py`, `fluency.py`, with tests.
   Python standard library only.
2. Run both calibrations in `PIPELINE.md` ("Calibration before the first item"). Write each pass bar in the
   experiment README and commit before running. If one fails, fix the aligner and say what was wrong.
   Do not start an item until both pass.

**Phase 1 — pilot, one item.**
1. Pull a fresh `catalogue.json`, run `queue.py`, and gate the pilot candidate: no. 2192; if it fails the gate,
   no. 2345; if that fails, the head of the queue.
2. Take the item through stages 0–7. Write the stage 4 pass bar before the run.
3. Stop after the pilot. Report: the key's numbers, what each stage cost (agents, wall time), where it stuck,
   and what you would change in `PIPELINE.md`. Wait for Greg before Phase 2.

**Phase 2 — batches of five,** after Greg says go. Gate all five first, then work the `go` items. After each
batch update the ledger, append a batch note to `research.md`, and list the keys ready to announce.

**Agents.**
- Gate scouts and readers run on **Opus**. One scout per item. Two readers per side per page, isolated: a reader
  sees the sign guide and its own pages, never the decipherment, a key, or the other reader.
- Alignment, the key table, the held-out verdict, the reading and the sense check are **Fable** work: you, or one
  Fable agent per item, at most two at once.
- No agent may spawn agents. Say so in every dispatch. Each dispatch points at `CLAUDE.md`, `PIPELINE.md` and the
  item folder, states what the agent may write and where, and does not re-brief.
- Readers have an image budget of about 60 views each; give it in the prompt.

**Discipline.**
- Every number comes from a script in the dive, with its output checked in (rule 6).
- Findings land as they happen: true → `canon.md`; how learned → `research.md`; suspected → `hypotheses.md`.
- Unknown tokens stay unknown. No value is assigned from one context.
- Give an English translation beside every Spanish, Italian, Latin or French quotation.
- Commit small and by file name. Do not push.

**Stop and ask Greg** before: any message to Tomokiyo, Bourdeau, DECODE or an archive; reserving an item; anything
that needs a login or costs money. Stop the line, and say why, if two items in a row fail stage 4 for the same
reason, or if the queue pull shows the remaining items taken.

**End of session.** Run `/session-close`.
