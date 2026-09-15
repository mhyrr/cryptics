+++
title = "Poe's cipher challenges and the \"W. B. Tyler\" ciphers (1839–1841, solved 1992 and 2000)"
slug = "poe-tyler-ciphers"
kind = "cipher"
era = "1839–1841; solved 1992 and 2000"
origin = "Philadelphia, USA"
language = "English"
status = "solved"
confidence = "medium"
digitized = "https://en.wikipedia.org/wiki/Edgar_Allan_Poe"
tags = ["Poe", "substitution-cipher", "calibration", "compute-calibration", "solved", "pseudonym"]

[scores]
mystery = 2
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 2
+++

# Poe's cipher challenges and the "W. B. Tyler" ciphers (1839–1841, solved 1992 and 2000)

## What it is
Between December 1839 and 1841 Edgar Allan Poe ran a public cryptanalysis stunt: he advertised in the Philadelphia paper *Alexander's Weekly (Express) Messenger* that readers should send him ciphers, and he published solutions, claiming to have broken everything submitted. He consolidated the campaign in the essay "A Few Words on Secret Writing" in *Graham's Magazine*, July 1841, and turned cryptography into fiction in "The Gold-Bug." In the course of the *Graham's* exchange two ciphers arrived from a correspondent signing "W. B. Tyler," which Poe printed and declined to solve, saying he lacked time. No W. B. Tyler has been identified, and Poe has long been suspected of having written them himself.

## What is unsolved
Nothing about the ciphers: both were broken, the first in 1992 and the second in 2000. What remains open is the authorship question — whether "W. B. Tyler" was Poe under a pseudonym — and it is a historical, not a cryptologic, problem. This entry is kept as a calibration case. It is the cleanest example in the catalog of the pattern the rubric is built to detect: a "famous unsolved text" that was unsolved only because nobody competent had seriously attacked a short classical cipher, and that fell to ordinary cryptanalysis plus one organized competition, within months of someone trying properly.

## What survives
The printed ciphers themselves, in the original magazine issues, plus Poe's essay, his *Alexander's Weekly Messenger* columns, and the recovered plaintexts. Both ciphertexts are short and fully transcribed in the modern literature; the corpus is trivially machine-readable. The first Tyler cipher proved to be a monoalphabetic substitution concealing a passage from Joseph Addison's tragedy *Cato*; the second was polyalphabetic and concealed a text reported to be based on a poem by Hester Thrale.

## Prior attempts and current consensus
The ciphers sat unread for 150 years, cited as a Poe mystery. The first was solved in 1992; the second fell in 2000 in the course of a public Poe Cryptographic Challenge with a cash prize, after which nothing cryptologic remained. The literature that frames the episode is Shawn Rosenheim's *The Cryptographic Imagination* (Johns Hopkins, 1997), which argues for Poe's authorship of the Tyler ciphers on stylistic and circumstantial grounds; the counter-argument is that Poe's own claims about his cryptanalytic prowess were promotional and that a real correspondent is the simpler explanation. The field's position is that the texts are solved and the pseudonym is unresolved and probably unresolvable without a new document.

## What a solution would have to do
For the ciphers: nothing further — a key that produces continuous English, matching a locatable printed source, is a mechanical verification and both have it. For the remaining authorship question, a claim that Poe was Tyler would have to: (a) rest on features of the ciphertexts that are diagnostic of Poe rather than of 1840s American cipher practice generally — his known cipher habits from the *Alexander's* columns, his spelling and transcription errors, his choice of source texts; (b) explain why Poe would print ciphers he then declined to solve, which is the strongest circumstantial argument for the hoax and also the easiest to explain innocently; (c) be tested against a control set of other reader-submitted ciphers from the same columns, so that "Poe-like" is shown to distinguish Tyler from the other correspondents; and (d) ideally produce external evidence — correspondence, a ledger entry, an editorial memorandum. A stylometric argument on two short ciphertexts and their plaintexts is very weak evidence and should be presented as such.

## Why the scores
- mystery 2: the ciphers are solved; a working consensus holds that the Tyler identity is open but minor, so the residual mystery is real but small.
- material 5: both ciphertexts survive in print with their plaintexts and keys recovered; the surrounding Poe corpus is complete and digitized.
- solvable 5: demonstrated — the ciphers decrypt to sensible English matching known sources.
- compute 5: the calibration anchor. A monoalphabetic and a short polyalphabetic cipher are routine for standard cryptanalysis; the rubric should have scored this 5 in 1985, when nobody had tried.
- verifiable 5: a key decrypts the whole text and the plaintext matches a printed source word for word — the strongest form of verification the rubric recognises.
- crowding 2: a public competition drew many entrants and the Poe scholarly literature is large; not 1 because the authorship question has had comparatively little serious archival attention.

## Sources
- SECONDARY — Wikipedia, "Edgar Allan Poe," Cryptography section (the *Alexander's Weekly (Express) Messenger* challenge; "A Few Words on Secret Writing," *Graham's Magazine*, July 1841; "The Gold-Bug"; two ciphers submitted under the name "W. B. Tyler" in 1841, the first solved in 1992 and the second in 2000; the plaintext sources identified as a quotation from Addison's *Cato* and a text probably based on a poem by Hester Thrale). https://en.wikipedia.org/wiki/Edgar_Allan_Poe
- SCHOLARLY — S. Rosenheim, *The Cryptographic Imagination: Secret Writing from Edgar Poe to the Internet* (Johns Hopkins UP, 1997) — the standard treatment and the source of the Poe-as-Tyler argument; cited from general reference, not read directly.
- PRIMARY — E. A. Poe, "A Few Words on Secret Writing," *Graham's Magazine* (July 1841) — the essay containing the challenge; no verified digitization URL was pinned in this pass.

## Unverified claims
- The names usually given for the solvers — Terence Whalen for the first cipher (1992) and Gil Broza for the second (2000) — are reported in the popular literature but could not be verified in this pass; the Wikipedia article names neither. Treat the attributions as reported, not established.
- The Poe Cryptographic Challenge is commonly said to have been organized by Shawn Rosenheim with Bokler Software, running from 1998, with a cash prize in the low thousands of dollars. The organizer's page (bokler.com) no longer resolves and the Internet Archive is not reachable from this environment, so none of this is verified.
- The precise issue of *Graham's Magazine* in which the Tyler ciphers appeared (commonly cited as December 1841) was not verified.
- The Hester Thrale attribution of the second plaintext is given in the secondary source as "probably".
- Whether the second cipher was Vigenère-type or another polyalphabetic form was not verified.
