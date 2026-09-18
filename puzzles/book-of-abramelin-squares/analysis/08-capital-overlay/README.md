# 08 — Do capitalized cells account for symmetry conflicts?

## Specification, before computation — 2026-09-17

This is a discovery diagnostic of edited examples, not a hidden-letter trial
or a recovered construction. The question is whether deleting precisely the
capitalized cells leaves a grid compatible with symmetry. A name overlay on an
otherwise symmetric precursor predicts such compatibility if only the capitals
were replaced. Residual lowercase conflicts falsify that narrow account for
that symmetry and edited reading. They do not falsify overlays plus other changes.

Fixed scope: compilation Qu. 3.1 (dragon), 3.2 (beast), 3.4 (bird), and 4.8
(water), all already discovery-exposed. The edition identifies name insertions
for the first three; its water/Amaimon suggestion is explicitly tentative.
No further corpus examples or raw witnesses will be opened for this test.
Rows retain case and are visually read from local source pages 3–4.

Primary symmetry: TA (transpose and anti-diagonal reflection, four elements),
already used in experiments 01/06. Report T, A, HV and D4 alongside it without
choosing a winner or treating any as an established historical constraint.
Compare letters case-insensitively; use original ASCII case only to select the
mask. Do not correct spelling, reorder cells, fit a name path or supply names.

For each family, report full-grid conflicting orbits, residual lowercase
conflicting orbits and their exact coordinates/letters, and the minimum number
of further lowercase cells that would have to be erased for compatibility.
This minimum is an erasure lower bound, not a recommendation to edit letters.
Only if all surviving orbits agree, list capital cells whose hypothetical
precursor letter is forced by a lowercase orbit mate, separating equal letters,
changed letters and unconstrained cells. A whole erased orbit remains free.

Two exact combinatorial controls: among all masks deleting the same number of
cells, count those that leave no conflicting orbit; also condition on the same
number of deletions in each concentric frame. Dynamic programming over orbit
erasure counts computes the exact numerator and denominator. These are control
fractions, not inferential p-values: examples and capitalization are selected,
and this diagnostic has no random sampling design. It does not establish name
identity, name order, historicity or prediction accuracy.

## Sources and provenance

Edited PRIMARY — [Kollatsch compilation](https://works.hcommons.org/records/xep4n-asx54),
`sources/buchstabenquadrate.pdf`, pp. 3–4. Supplied locally by Greg, checksum
recorded in `sources/LOCAL-PDFS.json`; its MD5 agrees with the public record.
CLAIMANT apparatus / edited PRIMARY — [edition preview](https://works.hcommons.org/records/pd060-xcq09),
`sources/lp_wp.pdf`, printed pp. 140–141 (PDF 122–123), notes 140,6/8/12 and
141,14. Conjectures in both publications preclude independent raw-witness
validation. The draft's own diagrams are still unavailable.

## Reproduce

Python standard library, from repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/08-capital-overlay/analyze.py
python3 puzzles/book-of-abramelin-squares/analysis/08-capital-overlay/analyze.py --check
python3 -m unittest discover -s puzzles/book-of-abramelin-squares/analysis/08-capital-overlay -p 'test_*.py' -v
```

Tests compare the control DP to exhaustive enumeration of every mask on small
grids, and check that erased independent orbits stay undetermined. The scripts
use the pinned experiment 06 orbit implementation; hashes identify inputs.
PDFs are local, gitignored sources. Computation uses the checked-in readings;
the PDF manifest permits separate verification of the original files.

## Result

See generated `RESULTS.md` and the per-orbit/cell audit in `results.json`.
