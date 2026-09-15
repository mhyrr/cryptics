+++
title = "Herculaneum papyri (the unopened scrolls and the Vesuvius Challenge)"
slug = "herculaneum-papyri"
kind = "fragment"
era = "c. 300 BCE – 79 CE (copied); buried 79 CE"
origin = "Villa of the Papyri, Herculaneum, Campania"
language = "Greek (mostly); some Latin"
status = "partial"
confidence = "medium"
digitized = "https://scrollprize.org/"
tags = ["papyrus", "carbonized", "virtual-unwrapping", "compute-calibration", "Philodemus", "Epicurean", "Stoic"]

[scores]
mystery = 4
material = 4
solvable = 5
compute = 5
verifiable = 5
crowding = 2
+++

# Herculaneum papyri (the unopened scrolls and the Vesuvius Challenge)

## What it is
The only library to survive from classical antiquity in situ: roughly 1,800 carbonized papyrus rolls and fragments excavated 1752–54 from the Villa of the Papyri at Herculaneum, buried by Vesuvius in 79 CE. Most of what has been read is Epicurean philosophy, above all Philodemus of Gadara. The bulk is in the Officina dei Papiri of the Biblioteca Nazionale di Napoli; smaller groups are in the Institut de France (Paris), the Bodleian and the British Library (royal gifts of 1810). A few hundred rolls were never opened; physical unrolling (Piaggio's machine from 1756, the Oslo peeling method from 1969) destroyed or damaged many others.

## What is unsolved
What the still-rolled scrolls say. This is not an interpretive puzzle; it is a reading problem: the text is intact inside the rolls but the carbon-based ink has almost no X-ray contrast against carbonized papyrus, and the rolls cannot be opened. The entry is here as the catalog's key calibration case for the `compute` axis: a text whose "solution" is purely a matter of imaging, segmentation, and ink detection, and which is now falling year by year. Secondary open questions: which authors are in the unread rolls (Latin literature? lost Epicurus? lost Stoics?), and whether the unexcavated parts of the villa hold more.

## What survives
- The physical rolls and fragments, catalogued as PHerc. numbers (Naples) and PHerc. Paris (Institut de France); many opened pieces published in *Cronache Ercolanesi* and the CISPE editions since 1969. The Wikipedia summary of the inventory gives about 1,826 items: more than 340 nearly complete, about 970 partly decipherable, more than 500 mere fragments (SECONDARY; the "unopened" count is not stated there and estimates vary; see Unverified claims).
- Micro-CT scans of a handful of intact rolls (PHerc. Paris 3, PHerc. Paris 4, PHerc. 172, PHerc. 332, PHerc. 1667, PHerc. 139) at Diamond Light Source (2019, 4–8 µm) and ESRF Grenoble (2025–26, down to ~1.1 µm), released openly by the Vesuvius Challenge with segmentation and ink-detection code under Creative Commons (PRIMARY, machine-readable volumetric data).
- What has been read from unopened rolls, as of 15 Sept 2026: (a) Oct 2023, first word, *porphyras*, in PHerc. Paris 4; (b) Feb 2024, Grand Prize, 15 columns plus 11 partial columns, over 2,000 characters, about 5 % of PHerc. Paris 4, an Epicurean text on pleasure attributed to Philodemus; (c) May 2025, the title of the still-rolled PHerc. 172 (Bodleian) read as Philodemus, *On Vices*, Book 1; (d) 25 June 2026, PHerc. 1667 read end to end: ~1.4 m of papyrus, ~22 columns, a Stoic ethical treatise naming Aristocreon (nephew of Chrysippus), transcribed by papyrologists from ML ink predictions, with the caveat that the roll is only the 8 cm inner core of an originally 19–24 cm roll and that readings are gappy; (e) PHerc. 139 identified as Philodemus, *On the Gods*, Book 8. The end-to-end result is a preprint (arXiv 2606.29085, submitted 27 June 2026), not yet peer-reviewed.

## Prior attempts and current consensus
Seales (Kentucky, EduceLab) demonstrated virtual unwrapping on the En-Gedi scroll (2016) and argued for a decade that Herculaneum ink could be recovered from phase-contrast tomography. The 2023 Vesuvius Challenge (Seales, Friedman, Gross) turned this into an open competition; the winning pipeline is segmentation of the rolled sheet in the CT volume, flattening, then a supervised ink detector trained on "crackle" texture visible in the volume and validated against opened fragments where ground truth exists. Verification is by an independent papyrological board (Nicolardi, Delattre, Del Mastro, McOsker, Fleischer among those named) reading the flattened output. The consensus is that the method works and is limited by scan resolution, roll condition, and the labour of segmentation, not by any theoretical barrier; the stated program for 2026–27 is "read multiple entire scrolls," with prizes closing 25 June 2027. The remaining scholarly debate is about the readings themselves (the Stoic attribution of PHerc. 1667 is offered as evidence-based but not settled) and about how much of a badly compressed roll can ever be flattened.

## What a solution would have to do
For any single roll: produce a continuous flattened surface covering the roll, an ink map, and a transcription that a papyrologist can read column by column, with the ML predictions checked against (i) opened fragments of the same roll where they exist, (ii) internal consistency of Greek, (iii) reproducibility of the pipeline by a second team from the released volume. The bar is already defined by the challenge's own criteria (for 2023: four passages of 140 characters with at least 85 % recoverable). For the collection: a cost-per-scroll and throughput that make the several hundred unopened rolls a finite project, plus a rule for what counts as "read" for a roll whose outer layers are lost. A claimed attribution (author, title) must rest on a read *subscriptio* or on verbatim overlap with known text, not on subject matter alone.

## Why the scores
- mystery 4: the content is genuinely unknown and finds so far (a Stoic text among Epicurean rolls) already shift the picture of the library; not 5 because each roll is one more work of Hellenistic philosophy rather than a field-changing event.
- material 4: the objects exist and the scanned rolls are fully digitized and open; but only a handful of the few hundred unopened rolls have been scanned, and outer layers of some rolls are physically gone.
- solvable 5: there is certainly text, and pieces of it have now been read.
- compute 5: the whole problem is imaging plus ML segmentation and ink detection, the data is public, and progress is measurable in characters per year. This is the calibration anchor for the axis.
- verifiable 5: recovered Greek is either readable or not; independent teams reproduced the 2025 title reading.
- crowding 2: thousands of competitors, a funded organization, and a dedicated papyrological community; not 1 because the per-roll work is far from exhausted.

## Sources
- PRIMARY — Vesuvius Challenge, "An entire Herculaneum scroll has been read for the first time" (25 June 2026), PHerc. 1667 details. https://scrollprize.org/firstscroll
- PRIMARY — Vesuvius Challenge, 2023 Grand Prize announcement (5 Feb 2024): PHerc. Paris 4, 15 columns, >2,000 characters. https://scrollprize.org/grandprize
- PRIMARY — Vesuvius Challenge FAQ (scanned rolls, prize deadlines to 25 June 2027, resolution caveat). https://scrollprize.org/faq
- SCHOLARLY (preprint) — Angelotti, Parsons, Nicolardi, Nader, Johnson, … Seales, "Complete virtual unwrapping and reading of a rolled Herculaneum papyrus," arXiv 2606.29085 (27 June 2026). https://arxiv.org/abs/2606.29085
- SCHOLARLY — University of Kentucky Research, "The day the Herculaneum scrolls began speaking again." https://uknow.uky.edu/research/day-herculaneum-scrolls-began-speaking-again
- SCHOLARLY — Herculaneum Society (Oxford), "Papyri": ~1,800 fragments, perhaps 800 original volumes; hundreds still rolled. https://www.herculaneum.ox.ac.uk/index.php/papyri/
- SECONDARY — Wikipedia, "Herculaneum papyri" (inventory counts, unrolling history, challenge timeline). https://en.wikipedia.org/wiki/Herculaneum_papyri
- SECONDARY — Wikipedia, "PHerc. Paris. 4" (2019 Diamond scans at 4–8 µm; 2024 reading). https://en.wikipedia.org/wiki/PHerc._Paris._4
- POPULAR — CNN, "Title and author of burned, still-rolled Herculaneum scroll decoded" (6 May 2025): PHerc. 172 = Philodemus, *On Vices*, Book 1. https://www.cnn.com/2025/05/06/science/herculaneum-scroll-title-author-decoded-intl-scli
- POPULAR — Artnet, "Entire Herculaneum Scroll Deciphered by A.I. for the First Time" (2026). https://news.artnet.com/art-world/herculaneum-scroll-translated-unraveled-vesuvius-challenge-2784765

## Unverified claims
- The exact number of unopened rolls. Figures between roughly 280 and 600 circulate; the challenge speaks of "a few hundred" and, in 2024, of "all 300 scrolls." No authoritative per-institution count of intact rolls was found.
- The attribution of PHerc. 1667 to Chrysippus himself (Wikipedia phrases it "may be attributable to Chrysippus"); the challenge's own page says only that Aristocreon is named and the context is Stoic.
- Whether the PHerc. 172 book number "1" is secure; the CNN report says "could even be the first book … though this is not yet clear."
- Whether further rolls remain in the unexcavated parts of the villa (the Herculaneum Society calls this "tantalising," not established).
