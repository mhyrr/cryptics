# No. 2946 (with 2947) — Gianfrancesco Gonzaga to Cosimo de' Medici, 1439

**Verdict 2026-11-19: go, under an 11 px exception that Greg accepted the same day.** The readable gate (15 px)
fails: signs measure 10–11 px, and the server's native size is 1272 px wide (`info.json`, checked). Every
other gate passes. The precedent is no. 1336 c. 269r (11 px, readers 0.80, four readers and a vote merge).

## The two letters
| | Catalogue 2946 | Lead 2947 (not in the catalogue) |
|---|---|---|
| Shelfmark | ASF, Mediceo avanti il Principato XI, c. 215 (viewer image 432) | same filza, viewer images 690–694 |
| Date | "Ex Sablo die xxiiij Januarij 1439" | "31 Xbre 1439" (later hand, 691); dateline on 694 "... die ultimo decembris 1439" |
| From / to | signed "Johannesfranciscus Marchio Mantue" | same signature on 694; address on 694 verso side and 690: "Magnifico Amico nostro car(issi)mo Cosme de Medicis" |
| Form | about 19 lines, clear Italian with cipher runs; nothing between the lines | four pages, about 165 lines, clear Italian with cipher runs; **a second hand glosses the cipher word by word between the lines** (form A2) |
| Role | the bare target | the pair |

PRIMARY · [c. 215](https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/00100011/A0000432.ptif/full/full/0/default.jpg);
images 690–695 by the same path (`PROVENANCE.md`).

## Checks
1. **Race.** Not in `line/taken-2026-11-19.tsv`. A grep of the 887 outside profiles fetched today (Gonzaga,
   Cosimo, `00100011`, filza XI) finds no target on MAP XI. The outside Gonzaga targets of the 1420s–30s are
   letters **to** Gianfrancesco in the Mantua archive (below). CLAIMANT · [catalogue](https://dbourdeau.github.io/cyphersolver/).
   Not checked: DECODE live search (login wall), Mantua copy-books for a clear minute.
2. **The pair is real.** The gloss on 691–694 sits over the cipher runs of the same leaves, in a second hand.
   The c. 215 run `θ ⊕υ. M. ⊧HX-o-ΔL:υ⊥+` (line 1) recurs on 691 (line 10) and on 694 (line 3), glossed there
   (by eye: "quelle comunita"). One table is likely (H10); the shared run is an observation, not a test.
3. **Images.** All five pages fetched at the native maximum (1272 px wide). Signs separate cleanly at 3x
   (`strips.py`). The gloss is small and faint but mostly legible at 3x (seen on 691: "partissemo",
   "tanto bene", "alchuna", "di Signori da milano").
4. **Size.** By eye: 2947 about 4,000 cipher signs, many under gloss; 2946 about 400 bare signs. Above the
   150-sign floor by far. Counts follow from the readers.
5. **A period key.** No key for Gianfrancesco's own cipher of 1439 is known to us. Four outside targets read
   letters to him of 1428–30 (Mantua archive, DECODE R1854) with keys of their own: `mutiliana1428`
   (Italian, homophonic, nulls including `+`, three name codes), `r1854`, `cattanei1430`, `malatesta1428`
   (Latin). Their files are in `sources/raw-outside/` (untracked). They are neighbours to hold on the pair
   (METHOD 0b) once our transcription exists. DECODE R1853 (Gonzaga register c. 1401–20) did not fit those
   letters (outside profiles).

## What this item costs, and the caveats
- **11 px.** Readers will disagree more than at 20 px. Plan four cipher readers and a vote merge from the start.
- **Form A2.** The gloss sits on the cipher page, so the cipher readers see it. Their reading of shapes is not
  blind to the plain side. The clean test is therefore c. 215, which has no gloss, and a held-out page of 2947
  whose gloss the build never sees.
- **Number groups** (19, 32, 33, 39, 66, 68) inside the runs are probably codes (nomenclator). They may stay
  unvalued.
- **Language.** Mantuan chancery Italian of 1439, not the Tuscan or Venetian of the letter model. The letter
  model for step 6 must be checked on the clear text of these letters first.

## Order (METHOD)
Strips (`strips.py`) → plain guide and clear-word readers (line frame and gloss) → sign guide → four cipher
readers → merge → design counts and the neighbour keys held (0b, 0c) → **stop for Greg** → build on Fable →
registered test → lattice on c. 215.
