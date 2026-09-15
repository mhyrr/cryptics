+++
title = "D'Agapeyeff challenge cipher (1939)"
slug = "dagapeyeff-cipher"
kind = "cipher"
era = "1939"
origin = "London (Alexander D'Agapeyeff, Codes and Ciphers, 1st ed.)"
language = "presumably English"
status = "unsolved"
confidence = "medium"
digitized = "https://en.wikipedia.org/wiki/D%27Agapeyeff_cipher"
tags = ["challenge-cipher", "Polybius", "nulls", "author-forgot-key", "short-ciphertext", "20th-century"]

[scores]
mystery = 1
material = 2
solvable = 3
compute = 4
verifiable = 2
crowding = 2
+++

# D'Agapeyeff challenge cipher (1939)

## What it is
A short numeric cryptogram printed as a challenge at the end of the first edition of *Codes and Ciphers: A History of Cryptography* (1939) by Alexander D'Agapeyeff, a Russian-born English cartographer and popular writer on cryptography. Eight lines of ten five-digit groups, all digits, beginning `75628 28591 62916 48164 91748 58464 74748 28483 81638 18174` and ending `82858 47582 81837 28462 82837 58164 75748 58162 92000`. It was removed from subsequent editions of the book. D'Agapeyeff is reported to have admitted later that he had forgotten how he encrypted it.

## What is unsolved
The plaintext, and quite possibly the question is malformed. Three obstacles compound. (1) Length: the encyclopedic reading treats this as a 196-character message, which is short. (2) Nulls: the digits appear to be read as pairs horizontally, giving an index of coincidence of 1.812 in pairs, while the resulting letter-frequency distribution is too flat for a 196-character English message — the natural explanation, and one D'Agapeyeff himself recommends in the book, is that a proportion of the characters are dummies inserted after encipherment ("if every third, fourth, or fifth letter … is a dummy inserted after a message has been put into cipher, it is then extremely difficult to decipher"). (3) The author's own admission that he lost the method means there is no key to recover from anywhere, and no way to confirm a solution by asking. A fourth possibility that the community takes seriously and this catalog should record: that the printed digits contain a typesetting or transcription error, in which case the ciphertext as published may not decrypt at all.

## What survives
Only the printed ciphertext, from the 1939 first edition, and the book around it — which is the most underused resource. D'Agapeyeff's *Codes and Ciphers* is a teaching text: it works Polybius-square examples, discusses null insertion, and generally documents the toolkit its author had in mind in 1939. Any serious attack should be a reading of the book as the key to the cipher rather than a blind search. First editions are scarce but the ciphertext is everywhere, exactly transcribed, and trivially machine-readable.

## Prior attempts and current consensus
It has been a standard target of the amateur cryptographic community for eighty-odd years, features in the classic unsolved-cipher lists, and has resisted. There is no substantial scholarly literature — no *Cryptologia* paper that I could locate establishing its structure — and the working consensus is a shrug: probably a Polybius or checkerboard substitution with nulls, possibly corrupt, definitely underdetermined. It is worth noting that the D'Agapeyeff cipher's reputation for difficulty may be mostly an artifact of the null hypothesis: if a third or a fifth of the characters are meaningless, the effective plaintext is well under 150 characters and the search space over "which positions are nulls" multiplies out fast.

## What a solution would have to do
Because the author lost the key and may have miscopied the text, internal coherence is the only available criterion, and it must be strong. A solution should: (1) state the null-insertion rule and the substitution together, as one system, and derive both from methods D'Agapeyeff actually teaches in *Codes and Ciphers* — a system he never mentions is a much weaker claim; (2) produce grammatical, idiomatic 1939 English with no discretionary letter choices, and of a content plausible as an author's challenge (a self-referential message, a quotation, a dedication); (3) explain the terminal `92000`, which looks like padding and is the one structural feature the ciphertext hands you; (4) account for the flat letter-frequency distribution under its own hypothesis rather than invoking nulls ad hoc wherever the reading breaks. If the solution requires emending printed digits, it must say exactly which and why, before decoding. The negative result is also worth having and is achievable: an exhaustive search over checkerboard/Polybius systems crossed with regular null-insertion patterns, scored by English n-gram statistics, would either find it or establish that no system in that family works — which would turn the transcription-error hypothesis from a guess into a conclusion.

## Why the scores
- mystery 1: nobody's picture of anything changes. This is a puzzle-book challenge, and its interest is purely methodological.
- material 2: a couple of hundred characters from a single printed source that may be corrupt.
- solvable 3: the author certainly enciphered something, so intent is certain; but with the key lost, possible nulls, and possible typesetting corruption, whether a determinate plaintext is recoverable from this evidence is genuinely open.
- compute 4: this is the best pure-search target in the catalog relative to its fame. The hypothesis family is small and enumerable — digit-pair Polybius variants crossed with periodic null patterns — and the search is cheap in 2026. Not 5 because a corrupt ciphertext would defeat any search and there would be no way to tell.
- verifiable 2: only by plausibility. No key, no author, no external corroboration; a grammatical 196-character English reading would be persuasive but competing readings could survive, especially with free choice of nulls.
- crowding 2: a long amateur history and many failures, but no serious published cryptanalysis and, as far as I can establish, no exhaustive modern search.

## Sources
- PRIMARY — Alexander D'Agapeyeff, *Codes and Ciphers: A History of Cryptography* (Oxford University Press, 1939), 1st edition, challenge cipher on the final page.
- SECONDARY — Wikipedia, "D'Agapeyeff cipher" (the full ciphertext, eight lines of five-digit groups, "196 character message," index of coincidence 1.812 in horizontal pairs, the flat frequency distribution, the null-insertion quotation from the book, D'Agapeyeff's reported admission that he forgot the method). https://en.wikipedia.org/wiki/D%27Agapeyeff_cipher
- SECONDARY — Wikipedia, "List of ciphertexts": D'Agapeyeff cipher (1939) listed as "Unsolved." https://en.wikipedia.org/wiki/List_of_ciphertexts
- SCHOLARLY — Craig P. Bauer, *Unsolved!* (Princeton UP, 2017), which treats the standard 20th-century challenge ciphers. https://press.princeton.edu/books/hardcover/9780691167671/unsolved

## Unverified claims
- The character count. The encyclopedic source says "196 characters arranged in groups of five digits," which is internally awkward: eight lines of ten five-digit groups is 400 digits, i.e. 200 digit-pairs, and 196 is not a multiple of five. The most likely reading is 196 or so plaintext characters recovered from ~400 digits read as pairs with padding at the end, but this was not resolved. Anyone computing statistics must fix this first.
- Whether the ciphertext as printed is complete and correct. The transcription-error hypothesis is widely repeated in the amateur literature; the encyclopedic article "does not explicitly discuss the possibility of transcription errors," and no collation against a first edition was done here.
- The exact wording and source of D'Agapeyeff's reported admission that he forgot his method. Reported as "is said to have admitted"; no primary citation found.
- That the cipher was removed from later editions is stated in the encyclopedic source; which edition first omitted it was not established.
- Whether the book uses a Polybius square in a way that specifically matches this ciphertext's digit-pair structure was not verified by reading the book.
- Whether any exhaustive modern search over Polybius-plus-nulls has in fact been published. I could not find one, which is not the same as there not being one.
