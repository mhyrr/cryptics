# 10 — Saint-Goard's file, BnF fr. 16106 (1579)

**Question.** What does the French ambassador's own file say about the matters es. 132 leaves open: where he got
his knowledge of Madrid business in 1579 (H18), and what he reported to Henri III?

**Correction (2026-11-10, later).** The letter is not undeciphered. Its contemporary decipherment survives at
ff. 208r–209v of the same volume under the wrong date "23 avril 1579" (`sources/fr16106-ff208-209-decipherment.md`).
It confirms the cipher readings below passage by passage and supplies the unread half. What follows is kept as run.

**Status (2026-11-10).** Volume indexed from f. 189 to the end. One long cipher letter with no contemporary
decipherment found and partly read: Saint-Goard to Henri III, Madrid, 23 December 1579, ff. 363r–366r.

## What a reading would have to do (written before the readers ran)
One key (Longlée's cipher, Mousset 1912 pp. lviii–lix) reads the whole letter as continuous French of 1579;
independent readers agree; names and facts read from the cipher match documents outside the letter.

## Files
- `index-*.tsv`: one row per spread, views 196–391 (three Opus readers; dates as written, cipher line counts).
- `GUIDE.md`: reader protocol. `crop.py`, `crop_half.py`: strips. `unbleed.py`: show-through subtraction.
- `readerA/` (full-width strips), `readerB/` (half strips), `readerC/` (half strips after `unbleed.py`): one file
  per page, one row per cipher line: glyph tokens, then French. Opus agents, one page each, isolated from each other.
- `compare.py` → `results/agreement.tsv`, `results/aligned-<page>-<pair>.txt`.
- `reading-1579-12-23.md`: the working text, with what the main thread checked on the images.

## Results
- **Agreement** (`results/agreement.tsv`; share of glyph tokens with the same value after alignment). Best pair per
  page: 363r 0.68, 363v 0.70, 364r 0.82, 364v 0.71, 365r 0.66, 365v 0.41, 366r 0.93. The es. 132 readers reached
  0.80–0.97. Agreement is not accuracy.
- **Show-through was the main obstacle.** After `unbleed.py`, unknown glyphs fell from 4–52% (A, B) to 1–17% (C),
  and ff. 363r, 363v and 364r read as continuous French for the first time. Registration scores 0.51–0.68 per page.
- **Read as continuous French:** f. 363r (cipher part), f. 363v ll. 1–7 and 17–37, f. 364r, f. 366r. **Fragments
  only:** f. 364v, f. 365r, f. 365v, f. 363v ll. 8–16.
- **Checked on the image by the main thread, glyph by glyph:** f. 363v ll. 1–2 and 26–28; f. 364r ll. 2–7.
- **External check passed:** the cipher names "don Anthoine de Castre, seigneur de Cascais" as the writer of
  enclosed letters. BnF Espagnol 336 ff. 72–78 holds a letter of António de Castro, Cascais, 25 Nov 1579, to
  Saint-Goard, with a French translation and a copy for the King of France (Morel-Fatio 1892, no. 183; listed in
  `sources/bnf-survey-2026-10-15.md` before this experiment). No reader was told of it.

## Limits
- Readers are language models reading microfilm scans. No paleographer has checked any line.
- Reader C was given sign values that A and B had reported, including "don Anthoine" and "le Roi catholicque" as
  recurring words. "Castre", "Cascais", "Pierre Dor", "Doria", "Calis" and "Port Sainte Marie" were not given.
- `unbleed.py` alters the image. Lines read from it are checked against the untouched strip only where the main
  thread did so (listed above).
- About half the letter is still unread. The 1574 cipher letters (ff. 191–199) have their own decipherment sheets
  and were not read. The Spanish papers (ff. 210–358, 369–376) were indexed, not transcribed.

## Run
`uv run --with pillow python3 crop.py`; `uv run --with pillow python3 crop_half.py`;
`uv run --with pillow --with numpy python3 unbleed.py 363v 374 L 373 R` (page, view, side, other view, other side);
`python3 compare.py`. Images are fetched through a browser session (Gallica refuses scripts) into
`sources/cache/fr16106/full/`, which is not in git.
