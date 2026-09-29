+++
title = "Rilke cryptogram (typed insert in a 1942 Rilke biography) — calibration case"
slug = "rilke-cryptogram"
kind = "cipher"
era = "c. 1942–1945"
origin = "Germany or German-occupied France"
language = "none established"
status = "likely-noise"
confidence = "medium"
digitized = "https://scienceblogs.de/klausis-krypto-kolumne/the-rilke-cryptogram/"
tags = ["calibration", "likely-noise", "WWII", "typewritten", "keyboard-patterns", "long-ciphertext", "transcribed"]

[scores]
mystery = 1
material = 5
solvable = 1
compute = 4
verifiable = 3
crowding = 3
+++

# Rilke cryptogram — calibration case

## What it is
A typewritten, hectographed alphanumeric text of 33 pages and 18,760 characters in groups of four, glued into one copy of a 1942 Paris front-edition of Gert Buchheit's biography of Rainer Maria Rilke. Its alphabet is a–z, digits and the German umlauts; a sample: `abdh jgzt 23c5 vzbi opLö üäui 87dw`. The owner, Dr. Karsten Hansky, gave it to Klaus Schmeh, who published scans and a transcription on Cipherbrain (entry #15 on his top-50 list).

## What is unsolved
Formally, whether it encodes anything. The answer that has emerged is that it does not. It looks like keyboard noise: finger-rolls across a German QWERTZ typewriter, with an unusual share of runs such as `qwer` and `aswq` between physically adjacent keys. The likeliest purpose is practice material, perhaps for Morse or radio operators.

## What survives
The book with its insert, in private hands; the complete scans and transcription on Cipherbrain.

## Prior attempts and current consensus
Commenters on Cipherbrain suggested practice material as early as 2018. Schmeh, Tobias Schrödel and others pointed to keyboard-adjacency patterns around 2020. Floe Foxon's "A treatise on the Rilke cryptogram," *Cryptologia* 47 (6) (2022/23), measured character and n-gram entropy: less ordered than English or German, more ordered than random text. Foxon also reports that consecutive characters lie much closer together on the keyboard than natural language, known ciphers or random text would put them. A reader update on *Futility Closet* (June 2026) calls the case effectively closed as keyboard mashing. Consensus: likely noise; no competing reading.

## What a solution would have to do
Already done, in the negative. A noise verdict is established when a generative model of a typist (keyboard-adjacency transitions, hand alternation, group formatting) reproduces the text's statistics, and cipher and plaintext models of the same length do not. A claimed decipherment would have to overturn that by reading continuous text under one key, which the keystroke-distance result makes very unlikely.

## Why the scores
- mystery 1: effectively resolved as noise; the only open question is who typed it and why.
- material 5: complete, fully scanned and transcribed; 18,760 characters.
- solvable 1: the statistical evidence is that there is no plaintext.
- compute 4: the question that mattered was statistical and computation answered it. This is the DESCRIBE mode working as intended.
- verifiable 3: a noise verdict is statistical; it persuades, but no decrypt can confirm it.
- crowding 3: a blog community, one peer-reviewed paper.
- compute mode (retrospective): DESCRIBE (keyboard-geometry null model) · verifier STRONG · space ENUMERABLE · signal NO · fit HIGH.
- Calibration point: length and full transcription, the two properties that made Copiale fall, do not by themselves make a text attackable. Before scoring any long, uncrowded, digitized ciphertext at `solvable 4+`, run the keyboard, glossolalia and random-generator null models. This applies to the Hampton notebook entry.

## Sources
- PRIMARY — Scans and transcription of the insert, via Klaus Schmeh, "The Rilke cryptogram," Cipherbrain. https://scienceblogs.de/klausis-krypto-kolumne/the-rilke-cryptogram/
- SCHOLARLY — Floe Foxon, "A treatise on the Rilke cryptogram," *Cryptologia* 47 (6). https://www.tandfonline.com/doi/abs/10.1080/01611194.2022.2092784
- POPULAR — *Futility Closet*, "The Rilke Cryptogram," 18 Jun 2026, with reader update (33 pages, 18,760 characters, keyboard-mashing verdict, Morse-practice explanation). https://www.futilitycloset.com/2026/06/18/the-rilke-cryptogram/

## Unverified claims
- Foxon's conclusions are reported from secondary summaries; the paper's abstract could not be fetched (publisher 403).
- The Morse- or radio-practice explanation is conjecture, not documented.
- Page count: Schmeh's list of encrypted books gives 184, and his page shows images numbered up to 189, against 33 pages in *Futility Closet*. The larger figures may be the host book's page numbers; not reconciled.
- The attribution of the 2020 keyboard-pattern identification to named individuals comes from a reader update, not from their own publication.
