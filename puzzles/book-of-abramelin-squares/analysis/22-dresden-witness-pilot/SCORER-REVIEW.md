# Scorer review — 2026-09-26

Scope: static audit and local reproduction only. No manuscript image was
opened. No script, raw reading, or result was changed.

## Findings

1. **The join key is invalid for these inputs.** `score.py:26` and
   `score.py:38` pair records by `(physical_page, grid_index)`. The readers
   traversed multi-column pages differently. Exact raw-grid matches show, for
   example, A `244/2` = B `244/4`, A `244/3` = B `244/8`, A `245/3` = B
   `245/7`, and A `245/7` = B `245/6`. Twelve of 22 index pairs are discarded
   for shape disagreement. Two more, `245/3` and `245/8`, happen to have the
   same shape but are different source grids; they contribute 91 of the 92
   reported conflicts. The aggregate `304/397` agreement is therefore not a
   transcription-agreement statistic.

2. **`collation.json` is not a per-cell collation of the cohort.** Shape
   disagreements are omitted at `score.py:44-47`, leaving 10 of 22 records.
   The two false same-shape joins above remain in it. `collation.json` also
   omits `reading_issues`, so the file does not disclose its missing 12 records
   without consulting `results.json`. It is safe to describe only as the
   preserved first index-key comparison. The post hoc plan's physical locator
   map and separate output are required before the packet is reusable.

3. **Literal I/J disagreement is not preserved in the collation output.** At
   `score.py:53` and `score.py:67-70`, `I` versus `J` becomes an agreed `I` and
   creates no conflict record. The test at `test_score.py:36-42` confirms the
   normalized merge but its name overstates the result: only an aggregate
   `j_to_i_positions` count remains. Raw values survive in the two reader
   files, but a reusable per-cell output must retain both reader values for
   every cell, as `POSTHOC-PLAN.md` now requires. The present readings contain
   no J, so this does not alter the frozen counts.

4. **The reader-completeness check is too weak for future use.**
   `score.py:22-31` verifies only the declared `pages_completed` list, unique
   local keys, allowed characters, and cohort pages. Both readers can omit the
   same grid, or even all grids, and pass. It does not validate page labels,
   positive integer grid indices, distinct reader identities, or expected item
   coverage. The actual files each contain 22 items and have different hashes;
   the defect is latent rather than a cause of this result.

5. **The source-ID and truth gates are conservative once the physical join is
   valid.** A source ID exists only when both readers agree on positive integer
   chapter and number (`score.py:72-79`). Missing or duplicate IDs, incomplete
   or non-square grids, Mathers shape differences, and less than 50% visible
   agreement are excluded (`score.py:88-110`). `?` truth becomes
   `unreadable_truth`; `.` truth becomes `blank_truth`; neither counts toward
   the 50-cell interior threshold (`score.py:123-135`, `score.py:162-167`). The
   chapter 4 versus chapter 1 disagreement is therefore handled honestly in
   the preserved primary result. A source-ID match alone still cannot repair a
   bad local-index join.

6. **The freeze pins the declared inputs, not the implementation or Mathers
   gate source.** Commit `8d25cfa` contains the protocol, acquisition script,
   manifest, and freeze. The scorer and tests first appear with the exposed
   readings and results in commit `6de0a8a`. `freeze.json` pins the protocol,
   image manifest, and experiment-13/20 predictions, but not `score.py` or
   `sources/mathers-squares.json`, even though the latter controls shape and
   visible-agreement admission at `score.py:99-107`. The protocol did declare
   those rules before exposure, so the primary result remains auditable. It
   should not be described as a pre-exposure-frozen implementation.

7. **The protocol asks for coverage that the result does not report.** It asks
   for abstentions, disagreements, and whole-square/orbit coverage. The scorer
   reports model outcomes only for Mathers-blank prediction cells after a
   primary join. It does not report orbit coverage or a whole-square coverage
   denominator. In the preserved result, the only admitted square (`4/4`) has
   zero frozen prediction positions, so there is no model score to interpret.

8. **`access.py --check` verifies two local artifacts but does not bind them
   together.** It regenerates `page-index.json` from the pinned METS and checks
   each cached image against the hash stated in `image-manifest.json`. It does
   not check the manifest's `metadata_sha256`, physical page, page label, or
   image URL against the regenerated index. The frozen hash of the whole
   manifest protects the present experiment, but the access check alone is not
   a complete source-provenance check.

9. **The exposure claim is bounded correctly, with a provenance limit.** Both
   raw files identify `gpt-5.6-sol` and state that the reader saw only the three
   pages. The scorer does not verify prompt isolation or distinct executions.
   These are two separate same-model readings, not independent model families
   or evidence against training exposure. `PROTOCOL.md` and `README.md`
   correctly state that project-fresh access does not establish manuscript
   independence or absence from model training.

## Post hoc scorer review

`posthoc.py` corrects the main structural defect without changing either raw
reading. `remap()` requires exhaustive one-to-one use of both 22-item reader
sets, rejects record reuse and cross-page joins, and replaces only the working
locator and source identifier. It now checks the map against the complete
source-only locator inventory and rejects source-ID differences. The checked
post hoc collation retains both raw records and both cell values; the audit
confirms they are byte-for-data unchanged. The outputs are separate from the
primary outputs and explicitly non-confirmatory.

The checked result has 22 mapped grids, 10 Mathers joins, and 12 Mathers
exclusions. Its 935 row-group positions comprise 926 reader agreements, eight
conflicts, and one unknown. These limits remain:

1. **The alignment hash list is caller-defined, not enforced.**
   `posthoc.py:83-90` accepts any keys in `alignment["input_sha256"]`; an empty
   object would pass. The actual map committed in `c68d901` pins both raw
   readings, the source-only locator audit, image manifest, primary scorer,
   and Mathers export. The original freeze pins both prediction files and the
   protocol. `posthoc.py` itself is not pinned by either manifest and was not
   included in that pre-score commit. The source map is demonstrably
   pre-score; the implementation is reproducible from its eventual commit but
   is not a pre-score-frozen program.

2. **The synthetic `grid_index` is global map order, not an image-local
   index.** `posthoc.py:16` and `posthoc.py:28-33` enumerate the full alignment
   list and write that number into each remapped reader record. This is safe
   for the internal `(page, index)` key, but its name can mislead downstream
   users. `locator_id` is the authoritative physical locator; preserve the two
   original grid indices and call the synthetic field `alignment_index`, or
   number it within each page.

3. **Locator validation now binds the map to the source-only inventory.**
   `posthoc.py:97-106` requires the same complete locator set and the same
   physical page, chapter, and item number. Positive integer chapter and
   number are also validated. `reason` is copied without a non-empty check,
   but every committed entry has a concrete source-only reason.

4. **I/J normalization remains semantically compressed.** `cell_records()`
   preserves both raw values, which fixes the primary collation's data loss.
   It still labels raw `I` versus `J` as `agreed_letter`, rather than
   `normalized_agreement`. This does not affect the present no-J readings.

5. **The coverage calculation matches the declared symmetry, but combines
   zones.** Its orbit key
   at `posthoc.py:65-67` is the group generated by transpose and half-turn,
   matching experiments 1 and 16. Coverage is explicitly limited to frozen
   Mathers-blank targets, and it warns that class correctness is not letter
   recovery. The two admitted target squares contain 22 border cells in 12
   TA-orbits and 50 interior cells in 18 TA-orbits. `coverage` reports 15
   combined orbits per square, so its `target_orbits_all_correct` counts mix
   border and interior. That makes the symmetry result `6/15` per square look
   opaque: it is 6/6 border orbits and 0/9 interior orbits, with all interior
   positions abstained. Report coverage by zone before using orbit counts in
   prose. No unit test exercises `coverage()`.

6. **“All 22 have the same shape” includes two matching ragged records.**
   Twenty mappings are square coordinate grids. `1/8` has row lengths
   `6,5,5,5,5`; `3/4` has `6,7,7,7,7,7`. Both readers agree on each ragged
   shape, so all 22 enter the reader-agreement total. The output correctly
   labels these two as `row_group_position_only` and excludes them from Mathers
   scoring as non-coordinate-bearing. Describe 926/935 as agreement on aligned
   row-group positions, not 22 square grids.

7. **The 50 interior cells are 18 symmetry orbits and two squares.** The
   checkerboard result is 27/50 cells but only 4/18 wholly correct interior
   orbits. The chapter and class-mode letter models are 11/50 cells and 2/18
   wholly correct interior orbits; the global model is 10/50 and 3/18. Neither
   cells nor orbits are independent trials across only two squares. These
   figures are descriptive because the locator correction is post hoc.

8. **Historical independence remains unknown.** Both readings came from the
   same model family, and the Dresden witness can share ancestry with sources
   behind Mathers, Dehn, modern corrected editions, or model training data.
   `posthoc-results.json` says the result is non-confirmatory, but it does not
   carry the ancestry/training limitation itself. Keep that limitation beside
   every model score, not only in the protocol or README.

## Reproduction

All existing checks pass:

```text
python3 -m unittest -v test_score.py   6 tests, OK
python3 score.py --check               Pilot reproduces
python3 access.py --check              Metadata index and image hashes verify
python3 audit_scorer.py --check         Scorer audit reproduces
python3 -m unittest -v test_posthoc.py  5 tests, OK
python3 posthoc.py --check              Post hoc collation reproduces
```

These checks establish deterministic reproduction. The five post hoc unit
tests do not exercise coverage, blank/unknown cell status, I/J provenance,
positive identifier rejection, or the dependency manifests.

`audit_scorer.py` independently derives the primary comparison counts from the
two raw readings and writes `audit-scorer.json`. Its checked output records 22
local-index pairs, 12 dropped shape disagreements, 10 same-shape pairs, 92
conflicts, and 91 conflicts in the two same-shape pairs contradicted by exact
same-page cross-index full-grid matches.

The same audit now verifies the post hoc outputs. It records the 22/10/12
mapped/aligned/excluded split, raw-reader preservation, the two matching ragged
grids, and cell and orbit coverage split into border and interior.
