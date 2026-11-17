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

(none yet)
