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

## Result (2026-10-01; `measure.py` → `result.txt`)
| | Reader A | Reader B | Bourdeau |
|---|---|---|---|
| Tokens | 365 | 367 | 358 |
| Sign tokens N (non-numeric) | 344 | 345 | 327 |
| Distinct labels D | 145 | 165 | 127 |
| N / D | 2.37 | 2.09 | 2.57 |
| Hapax labels | 70 | 96 | 56 |
| Marked tokens / labels | 80 / 40 | 81 / 37 | 95 / 48 |
| Arabic numbers | 19 | 20 | 29 (he reads small digits 2–6 where A and B read letter-signs) |

- Per-line token counts agree within 3 across all three readers on every line.
- The Arabic number sequence agrees between A and B except 199/139? and B's extra "2":
  88 196 223 184 152 89 86 30 209 152 30 25 199 174 152 54 89 128 85. 152 occurs three times.
- No word breaks are visible (A, B).
- **G1: PASS** (N = 344 ≥ 300).
- **G2:** N / D ≈ 2.1–2.6, against ≈ 8.4 for Marmont and 10.0 for f. 555 (858 symbols / 86
  distinct, Lasry 2022). Each sign is seen about two and a half times. Half the labels are
  hapax. The gate passes on length, and the control decides the rest.
- Label disagreement (D from 127 to 165) is mostly how finely each reader splits variants,
  not missed tokens. Reconciling the inventories is deferred: it matters only if the control
  says annealing can work at this length.
