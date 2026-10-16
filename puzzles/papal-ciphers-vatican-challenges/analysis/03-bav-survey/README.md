# 03 — Survey: cipher material on DigiVatLib (Vatican Library)

**Question.** Which Vatican Library manuscripts that are free on DigiVatLib hold
ciphertext that has not been deciphered, with or without a known key?

**Method.**
1. `harvest.py` (uses `opac.py`) runs the library catalogue's keyword search
   (opac.vatlib.it/mss, simple search, `k_f=0`) for 39 cipher terms in Italian,
   Latin, French and German. It needs a session cookie, which `opac.py` gets.
   Output: `opac-cipher-hits.json` (326 shelfmarks). `strong-hits.txt` keeps
   the 111 matched by a term other than "cifre"/"chiffres" (those two mostly
   match "Arabic numerals" in foliation notes).
2. The cipher-relevant subset was probed for an IIIF manifest
   (`digitized.json`: shelfmark, canvases, max width; 0 = not online).
3. `page.py` fetched sample pages of every online candidate, which were
   inspected by eye (Claude, 2026-10-16). `detail.py` pulls full records.

Run from this folder with plain `python3` (not `-I`; the scripts import each
other). DigiVatLib rate-limits (HTTP 429) after a few dozen requests; the
fetchers back off.

**Result (2026-10-16).**

| Shelfmark | Online | What it is | Status |
|---|---|---|---|
| Barb.lat.6956 | yes | Pallotto, Vienna 1628, digit cipher; decipherments in volume | read (Vatican Challenge 1) |
| Barb.lat.6960 | yes, microfilm | Pallotto, Vienna 1629, digit cipher | probably read by 1628 key; printed by Kiewning (exp 02) |
| Borg.lat.898 | yes, colour | Whole book in symbol cipher, "Cifrario farmacologico" | **the Borg cipher**, solved 2017 (Aldarrab, Knight, Megyesi) |
| Barb.lat.9848–9849 | yes, colour | Francesco Mancini, Madrid, to Card. F. Barberini, 1644–55; digit cipher passages | **interlinear contemporary decipherment** (f. 7r: Christina of Sweden, Medinas, Paris) |
| Cappon.164 ff. 292–299 | yes | "Lettere in cifra" of the nuncio in Spain (Taverna), 1584–85, incl. Mary Stuart 9 Nov 1584 | plaintext decipherments, no ciphertext |
| Urb.lat.948, 949 | yes | Federico da Montefeltro's cipher tables ("scriptura occulta") | keys/tables, no messages |
| Urb.lat.998 | yes | 15th-c. papal key collection | keys |
| Borg.lat.565 ff. 18v–19r | yes, microfilm | Jesuit China-mission cipher key | key; faint on microfilm |
| Vat.lat.9684 | yes, microfilm | Lincei letters (Cesi, Heckius), short enciphered names in plaintext letters | period decipherment in volume (f. 140r) |
| Vat.lat.2392 f. 72v | yes | 14th-c. bird-catching secret "in cifra cum eius explicatione" | self-explained substitution |
| Urb.lat.1704, Urb.lat.868, Vat.lat.13153 | yes | catalogue says "cifra"; pages checked are plaintext copies | not cipher |
| Barb.lat.7633–7636, 9846, 9850–9886, 9914–9915; Vat.lat.14673, 12531, 10421 | **no** (404) | Zacchia decipherments 1621–23; Barberini agents' letters 1644–1705 "cifre, decifrati"; "Cifre antiche"; cipher copies to Gesualdo 1617–21 | not digitized |
| Vat.lat.8214, Borg.cin.520, Vat.lat.7203 | yes / yes / 429 | Mantua ambassadors 1523–24; Japan mission letter; Tolomei's treatise on ciphers | not inspected |

**Verdict.** No online Vatican Library volume found so far holds ciphertext
without a period decipherment, a modern solution, or a printed edition. The
recurring pattern: the Barberini holdings preserve cipher letters *with* the
decipherment written between the lines or filed alongside.

**Limits.** The catalogue under-describes cipher material: Barb.lat.6956 and
6960, both cipher volumes, are catalogued as "shelfmark only" and no keyword
finds them. The Barberini nunciature series (around Barb.lat.6950–6990 and
beyond) is the same, so a keyword survey cannot be complete. A complete sweep
needs page sampling by shelfmark range.
