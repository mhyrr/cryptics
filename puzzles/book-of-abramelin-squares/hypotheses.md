# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` /
`refuted` / `superseded by Hn`. Every hypothesis names the test that would
move it. Results are recorded in `research.md` and in `analysis/`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H1 | One of the tested elementary symmetries holds across every uncorrected grid in the digital Mathers sample. | refuted | Count known-letter contradictions without correction. | No tested family fits all 81 complete grids. Transpose fits 69; combined transpose/half-turn 55. |
| H2 | First row generates later rows by cyclic shifts in the digital Mathers sample. | refuted | Exhaust shifts on complete grids. | 0/81 fits even allowing arbitrary row rotations. This does not reject corrupted historical precursors. |
| H3 | Boundary letters generate interiors by the four declared A=0 mod-26 addition/subtraction formulas. | refuted | Test fixed alphabet and formulas on complete grids. | 0/81 fits for each formula. Other alphabets and formulas remain untested. |
| H4 | Assumed symmetry can force some missing letters while leaving free choices. | supported | Compute symmetry orbits, contradictions, forced cells and unconstrained orbits. | 1,064 conditional fills under combined symmetry; MAIAM still has 4 free orbits. Historical accuracy untested. |
| H5 | Existing reconstructions provide independent validation data. | weakened | Trace every candidate target cell to an uncorrected manuscript reading. | Kollatsch's compilation admits conjectures; modern corrected grids need an apparatus. |
| H6 | The squares have not previously been structurally studied. | refuted | Locate a prior structural study. | Kollatsch lists a symmetry draft; see canon and research log. |
| H7 | The lexical seed words derive from a period multilingual dictionary. | open | Replicate Kollatsch's cited entries and characteristic errors with dictionary facsimiles, including an earlier comparison edition. | Exact source identified: Frankfurt Palthenius/Basse Sylvae quinquelinguis 1595/1596, part I (A–S and T–Z). Six Latin dictionary quotations verified on the acquired facsimiles; alternatives and uncertainty retained in Exp. 05 facsimile audit. This checks selected spellings, not derivation or edition-specific dependence. Earlier comparison edition and Hebrew adjudication still missing. |
| H8 | Separate frame symmetries with the fixed error cost expand correct recovery of scattered blanks beyond exact global symmetry. | supported | Mask cells, compare correct counts, precision and exact tasks; repeat on geometry-preserving controls. | 555/591 correct versus 456/463; coverage 79.6% versus 62.4%, but exact tasks fall 30→18. Whole hidden orbits yield no predictions. Exp. 02. |
| H9 | Cross-family row/column fragments reliably predict independent letters. | weakened | Exclude donor families, hide whole symmetry orbits, compare matched shuffled controls and planted fragments. | 2/10 correct over 841 hidden cells; three folds abstain entirely. Standalone method recovers 320/320 planted motif centers. Exp. 03. |
| H10 | The tested shared local recurrence families reliably generate new square interiors from boundaries. | weakened | Nested selection of family/corner, followed by held-out recursive rollout and planted-rule recovery. | 301/1,429 correct, zero exact tasks, no confident predictions; baseline 262 on the same cells. Planted rule generates 3,920/3,920. Exp. 04. |
| H11 | The fixed frame error model repairs injected substitutions while leaving unmodified digital readings unchanged. | refuted | Inject one/two errors, score restorations and collateral changes, also run on the unmodified export. | Flags 12 unmodified letters in eight grids; with one substitution/grid, 48/62 repairs correct and 13 collateral proposals. This does not determine which historical readings are corrupt. Exp. 02. |
| H12 | A frozen period lexicon and independently fixed interior word placements predict whole hidden inner orbits beyond symmetry and frequency baselines. | open | Verify discovery figures, then freeze primary lexicon, applicability, caption mapping, spelling policy and all placements; run interior-orbit masks with competing completions and shuffled controls. | Exp. 07 verifies all ten Exp. 06 sequences against published compilation figures; Exp. 09 now checks the draft figures and preserves their discrepancies. Central-line, near-central expansion, overlap and name-overlay alternatives remain. No recipe selected or historical evaluation run; construction selector and independent inputs remain missing. The draft also allows names derived from square letters, so name independence cannot be assumed. |

| H13 | Erasing only capitalized name cells restores TA symmetry in the selected dragon, beast and bird compilation grids. | refuted | Mask exactly those cells, retain all lowercase readings, and count conflicting orbits. | Exp. 08 leaves 14, 13 and 12 conflicting orbits, requiring at least 22, 22 and 21 additional lowercase erasures. This is narrower than the author's hypothesis of wider rewriting. |

## Notes
H1–H4 are deliberately narrow first-pass tests, not claims about all possible
historical constructions. H7 is a literature hypothesis, not a new conjecture.
Results for H1–H4: [experiment 01](analysis/01-mathers-structure/RESULTS.md).

H8–H11: [three-experiment stress test](STRESS-TESTS.md). H8 supports a narrower
completion tool, not automatic correction or generation. H9–H10 do not exhaust
external dictionaries, different alphabets or mixtures of historical recipes.

H7 and H12 are different claims: source attribution versus independent-letter
prediction. [Experiment 05](analysis/05-period-dictionary/README.md) preserves
that distinction. Its synthetic recovery does not support H12 historically;
its missing inputs do not weaken H7. No new randomness inference is warranted.

After acquisition `d812620` and the facsimile audit (2026-09-17), **H7 and H12
remain open**. The image-access wall is resolved for the selected entries.
Their Latin readings are checked; no earlier edition or independent positional
rule is supplied by these pages. No new transformations are justified. See
[FACSIMILE-FINDINGS.md](analysis/05-period-dictionary/FACSIMILE-FINDINGS.md).

After `bb87024`, H7/H12 remain open. The
[construction audit](analysis/06-construction-evidence/EVIDENCE.md) does not
support a boundary-only account: the apparatus reports inner lexical strings.
Their occurrence does not select dictionary alternatives, transformations,
placements or symmetry on other grids. A frame-filling order is not a letter
assignment rule. Source diagrams could not be inspected; no exploratory recipe
was promoted to a frozen historical model. The alternative constructions and
their prospective falsifiers remain listed in experiment 06. The original
experiment 05 freeze is unchanged.

After `3815688`, [experiment 07](analysis/07-published-diagrams/README.md)
verifies selected edited compilation figures and the edition preview. It
confirms the recorded orientation without resolving the separate draft's
row/column discrepancy. H7/H12 stay open: reproducing an edited figure does
not choose inputs or placements independently, nor validate a reconstruction.
Experiments 05 and 06 remain unchanged.

After acquisition on 2026-09-18, experiment 09 resolves the draft access and
layout questions. Beast/bird also fail capital-only erasure under the source's
T hypothesis. NEBBELAH/GEBHINAH fit conditional T but retain three free central
orbits each; no changed original letter is recovered. H7/H12 remain open.
Compatibility with symmetry does not identify a historical precursor.
