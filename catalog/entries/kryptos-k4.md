+++
title = "Kryptos K4 (Jim Sanborn, CIA headquarters)"
slug = "kryptos-k4"
kind = "cipher"
era = "dedicated 3 November 1990"
origin = "CIA headquarters, Langley, Virginia (sculpture by Jim Sanborn)"
language = "English"
status = "unsolved"
confidence = "medium"
digitized = "https://en.wikipedia.org/wiki/Kryptos"
tags = ["modern-cipher", "author-living", "crib-known", "sculpture", "short-ciphertext", "sealed-solution"]

[scores]
mystery = 3
material = 5
solvable = 5
compute = 4
verifiable = 5
crowding = 1
+++

# Kryptos K4 (Jim Sanborn, CIA headquarters)

## What it is
The fourth and last section of Jim Sanborn's copper-scroll sculpture *Kryptos*, dedicated 3 November 1990 in the courtyard of CIA headquarters at Langley. The sculpture carries 869 characters (865 letters and four question marks) in four passages. K1 (Vigenère, keyword PALIMPSEST), K2 (Vigenère, keyword ABSCISSA, containing a set of coordinates and the phrase "ONLY WW") and K3 (a transposition, quoting Howard Carter's account of opening Tutankhamun's tomb and ending "CAN YOU SEE ANYTHING Q") fell between 1998 and 1999 — internally to CIA analyst David Stein, publicly to Jim Gillogly. K4 is 97 characters and has never been publicly broken:

`OBKR UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO TWTQSJQSSEKZZWATJKLUDIAWINFBNYP VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR`

## What is unsolved
The cipher *system*. This is the one text in the catalog whose plaintext is, as of 2026, known to exist in writing and to a small number of people, while the method that produced it remains unknown to the public. Sanborn released four cribs: BERLIN at positions 64–69 (2010), CLOCK at 70–74 (2014), and NORTHEAST and EAST (2020). In August 2025 he announced an auction of the solution; the archive — including the K4 solution, a prototype, and encryption tables — sold through RR Auction for $962,500 on 20 November 2025. In September 2025, journalists Jarett Kobek and Richard Byrne found what appeared to be the full K4 plaintext among papers Sanborn had mistakenly included in a donation to the Smithsonian's Archives of American Art while compiling material during cancer treatment; Sanborn confirmed the find was accurate and asked the Smithsonian to seal the files until 2075. Kobek and Byrne declined to sign non-disclosure agreements and report having been threatened with copyright action if they published. So the public position is: a known-to-exist plaintext, not published; a method, not published; the ciphertext, fully public.

## What survives
Everything material. The complete ciphertext is public and exactly transcribed, including the deliberate misspellings elsewhere in the sculpture (IQLUSION in K1, UNDERGRUUND and DESPARATLY in K3) which Sanborn has said are intentional. The four cribs are public. The auction catalogue and press coverage document what was sold. The sealed Smithsonian files and the private buyer's archive are the two places the answer sits. Uniquely in this catalog, the author is alive and has repeatedly commented on the piece — which makes the material situation excellent and the epistemics strange.

## Prior attempts and current consensus
Thirty-five years of effort by the strongest amateur and professional community in the field: Elonka Dunin and Klaus Schmeh's *Codebreaking: A Practical Guide* treats it as a canonical case, and Dunin maintains the long-running Kryptos group. The community consensus before 2025 was that K4 uses something beyond the Vigenère-plus-transposition toolkit of K1–K3, that the cribs constrain any candidate system tightly (BERLIN/CLOCK at fixed positions is a 11-character known-plaintext attack), and that despite this no system has been found that yields English beyond the cribs — which strongly suggests either a non-standard hand method or an artist's idiosyncratic construction. Richard Bean and others have published statistical constraints. The 2025 events did not change the cryptanalytic position; they changed the social one. Wikipedia still describes K4 as unsolved.

## What a solution would have to do
State the algorithm and key, then produce the full 97-character plaintext including the four known cribs at their published positions, and do it reproducibly by hand — Sanborn built this with paper tables in 1989–90, so any proposed system must be executable with the materials he had, which is a strong filter on machine-heavy proposals. It must be consistent with the cribs' *positions*, not just their presence. And it must now clear a bar no other entry faces: because a written plaintext exists in two archives, any claimed solution can in principle be checked against it, and any claimed solution that Sanborn declines to confirm is in a genuinely novel epistemic position. A related and now-significant question a "solution" might address instead: whether the 2025 disclosure's plaintext can be independently authenticated without Sanborn, e.g. by exhibiting a system that generates exactly it.

## Why the scores
- mystery 3, not 5: the answer exists, is written down, and has been read by at least three people. What is unresolved is public knowledge of it and of the method — a real and interesting question, but no longer an open one in the strong sense. Deliberately scored down from where a pre-2025 assessment would have put it.
- material 5: complete, exact, public ciphertext; documented cribs; a living author.
- solvable 5: near-certain — the author says so, the plaintext has been seen, and three of four sections decode.
- compute 4, not 5: the constraint set is small and 97 characters is short, so exhaustive search over hypothesis families is feasible and has been pursued hard; the binding difficulty is that the system may be idiosyncratic rather than in any enumerable family.
- verifiable 5: a system that yields the cribs at the right positions and coherent English is instantly recognizable, and a ground-truth text exists.
- crowding 1: one of the most-attacked ciphertexts in existence, with a dedicated expert community, books, and mailing lists.

## Sources
- PRIMARY — Jim Sanborn's own statements via the Kryptos clue releases (BERLIN 2010, CLOCK 2014, NORTHEAST/EAST 2020), reported in the New York Times and collected by the Kryptos community.
- PRIMARY — RR Auction, "Decoding History: Kryptos, Enigma and the Rosetta Stone," 16 October – 20 November 2025; K4 solution archive sold for $962,500. https://www.rrauction.com/
- SECONDARY — Wikipedia, "Kryptos" (869 characters, K1–K3 solutions and solvers, full K4 ciphertext, crib positions, the 2025 auction, the Smithsonian disclosure and the 2075 seal). https://en.wikipedia.org/wiki/Kryptos
- SCHOLARLY — Elonka Dunin & Klaus Schmeh, *Codebreaking: A Practical Guide* (No Starch Press, 2020; 2nd ed. 2023), Kryptos chapter. https://nostarch.com/codebreaking
- SECONDARY — Elonka Dunin's Kryptos pages and the Kryptos discussion group. https://elonka.com/kryptos/

## Unverified claims
- The exact content of the K4 plaintext. Not published; this entry deliberately does not report any version of it.
- Whether the encryption *method* is described in the sealed Smithsonian papers or in the auctioned archive, and therefore whether the buyer now knows the system as well as the text. Not established.
- The precise positions of NORTHEAST and EAST in the plaintext were not recorded in the source consulted; only BERLIN (64–69) and CLOCK (70–74) were.
- Whether David Stein's 1998 internal solution or Jim Gillogly's 1999 public one came first for each of K1–K3 individually was not disentangled.
- Richard Bean's published statistical constraints on K4 were not located by citation and are reported here from general knowledge of the community's work.
- Kobek and Byrne's reported legal threats are as characterized in the encyclopedic account; no primary correspondence was seen.
