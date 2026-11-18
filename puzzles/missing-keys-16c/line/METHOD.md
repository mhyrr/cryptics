# From no key to a reading — the method as practised

Written 2026-11-18 from two items: no. 2911 (Machiavelli, 1510; a known answer, used as the bench) and no. 1336
(Speciano and Borromeo, 1574–75; no published key). `../PIPELINE.md` is the design. This file is what worked,
in the order to do it, with the command for each step. Every number below has a script and a result file in
the item named.

## What you need before you start
1. **A pair.** One passage in cipher and the same passage in clear: a period decipherment, a translation, a
   draft, a printed edition. Without a pair this method does not apply.
2. **Images you can cut into strips.** About 15 px of sign height is the floor. Below it readers agree at
   about 0.80 and you work with votes (step 3), not with one transcription.
3. **A second passage in the same cipher**, with or without clear text. It is the test of the key (step 5)
   and, if it has no clear text, it is the thing you came to read (step 6).
4. **Italian or Spanish of the period as plain text**, a few hundred thousand letters, for the letter model.

## The steps

| # | Step | Tool | Bar or stop |
|---|---|---|---|
| 0 | Gate: is a key already published? Is the pair real? | `items/<n>/gate.md` | Stop if a key exists: that is a known-key reading, another job. |
| 1 | Cut strips; freeze a guide that names signs by shape only | `items/<n>/strips.py`, `SIGN-GUIDE.md` | One revision of the guide, made from readers' notes, never from values. |
| 2 | Readers: isolated Opus agents, two or more per passage; cipher readers never see clear text | `reader-prompt-*.md` | Agreement by `compare.py`; 0.85 means one consensus text will do. |
| 3 | Under 0.85: add readers and merge by vote | `merge.py` | Needs three or more readers. |
| 4 | Build the key blind from the pair | `align.py build`, or `build --abridged` | The plain build stops itself when over half the places are null: rebuild with `--abridged`. |
| 5 | Test the key on text it was not built from | second pair, or shuffled-table controls | Registered before the run. |
| 6 | Read the bare passage: votes, the key, a letter model | `items/1336/lattice.py` | True table above 190 of 200 shuffled tables. |
| 7 | Write the reading with what each letter rests on | `items/<n>/READING.md` | `?` wherever no reader's sign has a value. |

## What we learned, by step

**Step 2. Readers.** Two readers who agree at 0.80 are not a failed transcription. They err at different
places. On c. 269r of no. 1336 the two-reader consensus left 143 of 768 places unread; a four-reader majority
left 77 of 784 (`items/1336/results/w2-merge.tsv`). Tell readers the true line count, or they disagree on
layout before they disagree on signs. Make the second pass run in the other direction.

**Step 3. Merge.** `merge.py` lines the readers up on one frame and keeps a sign with half the votes or more.
A doubtful sign (`x?`) is 0.7 of a vote; `x|y` is half each. Two readers who agree outvote two who disagree
with each other.

**Step 4. Build.**
- A period decipherment is rarely a letter-for-letter copy. On no. 2911, with the true key held, a sign spells
  the printed text at 55% of its places. A builder that assumes a close copy fills the table with nulls.
- What works on a loose pair (`build --abridged`): read the cipher in order with a pointer in the plain text; a
  new sign takes its value from the letters at the pointer and earns nothing; a repeated sign must spell its
  value to earn. Wrong guesses die because they fail to repeat. Then soft passes in a corridor round that path,
  repeated until the path settles.
- Mark rows by evidence, not by share: hits and misses against the chance that the value turns up anyway
  (three times its frequency in the plain text). On no. 2911 this marked 36 of 36 rows right on the first page.
- No null value unless a pair shows one directly.
- A short clean pair beats a long dirty one as the first table. On no. 1336 a 102-sign slip with a two-line
  note gave 17 values; the 795-sign slip was too blotted to start from.

**Step 5. Test.**
- A fixed accuracy bar is wrong for a loose pair, and a control scored with unvalued signs forgiven is wrong
  for a partial table: a shuffled table scored 0.46 that way. Count exact matches at held signs instead: with
  the table held, how many places spell the plain text, against tables with the values shuffled among the same
  signs. On no. 1336: 263 of 373 against 110 to 141.
- The strongest test is a second table built blind from a second pair. Count the signs both tables value and
  how many agree. On no. 1336: 13 of 14, then 23 of 24 after the four-reader merge.
- Write the bar before the run. When a bar turns out wrong, the test stays failed and the next test is
  labelled post hoc. Two of the five tests on no. 1336 failed as written and are recorded so.

**Step 6. Read a passage that has no clear text.**
- Do not ask each reader's decode to pass alone. Line the readers up as columns of votes. Each column's
  candidates are the key's values for the signs voted for. A letter-trigram model picks the path. The model may
  choose only among letters some reader supports; where no vote has a value the reading prints `?`.
- Control: the same procedure with shuffled tables. Self-check first on planted lines: on no. 1336's settings
  16 of 20 planted Italian lines pass and 1 of 20 random lines does.
- A place can be open for two reasons, and they need different cures. Readers disagree: a better image or more
  readers. Readers agree but the key has no value: more paired text. The reading file says which.

**Step 7. The reading.** Print the supported letters, the vote share of each, and `?` elsewhere. Word division
and the English gloss are interpretation and are marked as the writer's. The letter model's fill is shown
apart and is not evidence.

## What it costs
One item, from strips to a partial reading: about 12 Opus reader runs of two to four minutes each, and builds
of 20 seconds to a few minutes on one core. The long pole is the image, then the guide.

## Known limits
- The builder is fitted to one known answer (no. 2911). Its second use (no. 1336) is confirmed by two tables
  agreeing, not by a published key.
- The letter model is trained on Machiavelli's letters of 1500–1512. It is Tuscan and two generations older
  than no. 1336.
- Signs seen fewer than three times in paired text stay unvalued. A short bare passage will always have some.
- Nothing here handles a code list (signs for whole words) beyond leaving such signs unvalued.

## Where the pieces are
- Tools: `align.py`, `compare.py`, `merge.py`, `fluency.py`, tests in `test_line.py`.
- Bench with a sealed answer: `../items/2911/bench/README.md`.
- Worked item without one: `../items/1336/README.md` (every registered test, passed or failed), `run.py`,
  `lattice.py`, `READING.md`.
