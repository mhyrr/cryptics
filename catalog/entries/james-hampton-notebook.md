+++
title = "James Hampton's notebook (\"Hamptonese\", St. James: The Book of the 7 Dispensation)"
slug = "james-hampton-notebook"
kind = "cipher"
era = "c. 1950–1964"
origin = "Washington, D.C."
language = "unknown (English suspected; possibly glossographia)"
status = "unsolved"
confidence = "medium"
digitized = "https://www.cs.sjsu.edu/faculty/stamp/Hampton/hampton.html"
tags = ["private-script", "visionary-art", "religious", "glossolalia", "transcribed", "Smithsonian", "outsider-art"]

[scores]
mystery = 3
material = 4
solvable = 3
compute = 4
verifiable = 4
crowding = 4
+++

# James Hampton's notebook ("Hamptonese")

## What it is
James Hampton (1909–1964), a Black janitor for the General Services Administration in Washington, D.C., built *The Throne of the Third Heaven of the Nations' Millennium General Assembly* in a rented garage; it is now in the Smithsonian American Art Museum. With it he left notebooks titled *St. James: The Book of the 7 Dispensation*, written mostly in a script of his own, now called Hamptonese, with chapter numbering like the Bible and occasional English words ("Jesus", "Virgin Mary", "Revelation", "fear not"). The writings came to the Smithsonian with the Throne and exist on microfilm in the Archives of American Art.

## What is unsolved
Whether Hamptonese encodes language at all, and if so, what it says. The realistic possibilities: a substitution or syllabic cipher for English; a private shorthand; or "writing in tongues" (glossographia), a devotional script with no plaintext. The last is a respectable hypothesis, not a dismissal: Hampton was a religious visionary, and the chaptered, carefully spaced pages fit both a scripture he meant to be read and a performance he meant to be looked at.

## What survives
Stamp and Le count 164 pages of Hamptonese in two sets. The first mixes tombstone-shaped drawings, Roman numerals, Hamptonese and a good deal of English. The second is 100 pages of almost "pure" Hamptonese, 25–26 lines a page, no punctuation, the direction of reading not certain. Mark Stamp (San José State) put images of all 100 pure pages online in JPEG and TIFF (104 files, four duplicates) and, with Ethan Le, a complete plain-text transcription with a symbol key. It marks illegible symbols `*` and doubtful ones `#`, and puts interspersed English in brackets: more than 29,000 characters in all. Some pages have water damage and ink blots. The Smithsonian microfilm is the primary.

## Prior attempts and current consensus
Stamp and Le, "Hamptonese and Hidden Markov Models" (Springer, *Lecture Notes in Control and Information Sciences*, 2005), is the one serious study. Single-, di- and tri-symbol entropies are close to English (4.41 / 3.63 / 3.08 bits against 4.11 / 3.54 / 2.68 for English letters). Hidden Markov models that separate vowels from consonants in English with 10,000 symbols found no comparable structure in 29,000 Hamptonese characters. The authors conclude it is not a simple substitution for English and give "some evidence" that it is the written equivalent of speaking in tongues. They list the other explanations themselves: transcription noise, wrong segmentation (symbol combinations as units), or a script that is not a letter substitution. Since then there have been popular articles, a Medium statistical write-up, and a chapter in Bauer's *Unsolved!* (2017). No proposed decipherment has been taken seriously.

## What a solution would have to do
If a cipher: a stated mapping that reads the 100 pure pages continuously as English, or another named language, and also reads the mixed pages, where the English glosses around the script give a check the fitting never saw. It must say how the transcription's symbol inventory is to be segmented, since that is the likeliest point of failure. If glossographia: a positive demonstration, not a failed decode. That means showing the text's statistics match known glossolalia and glossographia corpora (syllable-like repetition, low long-range dependency, drift of the inventory over time), and do not match cipher and shorthand controls of the same size. Either answer must account for the Stamp–Le finding that the inventory changes substantially across the 100 pages.

## Why the scores
- mystery 3: wide open; a reading would matter to the history of American visionary art and to Hampton scholarship, and would be widely noticed, but it changes no field.
- material 4: complete images and a public transcription, but the segmentation into 42-odd symbols is one transcriber's and unchecked; it has doubtful marks and damaged pages.
- solvable 3: serious people hold both views. Its entropy is English-like and its layout scriptural; its HMM behaviour and devotional context point to tongues.
- compute 4: the data is ready, and the decisive tests are computational: re-segmentation, homophonic and syllabic fits against English, and a glossolalia-versus-cipher discriminator on matched controls. These can settle the family question even if they read nothing.
- verifiable 4: a cipher reading would be checkable mechanically and against the English on the mixed pages; a glossographia verdict is statistical, hence 4, not 5.
- crowding 4: one academic paper and popular write-ups; the modern homophonic and segmentation toolkit that broke Copiale and Z340 has not been published against it.
- compute mode: SAMPLE-VERIFY (segmentation × cipher family, checked by continuous decode) with a DESCRIBE fallback · verifier MECHANICAL if a cipher, CONSENSUS if not · space SAMPLABLE · signal YES · fit HIGH.

## Sources
- PRIMARY — James Hampton writings, circa 1950–1964, Archives of American Art, Smithsonian Institution (microfilm). https://www.aaa.si.edu/collections/james-hampton-writings-7162
- PRIMARY — Mark Stamp, Hamptonese page images (100 pages, JPEG/TIFF) and transcription with symbol key. https://www.cs.sjsu.edu/faculty/stamp/Hampton/pages.html and https://www.cs.sjsu.edu/faculty/stamp/Hampton/hampton.html
- SCHOLARLY — Mark Stamp and Ethan Le, "Hamptonese and Hidden Markov Models," in *New Directions and Applications in Control Theory*, LNCIS 321 (Springer, 2005). https://www.cs.sjsu.edu/faculty/stamp/Hampton/hamptonHMM/hamptonese.pdf and https://link.springer.com/chapter/10.1007/10984413_23
- SECONDARY — Smithsonian American Art Museum, "Reading Into the Throne: On James Hampton's Notebook." https://americanart.si.edu/blog-post/1337/reading-into-the-throne-on-james-hamptons-notebook
- SECONDARY — Wikipedia, "James Hampton (artist)" (108-page loose-leaf notebook, title). https://en.wikipedia.org/wiki/James_Hampton_(artist)
- POPULAR — Craig P. Bauer, *Unsolved!* (Princeton, 2017), ch. 10.

## Unverified claims
- The symbol inventory is given as 42 in a secondary summary of the paper; the paper's Table 1 was not recounted here.
- Notebook size is given variously: 108 pages (Wikipedia) and 164 pages of Hamptonese in two sets (Stamp and Le). The two counts may measure different things and were not reconciled.
- Whether the Stamp transcription files are still downloadable (the page was last updated 2003 and was not re-fetched file by file).
- Whether the SAAM blog post reports any newer analysis; it was located but not read.
- Whether the Smithsonian holds a second notebook or loose sheets beyond the microfilmed set.
