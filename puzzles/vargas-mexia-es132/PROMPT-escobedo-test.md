# Session prompt: verify the pre-murder record on Don John and the Guises (H16)

Paste everything below the line into a fresh session.

---

/focus vargas-mexia-es132

Goal: independently verify, from the ciphered originals, what Philip II knew and asked about Don John and the Guises
before Juan de Escobedo was murdered (31 March 1578), and close H16. Then reconcile our work with the two third-party
projects that read es. 132 before or alongside us.

## Read first, in order
1. `NEXT.md`, `README.md`, `canon.md`, `hypotheses.md`; search `research.md` (entries of 2026-10-04 "session 3, later"
   and "after close" are the context for this session).
2. `OVERVIEW.md` §7 (the argument) and §5 (what is and is not new).
3. `sources/escobedo-letters-survey-2026-10-04.md` (every letter in the window: where it is, cipher, print, images).
4. Third-party readings, cached in `sources/cache/thirdparty/` (git-ignored; re-fetch from GitHub if missing):
   `el-descifrador/cabinet-noir` folder `es132-vargas-mexia/` (30 letters, 29 Sep – 1 Oct 2026) and
   `pangoleen/cipher-readings` (4 Oct 2026). Both CLAIMANT, model-produced, no paleographer.
5. `sources/transcription/CIPHER3-GUIDE.md`, `sources/keys/README.md`, `sources/cache/mignet1846.txt`.

## Where things stand (do not re-derive)
- Pérez (via Mignet pp. 68–69) named a Don John–Guise "confederation … de défense des deux couronnes", denounced by
  Vargas, among the reasons for the murder. Mignet (pp. 71–73): Vargas reached Paris only on 10 Dec 1577; his Guise
  reports are "presque toutes postérieures au meurtre".
- Printed already (Teulet vol. 5, 1862, official Simancas decipherments; archive.org `relationspolitiq05teul_0`):
  Vargas 16 Feb 1578 relays hearsay of a Don John–Mary Stuart marriage and an English enterprise with Guise help, which he
  calls "quimeras"; Vargas 13 Apr 1578 (post-murder) is the "unión destas dos coronas" letter with Philip's "Ojo!", about a
  Spain–France union.
- The King's reply of 8 Mar 1578 is es. 132 **f. 17–20v with its duplicate f. 22–25r (Cipher 2)**: two passages printed by
  Mignet (app. E pp. 437 n. 2, 439 n. 5); full reading by cabinet-noir ("de poco fundamento"; keep Guise "en mi devoción";
  no money out of France to Don John without the French King's licence).
- Provisional verdict in OVERVIEW §7: rumours before the murder, discounted; the "confederation" as Pérez framed it is
  not in the pre-murder record.

## H16, pre-registered (write into `hypotheses.md` before any reading)
- H16a: a letter in the window (10 Dec 1577 – 31 Mar 1578) reports or asks about a Don John–Guise league, pact or
  "unión" (beyond the marriage/England hearsay of 16 Feb).
- H16b: none does; the window holds only the hearsay of 16 Feb and the King's dismissive reply of 8 Mar.
- Test: every es. 132 letter of the window is read in full by our blind readers (ff. 3, 11, 17–25, 26 [+dup], 32, 34),
  plus every Teulet excerpt of the window is checked against the printed page. H16a is supported by one clear passage
  quoted with token positions; H16b by all window letters read with none. Any letter not read is listed as the wall.

## Work, in order
1. **Experiment folder** `analysis/06-premurder/` with a README pre-registering H16 and the steps below. Commit first.
2. **Cipher 2 decoder** `decode_c2.py` from `keys/cipher2.tsv` and Tomokiyo's conventions (his page, cached at
   `sources/cache/cryptiana/spanish3D.htm`: + = e, e/ρ-like = a, underdot = i, overdot = o, dot to the right = u,
   overbar = null?; numbers 2–23; letter-forms for clusters). Frozen by commit. **Calibrate on three printed texts before
   any new reading**: Tomokiyo's partial transcription of f. 11v (his page), and Mignet's two printed passages of the
   8 Mar 1578 letter (the decoded f. 17–25 must reproduce them; score by script).
3. **Cipher 2 transcription guide** (shapes only, as `CIPHER3-GUIDE.md`), from Tomokiyo's f. 11v image
   (`sources/cache/cryptiana/BnFes132f11v.png`). One blind calibration reader on f. 11v, scored against Tomokiyo.
4. **Two blind readers each** (Sonnet 5.5; tell them not to spawn agents) for f. 17–20v and its duplicate f. 22–25r (the
   duplicate checks the original), f. 11–12v, f. 34, f. 26 (and its duplicate if imaged; a third party says ff. 26v–31r are
   missing from the scan: check canvas mapping, canvas c = f. (c+3) recto on the right page), and f. 32 (Cipher 3, guide
   v2.1). Readers see only the guide and the Gallica images
   (`https://gallica.bnf.fr/iiif/ark:/12148/btv1b10032556x/f{canvas}/{x},{y},{w},{h}/full/0/native.jpg`, python urllib with a
   User-Agent; shell curl is blocked). Never keys, decodes, third-party readings, Mignet, or this prompt. Commit each before
   decoding. Reconcile with `analysis/05-cipher4-v2/align.py` and a blind reconciler (crops only; watch for notation
   collapse, e.g. a digit merged with the virgula).
5. **f. 3 (16 Dec 1577, Cipher 1)**: `decode_c1.py` from `keys/cipher1.tsv` (partial table; report every gap; Devos's
   conflicting values 12 a / 21 e / 31 u are flagged, never chosen silently). Two readers. If the table is too thin, name the
   wall (Devos p. 418; Tomokiyo's Academia.edu reading of f. 3, which returned 403).
6. **Teulet check**: fetch the djvu text and page images of Teulet vol. 5 pp. 132–146 yourself; quote the 16 Feb and 13 Apr
   1578 passages exactly, with page numbers. (The survey read OCR only.)
7. **Compare with third parties** (after our decodes are frozen): for each letter both projects read, a script diff of
   decoded syllables or words; record agreement and disagreements in `analysis/06-premurder/thirdparty-compare.md`.
   Also check our Cipher 3 code values (u., 108⁺, 149⁺, T⁺) against Alcocer 1921 / Devos as quoted by cabinet-noir
   (`cle/`), and pangoleen's ff. 87, 157, 179 against our v2.
8. **Synthesis on the main thread**: judge H16; rewrite OVERVIEW §7 point 3 and §5 if anything changes; rebuild and
   republish (`python3 overview-build/build.py OVERVIEW.md overview-build/template.html <out>.html`, then publish to
   https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2 by passing its URL).

## Honest scope
This closes one plank of the Escobedo mystery (whether the Guise "confederation" was a pre-murder fact). It does not
show who wanted Escobedo dead or why; the King's complicity rests on his own April 1579 note (Mignet p. 120 n. 2), not on
these letters. Documents that could move the motive question are not ciphers we hold: Pérez's papers and the Hague
manuscript, the trial records, and Simancas Estado K 1543–1558 (PARES was down on 4 Oct; retry, or ask Greg).

## Rules
AGENTS.md throughout. Before claiming anything is new, search GitHub and the web for the shelfmark ("Espagnol 132",
"es132", "Vargas Mexía") as well as known solvers. Freeze before testing; commit transcriptions before decoding;
statistics from scripts; findings filed as they happen; stop at a clean wall and name it; `/session-close` at the end.
