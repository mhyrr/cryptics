+++
title = "Egyptian enigmatic (\"cryptographic\") writing in the royal tombs"
slug = "egyptian-enigmatic-writing"
kind = "inscription"
era = "New Kingdom, late 18th–20th Dynasty (c. 1330–1100 BCE)"
origin = "Thebes (Valley of the Kings) and Abydos"
language = "Egyptian, written in enigmatic hieroglyphic orthography"
status = "partial"
confidence = "low"
digitized = ""
tags = ["Egyptian", "hieroglyphs", "enigmatic-writing", "netherworld-books", "substitution", "Tutankhamun", "Ramesses-VI", "Ramesses-IX"]

[scores]
mystery = 3
material = 4
solvable = 5
compute = 4
verifiable = 4
crowding = 4
+++

# Egyptian enigmatic ("cryptographic") writing in the royal tombs

## What it is
A mode of hieroglyphic writing used in New Kingdom royal funerary monuments in which individual signs carry non-standard values: the sign is chosen for its shape, its picture, the sound of the word it depicts, or a theological association, rather than for its ordinary phonetic value. It is not a cipher in the modern sense — there is no key and no intent to conceal from a reader who does not exist — but a display orthography, and Egyptologists now prefer "enigmatic" to the older "cryptographic" or "sportive" writing. Its most substantial monuments are the compositions known as the Enigmatic Books of the Netherworld, written on the second gilded shrine of Tutankhamun (KV62, c. 1332–1323 BCE) and on walls in the tombs of Ramesses VI (KV9) and Ramesses IX (KV6), which describe the sun god and the netherworld in this orthography. Enigmatic passages also appear embedded in the ordinary-script Netherworld Books — the Amduat, the Book of Caverns, the Book of the Earth — which are otherwise written in standard hieroglyphs.

## What is unsolved
Not the corpus as a whole, and the entry exists mainly to say precisely where the line falls. What is read: the general subject and structure of the enigmatic compositions, a large majority of their individual sign values, and continuous stretches of text that can be translated with confidence. What is not read: individual passages where no orthodox spelling of the same word exists to anchor the substitution, so the sign values remain conjectural and the translations in print differ substantially from one another; and, at the level of theory, the principles by which a scribe chose a substitute sign — whether by acrophony, by the consonantal skeleton of the depicted object's name, by pictorial association, or by several competing principles at once — which determines whether the unread passages are recoverable in principle or only by lucky parallel. Because there is no ancient key, a wrong sign value can be self-consistent across a short passage, and the field's translations are correspondingly uneven.

## What survives
The monuments, in situ or in museums, and in good condition by New Kingdom standards: Tutankhamun's second shrine is intact; the KV9 and KV6 walls survive with damage. The Book of Caverns is complete in three places (the Osireion at Abydos, KV9 and KV6) and attested at eight sites in all; the Amduat's earliest complete version is in KV34 (Thutmose III), with other copies in KV20, KV38, Wadi C-4, KV35 and WV22. Publication history: Champollion and Rosellini published Book of the Earth and Book of Caverns material in the 1830s–40s; Alexandre Piankoff produced the first serious studies and a French translation of the Caverns (1942–45); Erik Hornung's German translations are the standard for the Amduat and the Caverns (1972); Daniel Werning's text-critical German edition is the latest for the Caverns. For the enigmatic material specifically, the reference works are John Coleman Darnell, *The Enigmatic Netherworld Books of the Solar-Osirian Unity: Cryptographic Compositions in the Tombs of Tutankhamun, Ramesses VI and Ramesses IX* (Orbis Biblicus et Orientalis 198, 2004), and the two-volume *Enigmatic Writing in the Egyptian New Kingdom* (2020), volume 1 by Joshua Aaron Roberson and David Klotz, the set edited by Klotz and Andréas Stauder. There is no machine-readable corpus of enigmatic spellings; everything is in printed transliteration and hand copy, which is the binding constraint on any computational attack.

## Prior attempts and current consensus
Étienne Drioton's mid-century work established the phenomenon and proposed an acrophonic principle, and is now regarded as over-reading: he found enigmatic writing where later scholars find ordinary orthography. Darnell 2004 is the full edition and translation of the Solar-Osirian Unity compositions and the basis for most subsequent work. Roberson, Klotz and Stauder's 2020 volumes are the current state of the question and treat enigmatic writing as a describable system of sign-selection principles rather than a code, with the corpus surveyed and sign values collected. The consensus is that the compositions are readable in the main and that the residue is a matter of sign-value evidence, not of a missing key. Darnell 2004 and Roberson–Klotz 2020 are the two things a newcomer must read; Piankoff and Hornung give the surrounding Netherworld Books.

## What a solution would have to do
The well-posed problem here is the derivation of sign values, and it has a mechanical check that most decipherment problems lack. A proposed value for an enigmatic sign must (i) be derived by alignment: the same word or phrase must be attested in orthodox orthography somewhere in the Egyptian corpus, so the substitution can be read off rather than guessed; (ii) predict correctly at every other occurrence of that sign in the enigmatic corpus, not only at the occurrence that motivated it — this is the test that kills the Drioton-style proposal that works once; (iii) be assigned to a stated selection principle, with the claim that the principle is productive tested across the corpus rather than asserted; (iv) yield Egyptian that is grammatical and theologically coherent with the accompanying scenes, which are pictorial and independent of the text. A claim to have read a currently unread passage must state which sign values are new, which are inherited, and what fraction of the passage rests on conjecture. The prerequisite for any of this at scale is the thing nobody has built: a machine-readable corpus of enigmatic spellings aligned to their orthodox equivalents. That is a finite, fundable digitization job, and naming it is the useful result of this entry.

## Why the scores
- mystery 3: real and open at the level of individual passages and of the underlying system; not higher because the compositions' content and purpose are broadly known and no field-changing revelation is expected.
- material 4: the monuments survive, are accessible, and are fully published in hand copy and photograph for the main witnesses; not 5 because there is damage and no critical digital corpus.
- solvable 5: these are texts written by priestly workshops to convey determinate theology, and much of them is already read. There is no serious hoax or noise hypothesis.
- compute 4: deriving a substitution system by aligning enigmatic spellings against a large corpus of orthodox spellings is exactly a computational decipherment problem with a built-in cross-validation test, and it has never been done at corpus scale. Not 5 because the data is not ready: it exists as print transliterations, so the first year of any project is encoding.
- verifiable 4: a proposed sign value predicts readings elsewhere in the corpus and either works or does not — strong criteria, short of the mechanical certainty of a key that decrypts.
- crowding 4: a handful of serious treatments (Drioton, Darnell, Roberson, Klotz, Stauder) and a very small specialist community; among the emptiest fields in this category.

## Sources
- SCHOLARLY — Joshua Aaron Roberson and David Klotz, *Enigmatic Writing in the Egyptian New Kingdom: Revealing, Transforming, and Display in Egyptian Hieroglyphs* (2020), and the two-volume set edited by David Klotz and Andréas Stauder (2020) — bibliographic records. https://openlibrary.org/search?q=Enigmatic+Writing+in+the+Egyptian+New+Kingdom
- SCHOLARLY — John Coleman Darnell, *The Enigmatic Netherworld Books of the Solar-Osirian Unity: Cryptographic Compositions in the Tombs of Tutankhamun, Ramesses VI and Ramesses IX*, Orbis Biblicus et Orientalis 198 (2004) — bibliographic record. https://openlibrary.org/search?q=Enigmatic+Netherworld+Books+of+the+Solar-Osirian+Unity
- SECONDARY — Wikipedia, "Enigmatic Book of the Netherworld" (the definition of the cryptic writing as using "non-standard meanings for each hieroglyphic sign"; attestation on Tutankhamun's second shrine in KV62, and in KV9 and KV6; the late 18th to 20th Dynasty range). https://en.wikipedia.org/wiki/Enigmatic_Book_of_the_Netherworld
- SECONDARY — Wikipedia, "Book of Caverns" (complete versions in the Osireion, KV9 and KV6; eight attesting sites; Rosellini 1836, Champollion 1844, Lefébure 1889, Piankoff 1942–45, Hornung 1972, Werning's text-critical edition). https://en.wikipedia.org/wiki/Book_of_Caverns
- SECONDARY — Wikipedia, "Amduat" (twelve-hour structure; KV34 as the earliest complete version; KV20, KV38, Wadi C-4, KV35, WV22 and the tomb of Useramun; Hornung's editions). https://en.wikipedia.org/wiki/Amduat

## Unverified claims
- The specific content of the Roberson–Klotz–Stauder 2020 volumes and any statement they make about how much of the corpus can be read. The publisher's page could not be retrieved (De Gruyter returned 405 / redirect loops), so the characterization of their approach above is the compiler's, from the titles and from the general literature, and is the main reason `confidence` is low.
- Étienne Drioton's acrophonic theory and the field's later verdict on it — reported from memory, not sourced here.
- The claim that no machine-readable corpus of enigmatic spellings exists. No such corpus was found, but the absence was not confirmed with the Thesaurus Linguae Aegyptiae or the Ramses project.
- Colleen Manassa Darnell's role in the Netherworld Books scholarship, and the SBL Press *Ancient Egyptian Netherworld Books* volume.
- Whether the Amduat and Book of the Earth contain enigmatic passages in the strict sense, as opposed to unusual orthography; the encyclopedic sources for both texts do not mention enigmatic writing at all, and the claim here that such passages are "embedded" in them should be checked against Roberson–Klotz before it is relied on.
