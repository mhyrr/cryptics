# NEXT — handoff for the next session

**Last session:** 2026-09-20. Experiments 12 to 15. E1 and E2 untouched.
**Where it stopped:** the seed half of the construction is supported with
controls; the interior half has a description (vowel/consonant filler) and no
rule for the letter. The handoff's E3 was redirected; read why below.

## The picture now

1. Caption subject, looked up as a German headword in the 1595/1596
   dictionary, gives the seed word (top row) from the printed Hebrew
   transliterations. H7, H17 supported. Experiments 12, 14.
2. Symmetry (transpose plus half-turn) gives the borders. Scored against
   Dehn's German-based readings: 83 of 90. H4 supported. Experiment 13.
3. The interior alternates vowel and consonant down from the seed (79 % on
   unseen cells). The letter inside that class is at 32 % against a 25 %
   baseline. Dictionary words do not sit on interior rows, with or without
   the caption. H16 supported; H12, H14, H15 weakened. Experiments 12 to 14.
4. The spirit names of Book II chapter 19 share rows with the squares, seeds
   and interiors alike. They do not fill blanks. H18. Experiment 15.

## Do first

1. **Raise the seed count from a floor to an estimate.** 56 of 232 top rows
   match the OCR vocabulary; 176 do not. Sort the misses: OCR gaps (check the
   entry image for a caption-nominated headword), Greek glosses (OIKETIS,
   PROXONOS, YPARCHOS look Greek; the dictionary prints Greek in Greek type,
   so romanize that column and rerun experiment 12's row test), Latin glosses,
   and true residue. Freeze the romanization before looking at hits.
2. **Per-square caption test with German captions.** Experiment 14 used
   English labels and scored by chapter. The Warburg print
   (`sources/warburg-1853.pdf`) has the German captions. Transcribe captions
   only, keep E2's crop discipline, reuse `lookup.py` unchanged, and score
   label-to-square alignment. Chapter 5 is development data.
3. **Read the 21 experiment 14 hits on the page images.** Two are done
   (`sources/caption-seed/`). Locators are in experiment 14 `lookups.json`.
4. **Attack the second clause of H16.** Is the interior letter free? Tests
   that could refute it: per-chapter or per-prince letter preferences; reuse of
   seed letters (39 % of interior letters occur in the top row; compute the
   chance rate); the AREPO pattern in row two; agreement between witnesses.
   If Mathers and Dehn disagree more in interiors than on seeds after
   controlling for position, copyists had nothing to correct interiors against.
   Current raw rates: top row 28 of 298, interior 71 of 563.
5. **Third witness.** The Warburg print's square letters are unread except
   chapter 4's moon and water rows. Freeze any new interior model first, then
   transcribe and score. This is the last cheap blind set.

## Named limit

The wall is the interior letter. Nothing tested predicts it much better than
class frequency. If item 4 finds no structure, the honest result is: seeds
from the dictionary, borders from symmetry, interiors chosen freely for
pronounceability, and blank interiors recoverable only by collation of the
German witnesses (Dehn, Kollatsch, Dresden, Wolfenbüttel).

## Exposure

Mathers: fully exposed. Dehn readings for chapters 1 to 14 (all that Peterson
prints): exposed on 2026-09-20; 5/1 and part of the reading beside 5/2 before
the experiment 13 freeze. Experiment 14 nominators saw labels only. The main
thread has seen which top rows match the dictionary. Warburg chapter-5 square
letters: still unread. No untouched-manuscript score exists.

## Earlier queue, still open

Mathers print audit, ten excluded layouts, label 25/4 among chapter 24, frame
disagreements, Dresden N 111 and HAB access, an earlier dictionary edition for
H7's edition-specific clause. TK-005 remains open.
