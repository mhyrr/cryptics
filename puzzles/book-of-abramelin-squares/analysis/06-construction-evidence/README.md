# 06 — Construction evidence, not a reconstruction trial

Started from `bb87024` on 2026-09-17. This is a separate discovery audit;
experiment 05's freeze and inputs must remain byte-for-byte unchanged.

## Question and audit specification (written before the script)

Do the exposed lexical examples specify positions that reach independent
interior orbits? What additional choices would a predictive recipe require?

Use the six previously audited dictionary examples, plus exposed central-word
and overlap examples from the edition preview. Preserve the printed polygram
sequence as reported by web extraction, including capitals. Put successive
polygrams in successive rows, left to right, top to bottom. Coordinates are
one-based `(row,column)` in **this convention**, not claims about PDF diagram
orientation. Do not rotate, transpose, correct, or merge source readings.
Reject non-square inputs. Keep editorial variants as notes, never repairs.
Captions are readable excerpts with long-s and abbreviations expanded, not
diplomatic transcriptions. Polygram separators become JSON array boundaries;
no letters are changed. Proposed opposed-word overlaps are checked at the
explicit cells in examples.json; they are not learned by path search.

For each record, compute exact occurrences of the cited square string along
full rows and columns in both directions. These searches describe exposed
data; they do not authorize a future placement search. Also compute the
explicitly nominated path's letters, its inner cells, overlaps with boundary
orbits, capital positions, and candidate lengths. Import alternatives for the
six entries unchanged from the facsimile readings. Missing dictionary readings
remain missing, not zero candidates in a supposedly exhaustive lexicon.

Compute orbits separately for identity, main-diagonal reflection T,
anti-diagonal reflection A, T+A (four group elements), horizontal+vertical
reflection HV, and full D4 (eight elements). Record every conflicting orbit
against the unmodified extracted rows. Do not pick a symmetry by fit and call
it a historical input. For each family, report interior orbits untouched by
the outer boundary and by the nominated lexical path. Give exact coordinate
lists, not just counts. Distinguish the quoted square spelling's geometrical
reach from the independently read dictionary spelling's exact admissibility.
No insertions, substitutions, h deletion, inferred transliteration, or silent
joining of uncertain alternatives. Case folding/long-s conversion and water's
already logged printed line join are the only comparison operations.

The residual count is freedom under **hypothetical constraints**, with all
other cells withheld; it is not a missing-letter count in the complete source.
If the full grid conflicts with a symmetry, that family is only a counterfactual
geometry diagnostic, not a compatible completion. Full D4 is useful for
conservative masking; it is not synonymous with T+A.

No historical solver, evaluation answers, new raw witness, independent lexicon,
or incomplete-square predictions enter this audit. No performance is scored.

## Source and access boundary

See [EVIDENCE.md](EVIDENCE.md) for exact source pages, statements versus
observations versus proposals, and the failed diagram access. Source figures
were **not visually verified**. The extracted sequences are provisional
discovery inputs. This limits what this pass can conclude and is part of the
handoff, not an omitted verification step.

## Reproduce

Python standard library, from the repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/06-construction-evidence/audit.py
PYTHONHASHSEED=7919 python3 puzzles/book-of-abramelin-squares/analysis/06-construction-evidence/audit.py --check
python3 -m unittest discover -s puzzles/book-of-abramelin-squares/analysis/06-construction-evidence -p 'test_*.py' -v
```

`examples.json` records exposure, locators, raw sequences, and nominated paths.
`results.json` records input/code hashes, all orbit coordinates and conflicts.
`TABLE.md` is generated. Its numbers describe the supplied sequences and
declared coordinate convention, not authenticated manuscript grids.

## Decision

There is evidence worth pursuing for inner lexical placement; a boundary-only
summary would be wrong. No source-verified, frozen rule assigning independent
inner letters is ready for evaluation. Retain the alternative constructions
in EVIDENCE.md. First resolve the source figure/sequence orientation and
applicability questions. Only then preselect and acquire a contiguous lexicon
sample, including misses, freeze a new predictive specification, and run the
unchanged protocol's whole-orbit and interior-only comparisons. This audit
cannot stand in for that experiment.
