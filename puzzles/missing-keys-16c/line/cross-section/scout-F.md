# Scout F: new candidates from sources the survey skipped (2026-11-19)

This is gating only. No reading was attempted. Rows are in `scout-F.tsv`. Images are in
`sources/cache/cross/<id>/`, which is gitignored.

## What was searched, by source

**1. DECODE (de-crypt.org).** Keyword search works through `RecordsList?cmd=search&search=<q>&searchtype=AND&recperpage=200`.
I ran "nunzio", "Simancas", "Venezia", "Mantova", "Modena" and "Firenze", keeping 1450-1650 and the statuses Non-decrypted, N/A and Partial.
- **AGS Estado (13 records, R9952-R9970).** All of them are covered by outside targets: vargas1552, renard1554,
  cifuentes1534, muxetula1531, mai1531, charles1536 (which also covers R9952), isabella1531, burgo1527 (R9970) and
  caracciolo1537 (R9966). None is new.
- **AAV, i. 1025 Segretario di Stato (R5612-R5624).** The Francia 32 records are in the catalogue as no. 881 and in
  outside profiles (sega1590, sega1591b). R5624 (Spagna 22, 1579, with interlinear plaintext) is new. Gated below.
- **BAV, Barb.lat 6956 and 6960 (R285-R318, Pallotto 1628-29).** New. Gated below.
- **Mantova and Firenze.** The hits are keys (E. I. 2 busta 423, ASFi SII vol. 9), not ciphers. Venezia gave no hit
  in range.
- **Modena (Costabili, Caprile, Beatrice d'Aragona).** These are marked partially decrypted. I did not grep them
  against the catalogue; that is worth a follow-up.
- **Images.** Every AAV record serves a 200 px thumbnail. The full image is a placeholder that reads "Insufficient
  permissions".

**2. Vatican.** I searched for BAV cipher letters with interlinear decipherment. The search found Filiberto Ferrerio,
nuncio in France 1537-40, AA.Arm. XVIII 6532, with interlinear decipherment (Histocrypt paper on Antonio Elio's
cipher). AAV holds it and it is not online, so it was not gated. Meister 1906 is on HathiTrust with US access only.
It was not fetched, and its tables stop at 1600 in any case.

**3. Venice.** The Capi del Consiglio dei Dieci, Lettere di ambasciatori, b. 22 (1523-25) holds 42 secret letters
deciphered by Soro, and an edition of them exists (https://faustosartori.altervista.org/alterpages/files/DISPACCI_1523_1525.pdf).
The keys are in CX, "Cifre, chiavi e scontri di cifra" (https://suriano.huygens.knaw.nl/?p=88). I found no online
images, and Soro's treatise is lost. Nothing was gateable in three fetches.

**4. Simancas.** The Valencia and Salamanca school has worked through this source heavily. That includes Luo 2025 on
Juana's regency (legajos 507-518, keys reconstructed), and the Estudios Románicos papers on Rome 1543 and Naples 1547
(leg. 1037). I gated one to record that it is taken. A direct PARES search was not run; PARES has no simple query
endpoint.

## Candidates

**new-pallotto1628: fail at Readable (8 px).**
- **What the pages show.** Barb.lat.6960 is Rome's book of *decifrati*. Its letters carry headers such as "Di Vienna
  da Mons. Pallotto ... Decifrata li 6 di settembre" ("From Vienna, from Monsignor Pallotto ... deciphered on 6
  September") (6960/0081). It holds no cipher. Barb.lat.6956 holds the cipher originals: continuous digit strings
  of the papal kind, for example 6956/0064, about 30 lines of about 90 digits each, counted by eye.
- **Pair.** The cipher, the decifrati and Kiewning's printed edition together are a natural pair.
- **Why it fails.** The scans are bitonal microfilm at about 1,100 px per page. `sign_height.py` gives h_median 8.0
  (a30 12.0), under the 11 px of no. 1336.
- **What would change it.** A colour rescan by BAV.
- **Taken in part.** The clear text is printed in NBD IV 1-2 (Kiewning 1895-97), so the gain would be the key, not
  the reading.

**new-sega1579: fail at Readable (no image access).**
- DECODE R5624 is numerical with "Inline Plaintext: Yes", which points to an interlinear decipherment of the time.
- DECODE names no sender. My attribution to Filippo Sega is unverified.
- The images need a DECODE login, and AAV is not online.
- Not checked: whether the DECRYPT papal-cipher work (Lasry et al. 2020) already covers it.

**new-juana1555: fail at Not taken.**
- AGS Estado leg. 510 docs 1-2 (doc. 2 is the decipherment).
- Luo 2025 (https://doi.org/10.6018/ER.615151) prints the reconstructed Cifrario B (1554-59) and Cifrario G (1556).
- Any work here would be a known-key reading.

**Net.** Scout F found no candidate that passes all four gates. The best lead is Pallotto: a large pair, one chancery,
many passages. Its wall is image quality (bitonal microfilm), and only a better scan would breach it.
