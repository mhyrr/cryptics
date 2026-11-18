# Published tables that could belong to the cipher of no. 2351

Scout run 2026-11-18, one agent, no sub-agents. Web search and fetch only, plus `gh api` reads of a public
GitHub repository. Nothing here was tested against our transcription and no reading was tried. About 22
fetches and searches were used. The run stopped because the three leads were worked through, not because it
hit the fetch limit.

## 1. Pandolfini 1514-15 key (Dudout, key v6): the table the gate means

**What it is.** A key rebuilt in November 2026 for Francesco Pandolfini's cipher letters from the French
court, December 1514 to March 1515. The letters are in Archivio di Stato di Firenze, Mediceo avanti il
Principato, **filza LXXII**, docs. 307, 309, 310, 311, 322 and 333, the same filza as our docs. 190-192.
Bourdeau's catalogue lists them as no. 2389. Brice Dudout (L'Europe chiffrée) built it with Claude Opus
agents from cipher/decipherment pairs written at the time and kept in the same filza (docs. 345/346, 340/341
and 342/343). WAINUT then applied it unchanged to a Pandolfini letter from Vercelli, 6-8 Sept 1515 (MAP
CXXXVII doc. 666, no. 2393). This is the "published table with a similar sign style" in our gate. It is a
modern reconstruction, not a period key sheet.

**Sources.**
- CLAIMANT · `https://github.com/dbourdeau/cyphersolver/tree/main/targets/pandolfini1514`: `NOTES.md`,
  `key_v3.json` (the only key frozen before it was measured), `key_v4.json`, `key_v6.json`,
  `frozen/LEGENDE.md` (the token legend, in French), `frozen/ARBITRAGE-v6.md`, `validation.txt`.
- CLAIMANT · `https://github.com/dbourdeau/cyphersolver/tree/main/targets/pandolfini1515`: `NOTES.md`,
  `SIGN_CONVENTIONS.md` (shapes in English), `key.tsv` and `key_frozen.tsv` (v6 as rows, with three shape
  aliases and one added sign).
- Our copies, fetched 2026-11-18 from `main`: `raw-bourdeau/` (8 files, unchanged).
- PRIMARY, not seen by us: the period pairs MAP LXXII 340/341, 342/343 and 345/346.

**How it is said to work** (their NOTES, in their words where it matters). Consonant signs carry the vowel as
a superscript figure: **1 = u, 2 = o, 3 = i, 4 = e, 5 = a**. A bare consonant sign is the consonant alone.
There are also:
- bare vowel signs (`3` = a, `W` = i, `O` = o, `Q` = e, `p` = u);
- homophones (c: 0, K, D; l: x, c; m: 5, A; n: y, t; r: 7, d; s: 6, r; t: 8, Z);
- a few context rules (`6` + vowel = p + vowel, while bare `6` = s; `y` + vowel = f + vowel);
- doubled consonants, written with a double bar (`t#` = tt, `4#` = ll);
- word signs (F et, M non, α per, D che, D^n con, T senza, T^m Sua Maestà);
- a nomenclator of numbers between points (.2. papa, .4. Cristianissimo, .20. Svizzeri, .24. Milano, and so on).

The marks `^n` and `^m` occur over word signs.

**How well it is supported.** Their own held-out tests are weak:
- P01 (346 against 345): character agreement 0.788, control 0.338. P02 (340/341): 0.691, control 0.341.
  Both fall short of their 0.85 bar.
- P03bis (342): "partial" under a lenient n-gram criterion.
- v4 and v6 are "declared, not measured".
- On no. 2393 (whole letter held out), frozen-key coverage was 0.820 against 0.629-0.685 for shuffled keys.

The values are reported, not established. The vowel rule is the part with the most support, because every
reading they made rests on it.

**How close it looks to ours.** Close in kind. Item by item:
- **Bases.** Their shapes are small letters, figures, capitals and invented signs. Several of them, judged
  only from the written descriptions, look like signs in our guide:
  - their `J` (ʄ, looped long s/f) is our `flong`;
  - their `Z` ("-2", a stroke then a lying 2) is our `2` with its flat entry stroke;
  - `A` (Δ) is our `triangle`; `H` (#) is our `hash`; `W` (ϖ) is our `omega`; `Q` (φ) is our `phi`;
  - `α` is our `alpha`; their `9` ("q-like") is our `q`.
- **Mark-taking bases.** Our sixteen are `7 3 8 y t x r s q z 6 2 4 S 5` plus one. At least 13 of them have a
  base of the same character, or a likely equivalent, among their consonant signs:
  `7 3 8 y t x r 6 2 4 S 5`, `q`=`9`, and `z`/`2` against their `2`/`Z`.
  Their bare-vowel and word signs (W O Q p F M α T) never take vowel marks in their key, and our non-marking
  signs include omega, phi, alpha and capitals. This is the same split.
- **Marks.** Theirs are figures 1-5 plus `n`/`m`. Ours are 1, 3, 4, 5, a tilde, and `^n`. **We record no
  `^2`, which would be their o, one of the commonest vowels in Italian.** A tiny 2 drawn small and quick can
  look like a wavy stroke, so our `^~` may be their `^2`. This is an observation for the main thread, not a
  finding.
- **Doubt.** Their `2`, `Z`, `d`, `G`/δ, `r`, `L` and `D` do not match our names one for one; see the notes
  column of the TSV. Their `2` is "a 2 or a curled ʒ, not told apart", which could be our `z`, `brace` or `2`.
- **Same people.** Desjardins-Canestrini vol. II prints joint letters "Pandolfini et Acciajuoli aux Dix"
  from Paris, 30 April-1 May and 9 May 1514 (MAP filza 105). Our OCR, `../cache/print/negociations-v2_djvu.txt`,
  has them at lines 29210 and 29360 (SCHOLARLY). The two men served the same embassy within seven months of
  our letters, so sharing one cipher is plausible. This is not shown.

**Files.** `table-pandolfini-v6.tsv` has 87 rows: 5 vowel marks, 33 bases, 38 tokens (syllable and word
exceptions), 9 codes, and 2 rows from no. 2393. The `sign` column uses our SIGN-GUIDE names where a
description match is plausible, and `|` or `?` where it is not sure. The `note` column always gives their
original token as `D:<token>` and how sure the shape match is. Their context rules and the alternatives
they did not apply (2 = b, bare 5 = h, J = s or f) are in `raw-bourdeau/pandolfini1514__key_v6.json`.

## 2. BNCF Carte Machiavelli VI/82: period key sheets "with the orators of France"

**What it is.** Four sheets of one Florentine chancery cipher, held in the Biblioteca Nazionale Centrale di
Firenze. Unit 1 has the endorsement "Cyfra co(n) li Or(ator)i di Francia / it(em) p(er) Roma ... Francesco
Gualterotti et ... Luigi della Stufa or(ator)i al Re Christianissimo" (cipher with the orators of France,
also for Rome, with Francesco Gualterotti and Luigi della Stufa, orators to the Most Christian King). Its name
list dates it to about 1500-1503. Units 3 and 4 have renumbered name lists naming Chaumont and La Trémoille,
so they date to about 1510. Item 2911 identified this cipher as the cipher of the Dieci's 1510 letters to
Machiavelli.

**Source.** PRIMARY · BNCF Teca images, `idr=BNCF0003858589` to `8607`. They are already cached in our repo
at `../../2911/cache/keysheets/`. The description is in `../../2911/keysheet-check.md` (fetched 2026-11-16),
which gives shapes and layout but no values. I did not open the images. Item 2911 asks its main thread and
readers to stay away from them.

**How it is said to work** (keysheet-check.md):
- a homophonic alphabet of 22 letters;
- a syllable table, one row per consonant and five vowels across, where the syllable signs are letters,
  doubled letters, signs with a **superscript o**, and invented marks;
- "Nulle" (nulls), "Duple" (doubled consonants) and "Dictioni" (about 28 word signs);
- names given two-digit numbers.

**How close it looks to ours.** Same office and same destination, three to thirteen years earlier, but a
different design. Its superscript is one small `o` that makes a separate syllable sign. There is no system
of figures 1-5 over a consonant, and there are many dotted and boxed invented marks that our guide does not
have. It is a weaker match than the Pandolfini table. I made no transcription and no TSV, because a
transcription would mean opening key material that item 2911 keeps blind.

## 3. Descriptions of the family (lead 3)

All from S. Tomokiyo, Cryptiana (SECONDARY: an independent researcher's site; he also publishes in
Cryptologia), fetched 2026-11-18:
- `https://cryptiana.web.fc2.com/code/castiglione.htm`: a cipher of the papal nuncio Castiglione, 1527, with
  "vowel indicators". Syllable signs are a base plus dots, strokes or superscript figures, and the same mark
  tends to give the same vowel. Separate indicators mark doubles. Base + superscript 10, 11, 12 gives words
  starting with that consonant. The key is shown only as an image (not saved). Tomokiyo lists no example of
  this method before 1527.
- `https://cryptiana.web.fc2.com/code/worcester.htm`: Silvestro Gigli, bishop of Worcester, 1526-29. Base
  letter + numeral superscript, with **no** regular vowel pattern. Other superscripts give names and words.
  Tomokiyo says superscripts are "often seen in Venetian or Milanese ciphers".
- `https://cryptiana.web.fc2.com/code/venetian.htm`: Venetian ciphers of 1519-1587. Only the late "Zifra
  Granda" (about 1578-87) ties figures to vowels (digits ending 1-5 = -a, -e, -i, -o, -u, an order unlike
  Dudout's 1514 order). It cites Meister (1902) p. 21 on where the superscript came from, without a date.

None of these is Florentine or as early as 1513. The Pandolfini key is the only description of the exact
mechanism, figure over consonant = following vowel, found in this family and decade.

## Not found

- **A period key sheet for Acciaiuoli 1513 or Pandolfini 1514.** Dudout's NOTES say "no key sheet of this
  system is known; the pairs are the key material" (known-keys: n/a). Bourdeau's entry for no. 2351
  (`https://cyphersolver.com/solve/2351.html`) lists no published table. PR 531 says the leaf is bare and
  Desjardins-Canestrini vol. II prints only Acciaiuoli's dispatch of 26 Sept 1513.
- **Desjardins-Canestrini vol. II** (our OCR). It prints deciphered texts with footnotes such as "Presque
  toute cette correspondance est en chiffres" (almost all of this correspondence is in cipher; line 29129,
  Pandolfini, Novalese, March 1513/14) and "Chiffre non déchiffré" (cipher not deciphered; line 31060). It
  prints no key and no description of signs.
- **Tomokiyo.** No Florentine page for 1490-1530. `crypto.htm` lists Florence only for Guicciardini, about
  1590. `italian.htm` is a stub (not fetched).
- **DECODE.** The Florentine records cited in Bourdeau's repo
  (`research/venice_milan_decode/hits.txt`; `research/medici_bia/README.md`) are:
  - Dieci di Balìa Responsive R3753-R3789, early filze 2-22 with a placeholder date of 1401, so
    fifteenth-century;
  - the grand-ducal key volumes R5687-R7459, seventeenth and eighteenth century.

  Neither is near 1513. I did not query DECODE's own interface, which needs JavaScript.
- **Meister**, *Die Anfänge der modernen diplomatischen Geheimschrift* (1902) and *Die Geheimschrift im
  Dienste der päpstlichen Kurie* (1906): no online text located in this run. Not searched beyond Tomokiyo's
  citation.
- **Marco Vito**, "A Florentine 'polyalphabetic' cipher in the 15th century" (dspace.ut.ee, 2025). This is
  the time of Lorenzo il Magnifico, about 1486-91. Not fetched.

## Unverified claims

- That Acciaiuoli in 1513 used the same cipher as Pandolfini in 1514-15. It is plausible because of the
  joint 1514 letters and the shared filza, but no source says so.
- That the 1514 pairs 345/346, 340/341 and 342/343 are cipher with a decipherment of the time. This is
  Dudout's statement and we have not seen the pages.
- The shape matches in the TSV come from written descriptions on both sides, not from images side by side.
- `^~` (ours) = `^2` (theirs): my conjecture, untested.
- Guicciardini's letters to Roberto Acciaiuoli with cipher passages (nos. 3155, 3247, 3352 in the SNS
  edition; `https://edizioni.sns.it/wp-content/uploads/2025/07/IntroGuicciardiniXIII.pdf`, SCHOLARLY,
  seen only as a search snippet). These belong to Acciaiuoli's later French embassy of the 1520s. Whether
  that cipher, or the editor's reconstruction of it, is related is unknown.
