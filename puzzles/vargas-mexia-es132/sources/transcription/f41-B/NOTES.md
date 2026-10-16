# f41-B blind transcription: notes

Blind to the key; guide CIPHER3-GUIDE.md v2.3 only. Seven screenshots `f41_s01` ... `f41_s07`, ~99 manuscript lines.
Line numbers below are line numbers of `transcription.txt` (comments included).

## Method and deviations (read first)
- Crops: 3-line strips cut at native resolution with ImageMagick into /tmp/claude-501/f41B/ (40 strips).
- **Deviation: full-width strips, not left/right halves.** The images are ~1500 px wide and the viewer showed them at
  native scale, so halves would not have added resolution but would have doubled the views (~160 > budget). Each strip is
  <=3 manuscript lines plus margin (lines rise to the right, so strips carry fragments of neighbouring lines).
- Pass 1: images s07 to s01 (reverse order), each strip left to right. Pass 2 (guide section 6): images s01 to s07,
  every strip re-viewed in full, each line re-read right to left against pass 1. About 55 views in pass 1 (incl.
  overview views and 2 zooms of s07 at 150-200%, used only to learn sign shapes) and 40 in pass 2.
- Pass 2 changes: s01 line 5 end re-read and marked `?`; bar added over `36+` (twice); acute over `8.` (twice); underline
  made certain on `33+` (f41_s03/s04 shared line); `23.<v>` on one s04 line; `71 /` in s05 line 2; `S<v>?`; `co d` unified.
- The right edge of s03 and s04 runs into a dark fold/page edge; lines there end with `<cut>` (s01 and s07 lines also
  `<cut>` where the right margin clips the last sign).
- Output header order is page order; lines inside an overlap are credited to the EARLIER image.

## Overlaps
- s01 / s02: the first 4 lines of s02 repeat the last 4 lines of s01 (read twice, text agrees); transcribed once under s01.
- s03 / s04: the first 5 lines of s04 repeat the last 5 lines of s03 (agree); transcribed once under s03. s04 line 6 is only
  clipped at the bottom of s03 and is transcribed under s04. A 20th line of s03 is a clipped fragment, not transcribed.
- s05 / s06: the first 2 lines of s06 repeat the last 2 lines of s05 (agree); transcribed once under s05.
- Page label "41" at the top of s01 and "42" at the top of s05 (s05 begins a new leaf; the fold edge of s04 is the end of the previous one).
- s01 carries "El Rey" and the salutation (clear). s07 ends with the date line (clear text; the day numeral
  `xxx?` is unclear: three x-like strokes, the last crossed) and a signature (not read: `[[<signature: Yo el Rey>]]` is a guess at the form).
  The year 1578 is underlined in the manuscript.

## Conventions I had to invent (shapes only, no values)
The guide does not cover these; I used them consistently. They are readings of shape, not of value.
- `u.` : a `u`-shaped sign with a dot after (very frequent). Not written `12.`; could be 12 per guide section 7.
- `23.` / `23+` : a v-shaped stroke plus a z-shaped stroke (e.g. "vz."), read as two digits. It might be 12, 13 or 23. Treated as a
  single convention rather than flagged `?` each time (it occurs ~60 times).
- `3` : any z-with-tail sign (digit 3 or z-shaped 2); `Z` : a plain capital-Z-like letter; `<sign:Z-with-large-tail>` : the large Z
  with a long looping tail that follows `20. 22.` (5 times).
- `co` : the omega/"ω"-shaped letter group; `d` : a small loop letter after `co`; `yp` : a long-tailed y with a hook;
  `r`, `n`, `S` as letter forms; `m6<v>` for an "M"-like letter plus 6.
- `24:` : 24 with two dots after (a colon); not in the guide's mark table, kept as `:`.
- `<v>` for a tilde-like or small curved mark above; `<2dot>` for two dots above; `~`-over-letters also written `<v>`.
- `166`, `176`, `246`, `256`, etc.: digit + curl joined (guide curl rule). I did not write a separate `6` for any curl.

## 3+ digit runs left joined (all are digit(s) + curl or hook-curl; counts in transcription)
256 (36x), 176 (16), 246 (14), 166 (13), 161 (13), 231 (12), 226 (12), 236 (10), 326 (5), plus 156 (2), 336<under>, 251, 206?, 201,
181, 171, 165, 113?<cross>. "161" and "231" are sometimes a curl and sometimes a real "1"; I could not tell. "166"/"161" are
the least certain; "231" may be `23`+curl.

## Every `?` (transcription.txt line numbers)
5 8 14 33 41 42 43 58 59 62 64 65 68 72 73 86 88 89 93 94 99 100 102 103 107 109 110. Total count in file: 33 (includes `?` marks
inside `<sign:..>`/`[[ ]]`: the signature and date). Main cases: first sign of s07 line 1 ending (`4?`), `06.?`, `165 S?`, `5p<v>?`,
`20p<v>6?`, `113?<cross>`, `24+<sign:...>` etc. All joined-curl doubts are marked.

## Every `<sign:...>`
- `<sign:ink-blots>` (s02, line near lines 31-32): a cluster of ink blots covering ~2 signs.
- `<sign:tall-vertical-stroke>` (s03 line 2): a thin tall stroke between `17p` and `u.`, not a virgula.
- `<sign:z-above>` x3: a small z-like mark above a sign (one in s06 line 14 `24+`, one in s02 over `24p`, one in s05 over `6.`).
- `<sign:Z-with-large-tail>` x5.

## Every `<under>`
`336<under>` (s01), `33+<under>` (s01 line 13 and s02, s03/s04 shared line, s02 line "28 co 236"), underlines on numbers in the 30s:
transcription.txt lines 9, 16, 27, 54. Others are `?`-free; the `<under>` after `33+` is visible in every pass.

## Image problems
- Lines rise to the right: top margin was widened to avoid cutting right-hand ink.
- s02 has heavy ink blotting at lines 5-6 of the image (partially illegible).
- Right-edge fold in s03 and s04 clips the last sign or two of each line.
- Full resolution is marginal for hat/tilde/bar marks above signs; I expect dropped or confused marks above (especially `<v>` vs `<hat>`).
- No strip failed to display; no strip transcribed unseen. Second pass was complete.
