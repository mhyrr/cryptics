# 25 — Blind test of the frozen recipe on Dresden N 111

**Result: the recipe holds.** Predictions computed from Mathers alone, frozen
before any of these manuscript pages entered the project, were scored once
against 119 squares of Mscr.Dresd.N.111. Symmetry predicts 88 % of missing
border letters, the vowel/consonant checkerboard 85 % of interior classes,
and no letter model beats the class mode's 25 %. All three pre-registered
forecasts fall inside their intervals. By the frozen rule in
[PROTOCOL.md](PROTOCOL.md): **recipe holds**.

## Order of freezes

| Commit | Frozen | Before |
|---|---|---|
| `8f1894d` | protocol, decision rule, forecasts, prediction hashes | any page was fetched |
| `242b08f` | image hashes of physical 246–297 | any page was located |
| `0c2ef61` | crop tool, scorer, 12 synthetic tests | any reading |
| `702450b` | locator inventory, crops, worklists | any reading |
| `7252fd2` | copyist addendum and its script | any reading was opened |
| `7c4a994` | raw readings A and B | scoring |
| `23e7b21` | the one scoring run | — |

The prediction files date from experiments 13, 20 and 24 and are checked by
hash at run time.

## Cohort

Four Opus locators found that Book IV ends on physical 272 (label 269), a red
"ENDE" after chapter 30 item 4; pages 273–297 are the register and subject
index. The cohort is 27 pages and **223 grids**, chapters 4 (item 5) to 30.
Two isolated Opus readers transcribed every grid: all 223 shapes agree, with
8,756 agreed letters, 3 conflicts and 37 cells either reader left unknown.
210 grids are n × n; 147 join a Mathers square by chapter and item under
experiment 20's gate; 119 of those have Mathers-blank cells to predict.
Of the 62 unjoined, 46 differ in size from the same-numbered Mathers square,
12 fail the letter gate, 3 are the copyist's unnumbered exemplar readings and
one has no Mathers counterpart.

## Primary result

| Measure | Forecast | Observed | 95 % interval (squares resampled) |
|---|---|---|---|
| M1 symmetry, border targets | 0.85 (0.75–0.95) | **0.883**, 571/647, 202 abstain | 0.817–0.940 |
| M2 checkerboard class, interior | 0.80 (0.70–0.88) | **0.854**, 1,475/1,728 | 0.816–0.892 |
| M3 class-mode letter, interior | 0.25 (0.18–0.35) | **0.252**, 435/1,728 | 0.224–0.279 |
| M3 palette (experiment 24) | — | 0.251, 434/1,728 | 0.224–0.279 |
| M3 chapter letter (experiment 20) | — | 0.197, 341/1,728 | 0.169–0.228 |
| M3 global letter | — | 0.175, 302/1,728 | 0.150–0.199 |

Interior target orbits: 723. The class is right in every target cell of 522;
the class-mode letter in every target cell of 123.

Given the true class, the class-mode letter is right on 523 of 1,728
interior cells (30.3 %). Experiment 16 measured 28.6–32.0 % inside Mathers.
The residue measured in one tradition predicts the other.

## Secondary tests, declared in the protocol

- **S1, seed alternation.** Where the Mathers seed alternates vowel and
  consonant at every step, the interior follows the checkerboard in
  1,021 of 1,055 cells (96.8 %); elsewhere 454 of 673 (67.5 %). Difference
  0.29, one-sided p 0.0002 over 118 squares. Kollatsch states the
  observation qualitatively (CLAIMANT, draft pp. 22–23); this quantifies it
  on a blind manuscript sample.
- **S2, palette against class mode.** 3 discordant orbits of 723; no gain.
- **S3, transmission (H24).** Mathers and Dresden differ on 64/876 top-row
  cells (7.3 %), 135/1,182 other border cells (11.4 %) and 173/798 interior
  cells (21.7 %). Interior excess with flags permuted inside each square
  pair: 173 against 99.7, p 0.0002.
- **S4, secondary join** (experiment 13's realignment): 168 joins; symmetry
  641/719, class 1,608/1,866, class-mode letter 474/1,866; recipe holds.
- **S6, J→I**: identical to the primary result.

## The correcting copyist (H28, addendum frozen at `7252fd2`)

Five squares appear twice: as the exemplar read ("ita stetit in libro",
"in libro legi") and as the copyist's correction ("Correctio mea"). On 12.4
he explains: "Hoc infra sequens ita stetit in libro quia sic non comparatum
putavi" — the grid below stood thus in the book; because I judged it not
properly composed, I corrected it above.

- **C1.** The correction has higher transpose agreement in 3 of 4 pairs with
  a difference (one-sided p 0.31; five pairs cannot do better than 1/32).
- **C2.** Three exemplars lack rows (5×7, 8×9, 7×8). In all three the
  copyist's added rows equal their transpose partners in **82 of 82** cells
  (forecast ≥ 0.8). He rebuilt lost rows by reading down the columns:
  symmetry completion by hand.
- **12.4, the cost of that method.** The exemplar's seed is MILCHAMAH,
  Hebrew "war", printed under *Krieg* in the 1595/96 dictionary
  ([scan 801](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=801));
  Mathers's top row is also MILCHAMAH. The exemplar had lost the fourth row,
  the row that starts with C. The copyist rebuilt it as EHACARIDA and
  changed the seed to MILEHAMAH: a C read as E, carried through a perfectly
  symmetric reconstruction. The dictionary, the French tradition and his own
  exemplar outvote him on the seed.
- **19.6** is a counter-case: the exemplar reading agrees with Mathers on
  26/26 shared cells, the correction on 22/26, with no gain in symmetry.

The copyist perceived the symmetry and used it. His corrections show no use
of the dictionary: symmetry repaired the structure and could not check a
misread letter.

## Limits

- Readers and locators are one model family (Opus 5.5). High agreement is
  not an adjudicated edition; errors shared by both readers are invisible.
- Readers may carry memory of printed Abramelin editions. They were told to
  transcribe literally; contamination cannot be excluded.
- Readers shared a scratchpad for image zooms. A reader reports overwriting
  zoom images; no transcription files were found there. Readers were told
  not to open each other's outputs; this was not verified at file access.
- One locator box (`p267-c1-g1`) framed the wrong grid; both readers noticed
  and read item 5 from the full page.
- Cells in a square are not independent; intervals resample squares.
- Dresden shares the German tradition with Warburg and Dehn's sources.
  Fresh access is not historical independence.
- The copyist's five pairs are the copyist's versions in the primary join
  where numbered. Reported, not removed.

## Files and reproduction

`COLLATION.md` is the readable double-keyed packet of all 223 grids.
`consensus.json`, `cells.json` (every scored cell) and `results.json` are the
scorer's output; `copyist-results.json` the addendum's.

```sh
cd puzzles/book-of-abramelin-squares/analysis/25-dresden-blind-test
python3 access.py --fetch      # restores the 52 pinned images to the ignored cache
python3 access.py --check
python3 crop.py --check        # needs the cache; crops are regenerated by crop.py
python3 test_score.py          # 12 synthetic checks
python3 score.py --check
python3 copyist.py --check
python3 collation.py --check
```
