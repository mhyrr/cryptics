+++
title = "Charles V and Philip II: unsolved and unread Spanish cipher letters, 1521–1579"
slug = "charles-v-unsolved-cipher-letters"
kind = "cipher"
era = "1521–1579"
origin = "Habsburg Spain and its embassies (Rome, Venice, Paris)"
language = "Spanish"
status = "partial"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b9000773m"
tags = ["nomenclator", "letters", "diplomatic", "spanish", "habsburg", "cryptiana", "BnF", "BRAH", "DECODE", "key-known-text-unread"]

[scores]
mystery = 2
material = 5
solvable = 5
compute = 4
verifiable = 5
crowding = 4
+++

# Charles V and Philip II: unsolved and unread Spanish cipher letters, 1521–1579

## What it is
Habsburg diplomatic cipher letters on Satoshi Tomokiyo's Cryptiana list, from the reign of Charles V into the early years of Philip II. They are grouped here because they share one cryptographic tradition. That tradition is a Spanish secretariat cipher: a symbol or letter alphabet combined with a large nomenclator of three-letter code words (for example *tac*, *byo*, *gao*, *sof*). It descends from the ciphers of the Catholic Monarchs. Almost all of these items are now in one of two states: solved, or "key identified, text not yet read." Only one has no key at all.

| Item | Shelfmark | Status (Sept 2026) |
|---|---|---|
| Charles V's letter of 26 Dec [1521?], partly in cipher, recipient unnamed | BnF Clairambault 322, ff. 105–106 | **Unsolved.** No key has been identified. It uses three-letter code words such as *mul*, *dem*, *hum* |
| Juan Manuel (imperial ambassador in Rome) to Charles V, Mar–Jun 1522 | BRAH 9/23–9/24; DECODE records R9499–R9529 (most of them) | **Key identified** (Tomokiyo, Sept 2025) |
| Alonso Sánchez (imperial ambassador in Venice) to Charles V, 1522 | BRAH 9/23; DECODE R9509 (= R9596), R9522 (= R9608), R9593–R9601 | **Key identified** (Tomokiyo, Sept 2025) |
| Letters of 1551 | Simancas, Estado, leg. 1381, docs 180 and 143 (24 Aug 1551) | **Solved** (2023). George Lasry solved them with his algorithm for syllable ciphers, and Carlos Köpte independently. Doc. 143's plaintext is French, in the Granvelle–Saint-Mauris cipher. Doc. 180 contains copies of letters to Doria, to "Ferando" and to ambassador Figueroa |
| Philip II and Antonio Pérez to Juan de Vargas Mexía, ambassador in Paris, 1577–79 | BnF Espagnol 132 (formerly Regius 9999 / Mazarin 498) | **Keys identified** (Tomokiyo, 2020). Four ciphers: one cracked by him, three matched to keys Devos (1950) printed from Simancas. **Being read** in this repository (`puzzles/vargas-mexia-es132/`, from Oct 2026): f. 198–199 (Pérez, 15 April 1579) has a provisional full reading in Cipher 4 |

Solved siblings, named for calibration (not separate entries):
- Juan Pérez to Charles V, 24 Sept 1527. Lasry solved it in 2023; it uses the same cipher as Juan Manuel's, which is Olga Kolosova's key Ko.1.
- A report to Charles V (BnF fr. 3022, f. 16). Lasry solved it in April 2026, with most code groups still open; Bourdeau improved the key.
- Del Vasto (Gasto) to Charles V, 1527 (BnF fr. 3022 ff. 26 and 40). Lasry solved it in 2026.
- Suárez de Figueroa to Charles V, 1529. Tomokiyo solved it in 2018.
- Charles V to Saint-Mauris, 1547 (Nancy). Pierrot, Gaudry, Zimmermann and Desenclos solved it in 2022.
- Idiáquez and Mendoza to Philip II, 1577 (Simancas Estado leg. 1386, 1). Köpte solved it in 2023.

## What is unsolved
Two different things are open here, and they should not be confused.

1. **A true cryptanalytic gap.** Charles V's 26 December [1521?] letter in Clairambault 322 has no identified key.
2. **Keyed but unread texts.** For Juan Manuel, Alonso Sánchez and Vargas Mexía, "key identified" means one of two things. Either a substitution alphabet and part of the code-word nomenclator have been reconstructed, by aligning cipher letters against contemporary decipherments filed with them (Manuel, Sánchez). Or each letter's cipher has been matched to a known key (es. 132).

What "key identified" leaves open:
- **The nomenclator is not complete.** Tomokiyo's Juan Manuel and Sánchez tables carry "?" marks, and his sample readings leave groups bracketed as unknown. Codewords that do not occur in the deciphered siblings have no value.
- **Full texts have not been read.** Tomokiyo published only the opening line of each BRAH letter, as a check that the cipher was the same. Two Juan Manuel letters have no contemporary decipherment at all: R9501 (7 March 1522) and R9515 (24 April 1522). R9501 is probably calendared in the *Calendar of State Papers, Spain*. For es.132, Tomokiyo has only a preliminary reading of f. 3. He has also picked out words in f. 198: "Escovedo", "mi inocencia", "falso testimonio". Nobody has published a full decipherment of the volume.
- **Many of these letters are already readable.** Most of the BRAH letters carry their own sixteenth-century decipherment (DECODE shows its first page), and many are calendared in English in the *Calendar of State Papers, Spain*, vol. 2. For those, the cipher adds nothing new. The residue that is actually unread is the two uncatalogued Juan Manuel letters, any Sánchez letters without plaintext, the es. 132 letters, and the Clairambault letter.

## What survives
All of it, in archives, mostly digitized:
- Clairambault 322 is on Gallica.
- The BRAH letters are imaged in DECODE.
- The Simancas letters are on PARES.
- BnF Espagnol 132 is on Gallica (ark:/12148/btv1b10032556x).
- The keys: Devos (1950) prints the Simancas keys that match es. 132 Ciphers 1 and 4. Tomokiyo's articles give the reconstructed Juan Manuel and Sánchez tables and the es. 132 Cipher 2 he cracked.

## Prior attempts and current consensus
- **Tomokiyo** (2011 onward) collected these items.
- In 2020 he identified all four es. 132 keys.
- In September 2025 he rebuilt the Manuel and Sánchez ciphers from DECODE's attached decipherments.
- **Lasry and Köpte** solved the 1551 Simancas pair in 2023.
- **Kolosova (2017)** reconstructed the Spanish key family (Ko.1) from Spanish archival material.
- **Bourdeau** (Sept 2026) worked nearby items: Adrian of Utrecht to Charles V, 30 December 1521, decoded and corrected from a printed decipherment. None of the items in this entry appear in his solved list.

Consensus: this is a cryptologically mature family. The open work is mostly applying known keys and editing the results, with one exception: Clairambault 322.

Newcomers should read Tomokiyo, "Ciphers during the Reign of Emperor Charles V"; "Correspondence in Cipher of Imperial Ambassadors Alonso Sanchez and Juan Manuel (1522)"; and "Finding the Keys to Philip II's Cipher Letters to Juan de Vargas Mexia".

## What a solution would have to do
- **Clairambault 322.** Produce continuous Spanish from a single key. The code-word values must be shown to hold in other letters of the same key; a context guess is not enough. A good first test is whether the Juan Manuel/Ko.1 family or another key from 1521–22 reads it, since it shares the three-letter-code design.
- **Keyed letters.** Give a full reading of R9501 and R9515 and the es. 132 letters, with the unknown codewords listed. Where a contemporary decipherment or a calendared summary exists, the reading should agree with it. This is the mechanical check that a keyed reading must pass.
- **es. 132 f. 198.** Any claim about the Escobedo murder must come from a full, key-consistent decipherment of the letter, not from selected words.

## Why the scores
- **mystery 2.** Diplomatic dispatches. The es. 132 letters could bear on the Antonio Pérez and Escobedo affair, which is a known historical question. That argues for 3, but the cipher is no longer the mystery there: the reading is.
- **material 5.** Whole originals survive and are digitized (Gallica, DECODE, PARES). Keys and partial tables are published.
- **solvable 5.** These are state nomenclators, and several have keys already identified.
- **compute 4.** Applying a key to many letters, aligning against contemporary decipherments, and inferring missing codewords across a corpus are computational tasks, and the data is ready. Two things keep it from 5. The Clairambault letter is short and code-heavy, which is code rather than cipher. And the es. 132 transcription is a handwriting problem.
- **verifiable 5.** Decipherments and calendared plaintexts exist to check against.
- **crowding 4.** A handful of specialists (Tomokiyo, Lasry, Köpte, Kolosova). Nobody has published a full reading of the keyed letters.

## Sources
- PRIMARY — BnF Clairambault 322 (Gallica). https://gallica.bnf.fr/ark:/12148/btv1b9000773m
- PRIMARY — BnF Espagnol 132 (Gallica). https://gallica.bnf.fr/ark:/12148/btv1b10032556x
- PRIMARY — PARES, Simancas Estado leg. 1381 doc. 180. http://pares.mcu.es/ParesBusquedas20/catalogo/description/3572428
- SECONDARY — S. Tomokiyo, Cryptiana, "Unsolved Historical Ciphers" (Spanish section; status notes up to Sept 2026). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Ciphers during the Reign of Emperor Charles V" (Clairambault 322, 1521?; 1527 items). https://cryptiana.web.fc2.com/code/spanish2.htm
- SECONDARY — S. Tomokiyo, "Correspondence in Cipher of Imperial Ambassadors Alonso Sanchez and Juan Manuel (1522)" (reconstructed tables; R9501 and R9515 have no decipherment in DECODE; opening lines only). https://cryptiana.web.fc2.com/code/AlonsoSanchez.htm
- SECONDARY — S. Tomokiyo, "Finding the Keys to Philip II's Cipher Letters to Juan de Vargas Mexia" (four ciphers; f. 198 words; Rubino 2012). https://cryptiana.web.fc2.com/code/spanish3D.htm
- SECONDARY — *Calendar of State Papers, Spain*, vol. 2 (British History Online), Juan Manuel and Sánchez letters "Autograph in cipher. Contemporary deciphering." https://www.british-history.ac.uk/cal-state-papers/spain/vol2/pp386-400
- CLAIMANT — Daniel Bourdeau, Unsolved Historical Ciphers working notes (Adrian of Utrecht 1521; no entry for the items above as of late Sept 2026). https://dbourdeau.github.io/cyphersolver/

## Unverified claims
- That Charles V's Clairambault 322 letter dates from 1521. Tomokiyo queries the year himself.
- Whether Lasry's 1551 solutions were published beyond Tomokiyo's report. They were not fetched.
- Rubino (2012) on es. 132 f. 198 and the Escobedo murder. Known only through Tomokiyo's citation.
- That es. 132 has no full published decipherment as of 2026. Tomokiyo says the keys "will allow historians" to read it, and no edition was found, but no search of the Spanish historiography was made.
- How many of the Sánchez letters lack any contemporary decipherment. Tomokiyo's list does not mark this per letter.
