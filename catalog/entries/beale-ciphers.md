+++
title = "Beale ciphers, papers 1 and 3"
slug = "beale-ciphers"
kind = "cipher"
era = "allegedly 1822; published 1885"
origin = "Bedford County, Virginia, USA"
language = "English (paper 2 plaintext)"
status = "contested"
confidence = "medium"
digitized = "https://en.wikisource.org/wiki/The_Beale_Papers"
tags = ["book-cipher", "treasure", "hoax-hypothesis", "Cryptologia", "Americana", "statistics"]

[scores]
mystery = 2
material = 4
solvable = 2
compute = 4
verifiable = 5
crowding = 1
+++

# Beale ciphers, papers 1 and 3

## What it is
Three number ciphers printed in an 1885 pamphlet, *The Beale Papers*, issued at Lynchburg, Virginia by James B. Ward at 50 cents. The frame story: one Thomas J. Beale deposited gold, silver and jewels in a vault in Bedford County in 1819 and 1821, left three enciphered papers with an innkeeper, and never returned. Paper 2 was solved with a numbered copy of the Declaration of Independence as the key — each number indexing the first letter of the nth word — and describes the deposits. Paper 1 allegedly gives the location; paper 3 the names and heirs of the thirty depositors. Both remain unread.

## What is unsolved
Formally: papers 1 and 3 have no known key. Substantively the prior question is whether they encode anything. The evidence is not neutral. Jim Gillogly showed that decoding paper 1 against the same Declaration key used for paper 2 throws out long alphabetical runs — the string usually quoted is `abcdefghiijklmmnohpp` — which is wildly improbable for a random number series and equally improbable for an unrelated book cipher, and which looks exactly like what you get if someone built the number series by walking an alphabet through a document. So the open question is really: are papers 1 and 3 (a) real book ciphers on unidentified keytexts, (b) meaningless filler constructed to look like ciphers, or (c) something in between — a decoy built from the Declaration plus noise.

## What survives
Not the manuscripts. The originals are not known to survive; everything anyone works on descends from the 1885 printed pamphlet, including whatever typesetting errors it introduced — a serious problem for a cipher in which one wrong digit destroys one letter and one dropped number destroys alignment. The pamphlet text and all three number series are freely available and trivially machine-readable. Standard numbers cited are 520 numbers in paper 1, 763 in paper 2 and 618 in paper 3, but I could not verify these from a primary count (see Unverified claims).

## Prior attempts and current consensus
Jim Gillogly, "The Beale Cipher: A Dissenting Opinion," *Cryptologia* (1980), is the load-bearing skeptical paper and the alphabetical-string argument is his. Louis Kruh's stylometric comparison and Carl Hammer's computer analyses are the other standard citations in the *Cryptologia* literature. Joe Nickell (1982) argued the pamphlet's prose is anachronistic for the 1820s — "stampeding" is the usual example — and that the narrative works as a Masonic allegory, Ward himself having been a Mason; stylometric work points to Ward as author of all the documents. Against this stands the brute fact that paper 2 *does* decode, cleanly, on a real and findable keytext, which no ordinary hoaxer needed to do. The working consensus among cryptologists is hoax with a minority holding the ciphers genuine; the treasure-hunting community is not part of that consensus. A newcomer reads Gillogly, then Nickell, then Poundstone's popular account for the narrative.

## What a solution would have to do
Name the keytext, in an edition available in Virginia before 1885, and decode paper 1 or paper 3 end to end without discretionary corrections. The verification bar here is unusually hard and unusually clean: paper 3 allegedly lists thirty surnames and next of kin, so a correct decode yields thirty proper names that must be checkable against Bedford County and St. Louis records of the 1820s — a genuine external test that no other cipher in this catalog offers. Paper 1 allegedly gives a location, which is testable with a shovel. A claimed solution must also explain Gillogly's alphabetical strings under its own hypothesis, not ignore them. Conversely, a hoax proof would have to exhibit the construction procedure that produces paper 1's number series *and* its Declaration-keyed alphabetical runs, and show it also produces paper 3's statistics.

## Why the scores
- mystery 2: a working consensus (hoax) exists with real minority dissent, and the popular mystery greatly exceeds the scholarly one.
- material 4: both ciphertexts are complete, public and machine-readable; not 5 because the manuscripts are gone and the printed transmission may be corrupt.
- solvable 2: the best evidence — the alphabetical runs, the stylometry, the anachronisms — favours fabrication.
- compute 4: a large-scale automated keytext search over the digitized corpus of pre-1885 English-language books available in Virginia is well-defined, cheap now, and has never been done exhaustively; it can also quantify how anomalous the Gillogly strings really are.
- verifiable 5: a key either decodes the paper or it does not, and paper 3's alleged names are externally checkable against archival records.
- crowding 1: more than a century of attempts, an active treasure-hunting ecosystem, and every naive approach exhausted.

## Sources
- PRIMARY — *The Beale Papers* (Lynchburg, Va., 1885), full text with all three number series. https://en.wikisource.org/wiki/The_Beale_Papers
- SCHOLARLY — Jim Gillogly, "The Beale Cipher: A Dissenting Opinion," *Cryptologia* 4(2) (1980). https://doi.org/10.1080/0161-118091854940
- SCHOLARLY — Joe Nickell, "Discovered: The Secret of Beale's Treasure," *Virginia Magazine of History and Biography* (1982).
- SECONDARY — Wikipedia, "Beale ciphers" (pamphlet details, decoded paper 2 text, Gillogly string, Nickell, Poundstone, stylometric attribution to Ward). https://en.wikipedia.org/wiki/Beale_ciphers
- POPULAR — William Poundstone, *Biggest Secrets* (1983), chapter on the Beale ciphers.

## Unverified claims
- The number counts 520 / 763 / 618 for papers 1 / 2 / 3. Commonly cited; the encyclopedic source consulted does not state them and they were not recounted from the pamphlet text.
- Louis Kruh's and Carl Hammer's papers were not located by citation; the encyclopedic article consulted does not name them. Their arguments are reported here as part of the standard *Cryptologia* literature on the strength of memory and should be pinned before being relied on.
- Whether the original Beale papers ever existed, and whether any manuscript is extant anywhere, is not addressed in the sources consulted; "not known to survive" is an inference from the pamphlet being the sole witness.
- Stephen Matyas's work on the Beale ciphers, and the exact dollar valuation of the deposits in current money, were not verified.
- Gillogly's exact *Cryptologia* volume, issue and DOI were not confirmed at the publisher.
