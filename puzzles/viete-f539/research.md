# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

-

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
