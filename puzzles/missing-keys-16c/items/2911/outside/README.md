# Outside check for no. 2911 (stage 7): what broke

Written by the main thread on 2026-11-17 from the files an isolated Fable agent left here. That agent read the
period key (BNCF Carte Machiavelli VI/82, units 1–4) and was cut off by a usage limit before it wrote this file;
its scripts and outputs are complete as far as listed below. It did not write `calibration-note.md`.

**Sealed.** `truth.tsv`, `sheet-signs.tsv`, `decode-*.txt` and `name-evidence.tsv` hold sign values. No reader and
no agent that builds a key blind may open this folder. Scripts may score against it.

**Question.** The held-out test failed with a table of nulls. Was it the transcription, the plain side, or the aligner?

**Files.** `truth.tsv` (106 rows: sign → value, with the sheet cell and a match grade), `decode.py` → `decode-*.txt`,
`diagnose.py` → `diagnosis.tsv`, `uncovered-print.tsv`, `uncovered-consensus.tsv`, `reader-error.tsv`,
`doubles_check.py` → `doubles-check.tsv`, `keycheck.py` → `keycheck.tsv`. Run each script from this folder.

**Results** (`diagnosis.tsv`, cipher consensus against the 1877 printed text unless said).
- The true key gives a value to 99.5% of the tokens the readers read. The transcription is usable.
- The cipher is not a letter cipher: 53% of valued signs are syllables, 41% letters, 0.2% nulls; 1.67 letters
  per valued sign. It decodes to 4,619 letters. The printed plain text has 3,145.
- **41.7% of the cipher tokens have no counterpart in the plain text**, in 20 stretches, all but 18 tokens of
  them in the interior, the longest 626 tokens. Machiavelli's copy is an abridgement throughout, not a copy with
  a missing opening. Against the two readers' consensus plain text, 71.5% of the tokens are uncovered.
- **The true key itself scores 0.735** by the held-out scorer on the covered stretches, and 0.447 on the whole
  pair. The registered bar of 0.85 could not be met by any key on this pair.
- Readers: where one reader's token decodes against the print and the other's agrees with it, 1.8% (A) and 1.5% (B)
  of covered tokens. Reader error is small beside the other two causes.
- The sign guide under-split: its `g` covers four sheet signs, and the readers' `s` covers two (s and l forms).
  Doubled signs: the counts in `../results/doubles.tsv` are confirmed in kind (`doubles-check.tsv`).
- Registered check, for the record (`keycheck.tsv`): 0 of 26 `certain` values, 0 of 39 marked values and 0 of 56
  frequent sheet signs agree. The built table is all nulls.

**What broke.** The aligner, on an assumption the calibration never tested: that the two sides of a pair hold the
same text from end to end. Here two fifths of the cipher has no plain text, so two fifths of the signs must emit
nothing, and null becomes the best value for every common sign. The plain side is the second cause: even with the
true key the bar is out of reach. The transcription is not the cause.

**Limits.** One agent matched sheet shapes to guide names; 66 of 106 rows carry no caveat in the note column, the
rest are flagged there. The printed text has 36 restored line-starts. "Covered" is defined by `diagnose.py`'s
semi-global alignment, not by a reader.
