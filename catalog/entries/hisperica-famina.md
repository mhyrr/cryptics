+++
title = "Hisperica Famina"
slug = "hisperica-famina"
kind = "constructed-text"
era = "mid-7th century"
origin = "Ireland or western Britain (disputed)"
language = "Hiberno-Latin"
status = "partial"
confidence = "low"
digitized = ""
tags = ["Hiberno-Latin", "deliberate-obscurity", "glossaries", "Greek loanwords", "school-text", "source-sweep"]

[scores]
mystery = 3
material = 3
solvable = 4
compute = 4
verifiable = 4
crowding = 4
+++

# Hisperica Famina

## What it is
A group of Latin compositions — described in the standard account as "rhetorical descriptive poems couched in a kind of free verse" — written in an extravagantly obscure register that became the type-specimen of what is now called Hisperic or Hiberno-Latin style. The title itself is a coinage, blending *Hibernia* with *Hesperides*, and is a sample of the manner it names. The pieces describe ordinary things — a day's course, a wind, a sky, a wave, a chapel, a writing tablet — in vocabulary drawn from glossaries, with Greek and Hebrew loanwords, invented compounds and rare or ghost words used as though they were ordinary, and with syntax stretched to the limit of construability. The conventional date is the mid-seventh century.

## What is unsolved
Three things, none of them the literal sense, which Michael Herren's editions supply. (1) **Where the vocabulary comes from.** The Hisperic lexicon includes words attested nowhere else, words attested only in glossaries, and words used in senses no dictionary supports; the received explanation is that the authors learned Latin from bilingual glossaries that did not distinguish common from freak words, but this has not been demonstrated word by word against the surviving glossary corpus. (2) **Where and by whom it was written.** Irish, British and Continental origins have all been argued, and the question matters because the text is the principal evidence for a whole stylistic tradition. (3) **What it was for.** Candidate answers in the literature: a school exercise in *copia*; a display of learning for an audience of rivals; a deliberate parody of Continental, Roman-oriented Latin stylists, blending their tricks with incompetent scansion to ridicule them; and a form of protective or initiatory obscurity. These are not compatible, and the choice between them is the interpretive question.

## What survives
Four recensions are conventionally distinguished — the A-text (the longest), the B-text, and the shorter C and D texts — surviving in a small number of manuscripts. Michael W. Herren's *The Hisperica Famina* in two volumes, published by the Pontifical Institute of Mediaeval Studies (vol. I, the A-text, 1974; vol. II, related poems, 1987), is the critical edition with translation and commentary and is where any work must start; F. J. H. Jenkinson's *Hisperica Famina* (Cambridge, 1908) is the earlier edition. Cognate texts in the same register — the *Lorica* of Laidcenn, *Altus Prosator*, the *Adelphus adelpha meter* poem — provide the comparative material. The Latin glossary tradition that the vocabulary is supposed to come from is largely digitized and searchable (Corpus Glossariorum Latinorum, the Library of Latin Texts, Corpus Corporum, DMLBS).

## Prior attempts and current consensus
The text was made usable by Jenkinson and then by Herren, whose edition, translation and lexical commentary converted it from a curiosity into a readable document; Michael Lapidge and Michael Winterbottom have written on the style and its diffusion, and the register's influence on Aldhelm and on Anglo-Latin generally is the main reason the field cares. The consensus is that the obscurity is deliberate and rhetorical, not a symptom of incompetence; that the style is associated with seventh-century Irish learning even where individual texts' origins are disputed; and that the parody hypothesis, though repeated, is not established. Herren was still publishing on the corpus recently, which indicates the questions are live rather than closed.

## What a solution would have to do
This is the entry in the category where the open question is most nearly computational, and the concrete unattempted work is a lexical provenance study. (1) Extract every lexical item in the A-text that is rare, unattested or used anomalously, and match it exhaustively against the glossary corpora, the Greek–Latin glossaries, the Irish glossaries (Sanas Cormaic and the O'Mulconry glossary), and the Late Antique poets, reporting for each word: source found, source not found, or source found with a different sense. The existing claim — that the vocabulary is glossary-derived — becomes a testable proposition with a number attached, and the residue of unmatched words becomes the real problem. (2) On origin: the same matching, partitioned by which glossary traditions the matches come from, is evidence about milieu that does not depend on stylistic impression. (3) On purpose: the parody hypothesis makes a checkable prediction — that the metrical and syntactic failures cluster where the imitated model's mannerisms cluster — and a scansion analysis of the whole A-text against the Continental models would support or kill it. (4) Any reading must handle the B, C and D texts, not only the A-text, and state whether they are by the same hand or the same school. A proposal that the obscurity encodes a message, rather than performs difficulty, would have to produce that message under a stated rule applied to the whole text.

## Why the scores
- mystery 3: the text is edited and translated, so the central question is not "what does it say" but "where is it from, what is it for, and where did the words come from" — a real residue of dispute, not a wide-open field.
- material 3: a substantial text with a modern critical edition and translation, but few manuscripts, four recensions whose relations are unclear, and no open digitization; the edition is print-only.
- solvable 4: the text demonstrably means things — Herren translated it — and the open questions are about provenance and purpose, which are the kind of question evidence settles.
- compute 4: the core open question (lexical provenance) is a mass source-parallel sweep against corpora that are already machine-readable, and it is the obvious next move nobody appears to have made at scale. Not 5 because the interpretive question about purpose would survive the sweep.
- verifiable 4: a source match is a hard result — a word either appears in a glossary with that sense or it does not — and a provenance profile would explain multiple independent features at once.
- crowding 4: a handful of serious treatments (Jenkinson, Herren, Lapidge, Winterbottom) and no crowd; the field is small and the lexical work is undone.

## Sources
- PRIMARY — Michael W. Herren, ed. and trans., *The Hisperica Famina: I. The A-Text*, Studies and Texts (Pontifical Institute of Mediaeval Studies, 1974); *II. Related Poems* (PIMS, 1987).
- PRIMARY — F. J. H. Jenkinson, ed., *The Hisperica Famina* (Cambridge University Press, 1908).
- SCHOLARLY — Pontifical Institute of Mediaeval Studies, lecture listing for Michael Herren, "Hisperica Famina III: Incipit, Finit, Amen?", confirming Herren's continuing work on the corpus. https://pims.ca/event/herren-hisperica-famina/
- SECONDARY — Wikipedia, "Hiberno-Latin" / "Hisperic Latin": the characterisation of the *Hisperica Famina* as "rhetorical descriptive poems couched in a kind of free verse," the *Hibernia*+*Hesperides* etymology of the title, the glossary-derived-vocabulary explanation, the Greek and Hebrew loanwords, the parody hypothesis (flagged in the article as needing a citation), and Herren's 1974 and 1987 volumes. https://en.wikipedia.org/wiki/Hisperic_Latin

## Unverified claims
- **`confidence` is low because the bibliographic and codicological facts could not be verified directly.** The PIMS catalogue pages for Herren's volumes returned 404 or 403 to automated fetches; the volume titles, years and series are reported from the secondary source and from the standard bibliography.
- The four-recension scheme (A, B, C, D) and the claim that the A-text is the longest are from general reference knowledge; no source consulted enumerated the recensions.
- The manuscript count and locations were not established at all.
- The mid-seventh-century date is conventional; no dating argument was located, and the article consulted gives only the 6th–12th-century span of Hiberno-Latin generally.
- The parody hypothesis is quoted from a Wikipedia passage that the article itself flags as uncited.
- The attribution of stylistic studies to Lapidge and Winterbottom is from the standard bibliography, not from a fetched source.
- Whether the glossary-provenance sweep described above has in fact been attempted — for instance inside Herren's lexical commentary — was not established. If Herren's apparatus already does this word by word, the `compute` score should fall to 3 and the `crowding` score to 3.
