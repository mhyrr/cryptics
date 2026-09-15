+++
title = "Cicada 3301 Liber Primus (the unsolved runic pages)"
slug = "cicada-3301-liber-primus"
kind = "cipher"
era = "2012–2014 (published); last verified signed message April 2017"
origin = "internet (4chan, Twitter, Tor hidden services); authorship unknown"
language = "English, enciphered in Anglo-Saxon runes"
status = "unsolved"
confidence = "low"
digitized = "https://github.com/rtkd/iddqd"
tags = ["modern-puzzle", "runes", "ARG", "born-digital", "author-unknown", "designed-to-be-solved"]

[scores]
mystery = 2
material = 4
solvable = 4
compute = 4
verifiable = 4
crowding = 2
+++

# Cicada 3301 Liber Primus (the unsolved runic pages)

## What it is
*Liber Primus* is a book of pages, published as images by the anonymous group or person signing as "3301," written in Anglo-Saxon futhorc runes and encrypted. It belongs to the third of three recruitment-style puzzle sets: the first was posted to 4chan on 4 January 2012, the second on 4 January 2013, the third to Twitter on 4 January 2014. The 2014 puzzle — of which *Liber Primus* is the core — has never been finished. Cicada 3301's last message verified by its OpenPGP signature was posted in April 2017, disavowing all unsigned material. Solvers who completed earlier rounds reported being asked about their views on information freedom and privacy.

## What is unsolved
Most of *Liber Primus* remains undecrypted. A minority of pages have yielded English text — the introductory and "warning" material and a handful of others — using a running-key or Vigenère-style scheme over the rune alphabet, where runes are given index values by the group's own published table (commonly called the Gematria Primus, which pairs each futhorc rune with a Latin transliteration and a prime number). The keys used on solved pages have been derived from the puzzle's own text and from number-theoretic constructions. The remaining pages resist the same attack, which means either the key material is external and not yet found, or the scheme changes, or later pages are differently constructed. It is also not established that the unsolved pages are solvable at all with what has been released — the author may have withheld a needed key, and since April 2017 there has been no authenticated party to ask.

## What survives
The complete set of released page images, mirrored widely; an archive of "every image used in the Liber Primus" was uploaded to the Internet Archive on 29 November 2020. The community repository `rtkd/iddqd` on GitHub holds unmodified files plus a master transcription of the runic text, which is the practical machine-readable corpus. Solver discussion, tooling and partial decryptions live in community wikis and Discord/Reddit archives of varying reliability. Material conditions are therefore good in the ways that matter computationally — the corpus is born-digital, exact, and transcribed — and poor in provenance: there is no authoritative statement of how many pages exist, how many are solved, or what counts as canonical.

## Prior attempts and current consensus
A large volunteer community has worked this continuously since 2014, has published the Gematria Primus mapping, has decrypted the early pages, and has built substantial tooling for key search over rune-index arithmetic. The consensus within that community is that the puzzle is genuine (the PGP signature chain is the evidence), that the solved pages demonstrate the general cipher family, and that the unsolved pages need a key nobody has identified. There is essentially no academic literature; this is an amateur-expert field, and its record is distributed across forums rather than papers, which is the main reason this entry's `confidence` is low and its `crowding` only 2 — heavily worked by non-specialists, barely touched by anyone with formal cryptanalytic training publishing results.

## What a solution would have to do
Decrypt a currently unsolved page to coherent English, and state the key and the derivation of that key from material the author published — not a key fitted to produce a desired output. The held-out test is natural and strong here: a correct key-derivation principle should then decrypt a *second* unsolved page without further tuning, and the community's existing partial decryptions provide an unusually clean ground truth to calibrate against. Any claim must survive the signature test on provenance (does the page come from a 3301-signed release?) and must not depend on modifying the transcription. A negative result would also be a result, and is achievable: demonstrate that the unsolved pages' rune-index statistics are inconsistent with running-key encryption of English under any key of a stated family, or that they are consistent with random rune generation — which would establish that the remaining pages are filler or that the needed key was never released.

## Why the scores
- mystery 2: a modern puzzle whose resolution would matter to its community and to nobody else; the interest is methodological, not historical.
- material 4: born-digital, exact, transcribed, mirrored; not 5 because there is no authoritative canon of which pages belong and the transcription is community-maintained.
- solvable 4: designed to be solved, and part of it demonstrably has been — strong internal evidence of purposeful construction. Not 5 because the needed key may never have been published and the author has been silent since 2017.
- compute 4: rune-index key search is exactly a machine problem, and a rigorous statistical test of "is this even encrypted English" has not been published. Not 5 because the likely bottleneck is a missing external key, which computation cannot manufacture.
- verifiable 4: English out of runes is recognizable, and a key that generalizes to a second page is a strong criterion.
- crowding 2: thousands of amateur hours and an active community; but no published professional cryptanalysis, so the field is emptier than it looks.

## Sources
- PRIMARY — `rtkd/iddqd`, "3301 — Unmodified files, transcription and other assets" (GitHub): the community's canonical image set and master runic transcription. https://github.com/rtkd/iddqd
- PRIMARY — "Liber Primus" image library, Internet Archive (uploaded 29 November 2020). https://archive.org/details/liber-primus
- SECONDARY — Wikipedia, "Cicada 3301" (puzzle dates 4 Jan 2012 / 2013 / 2014, "the third puzzle remains unsolved," April 2017 final signed message, the privacy/information-freedom questions put to solvers). https://en.wikipedia.org/wiki/Cicada_3301

## Unverified claims
- The total page count of *Liber Primus* and the number of solved versus unsolved pages. Figures around 58–74 pages total with roughly the first 19 solved circulate in community sources; none was verified. The Wikipedia article gives no counts, the GitHub directory listing did not expose a per-page file list to automated fetch, and the Uncovering Cicada wiki returned HTTP 402.
- The Gematria Primus as described — a futhorc-to-Latin-to-prime mapping published by 3301 — was not verified from a primary release; it is reported from community consensus.
- That the solved pages use a running-key/Vigenère scheme over rune indices, and that keys were derived from totient and prime constructions, is community knowledge, not verified here against a primary write-up.
- The claim that solved pages' plaintexts are philosophical/instructional in content was not verified.
- Whether any 3301-signed release after April 2017 exists. The encyclopedic source says April 2017 is the last verified signed message; nothing later was checked.
- Whether the 2012 and 2013 puzzles were "solved" in the sense of a solver being contacted is reported in secondary accounts and not verified.
