# Scout D: 2839+2841, 881, 1392, 649 (2026-11-19)

Rows are in `scout-D.tsv`. Images are in `sources/cache/cross/<id>/` (gitignored). No candidate passes. Two are
known-key jobs, one is stopped by image size, and one is an open outside target.

## 2839 + 2841: Hautefort to Bellièvre, 1584. Fail at not taken: the key is published
- **What I saw.** f. 158 (Gallica IIIF via openapi.bnf.fr, opening 8795 px wide; gallica.bnf.fr/iiif returns 403)
  is a full page of 31 lines in a sign cipher. A few tiny interlined letters sit over about four lines; that
  is not a usable pair. fr. 15568 f. 207 (9642 px) opens "Monsieur" in clear, then about 36 lines are entirely
  in cipher. Both pages show heavy show-through. By `sign_height.py` the median sign height is 25 px on f. 158
  and 28 px on f. 207; by eye the signs are 60-100 px tall. These are the best images in my set.
- **Tomokiyo's table** (henryiii.htm, image saved as `henryiii_Hautefort.png`). It gives about 39 letter signs,
  at least one for every letter a-x, with 2-4 homophones for the common letters. y and z have no value. It also
  gives 1 null and 4 word signs (vous 12, nous 20, par, que). That is complete enough to read the letters.
  What it lacks: two-digit signs seen on f. 158 (13, 14, 15, 17, 35) that are not in it and are probably more
  word signs.
- **Verdict.** This is a known-key reading of about 8 pages, a worthwhile separate job. It is not a key build.
  Tomokiyo assigns f. 162 to Maygnieulx's cipher, so the cipher passages on ff. 162-164 may not be Hautefort's.
- **What could change it.** Nothing on the key side. Open lead: an ARCSI PDF (https://www.arcsi.fr/doc/Tant/420.pdf)
  cites a Grenoble colloquium talk by Jacques de Monts de Savasse on "son déchiffrement"; it was not opened.

## 881: Francia 32, 1590-91. Fail at not taken: the key is published and already applied
- The outside targets sega1590 (R5612, R5616) and sega1591b (R5615, 82.7% read) read this volume with Meister 1906
  key 65 unchanged. The key was validated on the decifrato of 21 Dec 1590 (0.934, against at most 0.551 for
  shuffled keys). The remaining records (R5613-14, R5617-21) are Sega's series and almost certainly the same key.
  R5613 carries a "Decifrato" (Dudout, in the sega1591 profile).
- I did not view the images (DECODE needs a login). This is a known-key job, if anyone wants it.

## 1392: Trémais, Montréal 1759. Fail at readable
- **The pair is real and online.** NFA item 27540 (https://nouvelle-france.org/eng/item/details?id=27540)
  holds the 22 Sept cipher letter, ff. 342-343v, and its contemporary clear decipherment, ff. 344-345, in 4 images.
  I saw the decipherment page ("...Je crains bien, Monseigneur, que la précipitation...", "...I fear, my lord, that
  the haste..."). By eye the cipher letter has about 500 groups.
- **The same code is used on 6 Nov** (item 27542): the same groups and stacked pairs (8, 108, 287, 466, 219 over
  466) appear on both letters.
- **The wall.** The LAC server gives at most 1125 px per spread. Digit height is 5-6 px by script. The breach is
  ANOM's own scans or higher-resolution LAC images (not checked). Digits may stand up to small sizes better than
  invented signs, but the calibration was done on signs.
- **Not fully free.** The catalogue records Brice Dudout's partial key from this same pair (0.704 on held-out
  text, 5 Nov 2026). There is no outside profile for it yet. Coordinate before taking it.

## 649: Delacroix to Létombe, 1797. Fail at not taken; buildable would fail too
- The outside target delacroix1797 (profile fetched today) is still "not read", fraction 0, last worked
  2 Nov 2026. The catalogue id is not in the taken file because the profile does not name it.
- Frame 0245 (4552 px) is clean: the digits are about 40 px tall by eye. The script gives 9 px because the full
  stops between groups pull the median down.
- There is no pair, no minute online and no neighbour key. The wall is the AMAE CP États-Unis 47-48 minute or
  CADN 519PO/1. I could not check issue #122 directly (the GitHub tool is down).

## Searches run
1. "Hautefort Bellièvre 1584 chiffre Grenoble déchiffrement"
2. "Delacroix Létombe 1797 cipher despatch decrypted messidor an V"
3. "Querdisien Trémais lettre chiffrée 22 septembre 1759 déchiffrement"
4. "Filippo Sega nunzio Francia 1590 Dizionario Biografico"

None of them found a reading. I also ran a profile grep over all 887 profiles.
