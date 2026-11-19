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

**Stage 3 result (2026-11-18): fails** (`results/solve.txt`, `results/solve-test.tsv`). Eight restarts reach
−2.85 to −2.93 a letter (planted ciphers: about −2.33; real Italian of this length: median −2.09). The two
best agree on 21 of 21 bases and marks, so the search settles; what it settles on is not Italian. None of
the 67 judge words stands in the decode; shuffled tables find 0 or 1. All restarts give mark `1` = `u`.

## Stage 3b, registered 2026-11-18 before it is run: nearby forms of H9
The same solver and the same test, over twelve forms: the vowel after the consonant or before it (CV, VC),
and an unmarked base spelling its consonant alone or its consonant with one fixed vowel (none, a, e, i, o,
u). Three restarts each, seed 1 (`run.py forms`, `results/forms.tsv`). The form with the best score a letter
is then tested with `run.py solve-test` exactly as in stage 3. **Pass: as stage 3.** Twelve forms are tried
and one is tested; the shuffles do not correct for that choice, so a pass needs the count well clear of the
shuffles' maximum, not just above 190 of them.

**Stage 3b result (2026-11-18): fails** (`results/forms.tsv`, `results/forms-test.tsv`). The twelve forms reach
−2.60 to −3.08 a letter; none comes near a planted cipher's −2.33. The best (vowel before consonant, bare
base with `e`) finds 0 of the 67 judge words; shuffles find 0 to 2. The forms disagree with each other on
every mark but `1` = `u`.

## Where this stands (2026-11-18)
- **Cipher side: good.** Three readers agree at 0.906 to 0.912 on letter A; the merged text has 1,094 read
  places of 1,133. Letter B is not transcribed yet.
- **Plain side: the wall.** Four readers each read under half of c. 233 and agree on half of that. Every
  build from it failed (stages 2, 2b).
- **Structure: real, form unknown.** Five marks on sixteen bases is a fact of the cipher text
  (`results/marks.tsv`). "Base = consonant, mark = vowel" in twelve forms does not turn letter A into Italian
  (stages 3, 3b). The marks may instead pick one of several unrelated values for a base, which only a pair
  can teach.
- Four registered stages, four failures, no table kept, nothing claimed.

**What would breach the wall, in order of cost**
1. A published table of the same family. The gate notes one for the neighbouring Pandolfini correspondence;
   it has not been found or tried. A script can screen it against letter A in minutes.
2. A better reading of c. 233: a real scan from the Archivio di Stato di Firenze (outside request, Greg's
   call), or a reader stronger than the four Opus runs on the image we hold (Greg's call: the repo rule keeps
   transcription on Opus).
3. Letter B's 2,300 signs added to the cipher-only search, with forms that let a base hold several values.

## Stage 4, registered 2026-11-18 before it is run: the pair again, with a fifth plain reading
Greg's go-ahead, 2026-11-18: one clear-copy reader on Fable (PE), an exception to the Opus rule, given the
page image as well as the strips (`reader-prompt-plain-r3.md`). PE leaves 58 words unread and 52 doubtful of
about 480; the earlier four left about 250 each. PE saw no cipher page and no other reader's file. A scout
is looking for a published table (`scout-prompt-tables.md`); it has not reported. Three Opus readers (G, H,
I) are on letter B and have not reported.

**4a. Build** (`run.py pe`): PE's text from after "la sera"; the merged cipher of letter A.
- `align.py build --abridged` (signs unrelated): `key-pe-free.tsv`.
- `tied.py` (one value per base, one per mark): `key-pe-tied.tsv`.
- Report, with no bar: rows marked by each; and what the free table says about H9 without being told it: of
  its marked rows for a base with a vowel mark, how many have a two-letter value, and of those, how many end
  in the vowel most common for their mark and begin with the letter most common for their base.
- **Bar for keeping a table: the free table marks 30 rows or more.** (Stage 2's tables marked 7 to 10.)
  `key-v0.tsv` is then the free table's marked rows.

**4b. Test on letter B** (`run.py b-test`), registered now, run when G, H, I are merged. Letter B is never
used to build or change the table.
- Decode letter B with `key-v0.tsv`; an unvalued or unread sign breaks the text into runs.
- Statistic: mean letter-trigram log probability (Machiavelli corpus) over all trigrams inside runs.
- Control: 200 tables with the values shuffled among the same signs (seed 1).
- **Pass: the table's mean is above 190 or more of the 200, and at least 40% of letter B's read signs have a
  value.**
- A pass means the table reads text it never saw. Only then is a reading of letter B attempted, by the
  method of `../1336/lattice.py`, printing only supported letters.

**4a result (2026-11-18): the bar is not met** (`results/pe.tsv` was not written: the free build stopped with
"no path through the band" in its soft pass, as it did for reading PD). No table from the pair. The tied
build ran; its output is in `work/` and is not used.

## Stage 5, registered 2026-11-18 before it is run: screen the Pandolfini table
The scout (`sources/tables.md`) found B. Dudout's reconstructed key for Francesco Pandolfini's letters of
1514–15 in this same filza (CLAIMANT; its own held-out tests were weak). In it a figure over a consonant sign
gives the vowel after it: 1 = u, 2 = o, 3 = i, 4 = e, 5 = a. Our cipher-only solve of stage 3, run before
the scout reported, gave 1 = u, 3 = i, 4 = e, 5 = a, ~ = o in its first form: the same four figures, and
the tilde where their 2 stands.

`sources/map-pandolfini.tsv` is my mapping of their signs onto our names (34 rows: 5 marks, 13 bases, 16
bare signs), made from the scout's shape notes before any decode. `run.py screen`:
- Decode letter A's merged text with that mapping: a base with a mark spells consonant + vowel; a bare sign
  takes its bare value, or its base consonant; every other sign is unvalued and breaks the text.
- Judge words: every word of five letters or more in reader PE's text of the clear copy.
- Statistic: how many judge words stand in the decode, letter for letter.
- Control: 200 mappings with the consonants shuffled among the bases, the vowels among the marks and the bare
  values among the bare signs (seed 1).
- **Pass: the count is above all 200 shuffles and is 10 or more.**
- A pass says Acciaiuoli's cipher of 1513 is Pandolfini's of 1514, or close kin, and gives a first table to
  correct against the pair. It is still not a reading of letter B: stage 4b stands for that.

**Stage 5 result (2026-11-18): fails the bar as written; clears the control** (`results/screen.tsv`,
`results/screen-decode.txt`). 723 of 1,133 signs get a value. 6 of PE's 151 judge words stand in the decode
(altri, auanti, confidare, qualche, tanti, uoluto); the bar was 10. All 200 shuffled mappings find 3 or
fewer (mean 1.05). The count bar was mine and too high for exact words in a text broken at every third
sign; it stays failed. By eye the decode is Italian in runs ("magnificenta", "le pratiche di", "tanti
agenti", "confidare", "participi"), and those are words of PE's own summary of the page.

## Stage 6, registered 2026-11-18 before it is run: hold the Pandolfini values and learn the rest from the pair
`run.py held`. `tied.py` with the 34 mapped values held (never changed by the build), an unmarked base
treated as a sign of its own (the Pandolfini table shows bare values that differ from the base consonant),
PE's text as the plain side.
- **Test first:** exact matches on the path (places where a held entry spells PE's text) under the mapped
  table, against 20 tables with the same values shuffled inside each class (seed 1). **Pass: above all 20
  and at least 1.5 times their mean.**
- If it passes, each held entry is graded from the path: `confirmed` (3 hits or more and evidence 4 or more),
  `contradicted` (5 or more places and more misses than hits), else `untested`. Entries the build adds are
  kept when marked `certain` or `probable`.
- `key-v0.tsv` = held entries not contradicted, plus the added marked entries. Each row says which.
- Letter B is still untouched. Stage 4b is its test, with `key-v0.tsv` and with the shuffles made inside
  each class.

**Stage 6 result (2026-11-18): pass** (`results/held.tsv`, `key-v0.tsv`).
- With the 34 mapped Pandolfini values held, 383 places on letter A spell PE's text of the clear copy.
  Twenty tables with the values shuffled inside each class give 81 to 138 (mean 100.8); the ratio is 3.8.
- Graded on the path: 22 held values confirmed, 8 untested, 4 contradicted (mark `1` = u, 10 hits against 19
  misses; base `2` = t; `flong` = f; `hash` = ll). The four are dropped.
- Six entries added from the pair: base `r` = s (which the Pandolfini table also has, as an uncertain shape
  match), base `s` = m, bare `brace` = a, bare `7` = o (their "reversed c" = o), `sigma` = s, `i` = g.
- `key-v0.tsv`: 36 entries (30 held, 6 added), each row marked with which.

**What this means.** Acciaiuoli's cipher of October 1513 is, in most of its values, the cipher Dudout rebuilt
for Pandolfini's letters of 1514–15 from the same filza. So this is not a key nobody has: it is a
published reconstruction (CLAIMANT) shown to read two more letters, with four of its values corrected for
this hand and six added. What may be new is the text of letter B.

**Earlier failures, read again.** Stages 2 and 2b failed because the plain side was too poor, as said. Stage
3 failed although its marks were right, because an unmarked base is not its consonant (bare `3` is a, bare
`y` is n, bare `7` is o) and a third of the signs are bare letters and word signs that a one-letter model
cannot hold. The failures stay recorded as failures.

**Stage 4b result (2026-11-18): pass** (`results/b-prep.tsv`, `results/b-test.tsv`). Letter B: three readers
(G, H, I), 41 lines, 1,926 to 1,931 signs, pairwise agreement 0.861 to 0.911; the merge keeps 1,885 places
and leaves 43 unread. With `key-v0.tsv` (36 entries, built without letter B) 1,291 of 1,885 read signs get a
value (0.685). Mean trigram log probability inside runs is −2.055; 200 tables shuffled inside each class
give a mean of −2.561 and a maximum of −2.278. Real Italian of the corpus has a median of −2.09 at this
scale. The table reads a letter it never saw.

`run.py b-decode` (after the test): `results/b-decode.txt`. The reading is in `READING.md`.

## The blind table against key-v0 (2026-11-19; `compare_tables.py`, `results/compare-v2-v0.tsv`)
The bench is closed, so the values may be looked at. Run 2's table marks 74 signs; key-v0 values 66 signs of
letter A. 55 are shared: 53 the same, 2 different. 19 the blind table alone values; 11 key-v0 alone values.
The 21 open signs reduce to ten entries:

| Entry | Blind value | key-v0 | Signs | Note |
|---|---|---|---|---|
| mark `1` | u | none | `6+1 7+1 8+1 r+1 s+1 x+1 y+1 z+1` | Pandolfini's value, dropped at stage 6 as contradicted (10 hits, 19 misses) |
| base `2` | b | none | `2+3 2+4 2+5 2+~` | Pandolfini's value was t, dropped at stage 6 |
| base `S` | q | qu | `S+4 S+5` | the 2 that differ: "qe", "qa" against "que", "qua" |
| `flong` | et | none | | Pandolfini's value was f, dropped at stage 6 |
| `bbar` | i | none | | |
| `zm` | non | none | | |
| `Q` | per | none | | |
| `4` unmarked | maesta | none | | |
| `L4` | ell | none | | |
| `ttt` | tt | none | | |

## Stage 7, registered 2026-11-19 before it is run: new values or errors, judged on letter B
`newvalues.py`. The ten entries were built from letter A alone. Letter B has no clear text, so each is judged
by the letter-trigram model (Machiavelli corpus), one entry at a time, with `key-v0.tsv` fixed around it and
the other nine left out. Text: `work/B-merged.txt` (a sign needs two of three readers).

- **Statistic for an entry and a value.** Decode letter B with key-v0 plus that one value. Sum
  (log p + log 20) over every letter trigram that holds a letter of the entry and is not wholly inside one of
  its places. It measures how the value fits what stands round it, against a uniform guess; a value's own
  inside (the "aes" of "maesta") earns nothing, so a common word cannot win by being common.
- **Control.** The same sign with other values of the same length: for one letter, the other 19 letters; for
  a longer value, the 199 commonest strings of that length in the corpus. For base `S` the control also
  holds key-v0's "qu".
- **Bar, whole letter:** the entry stands at 6 places or more, its statistic is above zero, and it is above
  95% or more of the control values (for a letter: first of 20).
- **Split.** Odd lines and even lines of the 41, judged apart. Nothing is fitted on letter B, so this is a
  repeat on two halves, not a build-and-test split; the held-out text is letter B as a whole.
- **Verdicts.** `certain`: the bar is met on the whole letter and on each half. `probable`: met on the whole
  letter, and above 75% of the control values on each half. `error`: at 15 places or more the statistic is
  zero or below and under half the control values are below it; or, for base `S`, key-v0's value scores
  higher on the whole letter and on both halves. Otherwise `unknown`: not shown either way.
- **Joint check.** key-v0 plus the nine new entries together, sum of (log p + log 20) over all trigrams,
  against 200 tables with the nine values shuffled among the nine entries (seed 1). **Bar: above 190 of the
  200.** If it fails, no entry is marked above `probable`.
- **What enters `key-v1.tsv`:** every row of key-v0 unchanged, then each new entry with its verdict and its
  places in letter B. Only `certain` and `probable` rows are used by a decode. A failed entry stays failed.

Known before the run (`results/newvalues-check-A.tsv`, the same test on letter A, the text the values came
from; it is a check of power, not a test):
- On letter A 20 of 29 key-v0 entries with six places or more meet the whole-letter bar, and 18 of 22 with
  17 places or more. So `unknown` is a common outcome for a true value with few places. The run prints the
  same count for letter B.
- Of the ten candidates only `bbar` = i meets the bar on letter A; base `S` = q loses to "qu" there.
- The corpus is a modern print that spells the conjunction "e" (96 "et" against 6,175 "e"). The model
  cannot fairly judge `flong` = et; a failure there is the model's as much as the value's.
- Ten entries at a 5% bar: half a false pass is expected by chance. `certain` asks for both halves as well.

**Stage 7 result (2026-11-19): two entries pass as `probable`, one is an error, six are not shown; the joint
check fails** (`results/newvalues-test.tsv`, `key-v1.tsv`). Run once.

| Entry | Value | Places in B | Above, of control values (whole; odd; even) | Verdict |
|---|---|---|---|---|
| `bbar` | i | 39 | 19 of 19; 18 of 19; 19 of 19 | probable (the odd half is second of 20, so not certain) |
| `zm` | non | 19 | 190 of 199; 181; 194 | probable |
| base `S` | q | 19 | 0 of 20; key-v0's "qu" is first on the whole and on both halves | error: "qu" stands |
| `Q` | per | 25 | 175 of 199; 169; 178 | unknown |
| `ttt` | tt | 5 | 195 of 199; 199; 191 | unknown (under 6 places) |
| `4` unmarked | maesta | 8 | 174 of 199; 181; 140 | unknown |
| mark `1` | u | 37 | 15 of 19; 16; 15 | unknown |
| base `2` | b | 15 | 12 of 19; 17; 8 | unknown |
| `L4` | ell | 15 | 107 of 199; 109; 107 | unknown |
| `flong` | et | 68 | 107 of 199; 110; 102; statistic below zero | unknown (the model does not spell "et"; see above) |

- **Joint check: fails.** key-v0 plus the nine entries scores 1,698.7 (key-v0 alone 1,390.3); 120 of 200
  shuffles are below it, and the bar was 190. The check was badly made: a shuffle that puts the six-letter
  value on the commonest sign adds hundreds of trigrams, and the sum rewards that. It stays failed, and by
  the rule written above nothing is marked above `probable`.
- **Power on letter B:** 25 of 30 key-v0 entries with six places or more meet the whole-letter bar. So
  `unknown` here is weak evidence against a value, not proof.
- `key-v1.tsv`: the 36 rows of key-v0 unchanged, `bbar` = i and `zm` = non as `probable`, and the seven
  others listed as `unknown` (not used by a decode). Each new row carries its places in letter B.
- Of the 21 signs: 2 are errors of the builder (`S+4`, `S+5`: it gives a base one letter and "qu" is two);
  2 are new values at `probable` (`bbar`, `zm`); 17 are not shown (the 8 signs with mark `1`, the 4 with
  base `2`, `flong`, `Q`, `4`, `L4`, `ttt`).
- A lead, not evidence (it comes from this run): for mark `1` the value a scores above u on letter B (53.4
  against 21.3) and on letter A (31.8 against 26.5), though mark `5` is already a.

## Stage 8, registered 2026-11-19 before it is run: letter B read from three readers at once
`lattice.py`, ported from `../1336/lattice.py`. Readers G and I are lined up on reader H line by line; each
column holds three votes; a vote's candidate is the key's value for that sign; the path is chosen by log
vote share plus letter-trigram gain. The model may choose only among letters some reader supports. A column
where no vote has a value prints `?`.

Two changes from no. 1336, both made on planted passages before any real run:
- **Score.** Gain is log p + log 20 for a trigram, and nothing for a trigram wholly inside one sign's value.
  With the plain sum of no. 1336 a table is punished for long values, and this key holds "ancora" and
  "senza": on planted lines of random letters the true table beat its shuffles 14 times in 20.
- **Length.** On planted lines of 80 letters only 9 of 20 Italian lines pass, so the test is made on the
  whole letter (about 1,930 columns), not line by line.

**Self-check** (`results/b-lattice-selftest.tsv`): passages of 300 letters enciphered with key-v0's signs,
three noisy readers (8% wrong, 4% unread, 2% dropped), a quarter of the whole-sign entries hidden, 0.61 of
signs valued. 19 of 20 Italian passages pass (50 shuffles, bar 48) and 0 of 20 random ones. Of the letters
printed as supported 85% are right (4,064 of 4,769): the model sometimes takes one reader's wrong sign
over two readers' right one. So a supported letter is not a certain letter; the reading file marks the
letters all three readers support.

**The test** (`lattice.py test`): `key-v0.tsv`, which was built without letter B, against 200 tables with
the values shuffled inside each class (bases, marks, whole signs; seed 1). **Bar: the true table's path
score is above 190 or more of the 200.** The same is printed for `key-v1.tsv`, with no bar: its two added
values were chosen at stage 7 on this letter, so it is not an independent test of them.
After the test, `lattice.py read` writes `results/b-lattice-read.txt` with `key-v1.tsv`, marking the letters
that rest on the two added values.

**Stage 8 result (2026-11-19): pass** (`results/b-lattice-test.tsv`; committed before the decode was
written). 1,953 columns from readers H, G, I. With `key-v0.tsv` the path scores 1,093.8; 200 of 200 shuffled
tables are below it (mean 96.3, maximum 661.0). With `key-v1.tsv` (not an independent test): 1,214.3, above
200 of 200 (maximum 677.9).

`lattice.py read` → `results/b-lattice-read.txt` (key-v1): of 1,922 columns that hold a sign, 1,396 have a
supported value (2,530 letters), 1,184 of them from all three readers. 526 are open: 525 because the key has
no value for a sign the readers agree on, 1 because the readers did not read it. The single merged text of
stage 4b had 1,291 valued signs; key-v0 in the lattice gives 1,338 columns; the two values of stage 7 add 58.
`lattice.py words` → `results/b-words.tsv`: for each phrase quoted in `READING.md` (list and word division
in `b-words.txt`, the writer's), the letters all three readers support, those one or two support, and the
open places. Over 49 phrases: 969, 124 and 109 of 1,202.
The method's fault shows in the output: at line 36 two readers have the sign for "ne" and one for "se", and
the letter model took "se". The reading file marks such letters.

## Dudout's shapes for the four contradicted values (2026-11-19)
`results/dudout-shapes.md`, counts in `results/dudout-counts.tsv` (`dudout_shapes.py`). His target folders
were fetched again (CLAIMANT; `sources/raw-bourdeau-2026-11-19/`, untracked like the first fetch). They hold
no image of any sign, so shapes were compared through his written legend and through how each sign behaves
in his seven transcriptions (7,363 tokens) and in our two letters (3,061).

| Value held at stage 6 | Verdict |
|---|---|
| mark `1` = u | same shape and the same share of the vowel marks (0.052 and 0.051); no real difference shown; open |
| base `2` = t | our mismatch: his t is `Z`, unmarked, before `7` in 86 of 95 places, which is our unmarked `2` (before `7` in 24 of 45); our `2` with a mark is part of his `2` with a figure (b or c) |
| `flong` = f | our mismatch: `flong` behaves as his `F` (barred F = et; before `3`, `D`, `W`), not as his rare `J` |
| `hash` = ll | our mismatch: his `H` and `4#` (ll) stand after `3^4` and `S^4`, as our `L4` does; our `hash` never does |

So the cipher of 1513 is not shown to differ from Pandolfini's of 1514–15 at any of the four. Leads with two
independent supports (his key, our blind table) and no pass on letter B: unmarked `2` = t, `2` with a mark
= b, `flong` = et, `L4` = ll.

## Where this stands (2026-11-19)
- `key-v1.tsv`: 38 entries used (36 of key-v0, `bbar` = i, `zm` = non), 7 listed as `unknown`.
- Letter B: 0.73 of its columns read, on a test passed before the decode. `READING.md` has the phrases and
  what each rests on.
- Registered since the bench closed: stage 7 (2 of 10 entries pass as `probable`; the joint check failed
  and stays failed) and stage 8 (pass).
- **Wall:** the 525 open columns need key, not readers. The next key values are the four leads above;
  `flong` alone is 68 places. The test for them has to be registered first and must not lean on the letter
  model (it cannot judge "et"): hits and misses on letter A's pair, with letter B held out.
- Not done: any outside check of the reading; an image of Pandolfini's letters for the shapes.
