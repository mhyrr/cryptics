+++
title = "Ferdinand the Catholic's undeciphered cipher letters, 1497–1504"
slug = "ferdinand-catholic-cipher-letters"
kind = "cipher"
era = "1497–1504"
origin = "Crown of Aragon / Castile (Ferdinand and Isabella's secretariat and its ambassadors in Italy)"
language = "Spanish (one sibling in Italian)"
status = "partial"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b52503046q/"
tags = ["nomenclator", "letters", "diplomatic", "spanish", "catholic-monarchs", "cryptiana", "BnF", "code-groups"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 4
crowding = 3
+++

# Ferdinand the Catholic's undeciphered cipher letters, 1497–1504

## What it is
A group of diplomatic cipher letters from the court of Ferdinand and Isabella and their ambassadors and commanders in Italy. Satoshi Tomokiyo's Cryptiana list gives them as two items, plus two that have since been solved:

| Item | Shelfmark | Status (as of Sept 2026) |
|---|---|---|
| Postscript to Ferdinand's letter of 31 Aug 1498 to Garcilaso de la Vega, his ambassador in Rome | Reproduced in Parisi (2004), p. 115; the archive holding the original is not verified here | **Unsolved.** The body was deciphered by Parisi. The last ten lines are in a different cipher, and he left them undeciphered |
| Letter of 8 Jan 1497 (unaddressed leaf) | BnF Espagnol 318, f. 122, no. 95 | **Approximately solved.** George Lasry gave an alphabet in 2022. Daniel Bourdeau's labelled segmentation (2026) reads about two thirds of it, which concerns the French |
| Viceroy of Sicily to Ferdinand, 27 Apr 1503 | BnF Espagnol 318, ff. 120–121, no. 94 | **Unsolved.** The cipher family is identified, but the key is not available |
| Lorenzo Suárez to Ferdinand and Isabella, Venice, 24 Feb 1504 | BnF Espagnol 318, f. 118, no. 93 | **Unsolved.** Same situation as no. 94 |
| Federico of Naples to the Catholic Monarchs, 11 Jan 1497 (Italian) | BnF Espagnol 318, ff. 5–6, no. 5 | **Solved in print.** Parisi printed the full text in 2020 |
| Gonzalo Fernández de Córdoba to Lorenzo Suárez, 17 Aug 1500 | BnF Espagnol 318, f. 116, no. 92 | **Partly read** with the printed *Cifra general de los Reyes Católicos* |

Solved siblings kept for calibration (not separate entries):
- "A Spanish letter (1504?)", Simancas PTR, LEG 54, DOC 13. Tomokiyo found in 2023 that it is actually an English cipher (John Stile, 21 March 1514) deciphered in the nineteenth century. The repeated patterns he had noted were "the", "of" and "your".
- Catherine of Aragon's letter to Ferdinand (1509). Tomokiyo posted it to MysteryTwister C3 in 2018, and Victor and Thomas Bosbach solved it at once.

## What is unsolved
Three short texts remain. The first is the ten-line postscript of 1498, in a cipher different from the body. The other two are letters nos. 93 and 94, whose key family is known but whose key is not in hand.

Both of those letters are written in a homophonic symbol alphabet mixed with three-letter consonant-vowel-consonant code groups. Bourdeau reports that their code-initial letters rule out both keys in print and fall within the range of the *Gran cifra* of 1501–04. That cipher survives only in Gustav Bergenroth's nineteenth-century reconstruction, BNE MSS 20.211/52, which is not served online. No. 95 has a working alphabet, but no clean published text.

## What survives
- Espagnol 318 is digitized on Gallica, so the letters can be read from the images.
- The 1498 letter is reproduced as an image in Parisi (2004), *Pedralbes* 24, which is open access. The postscript is on p. 115. This repository could not fetch the PDF (HTTP 403).
- Bourdeau has transcribed no. 95 (963 signs) and f. 118r (about 1,016 signs) for his own tests.
- The printed keys are Galende Díaz (1994), Appendix 1 (*Cifra general*), and Parisi's Ciphers No. 1 and No. 2.

## Prior attempts and current consensus
- **Parisi (2004)** deciphered the 1495–98 Ferdinand–ambassador correspondence (Naples and Rome) from ten cryptograms and left the 1498 postscript open.
- **Tomokiyo** listed the Espagnol 318 letters in 2019 and the postscript in January 2019.
- **Lasry (2022)** produced the approximate key for no. 95.
- **Bourdeau (17 Sept 2026)** surveyed all five Espagnol 318 letters. He proved no. 92's key against glosses written between the lines, extended no. 95, and found that nos. 93 and 94 are nomenclator problems that need the *Gran cifra*. He tested and rejected the alternative that their code groups are runs of letter-shaped signs.

No one claims a reading of the 1498 postscript.

Newcomers should read Parisi (2004); Tomokiyo's "Spanish Ciphers during the Reign of Ferdinand and Isabella"; and Bourdeau's Espagnol 318 write-up.

## What a solution would have to do
- **1498 postscript.** Give continuous Spanish (or Catalan) from one key across all ten lines. The reading must fit the context of the letter's body, Ferdinand's Rome business in August 1498. If the code-group values come from a printed or archival key rather than being guessed, the reading should be checkable against that key.
- **Nos. 93 and 94.** Apply a key (the *Gran cifra* from BNE 20.211/52, or one rebuilt from deciphered siblings of 1501–04) that also reads at least one independently deciphered letter in the same system. The output must be Spanish consistent with the 1503 Sicilian and 1504 Venetian situations. Guessing CVC code values from context alone does not count.
- **No. 95.** A full text with its unread third accounted for, using the same alphabet throughout.

## Why the scores
- **mystery 2.** These are routine Catholic Monarchs' dispatches, of interest to specialists. No known historical question hangs on them.
- **material 4.** Espagnol 318 is fully digitized. The 1498 postscript survives only as a printed facsimile at second hand here, and it is short.
- **solvable 5.** These are state-issued nomenclators, used determinately.
- **compute 4.** The homophonic alphabet part can be hill-climbed, and Bourdeau's annealing tests show what can be done. The CVC code groups are code, not cipher: with only a few messages, their values come from a key or from sibling decipherments, not from statistics. The ten-line postscript is short. This could have been 3 if the code fraction is high.
- **verifiable 4.** Alphabet portions check mechanically. Code-group readings without the key remain partly conjectural, which is why this is not 5.
- **crowding 3.** Parisi, Tomokiyo, Lasry and Bourdeau have all worked this small group. The obvious steps (known keys, alphabet recovery) are done.

## Sources
- PRIMARY — BnF Espagnol 318 (Gallica). https://gallica.bnf.fr/ark:/12148/btv1b52503046q/
- SCHOLARLY — Ivan Parisi, "La correspondencia cifrada entre el rey Fernando el Católico y el embajador Joan Escrivà de Romaní i Ram," *Pedralbes* 24 (2004), 55–116 (the 1498 letter's postscript is on p. 115). https://www.raco.cat/index.php/Pedralbes/article/viewFile/101764/170134
- SCHOLARLY — Ivan Parisi, "Un cifrario in prestito per una lettera segretissima di Federico d'Aragona re di Napoli ai Re Cattolici nel BnF, Espagnol 318," *Studi di storia medioevale e di diplomatica* n.s. IV (2020), 157–177 (as cited by Cryptiana; not fetched).
- SECONDARY — S. Tomokiyo, Cryptiana, "Unsolved Historical Ciphers" (Spanish section). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, Cryptiana, "Spanish Ciphers during the Reign of Ferdinand and Isabella" (Parisi's ciphers; the 1498 postscript "left undeciphered by Parisi"). https://cryptiana.web.fc2.com/code/spanish.htm
- SECONDARY — S. Tomokiyo, Cryptiana, "George Lasry's Solutions of Unsolved Ciphers" (no. 95, approximate). https://cryptiana.web.fc2.com/code/GL.htm
- CLAIMANT — Daniel Bourdeau, "BnF Espagnol 318: five ciphered letters, 1497–1504" (17 Sept 2026). https://dbourdeau.github.io/cyphersolver/esp318.html

## Unverified claims
- The archival location of the original 1498 letter to Garcilaso de la Vega. It is probably in the Real Academia de la Historia (Salazar collection), like the rest of Parisi's corpus, but this was not confirmed because the PDF could not be fetched.
- That the postscript is exactly ten lines and in a cipher different from Parisi's Cipher No. 2. This is Tomokiyo's description of Parisi's plate, not checked here.
- Bourdeau's claims (the *Gran cifra* attribution, the reading of two thirds of no. 95) are a solver's own write-up and have not been independently reviewed.
- Whether Terrateig's or other printed editions already contain plaintexts of nos. 93 and 94. Nobody reports having checked.
