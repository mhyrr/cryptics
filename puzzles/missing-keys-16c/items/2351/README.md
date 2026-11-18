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
