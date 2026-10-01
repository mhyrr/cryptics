+++
title = "Short ciphers in letters to and from Walsingham, 1571–1584 (Bowes, Davison, Cotton Caligula residue)"
slug = "walsingham-related-ciphers"
kind = "cipher"
era = "1571–1584"
origin = "English embassies in Paris and Edinburgh; BL Cotton Caligula and Harley MSS"
language = "English"
status = "partial"
confidence = "medium"
digitized = "https://cryptiana.web.fc2.com/code/elizabeth.htm"
tags = ["nomenclator", "code-numbers", "letters", "diplomatic", "Elizabethan", "Scotland", "Cryptiana", "short-ciphertext", "context-crib"]

[scores]
mystery = 2
material = 3
solvable = 4
compute = 3
verifiable = 4
crowding = 4
+++

# Short ciphers in letters to and from Walsingham, 1571–1584

## What it is
Satoshi Tomokiyo's *Cryptiana* item "Ciphers related to Sir Francis Walsingham (Some Solved)" covers clear-English letters in the British Library's Cotton manuscripts that have a few words, or name and number codes, in undeciphered cipher. Most come from English agents in Scotland. This entry catalogs the item and its unsolved residue:

| Piece | Shelfmark | Status |
|---|---|---|
| Robert Bowes to (?)Walsingham, Edinburgh, 7 April 1583 | Cotton Caligula C VII f. 196 | **Partly solved** (Ryan Turner, 24 Sept 2026): names identified; numerical codes open |
| Robert Bowes to (?)Walsingham, St Johnstons, 31 July 1583 | Cotton Caligula C VII f. 299 | **Partly solved**, as above |
| William Davison to Walsingham, 27 July 1584 | Cotton Caligula C VIII f. 95 | Not deciphered |
| "Sir Robt. Bowes? to Secy Cecil?", 1583? | Cotton Caligula B VIII ff. 251–252 | Not deciphered (a few words) |
| Letter mentioning "Monsieur de la Noue", "Mr Randolph" | Cotton Caligula B VIII f. 306 | Not deciphered (a few words) |
| Walsingham to Killigrew, Woodstock, 30 July 1574 | Cotton Caligula C IV f. 278 | Not deciphered (a few words) |

Related pieces solved by others, kept here for context:
- Bowes's report against Lennox, c. 1580 (Caligula B VIII ff. 290–293): it has an interlinear decipherment, and Tomokiyo reconstructed the key.
- Walsingham to Randolph, 1581 (Caligula C VI f. 128): deciphered and printed.
- Walsingham to and from Edward Wotton, 1585 (Caligula C VIII f. 276; Add MS 32657): Tomokiyo reconstructed the key, and Bourdeau identified the name codes in September 2026.

Daniel Bourdeau's September 2026 write-ups add short, still unsolved pieces from Walsingham's Paris letter-book (Harley MS 260 and DECODE records):
- Walsingham to Burghley, 25 June 1571: a nine-symbol run and two code groups.
- Burghley to Walsingham, 5 July 1572: 15 tokens; code [3] is the French King.
- November 1572: code [3] is the Queen; the rest is open.
- 20 January 1572/3: one six-symbol place name.

He reports each as too short to recover a key without one surviving.

## What is unsolved
The values of the numerical name codes in Bowes's 1583 letters (870, 149, 19, 29, 85 and others; 189 has been identified as Montrose). Also the ciphered words in Davison's letter of July 1584, and the scattered few-word cipher runs in Caligula B VIII, Caligula C IV and Walsingham's letter-book.

## What survives
- The originals are in the BL Cotton and Harley collections. Tomokiyo links images through the BL digitized-manuscripts viewer, which has been offline since 2023 (Unverified claims).
- Tomokiyo has transcribed the Bowes pieces (`CottonMSBowes.txt`) and the Davison piece (`CottonMSDavison.txt`).
- Ryan Turner keeps a repository for the Bowes letters with the ciphertext, a key, code tables and a print check.
- **Cribs:**
  - *The Correspondence of Robert Bowes* (Surtees Society, 1842) and *CSP Scotland* vi (1910) contain the two Bowes letters, as Turner found. Tomokiyo had examined the 1842 volume and missed them.
  - For Davison, the cleartext of the letter itself and *CSP Scotland* vii are the evident cribs. Neither was checked here.

## Prior attempts and current consensus
- **Tomokiyo** judged the ciphers "simpler than some of Mary's ciphers," and possibly "easy for those who can read the cleartext parts of the letters."
- **Turner's solution of the Bowes letters**, which Tomokiyo checked, recovers names: SIR HENRI COBHAM, SMALLET, GLENCARNE, MAGNYVIL (Manningville), HUNTLEY, and Montrosse = 189. The other numerical codes are still unknown.
- **Turner's repository notes** (23 Sept 2026) record a sweep for prior decipherments of the Bowes and Caligula B VIII items. It found none and was blocked from the HathiTrust copy of *CSP Scotland* vi.
- **Bourdeau** solved several sibling Walsingham-network pieces in September 2026 by recovering keys from adjacent plaintext (Stafford 1586, Cobham 1588, Needham 1587, Wotton 1585). He closed the letter-book fragments as too short.

The consensus is that this is a set of small, tractable pieces where context and calendars do most of the work.

## What a solution would have to do
- Each recovered value must fit grammatically into the surrounding clear English and agree with the calendared or printed version of the same letter where one exists.
- Name codes must keep one referent across all letters in the same key. 189 must remain Montrose wherever it occurs.
- For pieces with no printed counterpart (Davison 1584 and the Caligula B VIII fragments), a reading should come from a key that also reads at least one other dated letter in the same cipher, and not from a guess fitted to a few words.

## Why the scores
- **mystery 2:** names and a few phrases in English intelligence from Scotland, 1583–84, a period that is well calendared.
- **material 3:** the letters survive whole and are transcribed by Tomokiyo, but each cipher run is short and the BL images are not reliably online.
- **solvable 4:** state ciphers with keys, used consistently. Some fragments may be too short to determine.
- **compute 3:** this could have been 4. The method is crib-and-context: align calendar text, recover the substitution alphabet, then propagate code numbers across the Bowes and Davison correspondence. Code can do the bookkeeping and the alignment, but most runs are too short for statistics.
- **verifiable 4:** where a printed or calendared version exists, the check is mechanical. Elsewhere, consistency across letters is the test.
- **crowding 4:** Tomokiyo, Turner and Bourdeau have worked parts of it.
- **compute mode:** CRIB-ALIGN · verifier MECHANICAL where printed text exists · signal PARTIAL · fit MEDIUM.

## Sources
- SECONDARY — S. Tomokiyo, *Cryptiana*, "Unsolved Historical Ciphers," §English, "Ciphers related to Sir Francis Walsingham" (with the 24 Sept 2026 note on Turner's solution). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — S. Tomokiyo, "Ciphers during the Reign of Queen Elizabeth I," §Walsingham (the list of Caligula C IV, C VI, C VII, C VIII and B VIII pieces, the transcriptions, and the solved siblings). https://cryptiana.web.fc2.com/code/elizabeth.htm
- CLAIMANT — Ryan Turner (NoAutopilot), cipher-lab, `bowes-walsingham-1583` (key, codes, print check, and the check-solved sweep in NOTES.md). https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/bowes-walsingham-1583
- CLAIMANT — D. Bourdeau, Unsolved Historical Ciphers, write-ups index (the letter-book fragments of 1571–73 "not solved"; the solved Stafford, Cobham and Wotton pieces). https://dbourdeau.github.io/cyphersolver/writeups.html

## Unverified claims
- That Davison's letter of 27 July 1584 is still undeciphered. Tomokiyo's list does not mark it solved. A web search and Bourdeau's index found nothing; not checked further.
- That *CSP Scotland* vii calendars the Davison letter in a way that would give a crib. Not checked.
- That the Caligula B VIII f. 251 and f. 306 fragments and Caligula C IV f. 278 are long enough to determine. Their lengths were not measured here.
- The identity of the remaining Bowes numerical codes. They are open; nothing is claimed.
- That the BL Cotton images are currently unavailable online. Inferred from the 2023 BL outage and Bourdeau's "BL offline" notes; not directly checked.
