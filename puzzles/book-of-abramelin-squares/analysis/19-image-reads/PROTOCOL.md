# 19 — Read the dictionary entries on the page. Frozen before any crop is viewed

Date: 2026-09-20.

## Two questions

1. Experiment 14 found 21 seed hits through OCR. Do the printed entries carry
   those transliterations? Two were read already (Löwe, Schnee).
2. How much does the OCR harvest miss? Experiment 17 needs this to call part
   of the seed residue an OCR gap.

## Worklist (`make_worklist.py`, seed 20260920)

- **Hits.** For every experiment 14 skeleton hit, every looked-up entry of the
  same chapter whose OCR candidates match the row at the skeleton tier.
- **Gap sample.** From experiment 14 lookups with tier `exact_key` or
  `frame_stripped`, the distinct entries that are in no hit; 30 drawn at
  random. The sample is drawn before any image is fetched.
- Crop: the entry's column, from 30 px above the headword line to 650 px below
  it, native resolution, BSB IIIF image API. The column gutter comes from
  experiment 12's `build_index.gutter`.

## Reading

Opus subagents, no nested agents. A reader sees dictionary crops and the OCR
headword only. It never sees a square, a caption or the OCR's transliteration
list. It transcribes every Latin-letter transliteration printed beside Hebrew
type in the named entry, in order, with long s written as s, and flags doubt.
The main thread does not read the crops before the readers' files exist.

## Scoring (`score.py`)

- Hits: a hit is confirmed when the image reading contains a word with the
  same skeleton as the square's top row (experiment 14's `skeleton`).
- OCR recall: over the gap sample, the share of image-read transliterations
  that experiment 12 harvested for the same entry (normalised, f/s merged).
- New seeds: image-read words the OCR missed that match a top row of the
  label's chapter at the skeleton tier. Control: the same words against the
  top rows of every other chapter, as a rate per chapter.
