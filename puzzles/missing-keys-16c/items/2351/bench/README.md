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

## Notes (2026-11-18, second agent; the first was cut off and left drafts, reviewed here)

### Steps 1 and 2: the two failures reproduced, and why (`diag.py`, counts only)
- `align.beam_read` (`python3 diag.py beam`): three passes; the pointer ends at letter 1,144 of 1,853, 709
  short. The soft pass needs a corridor 15 letters wide to reach the last letter, so `build --abridged` stops
  with "no path through the band". Cause: every sign has a value of its own, so the 66 kinds of marked sign
  are learnt one by one, 8 places a kind (`diag.py signs`), and a marked sign is two letters; the beam
  under-reads and falls behind 0.6 letters a unit.
- `tied.py` as it stood (`python3 diag.py tied`): score 30.9, 209 hits on 1,133 units, 2 entries marked, the
  pointer ends at 1,304. Cause: it makes an unmarked base spell the consonant it has under a mark (185
  places, 14 kinds). With the unmarked base a sign of its own (`tied.BARE_FREE`, the README's disclosed
  lesson): score 261.2, 325 hits, 18 entries marked (3 marks, 9 bases, 6 others), the pointer ends at 1,762.
- So the tying (16 bases and 5 marks learnt from 543 places, 26 places an entry) is what the pair needs, and
  the false assumption about unmarked bases is what broke it.

### Variants
- `v1_free`: `tied.py` with the unmarked base free; the table written one row per sign of the cipher text
  (a marked sign is valued when its base and its mark are both marked; status is the weaker).
- `v2_soft`: v1's beam, then forward-backward passes with the same tying in a corridor 40 letters each side of
  the beam's path, the end left free; rows marked by evidence on the last best path.
- `run.py <variant> <label>` builds on the real pair and prints counts; it does not score.

### Step 3: planted pairs (`plant.py`; the planted cipher has the README's lesson built in)
| Planted pair | v1_free | v2_soft |
|---|---|---|
| default (36 holes, 15% of words damaged, 25 word signs), seeds 1-6 | 6 of 6 pass; 75-88 signs marked, 3-5 wrong; recall 0.67-0.90 | 6 of 6; 89-96 marked, 0-1 wrong; recall 0.93-0.97 |
| hard (`damage=0.35 ncode=70 holes=58 wrong=0.06`), seeds 1-6 | 4 of 6; the four: 22-68 marked, 0-2 wrong | 4 of 6; the four: 58-84 marked, 0-4 wrong |

The two hard seeds that fail (3 and 5) fail for both and show it: beam score under 25, no base or mark
marked by the beam, 4 to 7 signs marked in all. The real pair's beam (score 303 after three passes, 9 bases
and 4 marks marked, pointer at 1,733 of 1,853) sits among the hard seeds that pass (scores 86 to 408).
The real pair has more letters a sign (1.64) than any planted pair (1.37 to 1.52): it is looser than the plants.

### Step 4: runs registered before scoring
| # | Label | Variant, settings | Why | Built table (before scoring) |
|---|---|---|---|---|
| 1 | `v1_free` | `v1_free`, defaults (`TIED_BEAM` 3000, 3 passes) | the smallest change: the old builder with the one false assumption taken out | 43 signs marked, 37 with a vowel mark; they cover 493 of 1,094 places |
| 2 | `v2_soft` | `v2_soft`, defaults (`BAND` 40, `EPS` 0.05) | on plants it adds recall and no more wrong rows than v1 when the beam has a foothold | 74 signs marked, 61 with a vowel mark; 768 of 1,094 places |

Both tables were built before either was scored; no setting was chosen with a score in hand.
