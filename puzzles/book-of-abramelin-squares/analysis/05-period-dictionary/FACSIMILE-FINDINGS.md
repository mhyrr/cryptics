# Facsimile check — 2026-09-17, after acquisition commit `d812620`

**The six cited Latin dictionary readings are present on the supplied images.**
This verifies readings of selected examples. It does not establish dependence
on this edition, a complete lexicon, or prediction of unseen square letters.

## Evidence and exposure

PRIMARY: the tracked [image packet](../../sources/period-dictionary/README.md),
with image URLs and scan/signature locators in `SOURCES.tsv`. Its 28 JPEGs and
source table pass the supplied SHA-256 manifest. This pass inspected both
title pages, the 1595 printer's note, and every page spanning the six entries.
It did not independently inspect every flanking page or rederive every quire
signature. Inferred signatures remain identified as such in the source table.

The reader had already seen Kollatsch's quotations, the acquisition reports,
and Greg's spot checks. These are direct checks against a separate primary
source, **not blinded readings**. Treat the whole inspected packet as discovery
exposure, including neighbouring words. No new square or German witness was read.

The [1596 title](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=3)
prints `PARS PRIMA`, `FRANCOFVRTI`, `EX OFFICINA PALTHENIANA`,
`sumtibus Nicolai Baſſæi`, and `ANNO M D XCVI`.
The [1595 title](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=1)
prints `Partis I. Pars II.` and the same place, printer and publisher, with
the date in apostrophus numeral forms. The
[printer's note](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=2)
explicitly says the new part starts at T. These are the two divisions of part I,
not the proper-name part II. Titles do not themselves print the A–S/T–Z spans.

## Readings and comparison

`facsimile-readings.json` contains scoped excerpts: the cited printed Latin
transliterations, adjacent alternatives, entry boundaries and uncertainties.
It is **not a full multilingual transcription**. Hebrew/Greek originals and
the long Latin poetic lists remain in the full-page images; no modern
transliteration is substituted for them. Unresolved Hebrew vowel points and
the bet/mem ambiguity are not converted into definite text.

The following comparisons are computed in `facsimile-audit.json` by
`audit_facsimiles.py`. The right-hand strings remain CLAIMANT quotations from
`claims.json`, not newly collated square readings. Long-s/case folding is the
only spelling normalization. Water also needs the explicitly recorded joining
of a printed line break, `ma-` / `iim` → `maiim`; that is a layout operation.

| Entry; PRIMARY locator | Image-read Latin target | Quoted square string | Equal after stated operations? |
|---|---|---|---|
| [Lehrer, 1596 scan 834](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=834) | moreh | moreh | yes |
| [Warſager, 1595 scan 159](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=159) | nabhi | nabhi | yes |
| [Vnterweiſer, 1595 scan 105](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=105) | melabbed | melabbed | yes |
| [Himmel, 1596 scan 690](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=690) | rakia | rakkia | no |
| [Waſſer, 1595 scan 160](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=160) | ma- / iim | MAIAM | no |
| [Wachs, 1595 scan 150](https://www.digitale-sammlungen.de/en/view/bsb10314207?page=150) | nechoth | necot | no |

All six image-read targets agree with the *dictionary* quotations. Only three
agree with the quoted *square* strings under the stated operations. This is
not a success rate for reconstruction: the examples were chosen because of
known correspondences, and no unseen letter was predicted.

Alternatives matter. Lehrer has `moreh`, `melammed`, `alluph`; Vnterweiſer has
`melabbed`, `moreh`. The latter also cross-refers to Lehrmeiſter. Warſager
places the line-broken `Ko-` / `ſem` next to `nabhi`. Himmel supplies several
alternatives before its extensive poetic material. They are retained, with
uncertainties, in the readings file rather than silently replaced by the
desired word. The neighbouring wax transliteration's n/r and the initial
cluster of Himmel's last transliteration remain unresolved in this pass.

The printed `melammed`/`melabbed` difference is a within-packet observation.
It does not decide which Hebrew type was set in the ambiguous 1595 word, whether
the lexical choice is an error, or whether any error is distinctive to this
edition. Those claims still require linguistic adjudication and an identified
earlier comparison edition's title and entry. Do not infer ambiguous Hebrew
from the readable Latin transliteration. The d/t difference in Vnderweiſer/
Vnterweiſer and the Hüfft/Hütte/Himmel sequence are also observed, not explained.

## Construction decision before historical implementation

These pages establish available words and alternatives. They supply no
Abramelin coordinates. A caption selecting a word does not specify which
alternative, orientation, row/column, offset or additional word fixes a
disjoint interior symmetry orbit. Symmetry equates cells within an orbit;
it does not transfer a value from a boundary orbit to a separate inner orbit.

The unchanged protocol's fixed straight-row/column construction is our testable
candidate class, not an independently justified historical rule. **No interior
placement is promoted to a historical input by this audit.** Do not search for
positions or letter alterations that make the exposed spellings fit and then
score those same examples as predictions. In particular, the three unequal
pairs do not authorize doubled consonants, substitutions or h deletion.

Before implementing a historical model, supply a source or a documented
discovery-only analysis that fixes caption-to-entry mappings, candidate
alternatives, exact permitted paths and symmetry for an identified grid class.
If several placements are allowed, freeze and enumerate them all. The
falsifiable prediction is the letter shared by all surviving completions at a
wholly hidden interior orbit; ambiguity must abstain, and contradictions and
misses remain in the denominator. Evaluate on the protocol's internal Mathers
folds and controls, without presenting reused data as blind validation.

No contiguous evaluation sample is extracted in this pass: positional inputs
do not yet suffice, and the supplied packet is selected, exposed discovery
material. Preselect a separate contiguous block, including misses, when the
placement question is resolved; log any prior exposure and freeze every
normalization before scoring. No historical performance fields change from
null, no incomplete-square predictions are issued, and no witness comparison
is opened. H7 and H12 remain open. Nothing here establishes randomness.

## Reproduce

From the repository root, with Python's standard library:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/05-period-dictionary/audit_facsimiles.py
PYTHONHASHSEED=7919 python3 puzzles/book-of-abramelin-squares/analysis/05-period-dictionary/audit_facsimiles.py --check
```

The script verifies all manifest files, looks up locators in `SOURCES.tsv`,
records source/input/code hashes, performs the declared operations and compares
the saved readings. It cannot verify a human visual reading. Inspect the linked
full pages for that. `claims.json`, `freeze.json`, `PROTOCOL.md`, the synthetic
fixture, solver and original preflight outputs remain unchanged; the new audit
is separate and does not retrospectively alter the original freeze.
