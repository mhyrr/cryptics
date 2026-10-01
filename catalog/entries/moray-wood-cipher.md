+++
title = "Moray–Wood cipher, 1568 (partially read 2026, ending open)"
slug = "moray-wood-cipher"
kind = "cipher"
era = "1568"
origin = "Edinburgh: James Stewart, Earl of Moray, Regent of Scotland, to John Wood at Elizabeth's court"
language = "Scots"
status = "partial"
confidence = "medium"
digitized = "https://de-crypt.org/decrypt-web/RecordsView/8345"
tags = ["substitution", "homophonic", "letters", "diplomatic", "Scotland", "short-ciphertext", "Cryptiana", "DECODE"]

[scores]
mystery = 2
material = 2
solvable = 4
compute = 3
verifiable = 4
crowding = 5
+++

# Moray–Wood cipher, 1568 (partially read 2026, ending open)

## What it is
A four-line cipher postscript of 134 glyphs. It is on a clear-Scots letter from James Stewart, Earl of Moray, Regent of Scotland, to his secretary John Wood at Elizabeth's court, dated Edinburgh, 13 July 1568: BL Add MS 32091 ff. 213–214, the cipher on f. 213v (DECODE R8345). Satoshi Tomokiyo listed it as "Moray-Wood Cipher — A Scotch Diplomatic Cipher (1568)": "although the cipher seems simple, the short ciphertext is not deciphered."

## What is unsolved
The ending and the two person-signs. Most of the postscript is now read, but the solver's own status (partial) is more cautious than Tomokiyo's (solved), and this entry follows the solver.

Andrew Aymeloglu notified Tomokiyo of a solution on 19 September 2026, and Tomokiyo's list now marks the item "Solved" with "the last seven symbols remain unidentified." Aymeloglu's own write-up says "Partial · ending unresolved."

The reading:

> The suffering of [Q] remane in Carlyle, and sending haym of the Lord Fleming, hes done greit evil. Gif the [Q2] cummis haom thair, la??is na mair to s(p)il the haill e? oure freindis [seven signs].

The still-open points:
- the closing seven signs (conjecturally *knauis*, "know");
- the doubled sign (k or t: *lakkis* or *lattis*);
- a singleton after *haill*;
- the two person-signs, which are read as Mary from context alone.

## What survives
- The single original at the BL, imaged on DECODE R8345. The BL's own viewer has been offline since 2023 (Unverified claims).
- Tomokiyo's 2024 transcription, attached to DECODE.
- Aymeloglu's own glyph transcription, key and verification script.
- No contemporary decipherment or key has been found.
- A line by John Wood to Cecil of September 1568 (Add MS 4136 f. 33) uses the same glyph repertoire under a different key; see `throckmorton-wod-ciphers`.

## Prior attempts and current consensus
- **Bourdeau's failed attempt.** Working from the transcription, Daniel Bourdeau built a 5-gram Scots annealer that read 5 of 6 matched 134-letter controls. It gave no reading of the target in Scots, English, French or Latin. He judged the result "undetermined rather than excluded." His explanations: the passage is mostly names (border news), and 13% of genuine Scots windows score below the solver's false optimum. He said it needed the page or a second letter. His index still lists the item as "not solved".
- **Aymeloglu's solution.** He read the glyphs afresh from the page image and found a simple substitution with a few homophones and word-signs, written with word spacing. It gives 118 of 134 glyphs a cryptanalytic assignment (grade S), with a permutation control.
- **The historical fit.** The plaintext fits the date precisely:
  - Mary was moved from Carlisle to Bolton on 13–15 July 1568.
  - Lord Fleming, sent to Elizabeth in June, was back in Scotland in arms by 21 August.
- **Tomokiyo** accepted the solution.

Consensus: read in substance, with the ending and the person-signs conjectural. Classed here as partial.

## What a solution would have to do
Met, mostly:
- One substitution key reads the whole postscript as Scots of 1568.
- The key's values are attested in several words each.
- The content agrees with events datable independently to that week (Carlisle; Fleming's return).

Not met:
- The last seven signs read without an unexplained deletion.
- Independent confirmation from a key or a contemporary decipherment.

## Why the scores
Scored as it stands in October 2026.
- **status partial, not solved:** Aymeloglu himself grades the reading "partial; ending unresolved". The last seven signs, one doubled sign, a singleton and the two person-signs remain conjectural, and no key or contemporary decipherment confirms the reading. Tomokiyo's "Solved" label is recorded above but not adopted.
- **mystery 2:** a short postscript of the Scottish Regent about Mary's custody. Most of it is now read, but the unread residue (who [Q] and [Q2] are, and what "our friends" know) is the politically pointed part.
- **material 2:** one witness of 134 glyphs. The whole text survives, but it is short enough that its length limits any method, which is what defeated Bourdeau's annealer.
- **solvable 4:** a Regent's diplomatic cipher, clearly purposeful. Not 5, because the text is so short and probably full of names and word-signs.
- **compute 3:** this is the instructive point. In 2026 the rubric would have tempted a 5 ("simple cipher, language known"). In practice an expert's well-controlled Scots annealer on the transcription failed. The break came from a careful re-reading of the glyphs on the page image, with context (Carlisle, Fleming) and word spacing, and computation used as a check. For texts this short, compute should be scored 3, and the transcription is a suspect variable.
- **verifiable 4:** consistent Scots plus an exact historical fit is strong. But the text is short, with no key or crib, and the ending is still open, so not 5.
- **crowding 5:** only Tomokiyo, Bourdeau and Aymeloglu have worked it.
- **compute mode:** ENUMERATE plus manual glyph re-read · verifier STRONG-CRITERIA (historical fit) · space SAMPLABLE · signal WEAK at 134 glyphs · fit MEDIUM.
- **Lesson for the rubric:** two capable 2026 solvers got opposite outcomes on the same short text. One worked from a third-party transcription, the other from the image. On sub-200-glyph ciphers, the rubric's `compute` should not exceed 3, and `material` should be scored for length.

## Sources
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Unsolved Historical Ciphers," §English, "Moray-Wood Cipher (1568) Solved" (Aymeloglu's solution, 19 Sept 2026; the last seven symbols unidentified). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Ciphers during the Reign of Queen Elizabeth I," §Moray-Wood Cipher (description; transcription). https://cryptiana.web.fc2.com/code/elizabeth.htm
- CLAIMANT — A. Aymeloglu, "Regent Moray to John Wood, 13 July 1568" (reading, glyph table, grades, open points), 18 Sept 2026. https://aaymeloglu.github.io/unsolved-ciphers/moray-reading.html
- CLAIMANT — A. Aymeloglu, `unsolved-ciphers/moray-1568` (README with method, controls, failure log; transcription and key). https://github.com/aaymeloglu/unsolved-ciphers/tree/main/moray-1568
- CLAIMANT — D. Bourdeau, write-ups index, "Regent Moray → John Wood … not solved" (the failed annealer, with controls). https://dbourdeau.github.io/cyphersolver/writeups.html · notes at https://github.com/dbourdeau/cyphersolver/tree/main/targets/moray/
- PRIMARY — BL Add MS 32091 f. 213, via DECODE R8345 (images not redistributed). https://de-crypt.org/decrypt-web/RecordsView/8345

## Unverified claims
- That the solution has appeared anywhere peer-reviewed. It is published only as Aymeloglu's GitHub write-up, accepted by Tomokiyo. Its status is that of a CLAIMANT solution endorsed by a SECONDARY expert source.
- That Bourdeau's "not solved" entry predates Aymeloglu's solution and was simply not updated. The ordering is inferred, not confirmed.
- That the two person-signs mean Mary. This rests on context only, by Aymeloglu's own grading.
- That the BL images are offline. Taken from Bourdeau's "BL offline" note.
