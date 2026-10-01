+++
title = "Unbroken original Enigma messages: the Oberrhein 'KR-Blitz' message (1945), U-534's P1030680 (1945), and the Weierud Army collection residue"
slug = "unbroken-enigma-messages"
kind = "cipher"
era = "1941–1945"
origin = "Germany (Wehrmacht, SS and Kriegsmarine radio traffic)"
language = "German (military)"
status = "unsolved"
confidence = "medium"
digitized = "https://scienceblogs.de/klausis-krypto-kolumne/2019/01/07/an-unsolved-enigma-message-from-the-second-world-war/"
tags = ["Enigma", "WWII", "machine-cipher", "military", "short-message", "hill-climbing", "distributed-computing", "Cipherbrain", "Cryptiana"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 5
verifiable = 5
crowding = 3
+++

# Unbroken original Enigma messages

## What it is
Original German Enigma messages from the Second World War that still resist modern codebreakers. Bletchley Park broke most traffic at the time, but these particular intercepts, or the keys for them, have not been recovered. Three groups are covered.

1. **The Oberrhein "KR-Blitz" message, 10 January 1945.** Cryptiana lists it as "Another Enigma Message (1945)". Hauptmann Wolfgang Schmidt, curator of a Bundeswehr museum in Feldafing near Munich, gave Klaus Schmeh a photograph of the original radio message form, which Schmeh published on Cipherbrain on 7 January 2019. The sender is "O.B. Oberrhein IIa", the deputy of the Oberbefehlshaber Oberrhein (Heinrich Himmler, appointed December 1944). It went to the Oberkommando der Wehrmacht at 20:03 and is marked "KR-Blitz", an urgency above the usual top level "KR". Daniel Bourdeau reads the header as "2003 – 97 – hiq rst": time, letter count, Grundstellung HIQ, and enciphered message key RST. The 97 letters follow in 19 five-letter groups plus two letters.
2. **P1030680, U-534, 1 May 1945.** A naval (M4) message of 72 letters, indicator groups VROL NMKA, received by U-534 in the last days of the war. Michael Hörenberg's site, which publishes the form and ciphertext, records that the operator first tried the "Potsdam" key and then marked it as M-Thetis, a key the boat did not hold. The project Enigma@Home has attacked it by distributed brute force for years.
3. **The residue of the German Army collection.** Frode Weierud and Geoff Sullivan's project "Breaking German Army Ciphers" (Crypto Cellar) holds close to 1,000 Enigma and Truppenschlüssel messages. Weierud's note of September 2026 says only seven Enigma messages remain unbroken, plus a puzzle: Nr. 138 WEUWY, which must share its plaintext with Nr. 140 of the same day, has "resisted all our attempts to break it."

**Solved siblings, not catalogued:**
- Cryptiana's "German Navy Enigma messages (1942)": three M4 intercepts published by Ralph Erskine. Stefan Krah's distributed M4 Message Breaking Project broke two (20 February and 7 March 2006), and Dan Girard broke the third (2013 per Cryptiana). The project left nothing open.
- **MVUEH**, broken about 15 September 2026 with OpenAI's GPT-6 Astra.
- **FMNGI** (Nr. 285, 31 July 1941, to the SS-Totenkopf Division quartermaster), broken 20 September 2026 by Jack Willis working with Claude Opus 5.
Both 2026 breaks come from the Army collection and were reviewed by Weierud.

## What is unsolved
For each message, the daily key and the plaintext. For the Oberrhein message the Enigma variant is also uncertain (a Wehrmacht Enigma I is most likely). P1030680's key, M-Thetis for U-boats in training, is not recorded in surviving key lists. For the Army residue, Weierud's note read here does not say why each message resists.

## What survives
- Oberrhein: one photograph of the form (Cipherbrain, 1200 × 1683 px). No second message in the same key is known. Transcriptions differ in about four letters (groups 4, 7, 12, 18), and the first indicator letter has been read as B or H.
- P1030680: a photograph of the form and a typed ciphertext on Hörenberg's site.
- Army residue: the Crypto Cellar collection, digitized and transcribed by Weierud and Sullivan. Whether the unbroken messages' ciphertexts are published individually was not confirmed here.

## Prior attempts and current consensus
- **Oberrhein.** The Enigma-breaking community examined it before Schmeh published it. Hörenberg, Girard and Richard Bean took it up in the 2019 comments; Hörenberg noted that his hill-climber is weak below 100 letters. Fränz Friederes's 2023 bachelor thesis (§5.3) ran his tool *bomm* over Enigma I with reflector B, all 60 wheel orders, and the full ranges of positions and right-ring settings, plus other reflectors and variants. He found nothing, and did not enumerate the middle ring. Bourdeau began a ciphertext-only attack on 16 September 2026; his notes report a partial first pass with no convincing plaintext.
- **P1030680.** Enigma@Home has run a long distributed search without result. At 72 letters with no crib, a hill-climb has little signal to work with.
- **Army residue.** These are what remain after two decades of systematic work by Weierud, Sullivan, Olaf Ostwald and others. They are by selection the hardest messages: short, garbled, or in odd procedures.

Consensus: all unsolved. The September 2026 breaks show that AI-assisted work can close cases of this type, though by Weierud's account the human direction (known signatures, historical context) was central.

## What a solution would have to do
For any message in the group: give a complete machine setting (variant, reflector, wheel order, rings, plugboard, start position) under which the indicator procedure of the right date and service is satisfied. For the Oberrhein message, RST deciphered at HIQ must give the message key. The setting must then decipher the whole message to continuous German in period military conventions, allowing only one to three garbled letters. For P1030680 and the other short messages, false positives are the main danger. A setting that also reads a second message of the same day and network is the strongest confirmation. The content should fit the sender's situation: Heeresgruppe Oberrhein during Operation Nordwind, and a U-boat in the capitulation week.

## Why the scores
- mystery 2: short operational messages. The group is of specialist and symbolic interest ("the last unbroken Enigma"), and no historical question depends on any of them.
- material 4: every ciphertext is complete, but survives as a single photograph with disputed letters (Oberrhein) or is only 72 letters long (P1030680). A short complete message is still a complete text.
- solvable 5: genuine Enigma traffic with indicators.
- compute 5: purely computational, with a known and enumerable key space. The obstacles (length, ring and variant uncertainty, transcription variants) are exactly what better search design and cribs from historical context address, and AI-assisted breaks of sibling messages happened in September 2026.
- verifiable 5: indicator consistency plus German plaintext is mechanical.
- crowding 3: the strongest Enigma solvers have worked these (Krah's and Enigma@Home's distributed efforts, Girard, Hörenberg, Weierud, Sullivan, Ostwald, Friederes, Bourdeau). The general literature is not huge, but these particular messages are what is left after capable people finished everything else.
- compute mode: ENUMERATE + HILL-CLIMB (wheel order × ring × position exhaustive, plugboard climb, n-gram scoring; enumerate transcription variants; crib-driven search from historical context) · verifier MECHANICAL · space ENUMERABLE · signal WEAK (72–97 letters) · fit HIGH.

## Sources
- PRIMARY (photograph) — Oberrhein Funkspruch form, 10 January 1945, Bundeswehr museum Feldafing, image on Cipherbrain. https://scienceblogs.de/klausis-krypto-kolumne/2019/01/07/an-unsolved-enigma-message-from-the-second-world-war/
- POPULAR — Klaus Schmeh, "An unsolved Enigma message from the Second World War," Cipherbrain, 7 January 2019, with comments by Hörenberg, Girard and Bean (same URL).
- PRIMARY (photograph) / SECONDARY — Michael Hörenberg, "P1030680 – Unbroken Enigma message (U534 – 01. May 1945)" (form, ciphertext, VROL NMKA, M-Thetis, Enigma@Home). https://enigma.hoerenberg.com/index.php?cat=Unbroken
- SECONDARY — Frode Weierud et al., "The FMNGI Break," Crypto Cellar (collection of ~1,000 messages, seven unbroken plus Nr. 138 WEUWY, MVUEH and FMNGI breaks). https://cryptocellar.org/bgac/the-fmngi-break.html
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," sections "German Navy Enigma Messages (1942)" and "Another Enigma Message (1945)." https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Stefan Krah, M4 Message Breaking Project. http://www.bytereef.org/m4_project.html
- CLAIMANT — Daniel Bourdeau, Oberrhein notes (header reading, transcription variants, Friederes' search, attempt in progress). https://github.com/dbourdeau/cyphersolver/tree/main/targets/enigma/
- POPULAR — IFLScience, "Only One Enigma Code Has Never Been Broken" (P1030680, Enigma@Home since 2018). https://www.iflscience.com/only-one-enigma-code-has-never-been-broken-69540
- SCHOLARLY — Fränz Friederes, *Breaking Enigma Ciphertext in 2023*, bachelor thesis, §5.3 (known via Bourdeau's notes; not read directly).

## Unverified claims
- Whether Weierud's "seven unbroken" count is before or after the MVUEH and FMNGI breaks; it is read here as after, the state on the date of the note.
- The designations, dates and lengths of the seven unbroken Army messages; not listed in the note read here.
- The physical source of P1030680 (wreck recovery, museum or archive) and the claim that Enigma@Home began on it in 2018 (IFLScience); not checked against the project.
- That M-Thetis was the U-boat training key; stated from the page's annotation and general knowledge, not from a key list.
- Friederes' thesis contents are known only from Bourdeau's summary.
- Girard's 2013 date for the third M4 message comes from Cryptiana; the M4 project page read here gives no date.
- The IFLScience headline ("only one Enigma code has never been broken") is false as a general claim, since this entry lists more than one unbroken message. It is cited only for P1030680.
- Status after 30 September 2026; Bourdeau's Oberrhein attack was in progress when checked, and the AI-assisted campaign on the Army residue was active.
