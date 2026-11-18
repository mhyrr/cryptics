# No. 2351 — Roberto Acciaiuoli, Amiens, 23 October 1513

Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 190–192. Gate: `gate.md`.
Images and the pair: `PROVENANCE.md`. Method: `../../line/METHOD.md`. Every figure here comes from `run.py`.

- **Letter A** (c. 232 and doc. 190): cipher, about 1,135 signs, with a chancery copy in clear (c. 233).
- **Letter B** (c. 234 and doc. 192): cipher, same day, no clear text here. The thing to read.

## What a solution has to do
1. A table of sign values built from letter A and its copy by script, with no value typed in.
2. The table, unchanged, turns letter B into Italian that beats shuffled tables, on a test written before the
   run. Letter B is never used to build or adjust the table.
3. A reading of letter B that prints only supported letters, and says what each rests on.

## Stage 1: transcription (2026-11-18)
- Clear copy: four readers (PA, PB on plain strips; PC, PD on red-channel strips). Each read under half the
  words. The image is the limit (strokes 2–3 px wide in a screenshot).
- Cipher, letter A: three readers (A, B, C) with `SIGN-GUIDE.md`. Each found 1,134 to 1,138 signs in 24 lines
  that hold cipher. First pair, before any renaming: agreement 0.891.

## Stage 2, registered 2026-11-18 before any build
`run.py prep`, then `run.py build`, then `run.py tables`.
- **Cipher text.** The three readers' rows from the line where the cipher starts to the last cipher line,
  clear words removed, names mapped by `names.tsv` (made from the readers' shape descriptions), merged by
  `line/merge.py` (a sign needs half the votes). A sign is a base with its mark: `x^4` is one sign.
- **Plain texts.** Each of the four readings from the word after "la sera" (where the cipher starts) to its
  end; `[...]` is a hole.
- **Build.** `align.py build --abridged` on the merged cipher against each plain reading apart: four tables.
- **Check.** For each of the six pairs of tables: the signs both mark `certain` or `probable`, and how many
  have the same value. **Pass: at least two pairs with 10 or more shared signs and 80% or more the same.**
- **If it passes,** `key-v0.tsv` holds each sign that two or more tables mark with the same value and no
  table marks with another. If it fails, no table is kept, and the wall is the clear copy's image.
- Known weakness: the four plain readings come from one page and share one cipher text, so agreement between
  their tables is weaker evidence than two separate pairs. The real test is letter B (stage 3, to be
  registered before letter B's readers report).

**Stage 2 result (2026-11-18): fails** (`results/prep.tsv`, `results/build.tsv`, `results/tables.tsv`).
- Cipher: pairwise agreement 0.906 to 0.912 (bases alone 0.933 to 0.938). The merge keeps 1,094 of 1,133
  places; 124 distinct signs, 70 of them seen five times or more.
- Plain: after "la sera" the four readings hold 623 to 871 letters in 65 to 98 holes each.
- Build: the tables mark 7, 8 and 10 rows of about 121; the fourth (PD, which never read "sera" and was cut at
  an arbitrary word) found no path. No pair of tables shares 10 marked signs. **No table is kept.**
- Cause as I read it: about 40% of the clear text, in 90 pieces, against 124 signs treated as unrelated.

## What the cipher text shows without any plain text (`run.py marks`, `results/marks.tsv`)
- 569 of 1,094 signs carry a mark. Four marks carry 518 of them (`4` 149, `3` 143, `~` 114, `5` 112); `1` has
  30; `n` has 15, all but one on `D`.
- Fifteen bases take the vowel-like marks: `7 3 8 y t x r s q z 6 2 4 S 5`. The other bases (`delta`,
  `flong`, `brace`, `beta`, `c`, `sigma`, `gamma`, `hash`, `Q`, …) never do.
- Several of the fifteen also stand unmarked often (`y` 46 of 68, `3` 29 of 91, `7` 27 of 94).

## Stage 2b, registered 2026-11-18 before it is run: the tied builder (H9)
`tied.py` reads the cipher against the plain text as `align.py build --abridged` does, but gives one value to
each base that takes vowel marks (a consonant), one to each vowel mark (a vowel), and one to each other
sign. Which bases take marks is read off the cipher alone. No value is typed in.

**Planted pairs first** (`results/tied-synth.txt`): real Italian enciphered with a planted cipher of this
kind, about 950 signs, the plain side cut to about 600 letters in about 70 holes with 10% of words damaged.
Six seeds: four rebuild 18 or 19 of the 20 bases and marks with no wrong row; one rebuilds 9 with one wrong
row of 10; one marks a single row, wrongly. So the builder works on four pairs of six, and when it fails it
marks few rows.

**The run** (`run.py tied`, `run.py tied-tables`): one table from each of the four plain readings, as in
stage 2. **Pass: at least two pairs of tables share 8 or more marked bases and marks, and 80% or more of
those have the same value.** If it passes, `key-v0.tsv` holds every entry that two or more tables mark with
the same value and none marks with another. If it fails, no table is kept.
The same weakness as stage 2 holds: one cipher text and one page behind all four. Letter B is the test.

**Stage 2b result (2026-11-18): fails** (`results/tied-build.tsv`, `results/tied-tables.tsv`). The four tables
mark 1 to 4 entries each; path scores are 13, 27, −11 and 3 against about 380 on a planted pair; no pair of
tables shares a marked base or mark. No table is kept. Either H9 is wrong in form or the plain readings are
too poor. The second is certain whatever the first: the four readings agree on 0.498 of their words (first
pair) and their agreed text is 302 letters; the planted pairs had 10% of words damaged, these have far more.
**Wall for the paired route: the image of c. 233.**

## Stage 3, registered 2026-11-18 before it is run: the cipher solved from its own text (H9)
`solve.py`. No plain text goes in. The table has one consonant per base that takes vowel marks (one-to-one),
one vowel per vowel mark (one-to-one), and one letter or nothing per other sign. Simulated annealing on the
letter-trigram score of the decode (Machiavelli corpus) with a penalty for letter counts that leave
Italian's. Planted ciphers of this kind (`results/solve-synth.txt`; about 950 signs, 3.5% unread, 3% wrong):
see the file; on seed 1, 19 of 20 bases and marks were right.

**The run** (`run.py solve`): letter A's merged text, 8 restarts, seed 1. Output `key-s0.tsv`.

**Test** (`run.py solve-test`), which uses the clear copy only as a judge:
- Word list: every word of five letters or more that at least two of the four plain readers give (anywhere
  on the page).
- Statistic: how many of those words stand in the decode of letter A as written, letter for letter.
- Control: 200 tables with the values shuffled inside each class (consonants among bases, vowels among
  marks, letters among the other signs; seed 1).
- **Pass: the solved table's count is above 190 or more of the 200, and the two best restarts agree on 80% or
  more of the bases and marks.**
- A pass supports H9 and gives a first table. It does not license a reading of letter B: that is stage 4,
  with its own readers and its own registered test.
