+++
title = "Book of Soyga (Aldaraia): the 36 letter-tables"
slug = "book-of-soyga"
kind = "cipher"
era = "16th century (text); Dee's copy owned by 1556"
origin = "England / Latin Europe"
language = "Latin (treatise); the tables are letter-strings"
status = "partial"
confidence = "medium"
digitized = "https://www.bl.uk/manuscripts/"
tags = ["John-Dee", "magic", "letter-square", "algorithm-solved", "calibration-adjacent", "Renaissance-occult"]

[scores]
mystery = 3
material = 4
solvable = 4
compute = 4
verifiable = 4
crowding = 4
+++

# Book of Soyga (Aldaraia): the 36 letter-tables

## What it is
A 16th-century Latin grimoire on incantation, astrology, demonology and angelology, whose distinguishing feature is a set of 36 large square tables of letters at the end. John Dee owned a copy and cared about it intensely: in a scrying session of 1583 he had Edward Kelley put the book to the angel Uriel, who replied (per Dee's record) that it had been revealed to Adam in Paradise and that only the archangel Michael could interpret it. The book then dropped out of sight until Deborah Harkness located two manuscript copies in 1994: Bodleian Library MS. Bodley 908 (197 pp., in the library since 1605) and British Library Sloane MS 8 (147 pp., the copy that was Dee's).

## What is unsolved
The tables' *construction* is solved; their *content* is not, and neither is most of the treatise around them. Jim Reeds showed that each table is generated letter-by-letter from a short keyword by a deterministic rule, so the tables contain no hidden message beyond their seeds — which means the open questions are: what the 36 seed words mean and why those seeds; what the tables were *for* in the ritual economy of the book; whether the surrounding Latin treatise has an identifiable source tradition; and what "Soyga" / "Aldaraia" denote. This is the catalog's cleanest example of a mystery that a computation dissolved in one direction while leaving the humanistic question untouched.

## What survives
Two complete manuscript witnesses (Bodley 908; Sloane MS 8), which Reeds showed descend from a common ancestor, with scribal corruption in both — he could identify and correct copying errors precisely *because* the generation rule makes every letter predictable. That is the strongest available demonstration that the algorithm is right. There is no critical edition and no published machine-readable transcription of the full Latin text that I could verify; Reeds's paper prints the rule and worked table material.

## Prior attempts and current consensus
Before 1994 the book was known only from Dee's diaries and treated as lost. Harkness's rediscovery (published in her work on Dee's angel conversations, and in *John Dee's Conversations with Angels*, CUP 1999) made the object available. Jim Reeds, "John Dee and the Magic Tables in the Book of Soyga," in Stephen Clucas (ed.), *John Dee: Interdisciplinary Studies in English Renaissance Thought* (Springer, 2006) — circulated from 1998 — gives the solution: the first column of each 36×36 table is a fixed sequence derived from the table's keyword, and every subsequent letter is a function of the letter above it and the letter to its left, using a fixed shift table. Run the rule and the whole square regenerates. Consensus accepts this completely; nobody disputes the algorithm. What consensus does *not* offer is a reading of the treatise or an account of the tables' purpose, and there is no monograph on the Soyga text as such, which is why `crowding` is high.

## What a solution would have to do
For the tables: nothing further is needed on construction, but a claim about *meaning* would have to (i) explain the choice of all 36 seed words as a set, not one or two, (ii) tie them to identifiable referents in the treatise or in a known angelological scheme, and (iii) survive the fact that the table interiors are algorithmically determined, so any "message" read out of the body of a table is an artifact. For the book: a solution means a source-critical edition — identify the Latin exemplars behind the incantations and the astrological material, date the compilation, and place it in the known grimoire stemma (Liber Juratus, Ars Notoria, Picatrix, Sworn Book traditions). That is a manuscript-parallel search problem, and a corpus-scale text-reuse sweep over digitized Latin magical manuscripts is a concrete, unexecuted move.

## Why the scores
- mystery 3: the headline puzzle fell in 1998; a real residue of dispute and ignorance remains about content and purpose.
- material 4: two complete witnesses with a reconstructible common ancestor, but no critical edition and no verified open transcription.
- solvable 4: the treatise is ordinary Latin with a determinate meaning; the tables are demonstrably purposeful structures.
- compute 4: the table problem was solved by exactly the kind of combinatorial reasoning this catalog cares about, and the remaining source-parallel question is a corpus sweep — but the interpretive question is not computational.
- verifiable 4: a source identification is checkable word for word; a claim about the seeds' meaning would need scholarly consensus.
- crowding 4: a handful of serious treatments (Harkness, Reeds, Clucas) and no dedicated monograph.

## Sources
- SCHOLARLY — Jim Reeds, "John Dee and the Magic Tables in the Book of Soyga," in S. Clucas (ed.), *John Dee: Interdisciplinary Studies in English Renaissance Thought* (Springer, 2006). https://link.springer.com/book/10.1007/1-4020-4246-6
- SCHOLARLY — Deborah E. Harkness, *John Dee's Conversations with Angels* (Cambridge UP, 1999); the 1994 rediscovery of both copies. https://www.cambridge.org/core/books/john-dees-conversations-with-angels/
- PRIMARY — British Library, Sloane MS 8 (Dee's copy). Catalogue via the BL archives and manuscripts catalogue. https://www.bl.uk/manuscripts/
- PRIMARY — Bodleian Library, MS. Bodley 908. https://medieval.bodleian.ox.ac.uk/
- SECONDARY — Wikipedia, "Book of Soyga" (shelfmarks, page counts, the Uriel exchange, Harkness and Reeds). https://en.wikipedia.org/wiki/Book_of_Soyga

## Unverified claims
- Reeds's paper was not read in full: the earlier preprint URL (dtc.umn.edu/~reedsj/soyga.pdf) 404s and the migrated www-users.cse.umn.edu path also 404s. The statement of the generation rule above is therefore given at the level of "each letter is a function of its neighbours above and to the left, driven by a keyword-derived first column"; the exact shift table and the page range of the printed chapter were not verified.
- The count "36 tables" and their dimension (36×36 is the usually cited figure) come from secondary summary; the encyclopedic source says only "36 large letter-squares."
- Whether either manuscript is digitized and publicly viewable was not confirmed; no page-image URL was found. The `digitized` field points at the BL manuscripts portal, not at an image set.
- Dee's date of acquisition ("by 1556") is from general accounts of his library and was not verified against the 1583 diary or the 1583 library catalogue.
