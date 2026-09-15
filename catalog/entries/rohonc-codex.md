+++
title = "Rohonc Codex"
slug = "rohonc-codex"
kind = "cipher"
era = "paper of Venetian manufacture, 1530s; text probably c. 1593"
origin = "Hungary (Batthyány family library, Rohonc / Rechnitz)"
language = "claimed: a Hungarian-language devotional text in a non-alphabetic code"
status = "partial"
confidence = "medium"
digitized = "https://real-ms.mtak.hu/"
tags = ["manuscript", "Hungary", "code-not-cipher", "breviary", "forgery-hypothesis", "Tokai-Kiraly"]

[scores]
mystery = 3
material = 3
solvable = 4
compute = 4
verifiable = 4
crowding = 4
+++

# Rohonc Codex

## What it is
A small paper codex of 448 pages (c. 12 × 10 cm), 9–14 rows of an unknown script per page, with 87 illustrations of religious, secular and military subjects. The paper is Venetian, watermark-dated to the 1530s, which dates the support and not the writing. It belonged to the Batthyány library at Rohonc (now Rechnitz, Austria) and was donated to the Hungarian Academy of Sciences in 1838 by Count Gusztáv Batthyány, where it remains, with restricted physical access; microfilm and digital surrogates are held in the Academy's REAL repository.

## What is unsolved
Two things, now separable. First, authenticity: from 1866 the Hungarian mainstream followed Károly Szabó in ascribing the codex to the forger Sámuel Literáti Nemes (1796–1842), and no evidence has ever tied the object to him specifically. Second, the reading. Gábor Tokai and Levente Zoltán Király's work since 2018 has moved this from "undeciphered" to "partially read": they argue the script is not a letter substitution but a code — signs stand for words and morphemes, with no word-internal structure marked — and they have identified substantial content as a Catholic devotional compilation. What is *not* settled is a complete, sign-by-sign lexicon that reads every page, and the field has not ratified their reading as final.

## What survives
The codex is complete as an object. Roughly 792 distinct signs have been counted, far too many for an alphabet and consistent with a syllabary or, on the Tokai–Király account, a word-level code. The illustrations are a partial crib: they depict identifiable Christian scenes, which constrains the adjacent text. Digitization is the weak point — the Academy's repository holds surrogates and Hamburg University rescanned eight pages at higher resolution in 2015, but there is no verified complete high-resolution open facsimile, and no published machine-readable transcription of the full sign sequence that I could confirm. This is the single largest obstacle to independent verification and is the reason `material` is 3, not 4.

## Prior attempts and current consensus
Three discredited decipherments: Attila Nyíri (1996, Sumerian ligatures yielding Hungarian), Viorica Enăchiuc (2002, an 11th–12th-century Daco-Romanian chronicle), Mahesh Kumar Singh (2004, an undocumented Brahmi variant yielding a Hindi apocryphal gospel). Each was criticized on the same ground: transliteration was not applied consistently, so the method could produce any desired output. Benedek Láng's work (2010–11, including *Why Don't We Decipher an Outdated Cipher System? The Codex of Rohonc*) shifted the scholarly frame from "forgery" to "deliberate encipherment" and set out the candidate hypotheses — cipher, shorthand, artificial language — as things to be tested rather than asserted. Tokai and Király then published "Cracking the code of the Rohonc Codex," *Cryptologia* 42(4): 285–315 (2018), followed by further structural papers through 2020–22; they propose 1593 as a probable composition date and read the content as a breviary-like compilation with paraphrased Gospel material plus non-biblical matter (Seth at the gate of Paradise, Marian prayers). Reception: the code-system hypothesis is taken seriously and has been built on; no full translation consensus exists. A newcomer reads Láng first, then the 2018 *Cryptologia* paper.

## What a solution would have to do
Publish the complete sign inventory with a stable numbering, and a sign-to-word lexicon, then read continuous text across pages the lexicon was not fitted on — the standard held-out test, which is exactly what the 1996–2004 claimants failed. Because the proposed plaintext is devotional, the reading is unusually checkable: it must produce recognizable Latin-liturgical or Hungarian-vernacular formulae (Pater Noster, Ave Maria, Gospel pericopes) in the right places, and those formulae must land next to the illustrations that depict them. It must explain the sign count (~792) as a coherent system rather than a residue, account for the direction of writing and the line structure, and cope with the paper-versus-text date gap (1530s paper, claimed 1593 text). A forgery verdict would now need positive evidence: Nemes's hand, his materials, or a source he copied — absence of provenance is not enough against a reading that produces coherent liturgical Hungarian.

## Why the scores
- mystery 3: partly resolved. The structural question is answered in outline and a large share of content is claimed; the residue of dispute is real but the headline is no longer wide open.
- material 3: complete codex, but restricted access, no verified complete high-resolution facsimile, and no confirmed open transcription.
- solvable 4: strong internal evidence of design — a stable 792-sign system, illustrations that match a devotional programme, and a reading that produces coherent religious content.
- compute 4: with a transcription this becomes a code-breaking and text-reuse problem against the digitized corpus of 16th-century Hungarian and Latin devotional literature. That sweep is the obvious next move and is gated on transcription, not on method.
- verifiable 4: a lexicon that reads held-out pages, checked against known liturgical texts, is close to a mechanical test; not 5 because a word-level code has more freedom than a letter cipher.
- crowding 4: a handful of serious treatments (Láng, Tokai, Király) plus discredited amateur claims; no dedicated monograph in English.

## Sources
- SCHOLARLY — Gábor Tokai & Levente Zoltán Király, "Cracking the code of the Rohonc Codex," *Cryptologia* 42(4): 285–315 (2018). https://doi.org/10.1080/01611194.2018.1449147
- SCHOLARLY — Benedek Láng, "Why Don't We Decipher an Outdated Cipher System? The Codex of Rohonc," *Cryptologia* 34(2) (2010). https://doi.org/10.1080/01611191003605718
- PRIMARY — Hungarian Academy of Sciences Library, REAL manuscript repository (surrogates of the codex). https://real-ms.mtak.hu/
- SECONDARY — Wikipedia, "Rohonc Codex" (448 pages, 87 illustrations, ~792 signs, 1530s Venetian paper, 1838 donation, the Nemes hypothesis, claimant history, 2015 Hamburg rescans). https://en.wikipedia.org/wiki/Rohonc_Codex

## Unverified claims
- The *Cryptologia* article page and abstract could not be fetched (publisher returned 403); the title, volume, issue and page range above are from the encyclopedic citation and were not read at the publisher.
- The 1593 composition date is Tokai and Király's inference, reported at second hand; the evidence for it was not examined.
- "~792 distinct signs" and "448 pages / 87 illustrations" are encyclopedic figures, not recounted from the object.
- Whether the REAL repository holds a complete open facsimile, and under what identifier, was not confirmed; the `digitized` field points at the repository root.
- The extent of the Tokai–Király reading — what fraction of the 448 pages they claim to read — was not established from a primary source and should be pinned before this entry's `mystery` and `status` are trusted.
- Láng's later book-length treatment of early modern ciphers (*Real Life Cryptology*, 2018) presumably discusses the codex; not verified.
