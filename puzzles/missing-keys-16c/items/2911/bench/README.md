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
