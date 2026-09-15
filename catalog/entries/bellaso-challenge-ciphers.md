+++
title = "Bellaso challenge ciphers (1555 and 1564)"
slug = "bellaso-challenge-ciphers"
kind = "cipher"
era = "1555 and 1564"
origin = "Brescia and Venice, Italy"
language = "Italian (and Latin)"
status = "solved"
confidence = "low"
digitized = "https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso"
tags = ["calibration", "polyalphabetic", "countersign", "Renaissance-cryptography", "challenge-cipher", "Biermann", "recently-fallen"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 5
verifiable = 5
crowding = 4
+++

# Bellaso challenge ciphers (1555 and 1564)

## What it is
Giovan Battista Bellaso (1505 – between 1568 and 1581) published three cryptographic books: *La cifra del Sig. Giovan Battista Bellaso* (Venice, 1553), *Novi et singolari modi di cifrare* (Brescia, 1555) and *Il vero modo di scrivere in cifra* (1564). His system is the one usually miscredited to Blaise de Vigenère: reciprocal mixed alphabets driven by an agreed keyword or "countersign," combining Alberti's mixed alphabets with Trithemius's letter-by-letter progression, and requiring no disk or table to be exchanged. In the 1555 and 1564 books he published sets of cryptograms enciphered by his own methods and challenged his detractors to solve them.

## What is unsolved
On the current record, nothing — which is why the brief's premise that "several were solved recently" needed checking and why this entry's status is `solved` rather than `partial`. The seven challenges of 1564 are decrypted, and their keys are published: MO-HUG, DE-OTU, QU-EHTBS, SP-FXOT, BA-TIS, HR-DIS, and BARTOLMEUS-PANFILUS. The 1555 challenges are reported solved in 2018 by Norbert Biermann, "Analysis of Giouan Battista Bellaso's cipher challenges of 1555," *Cryptologia* 42(5): 381–407. The hedge matters and is recorded honestly: the encyclopedic source says the 1555 challenges were "**purportedly** solved in 2018," and this entry's `confidence` is low because that qualifier was not resolved against the paper itself. If the 1555 solutions are in fact contested, the status of this entry should move to `partial`.

## What survives
All three printed books survive and two are digitized (the 1553 *La cifra* and the 1555 *Novi et singolari modi*); contemporary copies of correspondence in Bellaso's ciphers are mentioned as having been in private collections in Florence and Rome. The challenge cryptograms are printed text, exactly transmitted apart from possible typesetting error — which for a polyalphabetic cipher is a real hazard, since a single wrong letter corrupts only one position but a dropped letter desynchronizes everything after it. Machine-readable transcriptions of the cryptograms exist in the cryptologic-history literature and in the DECODE/DECRYPT database of historical ciphers.

## Prior attempts and current consensus
The modern rediscovery of Bellaso is owed largely to Augusto Buonafalce, whose *Cryptologia* work re-established Bellaso's priority over Vigenère and brought the challenge ciphers back into view; Tony Gaffney and others in the amateur cryptologic community broke several of them in the late 2000s; Biermann's 2018 paper closes out the 1555 set. Consensus on the historical point — Bellaso, not Vigenère, invented the keyword-driven polyalphabetic cipher in the form the world later used — is settled. This is a useful calibration case for a specific reason: four-hundred-and-fifty-year-old challenge ciphers, of moderate length, in a known language, with the system published by the author in the same book, fell to a mixture of patient human cryptanalysis and modern computer search within a decade of anyone seriously trying. The predictive signature is the same one Copiale shows: adequate length, one consistent system, a known plaintext language, and a thin prior literature.

## What a solution would have to do
Met for all the challenges on the current record, and the criteria are exemplary: state the countersign, decrypt the cryptogram completely to grammatical 16th-century Italian or Latin, and have the key be of the form Bellaso's own books describe — which is why the published 1564 keys (short two-part countersigns like `MO-HUG`, and the name-pair `BARTOLMEUS-PANFILUS`) are convincing: they are the right shape for the system. For anyone revisiting the 1555 set to check Biermann: the test is whether his keys are in Bellaso's documented key format, whether the plaintexts are idiomatic period Italian throughout rather than in patches, and whether they make sense as messages Bellaso would have chosen to publish — challenge texts in this period tend to be polemical or self-advertising, and content is evidence.

## Why the scores
Scored as of roughly 2005, before the modern breaks, which is the calibration point.
- mystery 2: a working consensus existed and the stake was a priority dispute in the history of cryptography, not a large question.
- material 4: printed books, some digitized, exactly transmitted; not 5 because the cryptograms are short, there is no critical edition of the challenge texts, and typesetting error is a live hazard in a polyalphabetic cipher.
- solvable 5: the author says so. He published the system, published the cryptograms, and dared readers to break them — the clearest possible statement of intent in this catalog.
- compute 5: keyword search over a published polyalphabetic system against an Italian language model is precisely a machine problem with mechanical verification, and the data was ready. A rubric that did not score this 5 in 2005 would be miscalibrated.
- verifiable 5: a countersign either decrypts the cryptogram to Italian or it does not.
- crowding 4: a handful of serious treatments (Buonafalce, Gaffney, Biermann) and no dedicated monograph. High crowding plus high compute plus high solvable is the profile of a case that falls, and it did.

## Sources
- SCHOLARLY — Norbert Biermann, "Analysis of Giouan Battista Bellaso's cipher challenges of 1555," *Cryptologia* 42(5): 381–407 (2018). https://doi.org/10.1080/01611194.2018.1493161
- SCHOLARLY — Augusto Buonafalce, "Bellaso's Reciprocal Ciphers," *Cryptologia* 30(1) (2006). https://doi.org/10.1080/01611190500383581
- PRIMARY — Giovan Battista Bellaso, *La cifra del Sig. Giovan Battista Bellaso* (Venice, 1553), digitized.
- PRIMARY — Giovan Battista Bellaso, *Novi et singolari modi di cifrare* (Brescia, 1555), digitized; contains the 1555 challenges.
- PRIMARY — Giovan Battista Bellaso, *Il vero modo di scrivere in cifra* (1564); contains the seven challenges whose keys are now published.
- SECONDARY — Wikipedia, "Giovan Battista Bellaso" (life dates, the three books, the 1555 challenges "purportedly solved in 2018," the seven 1564 keys as listed, the reciprocal-alphabet countersign system, copies in private collections in Florence and Rome). https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso

## Unverified claims
- Whether the 1555 challenges are *accepted* as solved. The encyclopedic source's word is "purportedly," and Biermann's paper was not read. This single word is the reason `confidence` is low, and resolving it should be the first action on this entry.
- How many challenges the 1555 book contains. Not stated in the source consulted; only the 1564 count (seven) is given.
- Who solved the 1564 challenges, and when. The source lists the keys without attribution. Buonafalce and Tony Gaffney are named here from general knowledge of the *Cryptologia* literature, not from a verified citation.
- Buonafalce's exact article title, volume and pages were not verified at the publisher.
- The digitization URLs for the 1553 and 1555 books were not captured; the source links to digitized versions but the URLs were not recorded.
- Whether the DECODE/DECRYPT database in fact holds the Bellaso challenge cryptograms in machine-readable form was not confirmed.
- Whether any Bellaso-enciphered correspondence survives in Florence or Rome today, as opposed to having been there historically, was not established.
