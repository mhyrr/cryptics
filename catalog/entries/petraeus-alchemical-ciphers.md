+++
title = "Enciphered passages in the Petraeus alchemical manuscript (Hamburg, Cod. alchim. 651)"
slug = "petraeus-alchemical-ciphers"
kind = "cipher"
era = "c. 1700 (compiling earlier material on Rudolf II's court)"
origin = "Hamburg (Benedikt Nikolaus Petraeus)"
language = "German presumed"
status = "unsolved"
confidence = "low"
digitized = "https://scienceblogs.de/klausis-krypto-kolumne/2021/01/05/ungeloeste-verschluesselungen-in-einem-300-jahre-alten-manuskript/"
tags = ["alchemy", "nomenclator", "homophonic", "Rudolf-II", "manuscript", "uncrowded", "short-ciphertext"]

[scores]
mystery = 2
material = 3
solvable = 4
compute = 3
verifiable = 3
crowding = 4
+++

# Enciphered passages in the Petraeus alchemical manuscript (Hamburg, Cod. alchim. 651)

## What it is
An alchemical manuscript of about 1700 connected with the Hamburg physician Benedikt Nikolaus Petraeus, now Staats- und Universitätsbibliothek Hamburg, Cod. alchim. 651. Its centrepiece is a German poem of about 500 lines, *Thorough Summary of All Celestial Influence*, attributed to "Martinus de Delle", said to be a chamberlain or court poet of Emperor Rudolf II. The poem makes claims about alchemists at Rudolf's court. Lang, Zotov and Piorko call de Delle fictional, likely the product of textual corruption. Both the prose introduction and the verse contain enciphered passages, five in all.

## What is unsolved
What the five passages say. Rafał Prinke, a historian of alchemy, found them and showed them to several cryptanalysts without result. Given where they sit, they are likely recipes, names, or the claims about Rudolfine alchemists that the writer did not want in clear. They are an alchemist's own secrets rather than a public revelation.

## What survives
The manuscript in Hamburg. Images of the ciphered sections are printed in Prinke and Zuber (2020). Schmeh's 2021 post gives images, frequency counts and a transcription spreadsheet. The passages differ in length, the shortest only a few words. The symbol set suggests a nomenclator: signs for whole words alongside letter substitutes, possibly with homophones. Some signs may be alchemical symbols for substances.

## Prior attempts and current consensus
Prinke and Zuber (2020) published the manuscript's context and the images. Schmeh's 2021 post drew blog-reader attempts; none succeeded, as far as found. Lang, Zotov and Piorko's survey of alchemical cryptography (HistoCrypt 2024) lists it among more than 100 instances of alchemical ciphering, most of them unstudied, and calls the field "a goldmine yet untapped." Consensus: unsolved, barely attempted.

## What a solution would have to do
Give a key (letter substitutes, homophones and code signs) that reads all five passages as German. The code signs should come out as alchemical substances or proper names consistent with the surrounding clear text and the poem's Rudolfine claims. Passages in verse should scan with the poem around them. Any sign read as an alchemical symbol must take that symbol's standard meaning. Because the texts are short, a reading that fits one passage alone is worthless: the test is one key across all five.

## Why the scores
- mystery 2: small stakes, a few passages in an alchemical compilation, though anything naming Rudolf's adepts would interest historians of alchemy.
- material 3: all five passages are imaged and transcribed by an amateur, but their total length is small and the full manuscript's digitization was not confirmed.
- solvable 4: a nomenclator embedded in clear text, in a context that explains why it was used; almost certainly meaningful.
- compute 3: the homophonic/nomenclator key search is standard and the surrounding German gives a language model; but a short text with code signs is near or below unicity, so the search will return several candidates.
- verifiable 3: a reading is checked by consistency across passages and with the clear text around them, not mechanically.
- crowding 4: Prinke and Zuber, one blog round, a survey mention.
- compute mode: ENUMERATE (homophonic and nomenclator hill-climb with alchemical-lexicon cribs) · verifier CONSENSUS · space SAMPLABLE · signal WEAK · fit MEDIUM.
- This entry stands for the class the Lang et al. survey maps: many short alchemical ciphers, each small, not yet studied. If one is worked, work them together; shared nomenclator conventions across manuscripts would add the length that each lacks alone.

## Sources
- PRIMARY — Staats- und Universitätsbibliothek Hamburg, Cod. alchim. 651 (not fetched; see Unverified).
- SCHOLARLY — Sarah Lang, Sergei Zotov and Megan Piorko, "Sources of Alchemical Cryptography," *Proceedings of HistoCrypt 2024* (over 100 instances; entry on Cod. alchim. 651 citing Prinke and Zuber 2020, esp. p. 418). https://dspace.ut.ee/server/api/core/bitstreams/18c0caf0-518f-4329-ad7f-8c2ad121f0cc/content
- SCHOLARLY — Rafał T. Prinke and Mike A. Zuber (2020), study of the Martinus de Delle poem and its ciphers (cited by Lang et al.; not seen).
- POPULAR — Klaus Schmeh, "Ungelöste Verschlüsselungen in einem 300 Jahre alten Manuskript," Cipherbrain, 5 Jan 2021 (five passages, images, transcription file, frequency tables, nomenclator hypothesis). https://scienceblogs.de/klausis-krypto-kolumne/2021/01/05/ungeloeste-verschluesselungen-in-einem-300-jahre-alten-manuskript/

## Unverified claims
- The full citation of Prinke and Zuber (2020) and what it concludes about the ciphers.
- Whether SUB Hamburg has digitized Cod. alchim. 651.
- The total character count of the five passages.
- Petraeus's exact role (author, compiler or owner) and the manuscript's date; "c. 1700" is from the blog post.
- Whether any blog reader's partial solution after January 2021 was accepted.
