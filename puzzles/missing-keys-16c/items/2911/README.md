# Item 2911 — the key line's pilot (known-answer run)

Written 2026-11-17, **before any transcription exists**. The pass bar in section 4 and the outside check in
section 5 are fixed here and are not to be changed after a run. Results will be added below section 6; nothing
above it is edited once the readers start.

## 1. The question

Can the key line (`../../PIPELINE.md`) rebuild a cipher key from one period pair, blind, well enough to
read sibling letters?

This run cannot make a new key. The period key survives and is online (BNCF Carte Machiavelli VI/82,
units 1-4; `gate.md` check 5, `keysheet-check.md`), which by the pipeline's rule gates the item out. Greg
approved running it anyway as a **known-answer pilot**: the key is rebuilt without sight of VI/82, and
VI/82 is then the answer sheet. What is under test is the line, not the cipher.

**Blindness.** The item agent and every reader stay away from `cache/keysheets/`, `keysheet-check.md`,
`cache/mag/VI_82*`, the survey copies of VI/82, and any printed or online statement of this cipher's values.
The outside check is run at the end by a different agent.

## 2. The pair and the bare letters

| role | shelfmark | pages (names used in files) | what it is |
|---|---|---|---|
| pair, cipher side | BNCF Carte Machiavelli V/140 | `V140-1r`, `V140-1v`, `V140-2r` | the Dieci's copy in cipher of Matteo Niccolini's letter from Rome, 5 Aug 1510 |
| pair, plain side | V/139 cc. 1v-2r | `V139-1v`, `V139-2r` | Machiavelli's autograph decipherment of V/140, called "inesatta ed incompleta" (inexact and incomplete) in the BNCF record |
| bare letter | V/134 c. 1r | `V134-1r` | Dieci to Machiavelli, 17 Aug 1510 (catalogue no. 2911) |
| bare letter | V/125 c. 5r | `V125-5r` | "Summario di l(ette)ra d(e) 18 dì" (summary of a letter of the 18th), 22 Aug 1510 (no. 2910) |

Sources, tiers and image recipe: `gate.md` and `PROVENANCE.md` (PRIMARY: the BNCF Teca 300 dpi masters).
Form A1: the decipherment is on separate leaves, so the cipher reading is blind to it.

## 3. Method (stages 1-4 of the pipeline, as set up for this item)

1. **Strips.** `crop.py` finds the text block and the lines of each page and cuts bands of four lines that
   step three lines, each whole-width and as two halves overlapping by a tenth of the width, at native
   resolution. Output `cache/strips/`, index `strips.tsv`. The line count in `strips.tsv` is the script's
   count of ink rows, used only to place cuts.
2. **Guides.** `SIGN-GUIDE.md` (shapes and names, from V/140 c. 1r; pictures in `sign-sheet/`, cut by
   `signsheet.py`) and `PLAIN-GUIDE.md`. `check_notation.py` tests that the notation parses with
   `line/align.py` and counts what the guide names. Both guides are frozen by commit before a reader runs.
3. **Readers.** Opus, isolated, two per page per side, prompts `reader-prompt-cipher.md` and
   `reader-prompt-plain.md` sent verbatim. Reader A re-checks top-down, B bottom-up. Cipher readers are not
   told the language, the correspondents or the matter. Plain readers are different agents from cipher readers.
4. **Agreement.** `line/compare.py` per page. Stop rule as in the pipeline: cipher token agreement under
   0.85 after one guide revision is the wall "sign legibility", with the page named. A guide revision may
   merge two look-alike names, or split one, only on the evidence of the readers' disagreements and NOTES,
   and only before any alignment has been run.
5. **Inputs to the aligner**, fixed now:
   - *Cipher side:* the both-readers-agree transcription (`compare.py --consensus`; each stretch of
     disagreement becomes one unread sign), pages in order, then `units.py`, which joins each base and
     its marks into one unit (`a^o` → `a+o`). The reason for one unit per base-with-mark is in
     `SIGN-GUIDE.md` section 4.
   - *Plain side:* a both-readers-agree text made by a script (to be written at stage 3, before the
     first alignment): words on which the two plain readers differ become a lacuna `[…]`; text inside
     `<del>…</del>` is dropped; `<ins>` tags are dropped and their words kept; `[?]` marks are dropped and
     the word kept if both readers have it.
   - *Anchors:* positions only (the clear words that stand in the cipher text, and line or paragraph
     breaks that both sides plainly share). No value is typed in.
6. **Build and test** with `line/align.py build` and `heldout`, defaults: five folds by line, 20 permuted
   keys, seed 1, values counted from status `probable` up.

The first line of `V140-1r` is the guide's worked example, so both readers of that page have seen one
reading of it. It stays in the pair; agreement on that line is not independent, and the agreement table
will be given with and without it.

## 4. The pass bar for the held-out test (stage 4)

The pipeline default as amended by calibration (`../../research.md`, "Key line, phase 0"). All four must hold
on the primary run of section 3.5:

| measure | bar |
|---|---|
| held-out letter accuracy on the units the table covers | ≥ 0.85 |
| coverage (share of held-out units the table covers) | ≥ 0.70 |
| shuffled-key control (values permuted within type) | ≤ 0.30 |
| gap between accuracy and control | ≥ 25 points |

**The imperfect plain side, decided before the run.** The held-out score compares the decode with
Machiavelli's decipherment, and that decipherment is the yardstick with the fault: the record calls it
inexact and incomplete. In the real calibration a faulty plain side capped the score (held-out 0.83 where
the true key itself scored 0.79 against the same plain text). So a right key may score under 0.85 here, and
this run has no way to know its own ceiling, because the ceiling needs the true key and the run is blind.

What will be done:

- **Accuracy ≥ 0.85 with the other three bars met:** pass. Freeze `key-v1.tsv`. Go on to stages 5-7.
- **Accuracy from 0.70 up to 0.85, other bars met:** **reported as failed.** The bar is not lowered, no
  second way of scoring is tried, and no bare letter is read as a result of this item. The report names
  the suspected cap. The table is still frozen as `key-v1.tsv`, marked "failed stage 4", and the outside
  check of section 5 is still run, because this is a known-answer pilot and that check is what tells a
  capped yardstick from a wrong key. The outside agent also measures the ceiling: the true key's own
  score against the same plain text, by the same script. If the ceiling is under 0.85, the finding is
  "the fixed bar cannot be met by this pair", and what to do about pairs like it (a bar set relative to
  something measurable without the answer) is a question for Greg before the next item. It changes nothing
  for this one.
- **Accuracy under 0.70, or coverage under 0.70, or the control over 0.30, or the gap under 25 points:**
  failed. Record the numbers. The outside check still runs, to say whether transcription, alignment or
  the plain side broke.
- **One run decides.** The primary run is the one in section 3.5. Two other runs will be reported beside
  it and cannot change the verdict: base and marks as separate units (the reader files as written, without
  `units.py`), and plain reader A's text alone. If one of those passes where the primary fails, that is
  written down as a finding about the line.
- A change to the aligner or to the inputs after the first held-out figure has been seen spends the pair
  as a test. Any figure after such a change is labelled "after a fix", as the calibration's were.

## 5. The outside check (stage 7), fixed now

Run at the end by an isolated agent that has not seen this run's reasoning. It gets `key-v1.tsv`,
`SIGN-GUIDE.md` with its sheets, the consensus cipher transcription, and the VI/82 images.

1. It first reads VI/82 into a table of sign → value, naming signs by the sign guide, **before** it opens
   `key-v1.tsv`. Signs on the sheet that the guide has no name for are listed, not forced.
2. A script then scores `key-v1.tsv` against that table. A letter value is right if it is the same letter
   after the aligner's normalisation (u/v and i/j merged). A syllable or word value is right if it is the
   same string. A null is right if the sheet gives a null. A sign in `key-v1.tsv` that the sheet does not
   list is counted apart and is in neither the numerator nor the denominator.

Proposed figures for "the line works" (all three; Greg may change them before the run, not after):

| measure | figure | why this figure |
|---|---|---|
| values marked `certain` that agree with VI/82 | ≥ 0.95 | calibration: 0 of 13 `certain` wrong on the real pair, 0 wrong among 41-44 marked values on the synthetic ones |
| values marked `certain` or `probable` that agree | ≥ 0.85 | calibration: 26 of 29 frequent signs right on the real pair |
| of the VI/82 signs that occur ten times or more in the pair transcription, the share that `key-v1.tsv` has right | ≥ 0.75 | a key that is right where it speaks but silent on common signs does not read a letter |

The same agent reports the ceiling of section 4, and decodes the two bare letters with VI/82 itself, so
that a stage 5 reading, if there is one, can be compared sign by sign.

Outcomes: held-out pass and outside check met, the line works on this kind of item. Held-out fail and
outside check met, the bar is the problem (see section 4). Held-out pass and outside check not met, the
held-out test can be fooled, which is the most serious result and stops the line. Both fail, the method
failed here; the agreement table and the outside agent's breakdown say where.

## 6. Files

| file | what |
|---|---|
| `gate.md`, `PROVENANCE.md`, `fetch.py` | stage 0-1 (not to be confused with `keysheet-check.md`, which the item agent does not open) |
| `crop.py`, `strips.tsv`, `cache/strips/` | reading strips |
| `SIGN-GUIDE.md`, `signsheet.py`, `sign-sheet/sheet-1..3.jpg` | the cipher readers' guide |
| `PLAIN-GUIDE.md` | the plain readers' guide |
| `check_notation.py`, `units.py` | notation test; joining of base and marks |
| `reader-prompt-cipher.md`, `reader-prompt-plain.md` | reader prompts with `{PAGE}`, `{READER}`, `{OUT}` |
| `readers/<READER>/<PAGE>.txt`, `.NOTES.md` | reader output (to come) |

Reader output folders: `{OUT}` is `puzzles/missing-keys-16c/items/2911/readers/{READER}` for cipher
readers and `puzzles/missing-keys-16c/items/2911/readers/plain-{READER}` for plain readers, so that no
reader's folder holds another side's files.

---

## Results

### Before the first alignment (written 2026-11-17, second call, after the readers and before any run of `align.py`)

State of the readers (`results/agreement.tsv`, main thread): cipher token agreement 0.893 (V140-1r), 0.912
(V140-1v), 0.745 (V140-2r, four lines), 0.896 in all. The total is over the 0.85 stop rule, so the run goes
on. No guide revision is made: the look-alike pairs the guide keeps apart (ex/alpha, tt/n/hash, b/h/bbar,
q/g/qj, c/e, z/3/3tail, wave/bar, theta/circdot/o) are **not** merged. Where the readers differ the
consensus has an unread sign. V140-2r stays in the pair with its disagreements.

Decisions, each made before any alignment figure was seen. `stage3_prep.py` carries them out; its counts are
in `results/prep.tsv`.

1. **Made-up names that are one sign** (`names.tsv`). `twobar` and `slash2bar` are mapped to `stem2bar`:
   three readers describe the same thing in the same places (one stem crossed by two short bars). Nothing
   else is mapped. `pbar`, `cbar`, `angle`, `eq`, `7`, `4`, `v`, `l` and the made-up marks stay as each
   reader wrote them. Reader A's "c f written as f" on V140-1r is left as it is.
2. **Plain consensus.** As section 3.5 says, with three points settled:
   - *The heading row is left out* (first row of V139-1v). It is the copyist's title for his copy, set
     apart at the top of the page; it is not part of the letter's text.
   - *"Differ" means differ in letters.* The two word sequences are matched after the aligner's own
     normalisation. A stretch where the readers have the same letters but divide the words differently is
     kept in reader A's division. Any other stretch of difference becomes one `[…]`.
   - Reader A's rows are the rows. A reader's own `[…]` stays a lacuna.
3. **The printed text** (`print/`, found after the readers reported; not foreseen in section 3). By the
   main thread's ruling the primary run stays exactly as section 3.5 has it and alone gives the verdict.
   One more reported-only side run is added: **"print plain side"**, the cipher consensus (base and marks
   one unit) against the printed text, with the same four bars computed. Clean-up of the print, by script:
   heading row and the editors' starred sub-note left out; page prefixes dropped; a word hyphenated across
   two printed lines joined; the transcriber's restored letters in ⟨ ⟩ kept as letters; `⟨…⟩` made a lacuna;
   `[?]` and the editors' `(?)` dropped. The print is in the editors' modernised spelling, which will cost it
   some letters against a decode in the cipher's spelling. If the primary fails and this run passes, that is
   a finding about the line and the main thread takes it to Greg. No bare letter is read on a side run.
4. **Side runs, all reported only:** (a) base and marks as separate units (`work/cipher-consensus.txt`
   against the plain consensus); (b) plain reader A alone (`work/plain-A.txt`, same clean-up, no consensus);
   (c) print plain side.
5. **Anchors: none.** The only clear words in the cipher are its opening words and its closing date line.
   Neither is in the plain side, and the aligner already lets a clear word be absent. The plain side has one
   paragraph break (before its last two lines), but the cipher has no break in its layout to tie it to. The
   aligner's own two ties stand: first unit to first letter, last unit to last letter.
   *The unmatched opening:* the plain text does not carry the cipher's opening clear words. Whether it also
   lacks deciphered matter at the start, the middle or the end cannot be known blind. No tie is added for it.
   If a missing stretch is long, signs there should come out as nulls or go into lacunae and letters as
   unaccounted; the aligned listing will show where.
6. **Fluency** (`line/fluency.py`, pair's cipher consensus with the built key): the word list
   (`work/wordlist.txt`) is the words of the printed text plus the words both plain readers agree on. **It is
   not independent of the pair**: it is made from the pair's own plain side, so a high share says only that
   the decode reproduces that text. It is reported as a description, not as a test.
7. **Held-out settings** are those of section 3.6, by `align.py heldout` unchanged.

### The first build did not run, and what was changed (written before any alignment figure existed)

`align.py build` on the primary inputs stopped on its first pass with "alignment band lost at unit 3417" (the
last unit), after 16 seconds. No table, no figure. Cause: arithmetic, brought on by the lacunae. The plain
consensus keeps 1,648 letters for 3,414 sign units, with 118 lacuna marks (`results/prep.tsv`). A unit lost
in a lacuna costs 0.5 and a unit that emits a letter costs about 0.03 before training, so on the forward
pass nearly all of each row's mass sits on states that lag in the plaintext and can never reach the end;
the states that can fall under the smallest float.

Change: `align_log.py` runs `line/align.py` with the E-step in log space. Same model, band, costs, Viterbi,
key rules and held-out procedure. `--selftest` shows the two E-steps agree to 1e-11 where the plain one does
not underflow. **Every run below, primary and side, uses `align_log.py`.** This is a change to the aligner
made after a crash and before any held-out or key figure was seen, so by section 4 it does not spend the
pair, but it is a departure from "`align.py` unchanged" (point 7 above) and is named as one.

### Stage 3 and stage 4, run 2026-11-17 (figures from `results/heldout.tsv`, `results/key-v0-counts.tsv`, `results/prep.tsv`)

**Verdict: stage 4 failed.** By the table of section 4 this is the third case (accuracy under 0.70, and the
control not under the accuracy). No bare letter is read. `key-v1.tsv` is frozen as a copy of `key-v0.tsv`
and marked failed in `key-v1.FAILED.md`. It is not a key.

| run | role | accuracy | coverage | control | gap (points) | recall | units | plain letters |
|---|---|---|---|---|---|---|---|---|
| cipher consensus (base+mark one unit) / plain consensus | **primary** | 0.333 | 0.782 | 0.333 | 0.0 | 0.008 | 3,414 | 1,648 |
| base and marks separate / plain consensus | side | 0.250 | 0.835 | 0.250 | 0.0 | 0.002 | 3,848 | 1,648 |
| one unit / plain reader A alone | side | 0.250 | 0.603 | 0.250 | 0.0 | 0.001 | 3,414 | 3,088 |
| one unit / printed text | side | 0.250 | 0.634 | 0.250 | 0.0 | 0.001 | 3,414 | 3,145 |

No run meets the bars. The print side run does not pass, so the finding the main thread asked about
("primary fails, print passes") did not occur.

**What the figures mean.** They are not a measurement of a key. In all four runs the aligner fell into one
state: nearly every frequent sign is given the value "nothing", and the plaintext letters are hung on rare
signs as three-letter pieces and whole words. In `key-v0.tsv`: 88 unit types; 27 certain, 13 probable, 48
unknown; of the 40 usable rows 39 are nulls and 1 is a word; 41 syllable rows and 6 of the 7 word rows are
unknown; 2,486 of the 2,552 valued places on the best path are null (0.974). A fold's table therefore
decodes almost no letters (recall 0.001 to 0.008), and accuracy equals the control because shuffling
nulls changes nothing. This is the failure named in `align.py`'s docstring from the first real calibration
run ("every sign drifts to null and a few rare signs swallow whole phrases"), come back at this item's
size. **So stage 4 did not test whether the cipher can be rebuilt from this pair. It showed that the aligner
as it stands cannot start on this pair.** Nothing here speaks for or against the transcription, the plain
side, or the unit decision.

**A correction to the note above on the first build.** After the runs, the unchanged `line/align.py heldout`
was tried on the print side run (same inputs as the side run, registered tool): it stops with the same "band
lost at unit 3417". The print text has 6 lacuna marks, so the underflow is not caused by the lacunae alone,
as that note says; it comes with one unanchored stretch of 3,417 units whatever the plain side. The
log-space E-step is needed for any run on this pair. (`results/log/heldout-check-print-plain-alignpy.err`.)

**Inputs** (`results/prep.tsv`). Cipher consensus: 69 lines, 3,414 sign units with base and mark joined
(3,848 separate), 322 of them unread stretches (161, 133 and 28 by page), 88 distinct units, 3 clear words.
Plain consensus: 336 of reader A's 590 words kept (0.569), 1,648 of 3,088 letters (0.534), 118 lacuna
marks: 43% of the words went to lacunae. Names mapped: 7 tokens, all to `stem2bar`. Anchors: none.

**Fluency** (`results/fluency.tsv`): the built key decodes 72 letters of the pair, all covered by the word
list (share 1.000), and the permuted keys score the same (1.000). With a key of nulls and one word this
says nothing. The word list is made from the pair's own plain side and is not independent of it.

**What was not tried, on purpose.** No second way of aligning was run after these figures were seen
(anchors by line, a different training schedule, a stronger cost on nulls). Any such run would be "after a
fix" and the pair is now spent as a clean held-out test for whatever is tuned on it. Untested guesses at
the cause, each with the test that would move it: (1) one stretch of 3,400 units with no tie inside it and a
flat start: build a synthetic pair of this size, 88 unit types, 9% unread, no anchors, and see whether the
aligner recovers a known table; (2) a rare unit can take a one-off span at almost no cost because the
smoothing weight is small beside its count: same synthetic pair, vary the weight; (3) the unread stretches
(9.4% of units) break the letter-for-sign rhythm: same pair, vary the unread share.

**Time** (clock of this machine, 17 Nov): inputs and decisions written 10:52-10:55; first build crashed
10:55 after 16 s; log-space E-step written and self-tested by 10:57; build and four held-out runs in
parallel 10:57-11:06 (about 70 s a pass for the primary, longer for the two full plain sides); collection,
fluency, freeze and this record by 11:10.

## After the failure (main thread, 2026-11-17). Every figure in this section is "after a fix".

The held-out test failed as recorded above, and the pair is spent as a clean test. Two changes were then tried
on the cipher consensus against the printed text, to learn whether the degenerate state has a cheap cure.

1. **Doubled signs** (`doubles.py`, `results/doubles.tsv`). Readers wrote a doubled shape as two tokens, as the
   guide told them. Counts say the pair is a sign of its own for five signs: `a a` 80 pairs where 7.9 are
   expected by chance, `s s` 59 (14.7), `b b` 52 (5.3), `f f` 4 (0.4), `o o` 4 (0.4). Joined as `aa` etc.
   (`work/cipher-doubles.txt`: 3,228 units).
2. **Null and skip made dear at the start** (`exp_fix.py`): the empty emission's prior weight 0.001 for the first
   six passes (then 0.04), and a plaintext letter that no unit accounts for costs 0.002 (was 0.02).

| run (`results/log/fix-*.out`) | units | null share of valued places on the best path | marked values that are not null |
|---|---|---|---|
| A: doubles joined, aligner unchanged | 3,228 | 0.690 | 0 |
| B: doubles joined, null and skip dear | 3,228 | 0.609 | 0 |
| C: doubles not joined, null and skip dear | 3,417 | 0.640 | 0 |

No run learns a single letter value. The letters are carried by three-letter spans on signs marked `unknown`.
The fix attempt stops here.

**Reading of it (not shown, to be tested).** The printed plain text has 3,145 letters and the cipher 3,228 units.
The period key is said to have a table of syllable signs, so the cipher probably spells more letters than the
plain side holds: the copy is partial (it starts at "Intendesi", after the cipher's opening, and BNCF calls it
incomplete). The aligner assumes the two sides cover the same text end to end. If a third of the cipher has no
plain counterpart, a third of the units must emit nothing, and "null" becomes the best value for every common
sign. The calibration pairs were complete on both sides, so they could not show this. The outside check
(`outside/`) measures how much of the cipher the plain text covers.
