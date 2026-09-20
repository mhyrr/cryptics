# NEXT — handoff for the next session

**Last session:** 2026-09-20. Experiments 12 to 15. E1 and E2 untouched.
**Where it stopped:** the seed half of the construction is supported with
controls; the interior half has a description (vowel/consonant filler) and no
rule for the letter. The handoff's E3 was redirected; read why below.

## The picture now

1. Caption subject, looked up as a German headword in the 1595/1596
   dictionary, gives the seed word (top row) from the printed Hebrew
   transliterations. H7, H17 supported. Experiments 12, 14.
2. Symmetry (transpose plus half-turn) gives the borders. Scored against
   Dehn's German-based readings: 83 of 90. H4 supported. Experiment 13.
3. The interior alternates vowel and consonant down from the seed (79 % on
   unseen cells). The letter inside that class is at 32 % against a 25 %
   baseline. Dictionary words do not sit on interior rows, with or without
   the caption. H16 supported; H12, H14, H15 weakened. Experiments 12 to 14.
4. The spirit names of Book II chapter 19 share rows with the squares, seeds
   and interiors alike. They do not fill blanks. H18. Experiment 15.

## What "solved" means here

Decide this before working, and judge every step against it (AGENTS.md rule 4).
The dive ends in one of two states. Both are finished results.

- **A. Generator recovered.** A frozen procedure takes a caption and returns
  the whole square, and it beats the class baseline on interior letters of a
  witness it has not seen. The bar: interior letter accuracy well above the
  32 % reached so far, on Warburg squares read after the freeze.
- **B. Construction characterized, wall named.** Seeds from the dictionary,
  borders from symmetry, interiors free pronounceable filler. The evidence
  needed: the seed rate raised from a floor to an estimate with its residue
  explained, per-square caption alignment, and a test showing interior letters
  carry no recoverable rule (item 4). Then blank interiors come only from
  collating German witnesses, and the deliverable is that collation plan plus
  the catalog entry re-scored.

Current evidence favours B. Do not assume it. Item 4 is the fork.

## Order of work to the end

1. Item 4 first (interior-letter freedom). It is cheap, runs on data already
   local, and decides between A and B. Freeze each test and its control
   before running. Include a per-orbit entropy estimate so "free" has a number.
2. Item 1 (Greek and Latin glosses, OCR gaps). Closes the seed half.
3. Items 2 and 3 (German captions per square; image-read the hits).
4. Item 5 (Warburg squares) last, once, with every model frozen. It is the
   only cheap unseen witness left. Do not spend it on development.
5. Close: write the construction account in `canon.md`, move hypotheses,
   re-score `catalog/` entry for Abramelin and regenerate `catalog/INDEX.md`,
   update TK-005, run `/session-close`.

## Tools already built (do not rebuild)

- `analysis/12-dictionary-index/`: `entries.tsv` (14,360 headword lines with
  scan locators) and `tokens.tsv` (Hebrew-adjacent OCR words). Raw hOCR is in
  `out/hocr/` on this machine, gitignored; `fetch_hocr.py fetch` restores it
  in about twelve minutes. Greek-script tokens are in the hOCR, not yet in
  the index: extend `build_index.py`, do not write a second parser.
- `analysis/14-caption-seed-test/lookup.py`: the frozen German headword
  lookup. `python3 lookup.py Wort ...` prints tier, scan and candidates.
  New spelling operations need a new experiment folder and a stated reason.
- `analysis/13-dehn-witness-test/dehn-readings.json`: 79 Dehn readings.
  `score.py` has `realign()` and `agreement()` for witness alignment.
- `analysis/15-spirit-names/spirit-names.json`: both spirit lists.
- Page images: `https://api.digitale-sammlungen.de/iiif/image/v2/<id>_<scan5>/<x,y,w,h>/full/0/default.jpg`.
  Word boxes in the hOCR give the crop region. Use Python urllib; a hook
  restricts curl.

## Pitfalls met on 2026-09-20

- The cached page `sources/cache/e2/mathers.html` is gitignored. If it is
  missing, refetch the Peterson URL and compare sha256 with
  `dehn-readings.json` before trusting any reparse.
- In the dictionary the Greek gloss often comes before the Hebrew. A harvest
  that stops at the first Greek word misses most transliterations.
- OCR prints long s as f. Match with f and s merged on the dictionary side.
- Dehn, Mathers and the Mathers label list use three different orders inside
  chapter 5. Align by visible letters or by meaning, never by number.
- Subagents: Opus, no nested agents, no web search budget assumptions.
  Nominators must see labels only. The main thread is exposed and must not
  nominate.

## Do first

1. **Raise the seed count from a floor to an estimate.** 56 of 232 top rows
   match the OCR vocabulary; 176 do not. Sort the misses: OCR gaps (check the
   entry image for a caption-nominated headword), Greek glosses (OIKETIS,
   PROXONOS, YPARCHOS look Greek; the dictionary prints Greek in Greek type,
   so romanize that column and rerun experiment 12's row test), Latin glosses,
   and true residue. Freeze the romanization before looking at hits.
2. **Per-square caption test with German captions.** Experiment 14 used
   English labels and scored by chapter. The Warburg print
   (`sources/warburg-1853.pdf`) has the German captions. Transcribe captions
   only, keep E2's crop discipline, reuse `lookup.py` unchanged, and score
   label-to-square alignment. Chapter 5 is development data.
3. **Read the 21 experiment 14 hits on the page images.** Two are done
   (`sources/caption-seed/`). Locators are in experiment 14 `lookups.json`.
4. **Attack the second clause of H16.** Is the interior letter free? Tests
   that could refute it: per-chapter or per-prince letter preferences; reuse of
   seed letters (39 % of interior letters occur in the top row; compute the
   chance rate); the AREPO pattern in row two; agreement between witnesses.
   If Mathers and Dehn disagree more in interiors than on seeds after
   controlling for position, copyists had nothing to correct interiors against.
   Current raw rates: top row 28 of 298, interior 71 of 563.
5. **Third witness.** The Warburg print's square letters are unread except
   chapter 4's moon and water rows. Freeze any new interior model first, then
   transcribe and score. This is the last cheap blind set.

## Named limit

The wall is the interior letter. Nothing tested predicts it much better than
class frequency. If item 4 finds no structure, the honest result is: seeds
from the dictionary, borders from symmetry, interiors chosen freely for
pronounceability, and blank interiors recoverable only by collation of the
German witnesses (Dehn, Kollatsch, Dresden, Wolfenbüttel).

## Exposure

Mathers: fully exposed. Dehn readings for chapters 1 to 14 (all that Peterson
prints): exposed on 2026-09-20; 5/1 and part of the reading beside 5/2 before
the experiment 13 freeze. Experiment 14 nominators saw labels only. The main
thread has seen which top rows match the dictionary. Warburg chapter-5 square
letters: still unread. No untouched-manuscript score exists.

## Earlier queue, still open

Mathers print audit, ten excluded layouts, label 25/4 among chapter 24, frame
disagreements, Dresden N 111 and HAB access, an earlier dictionary edition for
H7's edition-specific clause. TK-005 remains open.
