+++
title = "Robert Patterson's challenge cipher for Jefferson, 1801 (solved 2007, published 2009) — calibration case"
slug = "patterson-jefferson-cipher"
kind = "cipher"
era = "19 December 1801 (Jefferson's reply 22 March 1802); solved 2007, published 2009"
origin = "Philadelphia: Robert Patterson (University of Pennsylvania; American Philosophical Society) to President Thomas Jefferson"
language = "English"
status = "solved"
confidence = "medium"
digitized = "https://founders.archives.gov/pageref/TSJN-01-36-02-pb-0171"
tags = ["calibration", "solved", "transposition", "American", "Jefferson", "challenge-cipher", "dynamic-programming", "Cryptiana"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 4
+++

# Robert Patterson's challenge cipher for Jefferson, 1801 (solved 2007, published 2009) — calibration case

## What it is
Robert Patterson was a mathematician at the University of Pennsylvania and vice-president of the American Philosophical Society while Jefferson was its president. On 19 December 1801 he sent Jefferson a new cipher he considered perfect, with an enciphered specimen. He claimed it could not be deciphered "without necessary keys, even with the united ingenuity of the whole human race." Jefferson replied on 22 March 1802 and later, on 18 April 1803, sent a modified version to Robert Livingston in Paris.

The system is a transposition: letters are rearranged, not substituted. The plaintext is written in vertical columns and copied out horizontally in a scrambled order under two keys. A "key of lines" orders the lines within sections, and a "key of letters" adds nulls at the start of lines. The specimen stayed unread for about two centuries. Lawren M. Smithline, a mathematician at the Center for Communications Research in Princeton, broke it and found it was the preamble of the Declaration of Independence ("In Congress, July fourth, one thousand seven hundred and seventy six…").

## What is unsolved
Nothing. This is a calibration case: a short challenge cipher from a capable designer that held out until someone brought statistics and a sequence-alignment algorithm to it.

## What survives
The letter and specimen in the Thomas Jefferson Papers, Library of Congress. They are printed in *The Papers of Thomas Jefferson* vol. 36 and on Founders Online, along with Jefferson's reply and the 1803 letter to Livingston.

## Prior attempts and current consensus
**Before Smithline:** no published decryption in about 200 years. Jefferson himself did not decipher it, as far as the sources read here say.

**Smithline's method** (*American Scientist* 97 (2), March–April 2009, pp. 142–149):
- He used digraph probabilities to score which rows of the transposed text belong next to each other, without knowing the key structure in advance.
- He adapted "a technique originally developed for biological sequence comparison," that is, dynamic-programming alignment, to cope with the nulls.

The plaintext, a well-known text written by the recipient, confirms the solution beyond doubt. Consensus: solved.

## What a solution would have to do
Met: one set of line and null keys that turns the whole specimen into continuous English, consistent with the procedure Patterson's letter describes. The plaintext turned out to be a known document, the strongest possible check.

## Why the scores
Scored as it stood before 2007, except mystery.
- mystery 1 today. It was 2 before: a curiosity in the history of American cryptography, not a historical question.
- material 5: the complete specimen and the inventor's own description of the system are both in a critical edition and online.
- solvable 5: the designer states it is a cipher and describes the method.
- compute 5: a short transposition whose general form is known is exactly a combinatorial search scored by English digraph statistics. The solve was this computation.
- verifiable 5: continuous English, which turned out to be a known text.
- crowding 4: famous enough in Jefferson circles to be listed, but with no serious published attack before Smithline. It could have been 5.
- compute mode (retrospective): ENUMERATE (row-adjacency scoring plus alignment for nulls) · verifier MECHANICAL · space STRUCTURED · signal YES · fit HIGH.
- Calibration point: a designer's claim that a cipher is unbreakable, plus two centuries of neglect, did not mean it was hard. The rubric should, and does, give high compute to any short classical cipher whose system the author describes.

## Sources
- SCHOLARLY — Lawren M. Smithline, "A Cipher to Thomas Jefferson," *American Scientist* 97 (2) (March–April 2009), pp. 142–149. https://www.proquest.com/openview/59bc21390c7eac78f14dffcd66fb3067/1?cbl=40798&pq-origsite=gscholar
- PRIMARY — *The Papers of Thomas Jefferson* vol. 36, Patterson to Jefferson, 19 December 1801, via Founders Online page reference. https://founders.archives.gov/pageref/TSJN-01-36-02-pb-0171
- SECONDARY — Tomokiyo, Cryptiana, "Patterson's cipher for Jefferson": the dates, the system, the "united ingenuity" quote, the Livingston letter, Smithline's digraph method, and the Declaration plaintext. https://cryptiana.web.fc2.com/code/jeffers4.htm
- SECONDARY — Wikipedia, "Robert Patterson (educator)" (gives 2007 as the year of the solve). https://en.wikipedia.org/wiki/Robert_Patterson_(educator)
- POPULAR — Language Log, "A Fourth of July Cipher," citing Rachel Emma Silverman, "Two Centuries On, a Cryptologist Cracks a Presidential Code," *Wall Street Journal*, 2 July 2009. https://languagelog.ldc.upenn.edu/nll/?p=1556

## Unverified claims
- The 2007 solve date comes from Wikipedia. Cryptiana says "deciphered in 2009," probably the publication year. The *American Scientist* article itself (paywalled) was not read.
- The specimen's length, the key sizes, and any slips in Patterson's own encipherment were not read from the primary.
- That Jefferson never deciphered or used the specimen.
- The Founders Online link is a page reference into vol. 36. The exact document URL was not opened.
