+++
title = "Ciphertexts left undeciphered by François Viète, 1594"
slug = "viete-undeciphered-ciphertexts"
kind = "cipher"
era = "February 1594"
origin = "France / Rome (Catholic League correspondence intercepted by Henri IV's cabinet)"
language = "French"
status = "partial"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b10033958p"
tags = ["homophonic", "symbol-cipher", "letters", "diplomatic", "french", "catholic-league", "viete", "cryptiana", "BnF", "Gallica", "hill-climbing"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 5
crowding = 4
+++

# Ciphertexts left undeciphered by François Viète, 1594

## What it is
BnF Cinq Cents de Colbert 33 is a volume of intercepted Spanish and Catholic League dispatches that are thought to have been deciphered by François Viète. It came from the historian de Thou's library and is titled "Dechiffres de Correspondance Espagnole, par M. Viette." Viète was the mathematician and Henri IV's codebreaker, famous for breaking the Spanish cipher of Commander Moreo (1589). Among the volume's deciphered copies are a few original letters of February 1594 that carry no decipherment, which suggests the cabinet failed to break them. Satoshi Tomokiyo lists two:

| Item | Folio | Status (Sept 2026) |
|---|---|---|
| Cardinal de Joyeuse to Villars, admiral of France, Rome, 15 February 1594 | f. 539 | **Unsolved.** It is in an unidentified symbol cipher. It does not read with the f. 530 symbol alphabet (used by Pelissier and Joyeuse), nor with a known Joyeuse–agent cipher |
| Sennecey (Claude de Bauffremont, League ambassador in Rome) to the Archbishop of Lyon, about February 1594 | f. 555 | **Solved.** George Lasry broke it by computer in 2020 and published it at HistoCrypt 2022. It is a homophonic cipher with 79 symbols, short text |

There is also a related sibling. Sennecey's letter to President Jeannin of 15 March 1594 (f. 575) and Pelissier's to Joyeuse (f. 528) are undeciphered in the volume, but they read with the f. 530 alphabet, so they are not open. Tomokiyo gives a partial reading of f. 575.

## What is unsolved
The plaintext of the Joyeuse letter to Villars, f. 539.

The entry exists apart from the general run of French dispatches because of the Viète angle. If it was in fact sent to Viète and not broken, a modern break is a direct calibration of 2020s methods against the best cryptanalyst of the 1590s. The f. 555 result already shows that kind of gap: a short, 79-symbol homophonic text that the cabinet left alone fell to Lasry's hill-climbing.

## What survives
- The whole volume is on Gallica, including f. 539, so the images are available.
- No transcription of f. 539 has been published. Tomokiyo's article catalogues the volume folio by folio and identifies the ciphers in use (Cp.38, Cg.13, the f. 530 symbol cipher).
- The decryption and key for f. 555 are in Lasry's HistoCrypt 2022 paper.

## Prior attempts and current consensus
- **In the 1590s**, the original was left without decipherment, as far as the volume shows.
- **Tomokiyo** (2020) catalogued the volume. He showed that f. 539 is not in the f. 530 alphabet or the known Joyeuse cipher.
- **Lasry** (2020 and 2022) solved f. 555. It is not recorded whether he attempted f. 539.
- **Bourdeau's** solved list (late September 2026) has no entry for f. 539.
- No reading has been claimed.

Newcomers should read Tomokiyo, "Ciphers Broken by François Viète"; Lasry, "Deciphering a Letter from the French Wars of Religion" (HistoCrypt 2022); and Pesic (1997) on Viète's method.

## What a solution would have to do
- Read f. 539 continuously in French, with one key.
- The content must fit Cardinal de Joyeuse's Rome mission of February 1594. That was the League's negotiation at the Curia after Henri IV's abjuration. It must also fit the deciphered February 1594 letters around it in the same volume: Joyeuse, Sennecey, Montpezat and Pelissier.
- Pass a short-text control: show the same solver recovering a known key on a synthetic text of the same length and symbol count.
- Ideally, find that a symbol shared with the f. 530 or f. 555 keys, or an interlinear gloss elsewhere in the volume, agrees with the recovered key.

## Why the scores
- **mystery 2.** One League dispatch. The Viète connection is a strong story and a good calibration point, but historically it is a single letter in a well-documented negotiation.
- **material 4.** The original is whole and digitized. It is one letter of unknown length, untranscribed, and it may be short.
- **solvable 5.** A League symbol cipher of a kind whose siblings (f. 530, f. 555) are solved.
- **compute 4.** A homophonic symbol cipher is what hill-climbing does well. Lasry's f. 555 break is the direct precedent. The text is short and needs transcribing first, so this is 4 and not 5. It could be 5 if f. 539 proves longer than f. 555.
- **verifiable 5.** Continuous French in a well-documented context is a mechanical check.
- **crowding 4.** Tomokiyo has catalogued it, and Lasry has probably looked at it. There is no other literature.

## Sources
- PRIMARY — BnF Cinq Cents de Colbert 33 (Gallica). https://gallica.bnf.fr/ark:/12148/btv1b10033958p
- SCHOLARLY — George Lasry, "Deciphering a Letter from the French Wars of Religion," *Proceedings of HistoCrypt 2022* (Sennecey, f. 555). https://ecp.ep.liu.se/index.php/histocrypt/article/view/402
- SECONDARY — S. Tomokiyo, Cryptiana, "Ciphers Broken by François Viète" (volume catalogue; ff. 528, 530, 539, 555, 575; "Ciphertexts Left Undeciphered by Viète"). https://cryptiana.web.fc2.com/code/viete.htm
- SECONDARY — S. Tomokiyo, Cryptiana, "Unsolved Historical Ciphers" ("One of Two Solved"). https://cryptiana.web.fc2.com/code/unsolved.htm
- SCHOLARLY — Peter Pesic, *Cryptologia* (1997), on Viète's cryptanalytic memoir (cited by Tomokiyo as "Pesic (1997)"; not fetched).

## Unverified claims
- **That Viète himself handled and failed on f. 539.** Tomokiyo writes "apparently left undeciphered by Viète". The volume being Viète's work rests on its title and the "F.V." marks on a few folios, not on any note on f. 539. Viète's documented service also tails off around this period: Tomokiyo's Q3 asks how long he continued.
- The length of f. 539 and its number of distinct symbols. Not checked from the images.
- Whether Lasry or others have attempted f. 539. If they have, and failed, that is evidence about the cipher, and it is not recorded.
- The full title of Pesic (1997), recalled as "François Viète, Father of Modern Cryptanalysis — Two New Manuscripts" (Cryptologia 21). Not fetched.
- That f. 539 remains unsolved after September 2026. A search of Bourdeau's index and the web found no solution.
