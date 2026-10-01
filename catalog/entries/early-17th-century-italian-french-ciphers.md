+++
title = "Undeciphered French and Italian diplomatic ciphers, c. 1589–1637 (BnF fr. 4715, Cocquet, Sertori, Vizani)"
slug = "early-17th-century-italian-french-ciphers"
kind = "cipher"
era = "c. 1589–1637"
origin = "France, Rome, Milan/Madrid (diplomatic and League correspondence)"
language = "French and Italian (one item possibly Latin)"
status = "partial"
confidence = "medium"
digitized = "https://gallica.bnf.fr/ark:/12148/btv1b9000782k"
tags = ["nomenclator", "homophonic", "letters", "BnF", "BNE", "Cryptiana", "diplomatic", "short-ciphertext", "group-entry"]

[scores]
mystery = 2
material = 4
solvable = 4
compute = 4
verifiable = 4
crowding = 4
+++

# Undeciphered French and Italian diplomatic ciphers, c. 1589–1637

## What it is
A group of four items from the "French, Italian, Spanish" section of Satoshi Tomokiyo's Cryptiana list of unsolved historical ciphers. They are cipher letters or cipher passages from the French Wars of Religion and the early reign of Louis XIII, plus one Milanese cipher offered to Philip II of Spain:

1. **French (or Italian) ciphers, c. 1590: BnF français 4715.** A volume of League-era letters with many undeciphered pieces. Tomokiyo read several with reconstructed period keys (the Vieuville–Nevers cipher and others). Three stayed unread "despite their seeming simplicity": no. 59 (f. 82), no. 61 (f. 84) and no. 62 (f. 85). George Lasry solved no. 61 in 2020 by computer; the text is Italian ("catolico", "persuade", "promette"). He solved no. 59 in 2022 and reached "interim results" on no. 62 in 2022. Tomokiyo's article also lists no. 38 (f. 61), "Duke of Mayenne's polyphonic cipher? (Solution Incomplete)". Tomokiyo marks the whole item "Almost Solved". He points to BnF fr. 4712 for further undeciphered letters.
2. **Cocquet's cipher, 1616: BnF Clairambault 369, f. 316** (f. 317 in Bourdeau's foliation). A letter from Cocquet, Rome, 13(?) November 1616, to Claude Mangot, Secretary of State. It is partly in clear French, with about 160 letter-shaped glyphs in nine cipher runs.
3. **Fragments in a cipher invented by a Milanese: BNE Madrid Mss/994, ff. 83–90/91.** The papers of Luis Valle de la Cerda, Philip II's cipher expert, include ciphertext in a scheme offered to the King by Girolamo (Jerónimo) Sirtori/Sertori of Milan. Valle broke it and said he had devised the same scheme fifteen years earlier, but his solution does not survive. Tomokiyo reads the record as dated 7 October 1604; other authors put the episode in 1599. Tomokiyo marks it "Almost Solved?".
4. **Fra Guglielmo Vizani, 1637: BnF français 16158, f. 292.** A letter of 8 October 1637 in which "some portions seem to be in an unsolved cipher."

## What is unsolved
The open question is the plaintext, and for items 2–4 the key, of a handful of short diplomatic passages. Item by item:
- fr. 4715 no. 62 has interim results only. No. 38 is incomplete. fr. 4712 is not enumerated here.
- Cocquet: no key known. None of five period keys from the same volumes (Baugy–Mangot, Du Maurier–Mangot, the Bongars volumes) fits.
- Sertori: no accepted solution. Eloy Caballero's 2012 proposal is monoalphabetic substitution plus Milanese scribal abbreviation, producing a Latin petition to the King. Nick Pelling judged it "most of the way there … though not at the finishing line."
- Vizani: untouched as far as can be found. It is not even established that the "portions" are cipher.

## What survives
- fr. 4715, Clairambault 369 and fr. 16158 are BnF manuscripts on Gallica (Tomokiyo links Clair. 369 at the ark above). Tomokiyo's articles give partial transcriptions and dumps for fr. 4715.
- Bourdeau transcribed nothing of Cocquet beyond a gate check, and his tracker says no transcriptions exist for Cocquet or Vizani.
- BNE Mss/994 is digitised on BNE Digital (oid 0000174344). Bourdeau reports that the site sits behind a Cloudflare check that blocks scripts.
- Pelling's post says the Sertori text is about 27 distinct symbols and roughly 2,000 characters over three pages. A transcription was made by Caballero.

## Prior attempts and current consensus
- **Tomokiyo:** solved some fr. 4715 pieces himself with reconstructed keys and catalogued the rest.
- **Lasry:** solved no. 61 (2020) and no. 59 (2022) with his algorithms, and reached interim results on no. 62.
- **Caballero (2012):** the Sertori proposal, discussed on Pelling's Cipher Mysteries.
- **Daniel Bourdeau (September 2026):** gate-checked Cocquet and parked it. In his words, "none of the five period keys from the same volumes matches; du Croc regime", that is, too short for ciphertext-only work. Andrew Aymeloglu's tracker also lists Cocquet as "blocked, parked 16 Sept 2026", with a BnF inquiry drafted.
- **Vizani and Sertori:** neither of the 2026 solver groups lists an attempt.

No consensus reading exists for any of the four open residues. Read first: Tomokiyo's bnf4715.htm, louisxiii.htm (Cocquet, Vizani) and valle.htm (Sertori), then Pelling's post.

## What a solution would have to do
- **fr. 4715 no. 62:** a key that reads the whole letter in idiomatic period French or Italian. It should be consistent with the cipher families already reconstructed from the same volume (Vieuville–Nevers and others) or explicitly distinct from them, and it should fit the 1589–92 League context.
- **Cocquet:** a key that reads all nine runs and joins grammatically to the surrounding clear French. Ideally it also matches a key or sibling letter in Mangot's papers. About 160 glyphs is too short to accept a free hill-climb without a matched-control test.
- **Sertori:** a stated rule, applied uniformly across all ~2,000 characters, with every abbreviation drawn from attested Milanese or Spanish chancery practice and not invented ad hoc. It should explain why Valle could claim he had invented the same scheme. A reading that needs a new abbreviation for every difficult word fails.
- **Vizani:** first show that the passages are cipher and not an unfamiliar hand or a shorthand. Then the same standard as the others.

## Why the scores
- **mystery 2:** short dispatches and passages that matter to specialists in League and Louis XIII diplomacy. None is known to bear on a major historical question. Sertori is cryptologically interesting as an early "novel scheme", but that still scores 2.
- **material 4:** all are surviving archival originals, and the BnF items are on Gallica. Transcriptions are partial or missing (Cocquet, Vizani), and BNE access is awkward.
- **solvable 4:** these are state or professional ciphers with a determinate plaintext. Vizani is held at 4, not 5, because the cipher status of its "portions" is unconfirmed.
- **compute 4:** fr. 4715 no. 62 and the ~2,000-character Sertori text are exactly the targets for hill-climbing with a period language model. Cocquet (~160 glyphs) is below the unicity regime for a homophonic key, which caps the group below 5.
- **verifiable 4:** a full key reading coherent French or Italian is a strong check. The abbreviation-heavy Sertori scheme and the short Cocquet runs leave room for plausible-but-wrong readings, so not 5.
- **crowding 4:** Tomokiyo, Lasry, Caballero and, in September 2026, Bourdeau and Aymeloglu have each touched some items. Vizani appears untouched.

## Sources
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers" (section "French, Italian, Spanish"; September 2026 notice). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, "Undeciphered Letters in BnF fr.4715" (items nos. 38, 59, 61, 62; Lasry's 2020 and 2022 results). https://cryptiana.web.fc2.com/code/bnf4715.htm
- SECONDARY — Tomokiyo, Louis XIII-era ciphers (Cocquet, Clair. 369 f. 316; Vizani, fr. 16158 f. 292; contemporary Mangot keys). https://cryptiana.web.fc2.com/code/louisxiii.htm
- SECONDARY — Tomokiyo, on Luis Valle de la Cerda and BNE Mss/994 (Sertori episode, ff. 83–90, date 7 Oct 1604 on f. 90). https://cryptiana.web.fc2.com/code/valle.htm
- POPULAR — Nick Pelling, "Girolamo Sirtori cipher mystery," Cipher Mysteries, 14 June 2012 (Caballero's proposal; ~27 symbols, three pages). https://ciphermysteries.com/2012/06/14/girolamo-sirtori-cipher-mystery
- CLAIMANT — Daniel Bourdeau, cyphersolver README and TARGETS (Cocquet gate check, 16 Sept 2026; "no transcriptions" for Cocquet and Vizani; BNE Mss/994 access). https://github.com/dbourdeau/cyphersolver
- CLAIMANT — Andrew Aymeloglu, unsolved-ciphers TARGETS.md (Cocquet "blocked, parked 16 Sept 2026"). https://github.com/aaymeloglu/unsolved-ciphers/blob/main/TARGETS.md
- PRIMARY (link from Tomokiyo, not opened in this pass) — BnF Clairambault 369 on Gallica. https://gallica.bnf.fr/ark:/12148/btv1b9000782k

## Unverified claims
- Lasry's results on fr. 4715 nos. 59, 61 and 62 are known only through Tomokiyo's notes. No publication by Lasry was found, and the "interim" state of no. 62 may have changed.
- Whether fr. 4712 holds further unsolved letters, and how many (Tomokiyo's nevers.htm was not read).
- Caballero's own write-up of the Sertori solution was not read; the summary is Pelling's. Whether Caballero's reading has since been accepted or refuted is unknown.
- The date of the Sertori episode: 1599 per Navarro Bonilla et al. and Carnicer & Marcos, 7 October 1604 per Tomokiyo's reading of f. 90.
- The Cocquet foliation: Tomokiyo gives f. 316, Bourdeau f. 317.
- The Gallica and BNE images were not opened in this pass.
- Given the September 2026 pace of solutions, any of these residues may already be solved elsewhere.
