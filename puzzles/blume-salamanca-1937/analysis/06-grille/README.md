# 06-grille — 4 × 4 turning grille on telegram 2

**Question.** `04` could not test the turning grille at 160 letters (plants detected 2/20). T2 is exactly 10 blocks
of 16, and a 4 × 4 grille has only 4⁴ = 256 hole patterns. Is T2 a 4 × 4 grille cipher?

**Method.** `grille.py`, exhaustive. 256 hole patterns (each starting orientation is itself one of them) × 2
turning directions × grid read by rows or by columns = 1,024 keys. Each is tried in both uses: holes-then-grid
(the standard use) and grid-then-holes (the inverse). Every block uses the same key. Score: Spanish quadgrams per
letter. The best T2 keys are also applied to T1's first 608 letters (38 blocks), and T1 is searched alone. Ten
planted controls (160 letters, random key) use the same code. Run: `python3 -I grille.py > result.txt` (2 s).

**Result** (`result.txt`).
- Controls: 10/10 recovered exactly; each best key scores the true text (−3.99 to −4.28).
- T2: best −6.30 standard, −6.33 inverse; median over all keys −6.88. Readings are noise. The same keys on T1
  score −6.76 or lower. T1 alone: best −6.61.

**Reading.** A 4 × 4 turning grille is excluded for T2, in either use, and with one key on both telegrams. T1
fits no square grille without nulls (615 = 3 × 5 × 41). Not covered: a grille with nulls, a grille of side 6 or 8
on padded text, or a grille followed by a second transposition.
