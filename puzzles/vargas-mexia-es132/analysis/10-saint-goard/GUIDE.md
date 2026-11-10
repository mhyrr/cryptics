# Reader guide: Saint-Goard to Henri III, Madrid, 23 December 1579

BnF Français 16106, ff. 363r–366v (Gallica `btv1b90096628`, views 373–377). About 240 lines of
cipher with no contemporary decipherment on the page. Plaintext language: French of 1579,
phonetic and unstandardised spelling (`recepvoir`, `fet` for `fait`, `ce` for `se`, `an` for `en`).

## The cipher

"Longlée's cipher", inherited from Saint-Goard. A homophonic substitution: each plaintext letter has
one to four symbols; there are signs for doubled letters (cc, ff, pp, rr, ss), about twenty word
signs, and nulls. Words are not separated. i/j share signs; u/v share signs.

Key sources, both images; look at them before reading and keep them open:

- `sources/cache/fr16106/mousset1912-p-lviii.jpg` (letters) and `mousset1912-p-lix.jpg` (word
  signs): A. Mousset, *Dépêches diplomatiques de M. de Longlée* (1912), pp. lviii–lix. SCHOLARLY.
- `sources/cache/cryptiana-henryiii/henryiii_Longlee1.png`: S. Tomokiyo's reconstruction, which
  also shows the **nulls** (two right-hand columns) and a few extra word signs. SECONDARY.

Both keys were built from the 1582–90 dispatches. The 1579 letter may use signs they lack. A sign
not in either key is written `?` on first pass; if the context fixes its value, report it in the
"new or doubtful signs" list with the line numbers where it occurs. Do not silently assign it.

A worked sample (f. 363v, line 2), read by the main thread, to calibrate:
`[Roi] d e [Portugal] e t l a n o · b l e s e l e v e u l e n t a i n s i …`
→ *le Roi de Portugal et la noblesse le veulent ainsi*.

## Strips

`sources/cache/fr16106/strips/<page>-<nn>.jpg`, nine per page, top to bottom, each overlapping the
next by about one line and a half. A line cut by a strip edge is read from the strip that shows
it whole. Number lines per page from the first cipher line, L01 upward. Heavy show-through from
the other side of the leaf appears as faint mirrored writing: ignore it. The outer 3–5% of a strip
may show the facing page; ignore that too.

## What to write

One file per page, `analysis/10-saint-goard/reader<X>/<page>.txt`, one row per cipher line:

```
L07 | d e [Portugal] e t l a n o · b l e s e ? e … | de Portugal et la noblesse [l?]e …
```

- Column 2: one token per glyph, in order, separated by spaces. A letter; `·` for a null;
  `[Roi]` etc. for a word sign; `ss`, `rr` for a doubled-letter sign; `?` for a glyph you cannot
  identify; `(a/o)` when two values are possible.
- Column 3: the French you read from column 2, with word breaks. Put `[…]` round anything supplied
  by sense and not by the glyphs.
- Pass 1: glyph by glyph, without forcing sense. Pass 2: reread each strip with the French in mind
  and revisit every `?` and every word that makes no sense; correct column 2 only where the glyph
  on the image supports it. Keep a wrong-looking glyph as read if the image is clear.
- Clear-text lines (ordinary French script) are transcribed in column 3 with `CLEAR` in column 2.

End the file with: `## New or doubtful signs` (sign described in words, proposed value, lines) and
`## Summary` (five lines of English on what the page says; names of persons and places).

Do not translate or interpret beyond that. Do not consult any other reader's files.

## Reader B: half-width strips

Reader B uses `sources/cache/fr16106/halves/<page>-<nn><a|b>.jpg` (cut by `crop_half.py`): the same nine bands,
each split into a left half `a` and a right half `b` that overlap by about three glyphs, at native resolution
with the show-through washed out. Read `a` then `b` for each band and join each line across the overlap;
do not double-count the overlapping glyphs. Everything else in this guide applies. F. 366v holds no cipher
(its marks are show-through from 366r) and is not read.

## Reader C: show-through subtracted

Readers A and B lost long stretches to show-through: the other side of each leaf prints through almost as dark
as the text. `unbleed.py` subtracts the mirrored image of the other side. Reader C uses
`sources/cache/fr16106/unbleed/<page>-<nn><a|b>.jpg` (same nine bands, left half `a`, right half `b`, overlapping
by about 12% of the page width). In these images the real text is dark; the removed show-through is left as a
pale or white ghost, sometimes with a thin grey fringe. Read only the dark strokes. Where a white ghost cuts a
glyph, look at the same band in `halves/` to see the untouched strokes. Several pages are indented: the text does
not start at the left edge, and whatever ghost lies in that margin is not text.

Sign values reported independently by two or more earlier readers of this letter (check them, do not assume):
- "3 with a p-like tail" (Tomokiyo draws it among the nulls as "2p"/"ze") = **i/j** here.
- "=" (two short bars, Mousset's ⊐) = u/v. A small crossed, star-like sign also reads u/v in most places.
- Nulls: the hook-and-8 sign ("18"), the swash "ep"/"ef" loop, "ge"/"ze", and often the "δb" double loop.
- Y-fork with hooked foot = p; the same with a crossbar = m; plain S-shape = m; U-box = f.
- Tall F = pour/par; large looped L-flourish = que; ⊓ = qui; barred W = le Roi; the tall flourished 8 with a
  tilde = Portugal. "le Roi catholicque" (Philip II) and "don Anthoine" recur.
- "8" alone is doubtful (cc, par, or m).
