+++
title = "Unread French codes of Louis XIV's wars, 1690–1710 (with Stepney to Manchester, 1702)"
slug = "louis-xiv-diplomatic-military-ciphers"
kind = "cipher"
era = "1690–1710"
origin = "France (Versailles; embassies in Constantinople and Rome; armies in Alsace and Flanders); English embassy in Vienna"
language = "French (English for the Stepney letter)"
status = "unsolved"
confidence = "medium"
digitized = "http://www.traces-ecrites.com/expositions/louis-xiv-du-soleil-a-leclipse/laffaire-de-la-regale/"
tags = ["nomenclator", "code", "diplomatic", "military", "louis-xiv", "great-cipher", "wallis", "DECODE", "cryptiana", "key-hunt"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 3
verifiable = 5
crowding = 3
+++

# Unread French codes of Louis XIV's wars, 1690–1710 (with Stepney to Manchester, 1702)

## What it is
These are encoded French despatches from the Nine Years' War and the War of the Spanish Succession. All use numerical codes of a few hundred to about 800 groups, mixing letters, syllables and words in the style of the Rossignol "great ciphers." Each sits on Satoshi Tomokiyo's Cryptiana list under "French," apart from one English letter from his "Miscellaneous" section, included here as the English counterpart from the same war.

| Item | Date | Where | Status |
|---|---|---|---|
| Louis XIV to Castagnères, ambassador at Constantinople (secret instructions on Tekeli and Transylvania; code up to 420) | Jul–Aug 1690 | Printed in Paul Rycaut, *History of the Turks*, p.453 ff. | **Partially solved.** Tomokiyo identified it as the same code as a 1693 despatch whose decipherment by John Wallis is printed in Kahn's *Codebreakers* (p.168), and decoded much of it. Some groups remain conjectural or unread. John Davys apparently deciphered these letters about 1701, but his decipherment is not known. |
| Louis XIV to the duc de Chaulnes, ambassador at Rome (the *régale* affair; about 300 groups, 116 distinct, up to 535) | 10 Jul 1690 | Images on Traces Écrites; discussed on Klausis Krypto Kolumne, 31 Jan 2019 | Unsolved. Bourdeau (Sept 2026) verified the ciphertext and established a one-part, ten-column Croissy-table design. His ciphertext-only annealer recovers 4–12% on a matched 300-group control, so he reports no reading. The minute should be in AE Rome Corr. 331–332. |
| Marshal Catinat, camp of "Inglesheim" (probably Ingenheim, Alsace), apparently to Beat Jakob II Zurlauben (code up to 464) | 15 Sep 1702 | Aargau Cantonal Library, Zurlauben collection; images on Klausis Krypto Kolumne, 1 May 2016 | Unsolved. None of the known period codes fit (Tomokiyo). |
| Torcy to the French plenipotentiaries at Geertruidenberg, endorsed "M Blencow cannot decypher them" | 3 Apr 1710 | BL Add MS 61575 ff.38–41 (DECODE R8755) | Unsolved since William Blencowe failed in 1710. |
| Marshal Villars to the Abbé de Polignac (plenipotentiary at Geertruidenberg) | 1 Jun 1710 | BL Add MS 61575 f.44 (DECODE R8756), a copy | Unsolved; a different code from Torcy's. |
| George Stepney (English envoy, Vienna) to the Earl of Manchester (24 groups) | 23 Mar 1702 | Yale, Beinecke OSB MSS fc37, box 8, f.40 (Manchester Papers) | Unsolved. The Manchester papers' own key (THE = 454) does not read it. The key is likely "Mr. Stepney's cipher," requested in August 1701, perhaps in TNA SP 105/106 or BL Add MSS 7058–78. |

Solved siblings in the same section:
- Louvois to Lauzun in Ireland, 27 May 1690: the "French cipher unsolved by John Wallis." Norbert Biermann solved it in 2020 by finding the key in the archives (code to 451, letters scattered through the whole table). It shows the archival route working on exactly this kind of code.
- The 1691 coded despatch received by Catinat (Feuquières, Pignerol, 25 Jan 1691), read by Daniel Bourdeau in September 2026 as the Pignerol governors' *petit chiffre*.
- Seven 1691 Louvois/Louis XIV despatches to Catinat, decoded with Bazeries' 1893 Grand Chiffre table.

## What is unsolved
What the five French despatches (four unread, one partly read) and the Stepney passage say. Cryptographically, the problem is recovering one-part or two-part code tables of 400–800 entries from one or two letters each.

## What survives
- **Constantinople:** printed whole in Rycaut (Google Books).
- **Chaulnes:** page images on the Traces Écrites site, with Bourdeau's corrected transcription (two misreadings fixed).
- **Catinat 1702:** images on Klausis Krypto Kolumne; original in Aarau.
- **Geertruidenberg and Villars–Polignac:** in BL Add MS 61575, which is not digitized by the BL. DECODE holds images and transcriptions behind a login. Tomokiyo's own transcription files now return 404 (Bourdeau, Sept 2026).
- **Stepney:** Yale Beinecke, viewable through IIIF.

For two of the items, the French originals or minutes almost certainly survive in clear or decoded form at the Archives des Affaires étrangères: the Rome correspondence for Chaulnes, and the Geertruidenberg negotiation papers for Torcy.

## Prior attempts and current consensus
- **Tomokiyo:** reconstructed some fifteen French codes of 1676–1704 and partly decoded the Constantinople instructions (Cryptiana, "Louis XIV's Codes," "Decoding Louis XIV's Secret Instructions to His Ambassador in Constantinople," "A Great Cipher Left Undeciphered by William Blencowe").
- **Klaus Schmeh's readers:** worked Chaulnes (2019) and Catinat 1702 (2016) on Cipherbrain without a solution.
- **Bourdeau (2026):** worked Chaulnes to a negative result with controls, and lists the 1710 pair and Catinat 1702 as needing ciphertext or archive access.

The field's view, implicit in Biermann's 2020 success and in Bourdeau's negative controls, is that single letters in these large codes yield to a key or a parallel clear text, not to cryptanalysis.

## What a solution would have to do
- Produce a code table that reads the whole letter as grammatical late-seventeenth-century French. The table must respect the period's design features: underlined groups for varied terminations, nulls and deletion signs, and the one-part or two-part ordering visible in the numbering.
- Agree with the clear-text context and with the known course of events: the *régale* dispute for Chaulnes, the 1702 Alsace campaign and the Bavarian junction for Catinat, the Geertruidenberg talks of spring 1710.
- Ideally be confirmed by a second document: the archival minute, the recipient's decipherment, or another letter in the same code. A table fitted to one 300-group letter with no outside check is not a solution. Bourdeau's controls show that wrong keys score within noise of the true one at this length.

## Why the scores
- **mystery 2:** operational and diplomatic detail of known episodes. The Torcy letter at Geertruidenberg is the most historically interesting, but its substance is probably recoverable from French archives.
- **material 4:** all ciphertexts survive whole, and most have images or printed text online. The two BL 1710 letters are the exception (score 3 on their own).
- **solvable 5:** state-issued codes, used as designed.
- **compute 3:** this is the "large codebook, few messages" case. A 300–500-group letter in a 450–800-entry code is underdetermined for ciphertext-only methods, as Bourdeau's matched controls show. Computation helps with code-family identification, with partial reads where a related code is known (Constantinople), and with matching letters across DECODE. The decisive step is a key or a minute.
- **verifiable 5:** French plaintext in context, and very likely a clear copy in the AE archives to compare against.
- **crowding 3:** Tomokiyo, Cipherbrain readers and Bourdeau have each worked the main items, so it is lower than the genre default.

## Sources
- SECONDARY — S. Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," sections "French" and "Miscellaneous." https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Louis XIV's Codes" (§4B Chaulnes, §5 Louvois–Lauzun and Biermann's 2020 solution, §7 Catinat 1691, §9 Catinat 1702). https://cryptiana.web.fc2.com/code/louisxiv.htm
- SECONDARY — S. Tomokiyo, "Decoding Louis XIV's Secret Instructions to His Ambassador in Constantinople (1690)." https://cryptiana.web.fc2.com/code/louisxiv2.htm
- SECONDARY — S. Tomokiyo, "A Great Cipher Left Undeciphered by William Blencowe" (BL Add MS 61575). https://cryptiana.web.fc2.com/code/blencowe2.htm
- SECONDARY — S. Tomokiyo, Manchester Papers diplomatic code (Stepney 1702). https://cryptiana.web.fc2.com/code/glorious.htm
- SCHOLARLY — N. Biermann, "'I Suspect Somewhat of Peculiar in His Way of Ciphering'" (UdK Berlin repository; Louvois–Lauzun key). https://doi.org/10.25624/kuenste-1338
- PRIMARY — Louis XIV to Chaulnes, 10 July 1690, page images, Traces Écrites. http://www.traces-ecrites.com/expositions/louis-xiv-du-soleil-a-leclipse/laffaire-de-la-regale/
- POPULAR — K. Schmeh, Klausis Krypto Kolumne, "Wer knackt diesen verschlüsselten Brief von Nicolas de Catinat?" (1 May 2016). http://scienceblogs.de/klausis-krypto-kolumne/2016/05/01/wer-knackt-diesen-verschluesselten-brief-von-nicolas-de-catinat/
- POPULAR — K. Schmeh, Klausis Krypto Kolumne, "Can you decipher this letter written by Louis XIV?" (31 Jan 2019). http://scienceblogs.de/klausis-krypto-kolumne/2019/01/31/can-you-decipher-this-letter-written-by-louis-xiv/
- CLAIMANT — D. Bourdeau, cyphersolver `TARGETS.md` / `README.md` (Chaulnes attempt and controls; 1710 pair; Stepney MS location and rejected key; Catinat 1691 read). https://github.com/dbourdeau/cyphersolver

## Unverified claims
- That the Constantinople instructions are the letters John Davys deciphered about 1701. Tomokiyo says "appears to be."
- How much of the Constantinople text remains unread. Tomokiyo marks many readings as conjectural; no percentage was found.
- The Stepney shelfmark (Beinecke OSB MSS fc37 box 8 f.40) and the 24-group count are Bourdeau's. The suggestion that the key is in TNA SP 105/106 or BL Add MSS 7058–78 is his hypothesis.
- The recipient of the Catinat 1702 letter (Zurlauben) rests on Schmeh and Büsser (2008) as reported by Tomokiyo.
- Whether the AE archives hold clear minutes of the Chaulnes or Torcy letters. This is inferred from period practice, not checked.
- Whether any of these despatches has been decoded in print (for example, in Recueil des instructions, Rome, or in Geertruidenberg editions). Bourdeau reports none found for Chaulnes; the others were not checked.
