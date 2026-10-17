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
- The charges do not separate the two telegrams' systems. T1 pays 0.399 per word and T2 0.412 (stamped), within 3%.
  Under the 1932 Madrid Regulations (Art. 10) a code word may be any group of five letters or fewer, so five-letter
  cipher groups qualify as code language (CDE). **likely** (PRIMARY regulations; arithmetic in
  `analysis/11-one-or-two`; `sources/conventions-survey.md`)
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
- Letter counts against telegraph-style references (corrected 2026-10-17, after a glossary in one held-out book was
  found to fatten the null): no candidate language fits T1 well (Spanish p = 0.014, Portuguese 0.022, Italian
  0.004). T2: Spanish 0.024, Italian 0.074, Portuguese 0.108. The misfits: X in T1 (6 vs 1 expected, z +5.0), P in
  T1 (35 vs 23, and vs 16 when the stop word has no P, z +4.8), U low in T1; F in T2 (7 vs 1, z +4.7).
  **established** (`analysis/08-letter-fit`, `analysis/10-convention-fit`)
- The telegrams are letters of a natural-letter text in a new order: plain transposition, transposition with nulls,
  transposition of text mixed with code words, or a jargon code then transposed. Statistics cannot tell these apart
  at these lengths. Monoalphabetic and periodic substitution, bifid, ADFGX/ADFGVX, Playfair, homophonic substitution,
  nomenclator and codebooks of artificial words are excluded (each 40–1,137 log-likelihood units below the best
  transposition type, outside its 1–99% band on several statistics). **established** (`analysis/12-type-diagnostics`)
- T1 is slightly flatter than transposed Spanish telegraph text: IC 0.0695 at the 5th percentile and MIC at the 2nd
  of plain-transposition plants, inside the bands of transposition with nulls or mixed text. **established**
  (`analysis/12-type-diagnostics`, `analysis/10-convention-fit`)
- T1 and T2 fit one letter source (homogeneity p = 0.21) and both rank Spanish first. The F difference is borderline
  (7 vs 2.5 expected in T2; adjusted for 26 letters p = 0.056). Neither telegram shows structure by position inside
  the five-letter group (p ≥ 0.32). **established** (`analysis/11-one-or-two`)
- X in T1 and F in T2 sit where any other letter of the body could sit: residues and gaps at chance (p = 0.73 and
  0.28). Position cannot tell X-as-stop from X-as-null-before-transposition. X as a stop at every sentence end would
  give about 12.5 X in 615 letters, twice the count. **established** (`analysis/09-odd-positions`,
  `analysis/10-convention-fit`)
- T1's last 20 letters (`AXLNKIPLANFTULXREFLX`) hold 3 of 6 X, 1 of 2 K and 2 of 5 F. A scan over every window
  finds this end at every window length; corrected for window position and length, p = 0.019, and 1.8–3.1% of
  transposition plants reach it. T2 shows nothing comparable (p = 0.38). **established** as measured; what it
  means is open (H6). (`analysis/09-odd-positions`)
- Index of coincidence: T1 0.0695, T2 0.0710, natural-language level. **established** (computed 2026-10-16;
  agrees with Bourdeau)
- Letter counts. T1: E73 O69 A58 N53 I43 R40 S39 T36 P35 C30 M24 D24 L20 U16 B12 G9 H8 X6 F5 Z4 V3 Q2 Y2 J2 K2,
  W0. T2: no K, W, X, Q or Y. The catalog entry's "no k, w or x" holds for T2 only. **established** (computed)
- T1 and T2 share 9 distinct 4-grams where shuffles give 2.2 (p = 0.001), and the 6-gram APMOEP (p = 0.011).
  Repeats within T1 are at chance. **established** (`analysis/02-shared-repeats`). After correcting for the choice
  of n and statistic, the excess is suggestive, not established: family-wise p = 0.008 against letter shuffles,
  0.020 against transposed Spanish plants, 0.052 against bigram-preserving shuffles. Reversed matches show no
  excess. Both final groups begin REF (`REFLX`, `REFUD`), seen after looking. **established** as measured
  (`analysis/13-shared-strings`)
- Forward double columnar (CC) is excluded for telegram 1 with w1 ≤ 15 and w2 12–15, and the CR convention with
  w1 2–15 and w2 12–15, for Spanish, Italian or Portuguese plaintext. If both telegrams share keys, CC is also excluded
  for w1 8–15 and w2 16–17. **established** (`analysis/03-target-h1`; controls in `analysis/01-solver/controls/`)
- Every columnar exclusion holds only for the full 615 (or 160) letters. With 5–20 untransposed letters at either
  end, our double columnar solver recovers 0/10 plants (10/10 without), and a single columnar solver 0/40 (39/40
  without). The same mechanism, wrong column lengths, applies to Bourdeau's full-length searches. **established**
  for our solvers, **likely** for Bourdeau's (`analysis/15-tail-robustness`)
- At 615 letters the IDP score of a second key has a usable gradient only within about 3–4 swaps of the true key.
  Lasry-style search therefore fails beyond w2 ≈ 15 (alone) or 17 (jointly). **established** for this solver
  (`analysis/01-solver`, probe and band controls)
- No period source ties any transposition to the Oswalds, to Swiss commerce, or to Spain in 1936–37. The Swiss
  army's hand cipher of the time (Réglette, about 1918–39) is a Vigenère-type substitution. **likely**, as an absence
  of evidence (`sources/key-type-survey.md`)
- The 2020 attempt by Heinzmann, Matteotti, Liniger and Viveksanth is recorded only in Bochsler's note 44 (print);
  nothing of it is online. **likely** (`sources/key-type-survey.md`; Bourdeau NOTES.md)
- Neither telegram has bigram structure of its own, forward or reversed (T1 p = 0.53, T2 p = 0.61 against own
  shuffles). So word transposition, row and serpentine routes (width 5–30) and block moves (sets 3–12) are
  excluded, and the shared strings are not surviving plaintext runs. **established** (`analysis/04-run-keeping`,
  plants 20/20)
- No reversed-direction transposition fits (lag scan). **likely** (CLAIMANT: Bourdeau; not rerun here)
- Letters permuted within sets of n, sets from the first letter: excluded for n ≤ 10 only. `05`'s controls (78/78)
  were invalid: the solver reused the plant's seed, so its first restart was the planted key. With independent seeds
  the same solver recovers n = 5 in 20/20 and n = 10 in 18/20, but n = 20 in 1/20 and n = 35 in 0/20. So n ≥ 20 is
  untested, and n 11–19 unmeasured. Separately, sets of 5–12 at any alignment leave vowel/consonant contact
  structure that T1 lacks (`14`). **established** (`analysis/15-tail-robustness`, `check05-seed.txt`; `05` target
  runs stand where the solver passes)
- Nihilist read by rows is **not excluded**. `05`'s 72/72 controls had the same seed fault. With independent seeds
  the solver recovers n = 8 in 14/20, n = 15 in 2/20 and n = 25 in 0/20, below the 80% pass rule. **established**
  (`analysis/15-tail-robustness`)
- T2 is not a 4 × 4 turning grille in either use (all 1,024 keys), alone or with one key on T1. **established**
  (`analysis/06-grille`, controls 10/10). This holds with untransposed letters at the end (20/20 recovered), not
  with a preamble (0/20). (`analysis/15-tail-robustness`)
- A phrase shared by both telegrams under one key produces the observed excess of shared 4-grams only under
  single columnar and Nihilist read by rows. Under double columnar (8–25) and Nihilist read by columns it stays at
  chance. **established** (`analysis/07-shared-model`). Single columnar does not explain them even with
  untransposed ends: the seven shared runs fit no common column geometry (best 2 runs, where chance gives 2,
  p 0.37 and 0.23; planted geometries recovered in 99.6%, w 5–30), and a shared phrase under one single columnar
  key gives more runs than observed (median 8–33 by width). Nihilist by rows remains untested (above), and under
  `07`'s model it gives 22–74 shared 4-grams, against 9 observed. **established** (`analysis/16-run-geometry`)
- Neither telegram has vowel/consonant contact structure or uneven vowel density beyond what long-key double
  columnar plants give (T1 p 0.56, 0.87; T2 0.84, 0.17; power 0.78–0.98 at 615). The two telegrams' bigram profiles
  overlap beyond their letter counts (+70; p ≈ 0.003 under those plants), a statistic found after looking.
  **established** as measured (`analysis/14-contact`)

## Prior scholarship: settled points
- Tomokiyo (2023) excluded the British Government Telegraph Code. **likely** (SECONDARY, Cryptiana)
- Bourdeau's exclusions, all with planted controls: every single transposition (single columnar to width 45),
  all reversed-direction systems, forward double columnar with w2 ≤ 11 (w1 ≤ 41), both mixed conventions with
  w2 ≤ 10, and K2 a dictionary word or 1–5-word phrase. **likely** (CLAIMANT; table in `README.md`)
- No source documents any transposition system in use by any party in Spain in 1936–37. Documented Spanish Civil
  War systems are substitution-based (Enigma from Nov 1936, strip ciphers, LUCI). German army double transposition
  is documented for WWI and from 1940. **likely**, as an absence of evidence (agent B, `sources/context-cribs.md`)
- The German army separated sentences with X by 1930 (its Enigma test message). No Swiss or Spanish source for X as
  a stop was found; French and Spanish telegrams of the period used STOP. Givierge (1925) leaves an incomplete
  columnar table as it is, with no filler, and puts indicators at the head of a message. No final reference group
  or "REF" convention was found. **likely** (SCHOLARLY: Weierud; Givierge; `sources/conventions-survey.md`)
- Bourdeau's statement that German Doppelwürfel users were told to take key phrases of 15–25 letters has no source.
  **likely** (agent B; Bean, issue 37)
- Lasry's IDP method solved Schmeh's 599-letter challenge (keys 21 and 23; 599 = 26 × 23 + 1). Lasry reports
  over 60% success at keys 19 × 20 and 90% at 18–19 on simulations. **established** that he reports it (SCHOLARLY:
  Lasry thesis 2018, ch. 9, https://kobra.uni-kassel.de/handle/123456789/15274)
