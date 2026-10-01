+++
title = "French royal and court cipher passages left unread, 1567–1610"
slug = "french-royal-ciphers-1567-1610"
kind = "cipher"
era = "1567–1610"
origin = "France (Valois and early Bourbon court; the Nevers correspondence)"
language = "French (Birago passage Italian)"
status = "unsolved"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b9060248g/f120.item"
tags = ["nomenclator", "letters", "diplomatic", "french", "short-ciphertext", "cryptiana", "BnF", "Gallica", "wars-of-religion"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 3
verifiable = 4
crowding = 4
+++

# French royal and court cipher passages left unread, 1567–1610

## What it is
Four short ciphered passages in French court and noble correspondence. Satoshi Tomokiyo lists them in the "French (up to 1610)" section of his Cryptiana list of unsolved ciphers, and none had been read as of September 2026. Each is a few lines to a paragraph, set inside a letter that is otherwise in clear.

| Item | Location | Status (Sept 2026) |
|---|---|---|
| Catherine de Médicis (countersigned L'Aubespine) to Philibert du Croc, ambassador in Scotland, 27 April 1567 | Reproduced in Paul Destray, *Un diplomate français du XVIe siècle: Philibert du Croc* (1924), p. 53 and the plate after p. 56 (Gallica); the original's location is not verified here | **Unsolved.** The clear text just before the cipher ("jay recu du sr x3 lettres en datte") suggests the cipher opens with "du" |
| Lodovico Birago to the Duke of Nevers, Saluzzo, 13 November 1571 (Italian) | BnF fr. 3251, f. 119 (no. 63) | **Unsolved.** Birago's other letters of 1570–72 read with reconstructed keys; this paragraph is in a different, numerical cipher |
| Nicolas Potier de Blancmesnil to the Duke of Nevers, "ce dernier juin" (year not given) | BnF fr. 3633, f. 24 (no. 15) | **Unsolved.** "Some phrases" in cipher |
| Marie de Médicis, regent (countersigned Brulart), to Savary de Brèves in Rome, 15 September and 10 November 1610 | BnF fr. 3789, ff. 17, 19 | **Unsolved.** Short passages; they do not match Brèves's known ciphers |

Solved siblings on the same list (calibration, not separate entries):
- Charles IX to du Croc. Undated (1565–67 or 1572); reproduced in Destray. George Lasry solved it in 2022, and Daniel Bourdeau confirmed in 2026 that it is a different symbol system from Catherine's 1567 letter.
- Danzay to Henri III, 1574. Sergey Ryabov solved it in 2025.
- Villeroy to Henri III, 1577. Lasry solved it in 2022.
- Henri IV to Brèves, 5 January 1610 (BnF fr. 3541). Lasry, with Norbert Biermann and Tomokiyo, solved a significant part in 2021. Camille Desenclos then reported that the key survives in the BnF.

## What is unsolved
The plaintext of each of the four passages. Each needs a different kind of work:
- **Du Croc, 1567.** The key is unknown. Destray also reproduces a La Forest–du Croc cipher of 1567, which uses plain words as codenames. Nobody reports having tested it against Catherine's passage.
- **Birago, 1571.** This is the best-characterized of the four. Bourdeau re-transcribed the page glyph by glyph. He counts 483 digits, 15 null letters, 16 marked code digits and 9 inline wavy signs. His tests point to a heavily homophonic two-digit alphabet with marked one- or two-digit code groups, and they rule out variable-length, polyphonic and syllabic designs. He concludes the paragraph is "structure fixed, not deciphered". At about 228 tokens over 62 symbols, his annealer finds only false optima even on synthetic controls of the same profile. So the method is the limit, not the text. No sibling letter in this cipher has been found in the volume.
- **Blancmesnil.** Nobody has published a structural description beyond "some phrases in cipher". Tomokiyo says he has seen only some pages of fr. 3633. Other letters in that volume use known ciphers: Turenne, the Governor of Sy (Vieuville–Nevers), and Sillery.
- **Marie de Médicis, 1610.** Tomokiyo says the passages look like the cipher of Henri IV's 5 January 1610 letter to Brèves but do not match Brèves's known ciphers. That letter's key survives in the BnF (Desenclos). Nobody reports testing the surviving Henri IV–Brèves key, or Brèves's 1603 key (BnF fr. 3462 f. 103), against these passages.

## What survives
- All four are on Gallica as images: the Destray book, BnF fr. 3251, and BnF fr. 3789. BnF fr. 3633 is in the BnF catalogue, and Tomokiyo reports seeing pages of it.
- Machine-readable transcriptions exist only for Birago: Tomokiyo's (on the Cryptiana list page) and Bourdeau's corrected glyph-level version (on GitHub).
- The keys for the context are many reconstructed French and Nevers keys in Tomokiyo's catalogue of ciphers in BnF fr. 3995 and related volumes, plus Desenclos's work on French cryptographic sources of 1530–1630.

## Prior attempts and current consensus
- Tomokiyo listed all four.
- Bourdeau ran a documented structural and annealing campaign on Birago (16 September 2026) and stopped short of a reading.
- Klaus Schmeh's Cipherbrain blog publicized the du Croc letter; Tomokiyo learned of it there.
- No reading of any of the four has been published.
- Lasry has solved many nearby BnF ciphers. It is not recorded whether he tried these.

Newcomers should read Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III" and "French Ciphers during the Reign of Louis XIII"; his Nevers catalogue; and Bourdeau's Birago notes.

## What a solution would have to do
- **Read in the passage's language, with one key.** The decipherment must yield French (Italian for Birago) that continues sensibly from the clear text around it. For du Croc, it should start in a way that fits "du sr …".
- **Key provenance.** A key found in an archive or rebuilt from a sibling letter, and then shown to read a passage it was not built from, is the strongest evidence. A key fitted only to these few lines is weak evidence.
- **Short-text control.** For any key recovered from the ciphertext alone, show that the same solver reads synthetic controls of the same length and symbol count. Bourdeau's Birago work shows this check is not optional at 200–300 tokens.
- **Historical fit.** Names and events must match the documented situation: Scotland in April 1567 (just before Mary's marriage to Bothwell); Saluzzo and Carmagnola in November 1571; the Rome embassy after Henri IV's assassination in 1610.

## Why the scores
- **mystery 2.** Specialist interest. The 1567 Scottish passage, written in the weeks before the Bothwell marriage, could interest Mary Stuart historians, but it is a few lines long.
- **material 4.** The originals or facsimiles are digitized, but each ciphertext is short. That limits any method.
- **solvable 5.** These are court nomenclators used in real correspondence.
- **compute 3.** Hill-climbing does not reliably work at this length. Bourdeau's controls show it failing on Birago, so this is measured, not guessed. The realistic computational route is to test every published period key against each passage, which is a sweep that has not been done. That makes it 3 and not 2.
- **verifiable 4.** Continuous plaintext in context is checkable. With short passages, a fitted key can produce plausible fragments, so the evidence needs key provenance or controls.
- **crowding 4.** One structural campaign (on Birago) and catalogue listings. Otherwise untouched.

## Sources
- PRIMARY — BnF fr. 3251, f. 119 (Birago, 13 Nov 1571), Gallica. https://gallica.bnf.fr/ark:/12148/btv1b9060248g/f120.item
- PRIMARY — Paul Destray, *Un diplomate français du XVIe siècle: Philibert du Croc* (1924), facsimiles, Gallica. https://gallica.bnf.fr/ark:/12148/bpt6k932364m
- PRIMARY — BnF fr. 3789 (Marie de Médicis to Brèves, 1610), Gallica. https://gallica.bnf.fr/ark:/12148/btv1b9059628m
- PRIMARY — BnF fr. 3633, catalogue record (Blancmesnil). https://archivesetmanuscrits.bnf.fr/ark:/12148/cc57784f/cd0e3327
- SECONDARY — S. Tomokiyo, Cryptiana, "Unsolved Historical Ciphers" (French up to 1610). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III" (du Croc 1567; La Forest–du Croc cipher). https://cryptiana.web.fc2.com/code/henryiii.htm
- SECONDARY — S. Tomokiyo, "Catalogue of Ciphers (Mainly Related to Duke of Nevers)" (BnF fr. 3251, fr. 3633). https://cryptiana.web.fc2.com/code/nevers.htm
- SECONDARY — S. Tomokiyo, "French Ciphers during the Reign of Louis XIII" (Marie de Médicis 1610; Henri IV 1610 key). https://cryptiana.web.fc2.com/code/louisxiii.htm
- CLAIMANT — Daniel Bourdeau, Birago notes (16 Sept 2026): transcription, structure tests, failed controls. https://github.com/dbourdeau/cyphersolver/blob/main/targets/birago/NOTES.md
- CLAIMANT — Daniel Bourdeau, "Charles IX to Philibert du Croc" (confirms Lasry's 2022 solution and the separate system of Catherine's letter). https://dbourdeau.github.io/cyphersolver/charlesixducroc.html

## Unverified claims
- Where the original of Catherine's 27 April 1567 letter is held. Destray reproduces it, but the source is not established here.
- The year of the Blancmesnil letter, and the length of its ciphered phrases.
- Whether Lasry or anyone else has tried Marie de Médicis's passages against the surviving Henri IV–Brèves key.
- That none of the four has been solved in the weeks before this entry. Tomokiyo's September 2026 notice says solutions are arriving faster than he records them. Bourdeau's index, checked late September 2026, lists only Birago, as not deciphered.
