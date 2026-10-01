+++
title = "Ferdinand III and Habsburg ciphers of the Thirty Years' War (Plzeň 1634, DECODE R1579, R1887, R2179)"
slug = "ferdinand-iii-habsburg-ciphers"
kind = "cipher"
era = "1627–1644 (solved siblings 1626–1758)"
origin = "Habsburg court and envoys: Vienna, Brussels, Bohemia, Italy"
language = "Latin, German, Italian"
status = "partial"
confidence = "medium"
digitized = "https://de-crypt.org/decrypt-web/RecordsView/1887"
tags = ["nomenclator", "code", "digit-stream", "Habsburg", "Thirty-Years-War", "DECODE", "Cryptiana", "letters", "recently-fallen", "group-entry"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 4
crowding = 3
+++

# Ferdinand III and Habsburg ciphers of the Thirty Years' War

## What it is
This entry groups the open items in the "German" section of Satoshi Tomokiyo's Cryptiana list. They are imperial cipher letters, most of them involving Ferdinand III (King of Hungary and Bohemia from 1625–27, Emperor 1637–57). Most survive in Austrian, Czech and Belgian archives and are imaged in the DECODE database (DECRYPT project). The language is usually Latin, Italian or German.

Open, or open until September 2026:
1. **King of Hungary and Bohemia to Trauttmansdorff, 13 November 1634.** SOA Plzeň, Klášter office (Monastery office), Trauttmansdorff family archive, carton 6, inv. no. 68. Jakub Mírka (2012) reports it undeciphered. It is the only cipher letter between the two in that archive, and the clear text says it went by the future emperor's own messenger. **Unsolved.**
2. **"More ciphers of Ferdinand III?" (DECODE R1579).** The record holds the 20 July 1640 letter that Ernst read, plus other sheets in different systems. I7060 is a code of two- or three-digit and two- or three-letter groups, with German clear text and possibly Latin in the cipher. I7066 has blocks in what looks like a simple symbol cipher, and I7068 (a negative image) is a longer text in a similar-looking cipher. **Unsolved.**
3. **Ferdinand III ↔ Cardinal-Infante Ferdinand, governor of the Spanish Netherlands.** These are in the Brussels archives (Secrétairerie d'État Allemande, inv. 540), with Latin clear text.
   - **R1889** (16 Nov 1635) and **R1890** (22 Feb 1640) use a two-digit and letter cipher. Andrew Aymeloglu read both, notified 19 Sept 2026, building from a surviving plaintext draft of 1635 (R954). Tomokiyo marks them **solved**.
   - **R1887** (28 Oct 1634, Stuttgart) is in an older system of graphic symbols and three-letter codes. Aymeloglu posted a "substantial reading with unresolved passages" on 23 Sept 2026. It is context-assisted, with no key sheet and no plaintext draft. It has 474 groups, of which 457 are graded only "M" (medium), and six spans unresolved and three conjectural. **Partial.**
4. **Variable-length figure code in Austrian archives (ÖStA HHStA, Staatskanzlei Interiora, Chiffrenschlüssel).** These are continuous digit streams.
   - **R2159** (Fra Giovanni di Lucca to Ferdinand III, 30 May 1644, Italian) and **R1408** (Warsaw, 24 Dec 1627, Italian) were solved by Daniel Bourdeau on 16 Sept 2026.
   - **R2179** (Kt. 20, Fasc. 27, f. 54; Italian per DECODE; undated in Tomokiyo's notes) is **unsolved**. Tomokiyo can parse the opening groups but cannot segment the rest consistently.

Solved siblings, named for calibration:
- **Wallenstein, 1626:** simple substitution, solved by "Nagra" in 2016.
- **Ferdinand III ↔ Archduke Leopold, 1640–45:** a numerical cipher with digits disguised as geometric figures by stroke count. Broken by Thomas Ernst in 2017 and published in *MIÖG* 129 (2021).
- **Carl von Rabenhaupt to Amalie Elisabeth of Hesse-Kassel, 1646:** read in 2020 after the key was found in Marburg (Antal, Zajac and Mírka, HistoCrypt 2021).
- **Two imperial ministers' homophonic ciphers:** solved in 2018 by Bosbach and Nagra.
- **Georg Adam Starhemberg, Paris, 23 May 1758:** a variable-length digit stream, solved by Aymeloglu on 21 Sept 2026 with a 1752 key found in DECODE R1695/R1698.

## What is unsolved
The plaintext of the 1634 Plzeň letter, the non-Ernst sheets of R1579, the residue of R1887, and R2179.

For R2179 the first problem is segmentation. Its digit stream has no group boundaries, and Tomokiyo notes dots that may or may not separate groups. That is the same parsing problem that blocked the Starhemberg and Vatican Part 5 texts until their rules were found.

## What survives
- The DECODE records R1579, R1887, R1889, R1890 and R2179 carry archive images. Access requires a DECODE login, which Bourdeau reports he has used to fetch images since 18 Sept 2026.
- Tomokiyo publishes a transcription of R2179 in variable2.htm.
- Aymeloglu's repository holds an elected transcription of R1887 (474 groups), but he does not redistribute the images.
- The Plzeň 1634 letter is known from Mírka's article. Whether it is imaged online was not established; Bourdeau files it under "DECODE-only".

## Prior attempts and current consensus
The field is moving week by week.
- **Tomokiyo** catalogued and partly parsed the items.
- **Bourdeau** solved R2159 and R1408 by annealing with shuffled controls. He lists R1579, R1887 and R2179 as reopenable now that DECODE images can be fetched.
- **Aymeloglu** read R1889 and R1890 with draft support and published a partial, explicitly conjectural R1887. He makes "no first-solve claim".
- **Mírka's** Crypto-World series and Leopold Auer's chapter in *Geheime Post* (2015) are the background literature on imperial ciphers. No one has published an attempt on the Plzeň 1634 letter or the R1579 non-Ernst sheets.

## What a solution would have to do
- **Plzeň 1634 and R1579:** a key that reads the letter in Latin, German or Italian consistent with the clear portions and the 1634 or 1640 context. Ideally the key matches a key sheet among the many Habsburg keys in DECODE (R1474–R1777 and others) or Mírka's reconstructed Trauttmansdorff ciphers.
- **R2179:** first a parsing rule stated in advance and applied uniformly to the whole stream, then a key under which every group reads Italian. "Correcting" groups to fit is not allowed beyond documented scribal slips.
- **R1887:** close the six unresolved spans without adding values that occur only once. Best of all, find a matching key or a second letter in the same repertoire, as Aymeloglu himself says.

## Why the scores
- **mystery 2:** imperial correspondence at the height of the Thirty Years' War (Nördlingen 1634, the Westphalian campaigns). It is valuable to specialists, but no single letter is known to bear on a major open question.
- **material 4:** originals survive and are imaged on DECODE behind a login. The transcriptions are partial (R2179 by Tomokiyo, R1887 by Aymeloglu). The Plzeň letter's digital status is unverified.
- **solvable 5:** state nomenclators and codes, used by chanceries that kept keys. Sibling ciphers in the same families have been read.
- **compute 4:** R2179 segmentation and key recovery is squarely computational, and so is matching sheets against DECODE's large key holdings. The R1579 I7060 sheet is a code with few messages, where context matters more than search. So not 5.
- **verifiable 4:** a full Latin, German or Italian reading is a strong check. Code groups and short sheets leave single-occurrence values unconfirmable without a key sheet.
- **crowding 3:** few dedicated treatments. But three active solvers (Tomokiyo, Bourdeau, Aymeloglu) took several of these items within the same fortnight in September 2026, so the remaining residue is contested ground, not empty.

## Sources
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," section "German" (statuses and 2026 notifications). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, "Habsburg ciphers" (Ernst's Ferdinand III–Leopold break; Mírka's Trauttmansdorff ciphers; Auer 2015). https://cryptiana.web.fc2.com/code/habsburg.htm
- SECONDARY — Tomokiyo, "Variable-Length Numerical Code in Austrian Archives" (R2159, R1408, R2179, Starhemberg). https://cryptiana.web.fc2.com/code/variable2.htm
- SECONDARY — Tomokiyo, "Solutions of Ciphers in a Continuous Digit Stream" (R1408 and Starhemberg solutions; R2179 "remains undeciphered"). https://cryptiana.web.fc2.com/code/variable3.htm
- SECONDARY — Tomokiyo, German ciphers (Wallenstein; Rabenhaupt key found in Marburg, citing Antal, Zajac and Mírka, HistoCrypt 2021). https://cryptiana.web.fc2.com/code/german.htm
- SCHOLARLY — Thomas Ernst, "Eine Geheimschrift der Habsburger während des Dreißigjährigen Krieges," *MIÖG* 129 (1) (2021) (cited via Tomokiyo, not opened). https://doi.org/10.7767/miog.2021.129.1.124
- SCHOLARLY — Jakub Mírka, "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů Státního oblastního archivu v Plzni" (2012) (cited via Tomokiyo, not opened). https://www.researchgate.net/publication/313678538
- CLAIMANT — Andrew Aymeloglu, ferdinand-1634 README (R1887 partial reading, 474 groups, grades, unresolved spans) and ferdinand-1635-1640 README (R1889/R1890 from the R954 draft). https://github.com/aaymeloglu/unsolved-ciphers
- CLAIMANT — Daniel Bourdeau, cyphersolver README and TARGETS.md (R2159 and R1408 solved 16 Sept 2026; R1579, R1887, R2179 "reopenable"). https://github.com/dbourdeau/cyphersolver
- PRIMARY (record link, not opened in this pass) — DECODE R1887. https://de-crypt.org/decrypt-web/RecordsView/1887

## Unverified claims
- The date of R2179. Tomokiyo's heading "(1644, 1627)" covers R2159 and R1408; R2179's date was not found.
- Whether the Plzeň 1634 letter is on DECODE or otherwise imaged, and its length.
- Whether the R1579 sheets I7060, I7066 and I7068 have been read since Tomokiyo's note. No reading was found in the Bourdeau or Aymeloglu repositories as of late September 2026.
- Aymeloglu's R1887 and R1889/R1890 readings have not been independently reviewed. The second-model review he mentions is his own process.
- The ResearchGate and *MIÖG* articles were not opened. Their content is as Tomokiyo reports it.
