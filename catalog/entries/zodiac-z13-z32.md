+++
title = "Zodiac ciphers Z13 and Z32"
slug = "zodiac-z13-z32"
kind = "cipher"
era = "1970"
origin = "San Francisco Bay Area, California"
language = "presumably English"
status = "unsolved"
confidence = "medium"
digitized = "http://zodiackillerciphers.com/"
tags = ["Zodiac", "short-ciphertext", "unicity-distance", "criminal-case", "homophonic", "underdetermined"]

[scores]
mystery = 3
material = 3
solvable = 3
compute = 3
verifiable = 1
crowding = 1
+++

# Zodiac ciphers Z13 and Z32

## What it is
Two short ciphers sent by the Zodiac killer in 1970, in the aftermath of the two long ones. Z13 is thirteen characters, introduced in a letter postmarked 20 April 1970 by the line "My name is —" followed by the symbols. Z32 is thirty-two characters, sent 26 June 1970 with a Phillips 66 road map of the Bay Area on which a crossed circle was drawn over Mount Diablo; the accompanying letter said the cipher, combined with the map, would reveal where a bomb was buried, with instructions involving radians and inches from a magnetic-north baseline. No bomb was ever found.

## What is unsolved
Both, and probably permanently. The symbol sets overlap with those of the solved Z408 (July 1969) and Z340 (8 November 1969), so the alphabet is not the obstacle. Length is. Thirteen and thirty-two characters are far below the unicity distance for a homophonic substitution on a ~50-symbol alphabet: many plausible plaintexts fit, and the ciphertext cannot distinguish between them. David Oranchak, who led the team that broke Z340, has put the point bluntly — it is practically impossible to determine whether any candidate solution is correct. The open question is therefore not "what do they say" but "is there any evidence that could settle what they say," and the honest answer at present is no.

## What survives
Photographic reproductions of both letters and of the annotated Mount Diablo map, held by the San Francisco Police Department and the FBI and widely published; the symbol sequences are exactly transcribed and machine-readable at zodiackillerciphers.com, which is also the repository for the Z340 solution work. The Zodiac's full correspondence corpus — spelling habits, vocabulary, the misspellings that functioned as cribs in Z408 — is available and is the only external constraint anyone has. That is why `material` is 3 and not lower: the objects are fine; the texts are tiny.

## Prior attempts and current consensus
Thousands of proposed solutions exist for Z13 alone. Two are cited seriously as illustrations of the problem rather than as answers: Craig Bauer's reading as "ALFRED E NEUMAN" and Ryan Garlick's "DR EAT A TORPEDO," which between them show that a thirteen-character homophonic cipher can be made to say almost anything. For Z32, attempts have tried to combine the cipher with the map's radian-and-inches instruction; none has produced a location that survived a search. The consensus among the people who actually solved Z340 — Oranchak, Sam Blake, Jarl Van Eycke, whose December 2020 solution the FBI's Cryptographic and Racketeering Records Unit confirmed — is that Z13 and Z32 are underdetermined and that the community's effort is better spent elsewhere. This entry exists mainly as the negative-control companion to `zodiac-z340`: same author, same symbol repertoire, same tooling, and yet unbreakable, because the binding constraint is information content, not cleverness.

## What a solution would have to do
Bring information from outside the ciphertext, because there is not enough inside it. Three routes, in descending order of plausibility. (1) Establish the cipher *system* from the solved texts — Z340's transposition-plus-homophonic scheme and Z408's straight homophonic scheme — and show that exactly one plaintext of the right length is consistent with that system plus the author's documented spelling habits. This is the only internal route and it is probably not decisive. (2) For Z13, corroborate the name externally: a plaintext yielding a real name would have to be a person with a documented connection to the case, and the reading would have to be the unique consistent one under a system independently attested in Z408/Z340 — a bar no proposal has come close to. (3) For Z32, dig. A claimed decryption plus the map's stated procedure yields a specific location; the check is physical and was available in 1970 and is still available now. Any solution that requires a system not attested in the solved ciphers should be discarded, and any solution offered without a uniqueness argument — a demonstration that no other plaintext fits — is not a solution, it is a guess.

## Why the scores
- mystery 3: genuinely unresolved and consequential to an open homicide investigation, but the field's considered view is that they are unresolvable, which caps how "open" the question really is.
- material 3: the texts are complete and exactly transcribed, but 13 and 32 characters is all there is, and that limits every method.
- solvable 3: the author intended messages — he said what Z13 and Z32 contained — so intent is certain; but "a determinate meaning recoverable from this evidence" is the thing in doubt, and serious people say no.
- compute 3: exhaustive search is trivial and has been done exhaustively; computation's real contribution is the negative one of quantifying underdetermination, which is worth doing and mostly has been.
- verifiable 1: this is the score that defines the entry. For Z13 no internal criterion can recognize a correct answer, and any reading is as good as another. Z32 alone has a physical check, which is the only reason the rest of the entry is not hopeless.
- crowding 1: an enormous amateur literature, an active community, and every naive approach exhausted many times.

## Sources
- PRIMARY/SCHOLARLY — David Oranchak, zodiackillerciphers.com: exact transcriptions of Z13 and Z32, the Z340 solution, and the statistical arguments about short-cipher underdetermination. http://zodiackillerciphers.com/
- SECONDARY — Wikipedia, "Zodiac Killer" (Z13 in the 20 April 1970 letter; Z32 with the Mount Diablo map, 26 June 1970; Bauer's and Garlick's proposals; Oranchak's assessment; FBI confirmation of the Z340 solution). https://en.wikipedia.org/wiki/Zodiac_Killer
- SCHOLARLY — Craig P. Bauer, *Unsolved! The History and Mystery of the World's Greatest Ciphers* (Princeton UP, 2017), Zodiac chapters. https://press.princeton.edu/books/hardcover/9780691167671/unsolved
- PRIMARY — FBI, Zodiac Killer case file. https://vault.fbi.gov/

## Unverified claims
- The exact symbol inventory of Z13 and Z32 and how far it overlaps Z408 and Z340 was not recounted here; the overlap is reported from the standard accounts.
- The precise wording of the 26 June 1970 letter's radians-and-inches instruction was not transcribed from a primary image.
- Whether the original letters and map survive as physical objects in SFPD or FBI custody, as against photographic copies, was not confirmed.
- Craig Bauer's "ALFRED E NEUMAN" reading is attributed to him in the encyclopedic account; the venue in which he published or presented it was not verified.
- Ryan Garlick's "DR EAT A TORPEDO" reading: institutional affiliation and publication venue not verified.
- The count of Zodiac ciphers is given as four in the encyclopedic source (Z408, Z340, Z13, Z32); whether any other enciphered material in the correspondence corpus should count was not checked.
