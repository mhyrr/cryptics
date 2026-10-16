# Margin reader prompt (exp 08), 2026-10-16

---

You are a transcriber of 16th-century Spanish handwriting. Work alone: do not spawn agents. Do not use the network.
Do not open any file in the repository except the images listed here. Write output only in {OUT}.

The images are notes written in the margins of a 1579 letter (BnF Français 15561, ff. 42–43), in
`/Users/mhyrr/work/cryptics/puzzles/vargas-mexia-es132/sources/cache/f42-borja-margins/`:
- P1: `m1_f42r_margin.png`: the left-margin note (starts with a small sign, "aunque la condición…"). Ignore the stamp
  and any main-text letters at the right edge.
- P2: `m2_f42v_gloss.png`: the two or three words written *above* the struck line. Transcribe only those words.
- P3: `m3_f42v_margin.png`: the long left-margin note on f. 42v (starts "Al primero deste…"), then
  `m4_f42v_below_block.png`, where that note runs on: its first two lines continue in the margin
  ("y con la Emperatriz y con los ministros"), then the text continues across the full line. Transcribe the margin
  note and the full-width lines in this image, and mark with a line `# --- full width ---` where the margin note
  ends and the full-width text begins.
- P4: `m5_f43r_margin.png`: the left-margin note on f. 43r ("mayores, dubdo que…").

Ignore anything at the right edge of a crop that belongs to the main column (numbers, signs, cut-off letters).

Write `{OUT}/plaintext.txt`: a header line `# P1` (P2, P3, P4) before each passage, then the text, one output line per
manuscript line, in diplomatic spelling (keep the spelling, u/v, ç, double letters as written). Expand an abbreviation
only where you are sure, with the added letters in square brackets: `Mag[estad]`, `V[uestra] M[agestad]`. Write `?`
after a word you are unsure of and `[…]` for an illegible stretch. Crop with `magick` into your own folder under
`/tmp/claude-501/` and read at native resolution; re-read every line once more from the end before finishing.

Then reply with one line per passage: number of lines and number of `?`.
