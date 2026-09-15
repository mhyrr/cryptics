+++
title = "Chaocipher exhibits (John F. Byrne, 1918–1953; algorithm revealed 2010) — calibration case"
slug = "chaocipher"
kind = "cipher"
era = "invented 1918; challenge exhibits published 1953; algorithm revealed 2010"
origin = "United States (John F. Byrne)"
language = "English"
status = "solved"
confidence = "low"
digitized = "https://www.mountainvistasoft.com/chaocipher/"
tags = ["calibration", "solved-by-archive", "challenge-cipher", "secret-algorithm", "Cryptologia", "Moshe-Rubin", "20th-century"]

[scores]
mystery = 1
material = 2
solvable = 5
compute = 3
verifiable = 5
crowding = 4
+++

# Chaocipher exhibits (John F. Byrne, 1918–1953; algorithm revealed 2010) — calibration case

## What it is
John F. Byrne invented the Chaocipher in 1918, believed it simple and unbreakable, and spent decades unsuccessfully trying to interest the US government in it. In his 1953 autobiography *Silent Years* he published four "exhibits" — enciphered messages — and offered a cash reward to anyone who could break them, without disclosing the algorithm. The algorithm stayed secret for ninety years, known to a handful of people. It is a dynamic-substitution system: two 26-letter alphabets, conventionally pictured on rotating disks, the right holding plaintext and the left ciphertext; after each character both alphabets are permuted by a fixed rule involving letters at the zenith and nadir positions, so the substitution table changes every letter. Decryption is the same procedure run from the left disk to the right.

## What is unsolved
Nothing about the system. This entry is a calibration case and it is the most uncomfortable one in the catalog, because of *how* it fell. Moshe Rubin, an Israeli software engineer pursuing the puzzle, traced Byrne's surviving family in 2009; in May 2010 Byrne's daughter-in-law Patricia Byrne donated all the Chaocipher material to the National Cryptologic Museum at Fort Meade, and Rubin then published the algorithm and analyses in *Cryptologia*. The cipher was not broken. The papers were found. That is the calibration lesson, and it recurs live in this catalog: it is exactly what happened to Kryptos K4 in September 2025, and it is a standing argument for scoring `material` on *what could become accessible* rather than only on what is public.

## What survives
Today: the Byrne archive at the National Cryptologic Museum, the algorithm in print, Rubin's implementations and papers, and the four exhibits. Before 2010: only the four exhibits printed in *Silent Years*, of moderate length, with no algorithm, no key, and a dead author. That is the material situation that matters for scoring, and it was poor.

## Prior attempts and current consensus
The exhibits were a standard target of the amateur cryptologic community for half a century and resisted, including attention from people who broke harder-looking things. The reason is worth stating precisely, because it is a general point about the `compute` axis: cryptanalytic search works by enumerating a hypothesis space, and Chaocipher's space could not be enumerated, because the system was a bespoke dynamic substitution nobody had described. Frequency analysis is defeated by construction — the table changes every character — and there was no published family of ciphers to search within. Consensus today accepts Rubin's exposition entirely; the *Cryptologia* papers (2010 onward) are the reference, and Rubin's Mountain Vista Software site hosts the working material.

## What a solution would have to do
Historically met, by disclosure. For the record, and as the bar for any residual work: a claimed break of an exhibit must state the starting alphabets and produce the full English plaintext, reproducibly, from the published algorithm — and the check is instant. The genuinely open question a modern effort could still address is the one Byrne cared about: is Chaocipher secure? A rigorous cryptanalysis given the algorithm but not the starting alphabets — a known-algorithm, unknown-key attack, with a stated work factor — would settle whether Byrne's confidence was justified, and I could not establish that this has been published. That is a well-defined, purely computational, unexecuted piece of work.

## Why the scores
Scored as of 2009, before the archive surfaced, except `mystery`.
- mystery 1 today: fully resolved. In 2009 it would have been 2 — a famous amateur challenge, consequential to nobody outside the hobby.
- material 2: four printed messages of moderate length, no key, no algorithm, author dead. The surviving accessible evidence genuinely limited what any method could do.
- solvable 5: the author says so as explicitly as anyone in this catalog — he published the exhibits and offered money.
- compute 3, and this is the point of the entry: the verification would have been mechanical, but the hypothesis space was unenumerable because the system was unpublished and idiosyncratic. A rubric that scores `compute` from "is it digitized and is there a concrete check" would have said 5 and been wrong. `compute` must also ask whether the *hypothesis space* is enumerable.
- verifiable 5: English or not, instantly.
- crowding 4: a handful of serious attempts over fifty years and no dedicated literature before Rubin — which is why the archive route was still available.

## Sources
- SCHOLARLY — Moshe Rubin, "Chaocipher Revealed: The Algorithm," *Cryptologia* (2011), and related papers. https://doi.org/10.1080/01611194.2010.533252
- PRIMARY/SECONDARY — Moshe Rubin, The Chaocipher Clearing House (algorithm, exhibits, implementations, history of the 2010 donation). https://www.mountainvistasoft.com/chaocipher/
- PRIMARY — John F. Byrne, *Silent Years: An Autobiography with Memoirs of James Joyce and Our Ireland* (1953): the four exhibits and the reward offer.
- PRIMARY — National Cryptologic Museum, Fort Meade: the Byrne Chaocipher papers, donated May 2010.
- SECONDARY — Wikipedia, "Chaocipher" (1918 invention, *Silent Years* 1953, ninety years of secrecy, Rubin locating Patricia Byrne in 2009 and the May 2010 donation, the two-disk permutation algorithm). https://en.wikipedia.org/wiki/Chaocipher

## Unverified claims
- Whether all four exhibits are now decrypted. The encyclopedic source does not say; my recollection is that Exhibit 1 was solved and that at least one of the later, longer exhibits remained partly unresolved even after the algorithm was published, but this could not be confirmed and should be checked before the entry is used.
- The amount of Byrne's reward offer (commonly cited as $5,000) was not verified.
- Rubin's exact article titles, journal volumes and pages, and the DOI above, were not verified at the publisher.
- Whether Rubin located Patricia Byrne as daughter-in-law or another relation, and whether Byrne's son was involved, was not fully resolved; the encyclopedic source says daughter-in-law Patricia Byrne.
- Whether any known-algorithm cryptanalysis of Chaocipher with a stated work factor has been published. None found; asserted here as a gap.
- The precise permutation rule (which positions shift, and by how much) is given here only in outline from a secondary summary and should be taken from Rubin's paper before any implementation.
