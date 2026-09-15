+++
title = "Copiale cipher (solved 2011) — calibration case"
slug = "copiale-cipher"
kind = "cipher"
era = "18th century (1730s per one account; 1760–1780 per another)"
origin = "Germany (Oculist order, Wolfenbüttel)"
language = "German"
status = "solved"
confidence = "high"
digitized = "https://cl.lingfil.uu.se/~bea/copiale/"
tags = ["calibration", "solved", "homophonic", "expectation-maximization", "secret-society", "Freemasonry", "DECRYPT"]

[scores]
mystery = 1
material = 5
solvable = 5
compute = 5
verifiable = 5
crowding = 4
+++

# Copiale cipher (solved 2011) — calibration case

## What it is
A bound volume of 105 pages containing about 75,000 handwritten characters in a mixed alphabet of abstract symbols together with Greek and most of the Roman letters, produced in 18th-century Germany. It is called the Copiale cipher from the word "Copiales 3" on the last page. It sat unread for well over two centuries. In 2011 Kevin Knight (USC Information Sciences Institute) with Beáta Megyesi and Christiane Schaefer (Uppsala) decrypted it: the cipher is homophonic, plaintext German, with unaccented Roman letters functioning as spaces and several cipher symbols mapping to the same plaintext letter. The text is the initiation ritual of the "high enlightened Oculist order" of Wolfenbüttel, a society led by Count Friedrich August von Veltheim, involving symbolic blindness, spectacles, eye-washing and a mock operation plucking an eyebrow hair — evidently Freemasons preserving Masonic practice after the papal ban of Clement XII.

## What is unsolved
Nothing in the cipher. This entry is in `entries/` as a calibration case under the rubric's requirement to keep solved cases visible. Live historical questions remain: the order's membership and relation to regular Freemasonry, and the relation of this volume to the parallel manuscript at the Staatsarchiv Wolfenbüttel.

## What survives
The manuscript itself, in a private collection; a parallel manuscript at the Staatsarchiv Wolfenbüttel; and — the point for our purposes — a complete public transcription and images released by the decipherers, plus the decrypted German text and an English translation. The decipherment triggered the DECODE database and the ERC-funded DECRYPT project (Megyesi et al.), which has since collected thousands of historical ciphertexts and keys in machine-readable form and is the single most useful infrastructure that exists for anyone attacking entries in this catalog.

## Prior attempts and current consensus
Essentially no serious prior attempt is recorded, which is itself the lesson: the manuscript was not famous, so it was not crowded, and it fell within months of competent attention. The method is the canonical one: treat decipherment as machine translation, use expectation–maximization to fit a homophonic key against an n-gram language model of the candidate plaintext language, and iterate. Knight's team first ran it against German, having initially considered other languages, and the Roman-letters-as-spaces discovery came out of the fit rather than being assumed. Published at the 4th Workshop on Building and Using Comparable Corpora at ACL 2011 (Portland, Oregon), with a fuller *Cryptologia* treatment following. Consensus is complete and unanimous: the decryption is correct, it reads continuously, and the content is historically coherent with the Oculist order's documented existence.

## What a solution would have to do
Met, and the standard is worth stating because it is the bar other entries should be held to: a stated key that decodes all 105 pages continuously; plaintext that is grammatical German throughout, not just in the fitted stretches; content that coheres as a single document and matches independent archival evidence about the order; reproducibility by a third party from the published transcription and method. All four were satisfied. Note what made it possible and compare against the unsolved entries in this catalog: 75,000 characters (far above unicity distance for a homophonic cipher), one consistent system throughout, a plaintext language that is in fact a known language, and external documentary corroboration available.

## Why the scores
Scored as of 2010, before the break, which is the point.
- mystery 1 today: fully resolved. In 2010 it would have been 3 — an unread 18th-century volume, interesting but not field-changing.
- material 5: complete manuscript, one hand, one system, 75,000 characters. This is the axis that decided the case.
- solvable 5: obviously purposeful; the demonstrably non-random structure of a 90-odd-symbol system across 105 consistent pages.
- compute 5: the core question was computational — fit a homophonic key with EM against a language model — and 75,000 characters is more than enough data for it. A correctly calibrated rubric must have scored this 5 in 2010, on the strength of length and consistency alone, with no knowledge of the answer.
- verifiable 5: German text emerged and read continuously; mechanically checkable.
- crowding 4: almost nobody had worked it before 2011. The combination `material 5 + compute 5 + crowding 4` is the signature of a solvable-and-unworked case, and it is exactly the signature the `attackable` ranking is supposed to find.

## Sources
- PRIMARY — Kevin Knight, Beáta Megyesi, Christiane Schaefer, Copiale cipher project page: images, transcription, decrypted German and English translation. https://cl.lingfil.uu.se/~bea/copiale/
- SCHOLARLY — Knight, Megyesi & Schaefer, "The Copiale Cipher," *Proceedings of the 4th Workshop on Building and Using Comparable Corpora*, ACL 2011, Portland. https://aclanthology.org/W11-1202/
- SCHOLARLY — DECODE database / DECRYPT project (Megyesi et al.), machine-readable corpus of historical ciphers and keys. https://de-crypt.org/
- SECONDARY — Wikipedia, "Copiale cipher" (105 pages, ~75,000 characters, Roman letters as spaces, the Oculist ritual content, private collection, Wolfenbüttel parallel manuscript, ACL 2011 venue). https://en.wikipedia.org/wiki/Copiale_cipher

## Unverified claims
- The manuscript's date. The encyclopedic article says "created in the 1730s"; Wikipedia's own "List of ciphertexts" gives 1760–1780. The discrepancy was not resolved and matters for the historical argument but not for the calibration use.
- The number of distinct cipher symbols. Commonly given as about 90; the encyclopedic article consulted does not state a count and it was not recounted from the transcription.
- The identity of the private collection now holding the manuscript was not established.
- Whether a *Cryptologia* article followed the ACL paper, and its citation, was not verified.
- Whether the project page URL above is still live and hosts the full transcription was not confirmed by fetch.
- The exact relationship between this volume and the Wolfenbüttel parallel manuscript (copy, exemplar, sibling) was not established.
