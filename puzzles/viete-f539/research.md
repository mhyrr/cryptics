# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

- **Ciphertext-only annealing on f. 539 as it stands** (H2), 2026-10-01. The matched control
  fails (median 0.093) while the positive control passes (0.986): `analysis/01-annealing/`.
  Same conclusion as Bourdeau, 2026-09-16, reached with a different transcription, solver,
  corpus and structural assumption.

---

## 2026-10-03 — DECODE, Aubery, and the April 1594 packet summary

- **DECODE R2281:** images not accessible with Greg's account. Not needed for the images
  (Gallica is better); the record's text content is still unchecked. Bourdeau's index reading
  ("Non-decrypted, one page, no transcription") stands.
- **Aubery 1654** (Gallica bpt6k856018v): the text export is empty. Gallica's notice gives an OCR
  rate of 0%, so the book exists only as 591 page images. To search it, read the images.
- **Tomokiyo's folio list** (`sources/tomokiyo.md`, pulled by Greg) has nothing new on f. 539. It
  points to f. 394, "Sommaire du contenu en divers pacquets surpris sur ceux de la Ligue en Avril
  1594": a royal summary of intercepted League letters from the same weeks. Canvas 399 = f. 394.
  It opens with Agocchi's Rome letters of 29 Jan and 5 and 15 Feb 1594: the League ambassadors'
  audience of 24 January, and their asking the Pope to declare Navarre's absolution void. The full
  scan for Joyeuse/Villars is in progress (`sources/cache/f394-summary-scan.md`).
- **f. 394 digest, full scan** (`sources/f394-summary-scan.md`): ff. 394r–399v, all from Agocchi's
  Rome letters. Joyeuse appears four times: he takes the League embassy in place of the Primate of
  Lyon; on the last day of January he asks to enter the audience alone; around 15 Feb he attends
  an audience with Sennecey and the Abbé d'Orbes, and the Pope refuses to hear of Navarre.
  There is no Villars, Rouen, Normandy, or "chiffre", and no gist of f. 539. Dead end for a
  plaintext; useful as context.
- **Joyeuse's clear letters of the same day** (`sources/joyeuse-siblings.md`; f. 544 = canvas 549R,
  f. 551 = 557R + 559L, f. 553 = 560R + 561L):
  - The news Joyeuse sent everyone is the Pope's refusal to receive Navarre for want of sufficient
    penitence (ff. 544, 551), with Mayenne and Sennecey in the background.
  - f. 551 to the Archbishop of Lyon says "Si j'avois le bien d'avoir un chiffre avec vous": no shared
    key there.
  - f. 553 to the duc de Joyeuse carries code numbers in Roman-with-c form (ij^c ix = 209,
    ij^c xiiii = 214, ij^c xxij) and a short letter-and-digit group. F. 539 also has 209 (H4).
  - None of the three mentions Villars or Rouen. Crib candidates are now in H8.

## 2026-10-01 — opening: race check, images, blind transcription

**Race check (step 0).**
- Bourdeau's write-up index (https://dbourdeau.github.io/cyphersolver/writeups.html)
  has no f. 539 write-up.
- His `TARGETS.md` (repo https://github.com/dbourdeau/cyphersolver, HEAD
  `9226922ffb0663b1d9b95f4ef898d093efd74ef2` on 2026-10-01) lists f. 539 in short-list row 5 as
  "Gated out 2026-09-16 … Closed 2026-09-16: not solvable online. Joyeuse attempted (controls fail)".
- His `targets/joyeuse/` holds the full attempt: a glyph-level transcription (one reader,
  one pass), the solver, three matched controls and six target runs. Summary in `canon.md`.
  Pinned copies are in `sources/cache/bourdeau/` (git-ignored; re-fetch from the commit above).
- Cryptiana `viete.htm` and `unsolved.htm` still list f. 539 as undeciphered.
- Verdict: not solved and not under active attack, but already attacked once and closed.
  This dive goes on because the one thing Bourdeau names as unchecked is his transcription,
  and the Marmont recipe's new step is the transcription. A blind second reading is the
  contribution this session can make.

**Images (step 1).** Gallica IIIF, full resolution: canvases 544, 545 (f. 539, 540), 561, 562,
563 (f. 555r–v and neighbours). SHA-256 in `sources/PROVENANCE.md`. Cipher-block crops
for the readers: `sources/cache/f539_block_view.jpg` and `sources/cache/bands/` (regions in
`REGIONS.tsv`).

**Transcription (step 2).** Two blind Sonnet readers (A and B) transcribe from the same crops.
Neither has seen Bourdeau's transcription. Each keeps its own inventory and lists candidate
merges without applying them. I (the main thread) have seen Bourdeau's file, so I adjudicate
only and do not read.

**Transcription result.** A: 365 tokens, 145 labels. B: 367 tokens, 165 labels. Per-line counts
agree within 3 with each other and with Bourdeau. The number sequence agrees except one digit.
Raw readings committed (`6e83b62`) before any analysis. Labels are not yet reconciled across readers.

**Gate (step 3).** Frozen before the counts (`006fa0b`). G1 passes: 344 sign tokens ≥ 300. G2: about
2.4 uses per sign, against 10 for f. 555 and 8 for Marmont (`analysis/00-transcription-and-gate/`).

**Annealing pre-registration (step 4).** Corpus: Brantôme (Gutenberg) and Montaigne's 1595 Essais
(Wikisource), 2.7 M normalized characters, with 10% held out for controls. Gallica full text is
behind a bot check. Solver tuning was on off-protocol seeds at the Marmont shape only, recorded in
the README. Two scoring bugs were found and fixed there (conditional-model drift, frequent-letter
collapse). Frozen at `8328b9a` / `1412767`.

**Control (step 4, run).** Positive 0.986 PASS. Primary f. 539-shaped 0.093 FAIL. The ladder passes
at 1,400 tokens and fails at 700. Merging passes only at 40 signs. The target was not run (frozen rule).
Wall named in `NEXT.md`.

**Outside checks found (breach research).** Lasry 2022 on f. 555: 858 symbols / 86 signs; it does not
mention f. 539; the key is an image only. There is no published Joyeuse–Villars key. Aubery,
*Histoire du cardinal duc de Joyeuse* (1654, Gallica bpt6k856018v), prints Joyeuse letters and was
not searched. The clear frame shows Villars wrote to Joyeuse in cipher (H7). Details in
`sources/breach-research-2026-10-01.md`.
