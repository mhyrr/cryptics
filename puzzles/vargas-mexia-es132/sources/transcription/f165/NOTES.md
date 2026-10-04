# f. 165 blind transcription notes (Guide v2.1)

## Method
Folios verified from the page images: canvas 162 right page = f. 165r (foliation "165" top right); canvas 163 left = f. 165v, right = f. 166r
(foliation "166", otherwise blank). Native region fetches (python urllib), local native crops by `sips` into `sources/cache/f165-crops/`
(r01-r17 a/b = 165r, 1500x330 px halves overlapping about 150 px; v01-v07 a/b, vV4, vS1/2, vsp, vdoc*, vperez = 165v). No upscaling. No other repo file opened.

## Passes
- Pass 1: left to right, every crop viewed at native resolution. 27 cipher lines on 165r, 12 on 165v.
- Pass 2: re-read of every line right to left against the same crops (images already in context, not re-fetched). Changes: marks above re-checked
  (several `<bar>`/`<hat>`/`<v>` added), the 2-dot above 22 (R06, R10, R16, R23), the cross above 21 (R13, R18, V10).
  I did not independently re-derive every sign. Confidence is LOW to MEDIUM; treat this as one reader's draft to align with the others.

## Layout
- 165r: header "el Rey" (flourished, with a cross above the "el") top centre, "165" top right. Line R01 begins with the Spanish address
  "Juan de Vargas Mexia", then a virgula `/`, then cipher. Small marginal marks at left (a tilde at the address line, a dot, a dash) not transcribed.
  No date or signature on the recto; the cipher runs straight onto 165v.
- 165v: 12 cipher lines (V12 short, ends with `/`), then 3 lines of clear Spanish (S01-S03) ending with the date. Cipher lines run into the gutter
  shadow; the last 1-3 signs of lines V01-V10 sit in the dark edge. V06, V08, V09 show faint grey text at the edge (marked `?<faint>`).
  V04 has three small 2s written above its first three signs (no guide shape; written `<sign:small-2-above>`).
- 166r: blank (foliation only; faint show-through).
- Spanish as seen: "A los demas puntos de vras cartas, Se procurara responder con es[...] si el despacho principal porque se despacha dierelugar a ello, y sin[...]
  gra con otro, de s. lorenes a x. de Enero 1579." Line ends are cut at the gutter ("con es", "y sin").
- Date: "de S. Lorenzo a x. de Enero 1579" (10 Jan 1579 confirmed).
- Signatures: royal signature (large, faint, flourished; shape only) below the date; secretary signature "Ant. Peres" lower right, last letters lost at the gutter.
- Margins: bottom left "dup.da" with a flourish; bottom right a sideways docket in another hand (not read).

## Token count
1014 cipher tokens (R01-R27 and V01-V12, counting `/`; Spanish excluded).

## Conventions I had to add
- `P` = the letter-form p with a long descender and bar through the stem; `p` after a base = hook mark. Hard to separate; passes may differ.
- `d` = a delta-like looped glyph (not in the guide). `m` once (R08), `l` once (V02).
- "7" stands for a glyph that looks like `H` or a 7 with a crossbar; many `17`, `7+`, `71` tokens could be a different shape.
- The digit 4 and the letter q are almost the same shape. I wrote `q` for long-descender forms and `4` for short ones; many are uncertain.

## 3+ digit runs left joined
Three-digit: `256` (many), `236`, `246`, `176`, `769`, `869`, `166`, `156`, `226`, `121`, `286`, `356`, `231`, `217`.
Four-digit: `2269`, `2869`, `2610`, `1028`, and `2610<hat>` (V06).
Lines: R02-R27 and V01-V11 contain these; I did not split any.

## Unsure curls (joined vs separate)
R02 `256 6 10`; R03 `76 86 6p`, `256 24p`; R05 `66 2 96 4`; R06 `66 10`, `66p`; R10 `156 11. 769`; R19 `1028`; R20 `236 121 286`; R24 `21 67`; V01 `356 76`; V10 `2269`.
Every curl after a 5, 7 or 8 was written joined.

## Every `?`
R01 `1?`; R02 `24+<bar>?`, `1?`; R03 `p<bar>?`, `15p<bar>?`; R08 `3?`; R10 `8?.`; R14 `18<bar>?`; V02 `l?`, `231?`; V04 `18<bar>?`; V06 `21.? 22?`; V08 and V09 `6?<faint> 2?<faint>`.

## Every `<cross>`
R13 end `21<cross>`; R18 `21<cross>`; V10 `21<cross>`. (The cross above "el" in the header is a flourish on "el Rey", not a cipher sign.)

## Wall
The hook shapes (`p` vs `P` vs `e`), 4 vs q, and the `H`/7 glyph are the main uncertainties; native crops did not settle them. A second independent reader and alignment against the duplicate letter would.
