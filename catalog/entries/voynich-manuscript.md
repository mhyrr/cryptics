+++
title = "Voynich Manuscript (Beinecke MS 408)"
slug = "voynich-manuscript"
kind = "cipher"
era = "vellum radiocarbon-dated 1404–1438"
origin = "probably northern Italy"
language = "unknown (\"Voynichese\")"
status = "unsolved"
confidence = "medium"
digitized = "https://collections.library.yale.edu/catalog/2002046"
tags = ["manuscript", "vellum", "herbal", "astrological", "undeciphered-script", "hoax-hypothesis", "statistics"]

[scores]
mystery = 5
material = 5
solvable = 3
compute = 5
verifiable = 4
crowding = 1
+++

# Voynich Manuscript (Beinecke MS 408)

## What it is
A quarto codex of roughly 240 surviving vellum pages (23.5 × 16.2 × 5 cm), written in an otherwise unattested script and illustrated throughout with plants, nude female figures in pools and pipework, circular cosmological diagrams and zodiacal rosettes. The vellum is radiocarbon-dated 1404–1438; the conventional art-historical placement is northern Italy in the same window. Ownership is documented from the 17th century (Georg Baresch, Jan Marek Marci, who sent it to Athanasius Kircher in 1665/66), with an earlier signature of Jacobus Horcicky de Tepenecz on f1r; Wilfrid Voynich bought it in 1912 from a Jesuit sale at the Villa Mondragone. It has been Beinecke MS 408 at Yale since 1969, fully published online by Yale in 2020.

## What is unsolved
Everything about the text: whether "Voynichese" encodes a natural language under cipher, is an unrecorded language or script, is a constructed language, or is a meaningless but systematically generated hoax. Distinguish three separable questions, because claimants routinely conflate them: (1) is there a determinate plaintext; (2) what generative process produced the observed statistics; (3) what do the pictures depict. A demonstration that the statistics are reproducible by a mechanical generator would answer (2) without answering (1).

## What survives
- The codex itself: about 240 pages of an estimated 272, with roughly 14 folios lost; 18 of 20 quires extant. Six conventional sections (herbal ~126 pp., astronomical ~17, balneological ~20, cosmological ~14 incl. the six-page foldout rosettes, pharmaceutical ~16, recipes ~25).
- High-resolution digitization at Yale (PRIMARY) covering every folio including foldouts.
- Machine-readable transcriptions: the EVA (Extensible Voynich Alphabet) family, descending from Friedman's 1940s punch-card transcription, with the interlinear archive and later IVTFF-format files maintained by René Zandbergen. Transcription is not neutral: glyph-segmentation decisions (is `ch` one glyph or two?) change every statistic computed downstream, and rival transcribers disagree.
- Corpus size commonly cited as ~38,000 word tokens, ~9,000 types, ~170,000 characters.

## Prior attempts and current consensus
Three literatures. (a) Claimed decipherments — Newbold (1921, microscopic anagramming), Feely (1943), Strong (1945), Brumbaugh (1974, Alberti cipher), Stojko (1978, Ukrainian), Bax (2014, bottom-up proper nouns, ten words), Gibbs (2017, Latin abbreviation), Cheshire (2019, "proto-Romance") — none has been independently verified; Cheshire's was disavowed by the publishing university. (b) Statistical description — Currier's two "languages"/hands A and B, Zipf-law conformity at the word level, but a very low second-order character entropy (h2 ≈ 2.0 against 3–4 for natural language) and a rigid prefix–root–suffix word morphology with strong positional constraints. (c) The hoax/mechanical-generation family — Rugg's grille reconstructions and Timm & Schinner's self-citation model, which reproduce much of the word-level statistics from a copying process, and which the field treats as a live rival to any linguistic reading. Recent work has run the other way too: a 2025 proof-of-concept verbose cipher ("Naibbe", Nick Pelling) shows a 15th-century-plausible mechanism that could yield the observed low entropy from Latin or Italian plaintext, offered as a mechanism and explicitly not as a decipherment. Lisa Fagin Davis's palaeographic work assigning the writing to five scribes is the most consequential recent material finding, because a hoax model must now explain coordinated production. A newcomer should read Zandbergen's voynich.nu, Timm & Schinner, and the Davis scribal analysis before anything else.

## What a solution would have to do
State the mapping from glyph sequences to plaintext before applying it, then decode continuously — not word-picked — across at least two folios from different sections and different Currier hands, and publish the mapping so a third party can decode a third folio the claimant has not seen. It must account for: the low h2 entropy; the prefix–root–suffix positional morphology; the near-absence of the doubled and single-letter words natural languages have; line-initial and line-final glyph preferences (the "line as a functional unit" effect); the A/B vocabulary split across five scribal hands; label words attached to individual plants and stars, which are the only place the pictures constrain the text and which any reading must get right. A decipherment that yields herbal recipes should produce plant names that match the picture on the same page more often than chance. Conversely, a hoax proof would have to exhibit a generator, plausible with 15th-century materials, that reproduces the entropy profile *and* the morphology *and* the A/B split, and explain why five scribes ran it consistently over 240 pages. Either way the check is mechanical and the data is public; this is why `compute` is 5 and `crowding` is 1.

## Why the scores
- mystery 5: the central question is entirely open and a real solution would be an event well outside palaeography.
- material 5: near-complete codex, fully digitized, multiple machine-readable transcriptions.
- solvable 3, not 4: serious, technically competent people hold the "meaningless generated text" position, and the entropy evidence genuinely supports them.
- compute 5: the question is statistical and combinatorial, the corpus is ready, and generative-model comparison against candidate mechanisms is the obvious unexecuted program.
- verifiable 4, not 5: a full key that decodes unseen folios would be recognized instantly, but the hoax branch can only be settled by consensus about a generator, not by a mechanical check.
- crowding 1: the densest crank ecosystem of any text in this catalog; every naive substitution has been tried thousands of times.

## Sources
- PRIMARY — Beinecke Rare Book & Manuscript Library, MS 408, Yale digital collections (full facsimile). https://collections.library.yale.edu/catalog/2002046
- PRIMARY/SCHOLARLY — René Zandbergen, *The Voynich Manuscript* (analysis site, provenance, transcription formats, IVTFF). https://www.voynich.nu/
- SCHOLARLY — Torsten Timm & Andreas Schinner, "A possible generating algorithm of the Voynich manuscript," *Cryptologia* 44 (2020). https://www.tandfonline.com/doi/abs/10.1080/01611194.2019.1596999
- SCHOLARLY — Lisa Fagin Davis, "How Many Glyphs and How Many Scribes? Digital Paleography and the Voynich Manuscript," *Manuscript Studies* 5 (2020). https://repository.upenn.edu/mss_sims/vol5/iss1/6/
- SECONDARY — Wikipedia, "Voynich manuscript" (radiocarbon range, section counts, claim-by-claim reception, entropy figures). https://en.wikipedia.org/wiki/Voynich_manuscript
- CLAIMANT — Stephen Bax, "A proposed partial decoding of the Voynich script" (2014). https://stephenbax.net/?p=1447
- CLAIMANT — Nick Pelling, "Naibbe" verbose-cipher proof of concept (2025), Cipher Mysteries. https://ciphermysteries.com/

## Unverified claims
- The Yale catalog record at collections.library.yale.edu/catalog/2002046 is reached by 302 redirect from the older Beinecke digital-library record 3519597, but the page did not render to automated fetch; the title, call number and foliation as printed on that record were therefore not read directly.
- The "five scribes" figure is Davis's; I did not read her paper directly and the count of distinct glyphs she defends was not verified here.
- A 2023 deep-learning study reported that Voynichese glyph shapes most resemble the Khojki script among a seven-script sample. Reported in the Wikipedia article; the primary study was not read and the finding is scriptological, not linguistic.
- Word/type/character counts (~38,000 / ~9,000 / ~170,000) are transcription-dependent and were taken from the encyclopedic summary, not recomputed.
- Exact page range and DOI for the Timm & Schinner article were not confirmed.
