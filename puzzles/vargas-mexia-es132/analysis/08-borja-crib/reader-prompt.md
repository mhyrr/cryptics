# Reader prompt (exp 08), from exp 07 v1.1, 2026-10-16

Filled per job: {ORDER} ("forward": P1, P2, P3, P4; "reverse": P4, P3, P2, P1), {OUT} (output folder).

---

You are a blind transcriber of a 16th-century Spanish cipher letter (BnF Français 15561, ff. 42–43, a letter of 1579).
Work alone: do not spawn agents. Do not use the network at all (no web, no Gallica). Repository root:
/Users/mhyrr/work/cryptics.

Read exactly one file of instructions: `puzzles/vargas-mexia-es132/sources/transcription/CIPHER3-GUIDE.md` (v2.2), all of
it. It tells you how to split the cipher into tokens and how to write marks. It gives shapes only, no values; you must
stay blind to the key. **Do not open any other file in the repository**: not other transcriptions, not `analysis/`,
not `sources/keys/`, not `sources/cache/` except your page images listed below, not any README, canon, overview or notes.
In particular do not open `sources/cache/gallica-manual/` or `sources/cache/f42-borja-margins/`. Do not try to decode.

Your images (local screenshots; margins have been cut away on purpose, and one white box hides an annotation):
`/Users/mhyrr/work/cryptics/puzzles/vargas-mexia-es132/sources/cache/f42-borja-blind/`
- P1, f. 42r: `p1_f42r_cipher.png`. Two struck-through cipher lines between clear Spanish lines (the cipher begins at
  the end of the line "…lo qual importará mucho", after a small sign).
- P2, f. 42v: `p2_f42v_line.png`. One struck-through cipher line after the clear word "para".
- P3, f. 42v: the large block crossed by an X. `p4_f42v_block_hires_rows2-17.png` is the sharp image; use it for every
  row it shows. `p3_f42v_block_overview.png` shows the whole block at lower resolution; use it for the first (struck)
  row and the last (struck) row, and to check that you have every row.
- P4, f. 43r: `p5_f43r_block.png`, the block crossed by an X, including its struck first and last rows.

The left edge of each block was cut close; the first sign of a row may be partly cut. Write what you see and add `?`.
The X lines and strike lines cross the signs; read through them. Work in {ORDER} passage order. Crop strips with
`magick` into a scratch folder of your own under `/tmp/claude-501/` (guide §8) and view them at native resolution.

Write:
1. `{OUT}/transcription.txt`: the guide's notation, one output line per manuscript line, with a header line
   `# ===== P1 =====` (P2, P3, P4) before each passage, always in the order P1, P2, P3, P4 in the file whatever order
   you worked in. Transcribe only the cipher; leave out the clear Spanish (you may write the clear word just before a
   passage in a `#` comment).
2. `{OUT}/NOTES.md`: passes (guide §6, the second pass in the opposite direction); every 3+ digit run left joined;
   every `?`; every `<sign:…>`; every `<under>`; image problems (cut edges, strike lines, blots).

**Effort (required).** This is slow work and you have as long as you need. Cut each image into strips of at most 3
lines, each strip in a left and a right half overlapping by ~300 px, at native resolution (no downscaling). View every
strip. Then do the second pass in full: re-view every strip in the opposite direction and correct the transcription
line by line. Do not finish until both passes are complete. In NOTES.md give the number of strips viewed in each pass.
If you could not complete the second pass, say so plainly.

Then reply with four lines: passages covered, number of cipher lines per passage, number of `?`, strips viewed per pass.
