# 11 — Caption-first lexical test (E2)

**The pilot produced no evidence for a caption selector.** Eight source-backed
German captions yielded eleven frozen lookup nominations. Seven captions align
by purpose with Mathers labels; three aligned targets are complete. E2 predicts
none of their hidden interior letters because none receives a usable lexical
domain. The controls ran; they do not rescue the missing input. This is an
uninformative pilot, not a rejection of dictionary derivation.

The [results](RESULTS.md) distinguish failed retrieval, disallowed spelling,
incomplete targets, unmatched captions, and model contradictions. No target was
replaced. No square reconstruction or independent witness validation is claimed.
Experiment 10's E1 and its dictionary sample remain unchanged.

## Order of work

1. Wrote [PROTOCOL.md](PROTOCOL.md) and [policy-freeze.json](policy-freeze.json)
   before reading this pilot's captions. Fixed eight consecutive captions from
   German Book IV chapter 5, at most two lookup concepts, and central-row/T
   placement. This is a stipulated candidate, not an historical instruction.
2. Acquired the PRIMARY [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf),
   catalogued as Stuttgart 1853. OCR located captions on PDF pages 339–340.
   Inspected only the pilot's caption crops. Their German wording, context,
   crop coordinates and hashes are in [captions.json](captions.json).
3. Wrote all [nominations](nominations.json), with phrases, reasons, operations
   and unused alternative slots. Saved [selection-freeze.json](selection-freeze.json)
   before dictionary entries or target sizes were inspected.
4. Ran bounded exact/prefix dictionary searches and checked twelve full images.
   Preserved all relevant printed Hebrew-gloss Latin transliterations in five
   retrieved entries, including three spelling-excluded joins. Six lookups
   remain unresolved, not established dictionary absences. The immutable
   [lexicon](lexicon.json) and [freeze](lexicon-freeze.json) preserve these limits.
5. Independently aligned caption meanings to the familiar-spirit chapter's
   English purpose list in the mediated PRIMARY [Mathers transcription](https://www.esotericarchives.com/abramelin/abramelin.htm).
   German 2/3/4/5/6/7/8 align to Mathers 5/8, 5/3, 5/9, 5/4, 5/10, 5/5, 5/11.
   The German giant remains unmatched. These are purpose-label alignments, not
   assertions that the underlying square texts are identical or correctly placed.
   See [alignment](alignment.json) and its [freeze](alignment-freeze.json).
6. Tested the evaluator on synthetic data, then froze code, dependencies, masks,
   controls and source hashes in [evaluation-freeze.json](evaluation-freeze.json).
   Preparation alone reads the full corpus and produces masked tasks. The pure
   predictor receives one masked task at a time. No semantic choices are made
   after this point. Each scored group is wholly hidden from that predictor.
7. Wrote per-cell predictions and branch/completion records, then saved
   [prediction-freeze.json](prediction-freeze.json) before invoking the separate
   scoring stage. Hidden answers stay in a gitignored local cache. The checked-in
   [results](results.json) retain per-target/fold/mask errors and abstentions.

These are timestamped local hash records, not third-party preregistration.
Exact temporal sequence comes from the tool record. All Mathers targets already
have project-level exposure. Source-extraction mistakes exposed neighboring
German rows and some non-scored Mathers seed commentary; [EXPOSURE.md](EXPOSURE.md)
records them. **Do not call the session blind.** No German pilot-square letters
were displayed or used to choose nominations.

## What the narrow policy cost

The retrieved forms `Kriegsman`, `Alter man`, and `Reuter` need n/nn or ei/eu
equivalence to join the chosen German lookup labels. Those operations were not
frozen, so the joins stay excluded. The -gestalt compounds stay whole. A missed
second nomination blocks the whole caption; dropping it could create false
consensus. The flower entry has no eligible seven-letter form and its aligned
target is incomplete in any event.

The noun nomination `Blume` from historical `Bluemen` also deserves a stricter
annotation audit: its recorded inflection operation does not separately log the
historical ue/u change. That is a policy ambiguity in this development pilot.
It affects no scored caption prediction (the flower target is incomplete), but
the flower entry contributes to the caption-free pool and positional baseline.
Do not promote those baseline matches as clean confirmatory evidence. A future
procedure must make this spelling distinction explicit before nominations.

The useful next step is a new frozen policy for **German headword lookup**,
tested on new captions. This need not relax spelling of the printed Hebrew
transliterations. Keep that distinction explicit. Do not revise E2 to fit its
now-exposed dictionary entries or targets.

## Reproduce

Python standard library only. No network, PDF renderer or OCR is needed to
reproduce selection gates, masks, predictions and scoring. The scored input is
the existing pinned Mathers corpus, not Warburg square letters.

```sh
python3 -m unittest discover -s puzzles/book-of-abramelin-squares/analysis/11-caption-first-e2 -p 'test_*.py' -v
python3 puzzles/book-of-abramelin-squares/analysis/11-caption-first-e2/evaluate.py prepare
python3 puzzles/book-of-abramelin-squares/analysis/11-caption-first-e2/evaluate.py check
python3 puzzles/book-of-abramelin-squares/analysis/11-caption-first-e2/report.py --check
python3 puzzles/book-of-abramelin-squares/analysis/10-caption-selector/audit.py --check
```

`prepare` recreates the ignored answer cache after a fresh clone; it refuses to
overwrite differing artifacts. `check` recomputes all stages and compares saved
bytes. A changed frozen file fails verification. The four new tests check whole
group masks, preservation of unresolved alternatives, planted caption signal
versus ambiguous caption-free words, and orbit-control invariants. They verify
software, not history. Caption-free frequency ties abstain.

To reconstruct the caption crops, retrieve the PDF URL/hash in `captions.json`
and use Poppler at 240 dpi with each recorded crop box. Do not render uncropped
square pages into a selection context. OCR was a locator, never the source of
the final caption transcription. The checked-in crops and dictionary images
are the readable source evidence; see their [provenance](../../sources/caption-first-e2/README.md).
