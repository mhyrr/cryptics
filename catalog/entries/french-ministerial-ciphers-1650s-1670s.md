+++
title = "French ministerial cipher passages, 1636–1675 (Condé–Barrière 1654, Mélanges de Colbert, Sabran residue)"
slug = "french-ministerial-ciphers-1650s-1670s"
kind = "cipher"
era = "1636–1675"
origin = "France and the Spanish Netherlands (Condé's agent in London; Colbert's and Sabran's correspondents)"
language = "French"
status = "unsolved"
confidence = "medium"
digitized = "https://de-crypt.org/decrypt-web/RecordsView/8395"
tags = ["nomenclator", "one-part-code", "syllabary", "letters", "BnF", "British-Library", "DECODE", "Cryptiana", "Louis-XIV", "short-ciphertext", "group-entry"]

[scores]
mystery = 2
material = 3
solvable = 4
compute = 3
verifiable = 4
crowding = 4
+++

# French ministerial cipher passages, 1636–1675

## What it is
This entry groups the open residue of the "French (17th Century)" section of Satoshi Tomokiyo's Cryptiana list. Most of the section has fallen, much of it in September 2026: Richelieu 1629 and 1641, Brasset to Mazarin 1649, Bordeaux 1653–54, Le Tellier–Castelnau 1657. What remains:

1. **Prince of Condé–Barrière, 1654.** British Library Add MS 4200, f. 98 (DECODE R8395), dated 15 September 1654 NS. It comes from the correspondence between the rebel Prince of Condé, then serving Spain, and Henri de Taillefer, sieur de Barrière, his agent in Cromwell's London, preserved among the Thurloe intercepts. Tomokiyo reconstructed the 1655 Condé–Barrière cipher (f. 108, R8405–R8406). The 1654 letter does not use that cipher's hacek, and the records mention an accident with the cipher in October 1654 after which a new one was made. So f. 98 is probably in an earlier, unknown key. The short ciphertext at f. 101 (R8398, 18 June 1655) may be in yet another cipher.
2. **Mélanges de Colbert (BnF), three short pieces.**
   - (i) Mél. Colbert 172, f. 23: Louis de Béthune, duc de Charost, a short paragraph in figures. Tomokiyo lists it as 1673; Bourdeau reads Calais, 3 July 1675.
   - (ii) Mél. Colbert 168bis, f. 553: the abbé de Gravel to the comte de Maulevrier, Mainz, 1674, with short cipher passages.
   - (iii) Mél. Colbert 127, f. 349: a few words in figures, Ratisbon, 29 January 1665. Bourdeau identifies the writer as the abbé de Gravel.

   Bourdeau finds that (i) and (ii) are one key (Maulevrier's): 106 plain figures between them, in the range 52–489. Tomokiyo notes that all the Colbert instances he examined are one-part codes.
3. **Melchior de Sabran (Genoa, 1630–37): the one remaining piece.** Tomokiyo's heading is "Most Solved". Lasry solved the Louis XIII–Sabran cipher of 1631, which also reads Sabran's 1633–35 passages in BnF fr. 4134 and fr. 4135, as well as the 1637 Farnese enclosure. Tomokiyo solved the 1632 Servien–Sabran cipher. Still unread: BnF Baluze 156, f. 157, a copy of a letter of 9 February 1636 to "Mr de ch.gr", with passages "in a different cipher, yet unsolved".

## What is unsolved
The key and plaintext of Condé f. 98 (and possibly f. 101); the Maulevrier key behind the Charost and Gravel passages; the 1665 Gravel words; and the Sabran "ch.gr" passages.

## What survives
- The Condé items are in BL Add MS 4200, imaged on DECODE (R8394–R8406).
- The Colbert and Sabran volumes are on Gallica. Bourdeau read the Colbert passages from the Gallica images.
- Sibling material is extensive. There are eleven Condé–Barrière letters of 1654–55, some calendared in the Thurloe State Papers, and Tomokiyo's reconstructed 1655 key. Charost has 22 other letters online, but Bourdeau finds them all in clear. There are two Maulevrier letters, and the 1672 Colbert–Gravel cipher.

## Prior attempts and current consensus
- **Tomokiyo:** reconstructed the 1655 Condé–Barrière cipher and many Colbert-correspondent keys, and catalogued these as the leftovers.
- **Daniel Bourdeau (15–16 Sept 2026):** worked the Colbert passages. A monotone annealer reads matched controls of both strict alphabetical designs that this office used, but fails the target under each. He concludes it is "probably a word nomenclator; needs the key or a clear copy". His tracker lists Condé R8395 as not yet attempted (formerly "DECODE-only", now reopenable).
- **Sabran "ch.gr":** no attempt found.

The consensus is that these are unsolved, and that they are short. The binding constraint is a key sheet or sibling, not algorithms.

## What a solution would have to do
- **Condé f. 98:** a key that reads the whole letter in French that fits the Condé–Barrière correspondence of autumn 1654 (Condé's Spanish service, his dealings with the Protectorate). It should be either derivable from or explicitly distinct from the 1655 key, and it should not read f. 101 unless f. 101 is demonstrably the same system.
- **Colbert (i)+(ii):** one key that reads both passages. They share 13 groups, including a repeated four-group phrase, which any solution must render identically. The reading must fit Charost's "la mesme nouvelle" sent to Maulevrier that morning. With about 106 figures in a probable one-part code, a reading by context alone is weak. A recovered Maulevrier key sheet, or a clear copy, would be decisive.
- **Sabran ch.gr:** a key that reads every passage of the 1636 copy coherently within Sabran's Genoa correspondence.

## Why the scores
- **mystery 2:** routine-to-interesting diplomatic news. Condé's dealings with Cromwell are the most historically pointed item, but even that would add detail to a known story.
- **material 3:** the originals survive and are imaged, but the open ciphertexts are short (a paragraph, a few words, passages in a copy). That limits any method. It could have been 2 for the Colbert pieces alone; Condé f. 98 is a fuller letter and keeps the group at 3.
- **solvable 4:** state ciphers with determinate plaintext. Held at 4 because the Colbert passages may be a word code where the key, not the text, carries the information.
- **compute 3:** Bourdeau's matched-control result shows that ciphertext-only annealing cannot settle the Colbert key at this length. Computation can rank candidate designs and search sibling volumes and DECODE key sheets, but it is unlikely to decide alone. Condé f. 98 is the most computable piece.
- **verifiable 4:** a found key sheet would be mechanical. A context reading of short code passages would remain arguable.
- **crowding 4:** Tomokiyo and Bourdeau only. Condé 1654 and Sabran ch.gr have no recorded attempt.

## Sources
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," section "French (17th Century)" (Condé, Colbert, Sabran items; Bourdeau's 2026 corrections). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, Louis XIV-era ciphers (Condé–Barrière correspondence, Add MS 4200 ff. 96–108, the October 1654 cipher accident; Mélanges de Colbert survey, one-part codes, Charost and Gravel–Maulevrier). https://cryptiana.web.fc2.com/code/louisxiv0.htm
- SECONDARY — Tomokiyo, Louis XIII-era ciphers (Sabran: Lasry's 1631 key applying to fr. 4134 and fr. 4135; Baluze 156 f. 157 undeciphered). https://cryptiana.web.fc2.com/code/louisxiii.htm
- CLAIMANT — Daniel Bourdeau, cyphersolver README and TARGETS.md, row "Colbert passages" (one key, 106 figures 52–489, failed matched-control annealing; Condé R8395 listed as reopenable). https://github.com/dbourdeau/cyphersolver
- PRIMARY (record link, not opened in this pass) — DECODE R8395, BL Add MS 4200 f. 98. https://de-crypt.org/decrypt-web/RecordsView/8395

## Unverified claims
- **Direction of Condé f. 98.** Tomokiyo's list says "a letter from the Prince of Condé to Barriere". His own detailed table in louisxiv0.htm lists f. 98 as "Barriere to Conde, 15 September 1654 NS". Not resolved here.
- **Date of Charost (i).** 1673 per Tomokiyo, 3 July 1675 per Bourdeau. Bourdeau's reading of the Gallica image is the more recent and specific claim, but it was not checked here.
- **Date of the Sabran letter.** Tomokiyo's article prints "9 February 1536" under a heading "1636"; 1636 is assumed.
- Whether the Lasry or Tomokiyo Sabran keys were tested against the "ch.gr" passages and failed, or simply not tried. Tomokiyo says only "appears to be in a different cipher".
- Images were not opened in this pass. Given the September 2026 pace, any item may already be solved.
