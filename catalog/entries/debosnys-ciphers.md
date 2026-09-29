+++
title = "Debosnys cryptograms (Henry Debosnys, Essex County jail, 1882–83)"
slug = "debosnys-ciphers"
kind = "cipher"
era = "August 1882 – April 1883"
origin = "Elizabethtown, Essex County, New York"
language = "French suspected (Debosnys wrote plaintext in French, English and other languages)"
status = "unsolved"
confidence = "medium"
digitized = "http://cipherfoundation.org/older-ciphers/debosnys-ciphers/"
tags = ["prison", "murderer", "verse", "French", "symbol-cipher", "19th-century", "Adirondacks"]

[scores]
mystery = 2
material = 2
solvable = 4
compute = 3
verifiable = 3
crowding = 3
+++

# Debosnys cryptograms

## What it is
Henry (Henri) Debosnys, a man of uncertain origin who claimed a Lisbon birth c. 1836 and a career in wars and Arctic expeditions, arrived in Essex County, New York, in spring 1882. He married the widow Elizabeth Wells on 8 June 1882, and she was found murdered on 1 August. He was tried on 6–7 March 1883, convicted after eight minutes' deliberation, and hanged on 27 April 1883. In jail he wrote poems (in French, with errors suggesting French was not his first language), made drawings, and wrote cryptograms. Most of the papers went to a woman who visited him; her granddaughter gave them to what is now the Adirondack History Museum in Elizabethtown, and more arrived as late as 1991. His skull and noose are exhibited there.

## What is unsolved
What any of the cryptograms say. Schmeh counts four; not one word has been read. They are the private writing of a condemned man, likely verse, possibly biographical: Pelling notes a pair of clasped hands beside the initials "L.M.F." and dots under the letters of a name.

## What survives
The originals, too fragile to be handled and kept in storage at the museum. High-resolution scans made for Cheri Farnsworth's *Adirondack Enigma* (2010), six images of which are on the Cipher Foundation site. Schmeh's description: cryptogram 1 is six lines in an alphabet of simple symbols; 2 runs over two images; 3 is the shortest and carries French cleartext; 4 looks like an encrypted poem over two images. Wikipedia reports that one enciphered poem has a Greek text on the reverse. No agreed transcription exists, because nobody agrees how to segment the glyphs.

## Prior attempts and current consensus
Pelling's 2015 analysis is the most careful. Many glyphs are built from consistent sub-shapes, suggesting composites (vowel marks attached to consonants, as in a syllabary or shorthand). Cryptogram 4 scans as French alexandrines with visible hemistich breaks and matching end-symbols on rhymed couplets. Few doubled glyphs. His prediction is that the first word read will be *je*, *me* or *moi*. Schmeh judges them unlikely to be simple substitution, possibly homophonic or code. Commenters have floated Masonic elements; Debosnys claimed his cipher "was widely used in Europe." Consensus: unsolved, short, and blocked at transcription.

## What a solution would have to do
Give a glyph segmentation and a key that read at least the verse cryptogram as French. Lines should scan as twelve-syllable alexandrines with the caesura where the manuscript breaks, and the rhyme pairs should fall where the repeated end-symbols fall. That is a check the key-fitting does not get for free. The same key, or a stated family of keys, should read the other cryptograms. Readings should cohere with Debosnys's plaintext French poems and with what the trial record says of his life. A reading that needs a different system for each sheet should be treated as unfalsifiable.

## Why the scores
- mystery 2: a curiosity of Adirondack crime history; a reading would interest biographers of an obscure murderer and cipher hobbyists.
- material 2: four short texts, and the scans are good but not openly available at full resolution; the fragile originals limit fresh imaging.
- solvable 4: intent is plain (verse layout, rhyme-aligned symbols, a French cleartext on one sheet), but the texts may be personal enough to stay opaque.
- compute 3: if Pelling's structural reading is right, metre and rhyme are hard constraints that search can use, and that is real leverage on a short text. Still, the total length is near the unicity distance of a homophonic or syllabic system, and segmentation must come first.
- verifiable 3: alexandrine scansion plus rhyme is a good independent check on the verse text; the other sheets would be judged by plausibility.
- crowding 3: Pelling, Schmeh (his top-50 #3), Bauer's *Unsolved!*, Farnsworth's book, podcasts; a modest literature with the obvious substitution attacks tried.
- compute mode: ENUMERATE (segmentation × syllabic/homophonic key, scored by French metre and rhyme) · verifier STRONG · space SAMPLABLE · signal WEAK · fit MEDIUM: the full-resolution scans need to be obtained from the museum or Farnsworth.

## Sources
- PRIMARY — Debosnys papers, Adirondack History Museum (Essex County Historical Society), Elizabethtown, NY; scans reproduced at the Cipher Foundation. http://cipherfoundation.org/older-ciphers/debosnys-ciphers/
- SECONDARY — Wikipedia, "Henry Debosnys" (biography, dates, trial, museum custody, Greek on reverse of one poem). https://en.wikipedia.org/wiki/Henry_Debosnys
- POPULAR — Nick Pelling, "Thoughts on the Debosnys Ciphers...", Cipher Mysteries, 7 Nov 2015 (composite glyphs, alexandrines, storage status, Farnsworth scans). https://ciphermysteries.com/2015/11/07/thoughts-on-the-debosnys-ciphers
- POPULAR — Klaus Schmeh, "The Top 50 unsolved encrypted messages: 3. The Debosnys cryptograms," Cipherbrain, 6 Jan 2020. https://scienceblogs.de/klausis-krypto-kolumne/2020/01/06/the-top-50-unsolved-encrypted-messages-3-the-debosnys-cryptograms/
- POPULAR — Cheri L. Farnsworth, *Adirondack Enigma: The Depraved Intellect and Mysterious Life of North Country Wife Killer Henry Debosnys* (History Press, 2010).

## Unverified claims
- Total glyph count across the four cryptograms; no source states it.
- Whether the museum holds further unpublished cryptograms among the 1991 accession.
- Debosnys's real identity and birthplace (claimed, not established).
- The Greek text on the reverse of one poem: whether it is a translation of the cryptogram (which would be a crib) or unrelated.
- Whether the Cipher Foundation images are the full-resolution Farnsworth scans or reductions (the page shows images about 300 px wide).
