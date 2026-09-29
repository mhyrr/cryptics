+++
title = "Moustier altar inscriptions (St. Martin's Church, Moustier, Belgium)"
slug = "moustier-altar-inscriptions"
kind = "inscription"
era = "19th century (c. 1840s)"
origin = "Moustier, Frasnes-lez-Anvaing, Hainaut, Belgium"
language = "Latin suspected (abbreviated prayer?)"
status = "unsolved"
confidence = "low"
digitized = "http://cipherfoundation.org/older-ciphers/moustier-cryptogram/"
tags = ["church", "altar", "initialism", "prayer", "short-ciphertext", "Belgium", "Cryptolog"]

[scores]
mystery = 2
material = 3
solvable = 3
compute = 4
verifiable = 3
crowding = 3
+++

# Moustier altar inscriptions

## What it is
Two carved inscriptions on the side altars of St. Martin's Church in Moustier, in Frasnes-lez-Anvaing, Hainaut: one on the altar of St. Mary (left) and one on the altar of St. Martin (right). Each is ten lines of capital letters, about eighty characters each on Schmeh's count, mostly Latin letters with an occasional Greek letter and marks such as carets and brackets. The Mary altar begins `L F E G K R V Q`, the Martin altar `J N L K B F P R`. Both date from the nineteenth century. They were little known outside the parish until a 1974 article in the NSA's internal newsletter *Cryptolog*, declassified and found by Nick Pelling.

## What is unsolved
What the letters stand for. The likeliest reading is not a cipher of continuous text but an initialism: each letter the first letter of a word in a prayer, hymn or dedication. Carving the initials of a known devotional text is a documented custom. A related idea, reported in 2022, reverses Trithemius's *Ave Maria* cipher, with each letter standing for a prayer word. Jarl Van Eycke reported that the statistics of both texts argue against simple substitution.

## What survives
Both inscriptions, in situ and complete. Photographs and a video by Klaus Schmeh (visit 2015), and transcriptions by Nick Pelling. The transcription has disputed points: ligatures, variant letterforms and "extender" strokes that may merge or split letters.

## Prior attempts and current consensus
*Cryptolog* (September 1974). Pelling's blog posts and transcription. Schmeh's top-50 list (#18), with posts in 2013, 2015 and 2017. Dirk Huylebrouck's article in the Belgian magazine *EOS* (April 2022), with Van Eycke's statistics and the Trithemius hypothesis. No reading has been proposed that others accept.

## What a solution would have to do
If initialism: find a Latin (or French) text whose word initials match both inscriptions letter for letter over long runs, with any mismatch explained (a carver's error or a ligature). The text should suit a Marian altar and a St. Martin altar respectively, which is a second, independent check. Parish or diocesan records of the altars' dedication would corroborate. If a cipher: a key that reads both inscriptions as grammatical text under one system. Around 80 characters each is too short to accept an unconstrained key, so any cipher reading must bring outside evidence.

## Why the scores
- mystery 2: a parish curiosity with a small, persistent cryptographic following.
- material 3: complete and photographed, but only about 160 characters, with contested letterforms.
- solvable 3: an altar inscription is certainly meant to say something; but if it is an initialism of an unknown or local text, the meaning may not be recoverable.
- compute 4: the initialism hypothesis is a clean corpus sweep: match initial-letter strings from digitized Latin liturgy, the Vulgate, breviaries and Marian hymns against both inscriptions. A long exact run is significant against a null model, and nobody has published that sweep.
- verifiable 3: a long exact initialism match would be near-mechanical; failing that, readings stay plausibility-only.
- crowding 3: 170 years of local curiosity, a 1974 NSA article, two active bloggers and a 2022 magazine piece.
- compute mode: SWEEP (initial-letter matching against liturgical corpora) · verifier MECHANICAL on a hit · space ENUMERABLE · signal WEAK · fit HIGH if the transcription holds; the ligature dispute is the weak leg.

## Sources
- PRIMARY — The inscriptions, St. Martin's Church, Moustier; photographs and transcription gathered at the Cipher Foundation. http://cipherfoundation.org/older-ciphers/moustier-cryptogram/
- POPULAR — Klaus Schmeh, "The Top 50 unsolved encrypted messages: 18. The Moustier altar inscriptions," Cipherbrain, 7 Nov 2017 (line counts, opening letters, Greek letters and symbols). https://scienceblogs.de/klausis-krypto-kolumne/2017/11/07/the-top-50-unsolved-encrypted-messages-18-the-moustier-altar-inscriptions/
- POPULAR — Klaus Schmeh, "Neues zu den Moustier-Inschriften," Cipherbrain, 25 Apr 2022 (reporting Huylebrouck in *EOS*, Van Eycke's statistics, the Trithemius hypothesis). https://scienceblogs.de/klausis-krypto-kolumne/2022/04/25/neues-zu-den-moustier-inschriften/
- SECONDARY — *Cryptolog* (NSA internal newsletter), September 1974 article on Moustier (declassified; not seen).

## Unverified claims
- The exact date and maker of the altars; "19th century" and "about 170–180 years" are from the blog posts.
- The *Cryptolog* article's author and content.
- Whether parish or diocesan archives have been searched for the altars' dedication or commission.
- Exact character counts; "80+ characters" per inscription is a secondary summary.
