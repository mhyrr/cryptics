+++
title = "Feynman ciphers (all three solved; #2 and #3 in 2023) — calibration case"
slug = "feynman-ciphers"
kind = "cipher"
era = "1940s (Los Alamos); circulated publicly from 1987"
origin = "Los Alamos, New Mexico, USA"
language = "English"
status = "solved"
confidence = "medium"
digitized = "https://codewarrior0.github.io/cipher-blog/2023/05/27/feynman-solved.html"
tags = ["calibration", "solved", "transposition", "alternating-substitution", "quotation-cipher", "Feynman", "recently-fallen"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 3
+++

# Feynman ciphers (all three solved; #2 and #3 in 2023) — calibration case

## What it is
Three ciphertexts given to Richard Feynman at Los Alamos by a colleague as a challenge; Feynman could not break them. The encipherer has never been identified, though Paul Olum is the usual candidate on grounds of his friendship with Feynman and his taste for elaborate pranks. The texts entered public circulation through a 1987 Usenet post by Chris Cole. Lengths: cipher #1, 380 characters; #2, 261; #3, 231.

## What is unsolved
Nothing, as of May 2023 — which is why this entry is here. Cipher #1 fell in 1987 to Jack C. Morrison of JPL: a 5×76 transposition, read by stepping back five positions from the end and repeating from each previous start, yielding the opening of the General Prologue of Chaucer's *Canterbury Tales* in Middle English, in the spelling of F. N. Robinson's 1933 edition. Ciphers #2 and #3 then held out for thirty-six more years and were on every standard list of unsolved ciphers. David Vierra solved both, announcing on 28 May 2023: each uses **two monoalphabetic substitution alphabets that alternate after every word, with every word of even length written in reverse**, the first word of each line or sentence using alphabet 1. Cipher #2 is A. E. Housman's 1896 poem "Terence, this is stupid stuff" ("Why, if 'tis dancing you would be…"); cipher #3 is the opening of Feynman's own 1953 paper on the lambda transition in liquid helium ("The behavior of liquid helium, especially below the lambda transition…"). Feynman's paper postdates Los Alamos, so the framing story's date needs revision — a fact the entry records because it is the kind of thing that falls out of a solution and that nobody notices until the cipher breaks.

## What survives
All three ciphertexts, exactly, in public, mirrored on dozens of sites since 1987 and machine-readable. Vierra's own technical write-up is published. This is the easiest material situation possible for a cipher: no manuscript, no transcription dispute, no provenance problem, born as text.

## Prior attempts and current consensus
Thirty-six years of sustained amateur attack on #2 and #3, including by people who had broken hard things. The reason they failed is the calibration lesson, and it is a different lesson from Zodiac 340's. Both #2 and #3 look like monoalphabetic substitutions and are attacked as such; their letter frequencies are roughly right. But because the cipher alternates between two alphabets on a *word* boundary — and word boundaries are not marked in the ciphertext — a hill-climbing solver fitting one alphabet gets a persistently mediocre score that never resolves, and the even-length word reversal scrambles what little structure survives. The winning move was to hypothesize a *word-synchronized* alternation, which is an unusual construction that no standard solver's hypothesis space contains. Consensus accepts both solutions: the plaintexts are identifiable published texts, which is verification of the strongest kind. Note that neither solution required large compute; it required the right structural hypothesis, and then the check was instant.

## What a solution would have to do
Met. The criteria, stated for calibration: name the system, decrypt the full ciphertext, and have the output be a *pre-existing published text* that can be matched word for word against a printed source — which all three ciphers satisfied (Chaucer via Robinson's edition, Housman, Feynman's own paper). Quotation ciphers have the cleanest verification of any cipher type, because the plaintext is externally attested and cannot be fitted. When cataloguing any other challenge cipher, this is the right question to ask first: *if the plaintext is a quotation, is there a corpus I can match it against?* An automated pipeline that takes candidate plaintexts and matches them against a large digitized-book corpus is the transferable tool, and it is cheap.

## Why the scores
Scored as of 2022, before #2 and #3 fell.
- mystery 1 today: all three solved. In 2022 this would have been 2 — famous within the community, consequential to nobody.
- material 5: exact public digital text, no transcription issues, 231–261 characters for the two hard ones.
- solvable 5: certainly enciphered, and #1 had already fallen to a clean quotation plaintext, so the family was known.
- compute 5: the core question was a structural search over cipher families with mechanical verification, on ready data. A correctly calibrated rubric had to say 5 in 2022. The break came from a human hypothesis rather than raw search, which is a caution: `compute 5` names where verification is mechanical and data is ready, not a guarantee that a machine finds it.
- verifiable 5: the plaintexts are published works; matching is word for word.
- crowding 3: a modest, energetic amateur literature and no professional monograph; the obvious approaches (monoalphabetic and standard polyalphabetic search) had all been tried, which is exactly why an unconventional structure survived.

## Sources
- PRIMARY — David Vierra, "The Feynman Ciphers, solved" (28 May 2023): method, alphabets, and both plaintexts. https://codewarrior0.github.io/cipher-blog/2023/05/27/feynman-solved.html
- SECONDARY — Nick Pelling, Cipher Mysteries, Feynman ciphers posts (origin, lengths 380/261/231, Morrison's 1987 solution of #1, Cole's Usenet post, Olum as candidate encipherer, Vierra's 2023 solution). https://ciphermysteries.com/?s=feynman
- PRIMARY — Chris Cole, 1987 Usenet post circulating the three ciphertexts (sci.crypt archives).
- PRIMARY — R. P. Feynman, "Atomic Theory of the λ Transition in Helium," *Physical Review* 91 (1953): the plaintext source of cipher #3. https://journals.aps.org/pr/abstract/10.1103/PhysRev.91.1291

## Unverified claims
- Vierra's write-up was not read directly; the URL above was reported by a secondary source and the method description is at that remove. The announcement date is given as 28 May 2023 with the blog path dated 27 May 2023, unreconciled.
- The attribution of cipher #1's solution to Jack C. Morrison of JPL, and of the 1987 circulation to Chris Cole, are from the same secondary source.
- Paul Olum as the encipherer is explicitly a conjecture in the source, not an established fact.
- Whether cipher #3's plaintext being Feynman's own 1953 paper means the ciphers were composed after 1953 rather than at Los Alamos in the 1940s. The inference is mine; no source addresses the chronology, and the standard origin story may simply be wrong.
- The exact *Physical Review* volume and page for Feynman's lambda-transition paper were not verified.
- Wikipedia's "List of ciphertexts" does not include the Feynman ciphers, so the "solved" status here rests on the Cipher Mysteries account and Vierra's blog, not on an encyclopedic or peer-reviewed source. A second independent confirmation would be worth getting before this entry is used as a calibration anchor.
