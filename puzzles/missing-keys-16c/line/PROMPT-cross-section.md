# Prompt: a cross-section of new keys

Paste this into a fresh session in `/Users/mhyrr/work/cryptics`. Written 2026-11-19.

---

Resume `missing-keys-16c` with one goal: **build new keys for a cross-section of five historically
significant cipher items, and read what they open.** An item enters only if it passes three gates: it
matters, its pages can be read from the images we can get, and our method can plausibly build its key.

Read first, in this order: `CLAUDE.md`; `puzzles/missing-keys-16c/NEXT.md`; `line/METHOD.md` (all of it; it
is the method and the order of work); the newest two entries of `research.md` (the survey of candidates).
Do not re-derive what those files settle.

## Stage 1. Choose the five (one session, no key work)

Start from the survey's candidates and the fresh catalogue (`sources/cache/bourdeau-catalogue-2026-11-18.json`,
importance 4–5, online). Add candidates from sources the survey skipped only if a scout finds them in two or
three fetches: DECODE's non-decrypted records, the Vatican, Venice, Simancas.

Seed list, by catalogue number: 2339 (Farnese intercept, 1547), 2395 (Giulio de' Medici, 1521), 1556 and 1554
(Ercole Gonzaga, 1545), 2945 and the Sforza chancery families (c. 1450), 2854 (Ferdinand to John II, 1478),
1561 (Prince Philip to Ferrante Gonzaga), 566 (Willem Lodewijk of Nassau, 1610), 2939 (Gordon, 1884),
1388 (Vaudreuil, 1759).

For each candidate write one row in `line/cross-section.tsv`, every cell from a script or a cited fetch:

| Gate | What to record | Pass |
|---|---|---|
| **Matters** | Who wrote to whom, when, and what unread text would add; one SCHOLARLY or PRIMARY source | Stated in one sentence a historian would accept |
| **Not taken** | `line/taken.py` against the outside repository; two or three searches for a printed decipherment | No key and no reading found; say what was not checked |
| **Readable** | Fetch one cipher page at the largest size served. Measure sign height in pixels by script | 15 px or more (METHOD, "What you need") |
| **Buildable** | Is there a pair (cipher and the same text in clear)? How many signs? A neighbour's published key of the same chancery and decade? The design, from counts (METHOD step 0c) | A pair of 100 signs or more, or a neighbour key to hold; a second passage for the test |

Then pick five that pass all four gates and differ from each other: spread them over century, chancery and
cipher design, and include at least one where the key would open more than one document. Write the choice
and the reasons for each rejection in `line/cross-section.md`. Rejected candidates stay listed with the gate
they failed.

**Stop and show Greg the five before stage 2.** The choice is his.

## Stage 2. One item at a time, METHOD.md as written

For each chosen item make `items/<n>/` and follow METHOD steps 0 to 7 in order. The rules that are easy to
break:

- Gate first (step 0, 0b, 0c): hold every published key of the same chancery on the pair before building.
  A borrowed key that reads the letter is a known-key reading; report it as that and move to the next item.
- Bars and scripts are committed before readers report; readers' files before the test; the test result
  before any decode is opened. The commits are the proof of the order.
- Readers are isolated Opus agents, two or more per passage, with a frozen shape-only guide. Cipher readers
  never see clear text. Clear-word readers run first.
- Key building, the held-out test and the reading run on Fable: the main thread, or one agent per item that
  may not spawn. No agent spawns agents.
- A value that a decode suggests is a lead. It enters the key only through a new registered stage that holds
  out other text.
- A failed test stays failed. The next test is labelled post hoc.
- When an item hits a wall (images too small, no path, a code list), name the wall and what would breach it
  in the item's README, and go on to the next item. One honest attempt per wall.

## What done means, per item

`items/<n>/README.md` with every registered test, passed or failed; a key table with each value marked
`certain`, `probable` or `unknown` and the places that support it; `READING.md` with supported letters, `?`
elsewhere, English beside every quotation, and interpretation marked as the writer's. Names, dates and
events in a reading are checked against at least one outside source, or the reading says they are not.

## Limits

- Nothing leaves the machine: no push, no pull request, no message to an archive or another project.
  Public fetches of images and catalogues are fine; use Python, not curl, and no personal details in requests.
- Readers save their file after the first pass. A usage limit can stop every agent at once.
- Keep `canon.md`, `hypotheses.md` and `research.md` current as findings land. Commit small, by file name.
  End every session with `/session-close`.

## Report at the end of each session

Per item: gate result; readers' agreement; signs valued; each test with its bar and its number; what was
read; the wall, if any. Then one line on what the cross-section says about the method: which designs and
image sizes it handles, and which it does not.
