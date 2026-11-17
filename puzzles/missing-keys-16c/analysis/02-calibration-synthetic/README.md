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

**Result.** Not run yet.
