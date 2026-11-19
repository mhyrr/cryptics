# Scout B: 1308, 2645, 2405, 2630 (2026-11-19)

All four fail. No page image was fetched or measured. Every candidate's images are on DECODE, and DECODE
sends image requests to its login page (`ImagesList?showmaster=records&fk_id=5436` and `fk_id=7908` both
redirect to `/decrypt-web/login`). The record metadata is public, and for these records it is empty: no
Sender or Receiver, and dates 1450-1555. BnF ital. 1583 is not on Gallica (catalogue folio_note). This scout
saw no page. Every statement below about what a page shows comes from the catalogue or from the outside
profiles (`sources/cache/bourdeau-profiles-2026-11-19.json`).

## 1308: Tranchedini and Alamanni to Sforza, Nov 1446. Fail at Not taken.
- Matters passes. The DBI says Sforza sent Tranchedini to Florence in autumn 1446 as his trusted agent, that
  he built the tie with Cosimo, and that his letters were "spesso cifrate" ("often in cipher").
  https://www.treccani.it/enciclopedia/nicodemo-tranchedini_(Dizionario-Biografico)/
- Taken. Outside target `tranchedini1446` (lead 1317 in the taken file) works the same two leaves, f. 134
  and f. 139:
  - f. 139 is transcribed (778 signs) and 62% of its signs have values;
  - a contributor identified the key sheet DECODE R5318, headed "Nicodemus" (PRs #625 and #630), and tested
    it against the 1448 pair, ital. 1585 ff. 27-30;
  - the outcome is recorded as "work in progress".

  This item belongs to that target.

## 2645: cart. 1598/1591 family Z. Fail at Matters, and Buildable fails by construction.
- Outside `sforza1598/NOTES.md` lists Z as "38 singletons, unmatched hands". It is the leftover group from
  the box split, not one cipher.
- Writer and recipient are unknown for all 38 letters.
- The ASMi inventory dates cart. 1598 to 1471-1720 and cart. 1591 to 1494-1736, so the DECODE "1450" is a
  placeholder.
  https://archiviodistatomilano.cultura.gov.it/fileadmin/risorse/Patrimonio_archivistico/Fondi_e_Inventari/Visconteo-Sforzesco__1183-1593_/Potenze_sovrane_e_altre_voci-VS_2-1.pdf
  (pp. 216-218)
- No letter has a second passage in its own hand.
- What would change this: a key sheet matched to one letter.

## 2405: cart. 1597 family G. Fail at Matters; Readable blocked.
- The outside target `sforza1597` worked families A, E and F, and its notes list G but never work it. G is
  not taken.
- Writers are unknown, and G mixes several sign hands, so it is not one correspondence.
- One lead: the catalogue says R5436 is a clear leaf headed "da cifra" ("from the cipher", that is, a
  decipherment). If its cipher twin is among R5440, R5442 or R5472-R5474, that sub-family would have a pair,
  and Matters could pass from the clear text. Checking this needs a DECODE login.
- For readability, the outside profile reports that this box's DECODE images are about 1,671 px wide, with
  signs 15-25 px high on R5464 (family F, not G). That is borderline, and G itself is unmeasured.

## 2630: cart. 1598 family C. Fail at Not taken; Matters also not met.
- Outside `sforza1598` has already done the work:
  - transcribed 8 of the 9 letters;
  - recovered a key from the ciphertext alone;
  - tested it out of sample, with a word share of 0.42-0.47 against 0.10-0.17 for shuffled text;
  - read in part (conte Iacomo, l'impresa de Urbino, la Mirandola).
- It compared the family C key with all 208 key sheets and matched none.

## What was not checked
- Cerioni 1970 (it edits the keys of this series).
- The Voynich Ninja pointer to a paper on a 1449 Tranchedini cipher.
- The Pelling 2011 thread, not re-read.
- The pages themselves.
