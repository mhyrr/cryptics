# Research log — append-only, newest first

## 2026-09-16 — Verification and close

Eight unit tests pass. Re-running extraction, analysis and report generation
reproduces all four derived artifacts byte-for-byte; prediction input hashes
and the total fill count agree with the results. All 104 catalog entries pass
validation after adding the required tiered Sources list; rankings regenerated.
Git's default whitespace check flags the rank generator's existing intentional
Markdown two-space line breaks; the check passes with blank-at-eol disabled.
TK-004 is closed (first dive opened); TK-005 retains the witness-audit work.

## 2026-09-16 — First structural result and handoff

The web tool exposed rows and explicit dot placeholders, allowing an offline
corpus without the requested Python network download. Preserved a 207-line
row export spanning all numbered Mathers tables, then parsed its merged records
into 242 square records. The extraction excludes separately labelled German
supplements; raw rows and literal labels remain. Ten layouts fail the strict
square/single-letter criteria and stay excluded pending images.

[Experiment 01](analysis/01-mathers-structure/README.md) records the method;
[RESULTS.md](analysis/01-mathers-structure/RESULTS.md) gives generated counts.
Measured 81 complete and 151 incomplete analyzable grids. H1–H3 fail in their
declared exact forms. H4 is supported as a constraint statement: combined
symmetry forces 1,064 cells in compatible incomplete grids, yet MAIAM retains
four free letter choices. This is not a discovery of an original generator.

After that first result, added a fixed-rule diagnostic masking each complete
grid to top row and left column. It compares against a visible-letter mode on
the same prediction cells and counts errors and abstentions. No hidden answer
selects the evaluated sample. It tests artificial missingness in this export;
it neither trains nor validates against a second witness.

Saved conditional fills and source hashes in `predictions.json`. During source
discovery, Peterson's variants and examples from Kollatsch's November 2024 draft
were displayed. **Correction to the opening note:** no German manuscript images
were inspected, but some German *readings in editions* were exposed. Future
work must not call them blind targets.

Kollatsch's September 2025 inventory supersedes his 2021 count; see canon for
the updated source. The N 161 shelfmark was found in the SLUB holdings catalog,
but its open imaging remains unresolved. A [2020 source](https://solascendans.com/2020/05/15/abramelin-musings-the-dresden-manuscript/)
(POPULAR) places the N 111 squares at viewer image 243 / written page 240;
this is a locator to verify, not a checked folio reference.

Revised the catalog's absence-of-work claims, set status to partial, and reduced
compute 5→4 and crowding 4→3. Confidence becomes medium. The basis is prior
structural work and incomplete verification readiness, not the failure of an
exhaustive generator search. Follow-up ticket: TK-005.

## 2026-09-16 — Opening the dive and checking the premise

Greg selected Abramelin and authorized a first evening of witness discovery,
Mathers extraction, characterization and simple rule tests. The criteria and
finite first-pass families were written into README before computing results.

The literature search changes the proposed novelty claim. Peterson points to
Kollatsch's edition, and the author's publication list supplies a square-symmetry
draft and a conjecturally corrected compilation. See canon for tiered links.
Do not use those corrected letters as blind manuscript targets. The dictionary
derivation is a lead to replicate, not our finding.

The HAB records expose digitization requests but no direct manuscript images.
The Dresden N 111 viewer is linked but blocked by a JavaScript challenge.
N 161 access remains unresolved. No German square readings have been inspected.

The shell policy rejected curl, including an escalated call. Requested explicit
permission for Python HTTP downloads; web-source work continued independently.

## Dead ends

- 2026-09-16: H1–H3 fail as exact statements about the digital sample; see
  experiment 01. Preserve the distinction from possible corrupted precursors.
- 2026-09-16: H6, the claim of no prior structural work, refuted by the author's
  listing of an explicit symmetry study. No claim of first discovery is justified.
