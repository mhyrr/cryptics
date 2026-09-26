# 22 — Dresden N 111 manuscript pilot

**Access acquired 2026-09-21; analysis resumed 2026-09-26.** SLUB's public
OAI-PMH response supplies 302 physical image records for Mscr.Dresd.N.111.
The cover and the three selected manuscript pages downloaded successfully.
The viewer challenge is no longer an access barrier for this witness.

PRIMARY — [manuscript record](https://digital.slub-dresden.de/id364474017),
[published open-data interface](https://www.slub-dresden.de/mitmachen/open-source-open-data).
The unchanged metadata and acquisition details are in
[sources/dresden-n111](../../sources/dresden-n111/README.md).

## Frozen pilot and first result

Commit `8d25cfa` froze physical pages 243–245 (source labels 240–242), source
hashes and the existing experiment-13/20 predictions before any square image
was inspected. Two fresh Sol agents independently transcribed these pages.
They saw no other witness, prediction or each other's output. The selection
was a consecutive opening packet, not a random sample. It has not expanded.

The frozen comparison uses physical page and each reader's grid index. Both
readers returned 22 items, but only 10 paired items have the same shape:
304 agreed letters out of 397 comparable positions, 92 conflicts and one
unknown. One Mathers join passes, with **zero missing-cell predictions**.
These are transcription/identification results, not a negative model test.

Inspection of the raw records reveals a protocol defect: “top-to-bottom” did
not specify how to traverse a page with several columns. Reader A traversed
across parts of the page; reader B followed the source numbering down columns.
Reader A also assigned chapter 4 to the opening chapter; reader B assigned 1.
Consequently, many equal grid indices refer to different source objects.
Do not interpret the initial agreement fraction as manuscript legibility.

`readings-A.json` and `readings-B.json` retain these mistakes. `results.json`
and `collation.json` preserve the first comparison. The latter is an audit of
the original pairing, not a text ready for reuse. A separate source-only
locator audit and explicitly post hoc alignment address this defect; they
must not silently replace the primary result or become a fresh blind test.

## Reproduce the frozen result

From the repository root:

```sh
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/access.py --fetch
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/access.py --check
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/test_score.py
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/score.py --check
```

`--fetch` restores only the cover and the three frozen pages from pinned
metadata. It does not open or download any other manuscript page. Source
images are in the ignored cache; their SHA-256 hashes are checked. Six focused
scorer tests cover unknown truth, source identifiers, incomplete grids and
letter/class predictions. The original XML retains its original whitespace.

Fresh project access does not establish independence of manuscript ancestry
or absence from model training. No result here proves historical free choice.

## Source-keyed collation, 2026-09-26

A third fresh Sol agent inspected only the three images and their manifest.
It identified Book IV, chapters 1–4, and established traversal down each
column before moving right. Its [locator audit](LOCATOR-AUDIT.md) and the
explicit A/B key map (`alignment.json`) were committed as `c68d901` before
the corrected comparison ran. No source letter was changed. The map is based
on chapter headings, item numbers and source regions, not letter similarity.

All 22 mapped grids have matching row-length vectors. There are **926 agreed
letters / 935 comparable positions**, eight conflicts and one unknown.
Literal and J-to-I totals agree. Two grids have agreed uneven row lengths;
they remain row lists and are excluded from square-coordinate scoring.
`posthoc-collation.json` retains all 22 objects, both raw records, the source
region and image hash, and both literal values at every comparable position.
Agreed readings remain same-model consensus, not an adjudicated edition.
The generated [reading packet](COLLATION.md) displays every consensus row,
uncertain position and source-image link for review.

The unchanged same-number Mathers gate admits ten grids. Only **4/2 (ETHANIM)
and 4/3 (APPARET)** contain frozen missing-cell targets: 36 each, all 72 with
agreed Dresden letters. The other twelve source grids remain excluded, with
reasons recorded; shifted chapter numbering and shape differences are not
repaired by searching for a better Mathers match.

| Frozen prediction | Correct | Wrong | Abstain |
|---|---:|---:|---:|
| Symmetry, border | 22 | 0 | 0 |
| Symmetry, interior | 0 | 0 | 50 |
| Vowel/consonant class, interior | 27 | 23 | 0 |
| Class-mode letter, interior | 11 | 39 | 0 |
| Chapter letter, interior | 11 | 39 | 0 |
| Global letter baseline, interior | 10 | 40 | 0 |

No model recovers every missing letter of either grid. Per-grid outcomes and
TA-orbit target coverage are in `posthoc-results.json`. Orbit counts group
the frozen target positions; they do not make those letters independent
trials. The class result is substantially weaker here than in the aggregate
Dehn/Warburg cohorts. These two neighbouring grids do not estimate a corpus
rate or prove a historical construction process.

The independent audit splits orbit coverage by region in `audit-scorer.json`:
12 border target orbits and 18 interior target orbits. Symmetry gets all 12
border orbits and abstains on all 18 interior orbits. Class is correct across
4/18 complete interior target orbits; class/chapter letters across 2/18;
the global baseline across 3/18. Neither cell nor orbit counts are independent
trials. Run `audit_scorer.py --check` to reproduce the audit.

Despite reaching 50 evaluated interior positions, this is **post hoc source
alignment, with no confirmatory A/B verdict**. The primary zero-target result
is retained. The corrected packet provides manuscript readings for collation
and a diagnostic for the next, untouched packet. It does not prove either a
complete generator or free letter choice.

```sh
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/test_posthoc.py
python3 puzzles/book-of-abramelin-squares/analysis/22-dresden-witness-pilot/posthoc.py --check
```

The five mapping tests reject omissions, reused records and cross-page joins,
and check that alignment changes preserve letters and uncertainty. The code
also requires complete coverage of the source-only locator inventory and
checks pinned raw-reading, locator, prediction, image and Mathers hashes.
See [SCORER-REVIEW.md](SCORER-REVIEW.md) for the independent Sol review of the
preserved first comparison and the limits of its checks.
