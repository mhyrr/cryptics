+++
title = "Papal ciphers in the Vatican archives, 16th–18th centuries, and the Vatican Challenges"
slug = "papal-ciphers-vatican-challenges"
kind = "cipher"
era = "c. 1520–1767"
origin = "Papal Secretariat of State and nunciatures (Rome, Madrid, Paris, Brussels, Lisbon)"
language = "Italian"
status = "partial"
confidence = "medium"
digitized = "https://www.tandfonline.com/doi/full/10.1080/01611194.2020.1755915"
tags = ["papal", "Vatican", "nomenclator", "homophonic", "polyphonic", "digit-stream", "DECRYPT", "DECODE", "challenge-cipher", "hill-climbing", "recently-fallen", "group-entry"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 5
crowding = 3
+++

# Papal ciphers in the Vatican archives, 16th–18th centuries, and the Vatican Challenges

## What it is
This entry covers the papal Secretariat of State's enciphered correspondence with its nuncios, held in the Archivio Apostolico Vaticano (Segreteria di Stato, nunciature series) and imaged and transcribed in DECODE. The ciphers are Italian numerical systems: fixed- and variable-length homophonic ciphers, polyphonic ciphers (one figure standing for two letters), and nomenclators, often written as continuous digit streams.

In 2019, as part of the DECRYPT project, George Lasry, Beáta Megyesi and Nils Kopal systematically clustered and attacked hundreds of these letters. They recovered 16 of the 21 keys in use ("Deciphering papal ciphers from the 16th to the 18th Century," *Cryptologia*, online 2020, vol. 45). The paper also gives algorithms for clustering ciphertexts by key and for solving fixed-length homophonic, variable-length homophonic and polyphonic ciphers. Its historical finding is that the sophistication of 16th-century papal ciphers was lost in the 17th, when simpler ciphers were used.

Ciphertexts the project could not solve were released as public challenges on MysteryTwister (MTC3). All five are now solved:
- **Vatican Challenge Parts 1–2 (2018):** nuncio letters of 1628 (Pallotto) and 14 March 1625 (France). Solved independently by Thomas Bosbach and Norbert Biermann, and third by Tomokiyo, ciphertext-only for Part 2 and with a crib for Part 1. A contemporary decipherment was also already available.
- **Part 3:** Brussels, 9 October 1721, one- to four-digit groups. Solved by Lasry and Paolo Bonavoglia (HistoCrypt 2022), who recovered "most of the key and of the plaintext".
- **Part 4:** Bishop of Senigallia, March 1536. Solved August 2019 by Thomas Bosbach, who found a matching printed plaintext.
- **Part 5:** Cardinal Alessandro Farnese to Giovanni Poggio, nuncio in Spain, April 1542 (AAV Segr. Stato Spagna 1A ff. 70r–73v, DECODE R92). Solved by Simon Klee, published 16 Sept 2026 and accepted by MTC3. The key is a mixed one- and two-digit monoalphabetic cipher with dotted syllable and title codes. Bourdeau independently reviewed it and withdrew his own diagnosis.

Earlier related solves:
- the letter to Cardinal Schiner (1520), solved by Nicollier, Jacquemet and Evéquoz;
- three Vatican ciphers of 1593 (Tomokiyo, *Cryptologia* 2018);
- a 1573 cipher (Leighton, 1969).

## What is unsolved
The keys the 2020 survey did not recover (5 of 21 by its count), and the code groups left open in letters read with recovered keys. Tomokiyo's heading for the survey is "Many Solved", not "Solved". Two named residues:
- **R91** (Spagna IA-1), the companion of Vatican Part 5 in another key, which Bourdeau lists as still open.
- **The 1758–60 Acciaiuoli letters.** Lasry's 2020 key gave a letter stream with "all 107 code words open". In September 2026 Bourdeau fixed 25 of them from contemporarily deciphered leaves; about 80 rare codes remain.

The DECODE records marked "partially decrypted" are being completed piecemeal. In September 2026 Bourdeau extended Lasry's keys to the Alessandrino (1567–69), Dandini (1580), Sauli/Riario (1579–81) and Lucini (1767) letters.

## What survives
- Hundreds of letters in the AAV, many with contemporary decipherments or cleartext copies. They are imaged and transcribed in DECODE, often with Lasry's reconstructed keys attached.
- The challenge texts are on MTC3.
- The survey paper and the HistoCrypt paper are published; the HistoCrypt paper is open access.

## Prior attempts and current consensus
**For the challenges:** solved, with independent confirmations for Parts 1–2 and 5, and a printed plaintext for Part 4.

**For the corpus:** a large share is read and the methods are published. The field has not documented which five keys failed or why. The Part 5 history is instructive. A text that resisted "sophisticated computerized algorithms" in 2019 fell in 2026 once the key design was correctly diagnosed: monoalphabetic with codes, not the expected Elio-family syllabary. So the remaining failures may be diagnosis failures, not hard ciphers.

Read first: Lasry, Megyesi and Kopal (2020); Lasry and Bonavoglia (2022); Klee's Part 5 write-up; Tomokiyo's vatican.htm.

## What a solution would have to do
- For each remaining key: a reconstruction that reads every letter assigned to it continuously in period Italian, consistent with the clustering, and with the nunciature's known business and dates.
- Where contemporary decipherments or cleartext copies exist, the reading must match them. Bosbach's Part 4 match and the Acciaiuoli glosses are the model.
- A reading must not need a different parsing rule for different parts of one stream.
- Code-group identifications should be confirmed on more than one occurrence or against a glossed leaf.

## Why the scores
This is scored as the corpus stands, partly solved. The solved challenges serve as calibration points: before their solves they would have scored the same on compute and verifiable.
- **mystery 2:** nunciature dispatches are a rich source for Counter-Reformation and 18th-century diplomacy, but the unread residue is a scattering of letters and code groups, not a known historical question.
- **material 4:** a large archival corpus, imaged and transcribed in DECODE (login required) with published keys. Not 5, because transcription errors are documented: Bourdeau corrected 151 digits in Part 5.
- **solvable 5:** state ciphers with determinate plaintext. Most keys in the same series have been recovered.
- **compute 4:** the series is the canonical case for the axis: hill-climbing and clustering recovered 16 keys in about six weeks, and every challenge fell to computation plus diagnosis. But the unread residue is the part that resisted that attack: the five unrecovered keys, R91 and the Acciaiuoli code groups. Not 5, because the next step is diagnosis (which system, which nulls, which archive key), not more search.
- **verifiable 5:** continuous Italian, often checkable against contemporary decipherments or printed nunciature editions.
- **crowding 3:** the DECRYPT team, Bosbach, Biermann, Tomokiyo, Klee and Bourdeau have all worked the series, and the obvious algorithms have been run. The five failed keys survived a serious, well-tooled attempt.

## Sources
- SCHOLARLY — George Lasry, Beáta Megyesi, Nils Kopal, "Deciphering papal ciphers from the 16th to the 18th Century," *Cryptologia* 45 (published online 23 June 2020). https://www.tandfonline.com/doi/full/10.1080/01611194.2020.1755915
- SCHOLARLY — George Lasry, Paolo Bonavoglia, "Deciphering a Short Papal Cipher from 1721," HistoCrypt 2022 (abstract: several ciphertexts remained unsolved despite sophisticated algorithms and were offered as public challenges in 2019). https://ecp.ep.liu.se/index.php/histocrypt/article/view/401
- SCHOLARLY — Satoshi Tomokiyo, on three Vatican ciphers of 1593, *Cryptologia* (2018) (cited via Cryptiana, not opened). https://www.tandfonline.com/doi/full/10.1080/01611194.2018.1503207
- SECONDARY — Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," section "Italian (Vatican)" (statuses of the survey and Challenges 1–5). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, "Ciphertext-only Attack on 'Vatican Challenge' Ciphers (1625, 1628)." https://cryptiana.web.fc2.com/code/vatican.htm
- CLAIMANT — Simon Klee, "The Farnese letter" (Vatican Challenge Part 5 solution, Sept 2026). https://simonklee.dk/farnese-letter
- CLAIMANT — Daniel Bourdeau, cyphersolver README and vatican5 notes (review of Klee; R91 open; extensions of Lasry's keys to Alessandrino, Dandini, Sauli, Acciaiuoli and Lucini records). https://github.com/dbourdeau/cyphersolver
- SECONDARY — MysteryTwister, Vatican Challenge Parts 3–5. https://www.mysterytwisterc3.org/en/challenges/level-x

## Unverified claims
- "16 of 21 keys" is Tomokiyo's summary of the *Cryptologia* paper. The paper itself was not opened (publisher returned 403), and which five keys failed, and how many letters they cover, is not recorded here.
- Whether Klee's Part 5 solution has been formally published beyond his site and MTC3's acceptance.
- Whether any of the five unrecovered keys has since been solved by Lasry or others. The September 2026 Cryptiana notice warns that solutions are outpacing the list.
- Tomokiyo reports the survey's work period (24 April – 9 June 2019, p. 492); not checked.
