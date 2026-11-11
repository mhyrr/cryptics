# Reader brief: three cipher letters of 7 Feb 1580, BnF fr. 16107

Read `analysis/10-saint-goard/GUIDE.md` in full first: the cipher, the token format, the two passes, and the "Reader C"
section. Everything there applies, with these changes.

- Images: `sources/cache/fr16107/unbleed/<page>-<nn><a|b>.jpg`, nine bands per page (01–09, top to bottom), left half
  `a`, right half `b`, overlapping by about 12% of the page width. Show-through is already subtracted and is faint in
  this volume: read the dark strokes, ignore white or pale ghosts. Untouched pages, if a glyph is cut by a ghost:
  `sources/cache/fr16107/full/vNN.jpg` (8756 px wide; never Read one directly, crop first with pillow).
- Key images as in the guide (`sources/cache/fr16106/mousset1912-p-lviii.jpg`, `-lix.jpg`, and Tomokiyo's PNG).
- Sign values confirmed on this volume by a known-plaintext test (`analysis/12-sweep-fr16107/join-7feb.md`): curl with
  a tail = s; linked `oo` = d; `∂` (d with a flourish) = z; the `δb` double loop = null; "18" (hook-and-8) = null.
- Letters and pages (page = folio side; some pages begin or end in ordinary script, transcribe that as CLEAR):
  - **R**, to the Queen Mother: 59v (cipher starts about 65% down), 60r, 60v, 61r (cipher ends about 65% down).
  - **A**, to the King: 40v (cipher starts low on the page, after "…donner mauvaise reputation a ses subjectz"),
    41r, 41v, 42r, 42v, 43r (cipher ends about half-way down).
  - **B**, to the King: 44r (cipher starts in line 1 after "…loisir de fere ceste"), 44v, 45r, 45v, 46r, 46v,
    47r (cipher ends about 45% down).
- Output: `analysis/13-feb7-letters/reader<X>/<page>.txt`, format as in the guide, ending with `## New or doubtful
  signs` and `## Summary` (five lines of English; persons and places named). Give English beside any French you quote
  in your report.
- Do not consult the other reader's directory, `analysis/10-saint-goard/reader*/`, or any decipherment in `sources/`.
  No letter here has a known decipherment; do not force sense. `?` is a full answer for a glyph.
