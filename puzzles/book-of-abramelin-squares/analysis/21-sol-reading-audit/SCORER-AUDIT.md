# Experiment 20 scorer audit

2026-09-21. Independent code audit. I did not inspect the experiment-21 Sol
readings or any image crop. I reproduced the frozen prediction check, all eight
preflight tests, and `score_checked.py . --check`; all passed. I also ran
read-only diagnostics against the checked-in experiment-20 transcriptions.

## Verdict

The published experiment-20 numbers reproduce. I found no defect that changes
the 349-cell frozen-alignment scores. The failed whole-packet gate does **not**
show that the print is illegible. It shows that 132 items did not satisfy the
scorer's square-layout model. The gate assigns zero agreements to every printed
position in those items without comparing their letters. It therefore combines
layout coverage and legibility in one number.

End state B is a frozen threshold result, not confirmation that interior
letters were historically free choices. The repository usually states this
limit correctly. It has not recovered or excluded a full generator.

## Correctness defects

### 1. The checked gate labels excluded layout as unreadable text

`score_checked.py:51-58` sends an item to `unscored_printed_positions` when
either row list cannot be coerced to an n by n grid. It then adds the larger
reader character count to the denominator. `score_checked.py:75-83` credits no
agreement for those characters. Thus 6,107 positions receive an assumed 0%
agreement even when both readers supplied the same row words.

This is not a conservative estimate of character legibility. It is a lower
bound that treats missing coordinate geometry as transcription failure. It
also counts `.` placeholders as potentially lettered because line 57 sums row
lengths rather than letters or non-placeholder glyphs. The protocol itself
distinguishes ragged geometry from readable top rows (`PROTOCOL.md:67-71`).

The post hoc diagnostic supports the narrower interpretation. Of 132 excluded
items, 123 are ragged in both readings and 110 have identical row-length
vectors. Those 110 contain 4,843 aligned string positions, with 4,640 agreed
letters (95.8%). This diagnostic is post hoc and cannot repair the frozen gate,
but it identifies the failed assumption: square coordinates, not readable
print.

Recommendation: keep the historical failure. In a new experiment, report two
separate measures: literal character agreement on row lists with identical
shape, and coordinate coverage for items that can be represented as grids.
Do not call the latter a legibility gate.

### 2. J-to-I normalization is not applied consistently in the checked gate

The frozen scorer normalizes J to I while loading every row
(`score.py:29-35`), as required by `PROTOCOL.md:75-81`. The checked wrapper
loads raw J and I (`score_checked.py:23-41`) and runs both gate implementations
on those unnormalized strings (`score_checked.py:72-74`). If readers choose
different symbols for the shared sort, the checked gate records a disagreement
that the historical scorer records as agreement.

The present files contain 83 J characters in reader A and 81 in reader B. A
diagnostic run with and without normalization produced the same aggregate gate
counts, so this defect does not change the published result. It remains a code
and protocol inconsistency.

Recommendation: normalize J to I once, before both gate calculations, while
preserving raw files and separately reporting the number of normalized
positions.

### 3. The original gate omits shared unknowns from its denominator

`score.py:68-74` defines a position as lettered only if either reader supplied
an alphabetic character. A `?/?` position is absent from both numerator and
denominator. The checked gate fixes this for regular grids
(`score_checked.py:62-68`). There are no shared unknowns in the present regular
items, so the correction has no numerical effect. This is a real defect in the
original implementation, already bounded correctly by the checked result.

## Alignment and denominators

The primary alignment code matches the frozen rule: same identifier and size,
then at least 50% agreement where Mathers and the consensus Warburg grid both
contain letters (`score.py:95-105`). Of 119 coordinate-bearing consensus grids,
33 pass. Model scoring then uses only prediction cells in those selected pairs
where the consensus Warburg value is a letter (`score.py:129-141`).

For the 33 primary pairs, experiment 13 supplies 375 interior prediction
positions. The scorer evaluates 349 letters, omits 11 reader disagreements
stored as `?`, and omits 15 printed or padded `.` positions. Border coverage is
158 of 179, with 3 unknown and 18 blank. The reported 288/349 class result and
81/349 best-letter result are correct conditional accuracies. They are not
coverage over every predicted cell. Calling all 349 cells "unseen" is also
about pre-freeze exposure, not statistical independence.

Pair selection uses agreement with Mathers on nonblank Mathers cells. The
models are scored on cells blank in Mathers, so the alignment gate does not
directly select on the scored outcome. It can still select the branch of the
tradition most similar to Mathers and exclude divergent or ragged material.
Report 33/119 pair coverage and the 349/375 cell coverage beside every primary
accuracy.

The post hoc realignment is less clean. It converts `?` to `.` and imports
experiment 13's matcher (`score.py:107-112`), whose denominator includes every
lettered Mathers cell (`13-dehn-witness-test/score.py:18-21`). Missing Warburg
rows therefore count as disagreements during selection. This is documented in
the code but differs from a plain "visible in both" rule. Keep realigned results
descriptive and subordinate to the frozen alignment.

## Interpretation limits

The B rule is implemented as frozen: at least 50 evaluated interior cells, all
tested letter models below 0.40, and checkerboard class accuracy at least 0.70
(`score.py:157-176`). It yields 349 cells, 0.232 and 0.825. The label `B
confirmed` overstates what those thresholds establish. It confirms only the
predefined operational branch among the tested models. It cannot prove free
choice, rule out another conditioning variable, or establish a historical
construction method. `score_checked.py:128-130`, `hypotheses.md:115-119`, and
`canon.md:17-20` state this correctly. Prefer "threshold B met" wherever the
short label appears.

The caption-to-seed result is strong evidence for same-number association in
this print: the code uses the print's own `(chapter, number)` keys and permutes
candidate sets within chapter (`18-german-captions/run.py:32-53`; imported at
`score.py:196-203`). It does not validate the interior-letter model. It also is
not an independent witness to the historical selection rule: captions and rows
come from one edition, nominations and lookup machinery predate this read, and
the Warburg print shares German-tradition ancestry with Dehn. The permutation
tests association under the observed candidate and chapter structure; it does
not test textual ancestry or editorial dependence.

The audit counts are checked in at `audit-scorer.json`. Reproduce them without
altering experiment 20:

```sh
cd puzzles/book-of-abramelin-squares/analysis/21-sol-reading-audit
python3 audit_scorer.py --check
```
