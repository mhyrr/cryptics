+++
title = "Euler's \"logogriph\" to Goldbach, 1744 (solved 1953) — calibration case"
slug = "euler-logogriph"
kind = "cipher"
era = "1744"
origin = "Leonhard Euler (Berlin) to Christian Goldbach (Russia)"
language = "Latin"
status = "solved"
confidence = "high"
digitized = "https://www.apprendre-en-ligne.net/crypto/euler/"
tags = ["calibration", "solved", "homophonic", "substitution", "latin", "mathematician", "challenge-cipher", "cryptiana"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 4
+++

# Euler's "logogriph" to Goldbach, 1744 (solved 1953) — calibration case

## What it is
Near the end of a mathematical letter to Christian Goldbach dated 4 July 1744, Leonhard Euler wrote out a cryptogram he had made "some time ago" and called a *logogryphum*. It is 408 characters in lower-case letters, with the long ſ used as a separate symbol. Euler gave Goldbach three hints:
- the plaintext is Latin;
- every symbol stands for a letter (so there are no nulls);
- the meaning of the symbols does not change (so it is not polyalphabetic).

He added that such a text "may not be easily deciphered." Their later correspondence never mentions it. The letter was printed by P. H. Fuss in *Correspondance mathématique et physique* (1843), vol. 1, p. 293, and again by Juškevič and Winter in the Euler–Goldbach *Briefwechsel* (1965), p. 200.

## What is unsolved
Nothing. The entry is a calibration case: a short, author-designed challenge cipher with stated rules that sat unread in print for about 110 years.

## What survives
The full ciphertext in the 1843 and 1965 editions. Rohrbach notes that the 1965 printing renders long ſ as s and has a few misprints. The original manuscript was not checked here.

## Prior attempts and current consensus
- An Euler-related society reportedly offered a prize in 1907 without result, according to Tomokiyo.
- The prize was announced again in 1953, and Pierre Speziali (Geneva) solved it: "Le logogriphe d'Euler," *Stultifera navis* (Bulletin de la Société suisse des bibliophiles) 10, no. 1/2 (April 1953), pp. 6–9. He separated vowels from consonants using doubled letters, then used low-frequency symbols and the crib PROXIMIS. Kahn's *Codebreakers* (1967) mentions the solution only in passing.
- Because Speziali's paper had little circulation, Hans Rohrbach published an independent solution: "The Logogryph of Euler," *Journal für die reine und angewandte Mathematik* 262/263 (1973), pp. 392–399. He started by identifying homophone pairs from repeated sequences: j = f, k = x, w = t, y = g, z = r, then v = i and ſ = l. Plaintext QU is a single symbol.

The cipher is a homophonic simple substitution: 27 symbols for about 20 Latin letters. The plaintext is Caesar, *De Bello Gallico* VII.25 (the Gaul at the gate of Avaricum, killed by a scorpion bolt, and those who took his place), ending "Caesar de Bello Gallico libro septimo capite vicesimo quinto." Euler skipped a few words of Caesar and made a few enciphering slips. Consensus: solved.

## What a solution would have to do
Met: one fixed key reads all 408 characters as Latin, apart from a few explicable slips. The Latin is a known classical passage that matches word for word, and the passage names its own source.

## Why the scores
Scored as of about 1950, before Speziali.
- **mystery 1 today.** In 1950 it would have been 2: a curiosity of a great mathematician, of no historical consequence.
- **material 5:** complete, printed, single witness, unambiguous symbols.
- **solvable 5:** the author states it is Latin in a fixed substitution with no nulls.
- **compute 5:** a 408-character homophonic substitution in a known language is a textbook hill-climbing target today. Two hand solvers needed only frequency, doublets and repeats.
- **verifiable 5:** the plaintext matches a published Caesar text word for word.
- **crowding 4:** a prize had gone unclaimed since 1907, but few cryptanalysts appear to have worked it.
- Calibration point: an author-set challenge with stated rules and a known plaintext language behaves like Copiale or Zodiac 340. The rubric's compute 5 / verifiable 5 is the right prediction. What delayed it was attention, not difficulty.

## Sources
- SECONDARY — S. Tomokiyo, Cryptiana, "数学者オイラーの残した暗号文の解読" (Decipherment of the cryptogram left by Euler; ciphertext, both solution methods, plaintext, bibliography). https://cryptiana.web.fc2.com/code/euler.htm
- SCHOLARLY — Hans Rohrbach, "The Logogryph of Euler," *Journal für die reine und angewandte Mathematik* 1973 (262–263): 392–399. https://doi.org/10.1515/crll.1973.262-263.392
- SCHOLARLY — Pierre Speziali, "Le logogriphe d'Euler," *Stultifera navis* (Bulletin de la Société suisse des bibliophiles) 10 (1953), no. 1/2, pp. 6–9. Cited via Tomokiyo and Didier Müller; not seen directly.
- SECONDARY — Didier Müller, "Le logogriphe d'Euler," apprendre-en-ligne.net (date of letter, Speziali 1953 and Rohrbach 1973 publication details). https://www.apprendre-en-ligne.net/crypto/euler/
- PRIMARY — P. H. Fuss (ed.), *Correspondance mathématique et physique de quelques célèbres géomètres du XVIIIème siècle*, vol. 1 (St Petersburg, 1843), p. 293 (Euler to Goldbach, 4 July 1744). Cited via Tomokiyo; page not opened here.

## Unverified claims
- The 1907 prize and its 1953 re-announcement, and who offered it ("a society collecting Euler's documents" in Tomokiyo's account). Müller's page does not mention a prize.
- The 408-character count is from Tomokiyo's account of Speziali. It was not recounted here (rule 9).
- That Euler's letter was written from Berlin. Euler was in Berlin from 1741, but the letter's place line was not seen.
- Speziali's paper itself was not read. Tomokiyo reports that a copy is in the Friedman archives, with a cover letter to Friedman dated 23 November 1953.
