# f62-A notes (blind transcription of f. 62 ff., guide v2.3)

Reader A, 11 screenshots `f62_s01.png` .. `f62_s11.png`. Blind to the key; no other repo file opened; no network.

## Method and budget (read this first)
- Strips of at most 3 lines were cut at native resolution with ImageMagick, **full width** (about 1450-1570 px), not in
  left/right halves with 300 px overlap as the brief asked. I did this to stay within about 120 views. Display was 1:1,
  so no resolution was lost, but halves were not used. Strip folder: `/tmp/claude-501/f62A/` (`c_<image>_<n>.png`).
- Pass 1: left to right, 51 strip views + 1 full-image view of s01 + 2 extra short crops (s02 bottom, s04 gap, s11 gap).
- Pass 2 (guide §6): every strip viewed again, images in reverse order (s11 to s01), each line re-read right to left
  and compared with pass 1. About 49 views. Total about 105. The second pass was completed for all strips.
- Changes made in pass 2 (all small): s11 `49` split to `4 9`, acute dropped from `15.`; s10 `32+` to `34+?`; s09 line 1 got
  `<bar>` on the `12<cross>`; s07 `22+` to `24+`, `14+<cross>` to `14 4+<cross>`, line 12 end `21 4 2<cut>`; s08 `rom` to
  `xom<bar>?`; s05 `224?` to `22+?`; s04 `224?` to `22+?` and `6.<bar>`; s03 `61?` to `6+?`, second `12 4` to `124?`;
  s02 open-paren flourish and `Ra<bar>?` added; s01 `10<v>` to `10<acute>?`.
  Most `?` marks are on signs where pass 1 and pass 2 disagreed or the shape stayed ambiguous.

## Overlaps (transcribed once, in the earlier image)
- s02 starts with 2 lines that are the last 2 lines of s01 (`xom 21. 7p...`, `10 / 28 67 ...`). Not repeated.
- s04 starts with 4 lines that are the last 4 lines of s03 (`10 23+ 6 8 Rom...`, `14 17p...`, `23+ 86...`, `4 24. 6. ... nec`).
  The s04 view of the 4th was clearer, so the s03 copy of that line uses the s04 reading (initial `4<hat>`).
- s06 starts with 3 lines that are the last 3 lines of s05.
- s08 starts with 3 lines that are the last 3 lines of s07 (re-read there; one extra `2<cut>` at the end of the `qual` line).
- s10 starts with 2 lines that are the last 2 lines of s09.
- s03 and s05, s07, s09, s11: no overlap seen with the previous image (s03 top 0-97 px and s05 top 0-171 px blank or margin).

## Conventions I had to choose
- Clear-looking words inside cipher lines written `[[de]]`, `[[qual]]`, `[[qua]]`. `quam` left outside brackets (could be code).
- Letter groups written as one token: `xom`, `Rom`, `Ram`, `Rum`, `xal`, `yum`, `bul`, `dul`, `sel`, `sem`, `tem`, `tum`, `yuc`,
  `cem`, `xem`, `xul`, `Pam`, `Jim`, `Ham`, `Bam`, `Zim`, `mil`, `mo`, `ril`, `til`, `pil`, `nec`, `pol`, `gil`, `gi`, `bum`, `dom`, `Tam`, `Si`, `re`, `le`, `ho`, `quam`.
- `<sign:dot slash dot>` is a small `. / .` flourish ending a paragraph (6 times), once `<sign:dash slash dot>` (end of s08).
- Stray dots between signs (a dot after a hat, after a cross) were not written as marks.
- Digit `9` written like a `g` is written `9`. `6` with a hook is `6p`. Digit `1`+`4` written like `h`: I wrote `14` or `14+` mostly;
  only one case `ho?` (s07 line 1) where an h-shape is plausible; this is the h letter-form question of guide section 9.
- `T a?`: a sign like `Ja`/`Ta` appears 3 times (s01 line 4, s05 line 1, s09 line 2) and once `Ta?` (s11); could be `7 a`.

## 3+ digit runs left joined
Almost all are a number plus the curl written joined (guide section 2), many times each: `256` (about 40), `246`, `236`, `226`, `166`,
`296`, `176`, `326`, `106`, `126`, `216`, `156`, `366`, `316`, `116`, `276`, `306<under>` (2), and the same with marks above
(`166<bar>`, `296<bar>`, `236<hat>`, `246<hat>`, `246<v>`, `296<v>`, `296<hat>`, `176<v>?`, `106<v>`, `226<hat>`, `276<bar>`, `246`).
Runs that are not number+curl in shape (genuinely uncertain splitting):
`224?` (2: s03 L11, s03 L14; plus `224<bar>?` s05), `238?` (s01 L5), `660?` (s10), `324?` (s08), `121?` and `124?` x2 (s03),
`113<cross>?` (3), `133<cross>?` (2), `115<cross>?` and `115+<cross>?` (s03, s05), `118<cross>?` (s09), `100<cross>?` (s09), `166` after `4`
in s05 line 4 (`4 166`), `156` (s03, s05).
Curl uncertainty: any `6` after a number could be a free 6 token; I followed the guide and joined when touching.

## Every `?` 
95 question marks in `transcription.txt`. Find them with `grep -n '?' transcription.txt`. Groups:
- cross above, mark after uncertain or whether the cross is a cross: `8<cross>?` (6, the `6 8` sign with cross above),
  `113<cross>?`, `133<cross>?`, `115<cross>?`, `92<cross>?`, `66<cross>?`, `56<cross>?`, `51<cross>?`, `0<cross>?` (3, an `o`-like sign with cross above), `4<cross>?`, `7<cross>?`.
- bar above uncertain (could be a pen flourish): `10<bar>?` (3), `6<bar>?`, `Ra<bar>?`, `xom<bar>?`, `sem<bar>?`, `re<bar>?`, `le<bar>?`, `pol<bar>?`, `gi<bar>?`, `8p<bar>?`, `7+<bar>?`, `17.<bar>?`, `22.<bar>?`, `23.<bar>?`, `29.<bar>?`.
- acute / v: `10<acute>?` (3), `4<acute>?`, `67<v>?`, `24+<v>?`, `176<v>?`.
- digit identity: `22+?`/`224?`, `34+?`, `324?`, `238?`, `660?`, `121?`/`124?`, `6+?`, `66?`, `16+?`, `4+?`, `4?`, `6?`, `a?`, `r?`, `Si?`, `ho?`, `Ta?`, `T a?`, `22<dot>?`, `22<2dot> 4?`.
- Splitting: `14 4+<cross>?` (s07), `4. 6 12<hat> 4+?` (s09), `12.?` (s06).

## `<sign:...>` list
`<sign:blot>` (s02, ink blot after `20p<v>`); `<sign:tall curl with dot below>` (s01 line 10, tall hooked sign with a dot under it);
`<sign:close paren>` and `<sign:open paren>` (s02: a `)` after `gil`, and a large curved stroke `(` before `236<hat>`, perhaps a long flourish);
`<sign:tilde above>` (s11, a squiggle above `15`); `<sign:dot slash dot>` x6; `<sign:dash slash dot>` x1.

## `<under>`
`24.<under>?` (s01 line 14), `35+<under>` (s06), `30.<under>` (s02 and s03), `306<under>` x2 (s05, s11).
Looked for underlines on all numbers in the 30s; `35.<bar>`, `31.`, `32.`, `36+`, `34+` carry none that I could see.

## Image problems and other remarks
- Right edge cuts lines in s02-s11; those lines end `<cut>`. Marks above at a strip top can be partly clipped.
- s01 top: `El Rey` header and a cross; initial `J` flourish; page number 62 top right.
- s02, between lines 5 and 6: small interlinear writing `256 17p` with two small marks (`11`) sits above and below `21. 55`; it is not in the line
  transcription (a correction or insertion). Not transcribed as tokens.
- s11 ends with the clear date line and the royal signature (`Yo el Rey`, flourish). Date read `xxvij. de Junio. M.D. lxxviij.`, the `l`
  uncertain (could be `c`).
- Some lines are short and end with `. / .`: paragraph ends. Paragraph starts: after s02 line 6 gap, s04 line 1/2 (`21. 10 34+`), s07 L5/L6, s08 end, s09 start, s10 L3 / L4.
- The cipher line count: 120 pure cipher lines plus 2 mixed (clear plus cipher) lines.
