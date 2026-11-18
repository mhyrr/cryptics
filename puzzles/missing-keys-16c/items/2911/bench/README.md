# Bench for no. 2911: work on the key with scripts only

Set up 2026-11-17 at Greg's request. Everything a key build needs is frozen here, so a trial costs a script run
and no reader. The pair is spent as a held-out test (`../README.md`); it is now a development case with a known
answer.

## What is frozen
| File | What | From |
|---|---|---|
| `inputs/cipher-full.txt` | V/140, both-readers-agree signs, marks joined to bases, doubled signs joined by count (3,228 units, 69 lines) | `../work/cipher-doubles.txt` |
| `inputs/plain-full.txt` | Machiavelli's copy as printed in 1877 (3,145 letters) | `../work/plain-print.txt` |
| `inputs/plain-consensus.txt` | the two plain readers' agreed words (1,648 letters) | `../work/plain-consensus.txt` |
| `inputs/cipher-p1.txt`, `inputs/plain-p1.txt` | the first page only: 33 lines, 1,332 sheet signs, 1,893 plain letters | cut by the true decode, so the cut is exact |
| `../outside/truth.tsv` | the period key VI/82 as one agent read it | sealed, see below |

The first page is the fast case: its plain text is nearly complete (the true decode has 2,215 letters, the print
1,893). The full pair is the hard case: 42% of the cipher has no plain text.

## Commands (run from `bench/`)
- `python3 run.py <variant> [p1|full] [--plain print|consensus]`: build with `variants/<variant>.py`, score,
  append a row to `runs/results.tsv`.
- `python3 score.py <key.tsv> <cipher.txt>`: score any table.
- A variant is a module with `build(cipher_path, plain_path, log) -> rows`. `variants/v0_alignpy.py` is the
  aligner as it stood at the pilot.

## The score (`score.py`)
Place by place against the true decode: coverage, precision, recall, how many of the 56 frequent signs come out
mostly right, the null share of built values, and marked table rows right and wrong. Ceiling: the true key,
written one row per unit, scores precision 0.957 and recall 0.954 on the full pair (the rest are sheet signs the
readers wrote as two different names), 0.968 on the first page.

## The bar for H6 (written 2026-11-17, before any variant but v0 was run)
A variant passes when, on **both** `p1` and `full` against the printed text:
1. precision ≥ 0.90 (of the places where it speaks, nine in ten agree with the period key);
2. recall ≥ 0.60;
3. marked rows wrong ≤ 10% of marked rows, and no more than 2 `certain` rows wrong;
4. built null share ≤ 0.10 (the true key's is 0.002).
The first page may be used freely to develop. The full pair is run to confirm, and each full run is logged in
`runs/results.tsv` in the order run; nothing is deleted from that file.
A variant that passes here has been fitted to this pair. Its first clean test is the next item's held-out run,
or the bare letters V/134 and V/125 scored against the true key.

## What is sealed
`../outside/` and `runs/*.key.tsv` hold sign values. No transcription reader, and no agent asked to build a key
blind on this cipher, may open them. `runs/results.tsv` and this file hold none.

## What the bench does not test
One cipher, one hand of readers, one plain side. A variant can pass here and fail on a cipher of another design.
The Cp.30 calibrations (`../../../analysis/02-*`, `03-*`) must still pass after any change to `line/align.py`.

## Results so far (2026-11-17; `runs/results.tsv` has every run in order)

All on the first page (`p1`) against the printed text. None passes the bar.

| Variant | What it changes | Precision | Recall | Built null share | Reading |
|---|---|---|---|---|---|
| `v0_alignpy` | nothing (the pilot's aligner) | 0.00 | 0.00 | 1.00 | collapses to nulls even where the plain text is nearly complete |
| `v1_gap` | gap state; null prior 0.002; letter skip dear | 0.00 | 0.00 | 1.00 | a small null prior does not stop the drift: null counts feed themselves |
| `v1_gap`, nulls forbidden for 10 passes | | 0.00 | 0.00 | 0.00 | no collapse, but nothing sharpens: one marked row |
| `v2_boot` | tight start at the anchored beginning, then grow | 0.57 | 0.07 | 0.00 | learns a little in the first 250 units, then the free end lets gaps take every later unit |
| `v2_boot`, gaps and nulls off | | 0.00 | 0.00 | 0.00 | log-likelihood per unit worsens as the stretch grows (−1.66 → −2.30): the start table is not right enough to carry |
| `vx_oracle` (diagnostic, starts from the true table) | | 0.96 | 0.60 | 0.00 | the passes hold the true table: 31 of 32 marked rows right |

**What this shows.**
1. The model and the pair are sound. Started from the truth, the passes stay there. The open problem is the
   start, as the pilot's failure already suggested.
2. The likelihood barely prefers the truth. The oracle run ends at −1.46 per unit; the all-null run at −1.61 and
   an all-gap run at −1.07. Two reasons: gaps are too cheap (extend −1.0 a unit), and a true emission that
   meets a different spelling in the print costs as much as a wrong one. The true decode matches the print on
   72% of letters only.
3. Signs here occur 10–30 times each. A window of ±275 letters gives such a sign no signal. Cp.30's units each
   occur a hundred times, which is why calibration passed.

**Next trials, in the order I would take them.**
- `v3`: anchors from repeats. The cipher has 39 sequences of four signs or more that occur three times or more;
  the plain text has repeated words at matching relative positions. Matching the two by position gives anchors
  every hundred units or so, which is the tight start the passes need. Anchors are positions, never values.
- Emission noise: let a unit's value meet a one-letter spelling difference at a modest cost, so that the truth's
  likelihood stands clear of the degenerate states.
- Gap cost: extend dearer than a noisy emission (about −2.5), opened only where the table is already sharp.
- Then confirm on `full`, then rerun the Cp.30 calibrations.

## Bare letters (added 2026-11-17, after the four readers reported)
`inputs/bare-V134-1r.txt` (the Dieci to Machiavelli, 17 Aug 1510) and `inputs/bare-V125-5r.txt` (the summary sent
22 Aug 1510): both-readers-agree signs, marks joined, doubles joined by the same count rule. Reader agreement by
token: 0.838 and 0.810 (`../results/agreement.tsv`); V/125 is in another hand. These pages took no part in any
build. They are the clean test for a variant that passes the bar: build on the pair, decode these, and score
with `score.py <key.tsv> inputs/bare-V134-1r.txt`.
With the period key itself (`../outside/decode-bare-*.txt`, sealed) 83% and 77% of their signs get a value, and
V/134 reads as Italian in stretches: Venetian galleys at Civitavecchia, the French fleet, the duke of Urbino.
That is the period key reading a letter it was applied to by script, which shows the transcription chain is
sound on a page nobody tuned anything to. It is not a result of this dive's key work.

## Registered trial `v3_seed`

Find sign pairs from runs with one changed sign and compare them with the sealed
scorer. Pool evidence only if at least 90% of all candidate pairs, counting
unscorable pairs against the rule, share a value. A null requires the same
flanks to recur with and without the sign in two distinct contexts.

Start with repeated cipher runs and nearby repetitions in the print. Keep
segmentations that agree at repeated signs. Rank starts by exact matches to the
print beyond the seed itself. Extend from exact matches in reading order and
lock new values only when fixed letters bracket the same candidate span at
independent places. Use gap passes only after a majority of frequent signs have
values. Expect the verified locks to avoid null collapse and give more recall than
`v2_boot`. Low precision would count against the lock rule. High precision with
low recall would mean the locks do not reach enough of the text.

From `bench/`, run `python3 run.py v3_seed p1`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v3_seed` | p1 | 0.000 | 0.000 | 0.000 | 0 / 0 | 0.000 |

The only group candidate (two signs at 85 places) failed the check, neither
clear unit occurs in the printed text, and the repeat locks yielded no marked
row. The provisional start reached six of 44 frequent signs, below the gate for
the gap passes. The observed null share comes from an empty marked table.

Reproduce the group counts without printing pairs:

```sh
python3 variants/v3_seed.py inputs/cipher-p1.txt > /tmp/2911-v3-pairs.tsv
python3 diagnose.py groups /tmp/2911-v3-pairs.tsv
```

See `runs/v3_seed-p1-groups.tsv` and `runs/v3_seed-p1.log`.

### Stop and diagnosis

The bench stops under the rule for steps 1–3. No candidate qualifies for the
full-pair run or the bare letters. Step 4 (shape layout), step 5 (language score)
and step 6 (spelling tolerance) were deferred.

The repeat search generated 3,255 distinct seed tables. Sixteen agreed with
the period table at every proposed value. The first such seed ranked second
and two made the shortlist of 32. Neither gained a sign under the lock rule.
After extension the chain score selected a provisional table with five of
seven values right. It had no marked rows. More repeat candidates alone
would leave the lock rule unchanged. That rule needs known signs on both sides
of a single sign and repeats of the proposed value at independent places.
The search also limits its starting values to letters and open syllables.

The strongest blind result remains `v2_boot` (0.566 precision, 0.065 recall,
0.114 coverage, one of two marked rows right). It got 86 letter places right
and 64 wrong, all on signs with at least 20 occurrences. It got no syllable
places right and two wrong, both on signs with fewer than five occurrences.
The remaining 1,180 places were silent. See `runs/v2_boot-p1-errors.tsv`.

From `bench/`, reproduce the aggregate audits with:

```sh
python3 diagnose.py seeds inputs/cipher-p1.txt inputs/plain-p1.txt
python3 run.py v2_boot p1
python3 diagnose.py key runs/v2_boot-p1.key.tsv inputs/cipher-p1.txt
```

The seed audit repeats the blind generator, ranker and extension before
scoring any proposed value. It returns counts only. The `run.py` command
recreates the local v2 table and appends a trial row.

## Reopened trial `v4_islands`

Extend each shortlisted repeat seed through islands with several unresolved
signs. A candidate island must fix at least six letters with already-valued
signs and have a unique pair of plaintext boundaries within the position
window. Keep islands in reading order. Count a value at an unresolved sign
only when every segmentation within those boundaries agrees, then require
separate places before adding the value. Seed hypotheses and final tables
compete by independent positional evidence. Empty emissions remain off.

Expect a correct seed to gain values where the previous one-sign lock had
no foothold. Failure to mark values, or gains dominated by wrong values,
would count against the island evidence. The H6 bars and the held-out
inputs stay frozen.

Run from `bench/`:

```sh
python3 variants/v4_islands.py
python3 run.py v4_islands p1
```

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v4_islands` | p1 | 0.138 | 0.484 | 0.067 | 3 / 2 | 0.000 |

The synthetic segmentation controls passed. On p1, the islands added no
values to any start. The three correct marked rows came from the seed.

## Registered trial `v5_cribs`

Search the print for segmentations that satisfy repeated signs within each
cipher window. This requires no matching repeated words across windows.
Each sign consumes one letter or an open syllable. An unresolved reading
can consume either. A candidate must corroborate its proposed values outside
the window that supplied them. Rank corroboration by a monotone chain of
exact matches, then try extending the shortlisted starts. Expect this to
supply broader starts than the repeat phrase method. If well-corroborated
windows still produce wrong values or too little coverage, this local
substitution constraint is insufficient.

Run `python3 variants/v5_cribs.py` and `python3 run.py v5_cribs p1` from `bench/`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v5_cribs` | p1 | 0.000 | 0.000 | 0.000 | 0 / 0 | 0.000 |

The repeated-sign control passed. None of the long windows on p1 admitted
an exact letter-or-open-syllable segmentation under the repeated-sign and
position constraints.

## Registered trial `v6_merge`

Combine compatible starts from separate repeated passages. A merge may
compete only if the combined table explains an exact plaintext span that
needs a value supplied exclusively by each parent. Keep competing tables
in a beam and rank them by exact matches in reading order. Run the
multi-sign extension on the best combined tables. Expect a wider start
than either parent can supply. A large combined table with low precision
would count against the cross-support rule.

Run `python3 run.py v6_merge p1` from `bench/`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v6_merge` | p1 | 0.269 | 0.575 | 0.155 | 8 / 2 | 0.000 |

The merge produced 15 provisional values from four starts. Multi-sign
extension added none. The marked table got 206 places right and 152 wrong.
Of the syllable places, 105 were right, 57 wrong and 554 silent.
The exact bridge shows that some values agree with the same text span.
It does not verify every value carried in from either start.

This exhausts the bench's trial limit, counting the oracle as a diagnostic.
H6 still fails p1. The full pair and the bare letters remain held out.
`runs/v6_merge-p1-errors.tsv` breaks down the result by type and frequency.

## Reopened on Fable (2026-11-17, second session)

Greg ran the bench prompt again in a session on Fable; the trials `v3`–`v6` above ran on a harness without it.
The variant count starts again at `v7`. The H6 bar, the sealing and the held-out inputs are unchanged.

`synth.py <variant>` is new: a planted pair of the 2911 kind (letters and open syllables, 35% of the plain
text cut in six stretches, 8% unread signs, 2% wrong signs, 5% spelling noise). A builder is tried there
first, where the answer is ours. This is the synthetic abridged pair the last handoff asked for.

## Registered trial `v7_beam`

Read the cipher in order with a pointer in the plain text, and carry the table inside each hypothesis. A sign
met for the first time takes the 1, 2 or 3 letters at the pointer; this earns nothing. A sign met again must
spell its value at the pointer, and earns a point per letter. A miss costs 2.5. A run of cipher with no plain
text is a gap with the pointer held (open 5, 0.5 a unit). A beam keeps 4,000 hypotheses, 40 at most at one
pointer. There is no null value. The cipher is read three times; each later pass holds the `certain` rows of
the pass before and gives every other sign a fresh value. Steps 2 and 3 of the prompt in one builder; step 1
(groups) is not used.

On the planted pair (seeds 1 and 2): 58 and 63 marked rows right, 8 and 4 wrong, place precision 0.907 and
0.968, recall 0.850 and 0.923.

Expect on `p1`: most frequent signs valued, precision near the oracle's. Against it: a score that stays
negative (misses outweigh repeats), or precision under 0.5 with many marked rows, which would mean the real
values are not spans of the printed text often enough for exact repeats to carry.

From `bench/`: `python3 run.py v7_beam p1`.

| Variant | Note | Coverage | Precision | Recall | Marked right / wrong | Reading |
|---|---|---|---|---|---|---|
| `v7_beam` | as registered (miss 2.5, gap 5 + 0.5) | 0.101 | 0.000 | 0.000 | 0 / 3 | every unit goes into one gap |
| `v7_beam` | miss 1.0 | 0.137 | 0.000 | 0.000 | 0 / 9 | reads, but wrong |
| `v7_beam` | miss 0.4, gap 3 + 0.1 | 0.268 | 0.723 | 0.194 | 8 / 5 | first blind table that is mostly right |
| `v7_beam` | the same, rows marked by evidence score | 0.622 | 0.511 | 0.318 | 18 / 16 | more rows, half wrong: wrong vowels hit by chance |

The registered expectation failed: the score stayed negative. `vx_beam_oracle` (the same reader with the true
table held, counts only) says why. Even the true key spells the printed text at the pointer at only 55% of
places (637 match, 339 other spelling, 171 no counterpart). `spelling.py p1` gives the letter counts: 1,265 of
the print's 1,893 letters sit in blocks equal to the true decode; 714 decode letters have no print in 68
blocks (not a few long stretches: one every 20 signs), and 228 small differences of 158 kinds, so no spelling
rule mends it. The plain side is a loose abridgement. The planted pair in `synth.py` was too kind (5% noise).
The miss cost was set three times (2.5, 1.0, 0.4) and stays at 0.4.

## Registered trial `v8_handoff`

The beam's path and table start `v1_gap`'s passes, in a corridor of ±15 letters round the path. No null. Gap
cost about equal to an unvalued sign's emission. Expect the passes to mend wrong beam values, since the oracle
run shows they hold a right table: precision over 0.8, recall over 0.4. Against it: precision at or under the
beam's 0.51, which would mean the beam's path is too far from the truth for a ±15 corridor.

From `bench/`: `python3 run.py v8_handoff p1`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v8_handoff` | p1 | 0.265 | 0.924 | 0.245 | 9 / 3 | 0.000 |

The passes mend the beam's table: precision 0.51 → 0.92, over the bar for the first time on a blind run.
Recall and the row count are far under it: 12 rows marked.

## Registered trial `v9_rounds`

`v8_handoff`, then three more rounds of passes; each round re-centres the ±15 corridor on the best path of the
table just built. Expect recall to rise round by round with precision held. Against it: rows that stop
growing after round 1 (the path is as good as this corridor allows), or precision falling as rows are added.

From `bench/`: `python3 run.py v9_rounds p1`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v9_rounds` | p1 | 0.345 | 0.928 | 0.320 | 12 / 1 | 0.000 |

Rounds add three right rows and drop two wrong ones; the path stops moving after round 2. Of 80 rows 67 stay
unmarked, many with strong support (for example 15 of 28 places): `key_from_path` wants 60% of a sign's places
to agree, and on this pair a right value agrees at about half.

## Registered trial `v10_mark`

`v9_rounds` with rows marked by evidence against chance (hits and misses weighed by how often the value's
letters stand in the plain text), not by share. Expect about 30 marked rows and recall near the oracle's 0.60.
Against it: more than 10% of marked rows wrong, which would mean support on the best path is not evidence
enough and each value needs a check off the path.

From `bench/`: `python3 run.py v10_mark p1`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v10_mark` | p1 | 0.652 | 0.964 | 0.629 | 36 / 0 | 0.000 |

**Passes the H6 bar on `p1`**: precision 0.964 (bar 0.90), recall 0.629 (0.60), no marked row wrong (24
`certain`, 12 `probable`), no null. 30 of 44 frequent signs mostly right. The oracle start gave 0.96 and 0.60.

### `v10_mark` on the full pair (first full run of this session) and on the bare letters

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | Built null share |
|---|---|---|---|---|---|---|
| `v10_mark` | full | 0.628 | 0.921 | 0.579 | 33 / 4 | 0.000 |

**Fails the bar on `full`, narrowly**: recall 0.579 (bar 0.60) and 4 of 37 marked rows wrong (10.8%, bar 10%).
Precision passes. So H6's bar is met on `p1` and not on `full`.

Bare letters, scored with `score.py <key.tsv> inputs/bare-*.txt` (signs valued; of those, agree with the
period key):

| Table | V/134 1r (358 signs) | V/125 5r (550 signs, another hand) |
|---|---|---|
| built on the full pair (`runs/v10_mark-full.key.tsv`) | 0.662 valued, 0.941 agree | 0.629 valued, 0.792 agree |
| built on `p1` (`runs/v10_mark-p1.key.tsv`) | 0.701 valued, 0.960 agree | 0.571 valued, 0.933 agree |

The period key itself values 83% and 77% of these signs. The table from the first page is the better one:
the full pair adds text that is 42% uncovered and four wrong rows come with it.

## Registered trial `v11_settle`

In the full run the path still moved 1.0 letters a unit in the last round; on `p1` it had stopped. `v11` runs
rounds until the path moves under 0.2 letters a unit (12 at most). The idea comes from the log of the full
run, so its full run is a second look at `full`, not a clean confirmation; the bare letters were scored
before it. Expect no change on `p1`. Against it: `full` no better than `v10_mark`.

From `bench/`: `python3 run.py v11_settle p1`, then `full`.

| Variant | Subset | Coverage | Precision | Recall | Marked right / wrong | `certain` wrong | Built null share |
|---|---|---|---|---|---|---|---|
| `v11_settle` | p1 | 0.652 | 0.964 | 0.629 | 36 / 0 | 0 | 0.000 |
| `v11_settle` | full (second full run) | 0.659 | 0.935 | 0.617 | 33 / 3 | 1 | 0.000 |

**`v11_settle` meets the four bars on `p1` and on `full`.** On `full` the path settled at round 9. `p1` is
unchanged (it had settled by round 4). Caveat: the settle rule was written after reading the log of the first
full run, so `full` was looked at twice. The clean figures are the bare letters under `v10_mark` above. With
the `v11` full table (`score.py runs/v11_settle-full.key.tsv inputs/bare-*.txt`): V/134 0.654 valued, 0.940
agree; V/125 0.607 valued, 0.814 agree. `certain` rows alone on `full`: 28 right, 1 wrong
(`score.py ... --min certain`).

### What carried the result (this session)
1. **Reading in order with the table inside the hypothesis** (`v7_beam`, prompt step 2). It gives a path
   through the plain text and a table that is half right. Alone it fails.
2. **Soft passes in a ±15 corridor round that path, no null** (`v8`, `v9`; steps 2 and 3). They mend the table.
   The old passes failed because the window was ±275 letters; the beam path narrows it.
3. **Marking by evidence against chance** (`v10`). Recall 0.32 → 0.63 with no wrong row on `p1`.
4. **Costs fitted to a loose abridgement.** `vx_beam_oracle` and `spelling.py` showed that the true key spells
   the print at only 55% of places; a miss must cost 0.4 of a letter, not 2.5.
Not used: homophone groups (step 1), layout (4), language score (5), spelling tolerance as such (6; the
passes' soft counts do that work).
