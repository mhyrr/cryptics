# 19 — The dictionary entries, read on the page

**Result.** All 21 caption-selected seeds of experiment 14 stand on the
printed page. The OCR harvest holds about half of the transliterations that
the dictionary prints, so experiment 12's 56 exact seed matches undercount by
roughly a factor of two.

Protocol and worklist were committed before any crop was viewed
([PROTOCOL.md](PROTOCOL.md)). One Opus subagent read 50 crops. It saw the
crops and the OCR headword only.

## Hits: 21 of 21 confirmed

PRIMARY — Bayerische Staatsbibliothek, 1596 volume `bsb11762465`, scan numbers
linked. Crops of these entries are in `sources/caption-seed/experiment-19/`;
every crop's IIIF URL and sha256 is in `worklist.json`.

| Chapter | Mathers top row | Nominated headword | Scan | Transliterations printed in the entry |
|---:|---|---|---|---|
| 5 | CEPHIR | Löwe | [852](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=852) | arieh, labhi, laiisch, schachal, cephir, gur |
| 5 | NESER | Adler | [74](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=74) | nescher |
| 5 | PARAS | Reiter | [994](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=994) | rachabh, parasch |
| 5 | PETHEN | Schlange | [1049](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=1049) | nachasch, saraph, pethen |
| 8 | CANAMAL | Hagel | [651](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=651) | barad, chanamal, elgabisesch |
| 15 | BASAR | Fleisch | [470](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=470) | basar, scheer, lechem |
| 16 | SEGOR | Gold | [626](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=626) | dsahabh, betser, pads, cethem, segor, madhebhah |
| 18 | BUAH | Geschwür | [561](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=561) | schechin, buah |
| 19 | BETULAH | Jungfrau | [758](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=758) | almah, bethulah, naarah, ialdah, racham |
| 19 | CALLAH | Braut | [257](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=257) | callah |
| 19 | DODIM | Liebe | [839](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=839) | ahabhah, iedidath, rachem, dodim |
| 19 | IALDAH | Jungfrau | [758](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=758) | almah, bethulah, naarah, ialdah, racham |
| 19 | SARAH | Frau | [681](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=681) | gebhereth, gebhirah, sarah |
| 20 | SINAH | Feindschaft | [446](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=446) | ebhah, sinah, sitnah |
| 27 | ARIEH | Löwe | [852](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=852) | arieh, labhi, laiisch, schachal, cephir, gur |
| 27 | ATSARAH | Palast | [946](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=946) | chatser, atsarah |
| 27 | DOBERAH | Brücke | [265](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=265) | gescher, dobherah, raphsodah |
| 27 | ESAHEL | Baum | [160](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=160) | ets, siach, esahel, ascherah, edsrach |
| 27 | PERAC | Blume | [239](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=239) | perach, nets, tsits |
| 27 | REEM | Einhorn | [368](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=368) | reem |
| 27 | SELEG | Schnee | [1056](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=1056) | scheleg |

The square spelling is the printed word with its aspirates reduced: sch to S,
ch to C, bh to B, th to T (nescher NESER, chanamal CANAMAL, scheleg SELEG,
perach PERAC, dobherah DOBERAH). Experiment 14's skeleton tier already encodes
this. It is regular enough to be the compiler's habit. It is stated here as
an observation on 21 words, not as a tested rule.

## OCR gap sample: 30 entries drawn at random

| Quantity | Count |
|---|---:|
| Entries whose headword was found on the crop | 24 of 30 |
| Transliterations read on the page | 36 |
| of these, present in experiment 12's harvest | 15 (42%) |
| Missed words that match a top row of the label's own chapter | 0 |
| Missed words matching top rows of other chapters, per chapter | 0.034 |

Four of the 21 misses are words printed with an accent (náchal, péleg, dérech,
iggéreth), which the scorer's A to Z normalisation breaks; without them recall
is 19 of 36. Six locators pointed at a running head, not an entry: experiment
12's headword detection has that error rate, about one in five.

So "OCR gap" is a large class. With recall near one half, a complete reading of
the dictionary would be expected to raise the 56 exact seed matches towards a
hundred, which agrees with experiment 17's estimate from one-letter matches.
The sample found no new seed, which is unsurprising: 21 missed words from 15
entries are a small net.

## Limits

One reader, no second reading. The crops stop 650 px under the headword, and
four entries ran past the crop. Accents and line-break joins are recorded as
printed in `readings.json`.

## Reproduce

```sh
cd puzzles/book-of-abramelin-squares/analysis/19-image-reads
python3 make_worklist.py   # needs experiment 12's out/hocr; refetches crops into out/
python3 score.py           # needs only the checked-in files
```
