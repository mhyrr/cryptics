# Cross-section of five: stage 1 result (2026-11-19)

**No candidate passes all four gates as written. Five cannot be chosen today.** 28 candidates were gated:
the 10 seeds, 15 more from the catalogue (importance 4–5, untaken, class A or B online) and 3 new ones from
DECODE, the Vatican, Venice and Simancas. Rows: `cross-section.tsv`. Scout notes and URLs:
`cross-section/scout-{A..F}.md`. Images: `../sources/cache/cross/<id>/` (gitignored).

## How the gates were run
- **Not taken:** 887 outside profiles fetched today (`fetch_profiles.py`), ids by `taken.py`
  (`taken-2026-11-19.tsv`), then a grep of the profiles by shelfmark and names. The grep found three targets
  that do not name their ids (`tranchedini1446`, `delacroix1797`, `hpbk1896`). An item worked in an active
  outside target counts as taken here, even when that target lists it as a gap (rule applied to 2339 and 2646;
  Greg's call to change it).
- **Readable:** `sign_height.py`, calibrated on no. 1336 c. 269r (11 px, readers 0.80) and no. 2351 (20–21 px,
  readers 0.91). Two script faults found by scouts and fixed (`8c44f3e`): JPEG comments in the PGM header,
  and dots between groups pulling the median down (`h_median_a30`). On 2554 the script over-reads: joined runs
  count as one component; ruled by eye on a native crop.
- **Buildable:** pair of 100 signs or more, or a neighbour key to hold, plus a second passage.

## Where they failed
| Gate | Count | Items |
|---|---|---|
| Not taken | 12 | 1556, 1554, 1561, 566, 1388 (read outside); 1308, 2630 (outside targets); 2839+2841, 881, new-juana1555 (published keys: known-key readings); 649, 2646 (active outside targets) |
| Matters | 2 | 2645 (a leftover group, not one cipher), 2405 (writers unknown, mixed hands) |
| Readable | 8 | 2946 (11 px), 2950 (13), 2945 (13), 2554 (by eye), 1392 (5–6), new-pallotto1628 (8), new-sega1579 and 1270 (images behind a login or a 403) |
| Buildable | 5 | 2339, 2939, 2395, 2575, 2577 |
| Conditional | 1 | 2854 |

What the outside repository already covers: 6 of the 10 seeds, and every AGS Estado record on DECODE. The
online class A items, the ones with a pair, are where both projects look first.

## The near misses, and what would move each
| Item | What it is | What holds it back | What would move it |
|---|---|---|---|
| **2946 + 2947** | Gianfrancesco Gonzaga to Cosimo de' Medici, 24 Jan and 31 Dec 1439 (ASF MAP XI) | 11 px at the server's native maximum (1272 px; info.json checked) | Accept the no. 1336 floor: clean, separate signs (crop seen), four or more readers and a vote merge. Pair about 4,000 glossed signs (2947, images 691–694); 2946 about 400 bare signs as the target. |
| **2854** | Ferdinand to John II, Seville, 9 Jun 1478 (DARA) | No pair. Rests on Tomokiyo 2018's Ferdinand–John II key of 1476–79 (Academia 403) | The paper. If its key reads the letter, a known-key reading; if partial, a neighbour key to hold. 30 px, about 2,200 signs. |
| **Sforza family G** (2405) | cart. 1597, 11 records | DECODE images need a login | A DECODE account: R5436 is said to be a clear leaf headed "da cifra"; if its cipher twin is R5440, R5442 or R5472–74, that is a pair. |
| **new-sega1579** | Madrid nunciature 1579, interlinear decipherment (AAV Spagna 22, DECODE R5624) | DECODE login; sender unverified | Same account; then check Lasry et al. 2020. |
| **1270** | Juan Manuel to the Catholic Monarchs, 1496–1519 (BNE) | BNE refuses scripts (403); Chrome not connected | A browser session on BNE Digital. Gate 1 is also thin. |
| **2339** | Card. Farnese, intercepted, Aug 1547 | Bare; outside target lists it as a gap | Build the Amanio key from cc. 70–71 and hold it on c. 78r. A fit is not expected (another correspondent). |
| **1392** | Trémais, Montréal 1759 | 5–6 px on the LAC server; Dudout has a partial key | ANOM's own scans; clear it with Dudout. |

## Recommendation
Take **2946 + 2947** now, with the readable floor lowered to 11 px for this item on the no. 1336 precedent. It
has the largest pair found, a short bare target, a 15th-century chancery not yet in the line, and it is not
in the outside repository. The caveat is real: on no. 1336 the 11 px leaf needed four readers to leave 10% of
places open, and this one has number groups that may be codes.

Then breach the access walls before a second scouting round: a DECODE account (Sforza G, sega1579),
Tomokiyo 2018 (2854), a browser on BNE (1270). A cross-section of five may exist behind those three doors. It
does not exist in front of them.

## Not checked
Cerioni 1970; Meister 1906 (HathiTrust, US only); Vito 2025's Capponi key table; DECODE's partly decrypted
Modena records (Costabili, Caprile, Beatrice d'Aragona); a direct PARES search; ANOM scans of C11A 104.
