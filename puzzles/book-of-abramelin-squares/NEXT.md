# NEXT — handoff for the next session

**Last session:** 2026-09-17
**Where it stopped:** dictionary identified; experiment 05 source audit,
protocol and synthetic completion machinery checked in. Historical scoring
is blocked, not completed or failed. H7 and new H12 remain open.

## Do first

1. Read `analysis/05-period-dictionary/SOURCE-AUDIT.md` and `PROTOCOL.md`.
   The source is Decimator/Schindler/Palthenius, Frankfurt Basse,
   *Sylvae quinquelinguis* 1595/1596, part I, A–S plus T–Z. Do not substitute
   the proper-name part II or a later Leipzig dictionary.
2. Obtain legible title and entry images from the identified scans:
   [1596 A–S](https://www.digitale-sammlungen.de/de/view/bsb11762465) and
   [1595 T–Z](https://www.digitale-sammlungen.de/en/view/bsb10314207).
   Google Books IDs `jkY8AAAAcAAJ` and `LPyVAQ1q89cC` are alternative 1596
   digitizations. Catalogue metadata was accessible; actual pages were not.
   The six exact headword targets are in `claims.json`. Check neighbouring
   alternatives and entry boundaries, not just the desired word. An earlier
   comparison edition is needed for the alleged edition-specific error.
3. Transcribe a preselected contiguous entry block independently of target
   square letters. Preserve raw readings, uncertainty and normalization logs.
   `claims.json` is exposed claimant material, **not an independent lexicon**.
4. Freeze a justified interior placement and caption mapping before scoring.
   The next experiment is fixed interior lexical placement under whole-orbit
   masking. Separate seed recovery from independent inner-letter recovery.
   Do not assume every row is a word, or allow free insertion/deletion.
5. Run the declared Mathers comparisons only after the source gate passes.
   The 81 complete grids remain **internal evaluation**, not blind validation.
   Keep ambiguity, contradictions, misses and abstentions in the denominator.
6. Only if the method survives, freeze incomplete-square predictions before
   opening new uncorrected German targets. Audit exposure, editorial changes,
   caption/seed alignment and witness ancestry first.

## What exists

- Experiments 01–04 and source corpus are unchanged. Frame fitting remains a
  tool for scattered blanks; fragments and recurrences have not supplied a
  reliable independent-letter construction. See `STRESS-TESTS.md`.
- Experiment 05 enumerates fixed-path lexical constraints with symmetry and
  explicit residual orbit domains. It recovers nine planted inner letters;
  an alternative word leaves two completions and one abstention. The seed-only
  toy has 456,976 completions. These are software checks, not historical scores.
- Six tests pass. `run.py --check` reproduces both outputs under a different
  Python hash seed. Run commands and boundaries are in the experiment README.
- The new source discovery exposed edition Book IV pp. 138–142, including
  variants. Treat all examples in the retrieved symmetry draft as exposed too.
  No new raw German witness was read. No historical predictions were issued.

## Named wall

We lack **readable, edition-identified dictionary entry images and an
independently justified rule placing lexical material inside the square**.
The first prevents primary verification and independent lexicon extraction;
the second prevents a test of inner letters from being quietly replaced by
seed recognition. The accessible scholarship gives correspondences, not a
complete deterministic recipe. Source-access failures are logged, not inferred
absence of scans. Shell curl was rejected even on its escalated retry; do not
route around that policy restriction with another shell client.

Historical validation separately still needs the Mathers print audit and raw
German witnesses. Retain the prior audit queue: ten excluded layouts, label
25/4 among chapter 24, and frame-model disagreements. Dresden N 111's viewer
previously challenged the web tool; HAB facsimiles remain unresolved. A modern
corrected edition cannot stand in for uncorrected witness truth.

No source request or purchase was made. No failure or missing input here is
evidence that the text is random. TK-005 remains open.
