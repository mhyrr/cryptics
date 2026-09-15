+++
title = "Zodiac cipher Z340 (solved 2020) — calibration case"
slug = "zodiac-z340"
kind = "cipher"
era = "sent 8 November 1969; solved 5 December 2020"
origin = "San Francisco Bay Area, California"
language = "English"
status = "solved"
confidence = "high"
digitized = "http://zodiackillerciphers.com/"
tags = ["calibration", "solved", "homophonic", "transposition", "hill-climbing", "AZdecrypt", "Zodiac"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 1
+++

# Zodiac cipher Z340 (solved 2020) — calibration case

## What it is
A 340-character homophonic cipher mailed to the *San Francisco Chronicle* on 8 November 1969 by the Zodiac killer, in seventeen rows of twenty symbols. It followed the 408-character cipher of 31 July 1969, which Donald and Bettye Harden of Salinas — neither of them cryptologists — solved within days by guessing that the word "KILL" would appear and using it as a crib. Z340 then resisted every attempt for fifty-one years, including by NSA and FBI analysts and by the strongest amateur community in the field. It was solved on 5 December 2020 by David Oranchak (a software engineer in Virginia), Sam Blake (a mathematician in Australia) and Jarl Van Eycke (a Belgian programmer, author of the AZdecrypt solver). The FBI's Cryptographic and Racketeering Records Unit confirmed the solution and stated it gave no further clue to the killer's identity.

## What is unsolved
Nothing about the cipher. The entry is here as a calibration case, per the rubric's requirement to keep solved cases in `entries/` so the scoring can be checked against known outcomes. The residual open questions are historical, not cryptographic: the killer's identity, and why he chose an unusual encipherment scheme for Z340 after a plain homophonic substitution in Z408.

## What survives
The letter and cipher as mailed, in police and FBI custody, with high-quality reproductions public. The transcription has been exact and machine-readable for decades — this was never a material problem. The solution package is unusually complete: Blake's search methodology, Van Eycke's AZdecrypt solver, Oranchak's write-ups and video explanation, and the plaintext with its idiosyncratic spelling preserved. This is the best-documented modern cipher break in the catalog and the right thing to read before trusting any claim about any other entry here.

## Prior attempts and current consensus
Fifty-one years of failure by capable people, and the reason for that failure is the interesting part. Z408 was a straight homophonic substitution and fell to a crib in three days. Z340's symbol frequencies also looked homophonic, so the field attacked it as one — and it is one, but only after an unconventional transposition is undone. Blake enumerated candidate transposition schemes (period-19 diagonal reading patterns among them), generating on the order of 650,000 variant arrangements, and ran each through AZdecrypt's hill-climbing homophonic solver scored against English n-gram statistics. One arrangement produced English. The killer had also enciphered the text in three separate blocks with a shifting scheme, and made at least one encipherment error — so the plaintext is imperfect, which is itself part of why partial hits had been dismissed as noise for decades. Two lessons the rubric should absorb: a wrong structural assumption can hold for fifty years against unlimited effort on a text that is fully digitized and only 340 characters long; and the break came from systematically enumerating the *structural* hypothesis space, not from a better substitution solver.

## What a solution would have to do
Historical interest only, but state it for the record, since this is the calibration standard against which other entries' "What a solution would have to do" sections should be judged: specify the transposition and the homophonic key, decrypt all 340 characters to English, have the plaintext continue the documented voice and preoccupations of the Z408 plaintext, reproduce the author's characteristic misspellings, and be reproducible by a third party from a published solver and a published arrangement. Z340's solution met every one of these, and was then independently reproduced and officially confirmed. That is what a met bar looks like.

## Why the scores
Scored as of the day before the break (4 December 2020), which is the point of a calibration case.
- mystery 1: scored today, the central question is resolved; residual mystery is about the killer, not the cipher. On 4 December 2020 this would have been 4.
- material 5: complete text, exact public transcription, machine-readable for decades.
- solvable 5: near-certain — the author sent it as a message and his previous cipher had decoded cleanly.
- compute 5: the core question was computational (enumerate transpositions, hill-climb the substitution, score with n-grams), the data was ready, and success was mechanically checkable. A correctly calibrated rubric had to say 5 here in 2019, and this is the test of that.
- verifiable 5: English or not; independently reproduced; FBI-confirmed.
- crowding 1: the most-attacked unsolved cipher of its era. Note that crowding 1 did not prevent the break — which is a warning against over-weighting this axis.

## Sources
- PRIMARY/SCHOLARLY — David Oranchak, "Let's crack Zodiac" and the Z340 solution write-up, zodiackillerciphers.com. http://zodiackillerciphers.com/
- SCHOLARLY — Sam Blake, Jarl Van Eycke, David Oranchak, "A mathematical analysis of the Zodiac Killer's 340-cipher" (methodology of the transposition enumeration). https://arxiv.org/abs/2103.03072
- PRIMARY — Jarl Van Eycke, AZdecrypt solver. http://www.zodiackillersite.com/viewtopic.php?f=81&t=3198
- SECONDARY — Wikipedia, "Zodiac Killer" (8 November 1969 mailing; 5 December 2020 solution; the three solvers; ~650,000 candidate arrangements; FBI CRRU confirmation). https://en.wikipedia.org/wiki/Zodiac_Killer
- SCHOLARLY — Craig P. Bauer, *Unsolved!* (Princeton UP, 2017): the pre-solution state of the art, useful for calibration. https://press.princeton.edu/books/hardcover/9780691167671/unsolved

## Unverified claims
- The arXiv identifier and exact title of the Blake/Van Eycke/Oranchak methodology paper were not confirmed at the publisher; the citation above should be checked before reuse.
- "650,000 possible solutions tested" is the figure in the encyclopedic account; whether it counts transposition arrangements, solver restarts, or something else was not established.
- The period-19 diagonal reading description of the transposition is from general accounts of the solution and was not read off Oranchak's write-up directly.
- The exact number and location of the killer's encipherment errors in Z340 were not verified.
- The claim that three separate blocks were enciphered with a shifting scheme was not verified against a primary description.
