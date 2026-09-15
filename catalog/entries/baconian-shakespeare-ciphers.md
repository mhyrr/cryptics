+++
title = "The claimed Baconian ciphers in Shakespeare (1888–1957)"
slug = "baconian-shakespeare-ciphers"
kind = "attribution"
era = "claims 1888–1950s; texts 1590s–1623"
origin = "USA and Britain; claims about London printings"
language = "English"
status = "likely-noise"
confidence = "medium"
digitized = ""
tags = ["calibration", "likely-noise", "method-artifact", "Friedman", "Shakespeare-authorship", "crank-filter"]

[scores]
mystery = 1
material = 5
solvable = 1
compute = 4
verifiable = 5
crowding = 1
+++

# The claimed Baconian ciphers in Shakespeare (1888–1957)

## What it is
A body of claims, running from the late nineteenth century to the mid twentieth, that Francis Bacon concealed cipher messages in the printed texts of Shakespeare's plays and poems announcing his authorship and other secrets. The three principal systems: Ignatius Donnelly's arithmetical word-counting cipher in *The Great Cryptogram* (1888); Orville Ward Owen's "word cipher," worked with a large mechanical cipher wheel and published as *Sir Francis Bacon's Cipher Story* (1893–95), which produced a secret Elizabethan history in which Bacon was Elizabeth I's illegitimate son; and Elizabeth Wells Gallup's biliteral cipher, read out of the italic and roman typefaces of the First Folio, which produced similar revelations. Owen believed the cipher directed him to buried manuscripts and excavated the bed of the River Wye near Chepstow Castle from 1909 until his death in 1924, finding nothing. Gallup's backer George Fabyan won a 1916 lawsuit in which a judge held that her ciphers proved Bacon's authorship.

## What is unsolved
Nothing. The entry is in the catalog as a `likely-noise` calibration case, and it is the most important one for the crank filter the repository's rules describe. What makes it valuable is not that the claims were wrong but *how* they were shown to be wrong: William and Elizebeth Friedman, two of the ablest cryptanalysts of the twentieth century, examined every proposed system in *The Shakespearean Ciphers Examined* (1957) and demonstrated that none of them is a cipher at all. Their argument was not that the plaintexts were implausible but that the methods carried enough free parameters — choice of starting point, direction, counting rule, permitted substitutions, latitude in identifying typefaces — that they could be made to yield any desired message from any sufficiently long text. A method with that many degrees of freedom does not have a solution; it has an operator.

## What survives
The complete evidence base, on both sides. The 1623 First Folio and the quartos survive in many copies and are fully digitized with machine-readable transcriptions (the Folger's and the Internet Shakespeare Editions'; the Folger holds the largest First Folio collection and much of the Baconian cipher literature and apparatus). Donnelly's, Owen's and Gallup's books survive and state their methods in enough detail to be reimplemented. Owen's cipher wheel and Gallup's typeface classifications survive as documented objects. The Friedmans' book survives and is the standard treatment. There is nothing to recover and nothing missing.

## Prior attempts and current consensus
Donnelly's system collapsed almost immediately under arithmetical scrutiny — his own numbers could not be reproduced by others from his stated rules. Gallup's biliteral reading depends on classifying each italic letterform in the Folio into one of two founts, a judgement that the physical evidence of the printing does not support: the Folio was set from mixed sortes with worn and substituted types, so the "cipher" is largely a record of the classifier's decisions. Owen's word cipher is an unconstrained search. The Friedmans' 1957 verdict — that none of the ciphers claimed by Baconians is valid, and that the methods are unlikely to have been employed by any author — closed the question in mainstream scholarship and has not been reopened. All claimed ciphers remain rejected; the Shakespeare authorship question survives in other, non-cryptographic forms, which the catalog treats separately.

## What a solution would have to do
This section is written here as a standard, because the Friedmans effectively wrote the catalog's crank filter and their criteria transfer to every entry in it. A claimed hidden message in a text must: (a) state the key and the rule completely, in advance, so that a second analyst working independently from the stated rule recovers the same plaintext — reproducibility by a stranger is the whole test; (b) have no free parameters chosen after the plaintext is known, and where parameters exist, their number must be counted and the resulting search space compared against the length of the recovered message, since a message shorter than the information needed to specify the method is not evidence; (c) survive a control experiment — the same method applied to texts the author cannot have written must fail to produce comparable plaintext, and if it succeeds, the method is refuted; (d) be consistent with the physical evidence of the witness, which for a typographic cipher means the compositorial and type evidence of the actual printing, not a reader's impression of the letterforms; and (e) explain why the concealer would use a method that no contemporary is known to have used. The control experiment in (c) is cheap, decisive and computational, and almost no claimant has ever run it.

## Why the scores
- mystery 1: effectively resolved for nearly seventy years; the residual belief is popular, not scholarly.
- material 5: the Folio and quartos are fully digitized and machine-readable, and the claimants' own methods and apparatus survive in full.
- solvable 1: the strongest band for "the meaning is unrecoverable by construction" — the methods are demonstrably capable of producing any message, so there is nothing determinate to find.
- compute 4: the refutation is computational and reusable — reimplement Owen's and Gallup's rules, run them over control corpora, and measure how much plaintext they will yield from texts Bacon did not write. Doing this and publishing the numbers would be a genuinely useful piece of work and a template for the rest of the catalog; not 5 because the conclusion is already known.
- verifiable 5: the Friedman criteria are mechanical, and a claim either reproduces under an independent analyst or does not.
- crowding 1: thousands of attempts across a century and a half, with an active ecosystem that the Friedmans' verdict did not dislodge.

## Sources
- SECONDARY — Wikipedia, "Baconian theory of Shakespeare authorship" (Donnelly's *The Great Cryptogram*; Owen's *Sir Francis Bacon's Cipher Story* 1893–95, the cipher wheel, the claim that Bacon was Elizabeth's son, and the River Wye excavation from 1909 to Owen's death in 1924; Gallup's biliteral cipher in the First Folio and her influence on Dodd and Dawbarn; Fabyan's 1916 suit against William Selig in which the judge held Gallup's ciphers proved Bacon's authorship; William and Elizebeth Friedman, *The Shakespearean Ciphers Examined* (1957), concluding that none of the claimed ciphers is valid and that the methods are unlikely to have been used by the author; all claimed ciphers rejected by academic scholars). https://en.wikipedia.org/wiki/Baconian_theory_of_Shakespeare_authorship
- SCHOLARLY — W. F. Friedman and E. S. Friedman, *The Shakespearean Ciphers Examined* (Cambridge UP, 1957) — the decisive treatment; cited from the secondary source, not read directly.
- CLAIMANT — I. L. Donnelly, *The Great Cryptogram* (1888); O. W. Owen, *Sir Francis Bacon's Cipher Story* (1893–95); E. W. Gallup, *The Bi-literal Cypher of Sir Francis Bacon* (1899) — the claims, by their proposers.
- PRIMARY — The 1623 First Folio; the Folger Shakespeare Library's digitized copies and transcriptions. No specific URL was verified in this pass.

## Unverified claims
- The date of Donnelly's *The Great Cryptogram* is given as 1888 here; the secondary source's summary says 1880, which appears to be an error in that summary. Not resolved against a bibliographic record.
- The characterisation of Gallup's method as depending on classifying mixed and worn types is a standard part of the Friedman argument as usually reported, but was not verified against the Friedmans' text.
- The Folger Shakespeare Library's holdings of Baconian cipher material, and its status as the largest First Folio collection, are from general reference; the secondary source consulted does not mention the Folger.
- Elizebeth Friedman's forename is spelled "Elizebeth"; the secondary summary renders it "Elisabeth" in one place. The standard spelling is used above.
- Whether anyone has published the control-corpus reimplementation described in "What a solution would have to do" is unknown to this entry.
