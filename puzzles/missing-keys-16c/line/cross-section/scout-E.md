# Scout E: 2646, 2575, 2577 (Koç HPBK, palace to Yemen), 2026-11-19

Images are at `sources/cache/cross/<id>/` (gitignored). They come from the CONTENTdm IIIF route
`https://cdm21054.contentdm.oclc.org/iiif/2/HPBK:<n>/full/full/0/default.jpg`, which worked on the first try
today. A compound item's page ids come from `dmGetCompoundObjectInfo`, for example 688 → 686/687 and 533 → 531/532.
Sign heights come from `line/sign_height.py`. No reading was attempted.

**Requirement for all three:** someone who reads Ottoman Turkish in Arabic script, in an unvowelled rika
hand. That person has to judge the clerk's glosses, align the clear sheets and read any output. No pair below
can be confirmed beyond shape matching without them.

**Outside overlap:** `targets/hpbk1896` in the profiles covers systems A and B of this traffic by shelfmark.
The taken file does not list it under these ids. Under that target, Brice Dudout (PR #702) made blind AI
transcriptions of 10 B sheets and two gloss tables. One held-out test fell short of its bar (0.787 against
0.85). The other failed (0.5625). The outcome is "not read". The item is not solved, but someone else is
working on it. Greg should decide whether that rules 2646 out.

## 2646: system B, verdict pass, with caveats

- **Page seen:** 541 (w 2023), a printed telegram form with a 12-row grid. In it are two-digit Eastern Arabic
  numerals, with a letter written over almost every cell. Three-digit numerals (668, 745, 157, 771, 711) carry
  word glosses. The form's "Group" field reads about 109.
- **Measurement:** h_median 27 on box 1586,1790,230,1417. That median mixes the numerals (about 44) with the
  smaller glosses (about 10).
- **Design:** letter numerals plus word codes, which makes it a small nomenclator.
- **Are the glosses a full key?** No.
  - 587 and 602 have no glosses.
  - Three-digit codes are glossed only where they happen to occur.
  - Dudout found 49 glossed differently across sheets.
  - The job is therefore transcription, consolidation and a held-out test, then reading. It is not a blind
    key build.
- **Possible clear crib:** 575 (about 177 numerals) against 1070 (clear, same date). This is unconfirmed:
  575's From/To line appears to name Yıldız as the recipient. 688 and 533, which are filed under 2575, are
  also B sheets and belong here.
- **Sources:** https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/541,
  https://islamansiklopedisi.org.tr/huseyin-hilmi-pasa, https://dergipark.org.tr/tr/download/article-file/113954

## 2575: 18-19 Dec 1898, verdict fail at the buildable gate

- **Is 727 the same text as 772?** Yes. 727 is a clear text of about 6 lines. 772's interspersed clear words
  recur in it in the same order. This is a shape match, not a reading.
- **Which system is 772?** A code list of about 32 five-digit groups (w 2260). Some groups repeat: 15118 twice
  and 14772 three times.
- **Measurement:** h_median 36 on the whole block and 43 on the groups only.
- **Why it fails:** the pair is of a code, and 32 groups cannot build a codebook with our method.
- **688 and 533:** both are system B. 688 has about 27 lines per side with many clear words, and measures 30.0
  on its front page (686). Both should move to 2646.
- **Sources:** https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/772,
  https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/727

## 2577: 1901-02, verdict fail (merge)

- **Page seen:** 576 (w 2057, h_median 31), system B with letters over most numerals. About 110 numerals, and
  668 appears.
- **Possible crib:** 726 is a clear sheet of the same day, addressed to the cipher clerk Asım, about Farasan.
  It may not be 576's text, because 764 is also a Farasan cipher of that day.
- **Why it is not a separate item:** the entry pools A (550, 595, not viewed) with B. Its B sheets are test
  passages for the 2646 key.
- **Sources:** https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/576,
  https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/726

## What would change the verdicts

- If an Ottoman reader confirms that 1070 is the clear text of 575, or 726 of 576, 2646 gains a pair of more
  than 100 signs that is independent of the glosses.
- If Dudout's work is counted as "taken", 2646 fails the not-taken gate.
