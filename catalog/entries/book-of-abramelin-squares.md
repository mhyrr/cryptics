+++
title = "The word squares of the Book of Abramelin"
slug = "book-of-abramelin-squares"
kind = "constructed-text"
era = "earliest witnesses c. 1608; claimed for 1458"
origin = "German-speaking lands (Wolfenbüttel, Dresden witnesses); a Hebrew branch"
language = "German, with Hebrew and garbled Hebrew/Latin in the squares"
status = "unsolved"
confidence = "low"
digitized = "https://archive.org/details/bookofsacredmagi00abra"
tags = ["magic", "word-square", "combinatorial", "Hebrew", "Mathers", "collation"]

[scores]
mystery = 3
material = 3
solvable = 3
compute = 5
verifiable = 4
crowding = 4
+++

# The word squares of the Book of Abramelin

## What it is
*The Book of Abramelin* presents itself as the autobiography of Abraham of Worms, who travels to the Egyptian desert, learns a magical and kabbalistic system from an aged mage called Abramelin, and transmits it to his son Lamech. Its final book is a catalogue of word squares: grids of letters, each captioned with an effect ("to walk under water," "to know all things past and future"), to be used after a lengthy purification ritual. Some squares are transparently constructed — the underwater square contains MAIAM, Hebrew for water — and many are not. The squares, not the narrative, are the puzzle.

## What is unsolved
The construction rule and the original state of the squares. As transmitted, the squares are inconsistent: some are full and symmetrical, some have blank cells, some contain letter strings that are not recognisable words in Hebrew, Latin or German, and the witnesses disagree with one another about individual letters. So there are three nested questions. (1) Was there a generative scheme — palindromic, symmetric, acrostic, or keyed on the caption — that produced the squares, or is each an ad hoc composition? (2) Which of the transmitted irregularities are authorial and which are scribal corruption or printer's error? (3) Can the defective squares be completed, and would a completion be checkable? No published study has collated the squares across all witnesses, which is the precondition for any of this.

## What survives
The witnesses are late and divergent. Two German manuscripts at Wolfenbüttel, the earliest, about 1608; two more German copies at Dresden, about 1700 and about 1750; a partial Hebrew manuscript at the Bodleian, about 1740, containing only Book One; and the eighteenth-century French manuscript at the Bibliothèque de l'Arsenal, MS 2351, which S. L. MacGregor Mathers translated in 1897 and which was probably itself copied from a German original. Mathers's *The Book of the Sacred Magic of Abramelin the Mage* is freely available, is the version that made the squares famous, and is defective: it gives three of the four books, transmits a six-month ritual where the German witnesses give eighteen, and reproduces its squares from a single late French copy. Georg Dehn's edition (German 1995; English, *The Book of Abramelin: A New Translation*, Ibis, 2006) gives all four books from the German sources and is the current standard. No critical edition collates the squares of all six witnesses.

## Prior attempts and current consensus
Dehn's edition is the necessary starting point and the only one built on the early German witnesses; his proposal that the author was Rabbi Yaakov Moelin (c. 1365–1427) has been disputed and is not accepted. Stephen Skinner's commentary on the Dehn translation supplies the textual and ritual context. Gershom Scholem treated the work dismissively in the context of Jewish magical literature. Otherwise the squares live almost entirely in the practising occult literature descending from Mathers and the Golden Dawn, where they are used rather than studied. The scholarly consensus is thin: a late-sixteenth or early-seventeenth-century German composition in a Jewish magical frame, with a claimed 1458 date that nobody defends, and squares whose state nobody has systematically described.

## What a solution would have to do
This is a collation problem followed by a constraint problem, and both have hard checks. First, transcribe every square in every witness and publish the machine-readable collation — for each square, a per-cell table of what each witness has. That alone would be a first-order result and is verifiable letter by letter against the manuscript images. Second, from the collation, test for a generative rule: state a candidate scheme (symmetry axis, palindrome, caption-derived key, Hebrew root plus filler), fit it to a training subset, and then *predict* the contents of squares held out of the fitting, including the cells that are blank in one witness but filled in another. That is the Soyga test, and it is the reason this entry scores as it does: a rule that regenerates a witness's squares and correctly fills the gaps in another witness would be close to mechanically decisive. Third, any claim that the squares are meaningful Hebrew must be tested against a control — how often do random letter grids of this size contain strings as Hebrew-like as these? — because the alternative hypothesis is that the intelligible squares are a handful and the rest are filler.

## Why the scores
- mystery 3: a niche question in the history of magic rather than a major field problem, but genuinely unresolved and never seriously attacked.
- material 3: six witnesses across German, Hebrew and French branches, and two published editions; but the witnesses are late, they disagree, no critical edition collates them, and the imaging status of the Wolfenbüttel and Dresden manuscripts was not established.
- solvable 3: the readable squares (MAIAM and its kind) prove that at least some were built on a scheme, but the transmitted corpus is demonstrably corrupt and may be partly filler, so a determinate original may not exist for every square.
- compute 5: the core question is combinatorial and the objects are small discrete grids; collation, rule search and held-out prediction are exactly what computation does, there is an internal check, and nobody has done it. This is the most computationally addressable item in this category.
- verifiable 4: a rule that regenerates one witness's squares and predicts another's gaps would be strong evidence by the standard the Soyga tables set; not 5 because the squares may be individually ad hoc, in which case no single formula exists to find.
- crowding 4: one scholarly edition, one commentary, and an occult literature that uses the squares without studying them; the collation is untouched.

## Sources
- PRIMARY — S. L. MacGregor Mathers (trans.), *The Book of the Sacred Magic of Abramelin the Mage*, London, 1897 (from Arsenal MS 2351; three of four books; defective squares). https://archive.org/details/bookofsacredmagi00abra
- PRIMARY — Bibliothèque de l'Arsenal, MS 2351 (the eighteenth-century French witness Mathers used). https://archivesetmanuscrits.bnf.fr/
- PRIMARY — Herzog August Bibliothek, Wolfenbüttel, the two German manuscripts of c. 1608. https://www.hab.de/
- SCHOLARLY — Georg Dehn (ed.), *The Book of Abramelin: A New Translation*, trans. Steven Guth, Lake Worth: Ibis Press, 2006 (all four books, from the German sources). https://www.redwheelweiser.com/
- SCHOLARLY — Stephen Skinner, commentary and textual apparatus accompanying the Dehn translation.
- SECONDARY — Wikipedia, "The Book of Abramelin" (Abraham of Worms and Lamech; two Wolfenbüttel German manuscripts c. 1608; two Dresden copies c. 1700 and c. 1750; a partial Hebrew manuscript at the Bodleian c. 1740 containing Book One only; Arsenal MS 2351, eighteenth century, probably from a German original; Mathers's three of four books and six-month versus eighteen-month ritual; Dehn 2006; the disputed Yaakov Moelin attribution; the MAIAM example). https://en.wikipedia.org/wiki/The_Book_of_Abramelin

## Unverified claims
- The total number of squares, and how many are blank or defective in each witness. This is the single most important missing fact for this entry and no source consulted supplies it; the `material` and `compute` scores should be revisited once it is known.
- Whether the Wolfenbüttel, Dresden or Bodleian manuscripts are digitized and openly accessible.
- The characterisation of the squares as containing non-words and inter-witness letter disagreement is drawn from the general description of the corpus in the editions' apparatus as reported secondarily, not from a checked collation.
- Gershom Scholem's treatment of the work is cited from general knowledge, not located in this pass.
- Whether any published study has attempted a generative rule for the squares. None was found, which is the basis of the `crowding` score.
