# Breach research for BnF Colbert 500/33 f.539 (Joyeuse to Villars, 15 Feb 1594)

Fetched 2026-10-01. Tiers per AGENTS.md.

## 1. Lasry, HistoCrypt 2022 (SCHOLARLY)
URL: https://ecp.ep.liu.se/index.php/histocrypt/article/view/402 (PDF: .../article/download/402/360; DOI 10.3384/ecp188402). Saved as lasry-histocrypt2022.pdf (3.3 MB, 6 pp, text extracted OK).
- Letter: BnF Colbert 500/33 f.555, Claude de Bauffremont, baron de Sennecey, League ambassador in Rome. Cleartext with cipher passages.
- Ciphertext: 858 symbols, 86 distinct (paper). Tomokiyo's page says 79 symbols (inconsistent; paper wins for his own transcription).
- Method: homophonic key recovery by simulated annealing (his DECRYPT tool; swap two homophones, reassign one). Plain trigram scoring on a generic French Gutenberg corpus failed; 5-gram scoring gave partial confirmation; success needed a corpus of HISTORICAL French books plus manual processing. Key recovered 2-6 homophones per letter, some symbols = prepositions, some unidentified, encryption errors (T used for F).
- Length/control limits: NO explicit minimum length or control experiments stated. Only: failure attributed to "relatively short" text plus many distinct symbols. 858 symbols / 86 distinct (about 10 per symbol) is the one working datapoint.
- f.539: NOT mentioned. Joyeuse not mentioned. Paper only thanks Tomokiyo for introducing the cipher, and Desenclos, Tomokiyo, Biermann for transcription help.
- Key table: Figure 2 "Tentative Key" is an image in the PDF (not extractable as text); partial, tentative. Figure 3 gives tentative decryption. Check figures visually. No machine-readable key.
- Relevance: f.555 is a different cipher (Sennecey, Rome). f.539 is much shorter; no basis for transfer unless Joyeuse and Sennecey, both in Rome in Feb 1594, shared a symbol alphabet. Tomokiyo says f.539 "seems different" from f.530 alphabet. Whether f.539 matches f.555 has not been tested publicly (not found).

## 2. Candidate material
- Cinq Cents de Colbert 33 (Gallica ark:/12148/btv1b10033958p per Tomokiyo; SECONDARY pointer, not independently opened). Contains f.539 (undeciphered original) and neighbours:
  - f.528 Pelissier to Joyeuse, 13 Feb 1594, symbol cipher of f.530, many nulls, some interlinear decipherment. DECIPHERED/partly. Same recipient as our sender and same week; best nearby Joyeuse-network material.
  - f.530 partially reconstructed symbol alphabet (used for f.528 and f.575). Tomokiyo: f.539 cipher "seems different".
  - f.535 Mercier to M. de Joyeuse, 15 Feb 1594 (original; cipher status not stated).
  - f.544 Joyeuse to Montpezat; f.551 Joyeuse to Archbishop of Lyon; f.553 Joyeuse to Duc de Joyeuse (all originals; cipher status NOT stated by Tomokiyo; check images). Local cache already has c544/c545 etc. images.
  - f.546 Montpezat to Joyeuse (Madrid, 13 Feb 1594).
  - f.555 Sennecey to Abp of Lyon (Lasry-solved); f.575 Sennecey to Jeannin 15 Mar 1594, deciphered with f.530 alphabet per Tomokiyo.
  Source: https://cryptiana.web.fc2.com/code/viete.htm (SECONDARY/POPULAR; Tomokiyo is expert amateur, cites images).
- BnF fr.3985 no.48 fol.81: Caulet (agent of Joyeuse) to Joyeuse, Paris, 16 Aug 1593, cipher image on Tomokiyo league.htm (https://cryptiana.web.fc2.com/code/league.htm). Key status not stated. Tomokiyo (viete.htm): "One cipher used by Joyeuse with his agent is in league.htm, but does not seem to solve" f.539. Gallica for fr.3985: ark:/12148/btv1b90606498. Best lead for an actual Joyeuse key, but earlier (Aug 1593) and already tried by Tomokiyo.
- BnF fr.3974-3995 Memoires de la Ligue (Nevers papers; fr.3995 = Nevers cipher collection). No Joyeuse-Villars item found in league.htm. Full-text grep of league.htm: Joyeuse appears only for Caulet.
- BnF fr.15890-15911: 17 letters of Cardinal de Joyeuse but dated 1599-1606 (https://archivesetmanuscrits.bnf.fr/ark:/12148/cc461166, SECONDARY finding aid). Wrong period.
- Published edition: Aubery, L'histoire du cardinal duc de Joyeuse (1654), Gallica https://gallica.bnf.fr/ark:/12148/bpt6k856018v.image (PRIMARY-ish printed edition; includes "memoires, lettres, depeches ... non encore imprimees"). NOT searched for 1594 content or cipher; follow up (plaintext of a Feb 1594 Joyeuse letter to Villars could be a crib).
- Villars/Brancas papers, Joyeuse Rome embassy papers, Lettres missives: no hits found. UNVERIFIED that any exist.
- DECODE (https://de-crypt.org/decrypt-web/RecordsView/N): a search snippet claimed a record for "Joyeuse to Villars, Rome, 15 Feb 1594 (500 Colbert 33 f.539)". I could not find or open it; the four record pages I opened (933, 1686, 1220, 2370) are unrelated. UNVERIFIED. Records need authentication for images. Key search in DECODE by place/year remains to do manually.

## 3. Published keys of League ciphers 1593-94 (Tomokiyo)
- Pelissier/Joyeuse/Sennecey symbol cipher "f.530" (Feb-Mar 1594): partial reconstruction in viete.htm, symbols not numeric; Tomokiyo says used by Pelissier, Joyeuse (as correspondent), Sennecey (f.575). Not same as f.539.
- Syllabic Numerical Cipher (1593), used by Condeste[?] March 1594 (viete.htm list, SEC2-4): numeric/syllabic, closest in type to f.539's numbers+marked signs; link goes to spanish3/4.htm, not opened. Worth checking.
- Savoy cipher (savoy.htm) used by Lebel Aug 1593; Nevers collection numbered ciphers (nevers.htm) incl. no.57, 60, 65 (1593-94, Nevers/Lesdiguieres/Henry IV letters). Different users; not Joyeuse.
- No published key naming Joyeuse-Villars. UNVERIFIED: any cipher shared between Joyeuse and Villars.
Note: viete.htm calls f.575 "Senecey to President Jeannin, 15 March 1594" and f.555 "Senecey to Archbishop of Lyon" (date unstated).

## 4. Historical context (content check)
- Villars (Brancas) held Rouen for the League; submitted 27 March 1594 (SECONDARY: https://en.wikipedia.org/wiki/Andr%C3%A9_de_Brancas, stub; made Admiral of France 23 Aug 1594 there; search snippet said 10 May / Rouen: conflicting, unverified).
- Draft treaty from Henri IV to Villars, offered "a few days before the coronation" (Chartres, Feb 1594): debts of the admiral paid, financial advantages to Leaguers, city privileges. Vidalenc, Annales de Normandie 11(3), 1961, p.233, citing a Chartres municipal library MS. https://www.persee.fr/doc/annor_0003-4134_1961_num_11_3_6166 (SCHOLARLY, only abstract-level read). Timing coincides with 15 Feb letter: Villars was bargaining while Joyeuse wrote from Rome.
- Joyeuse broke with the League in 1593 and worked for Henri IV, getting the absolution Sept 1595 (https://en.wikipedia.org/wiki/Fran%C3%A7ois_de_Joyeuse, SECONDARY). So a Feb 1594 letter to Villars plausibly urges submission / reports Rome's stance on absolution, or reports Spanish and Mayenne manoeuvres. Hypothesis only.
- Paris entered 22 March 1594 (https://www.herodote.net/22_mars_1594-evenement-15940322.php, POPULAR).
- Better sources to get (not fetched): Persee/Annales de Normandie on pacification of Normandy; Lavisse Histoire de France VI (http://www.mediterranee-antique.fr/Fichiers_PdF/JKL/Lavisse/HF_T62.pdf, SECONDARY); Aubery 1654 above; Sully memoires.
