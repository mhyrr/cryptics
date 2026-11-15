# Calibration: the ranking against known outcomes

**Hindsight warning.** Every calibration entry was scored by someone who knew
how it ended. These checks catch gross errors in the formula; they do not
validate it. A rubric that passes them can still rank live entries badly.

Run `python3 scripts/calibrate.py`. It prints each check and exits 1 if any
fails. `--formula v1` scores the same entries with the formula before this
change, so the "before" column below can be reproduced.

## The test set

- **Solved** (`status = "solved"`), 16 entries: Copiale, Zodiac 340, Trithemius
  Book III, Poe/Tyler (the four TK-003 named), plus Bellaso challenges, Berg
  *Lyric Suite*, Chaocipher, Euler logogriph, Feynman ciphers, MacDonald
  telegrams, Marmont 1809, Mary Stuart letters, *Mene mene tekel*, number of
  the beast, Patterson–Jefferson, silk dress cryptogram.
- **Hoax or noise** (`likely-hoax`, `likely-noise`), 6 entries: Kensington,
  Oera Linda, *Le Serpent Rouge* (the three named), plus Flamel's
  *Figures hiéroglyphiques*, the Baconian Shakespeare ciphers, the Rilke
  cryptogram.

Noise cases sit with the hoaxes because the test is the same: there is no
intended meaning to recover, so no amount of compute should rank them above a
text that had one.

## The checks

| # | Check | Before (v1) | After |
|---|---|---|---|
| 1a | `attackable` ranks the 4 named solved cases above the 3 named hoaxes | PASS, margin +1 (Trithemius 23.5 vs Oera Linda 22.5) | PASS, margin +7.75 (23.5 vs 15.75) |
| 1b | `attackable` ranks all 16 solved above all 6 hoax/noise | **FAIL**, margin −5, 10 inverted pairs | PASS, margin +1.75 (*Mene mene tekel* 17.5 vs Oera Linda 15.75) |
| 2 | Solved cases score compute ≥ 4 and verifiable ≥ 4 | 10/16; 6 documented exceptions | unchanged (no scores changed) |
| 3 | Hoax/noise cases score solvable ≤ 2 | PASS, 6/6 | unchanged |

The ticket's own wording (check 1a) passed before any change, by one point.
It failed once the other solved and hoax entries were counted. The 10
inverted pairs under v1:

- Oera Linda (22.5) above Berg, Chaocipher, silk dress, *Mene mene tekel*,
  number of the beast.
- Baconian ciphers (20.5) and Rilke (19.5) above *Mene mene tekel* and number
  of the beast.
- Flamel (18.5) above *Mene mene tekel*.

Each inversion has the same cause. Under v1, `attackable` = mystery +
material + solvable + 2·compute + verifiable + ½·crowding. A hoax with ready
data and a mechanical test of the hoax hypothesis (Oera Linda: compute 4,
verifiable 4) collects those points in full. But compute and verifiable
measure how well you could attack a meaning, and they are worth nothing if
there is no meaning to find. The sum did not know that.

## The change

One formula change, in `scripts/rank.py`. No weight changed.

```
attackable = mystery + material + solvable
           + gate(solvable) · (2·compute + verifiable + ½·crowding)

gate(solvable) = 0 at solvable 1, 0.5 at solvable 2, 1 at solvable 3 or more
```

`classic` is unchanged. The maximum stays 32.5.

**Why a gate on these three axes.** `solvable` is the rubric's estimate that
a determinate meaning exists. The other three axes in the attack term are
conditional on that: how much computation could find it, whether you would
recognise it, how few people have looked. The honest expected value would
multiply them by the probability. A full multiplication would re-rank every
live entry, though, and the checks do not need that.

**Why this gate and not another.** Alternatives, run against the same data:

| Variant | 1b margin | Top-25 entries replaced | Top-25 positions changed |
|---|---|---|---|
| Multiply attack term by solvable/5 | +3.10 | 6 | 23 |
| Gate, 0.5 at solvable 2 (**chosen**) | +1.75 | 0 | 0 |
| Gate, 0.6 at solvable 2 | +0.40 | 0 | 0 |
| Gate, 0.75 at solvable 2 | −1.62 (fails) | 0 | 0 |

The chosen gate is the smallest change that passes with a clear margin, and
"doubtful" halving the attack term is easy to state. It leaves every entry at
solvable 3 or more exactly where it was.

**What the gate does not guarantee.** A hoax scored mystery 5, material 5,
solvable 2 and maxed on the other axes would reach 20.75, above the lowest
solved case. Check 1b exists to catch that; rerun it after scoring any new
calibration entry.

## Check 2: the six solved cases below 4

Check 2 asks whether the rubric would have rated the solved cases as
computational targets. Six fall short. None was re-scored. Each entry's
"Why the scores" section argues its score, and the arguments hold: these
cases fell to a document, a reading, or a consensus, not to computation, and
a calibrated `compute` should say so.

| Entry | Score | Why the lower score is right (from the entry) |
|---|---|---|
| Berg *Lyric Suite* | C2 V5 | Fell to an archival find: the annotated score Berg gave Hanna Fuchs, published by Perle in 1977. Fifty years of analysis of the notes produced nothing. |
| Chaocipher | C3 V5 | Verification was mechanical, but the hypothesis space was not enumerable. The system fell when Byrne's papers were donated in 2010. |
| Silk dress cryptogram | C3 V5 | A one-part code on dictionary words has no letter statistics to attack. It fell to a search of digitized codebooks (SWEEP), not key fitting. |
| *Mene mene tekel* | C1 V3 | Four words; a philological problem settled by scholarly consensus. The bottom anchor of both axes. |
| Number of the beast | C2 V4 | The gematria space is trivially enumerable; nothing is left for computation to decide. Verifiable 4 passes. |
| Trithemius Book III | C3 V5 | Fell to human reading of the number tables (Ernst 1996, Reeds 1998). See the open question below. |

The script holds these as named exceptions with their reasons. Check 2 fails
if a solved case misses the bar without an exception, or if an exception
starts passing and its reason goes stale.

The lesson for the rubric, recorded in TK-003's notes: `compute` must ask
whether the hypothesis space is enumerable, not only whether the data is
digitized and a check exists. `rubric/COMPUTE-MODES.md` carries that field
(`space`) for live entries.

## Re-scores

None. No entry's scores changed in this pass.

## Open questions

- **Trithemius compute.** The rubric defines `compute` forward-looking: "what
  a well-run 2026 effort could do." The entry scores it by what actually
  solved the case in the 1990s. A 2026 effort would probably attack the
  number tables statistically, which argues for 4 or 5. Re-scoring it would
  not change any check result, so it is left for Greg to decide which reading
  of the axis the calibration entries use.
- **Man'yōshū poem 9** (TK-003 observation 3): material 2 against compute 5,
  a tiny target with a large supporting corpus. Not a calibration case and
  not touched by the gate (solvable 5). Still open.
- **Beale ciphers** fall from 58 to 105 because the entry scores solvable 2.
  The gate makes that score matter a lot more than it did. The 13 live
  entries at solvable 2 now rank 104–118; their `solvable` scores deserve a
  second look before anyone relies on the lower half of the list.

## Effect on the live ranking

The top 25 by `attackable` is identical, entry for entry and position for
position. Only the 13 live entries at solvable 2 move:

| Entry | Rank before → after | Attackable before → after |
|---|---|---|
| Beale ciphers | 58 → 105 | 21.5 → 14.75 |
| Liber Loagaeth | 66 → 104 | 21 → 15 |
| Tianwen | 80 → 106 | 19.5 → 14.25 |
| Nostradamus, *Prophéties* | 81 → 108 | 19.5 → 13.75 |
| Piers Plowman prophecies | 91 → 109 | 18 → 13.5 |
| Rimbaud, "Voyelles" | 108 → 110 | 15.5 → 12.25 |
| Cad Goddeu | 109 → 111 | 15.5 → 11.75 |
| Publius enigma | 111 → 114 | 14.5 → 10.75 |
| Blitz ciphers | 112 → 115 | 14.5 → 10.25 |
| Europa Redux manuscript | 113 → 116 | 14.5 → 10.25 |
| Mallarmé, "Sonnet en -yx" | 115 → 113 | 12.5 → 10.75 |
| Ricky McCormick notes | 116 → 117 | 12.5 → 9.25 |
| Tamam Shud code | 118 → 118 | 9.5 → 7.75 |

As these drop, 48 entries at solvable 3 or more move up by 1 to 7 places,
all below rank 57. Their scores do not change. The largest move is the
Dorabella cipher, up 7.
