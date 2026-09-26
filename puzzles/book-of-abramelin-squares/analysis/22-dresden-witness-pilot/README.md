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
