# 10 — Frozen exploratory caption selector (E1)

Started from 9202fed, 2026-09-18. **A testable partial recipe now exists; no
historical prediction score exists.** E1 stipulates literal caption selection,
exact spellings, central-row placement and transpose symmetry. It is ours, not
an extracted historical instruction. All decisions are in [PROTOCOL.md](PROTOCOL.md).

## Order and separation

1. Read handoffs, canon, hypotheses and experiments 06/09, then experiment 05.
   No acquisition searches for the supplied PDFs were repeated.
2. Wrote E1 and its selector/solver. Checked exact enumeration against brute-force
   binary squares, conflicting visible letters and competing center words.
3. Saved [freeze.json](freeze.json), covering protocol, code, tests and orbit helper.
4. Only then selected the block by the prescribed SHA-256 rule. It selected
   1596 scans 326–327; [selection record](sample-selection.json) pins this choice.
5. Read every included headword and Hebrew-gloss Latin transliteration. Scan 328
   finishes the last entry. Preserve absent glosses, accents, multiword forms and
   one uncertain reading. Saved [lexicon.json](lexicon.json), then its separate
   [freeze](lexicon-freeze.json), before any target-caption join.
6. Audited discovery caption/headword associations separately. Their 2/9 literal
   matches are descriptive of exposed examples, not evaluation. The sample has
   not been joined to those discovery captions or to target captions.
7. Checked whether local inputs supply the required evaluation caption table.
   Mathers JSON has no captions. The supplied edition is a reading sample:
   Book IV printed pp. 138–142 are followed by a LESEPROBE leaf and an appendix
   header at printed p. 175. Page 125 was visually inspected. The compilation
   text extraction did not produce a verified caption-to-Mathers mapping.
   This bounded check did not acquire or inspect raw witness answers.

## What moved

[RESULTS.md](RESULTS.md) and [results.json](results.json) record the input audit.
The independent block has ten entries, five without Hebrew transliterations.
The initial letter of the second Dörffen transliteration is uncertain; that
whole entry abstains. The E1-eligible odd-length domains in sizes 3–25 are
PERESCH and NEKUDAH at n=7. They are *available dictionary words*, not selected
historical predictions. Accents and phrases were not silently simplified.

The exact selector handles alternatives without selecting the one closest to
an answer. It never fills unassigned orbits by plausibility. The toy checks
show that a central cross can leave many completions. Names are not inputs.

The discovery diagnostic identifies different missing operations in broader
lexical theories: semantic association (knowing past things → teacher),
orthographic equivalence (Wax → Wachs), and morphology (Vogels → Vogel).
They are distinct choices. No evidence here selects their scope or ordering.
Adding any of them after this audit starts a new recipe; it cannot repair E1.

## Exact remaining input wall

Historical evaluation requires a table with `target_id`, `caption_raw`, German
source locator, uncertainty, discovery exposure, and alignment evidence that
uses chapter/purpose/context rather than square letters. The existing Mathers
export supplies IDs and letters, but no captions. The supplied edition sample
covers only a limited part of Book IV. Numbering alone is not safe alignment.

No full caption table was produced in this session. No task can yet be labelled
an independent sample hit or miss. No scoring/control run or witness prediction
is claimed. Caption-free dictionary domains are not substitute captions.
The missing input is now explicit; it is not another missing-PDF search.
Obtain or transcribe caption-only material for the fixed manifest, preserving
unmatched targets, then freeze the mapping and evaluation harness before scoring.
Do not redraw the block if it yields zero overlap. If it does, report an
uninformative pilot, not rejection of dictionary dependence.

Experiment 05's whole-orbit and interior-only evaluation and all controls are
specified in E1, including caption-free comparison. They remain **unrun** because
the caption/alignment gate has not passed. H7/H12 remain open; E1 is H14.

## Sources and exposure

PRIMARY: [BSB 1596 scan 326](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=326),
[327](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=327),
[328, continuation/context](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=328).
Full images are in `../../sources/period-dictionary-e1/`; [images.json](images.json)
records direct URLs and SHA-256. This is a scoped lexical transcription, not a
full multilingual edition. Greek/Hebrew and other glosses remain in the images.

Edited PRIMARY: [supplied edition](https://works.hcommons.org/records/pd060-xcq09)
and [compilation](https://works.hcommons.org/records/xep4n-asx54).
[caption-source-audit.json](caption-source-audit.json) pins their hashes and the
bounded text-layer check. No hit for the two eligible headwords in these PDFs is
not a proof of absence from the full historical caption corpus. Old discovery
examples remain exposed. The first 45 lines of the already exposed Mathers row
export were reread during input-format inspection; no new raw witness was opened.

CLAIMANT: source interpretation is inherited from experiments 06/09, especially
the draft's statement that names can derive from square letters. No new source
claim about the original construction follows from our executable E1.

## Reproduce

Python standard library; optional supplied-PDF check also requires `pdftotext`.
Run from the repository root:

```sh
python3 -m unittest discover -s puzzles/book-of-abramelin-squares/analysis/10-caption-selector -p 'test_*.py' -v
python3 puzzles/book-of-abramelin-squares/analysis/10-caption-selector/audit.py --check
python3 puzzles/book-of-abramelin-squares/analysis/10-caption-selector/check_caption_sources.py --check
```

The audit reads source JSON to check its schema and hashes; no grid letters are
passed to the selector/solver. `recipe.py` itself loads no corpus or answer file.
Tests are synthetic software verification. No historical accuracy can be inferred.

Verification this session: all five E1 tests, six experiment 05 tests and four
experiment 08 tests passed. Experiment 05 saved outputs/facsimile hashes and
experiment 09 saved outputs/supplied-draft hash reproduced. E1 freeze/sample
checks reproduced with `PYTHONHASHSEED=7919`. New Markdown local links resolve;
`git diff --check` passed. Experiments 05–09 remain byte-for-byte unchanged in git.
