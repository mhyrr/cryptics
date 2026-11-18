# No. 1336 — Speciano and Borromeo: run record

Opened 2026-11-17 on Greg's instruction ("find a message that has not been decrypted and does not yet have a
key"). Gate: `gate.md`. This is the first run of the key line after the 2911 bench, and the first clean test
of its builder (H6) and of a key nobody holds (H8).

## The material
| Piece | Folio | Role |
|---|---|---|
| cipher slip, 13 lines | F 47 inf. no. 131 c. 269r | **build pair**, cipher side |
| clear text, about 14 lines | F 47 inf. c. 270r ("vedasi il foglio seguente" on 269r points to it) | build pair, plain side |
| cipher slip, 3 lines | F 49 inf. no. 18 c. 44r | **transfer test**: decoded with the frozen key |
| clear note of two lines under that slip | same leaf | the answer to the transfer test, if it is the slip's decipherment. Kept out of the build |
| cipher line in brackets | F 131 inf. no. 7 c. 14r (4 July 1574) | **bare**: no decipherment on the page. The reading, if the key holds |

## What the main thread has seen (stated before any reader runs)
The main thread looked at all the page images to cut strips and write the sign guide. It saw that the cipher
has about one sign per letter of the clear text (about 550 signs to about 600 letters on the pair), and, on
c. 44r, that the repeat pattern of the slip's first signs fits the first words of the note under it. No value
from that look enters the key: values come from `align.py` on the readers' files of the F 47 pair only.

## Stages and bars (written before the readers ran)
1. **Readers** (Opus, isolated): cipher A and B read all three cipher passages; plain A and B read c. 270r and
   the note on c. 44r. `line/compare.py` gives agreement. Stop if cipher agreement on c. 269r is under 0.85
   after one guide revision (PIPELINE.md stage 2).
2. **Build** on the F 47 pair, both-readers-agree signs against the plain consensus, with
   `align.py build` (the pair looks complete). If that build stops on its null check, or leaves over 20% of
   the plain letters unaccounted, rebuild with `--abridged` and say so.
3. **Held-out on the pair** (`align.py heldout`, five folds): accuracy ≥ 0.85 on covered signs, coverage
   ≥ 0.70, shuffled control ≤ 0.30. Fail → no reading; record and stop.
4. **Transfer** (the stronger test): decode the c. 44r slip with the frozen key, compare with the note under
   it by `align.score`. Bar: accuracy ≥ 0.85 with at least 70% of the slip's signs valued, and the shuffled
   control ≤ 0.30. If the note is not the slip's decipherment the comparison fails for that reason and the
   decode is judged as a bare letter.
5. **Bare line** on c. 14r: decode by script. Reported with every unvalued sign shown, English beside the
   Italian, and the sentence of clear text it stands in. It is a reading only if stages 3 and 4 pass.

## Result of stage 1 (2026-11-17): the main slip fails the agreement bar
`results/agreement.tsv`, `results/agreement-c269-pairs.tsv`.

| Piece | Agreement |
|---|---|
| c. 269r, readers A and B (guide as frozen) | 0.779 |
| c. 269r, readers C and D (guide revision 1) | 0.807 |
| c. 269r, all six pairs of the four readers | 0.742 to 0.807 |
| c. 44r slip, A and B | 0.941 |
| c. 14r line, A and B | 0.750 |
| c. 270r clear text, PA and PB (words) | 0.928 |
| note on c. 44r, PA and PB (words) | 0.933 |

The slip on c. 269r has 15 lines and about 795 signs (the brief said 13 and about 550). **Wall for plan A: sign
legibility of c. 269r at the 750 px the archive serves** (no larger size is served: nine URL variants return
the same file). The disagreements are spread over many pairs of shapes; the largest is q against qx (13 of
about 130 in C against D). Reader D made one full pass, reader C a full second pass on lines 7–15 only.
Breach: a better image of F 47 inf. c. 269r from the Ambrosiana.

## Plan B (registered 2026-11-17 after the agreement figures, before any build)
This departs from the stages above and is stated as such. What the main thread knew when writing it: the
agreement figures; the plain consensus texts; that the c. 44r slip has 102 signs against a note of about 101
letters; and the by-eye pattern match stated above. No table had been built.

1. **Build on the c. 44r pair**: `align.py build` on the A-and-B consensus of the slip against the PA-and-PB
   consensus of the note. The pair is small, so few rows can reach `probable` (4 places). Two tables are
   written: `key-v0.tsv` as built, and the **provisional** table: every row whose value holds at 60% of its
   places, whatever the count.
2. **Test on c. 269r** (this replaces the transfer test; the roles of the two slips are swapped). Decode the
   C-and-D consensus of c. 269r with the provisional table and score it against the c. 270r text with
   `align.score`, against 20 tables with values shuffled within type. The cipher there has about 795 signs to
   about 600 letters of clear text, so part of it has no counterpart and accuracy cannot reach the usual 0.85.
   **Bar: accuracy ≥ 0.55 on decoded letters, shuffled control ≤ 0.30, and at least 60% of the signs valued.**
   Fail → no reading of c. 14r.
3. **Bare line on c. 14r**: decode with the provisional table; each sign shown; unvalued signs as `?`.
   Two readers agree on only 0.750 of that line, so both readers' versions are decoded and shown.
4. If 2 passes: widen the table with `align.py build --abridged` on c. 269r against c. 270r, check that it
   does not contradict the c. 44r table (count of signs valued differently), and report it as a second,
   weaker table.

## Plan B results (2026-11-17)
1. **Build.** The plain build on the c. 44r pair stopped on its null check (71% of places null;
   `results/b-build.tsv`): the two plain readers disagree on two words of the note, so the agreed text has 82
   letters against 101 signs. Rebuilt with `--abridged` as the stages above prescribe
   (`results/b-build-abridged.tsv`, `key-c44-v0.tsv`): 20 rows, 3 `probable`, 17 provisional (16 letters, one
   two-letter value). Five signs spell their value at every one of 6 to 10 places.
2. **Test on c. 269r: fails the bar as written** (`results/b-test.tsv`).

   | Cipher text | Signs valued | Accuracy | Shuffled control |
   |---|---|---|---|
   | C-and-D consensus | 0.597 (bar 0.60) | 0.712 (bar 0.55) | 0.457 (bar 0.30) |
   | reader C alone | 0.534 | 0.680 | 0.431 |
   | reader D alone | 0.564 | 0.655 | 0.414 |

   Accuracy passes; coverage misses by 0.003; the control is far over its bar. The control bar was taken from
   calibrations where nearly every sign was valued. Here 40% of signs decode to `?`, which the scorer matches
   to anything, so a shuffled table scores 0.46. The bar was mine and it was wrong for this case; it stays
   failed. The gap between the table and its shuffles is 0.25.
3. **Bare line on c. 14r.** `run.py b-decode` was run in the same command as the test, before the result was
   read; that was a slip of procedure. Under the registered rule its output (`results/b-decode.txt`) is **not
   a reading**. What it shows, as an observation only: both readers' versions of the line decode to a string
   ending in `?rum?nto e` / `?rumn?to e`, and the clear text on c. 270r names a "monsignor Frumento".
4. Not run (it was conditional on 2).

**State.** A partial table of 17 values for a cipher nobody has published a key for, each value witnessed on a
clean one-sign-per-letter pair; a failed registered test; no reading claimed. The cipher is a simple
substitution with at least three signs for `a`. What would settle it: a control fit for partial tables
(decode only the valued signs and count exact matches at aligned places against shuffles), written before it
is run; and a better image of c. 269r, which would also widen the table.

## Second test (registered 2026-11-17 after the first test failed; a post-hoc test, labelled as one)
`run.py b-test2`. Read the C-and-D consensus of c. 269r against the c. 270r text with `align.beam_read`, the
17-value table held, beam 1,500. Count the places where a held sign spells its value at the pointer (exact
matches). Do the same with 20 tables whose values are shuffled among the same 17 signs (seed 1). A shuffled
table gets the same freedom to skip, gap and value the other signs. **Pass: the true table's match count is
above all 20 shuffles and at least 1.5 times their mean.** A pass says the c. 44r table reads c. 269r; it
does not undo the failed first test, and both are reported.

**Result of the second test: pass** (`results/b-test2.tsv`). Of 373 places on c. 269r that hold one of the 17
valued signs, 263 spell their value at the pointer in the c. 270r text. Twenty shuffled tables give 110 to
141 (mean 127.6); the ratio to the mean is 2.06. So the table built from the c. 44r slip and its note reads
the F 47 slip against its own period translation: the two slips share a table (H8, for these two leaves),
and the note on c. 44r is that slip's decipherment. The first test stays failed as registered.

**What is and is not claimed.**
- Claimed: 17 sign values of the Speciano–Borromeo cipher, built by script from one pair and confirmed on a
  second, independent pair. No published key for this cipher was found at the gate.
- Not claimed: a reading of the bare line on c. 14r. With 17 values and two readers who agree on 0.750 of
  its signs, about half of it decodes. It needs the wider table and a second transcription round.
- Not checked: whether c. 14r uses the same table (its decode ending in the name the c. 270r text gives is
  an observation, not a test); the attribution of F 47 no. 131 in Rivolta.

**Next.** (1) Widen the table: `align.py build --abridged` on c. 269r against c. 270r with the 17 values as
the check (count of signs valued differently), using a majority of the four readers. (2) Two more readers on
c. 14r with guide revision 1. (3) Ask the Ambrosiana for a better image of F 47 inf. c. 269r (Greg's call:
an outside message).

## Third stage (registered 2026-11-18, before any of it is run)
Greg's go-ahead, 2026-11-18: widen the table, then read the bare line. Four Opus readers were dispatched before
this was written and had not reported: E and F on the cipher line of c. 14r with guide revision 1
(`reader-prompt-c14-r1.md`), PC and PD on the clear lines round it (`reader-prompt-plain-c14.md`, strips
`p14-*`).

**W. Widen the table** (`run.py w-build`, `run.py w-check`).
- Blind `align.py build --abridged` on the C-and-D consensus of c. 269r against the c. 270r text. The 17
  values are not given to it. Output `key-c269-v0.tsv` (`results/w-build.tsv`).
- Check: of the signs the new table marks `certain` or `probable` that are also among the 17, count those
  with the same value. **Bar: at least 8 shared signs, and at least 80% of them agree.**
- If the bar is met, `key-v1.tsv` = the 17 values, plus every `certain` or `probable` row of the new table
  for a sign not among the 17. A shared sign valued differently keeps its c. 44r value and is listed. If the
  bar is not met, the table stays at 17 and the new table is reported as failed.

**T. Test the bare line** (`run.py c14-prep`, `run.py c14-test`), then and only then `run.py c14-decode`.
- Text: agreement of E and F by `compare.py`. If it is 0.85 or more, the test runs on their consensus. If
  not, it runs on E and on F apart and must pass on both.
- Word list: every word of four letters or more in the clear texts we hold: both readers' c. 270r and
  c. 44r, both readers' clear lines of c. 14r, and the printed text of no. 2911
  (`../2911/bench/inputs/plain-full.txt`, Italian of 1510, used only as a store of Italian words).
- Statistic: decode the line with the table in force (`key-v1.tsv`, or the 17). An unvalued or unread sign
  is `?`. Count the most letters that can be covered by word-list words laid end to end without overlap; a
  `?` may stand for any one letter, and a word counts only if at least three of its letters and at least
  two thirds of them are valued.
- Control: 200 tables with the values shuffled among the same signs (seed 1). **Pass: the true count is
  above 190 or more of the 200.**
- A pass allows a proposed reading, with every `?` left open and every word marked by whether E and F agree
  on its signs. A fail means no reading; the wall is then the image and the table size, and is named.
- Known weakness, stated now: the line has about 37 signs, so the test has little power, and the word list
  holds the name the earlier decode seemed to end in. That name came from a decode I had seen; the shuffles
  face the same word list.

**W result (2026-11-18): pass** (`results/w-build.tsv`, `results/w-check.tsv`). The blind build on c. 269r
gives 41 rows, 23 marked, null share 0. Of the 14 marked signs it shares with the c. 44r table, 13 have the
same value. Nine marked rows are new (all single letters), so `key-v1.tsv` has 26 values. Two tables built
apart, from two slips and two clear texts, agree on 13 of 14 signs.

**Amendment, written after W and before any run of T or any report from readers E, F, PC, PD.** The one
sign that differs is `2`: the c. 44r table values it from one place, the c. 269r table from 22 places (share
0.88). The registered rule keeps the c. 44r value. That rule did not foresee a one-place value against a
22-place one. Amended rule: where the tables differ, the value witnessed at more places stands, and the sign
is listed. `run.py w-check` now writes `key-v1.tsv` that way; `results/w-check.tsv` shows both values.

**T result (2026-11-18): fails as registered** (`results/agreement-c14.tsv`, `results/c14-test.tsv`).
- Readers E and F agree on 0.806 of the line's signs (37 and 35 tokens), under the 0.85 bar, so the test ran
  on each apart. The clear lines round it: PC and PD agree on 0.759 of the words.
- Reader E: 8 letters covered; above 194 of 200 shuffled tables. Passes.
- Reader F: 4 letters covered; above 167 of 200. Fails. Both must pass, so the test fails.
- **No reading of the line is claimed.**

`run.py c14-decode` was run after the test (`results/c14-decode.txt`). Observations only, by eye, not tested:
- All four readers' rows decode to `?con` at the start, to `icipa` in the middle after `pa` and two signs
  the readers disagree on, and to `rum?nto`/`rumonto` near the end. Read together they resemble
  "con … participa… … del Frumento e": "with … participat… … of Frumento and".
- Reader F's row gives `delfrumonto`. The `f` and the `d` there are values that came from the c. 269r build,
  which never saw this line.
- The clear line before the cipher ends "il tutto e" or "il succo e" on the page; both clear readers give
  "il tutto e" ("the whole of it is"). So the cipher line is the gist of what the writer reports.
- The stretch of four to six signs after `icipa` lies under the stain and a hole; no two readers agree on it.

**Wall.** The table is not the limit any more: 28 or 29 of the line's 36 to 38 signs have values. The limit
is the reading of about ten signs under a brown stain at 750 px. A better image of F 131 inf. c. 14r (and of
F 47 inf. c. 269r) would breach it; so would the Ambrosiana's own description of the letter if it summarises
the passage. Both are outside messages or catalogue searches and are Greg's call.

## Fourth test on the bare line (registered 2026-11-18 after T failed; post hoc, labelled as one)
Greg's point: readers who agree at 0.80 hold more together than apart, and T asked each to pass alone.
I have seen the four decodes, so the choice of this statistic is informed by them. The shuffles guard against
the method's freedom, not against my choice of method. T stays failed.

`lattice.py` (`python3 lattice.py test`, then `python3 lattice.py read`).
- **Columns.** Readers F, A and B are lined up on reader E's row by `difflib` on sign names (A and B through
  `names.tsv`). Each column holds each reader's vote: a sign (weight 1; 0.7 if marked doubtful, the other 0.3
  unread), two signs for `x|y` (0.5 each), unread, or no sign there.
- **Candidates.** A column's candidates are the table values of the signs voted for, "no sign" if a reader
  has none there, and "any one letter" if any vote is unread or unvalued. Each has the share of the votes.
- **Letter model.** Letter trigrams, add-0.1 smoothing, from the OCR text of Machiavelli's *Opere* vol. 3
  (`../2911/print/leoperediniccol03milagoog_djvu.txt`), words normalised by `align.norm_letters` and run
  together. First 90% trains; the last 10% is kept for the calibration below.
- **Path.** The best path through the columns by log vote share plus trigram log probability (exact, by
  dynamic programming on the last two letters). The model chooses among supported candidates; where it
  fills "any one letter", the reading prints `?`.
- **Test.** The best path's score under the true table against 200 tables with the values shuffled among
  the same signs (seed 1). **Pass: above 190 or more of the 200.**
- **Calibration, reported not barred.** The path's trigram log probability per letter, set against windows
  of the same length from the held-out 10% and against the shuffles.
- A pass allows a proposed reading: the supported letters of the best path, each with its vote share, `?`
  elsewhere, and an English gloss marked as mine. A fail means no reading.

**Self-check of the method** (`python3 lattice.py selftest`, `results/lattice-selftest.tsv`; run before the
test). Planted 36-letter lines read by four noisy readers with a quarter of the table hidden: 16 of 20
Italian lines pass (50 shuffles, bar 48) and 1 of 20 random-letter lines does; 323 of 358 supported letters
are right on the Italian lines.

**Result of the fourth test: pass** (`results/lattice-test.tsv`). 38 columns from readers E, F, A, B. The best
path under the 26-value table scores above 199 of 200 shuffled tables. Its trigram score per letter (−1.80)
is above the shuffles' mean (−2.43) and inside the range of real Italian windows of that length (median
−2.09; the path sits high in that range because the model also fills the open places). T stays failed; this
is a post-hoc test and is reported as one.

**Proposed reading of the bare line, F 131 inf. c. 14r** (`results/lattice-read.txt`):

    ?con?participa???u?ne??de?rum?ntoe

- Every letter shown is the table value of a sign at least one reader wrote there; `?` is a place where no
  reader's sign has a value. 21 of the 26 letters shown rest on all four readers.
- Words I see in it (interpretation, mine): `con` ("with"), `participa…` ("participat…"), `de? ?rum?nto`
  ("del Frumento", "of Frumento": the first deputy named on c. 270r), `e` ("and"). Three readers write a
  sign valued `f` before `rum`; the path dropped it because one reader has no sign there.
- Not read: the first sign; the sign after `con`; three or four signs after `participa`; one after `u`; two
  before `de`. Six of the signs there (`u`, `utail`, `pi`, `boxbar`, `9`, `phi`) are agreed by the readers
  and simply have no value in the table yet. That is a table gap, not an image gap, and c. 269r can fill it:
  `u` alone stands at about 15 places there.

**Next.** Value the six open signs from c. 269r with the same four-reader columns read against the c. 270r
text (register first). Then rerun `lattice.py read`. A better image is still wanted for columns 5, 9, 24–29
and 33.
