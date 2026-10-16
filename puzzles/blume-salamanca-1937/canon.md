# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` / `disputed`), and a source pointer.

## The object
- Two cipher telegrams, Zurich to "BLUME SALAMANCA", 8 January 1937, are in the Swiss Federal Archives,
  E4320B#1974/47#277 (*Spanische Revolution (Passvisas etc.)*), subdossier 0000066, Unterlagen_0000072, canvases 9
  (telegram 1) and 13 (telegram 2). These are PTT copies sent to the Federal Police on 15 Jan 1937. **established**
  (PRIMARY: IIIF scans, `sources/images/`, `sources/headers.md`)
- Telegram 1: printed form, serial 1381, Zurich office 797, handed in 11:31, sent on to London at 11:42, fee 49.90,
  125 words (= 123 groups + 2 address words), routed "Angleterre Eastern". A typed "(VIA VIGOEMDENKABEL)" is struck
  through. Margin note "als Chiffriert aufgegeben" ("handed in as cipher"). Red note: "Aufgabe: Oswald Viktor,
  geb. 15.11.1909, in Burgos" ("handed in by Viktor Oswald, born 15 Nov 1909, in Burgos"). **established** (PRIMARY,
  `sources/headers.md`)
- Telegram 2: plain sheet, serial 1486, Zurich office 910, "Cde" stamp, handed in 17:34, sent on 17:40, fee 14.00.
  The reverse has 47 × 34 = 15.98, and 34 = 32 groups + 2. **established** (PRIMARY, `sources/headers.md`)
- The sender block names "Dr. ing. W. E. Oswald, Bureau Bahnhofstr 12, Zürich". **established** (PRIMARY)
- The dossier holds no key, no plaintext and no third ciphertext. **likely**: the telegram unit was viewed in full,
  and the other 219 files were checked by the archive's OCR only (agent A, 2026-10-16). Bourdeau read all 42 images
  and agrees (CLAIMANT, NOTES.md, 11 Oct 2026).

## The text
- Telegram 1 has 123 five-letter groups, 615 letters; SHA-256 of the letters e266615d…434c55. Telegram 2 has
  32 groups, 160 letters; SHA-256 8fd5cfb8…e17a644. Our blind reading from the archive scans agrees letter for letter
  with Bourdeau's and Bean's. **established** (`sources/PROVENANCE.md`)
- The three formerly disputed groups are SOLRS (38), ACCEL (48) and FTULX (122). On this typewriter the L has a top
  serif on the left and a long foot; the I has serifs at both ends. **established** (issue 14; our reading)
- Group 113 RBEEP is counted and legible. The red stroke is the underline of the red note, not a deletion.
  **established** (PRIMARY)

## Dating, provenance, authorship
- Werner Oswald told the police (28 Apr 1937) that his brother Viktor sent the telegrams while passing through Zurich.
  He said they concerned reopening an office in Nationalist Spain and a wool deal to unfreeze Swiss export credits,
  kept from Hisma (Seville) until it had been put to the authorities in Burgos. He said he did not know the content
  or the key. **established** that he said so (PRIMARY via Bourdeau's and agent B's reading of the interrogation);
  the content of the claim is unverified.
- Who or what "Blume" is: unknown. **established** (agent B, `sources/context-cribs.md`)

## Structure and statistics (from `analysis/`, never from impression)
- Index of coincidence: T1 0.0695, T2 0.0710, natural-language level. **established** (computed 2026-10-16;
  agrees with Bourdeau)
- Letter counts. T1: E73 O69 A58 N53 I43 R40 S39 T36 P35 C30 M24 D24 L20 U16 B12 G9 H8 X6 F5 Z4 V3 Q2 Y2 J2 K2,
  W0. T2: no K, W, X, Q or Y. The catalog entry's "no k, w or x" holds for T2 only. **established** (computed)
- T1 and T2 share 9 distinct 4-grams where shuffles give 2.2 (p = 0.001), and the 6-gram APMOEP (p = 0.011).
  Repeats within T1 are at chance. **established** (`analysis/02-shared-repeats`)
- The ciphertext has no bigram structure of its own, and no reversed-direction transposition fits (lag scan).
  **likely** (CLAIMANT: Bourdeau's planted-control results; not rerun here)

## Prior scholarship: settled points
- Tomokiyo (2023) excluded the British Government Telegraph Code. **likely** (SECONDARY, Cryptiana)
- Bourdeau's exclusions, all with planted controls: every single transposition (single columnar to width 45),
  all reversed-direction systems, forward double columnar with w2 ≤ 11 (w1 ≤ 41), both mixed conventions with
  w2 ≤ 10, and K2 a dictionary word or 1–5-word phrase. **likely** (CLAIMANT; table in `README.md`)
- No source documents any transposition system in use by any party in Spain in 1936–37. Documented Spanish Civil
  War systems are substitution-based (Enigma from Nov 1936, strip ciphers, LUCI). German army double transposition
  is documented for WWI and from 1940. **likely**, as an absence of evidence (agent B, `sources/context-cribs.md`)
- Bourdeau's statement that German Doppelwürfel users were told to take key phrases of 15–25 letters has no source.
  **likely** (agent B; Bean, issue 37)
- Lasry's IDP method solved Schmeh's 599-letter challenge (keys 21 and 23; 599 = 26 × 23 + 1). Lasry reports
  over 60% success at keys 19 × 20 and 90% at 18–19 on simulations. **established** that he reports it (SCHOLARLY:
  Lasry thesis 2018, ch. 9, https://kobra.uni-kassel.de/handle/123456789/15274)
