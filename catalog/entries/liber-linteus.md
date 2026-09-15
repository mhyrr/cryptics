+++
title = "Liber Linteus Zagrabiensis (the Etruscan linen book)"
slug = "liber-linteus"
kind = "scripture"
era = "text c. 250 BCE (palaeography); linen radiocarbon c. 390 ± 45 BCE"
origin = "Etruria (found reused on a mummy in Ptolemaic Egypt)"
language = "Etruscan"
status = "partial"
confidence = "medium"
digitized = ""
tags = ["Etruscan", "linen", "ritual-calendar", "longest-text", "Zagreb", "mummy-wrappings"]

[scores]
mystery = 3
material = 3
solvable = 4
compute = 4
verifiable = 3
crowding = 3
+++

# Liber Linteus Zagrabiensis (the Etruscan linen book)

## What it is
The longest surviving Etruscan text and the only ancient linen book (*liber linteus*) that survives at all. It was written in black ink on linen, with red ink used for diacritical marks, in twelve columns functioning as pages, and it survives because the cloth was later cut into strips and reused as the wrappings of a mummy in Ptolemaic Egypt. Palaeography puts the writing about 250 BCE; radiocarbon dates the linen itself to about 390 BCE ± 45 years, so the cloth was old when it was written on, or the dating methods disagree. Roughly 60% of the original text survives: 230 lines, about 1,330 legible words drawn from some 500 distinct roots. It is in the Archaeological Museum in Zagreb, kept in a refrigerated room. A papyrus from the sarcophagus names the mummified woman as possibly Nesi-hensu, wife of a Theban tailor, but later analysis indicates the papyrus postdates the mummy by nearly a century, so the identification is doubtful.

## What is unsolved
What most of it means. Etruscan is not an undeciphered script — the alphabet is read and the language is partly understood — so this is not a decipherment problem of the Linear A kind. It is a vocabulary and syntax problem with a real corpus behind it. The content is identified in outline as a ritual calendar prescribing ceremonies and offerings to named deities across the year: Crap (the Jupiter equivalent), Nethuns (Neptune), Thesan (Dawn) and underworld figures are named, and two unambiguous dates appear, 18 June and 24 September, which suggests a month-by-month structure running from March through February. But the great majority of the ritual vocabulary — the verbs of offering, the names of objects and acts, the grammatical particles that would tell you who does what to whom — is not securely understood, so the book cannot be translated, only paraphrased at the level of its headings.

## What survives
- The object: twelve columns, 230 lines, about 1,330 legible words, roughly 60% of the original, in Zagreb under refrigeration. The strips were separated from the mummy and reassembled, so column order and strip placement are themselves reconstructions.
- Jakob Krall (1892) identified the language as Etruscan and reassembled the text; his complete transcription is reported to be available on archive.org, though the item could not be located in this pass (see Unverified claims).
- Modern treatments: Francesco Roncalli's work on the physical reconstruction; L. B. van der Meer (2007), a word-by-word analysis; Valentina Belfiore (2010), a textual and content study.
- The comparanda that make progress possible are the other long Etruscan ritual texts: the Tabula Capuana (a second ritual calendar, and the closest parallel), the Cippus Perusinus, the Tabula Cortonensis, and the roughly 13,000 short inscriptions of the Etruscan corpus.
- Photographs appear in academic publications and museum documentation; no open high-resolution digital facsimile or machine-readable transcription of the whole book was found.

## Prior attempts and current consensus
The consensus is that the genre is right — this is a liturgical calendar — and that understanding has improved substantially in recent decades through the growth of the Etruscan corpus rather than through any key. The method that works is internal: collocation. A word whose occurrences cluster with a date, a deity name and a recurring verb is constrained by that pattern, and van der Meer's and Belfiore's work is essentially this done by hand across the Liber Linteus and its parallels. No proposed full translation has been accepted. A newcomer reads van der Meer 2007 for the text word by word and Belfiore 2010 for the structure, with the Tabula Capuana alongside.

## What a solution would have to do
This is the entry in this category where a computational attack is most obviously the next move, and the requirements follow from that. A proposed reading of the ritual vocabulary must (i) be derived from the whole Etruscan corpus, not from the Liber Linteus alone: a meaning assigned to a verb must be consistent with every attested occurrence of that verb elsewhere, including the short votive and funerary inscriptions where the context is independently known from the object it is written on; (ii) survive the parallel test against the Tabula Capuana, which is a separate calendar in the same genre and is the only place where the same formulae can be expected to recur in a different arrangement; (iii) produce a consistent morphology — a claim about a case ending or a verbal suffix must hold across the corpus, and its failures must be counted and reported, not passed over; (iv) respect the physical reconstruction, since a reading that depends on a particular strip order must say so and must be robust to the alternatives Roncalli's work leaves open; (v) predict. The strongest available form of confirmation is that a hypothesis about the calendar's structure should let you say what stands in a damaged passage before you read it, and then be checked against the traces. A translation that reads smoothly but cannot survive (i) and (iii) is a paraphrase of the genre, not a reading of the text.

## Why the scores
- mystery 3: the longest Etruscan text, and a real reading would be a significant event in Etruscology; not higher because the genre and much of the frame are already established and the content is liturgical routine rather than history or literature.
- material 3: a substantial text at 230 lines and 1,330 words, which is a great deal by Etruscan standards, but 40% is lost, the strip reconstruction is provisional, access is through print photographs, and there is no open machine-readable transcription.
- solvable 4: certainly a determinate ritual prescription in a language with a known script and a partly known grammar; the main text is not in doubt as text.
- compute 4: the core problem — fixing the meanings of recurring ritual terms by collocation and morphological pattern across a closed corpus of some 13,000 inscriptions plus four long texts — is statistical, the corpus exists in published form, and no modern quantitative treatment appears to have been published. Not 5 because the corpus is not assembled in machine-readable form and because the final semantic assignments need Etruscological judgement.
- verifiable 3: consensus could form on particular lexical items through corpus-wide consistency, and the field has absorbed such results before; but there is no key that either works or fails, so a full reading would be adjudicated by scholarly agreement over years.
- crowding 3: a modest dedicated literature (Krall, Roncalli, van der Meer, Belfiore) sitting inside a very large Etruscan-language literature; the obvious hand methods have been applied, the computational ones have not.

## Sources
- SECONDARY — Wikipedia, "Liber Linteus" (longest Etruscan text and only extant linen book; c. 250 BCE palaeographic date against a radiocarbon date of c. 390 BCE ± 45 for the linen; reuse as mummy wrappings in Ptolemaic Egypt; the Nesi-hensu identification and the century-long discrepancy with the papyrus; the Archaeological Museum in Zagreb and the refrigerated storage; twelve columns, 230 lines, c. 1,330 legible words from c. 500 roots, c. 60% surviving; black ink with red diacritics; identification as a ritual calendar; Crap, Nethuns, Thesan and underworld deities; the dates 18 June and 24 September and the March-to-February structure; Krall 1892, van der Meer 2007, Belfiore 2010). https://en.wikipedia.org/wiki/Liber_Linteus

## Unverified claims
- The archive.org location of Krall's 1892 transcription. The encyclopedic source states it is there; a search of archive.org by Krall's name returned three other works by him and not this one, so the `digitized` field is left empty. Locating it is a five-minute job for the next pass and would raise `material`.
- The figure of roughly 13,000 Etruscan inscriptions in the corpus, used above to size the comparative material — cited from memory, not verified here.
- Whether the Tabula Capuana, Cippus Perusinus and Tabula Cortonensis are available in machine-readable transcription (for example through the Etruscan Texts Project), which determines whether the `compute = 4` score is actionable now or after a digitization effort.
- Francesco Roncalli's specific conclusions about strip order and column reconstruction.
- Whether any proposed full or partial translation published since 2010 has gained acceptance.
