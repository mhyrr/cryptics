+++
title = "Italian and Latin ciphers with superscript digits, 1527–1529 (Garbino/Ranzo code, Serno Gilino, Worcester residue)"
slug = "italian-superscript-digit-ciphers-1520s"
kind = "cipher"
era = "1527–1529"
origin = "Imperial court in Spain and Italian diplomats writing to Wolsey; now in the BnF (Paris) and BL Cotton Vespasian (London)"
language = "Italian (Garbino/Ranzo); Latin (Gilino, Worcester)"
status = "unsolved"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b90601558"
tags = ["nomenclator", "code", "superscript", "letters", "diplomatic", "Cryptiana", "DECODE", "Gallica", "1520s"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 3
verifiable = 4
crowding = 4
+++

# Italian and Latin ciphers with superscript digits, 1527–1529

## What it is
A family of 1520s diplomatic ciphers whose symbols are a base letter carrying a superscript number (a327, g215, s395). Satoshi Tomokiyo's *Cryptiana* list has three items in this family. This entry groups the two that are still unsolved and records the third, nearly solved, as their control.

1. **The "Garbino" letter and Hieronimo Ranzo's code (1528).** Tomokiyo lists it as "Venetian? Cipher with Superscript Digits".
   - BnF fr. 3022 f. 44 (catalogue no. 20) is an unsigned Italian memoir dated Madrid, 11 April 1528, endorsed to "Seigneur Garbino". BnF Clairambault 327 ff. 279–280 is an eighteenth-century copy of it. Daniel Bourdeau established in September 2026 that the copy is not a second witness.
   - Letters of Hieronimo Ranzo use the same code: BnF fr. 2988 f. 2 and ff. 9–10, fr. 3019 ff. 73–74, and fr. 20506 f. 136, which copies fr. 2988 f. 9. Ranzo was a Vercelli nobleman at Charles V's court, of the family of Gattinara's mother.
   - An "Aditione nel zifra" survives as fr. 3022 f. 50, with a copy in Clairambault 314 f. 337. It shows how the code works: each group is the initial letter of a word plus a number, and the addition continues the base table past a326, b156, and so on.
   - All of these are undeciphered.
2. **Serno Gilino's letter (1527).** BL Cotton Vespasian C IV f. 214 (DECODE R8572) is a Latin letter from one Serno Gilino, 15 September 1527. Most of its superscripts are two-digit numbers. It is undeciphered.
3. **The Bishop of Worcester's cipher (1526–1529): solved except for one letter.** Girolamo Ghinucci, the Italian absentee bishop, wrote four Latin letters with passages in a syllabic cipher with superscripts: Vespasian C III f. 304 (R8476) and C IV ff. 313, 315 and 363 (R8589, R8590, R8613).
   - Andrew Aymeloglu pointed out on 18 September 2026 that the 1526 and February 1529 letters had been printed with their decipherments (*State Papers* VI, 1849; *Letters and Papers* IV no. 5282).
   - With those texts Tomokiyo completed the key on 21 September 2026. Its features: nulls; irregular superscripts; syllable symbols with alternative superscripts for proper names (n2 = Cesare, x1 = Hispania); word symbols that ignore case endings.
   - The fourth letter, 22 July 1529 (Vespasian C IV f. 363, R8613), "seemingly in the same cipher, still has many unidentified symbols and is deemed unsolved yet."

## What is unsolved
The plaintext of the coded passages in the Garbino letter and Ranzo's letters, the whole of Gilino's letter, and the 22 July 1529 Worcester-cipher letter.

The three are different problems:
- **Garbino/Ranzo** is a one-part code of several hundred word groups, keyed by initial letter. About two-thirds of the Garbino letter is in code. Bourdeau tested whether the numbers run in alphabetical order within each initial (the usual weakness of such codes). They do not (z = −0.5, against +6.5 for a genuinely alphabetical control).
- **Gilino** is a superscript cipher with no published reconstruction.
- **The Worcester residue** sits under a key that is now largely known, but its unread symbols are probably word signs and nulls.

## What survives
- **BnF:** the Garbino letter, the code-addition sheet, a jargon with cover names (fr. 3022 ff. 48–50), and six Ranzo pages, all digitized on Gallica (fr. 3022 = btv1b90601558).
  - Bourdeau has transcribed all 1,315 groups of the Garbino letter and about 2,600 groups from the Ranzo pages.
  - The two sets share 316 group types, which confirms they use one table. That gives about 3,900 groups, with roughly 550 group types in the Garbino letter and 730 in Ranzo's.
- **BL Cotton Vespasian:** the four Worcester-cipher letters and Gilino's letter, imaged on DECODE.
  - Tomokiyo has published a reconstructed Worcester key.
  - No transcription of Gilino's letter was found online.
  - The BL's own digitized-manuscripts viewer has been offline since 2023 (Unverified claims).

## Prior attempts and current consensus
- **Garbino/Ranzo:**
  - Tomokiyo identified the family and the addition sheet, and Norbert Biermann tied that sheet to Ranzo's code on Cipherbrain in 2017.
  - In September 2026 Bourdeau ran an annealer over all ~3,900 groups. It assigned each group a word with the right initial and scored the result with a word-bigram model of Castiglione's and Guicciardini's Italian. It recovered function words stably (c170 che, i100 il, p149 per, n38 non, s233 sua). The content words, which occur only once or twice each, varied from restart to restart.
  - He found no crib: the Clairambault copy carries no decipherment, and no Ranzo page repeats the Garbino text.
  - His verdict: "No. 20 needs Ranzo's code table or a clear copy of one of his letters."
  - Bourdeau also reads the cover names (the Emperor is "Joan Jacobo") and the Ranzo connection as Imperial, not Venetian. The "Venetian?" label is Tomokiyo's provisional guess from the superscript form, and should not be taken as an attribution.
- **Gilino:** Tomokiyo lists it as undeciphered. No published attempt was found.
- **Worcester:** solved for three of four letters, by printed contemporary decipherments plus Tomokiyo's key. The fourth is open.

Read first: Tomokiyo's "Venetian Ciphers with Superscripts", "Bishop of Worcester's Latin Cipher with Superscripts", and "Ciphers during the Reign of Henry VIII", then Bourdeau's "Del Vasto to Charles V, and a letter to 'Garbino'".

## What a solution would have to do
- **Garbino/Ranzo:** produce one code table, respecting the initial-letter constraint, that gives continuous, period-plausible Italian across the Garbino letter and all the Ranzo letters at once. It must hold for the content words, not only the function words.
  - The decisive checks are a recovered key (a Ranzo code sheet in Simancas, Vienna or the Gattinara papers) or a cleartext or calendar copy of any one Ranzo letter.
  - Bourdeau's control shows that a fluent-looking content-word reading produced by the annealer alone proves nothing.
- **Gilino:** a key that reads the whole letter in Latin consistent with English diplomacy in late 1527.
- **Worcester residue:** extend Tomokiyo's key so that f. 363 reads as Latin consistent with July 1529 (the Legatine court and the Cambrai negotiations). Symbols newly assigned there must recur sensibly or be justifiable nulls.

## Why the scores
- **mystery 2:** unread passages of minor Imperial and English diplomatic correspondence of 1527–29. They are of real interest to specialists (Gattinara's circle, the Sack of Rome aftermath), but no known historical question hangs on them.
- **material 4:** everything survives whole and is imaged (Gallica for the BnF items; DECODE for Vespasian). Bourdeau's transcription covers the Garbino/Ranzo corpus. Not 5: there is no transcription of Gilino, and the BL's own viewer is down.
- **solvable 5:** state diplomatic codes used consistently, with a surviving addition sheet that explains the design.
- **compute 3:** this could have gone to 4 for the two smaller items, but the core item is code, not cipher. Bourdeau's well-built annealer with a period language model hit the ceiling: about 550 types, half used once, with non-alphabetical numbering. Computation fixes the function words and can rank candidates. The content needs a key or a crib, which is an archival search. Gilino and the Worcester residue are better suited to hill-climbing and context work, but they are small.
- **verifiable 4:** a found key or a cleartext copy would verify mechanically. Without one, a code reading of hapax words can only be judged by plausibility, so not 5.
- **crowding 4:** Tomokiyo, Biermann and Bourdeau have worked the main item. Gilino seems untouched.
- **compute mode:** ENUMERATE plus archival SEARCH · verifier MECHANICAL if a key or crib is found, otherwise PLAUSIBILITY · signal PARTIAL (function words) · fit MEDIUM.

## Sources
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Unsolved Historical Ciphers," §Italian/Latin (1520s), with September 2026 updates. https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Venetian Ciphers with Superscripts" (the Garbino and Ranzo sections; the addition sheet). https://cryptiana.web.fc2.com/code/venetian.htm
- SECONDARY — S. Tomokiyo, "Bishop of Worcester's Latin Cipher with Superscripts (1526, 1529)," posted 21 Sept 2026 (printed decipherments; the updated key; the fourth letter unsolved). https://cryptiana.web.fc2.com/code/worcester.htm
- SECONDARY — S. Tomokiyo, "Ciphers during the Reign of Henry VIII" (the Gilino letter, Vespasian C IV f. 214, R8572). https://cryptiana.web.fc2.com/code/henryviii.htm
- CLAIMANT — D. Bourdeau, "Del Vasto to Charles V, and a letter to 'Garbino', 1527–28," posted 18 Sept 2026 (the Clairambault copy, the alphabetical-order test, the annealer result, the needed key). https://dbourdeau.github.io/cyphersolver/vasto1527.html
- PRIMARY — BnF fr. 3022 on Gallica (the Garbino letter at f. 44, the addition sheet at f. 50). https://gallica.bnf.fr/ark:/12148/btv1b90601558
- SECONDARY — *Letters and Papers, Foreign and Domestic, Henry VIII*, vol. 4 (British History Online), no. 5282 (the February 1529 Worcester letter deciphered). https://www.british-history.ac.uk/letters-papers-hen8/vol4

## Unverified claims
- That no one has deciphered Gilino's letter or the 22 July 1529 letter after 21 September 2026. Tomokiyo's notice says solutions are arriving faster than he records them. No Bourdeau or Aymeloglu write-up for either was found, and a web search for Gilino found nothing.
- Whether a decipherment of the 22 July 1529 letter is printed in *Letters and Papers* IV or *State Papers* VII. Not checked.
- The identity of "Serno Gilino" (possibly a corrupt form of a known Italian agent's name). Not researched.
- Whether Ranzo's code table survives in Simancas, Vienna or Vercelli. Bourdeau names this as the breach; no one has reported searching for it.
- That the BL digitized-manuscripts viewer is still offline (Bourdeau reports "BL offline" for a sibling item). Not independently checked for Vespasian C III/IV.
