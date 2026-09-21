# NEXT — handoff for the next session

**Last session:** 2026-09-20, evening. Experiments 16 to 20 complete.
**Where it stopped:** end state B. The construction is characterized, the
wall is named, the Warburg print has been read once. The cheap unseen
witnesses are spent. TK-005 can close once Greg accepts the account.

## What the dive concludes

The construction account is at the top of `canon.md`. In one breath: caption
subject, looked up in the 1595/1596 dictionary, gives the seed; transpose plus
half-turn gives the borders; interiors alternate vowel and consonant, and
nothing tested predicts the letter (2.9 bits per symmetry orbit; best frozen
model 32 % on Dehn, 23 % on the Warburg print).

Say it this way and no stronger: no rule was recovered. That the letters were
freely chosen is unrefuted and cannot be proven.

## The wall

Blank or disputed interior letters cannot be computed on present evidence.
They can only be collated. What would breach the wall:

1. **Images of a German manuscript with full squares.** Dresden N 111 (SLUB
   viewer sits behind a JavaScript challenge; a browser session or a written
   request to SLUB should get it), Dresden N 161, Wolfenbüttel 47.13 Aug. 4°
   and 10.1 b Aug. 2° (HAB offers digitization on request; that costs money,
   so it is Greg's call).
2. **Dehn's edition in full.** Peterson prints Dehn readings for chapters 1
   to 14 only. The book has all 30.
3. **Kollatsch's 257-square compilation**, already local
   (`sources/buchstabenquadrate.pdf`), used with its conjectures marked.

The deliverable behind the wall is a per-cell collation table: witness,
reading, image locator, and editorial conjecture kept apart. The frozen models
then serve as checks (border symmetry, interior class), never as fills.

## One open flag on experiment 20

Two legibility gates were written before the read. This session's frozen gate
passes (97.8 %). A parallel session's stricter gate (`score_checked.py`) fails
(38.6 %) because it counts the print's uneven row lists as unread; a post hoc
check shows 95.8 % reader agreement on those rows. This session ran `score.py`
first, before it knew the parallel handoff said to use `score_checked.py`
only. Both outcomes are in the experiment README. Greg should decide whether
the Warburg scores are cited as corroboration or set aside; end state B holds
either way on experiments 13 and 16.

## Small things still open

- H22: the itacist Greek reading was found post hoc. A blind repeat needs a
  witness not yet used; the Warburg top rows are now exposed.
- The aspirate reduction (sch S, ch C, bh B, th T) is an observation on 21
  words; a test would apply it to all image-read transliterations.
- Seed coverage: OCR holds about half of the sampled printed
  transliterations. A full image read of nominated entries would turn the
  exploratory 45 % into a count. It is cost, not difficulty.
- Earlier queue, unchanged: Mathers print audit, ten excluded layouts, label
  25/4, earlier dictionary edition for H7's edition-specific clause.

## Tools (do not rebuild)

- `analysis/12-dictionary-index/`: OCR index; hOCR restores with
  `fetch_hocr.py fetch`. `17-greek-latin-seeds/` adds Greek, Latin and
  Hebrew-line vocabularies.
- `analysis/14-caption-seed-test/lookup.py`: frozen German lookup.
- `analysis/18-german-captions/`: `bands.py`, `mask_pages.py`, layout labels,
  239 German captions, nominations. Masked pages regenerate into `out/`.
- `analysis/20-warburg-witness/`: `readings-A.json`, `readings-B.json`,
  `warburg-squares.json` (agreed cells; `?` where readers differ).
- Several experiment folders have a `run.py` or `score.py`. Load siblings by
  path with `importlib`, as `20-warburg-witness/score.py` does.

## Pitfalls met this session

- Opus subagents died three times on the account spend limit. Tell readers to
  save after every page and to resume from their own file.
- A parallel session committed to the same files mid-session. Run `git log`
  before writing a README or a handoff, and read what is there.
- Image readers drift toward using symmetry to settle a letter. Forbid it in
  the brief.

## Exposure

Everything local is now exposed to the main thread: Mathers, Dehn chapters 1
to 14, and the Warburg print. No blind witness remains on disk.
