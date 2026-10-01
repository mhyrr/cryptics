+++
title = "Throckmorton's marginal code (1559) and John Wod's line to Cecil (1568), BL Add MS 4136"
slug = "throckmorton-wod-ciphers"
kind = "cipher"
era = "1559, 1568"
origin = "Paris (English embassy) and the Scottish envoy at Elizabeth's court; copies in the Forbes papers, British Library"
language = "English (margin, presumed); Scots or English (Wod line, presumed)"
status = "unsolved"
confidence = "medium"
digitized = "https://de-crypt.org/decrypt-web/RecordsView/2988"
tags = ["code", "nomenclator", "letters", "diplomatic", "Elizabethan", "Cryptiana", "DECODE", "short-ciphertext", "needs-crib"]

[scores]
mystery = 2
material = 3
solvable = 4
compute = 2
verifiable = 4
crowding = 4
+++

# Throckmorton's marginal code (1559) and John Wod's line to Cecil (1568)

## What it is
Two leaves in BL Add MS 4136, part of Patrick Forbes's eighteenth-century working papers on Elizabethan diplomacy. Each carries a cipher that Satoshi Tomokiyo could not identify.

- **f. 32 (DECODE R2988).** Sir Nicholas Throckmorton's holograph letter to Elizabeth I from Paris, 10 July 1559, sixteen lines in his "Cipher 1". In the margin, about half the page, is a separate text of about 405 small signs in 222 groups, dated "… 8 … 1559".
- **f. 33 (DECODE R2989).** Throckmorton to Cecil, 8 August 1559, which reads with his "Cipher 3" and is printed in Forbes. At its foot is one line docketed "Mr John Wod to Secretary Cecil, 6 Sept 1568", of 39 signs.

## What is unsolved
Two things: the marginal text on f. 32 and the 39-sign Wod line on f. 33. The 10 July letter itself was decrypted at about 85–90% by Daniel Bourdeau in September 2026, using Tomokiyo's Cipher 1 key with seven corrections. Twelve of its code signs are still open.

## What survives
Both leaves are imaged on DECODE.
- **Margin:** Bourdeau has transcribed it sign by sign. It has about 29 base shapes and about 80 shape-and-dot combinations, with "/" and "//" as clause marks. One boxed group occurs four times and is probably a name.
- **Wod line:** Bourdeau has transcribed it too: 39 signs, 16 distinct, in the symbol family of the Moray–Wood cipher of July 1568 (see `moray-wood-cipher`) but under a different key.
- **Probable cribs:**
  - For the margin, the original despatches of 8 July 1559 (TNA SP 70/5; CSP Foreign I nos. 947, 950). They are available only through the subscription State Papers Online.
  - For the Wod line, the Hatfield original of the letter (Cecil Papers vol. 1). Bain prints it in CSP Scotland II no. 804 and marks one phrase as cipher.

## Prior attempts and current consensus
- **Tomokiyo** reconstructed Throckmorton's Ciphers 1–3 from Add MS 4136 and Add MS 35830 and listed these two as "yet unidentified".
- **Bourdeau** (posted 21 Sept 2026, updated 24 Sept) closed both without a decryption.
  - **The margin.** Taken as words, its 222 tokens give 141 types and 113 once-only types. That matches 222-word stretches of English calendar prose (median 140 and 107). Its groups average 1.9 signs, where letter-for-letter English would give about 4.3. The signs change value with the position of their dots. So it is a word-sign code or shorthand, like Thomas Smith's 1563 dotted-letter code. 51% of the tokens are signs used once, "which the ciphertext alone cannot determine."
  - **The Wod line.** An exhaustive alignment against Bain's cipher phrase failed. Simulated annealing from 200 random starts produced 92 mutually different "English" decryptions that all fit better than real text. The line is below unicity: it has no unique solution from its own text.

Current position: open, and blocked by missing evidence, not by method.

## What a solution would have to do
- **Margin:** produce a word-sign table under which the whole margin reads as coherent English, with each sign keeping one meaning (allowing for its dot positions). The reading must also coincide in substance with the 8 July 1559 despatches. Coincidence with an independent plaintext is the only convincing test, because half the tokens are hapaxes.
- **Wod line:** match the cipher phrase in the Hatfield original or its contemporary decipherment, or use a key shared with another dated Wood letter. A reading obtained from the 39 signs alone cannot be accepted, since dozens of decryptions fit equally well.

## Why the scores
- **mystery 2:** two short pieces of 1559 and 1568 diplomatic traffic whose context is largely known from calendars.
- **material 3:** both survive whole and imaged on DECODE, with transcriptions. But the Wod line is only 39 signs, and the cribs needed to read either piece are not freely online.
- **solvable 4:** clearly purposeful systems. The margin has word-code statistics, and the Wod line belongs to a documented Scottish symbol family. Not 5, because the margin's design (code or shorthand) is inferred.
- **compute 2:** this could have been 3. Computation has already done its useful work here: it measured that ciphertext-only cannot succeed (margin hapax rate; Wod non-uniqueness). The breach is archival (SP 70/5, Hatfield). Once a crib is in hand, aligning it is mechanical.
- **verifiable 4:** given a crib, verification is mechanical. Without one, nothing can be verified.
- **crowding 4:** treated by Tomokiyo and Bourdeau only.
- **compute mode:** CRIB-ALIGN after archival SEARCH · verifier MECHANICAL given the crib · signal NO from ciphertext alone · fit LOW.

## Sources
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Unsolved Historical Ciphers," §English, "Nicholas Throckmorton (1559) / John Wod (1568)." https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Ciphers during the Reign of Queen Elizabeth I" (Throckmorton's Ciphers 1–3; "Unidentified Ciphers in Add MS 4136"). https://cryptiana.web.fc2.com/code/elizabeth.htm
- CLAIMANT — D. Bourdeau, "Throckmorton to Elizabeth I, 10 July 1559, the marginal code, and John Wood to Cecil, 1568," posted 21 Sept 2026, updated 24 Sept 2026 (the partial decryption of the letter; the word-code statistics; the Wod non-uniqueness test; the cribs needed). https://dbourdeau.github.io/cyphersolver/wod1568.html
- PRIMARY — BL Add MS 4136 f. 32 and f. 33, images via DECODE R2988 and R2989. https://de-crypt.org/decrypt-web/RecordsView/2988 · https://de-crypt.org/decrypt-web/RecordsView/2989
- SECONDARY — J. Bain (ed.), *Calendar of State Papers relating to Scotland* II (1900), no. 804 (the Wood letter, with one phrase marked as cipher). Cited via Bourdeau, not fetched.

## Unverified claims
- That the margin copies the 8 July 1559 despatches. This is Bourdeau's inference from the date line and the letter's text, and is untested.
- That the Hatfield original of Wood's letter carries a decipherment. Unknown.
- That neither item has been solved since 24 September 2026. Not checked beyond Bourdeau's index and Tomokiyo's list.
- Whether "John Wod" (1568) is the same John Wood who received Moray's cipher letter of July 1568. Bourdeau's same-family observation suggests so; not confirmed here.
