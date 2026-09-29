+++
title = "Mary Stuart's cipher letters, 1578–1584 (solved 2023) — calibration case"
slug = "mary-stuart-cipher-letters"
kind = "cipher"
era = "1578–1584"
origin = "England (Mary, Queen of Scots, in captivity) to the French embassy in London"
language = "French"
status = "solved"
confidence = "high"
digitized = "https://www.tandfonline.com/doi/full/10.1080/01611194.2022.2160677"
tags = ["calibration", "solved", "homophonic", "nomenclator", "letters", "archival-discovery", "hill-climbing", "DECRYPT"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 5
+++

# Mary Stuart's cipher letters, 1578–1584 (solved 2023) — calibration case

## What it is
Fifty-seven enciphered letters that George Lasry, Norbert Biermann and Satoshi Tomokiyo found in the Bibliothèque nationale de France's online collections. The BnF had catalogued them as early-sixteenth-century and concerned with Italian affairs. They are in French, written by Mary, Queen of Scots, during her English captivity, mostly to Michel de Castelnau, the French ambassador in London. The cipher is homophonic (several symbols per letter) with nomenclator symbols for frequent words and people; an elongated "H", for instance, stands for her keeper, the Earl of Shrewsbury. Deciphered, they come to about 50,000 words, and some 50 of the letters were previously unknown to historians. They cover her health and captivity, negotiations with Elizabeth I, her distrust of Walsingham, and her son James.

## What is unsolved
Nothing in the cipher. The entry is here as a calibration case. It is the closest living analogue to Copiale for the shape this catalog hunts: a long body of personal letters in a period homophonic nomenclator, misfiled and never attacked.

## What survives
The originals at the BnF, digitized (which is how they were found). Copies of seven letters survive in plaintext in Walsingham's papers in the British Library. The decipherment and key reconstruction are published in *Cryptologia* (2023), open access.

## Prior attempts and current consensus
None before the three found them: the catalogue error hid them. They were identified in 2022 while systematically searching digitized archives for ciphers. A computer hill-climb over homophonic keys recovered about 30% of the text; the remaining 70% was worked by hand, "somewhat analogous to solving a large crossword puzzle," with nomenclator symbols fixed from context. The team recognised the letters when "Walsingham" came out. Verification: seven decrypted letters match plaintext copies in the British Library, and the rest is consistent with feminine grammatical forms and the facts of her captivity. Consensus: solved, and a major addition to the Mary Stuart corpus.

## What a solution would have to do
Met: one reconstructed key reads all the letters continuously in French. Decrypts coincide with independently surviving plaintext copies (the strongest possible check). The recovered content fits the documented chronology of 1578–1584.

## Why the scores
Scored as of 2021, before discovery.
- mystery 1 today. In 2021 it would have been 4: unknown letters of a major historical figure, though nobody knew they were there.
- material 5: 57 letters, clearly written, digitized.
- solvable 5: a period diplomatic cipher system, used consistently.
- compute 5: tens of thousands of symbols in a homophonic nomenclator is exactly what hill-climbing with a language model is for. The only non-computational step was noticing the documents.
- verifiable 5: continuous French plaintext, plus matching copies in another archive.
- crowding 5: untouched; hidden by a catalogue error.
- compute mode (retrospective): ENUMERATE (homophonic hill-climb) · verifier MECHANICAL · space SAMPLABLE · signal YES · fit HIGH.
- Calibration point: the rubric scores the text, but the binding constraint was finding it. Mis-catalogued ciphers in digitized national libraries are a source of Copiale-shaped targets that the catalog should search for directly (DECODE, BnF Gallica, the Vatican's digitized fonds), not wait to hear about.

## Sources
- SCHOLARLY — George Lasry, Norbert Biermann and Satoshi Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578–1584," *Cryptologia* 47 (2) (2023). https://www.tandfonline.com/doi/full/10.1080/01611194.2022.2160677
- SECONDARY — ScienceDaily, "Codebreakers crack secrets of Mary Queen of Scots' lost letters," 7 Feb 2023 (the BnF mis-cataloguing, ~50,000 words, ~50 new letters, verification against Walsingham's papers). https://www.sciencedaily.com/releases/2023/02/230207191551.htm
- POPULAR — *Smithsonian Magazine*, "Code Breakers Discover—and Decipher—Long-Lost Letters by Mary, Queen of Scots" (homophonic system, the Shrewsbury symbol, 30% automated / 70% manual, seven known letters matched, Lasry quotes). https://www.smithsonianmag.com/history/codebreakers-discoverand-decipherlong-lost-letters-by-mary-queen-of-scots-180981613/

## Unverified claims
- The number of distinct cipher symbols and the size of the nomenclator; in the paper, not read here.
- The BnF shelfmarks of the letters.
- The exact split between "57 letters deciphered" and "about 50 previously unknown"; the reports give both figures without reconciling them.
