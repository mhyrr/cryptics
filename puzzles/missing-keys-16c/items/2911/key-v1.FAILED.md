# key-v1.tsv: FAILED STAGE 4

`key-v1.tsv` is a copy of `key-v0.tsv`, frozen 2026-11-17 as README section 4 requires. **It failed the held-out test and is not a key.** 39 of its 40 usable rows are nulls (`results/key-v0-counts.tsv`). Do not decode anything with it. The mark is in this file because `line/align.py read_key` does not accept a comment row in the table.
