# 00 — transcription agreement and the length gate

**Frozen 2026-10-01, before either blind reading was returned.**

## Question
How long is the f. 539 cipher, in tokens and distinct signs, when two blind
readers count it? Does it pass the length gate for ciphertext-only annealing?

## Inputs
- `../../sources/transcription/reader-A/`, `reader-B/`: blind readings (raw, unmerged).
- Bourdeau's single-reader transcription, pinned at commit
  `9226922ffb0663b1d9b95f4ef898d093efd74ef2` (`targets/joyeuse/ct_f539.txt`), as a third reader.
  The script fetches it by that URL.

## Measures (label-independent where possible)
1. Tokens per line and in total, for each reader.
2. Number tokens: the sequence of Arabic numbers and Roman numerals in reading order.
   Labels do not matter here, so this is the cleanest agreement test.
3. Non-numeric sign tokens N, distinct non-numeric labels D, and the ratio N / D.
4. Marked vs unmarked split, using each reader's own mark suffixes.

## Gate (fixed now)
- **G1 (the session rule):** N ≥ 300 non-numeric sign tokens, taken as the
  *lower* of the two blind readers' counts. Below that: "short-text wall", no annealing.
- **G2 (reported, not gating):** N / D. For reference, Marmont is about 1,300 / 155 ≈ 8.4
  (Church). F. 555 is measured from Lasry's paper if it gives the figures.
- If G1 passes, the next step is a pre-registered matched control
  (`01-annealing/`). The control, not the gate, decides whether a target run means anything.
