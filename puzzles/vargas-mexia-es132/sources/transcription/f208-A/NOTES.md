# f208-A: blind transcription notes (ff. 208-210, letter of 4 June 1579)

Reader worked from the six page images in `sources/cache/pages/exp07/` and from CIPHER3-GUIDE.md v2.2 only. No key, no
other transcription, no network. No decoding attempted.

## Extent
- Letter begins f. 208r (the King's "Yo el Rey" head, salutation, a clear opening paragraph in Spanish, then cipher from
  the 4th text line) and ends f. 209v (last cipher line, then clear "de Aceca a quatro de / Junio 1579", the King's
  signature, and the secretary's countersignature at lower right).
- f. 208r: 3 clear lines + 22 cipher lines. f. 208v: 27 cipher lines. f. 209r: 25 cipher lines. f. 209v: 7 cipher lines,
  then date and two signatures. Total 81 cipher lines.
- f. 210r: blank leaf, foliation "210" only; faint mirror show-through of the address on 210v. Not transcribed.
- f. 210v: address leaf, text rotated 90 degrees (reads when turned counter-clockwise): "Por el Rey" (small cross above
  "el") and below it "Juan de Vargas Mexia" with a large opening flourish (A-shaped) and a long closing stroke. Transcribed
  in `[[ ]]` under its own header. No docket, no other note.
- Clear text read: "Yo el Rey" (the head of 208r is written as a cross-barred flourish over "el Rey"; "Yo" is a small looped
  stroke, so I wrote `[[+ el Rey]]` at the head of f. 208r). On f. 209v the King's signature is `[[Yo el Rey]]`: "Yo" with a heavy
  ink blot, then a large flourished "el Rey" with a long descending tail (overlaid by show-through of 210v).
- **Countersignature as I read it: "Ant.º Pz"** (the abbreviation "Ant." followed by a P-loop with a z/3 form;
  I take it to be Antonio Perez, but only the shapes "Ant." + P + z are certain; large flourishes above and below).

## Passes and strip counts
- Strips: for each page, 3-line strips (4 lines visible in some because of line overlap), each a left half and a right half,
  1500-1550 px wide, native resolution, overlap between halves 150-420 px (the guide asks for ~300; on f. 208r the overlap is
  ~150 px, on f. 209r ~420 px, on ff. 208v and 209v ~160 px). Strip files: `/tmp/claude-501/t208/<page>/tNNL|R.jpg`.
- Pass 1 (left to right, first folio to last): 28 strips (8 on 208r, 9 on 208v, 8 on 209r, 3 on 209v) = 56 half-strips,
  plus extra crops of the clear lines, signatures, address leaf and f. 210r.
- Pass 2 (last folio to first, bottom strip to top, right half before left half, each line read right to left against the
  pass-1 line): 28 strips = 56 half-strips, complete. Plus a re-read of the clear lines on 208r. The signature crops on 209v
  and the address leaf were viewed once only (no second reading needed for clear text; flourishes described, not decoded).
- What pass 2 changed (the main corrections): (a) the q-shape sign (loop top, straight tail) was first written 9 on ff. 208r-209r
  and was re-read as 4 everywhere; the g-shape (curved tail to the left) stays 9. (b) Several "7 e" / "d e" and "p e" splits
  corrected; the "25" vs "28" reading of "2s." fixed in many places; missing marks above (hat, acute, grave, bar) added on
  about 25 signs; "xxxvy" on 208r line 2 corrected to "xxvy" (one x fewer). (c) A few 3-digit joins re-split.
- Unfinished: no strip was skipped. Reading confidence is low to moderate for the whole cipher: the hand is fast, pen joins
  are everywhere, and many glyphs (the e-curl vs 6, the d-shape, the hook p, 4 vs 9, 25 vs 28, 17 vs 12 vs 7) are
  close. Treat every line as a first reader's attempt, not a settled text. The most reliable parts are the repeated frames
  that recur across lines (e.g. `d. 15+`, `21.`, `7 e`, `4<hat> 24<hat>.`, `286 9`).

## Conventions I used beyond the guide (shapes only)
- Letter forms written as letters: `d` (a loop with a back-stroke, like a script d or a mirrored 6 with a tail), `e` (a small
  open loop, appears after many numbers and after `d`, `p`, `7`, `1 5`), `m`, `n` (as in `m n y`), `L`, `y`, `p` (a free p
  with a foot), `u`, `i` (once, `i m`), `o`, `S` not used. `0<cross>` is a small round sign with a cross above it (three
  times, written `0<cross>`; one other `0` unmarked).
- `4` is the loop-top sign with a straight descender (also the H-shaped "1H"); `9` is the curved-tail g-shaped sign. The hook
  after a number is `p` joined (`24p`, `13p`, `7p`, `20p<v>`, `12p`, `6p`).
- `<zeta-like curl>`: a large initial curl like a flourished ζ or a script 3 that opens several lines, always followed by
  `u m`, `o m` or `i m`.

## 3+ digit runs left joined (each is a number plus a curl touching it, or two numbers I could not separate)
- `286` (25 times, the frequent `286`/`2 8 6` frame, with a closed 8 and a curl)
- `236` (8), `246` (5), `126` (3), `176` (2), `156` (2), `316`, `206`, `216`, `296` (1 each).
- All of these were left joined by the curl rule; none of the joins is certain. `236` is sometimes `23 6` in appearance.
- Other near-runs written split: `1 6 6`, `16 6`, `3 16`, `18 18`, `12 1`, `156` appears once as a join.

## Every `?` (69 tokens; by folio: 208r 29, 208v 22, 209r 16, 209v 2)
The `?` marks are in the transcription lines themselves. Groups:
- unsure whether a mark above exists or which mark (`<bar>?`, `<2dot>?`, `<acute>?`, `<grave>?`): about 35 places.
- unsure of the sign identity or split (`9`/`4`, `5`/`15`, `6?`, `86?`, `216?`, `27+?`, `24 e?`, `1?`): about 25 places.
- unsure whether a curl is joined: `86?`, `36?` (first reading, then re-read `86`), `246<v>?`, `76?`, `76 16?`.
- a faint or smudged stretch on f. 208r last line (ink fainter, show-through of the facing leaf): `24 e? 17+ 1?`.
- `5+?` on 209v line 2 (the leading 1 of `15+` may be missing).

## Every `<sign:...>`
- `<sign:zeta-like curl>` x6 (208r cipher lines 14, 15, 18 and 21; 208v line 9; 209v line 6; cipher lines counted from the first cipher line of each folio): a large curl, once or twice per paragraph, always before `u m`, `o m` or `i m`.
- `<sign:large initial flourish>` x2 (208r cipher line 16 start; 209r line 17 start): a big opening loop before `p e`.
- `<sign:large curl>` x1 (208r cipher line 17 start).
- `<sign:small-2-above>` x1 (209r line 1): a tiny "2" above a `9`.
- `<sign:unclear, bar above>` x1 (end of 208r cipher line 13): the last sign(s) of the line under a long bar.
- On 208r cipher lines 14-15 several tiny "2" marks hang above signs (written `<2dot>?` where I took them for dots).

## Every `<under>`
- 208r: `35+<under>` (once, in the line `... 15+ 35+ 24 6 7+ ...`).
- 208v: `34<under>.` twice (`13<hat> 34<under>.` and the start of line 2 `34<under>`), `34+<under>` once, `4<hat><under>` once,
  `5.<under>?` once (a short swash under `6 5.`, near the end of a line; may be a flourish).
- 209r: `34<under>.` once.
- 209v: `35+<under>` once.
- The underlined numbers are all in the 30s (34, 35) except the uncertain `5.` and the underlined `4<hat>`.

## Image problems
- ff. 208v and 209v: the right side of every text line is cut or shadowed by the gutter (black binding strip at about
  x = 3320 on 208v, x = 3316 on 209v). The last sign or two of each line is lost or half hidden: marked `<cut-gutter>`
  (22 lines on 208v, 6 on 209v). Some lines may continue under the gutter.
- f. 209v: show-through of the address leaf and of f. 210r writing fills the bottom half under the signatures; the King's
  signature overlaps faint mirrored strokes.
- f. 208r: a dark blot sits on one sign near the start of 209r line 3 (`6? e L`); a blot sits under the signature on 209v.
- Light grey faint ink in places on 208r (last line) and 208v (line 1 right end: `6? 1 p`) reads as show-through or faded
  ink. These lines carry `?`.
- Ink varies in weight: lines with thin pen strokes (thin 4, thin 1) are harder to tell from dots and ticks; marks above
  were the commonest source of disagreement between my two passes.
