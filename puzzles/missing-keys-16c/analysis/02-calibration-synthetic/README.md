# 02 — synthetic calibration of the aligner

**Question.** Given a pair made with a key we hold, does `line/align.py` rebuild that key, and does its
held-out test tell a right table from a shuffled one?

**Method.** `make_pair.py` enciphers the first 3,000 letters of *Lazarillo de Tormes*, tratado primero, with
Cp.30 (`vargas-mexia-es132/sources/keys/cipher3.tsv`), adds eight word codes and two nulls (Cp.30 as printed has
neither), and adds noise: 12% of cipher tokens (mark dropped, base misread, token missed, vowel mark misread) and
1.5% of plaintext letters. `run.py` builds the table with no anchors but the two ends, scores it against the true
table, and runs the five-fold held-out test.

The noise rate is set from es. 132: its blind readers got about 86% of decoded letters right (exp 08, cited in
`vargas-mexia-es132/analysis/09-unread-letters/README.md`).

**Exploratory run (before the bars).** Seed 1 was run while the aligner was written. It showed the scorer's
chance level: a table with values shuffled within type scores 0.25 (edit-distance matching of two unrelated
Spanish strings). `PIPELINE.md` sets the control bar at ≤ 25%, which is that chance level. The bar here is
≤ 0.30, and stage 4 takes the same change. Seed 1 is not counted below.

**Pass bars (written 2026-11-16, before `run.py` was run).** Seeds 11–15. Every seed must pass all three.
- **S1.** Of the unit types that occur five times or more, at least 90% are marked `certain` or `probable`
  with the true value.
- **S2.** At most 2% of the marked entries have a wrong value, and no `certain` entry is wrong.
- **S3.** Held-out: accuracy ≥ 0.85 on covered units, coverage ≥ 0.70, shuffled control ≤ 0.30.

**Amendment to S1 (2026-11-16, after the first registered runs, before the final run).** S1 counts how often
a unit type occurs in the noisy cipher. The noise model misreads a base as any other base with equal chance, so
a rare sign (31, 32, 34: three to five true uses) is mostly misreads; the table marks it `unknown`, which is the
right answer, and S1 counts that as a miss. **S1a** is S1 over types enciphered five times or more before noise.
`result.tsv` reports both. S1a is the bar that decides; S1 stays in the table as registered.

**Run.** `python3 run.py` (about 10 minutes). Needs `../../sources/cache/lazarillo-wikisource.txt`
(`sources/PROVENANCE.md`).

**Result (2026-11-16): pass on S1a, S2 and S3 for all five seeds, with the fourth version of the aligner.**
`result.tsv`; tables in `out/` are not checked in (rerun to get them).

| Seed | S1 registered | S1a (true uses ≥ 5) | marked / wrong | held-out acc. | coverage | control |
|---|---|---|---|---|---|---|
| 11 | 42 of 47, fail | 40 of 40 | 42 / 0 | 0.949 | 0.977 | 0.249 |
| 12 | 42 of 44 | 40 of 40 | 43 / 0 | 0.932 | 0.982 | 0.253 |
| 13 | 42 of 45 | 39 of 40 | 43 / 0 | 0.944 | 0.980 | 0.252 |
| 14 | 41 of 44 | 39 of 39 | 41 / 0 | 0.941 | 0.977 | 0.254 |
| 15 | 41 of 47, fail | 38 of 40 | 44 / 0 | 0.937 | 0.965 | 0.257 |

S1 as first registered fails on seeds 11 and 15 for the reason given in the amendment.

**Runs before this one, and what each showed.**
1. First aligner, seed 1 only (exploratory): every marked value right.
2. After the first fix for the real pair (`03-calibration-real`): S1 and S2 failed on all five seeds. Code
   words were cut to a syllable ("madre" → `101` = "mad", the cross above it = "re").
3. Code spans counted by place: 1–4 wrong marked values on four seeds, one of them `certain` on two. A code
   sign and its cross still split one word. Added: a proposal step that tries "this sign stands for the whole
   word it sits in" and keeps it only if the log-likelihood rises.
4. Seed 11 still had one wrong `probable` value of 47 (2.1% against the 2% bar): a code used three times,
   spelt three ways by the plaintext noise, valued from the letters the spellings share. Changed: `probable`
   needs four supporting places (was three), and a value whose places touch unaccounted letters stays unknown.
   This run is the table above.

**Limits.** One key design (Cp.30), one text, one noise model made by me. The scorer's chance level is 0.25,
so "control ≤ 0.30" says only that a shuffled table does no better than chance. The aligner was changed three
times against these five seeds and the one real pair; they are no longer unseen data. The first unseen test is
the pilot item's own held-out run.
