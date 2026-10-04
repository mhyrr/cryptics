# 05 — Cipher 4 v2: second readers, reconciliation, decoder v2, held-out f. 154

## Question
1. Do reconciled two-reader transcriptions of all Cipher 4 letters (ff. 87, 123, 157, 179, 198) keep the v1 readings?
2. Do the key extensions hold on the v2 texts and on an untouched held-out letter (f. 154)?

## Method (2026-10-04)
- Second blind readers for ff. 87, 123, 157, 179 (Sonnet 5.5; f. 198 already had two). Each frozen by commit before decoding.
- `align.py` diffs the two raw transcriptions (`diffs_*.txt`). A blind reconciler per letter (no key, no decodes) decides
  every block from the ink and spot-checks agreed tokens (`sources/transcription/v2/*-DECISIONS.md`).
- `decode_v2.py`, frozen `8fafd88` before any v2 text and before f. 154 was transcribed: v1 + tokenizer fix for
  "<cross above>" + Devos's rule that a cross above doubles the letter.
- `tally.py` lists every extension occurrence; `tally-judged.md` records the reading-based judgment.
Run: `python3 decode_v2.py ../../sources/transcription/v2/f198.txt`; `python3 tally.py > tally.txt`.

## Result
- Reader agreement before reconciliation (aligned tokens): f. 123 260 of ~300; f. 198 857 of ~1,116 tokens incl. clear words;
  spot-checks of agreed tokens: f. 87 0/28, f. 123 1/22, f. 157 2/24, f. 179 1/16, f. 198 3/30 changed (shared errors exist,
  ≈ 5–10% at f. 198).
- Held-out (ff. 87, 154, 157, 179): 2H = que 83/84, Σ = o 37/38, cross doubles 36/36, H = ne 14/16: all pass.
  21. = que fails outside f. 198 (1 fit, 1 misfit, 1 unclear); 21_ = qui untested.
- f. 154 (King, 4 Dec 1578) reads as continuous Spanish: Arras; Lalaing, Egmont and the Catholic nobility; Mota's
  envoy Andrés de Ayala; Guise's cipher with Don John and "los 800 mill ducados"; Alençon's agents in Philippeville.
- Readings and the full list of unresolved spans: `readings-v2.md`.
