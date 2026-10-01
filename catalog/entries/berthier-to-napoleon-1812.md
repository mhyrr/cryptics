+++
title = "Encoded letter from Berthier to Napoleon, 22 December 1812"
slug = "berthier-to-napoleon-1812"
kind = "cipher"
era = "22 December 1812"
origin = "French Empire: Marshal Berthier (Prince of Neuchâtel), with the remnants of the Grande Armée in East Prussia, to Napoleon"
language = "French"
status = "unsolved"
confidence = "medium"
digitized = "https://cryptiana.web.fc2.com/code/napoleon2.htm"
tags = ["Napoleonic", "grand-chiffre", "code", "nomenclator", "letters", "Cryptiana", "retreat-from-Russia"]

[scores]
mystery = 2
material = 3
solvable = 5
compute = 3
verifiable = 5
crowding = 5
+++

# Encoded letter from Berthier to Napoleon, 22 December 1812

## What it is
A dispatch dated 22 December 1812 from Louis-Alexandre Berthier, Napoleon's chief of staff, to the Emperor. At that date Berthier was at Königsberg with what was left of the army after the retreat from Russia, and Napoleon had already returned to Paris. The letter is entirely in numerical code. Like the Marmont letter, it is reproduced as a plate in J. Vilcoq, "Le Chiffre sous le Premier Empire," *Revue historique de l'Armée* no. 4 (1969). It bears the note "Duplicata, Chiffre du Prince de Neufchâtel, La Primata a été déchiffrée": this is the duplicate copy, it is in Berthier's own code, and the first copy had been deciphered.

## What is unsolved
The plaintext of the code groups. That plaintext probably exists: the note says the first copy was deciphered on receipt, so a decipherment or the "Chiffre du Prince de Neufchâtel" table may survive in the French army archives.

## What survives
- The Vilcoq plate.
- Tomokiyo's transcription of its opening on Cryptiana: 22 lines, about 400 numeric groups, ending "....". The full length of the message is therefore not established here.

The groups run from 2 to 1388 and include many four-digit values above 1000. Tomokiyo puts the code at "at least 1200 entries." No SHD shelfmark for the original is given.

## Prior attempts and current consensus
**Status:** Cryptiana lists it as unsolved. Its September 2026 notice warns that solutions are arriving faster than they are recorded. No solution was found here, and Daniel Bourdeau's site was not checked item by item (see Unverified claims).

**Is it the same cipher family as the Marmont letter?** No, and this matters for the compute score. The Marmont letter (solved 2026, see `marmont-letter-1809`) is a small homophonic cipher: about 155 signs that are letters, two-digit figures and symbols, plus 29 whole-word signs. Within such a system 1,300 units are enough for n-gram annealing. The Berthier letter is a numeric "grand chiffre" with at least 1,200 entries. That is the class of the Great Paris Cipher, whose 1,200 entries were enlarged to 1,400, and of the other 1,200-entry great ciphers Tomokiyo describes. In such a code most groups stand for syllables and words, so a single message of a few hundred groups gives letter statistics almost nothing to work with.

**Leads that are not statistical:**
- Daniel Tant's inventory of coded messages at the SHD includes PDFs of three 1,200-entry great ciphers "from unknown period." Each is a candidate key that can be tested mechanically.
- The French army archives (SHD) hold Napoleonic code tables.
- The deciphered first copy may survive among Napoleon's papers.

Tomokiyo's article on Napoleonic codes is the place to start.

## What a solution would have to do
1. Produce a code table, either recovered from an archive or reconstructed, that turns the whole dispatch into French. Group-level consistency must hold: a group that recurs (918 and 13 recur often in the transcribed portion) must keep one meaning everywhere.
2. If the code is one-part (numbers in alphabetical order), the numeric order of groups must match the alphabetical order of their meanings.
3. The content must fit the documented situation at Königsberg in late December 1812: the remains of the corps, Murat's command, and Yorck's defection a week later at Tauroggen. Berthier's other surviving correspondence of those days should cross-check it.
4. Ideally, match a surviving plaintext or the deciphered first copy.

A reading built from a few hundred groups and guessed word meanings without a table would be weak. Only a table or an archival plaintext settles it.

## Why the scores
- mystery 2: one staff dispatch from a well-documented week. It matters to specialists, and its general subject (the state of the army after the retreat) is predictable.
- material 3: the whole message probably survives on the 1969 plate, but only the opening is transcribed publicly. The original was not located and Persée access to the plate is unconfirmed.
- solvable 5: a state code, used in earnest, which the recipient deciphered.
- compute 3: this could have gone 2 or 4. A 1,200+ entry code with one message resists the annealing that broke the Marmont letter: it is a code, not a cipher. Computation still has clear jobs. It can test the candidate 1,200-entry tables in Tant's inventory and the SHD tables against the groups, which is cheap and mechanical. It can test whether the code is one-part, using the ordering constraints. It can transcribe the plate the way the Marmont solve did. Each of these can settle sub-questions without deciding the whole.
- verifiable 5: a recovered table either produces continuous French or it does not.
- crowding 5: no published attempt beyond Tomokiyo's listing.

## Sources
- SECONDARY — Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," entry "Encoded Letter from Berthier to Napoleon (1812)": the opening transcription, the "Duplicata… La Primata a été déchiffrée" note, and the Vilcoq citation. https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, Cryptiana, "Napoleonic ciphers": the Berthier letter as a great cipher of at least 1,200 entries, the Great Paris Cipher's 1,200 to 1,400 entries, Tant's inventory with three 1,200-entry great ciphers, SHD holdings, and Marmont's 150-entry code of 1811. https://cryptiana.web.fc2.com/code/napoleon2.htm
- CLAIMANT — Carter Church, "Breaking the Marmont Cipher, 1809": the Vilcoq article as *Revue historique des Armées* 25 (4), 1969, pp. 22–27, on Persée, and the structure of the Marmont cipher used for the comparison above. https://carter.church/writeups/the-letter-to-marmont/
- PRIMARY (not opened) — J. Vilcoq, "Le Chiffre sous le Premier Empire," *Revue historique des Armées* 25 (4) (1969).

## Unverified claims
- Whether the Berthier code is one-part or two-part. The summary of Tomokiyo's article read here does not settle it.
- The total number of code groups in the letter.
- Whether the Berthier plate is in the Persée digitization of Vilcoq. Only the Marmont plate is reported there.
- Whether Daniel Bourdeau or anyone else has solved it since 2025. Bourdeau's index was not checked for this item.
- The location of the original and of any deciphered first copy.
- That Tant's three 1,200-entry tables are unrelated to this code. Nobody has reported testing them against it.
