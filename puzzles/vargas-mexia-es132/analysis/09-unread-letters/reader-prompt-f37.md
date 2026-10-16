# Reader prompt (exp 09, f. 37–38), from exp 08's passage prompt, guide v2.3, 2026-10-16

---

You are a blind transcriber of a 16th-century Spanish cipher letter (BnF Espagnol 132, ff. 37–38, a letter of 1578).
Work alone: do not spawn agents. Do not use the network at all. Repository root: /Users/mhyrr/work/cryptics.

Read exactly one file of instructions: `puzzles/vargas-mexia-es132/sources/transcription/CIPHER3-GUIDE.md` (v2.3), all of
it. It gives shapes only, no values; stay blind to the key. **Do not open any other file in the repository**: not other
transcriptions, not `analysis/`, not `sources/keys/`, not `sources/cache/` except the images below, not any README,
canon, overview or notes. Do not try to decode.

Your images (screenshots), in `/Users/mhyrr/work/cryptics/puzzles/vargas-mexia-es132/sources/cache/f37-blind/`:
- P1, f. 37r: `p1_f37r_block1.png`, four cipher lines after the clear words "buena gana."
- P2, f. 37r: `p2_f37r_block2.png`, nine cipher lines.
- P3, f. 37v: `p3_f37v_top.png`, the five cipher lines at the top (ignore the clear Spanish below them).
- P4, f. 37v: `p4_f37v_bottom.png`, three cipher lines at the foot. **The right ends of these lines are cut off at the
  gutter**; transcribe to the cut and end each line with `<cut>`.
- P5, f. 38r: `p5_f38r.png`, the four cipher lines at the top (ignore the clear Spanish below them). P5 continues P4.
Work in {ORDER} passage order. Crop strips with `magick` into your own scratch folder under `/tmp/claude-501/` and view
them at native resolution. **View at most about 60 images in total** (strips plus overviews): use strips of 2–3 lines,
left and right halves, and reuse your crops in the second pass.

Write:
1. `{OUT}/transcription.txt`: the guide's notation, one output line per manuscript line, a header line
   `# ===== P1 =====` (… P5) before each passage, always in the order P1–P5 in the file. Cipher only.
2. `{OUT}/NOTES.md`: passes (guide §6, the second pass in the opposite direction); every 3+ digit run left joined;
   every `?`; every `<sign:…>`; every `<under>`; image problems.

**Effort (required).** View every strip; then do the second pass in full in the opposite direction and correct line by
line. Do not finish until both passes are complete. Give the number of images viewed in each pass. If you could not
complete the second pass, or images failed to display, say so plainly.

Then reply with four lines: passages covered, cipher lines per passage, number of `?`, images viewed per pass.
