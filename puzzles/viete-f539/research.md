# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

- **Ciphertext-only annealing on f. 539 as it stands** (H2), 2026-10-01. The matched control
  fails (median 0.093) while the positive control passes (0.986): `analysis/01-annealing/`.
  Same conclusion as Bourdeau, 2026-09-16, reached with a different transcription, solver,
  corpus and structural assumption.

---

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
