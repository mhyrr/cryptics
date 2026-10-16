# 02 — Does the 1628 Pallotto key read Barb.lat.6960?

**Question.** Does Tomokiyo's reconstructed key for Vatican Challenge Part 1
(Pallotto, 1628, Barb.lat.6956) read the 1629 cipher letters in Barb.lat.6960?

**Method.** One eye transcription (Claude, 2026-10-16) of line 1 of image 0005,
read from 6× enlarged crops of a ~750 px microfilm image. Parsed with 1 and 8
as one-digit separators. Decoded with `check.py`. The letter is headed "Di
Vienna 4 di Agosto" and is compared with Kiewning, *Nuntiaturberichte* IV/2
(1897), Nr. 153, Pallotto to Barberini, 4 Aug 1629, deciphered 22 Aug, from
Arch. Vat. Nunz. di Germ. 119 ff. 11–19, which opens "Ho ricevuta la risposta".

**Run.** `python3 -I check.py` → `result.txt`.

**Result.**
```
decode : h[7?]__rilievto_la__rislio[79]p[0?]
crib   : ho_ricevuta_la_risposta
```
19 of 22 groups are in the key. The decode aligns with the crib position by
position (h·o, r i · e v, la, r i s · o · p). Two groups differ: 37 (key: li)
where the crib needs c (key: 32), and 93 (key: to) where the crib needs "uta".
Both are plausible misreadings of this hand at this resolution (2/7, 9/u-group).

**Verdict.** Suggestive, not established. The same key, or a close variant,
probably reads 1629. To settle it: a second independent transcription of the
first three lines, then a decode against the full printed Nr. 153 text.

**Limits.** One reader, one line, one letter. Microfilm images of ~700 px per
page; digit confusions 2/7, 1/4, 0/6, 9/g likely.
