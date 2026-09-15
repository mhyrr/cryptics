+++
title = "Trithemius, Steganographia Book III (solved 1996/1998) — calibration case"
slug = "trithemius-steganographia-book-iii"
kind = "cipher"
era = "written c. 1499; printed Frankfurt 1606"
origin = "Sponheim Abbey, Germany"
language = "Latin (surface); Latin plaintext concealed"
status = "solved"
confidence = "medium"
digitized = "https://www.esotericarchives.com/tritheim/stegano.htm"
tags = ["calibration", "solved", "steganography", "angel-magic", "Renaissance", "Ernst", "Reeds", "Index-librorum"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 3
verifiable = 5
crowding = 3
+++

# Trithemius, Steganographia Book III (solved 1996/1998) — calibration case

## What it is
A three-book treatise written about 1499 by Johannes Trithemius, Benedictine abbot of Sponheim, and first printed at Frankfurt in 1606. On its face it teaches long-distance communication by conjuring spirits: pages of barbarous angel names and invocations. Books I and II are in fact cryptographic — the concealed plaintext is carried inside the "conjurations" — and a key published with the 1606 edition made that plain. Book III was different. It presented tables of planetary angels, periods and numbers with no obvious cover text, and for nearly five centuries readers including its defenders and its ecclesiastical censors took it for genuine occult material. The book was on the *Index Librorum Prohibitorum* from 1609 until 1900.

## What is unsolved
Nothing. Thomas Ernst (1996, in the German journal *Daphnis*) and Jim Reeds (1998, in *Cryptologia*), working independently, showed that Book III's angelic and astrological apparatus is itself a cover for further cryptographic material — the numbers and names conceal text by the same class of device as Books I and II. The entry is here as a calibration case. The residual open questions are about Trithemius's intentions and his reception: whether he meant the magical frame as pure cover, as a genuine belief he also happened to encode within, or as deliberate provocation, and how far his readers (Agrippa, Dee) understood the trick.

## What survives
Excellent conditions. The 1606 printed text and later editions are digitized and transcribed, including at Joseph Peterson's Esoteric Archives; manuscript copies of the pre-print circulation exist; and Trithemius's own *Polygraphia* (1518) provides a published, contemporaneous account of his cryptographic methods, which functions as the key to his mind. The material situation is as good as anything in this catalog: complete text, multiple witnesses, printed, transcribed, with the author's own methodological treatise alongside.

## Prior attempts and current consensus
Five hundred years of reading Book III as magic, by people who had every reason to look for a cipher — including scholars who knew Books I and II were ciphers. That is the calibration lesson: the failure was not one of data or computation but of *hypothesis*. Nobody assumed the third book was the same kind of object as the first two, because it did not look like it. Ernst and Reeds, independently and within two years, asked the obvious question and answered it. Reeds's paper, "Solved: The Ciphers in Book III of Trithemius's Steganographia," *Cryptologia* 22(4) (1998), is the accessible English treatment and the thing to read; Ernst has priority and published in German. Consensus is complete. Related: Trithemius is the origin of the Trithemius cipher (progressive-key polyalphabetic), and Robert Hooke speculated that Dee used Trithemian steganography in his reports to Elizabeth I.

## What a solution would have to do
Met, and the criteria were mechanical: state the extraction rule, apply it to Book III's tables and names, and produce Latin plaintext that reads continuously and coheres with the cryptographic content of Books I and II and with *Polygraphia*. Ernst and Reeds independently produced the same result, which is the strongest form of verification available short of a key from the author — and in effect the author did supply the key, in *Polygraphia*, for anyone who thought to look. For this catalog the transferable question is: which other "magical" texts are cover for something else, and has anyone applied the Ernst/Reeds question to them? The obvious candidates are in this catalog already — the Book of Soyga tables (where the answer was yes, an algorithm), the Liber Loagaeth tables (where nobody has run the test).

## Why the scores
Scored as of 1995, before the break.
- mystery 1 today: resolved by two independent solutions. In 1995 it would have been 3, and the scholarly framing would have been "an occult text," not "an unsolved cipher" — which is the interesting failure.
- material 5: complete printed text, multiple witnesses, digitized and transcribed, plus the author's own cryptographic manual.
- solvable 5: near-certain even in 1995 on structural grounds — Books I and II of the same treatise were known ciphers, and the author wrote a cryptography textbook.
- compute 3, not 5: this fell to human reading and hypothesis, not to search. Number-and-name tables of this size do not need a computer, and no statistical fingerprint was involved. Honest scoring of a solved case has to admit when computation was not the lever.
- verifiable 5: the extraction rule yields Latin or it does not, and two independent solvers converged.
- crowding 3: a modest scholarly literature on Trithemius, and the obvious approaches had been tried on Books I and II — but not on III, which is why it was still open in 1995.

## Sources
- SCHOLARLY — Jim Reeds, "Solved: The Ciphers in Book III of Trithemius's Steganographia," *Cryptologia* 22(4): 291–317 (1998). https://doi.org/10.1080/0161-119891886948
- SCHOLARLY — Thomas Ernst, "Schwarzweiße Magie. Der Schlüssel zum dritten Buch der Steganographia des Trithemius," *Daphnis* 25 (1996). https://brill.com/view/journals/daph/25/1/daph.25.issue-1.xml
- PRIMARY — Johannes Trithemius, *Steganographia* (Frankfurt, 1606), text and translation at Esoteric Archives. https://www.esotericarchives.com/tritheim/stegano.htm
- PRIMARY — Johannes Trithemius, *Polygraphiae libri sex* (1518): the author's own cryptographic manual.
- SECONDARY — Wikipedia, "Steganographia" (1499 composition, 1606 printing, the 1606 key to Books I–II, Ernst 1996 and Reeds 1998 on Book III, Index 1609–1900, Hooke on Dee). https://en.wikipedia.org/wiki/Steganographia

## Unverified claims
- Reeds's exact page range and Ernst's exact pages and article title were not verified at the publishers; the citations above should be checked before reuse.
- Precisely *what* Book III's concealed plaintext says — whether it is further cryptographic instruction, filler, or substantive text — was not established from a primary reading. The encyclopedic source says only that the magical formulas are "covertexts for yet more material on cryptography."
- Whether Ernst's and Reeds's solutions agree in every detail, or only in the central claim, was not verified.
- The claim that a key published with the 1606 edition revealed Books I and II is from the encyclopedic account; the identity of that key's author (sometimes given as Vigenius/Vigenère) was not confirmed.
- Whether any manuscript witness of the pre-1606 circulation is digitized was not checked.
