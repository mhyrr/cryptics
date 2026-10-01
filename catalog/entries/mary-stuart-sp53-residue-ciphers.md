+++
title = "Unsolved residue of the Mary Stuart cipher papers, TNA SP 53 (Tempest and Barret letters, 'Spanish spy'), c. 1585"
slug = "mary-stuart-sp53-residue-ciphers"
kind = "cipher"
era = "c. 1585"
origin = "English Catholic exile network (Paris and Rheims), intercepted by Walsingham's office; TNA SP 53"
language = "unknown (French clear lines; English, French or Latin plaintext likely)"
status = "unsolved"
confidence = "medium"
digitized = "https://cryptiana.web.fc2.com/code/mary3.htm"
tags = ["numerical", "nomenclator", "letters", "Elizabethan", "Mary-Queen-of-Scots", "Phelippes", "Cryptiana", "needs-crib"]

[scores]
mystery = 2
material = 4
solvable = 4
compute = 4
verifiable = 5
crowding = 3
+++

# Unsolved residue of the Mary Stuart cipher papers, TNA SP 53, c. 1585

## What it is
Three enciphered pieces in The National Archives' SP 53, Walsingham's office papers concerning Mary, Queen of Scots. All three are still undeciphered after the 2023–2026 work on their neighbours.

| Piece | What it is | Tokens (Bourdeau's count from Tomokiyo's transcription) |
|---|---|---|
| SP 53/16 no. 78 (1585?) | Anonymous letter in cipher to "Mr Tempest", an English priest in Paris. Clear lines in French; endorsed by Thomas Phelippes | 507 numbers, 132 distinct (range 1–141) |
| SP 53/16 no. 79 (1585?) | Anonymous letter in the same hand as no. 78, to Dr Richard Barret, President of the English College at Rheims; endorsed by Phelippes | 644 (+27 illegible), 102 distinct, some with letter variants |
| SP 53/22 f. 52 | Short ciphertext endorsed "Cifer with[?] Spanish Spye" | 84 tokens, 22 distinct |

Tomokiyo also notes a short undeciphered ciphertext on the verso of the cipher key at SP 53/22 f. 40.

This entry is distinct from `mary-stuart-cipher-letters`. That one is a solved calibration case: Mary's own letters to Castelnau in the BnF, in her symbol cipher. These pieces are numeric ciphers of the English Catholic exiles around her.

## What is unsolved
The plaintext of all three pieces, and whether nos. 78 and 79 share a key.

## What survives
- The originals are in TNA SP 53. Images are online only through the subscription *State Papers Online*.
- Satoshi Tomokiyo has transcribed all three. His files `SP53_16_78.txt` and `SP53_16_79.txt` are linked from *Cryptiana*; the f. 52 transcription is printed on his list.
- No contemporary decipherment is known. Both letters are endorsed by Phelippes, Walsingham's decipherer, so his reading may survive elsewhere in SP 53, as the plaintexts of the siblings did.

## Prior attempts and current consensus
**The siblings, solved.** Five sibling ciphertexts from the same Tomokiyo list were solved in 2023 by George Lasry, Norbert Biermann and Tomokiyo, and published in 2026: SP 53/11 no. 50, SP 53/16 no. 28(3), no. 29(2), no. 29(3), and SP 53/18 no. 64. For no. 28(3) and no. 64 the plaintext was afterwards found in the archive itself: Biermann found no. 28(3)'s in SP 53/17/74, and no. 64 matches SP 53/18/26(2). Biermann attributes no. 28(3) and no. 29(3) to William Allen at Rheims. Tomokiyo notes "there is some possibility that the plaintext for the following pieces may also be found."

**Bourdeau's attack, September 2026.** Daniel Bourdeau worked over three sessions, from the transcriptions alone, since no images were available.
- The published Mary–Castelnau keys do not apply, and Tomokiyo had already tried the neighbouring SP 53/22 keys without success.
- His ciphertext-only pipeline reads clean 507- and 1,151-token controls, including a control with word-signs.
- No. 78 shows no language basin in English, French, Latin, Italian or Spanish, and no. 79 scores at random level.
- Pooling the two scores worse than either alone, so he withdrew his earlier claim that they share a key.
- He leaves "nulls plus nomenclator" open as a design his controls do not read at this length.
- He judges f. 52 too short to have a unique solution.
- He concludes that solving them "needs the images and the SP 53/22 keys."

**Consensus:** open. The failure of ordinary homophonic attacks points either to a heavier nomenclator, nulls, or transcription problems, and not to meaninglessness.

## What a solution would have to do
- Recover one key, or two keys if nos. 78 and 79 are separate, that reads each letter continuously in a language fitting the clear French lines and the Paris–Rheims exile context of c. 1585.
- Any nulls or nomenclator entries it posits must be used consistently, not invoked ad hoc.
- The strongest proof would be a match against a plaintext or Phelippes decipherment found in SP 53, the route that settled two of the siblings.
- For f. 52 (84 tokens), only a key found in SP 53/22 or a matching plaintext can count. A ciphertext-only reading of 84 tokens cannot be accepted.

## Why the scores
- **mystery 2:** intercepted exile correspondence from the run-up to the Babington plot. It is of real interest to specialists. It could rise to 3 if the content touched the plot or Mary's betrayal by Morgan, the theme of sibling no. 29(3).
- **material 4:** whole letters of 507 and 644 tokens, transcribed. This could have been 3: the images are paywalled, and Bourdeau suspects the transcription itself may be part of the problem.
- **solvable 4:** state-era intercepts endorsed by Walsingham's decipherer, in the same family as solved siblings. Not 5, because the cipher design is unknown and the attacks so far found no language signal.
- **compute 4:** 1,151 tokens is enough for hill-climbing with nulls and nomenclator models. A systematic sweep of SP 53 for matching plaintexts (the route that solved two siblings) is the obvious computational-plus-archival move. Not 5, because the data needs re-checking against the images first.
- **verifiable 5:** a reading that matches a plaintext surviving in SP 53, or that reads continuously, is a mechanical check.
- **crowding 3:** Tomokiyo, Lasry, Biermann and Bourdeau have all worked this cluster, and the obvious approaches (published keys, standard homophonic hill-climbing) have been tried.
- **compute mode:** ENUMERATE (nulls + nomenclator) plus archival SEARCH for plaintext · verifier MECHANICAL · signal NONE so far · fit MEDIUM.

## Sources
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Solution of Ciphered Letters Related to Mary, Queen of Scots," posted 16 Sept 2026 (the solved siblings, the plaintexts found in SP 53, and nos. 78 and 79 undeciphered, with transcriptions). https://cryptiana.web.fc2.com/code/mary3.htm
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Unsolved Historical Ciphers," §English, "More Undeciphered Letters Related to Mary, Queen of Scots" (no. 78, no. 79, and SP 53/22 f. 52 with its transcription). https://cryptiana.web.fc2.com/code/unsolved.htm
- CLAIMANT — D. Bourdeau, cyphersolver `targets/sp53/` NOTES.md (statistics, controls, the three failed sessions, the same-key claim withdrawn). https://github.com/dbourdeau/cyphersolver/tree/main/targets/sp53/
- CLAIMANT — D. Bourdeau, write-ups index entry "SP 53/16 nos. 78-79 and SP 53/22 f. 52 … not solved." https://dbourdeau.github.io/cyphersolver/writeups.html

## Unverified claims
- The 1585 dating of nos. 78 and 79. Tomokiyo marks it with a query.
- That a Phelippes decipherment or plaintext of nos. 78 and 79 survives in SP 53. This is suggested by the siblings, not established.
- The identification of "Doctor Barret" as Richard Barret, President of the English College at Douai/Rheims from 1588. Tomokiyo gives "Doctor Barret, President of the English seminary at Rheims", and the first name is not in the source. If the letter dates to 1585, Barret was not yet President, so either the date or the title needs checking.
- That nothing has been solved since Bourdeau's sessions of mid-September 2026.
