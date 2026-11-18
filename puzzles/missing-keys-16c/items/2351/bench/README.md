# Bench: rebuild the key of no. 2351 blind

**Why.** On 2026-11-18 we read Acciaiuoli's letter B with a key that is mostly B. Dudout's published
reconstruction (`../README.md`, stages 5, 6, 4b). Our own builders did not build it: with the good plain
reading, `tied.py` marked 2 entries and `align.py build --abridged` stopped with "no path through the band".
This bench asks whether a builder of ours can rebuild that key from the pair alone. The key is now a
confirmed answer the builder never sees, as on no. 2911 (`../../2911/bench/README.md`).

## The bar (written 2026-11-18, before any bench run)
`python3 score.py <table.tsv> <label>`: of the signs the blind table marks that the answer also values,
**at least 20 shared and at least 80% with the same value.** Report place precision and recall beside it.
Every call of `score.py` is logged in `runs/results.tsv`; the number of scored runs is part of the result.
A pass on this one pair is a builder fitted to one pair. Say so.

## What a builder may see
- `inputs/cipher-A.txt`: letter A, three readers merged; a sign is a base, or a base and its mark (`x+4`).
- `inputs/plain-A.txt`: reader PE's text of the chancery copy from where the cipher starts; `[...]` is a hole.
  It is about 1,850 letters for 1,133 signs, with 58 holes and many doubtful words: a loose plain side.
- `inputs/marks.tsv`: counts of marks by base in the cipher text.
- `../tied.py`, `../solve.py`, `../../../line/align.py`, `../../../line/METHOD.md`: our tools and method.
- Planted pairs you make yourself (`../tied.py synth` is one generator).

## What is sealed
**`../key-v0.tsv`, `../key-s0.tsv`, `../key-pe-tied.tsv`, everything in `../sources/`, `../results/`,
`../work/`, `../readers/`, `../READING.md`, `../cache/`, and the stages of `../README.md` from "Stage 3"
down hold the answer or text decoded with it. `score.py` may read the answer. You may not open those files,
print them, or let a builder import them. Do not paste sign values into your reports; report counts.**
Your own builder's output tables hold values; keep them in `runs/` (not checked in) and do not quote them.
Letter B is out of bounds entirely.

## What is known about the cipher without the answer (fair to use)
- 569 of 1,094 signs carry a mark. Five marks (`4 3 ~ 5 1`) sit on sixteen bases; other bases never take them.
- H9: a base with a mark spells a consonant and the vowel after it; one value per base, one per mark.
- **One lesson that did come from the answer, disclosed here because it shapes the model:** do not assume an
  unmarked base spells the consonant it has under a mark. Treat an unmarked sign as a sign of its own. Some
  unmarked signs stand for whole words, some for double letters, and some may stand for nothing.
- The plain side is a period decipherment in normalised letters (u and v merged, as `align.norm_letters`).

## Work
1. Read `../../../line/METHOD.md` (steps 4 and 5) and `../tied.py`. Reproduce the two failures on the inputs.
2. Find out why, with scripts that report counts. Fix or write a builder in `variants/` (`v1_….py`, each
   with `build(cipher_path, plain_path, log) -> rows`). Python standard library only.
3. Prove each variant on planted pairs first, made as loose as this pair (holes, wrong words, unread signs,
   word signs, bare vowels). A variant that cannot rebuild a planted key is not run on the real pair.
4. Register each real run in this README before it is scored: the variant, its settings, why. Then score.
5. Stop when the bar is met, or after eight scored runs, or when you can name what is missing. Then write
   "Result" and "What carried it" (or "The wall") here, and port what worked into `../tied.py` or
   `../../../line/align.py` with a unit test in `../../../line/test_line.py` on a planted pair.
6. Commit by file name as you go (`git add <files>`; never `git add -A`; no attribution lines; do not push;
   leave `AGENTS.md` alone).
