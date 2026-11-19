# From no key to a reading — the method as practised

Written 2026-11-18 from two items: no. 2911 (Machiavelli, 1510; a known answer, used as the bench) and no. 1336
(Speciano and Borromeo, 1574–75; no published key). Revised the same evening after no. 2351 (Acciaiuoli, 1513)
and a third leaf of no. 1336. `../PIPELINE.md` is the design. This file is what worked,
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
| 0b | Hold every published key of the same chancery and decade on the pair | `items/2351/results/held.tsv` is the model | Places that spell the plain text, against shuffled tables. A neighbour's key that fits is most of your key. |
| 0c | Find the design before building: count marks by base, sign types, repeats | `items/2351/results/marks.tsv` | Choose the builder by design (below). |
| 1 | Cut strips; freeze a guide that names signs by shape only | `items/<n>/strips.py`, `SIGN-GUIDE.md` | One revision of the guide, made from readers' notes, never from values. |
| 2 | Readers: isolated Opus agents, two or more per passage; cipher readers never see clear text | `reader-prompt-*.md` | Agreement by `compare.py`; 0.85 means one consensus text will do. |
| 3 | Under 0.85: add readers and merge by vote | `merge.py` | Needs three or more readers. |
| 4 | Build the key blind from the pair | `align.py build`, or `build --abridged` | The plain build stops itself when over half the places are null: rebuild with `--abridged`. |
| 5 | Test the key on text it was not built from | second pair, or shuffled-table controls | Registered before the run. |
| 6 | Read the bare passage: votes, the key, a letter model | `items/1336/lattice.py` | True table above 190 of 200 shuffled tables. |
| 7 | Write the reading with what each letter rests on | `items/<n>/READING.md` | `?` wherever no reader's sign has a value. |

## Choose the builder by the cipher's design
| Design, as the counts show it | Builder | Proven on |
|---|---|---|
| One sign for a letter or a syllable, no marks | `align.py build`, or `build --abridged` on a loose pair | no. 2911, no. 1336 |
| A base sign with a mark above: consonant and vowel | `items/2351/tied.py blind` (one value per base, one per mark) | no. 2351 |
| A code list: signs or numbers for whole words | none; such signs stay unvalued | — |

A builder passes a bench only on the pair it was shaped on, so far. Each new item is the test of the builder
as well as of the key.

## What we learned, by step

**Step 0. The gate.** On no. 2351 four stages of our own building failed, and then a key published for
another envoy of the same chancery a year later spelt the plain text at 383 places against 81 to 138 for
shuffled tables. Chanceries reused designs and often values. Test the neighbours' keys by script before
building anything. A borrowed key that reads the letter is a known-key reading and is reported as one.

**Step 0c. The design.** On no. 2351 the counts showed five marks on sixteen bases before any value was
known. Tying base and mark lets 21 values be learnt from 543 places, where an untied builder must learn 66
signs from about 8 places each and finds no path. Do not carry a value from one context to another without
evidence: the same base without its mark was a different sign, and assuming otherwise left 2 entries marked.
A cipher-only solve that had the design right still did not reach Italian. The pair is what carries a build.

**Step 2. Readers.** Two readers who agree at 0.80 are not a failed transcription. They err at different
places. On c. 269r of no. 1336 the two-reader consensus left 143 of 768 places unread; a four-reader majority
left 77 of 784 (`items/1336/results/w2-merge.tsv`). Tell readers the true line count, or they disagree on
layout before they disagree on signs. Make the second pass run in the other direction.
Run the clear-word readers first: on c. 652r of no. 1336 they found an eighth line of cipher that the scout's
count missed. Amend the readers' brief with a dated note beside the prompt, and leave the guide frozen.
Readers make up different names for one unknown sign (`n-dollar`, `n-phi8`, `n-sbar`); give the merge a
rename table made from their descriptions, never from values. Questions that every reader raises (here `q`
against `qx`) are the next guide revision.

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
- The order that makes a test clean, with a commit at each arrow: script and bar → readers' files → test
  result → decode. On c. 652r of no. 1336 this gave the first pass on that item that needed no label
  (above 200 of 200 shuffled tables). The commits are the proof of the order; timestamps within one minute
  are not.
- A value that a decode suggests is a lead, and it is not evidence on the passage it came from. To add it
  to the key, register a stage that holds out other text.

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

## Benching a builder against a sealed answer
Once an item has a confirmed key, it is a bench for the builders (no. 2911, no. 2351). The session that has
seen the values does not write builder code. One fresh agent gets the bar, the list of sealed files and the
list of what is fair to use; it proves each variant on planted pairs made as loose as the real one, registers
each real run before scoring, and reports counts, never values. Disclose in the bench file any lesson that
came from the answer and shaped the model.

## Running agents
- A usage limit stops every agent at once and none can be resumed. Readers must write their file after the
  first pass, and the handoff must say which files exist and which are unreviewed.
- A restarted reader writes to a new folder and is told not to open the old one.

## What it costs
One item, from strips to a partial reading: about 12 Opus reader runs of two to four minutes each, and builds
of 20 seconds to a few minutes on one core. The long pole is the image, then the guide.

## Known limits
- Each builder is fitted to one known answer (`build --abridged` to no. 2911, `tied.py blind` to no. 2351).
  The use on no. 1336 is confirmed by tables agreeing and by a registered test on a third leaf, not by a
  published key. No builder has yet passed on a pair it was not shaped on with a sealed answer.
- `tied.py blind` needs a foothold: 3 of 6 planted pairs of 450 to 600 signs fail. They fail visibly, with
  under ten signs marked.
- A reading is partial until the names and events in it are checked against outside sources. No reading here
  has had that check.
- Without a pair nothing here applies. Most open items have none.
- The letter model is trained on Machiavelli's letters of 1500–1512. It is Tuscan and two generations older
  than no. 1336.
- Signs seen fewer than three times in paired text stay unvalued. A short bare passage will always have some.
- Nothing here handles a code list (signs for whole words) beyond leaving such signs unvalued.

## Where the pieces are
- Tools: `align.py`, `compare.py`, `merge.py`, `fluency.py`, tests in `test_line.py`.
- Bench with a sealed answer: `../items/2911/bench/README.md`.
- Worked item without one: `../items/1336/README.md` (every registered test, passed or failed), `run.py`,
  `lattice.py`, `READING.md`.
