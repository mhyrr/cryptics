# Period-dictionary page images (Decimator, *Sylvae quinquelinguis*, Frankfurt 1595/1596)

Full-page scans, uncropped, at the native resolution the Bayerische
Staatsbibliothek (BSB) IIIF image service exposes (about 1290 × 2120 px per
octavo leaf, roughly 300 ppi). Acquired 2026-09-17 for experiment 05
(`../../analysis/05-period-dictionary/`). Tier: PRIMARY (digital facsimile).

- `SOURCES.tsv` — one row per image: filename, IIIF source URL, viewer URL,
  viewer page, printed signature (read from the image), volume/year, capture
  date, uncertainties. Read this before using any image.
- `MANIFEST.sha256` — `shasum -a 256 -c MANIFEST.sha256` from this directory.

## Volumes

| BSB id | Object | Scans | Division evidence |
|---|---|---|---|
| bsb11762465 | Pars prima, Frankfurt, Ex Officina Paltheniana, sumtibus Nicolai Bassaei, 1596 | 1158 | Title page does not print a letter span. Body runs scan 55 (initial A, headword "Aal.", sig. A 3) to scan 1153 (last headword "Syrup."). |
| bsb10314207 | "Partis I. Pars II.", same imprint, 1595 | 276 | Title page does not print T–Z. Scan 2, "Palthenius lectori", states the new part begins "hac ipsa litera T"; scan 3 opens with "Tach." Running heads T → V (34) → W (150) → Z (214). |

Neither volume is paginated or foliated. Locators are viewer scan + gathering
signature (rectos) or catchword (versos). Verso leaf identities are inferred
from flanking rectos and are marked as such in `SOURCES.tsv`.

## Entry locators

| Headword as printed | Volume | Entry begins | Entry ends | Signature | Neighbours |
|---|---|---|---|---|---|
| Himmel. | 1596 | scan 690, left col., lower | scan 692, right col., upper; next headword "Himmelblaw." | 689 = Ss 2, 691 = Ss 3, 693 = Ss 4 | before: Hüfft, Hütte (non-alphabetical, verified on image); after: Himmelblaw, Himlisch |
| Lehrer / Schulmeiſter / Vnderweiſer. | 1596 | scan 834, right col. | same page; next headword "Lehrnen/Studieren." | 833 = Ddd 3, 835 = Ddd 4 | before: Lehr, Lehren; after: Lehrnen, Lehrhafftig, Lehrnung, Lehrung |
| Vnterweiſer. | 1595 | scan 105, foot of left col. | scan 105, top of right col.; next "Vnterweiſung." | Gggg 5 | before: Vnterweiſen; after: Vnterweiſung, Vnterwerffen |
| Wachs. | 1595 | scan 150, right col., foot | scan 151, left col. | 151 = Kkkk 4 | before: Wachendt; after: Wachſen. W section opens on scan 150. |
| Warſager. | 1595 | scan 159, left col. | same column | none printed (Kkkk 8 recto, by quire arithmetic) | before: Warlich; after: Warſagung |
| Waſſer. | 1595 | scan 160, left col., mid | scan 161, right col. | 161 = Llll | before: Warumb; after: Waſſer auß dem Brunn ſchöpffen |

U and V are merged under V in the 1595 volume. Note the 1596 volume spells the
Lehrer synonym "Vnderweiſer" (d), while the 1595 headword is "Vnterweiſer" (t).

## Legibility limits

Latin, French, Fraktur and long-s are fully legible. Greek accents mostly
legible; breathings in italic Greek are marginal. Hebrew consonants legible;
Hebrew vowel points are at or past the limit of this digitization. In the
Vnterweiſer entry (scan 105) the first Hebrew gloss, transliterated
"melabbed", has a third letter ambiguous between bet and mem at native
resolution. Left unresolved; do not infer it from the square.

## What these are not

These pages are discovery-exposed checks of Kollatsch's quoted examples. They
are not an independent test lexicon. A subsequent main-thread reading saved
scoped Latin transliteration excerpts and a comparison audit in
[experiment 05](../../analysis/05-period-dictionary/FACSIMILE-FINDINGS.md).
No full multilingual transcription or comparison edition for the alleged
Vnterweiſer error has been acquired.
How they were found (IIIF manifest, per-canvas hOCR, running-head sweep, then
image verification at 200–400 %) is in `../../research.md` under 2026-09-17.
