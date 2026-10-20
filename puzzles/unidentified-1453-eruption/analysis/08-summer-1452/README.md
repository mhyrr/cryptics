# 08 — Summer 1452

**Question.** Was summer 1452 already cool anywhere in the NH tree-ring
network? A high-latitude NH eruption in spring or early summer cools the
same summer (Laki, June 1783; Novarupta, June 1912). A tropical eruption, or
any eruption after the growing season, should not. So the 1452 response
bounds the eruption season, and the 1452 site pattern may hint at a region.
Bears on README criteria 2 and 5 and on H2, H3, H5, H6.

## Pre-registration (written 2026-10-20, before any 1452 value was computed)

What I knew when I wrote this: 04's results (1453 is the response year in
every dataset; 1454 reverses; the per-site 1453 pattern), and 02's ice window.
I had not computed or looked at any 1452 anomaly, in any dataset. 04's
`classify` output lists the reference years 1443–1452 for 1453 but not the
1452 values.

**Datasets.** As in 04, and parsed by 04's code (imported from
`../04-cooling-fingerprint/fingerprint.py`).
- *Primary:* Schneider 2015 MXD, 14 sites (Zha excluded), coordinates from
  Esper 2017 Table 1 (`../04-cooling-fingerprint/sites_schneider2015.tsv`).
- *Replication:* N-TREND2015 site records (53 usable), coordinates from the
  NOAA metadata (box centre).
- The N-TREND 2017 grid is not used. It is interpolated from the same N-TREND
  sites and needs the netCDF environment.

**Calibration events.** `events.tsv`. Every NH-relevant eruption with a
verified climactic month and enough sulfur to matter. Season classes: early =
climax in January–June of year E, late = July–December. Four classes:
XE (extratropical, early), XL (extratropical, late), TE, TL. Zavaritskii 1831
("spring–summer", straddles the split) and Samalas 1257 (month from ice core
only) get no class. Their numbers are printed but enter no test.

**Anomaly.** 04's definition, unchanged. Per site: value(Y) minus the mean
of E−10 … E−1, leaving out [E′, E′+2] for every other eruption in the
exclusion list (eVolv2k VSSI ≥ 3 Tg S plus every event in `events.tsv`).
At least 5 reference years. Divided by the site's interannual SD
(SD of value − centred 11-year running mean, 1250–1990).

**Statistics.**
- M_E = network-mean standardized anomaly in the eruption year E.
- M_E1 = the same for E+1.
- N_E = count of sites with z ≤ −1 in E, and its share of sites.
- **Background.** M for every year Y in 1260–1990 with no exclusion-list
  start in [Y−2, Y], computed the same way with E = Y. Each calibration and
  target value gets its percentile in this background.

**Tests on the calibration set.**
- P1 (primary): XE events have lower M_E than all other classed events.
  AUC = P(M_E(XE) < M_E(rest)); one-sided permutation p over class labels,
  10 000 permutations, seed 1453. Leave-one-out: threshold on M_E chosen to
  maximize balanced accuracy (04's `best_threshold`), applied to the held-out
  event; LOO balanced accuracy with permutation p.
- P2: XE versus TE alone (the season-matched comparison), AUC and
  permutation p.
- Descriptive: class medians of M_E and M_E1; count of events per class with
  M_E below the background 10th percentile ("cooled in E").
- Sensitivity: Parker as 1641, early; VSSI ≥ 3 Tg S only (drops Hekla 1766
  and Katla 1755; keeps events with no eVolv2k estimate).

**Target.** UE 1453. Reference years fixed at 1442–1451 (the ten years
before the earliest year 02 allows, early 1452). Report M, N and per-site z
for 1452, 1453 and 1454 against this one reference, with background
percentiles.

**Decision rule for 1452.** For each class c, k_c = number of class events
whose M_E is ≥ M_1452 (as warm as 1452, or warmer), and
p_c = (k_c + 1)/(n_c + 1).
- If M_1452 is above every XE value (k = 0), "Jan–Jun 1452, extratropical"
  is *disfavored*. Same for TE and "Jan–Jun 1452, tropical".
- If M_1452 is below the background 10th percentile, 1452 counts as
  *cooled*. Then "eruption after June 1452" is disfavored for both classes
  (a summer before the eruption should look like background), unless the
  late classes' E-year values reach as low.
- Otherwise 1452 counts as *normal*, and every class stays allowed in 1452.
- With five events in a class, p_c cannot fall below 0.17. A "disfavored"
  is therefore weak. It is written as a bound, not a refutation.

**Decision rule for 1453.** If M_1453 is below every background year, then
an eruption after June 1453 is disfavored for both classes (the summer before
the eruption cannot be the coldest one). `window.py` intersects these
verdicts with 02's ice windows (extratropical analogues 1452.9–1453.7,
tropical 1452.0–1453.1) and prints the arithmetic. Season boundaries are
1452.0, 1452.5, 1453.0, 1453.5.

**Regional pattern (step 5).** For 1452 and 1453, per-site z with
coordinates, both datasets.
- Moran's I with binary weights (great-circle distance < 2000 km), two-sided
  permutation p (10 000 shuffles of z over sites, seed 1453).
- Sector test: sites grouped by longitude into North America (−170 to −50),
  Europe (−20 to 40), Urals–West Siberia (40 to 100), East Asia–Siberia
  (100 to 180). Statistic: the lowest sector mean (sectors with ≥ 2 sites).
  One-sided permutation p: share of shuffles whose lowest sector mean is ≤
  the observed one.
- A regional cluster is reported only if p < 0.05 in the primary dataset and
  the same sector is lowest in N-TREND. Otherwise "no cluster detected".
- Calibration (rule 7): the same sector test on the E-year (XE) or the
  response year chosen as in 04 (others) of every classed event, reporting
  whether the lowest sector contains the source longitude.

**Secondary (step 6).** Up to ~6 fetches for frost-ring or light-ring
records covering 1452–1454. Report what exists. No analysis.

## Deviations

- The `--vssi3` sensitivity was registered for the calibration. After the
  first target run I also passed it through the 1452 decision rule
  (`results/target_schneider_vssi3.txt`). It is labelled as a sensitivity.
- `frostrings.py` (step 6) ranks years in the Colorado frost-ring table. That
  ranking was not pre-registered. It is descriptive.
- `summer.py` sets `sys.dont_write_bytecode` so importing 04's code leaves no
  `__pycache__` in 04's folder. No number changed.

## Run

```
D=../04-cooling-fingerprint/data; S=../04-cooling-fingerprint/sites_schneider2015.tsv
python3 -I summer.py calibrate schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab > results/calibrate_schneider.txt
python3 -I summer.py calibrate schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab --parker1641 > results/calibrate_schneider_parker1641.txt
python3 -I summer.py calibrate schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab --vssi3 > results/calibrate_schneider_vssi3.txt
python3 -I summer.py calibrate ntrend $D/ntrend2015tr.txt $D/ntrend2015-RecordsUsed_Metadata.txt events.tsv $D/evolv2k_v4.tab > results/calibrate_ntrend.txt
python3 -I summer.py target schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab > results/target_schneider.txt
python3 -I summer.py target schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab --vssi3 > results/target_schneider_vssi3.txt
python3 -I summer.py target ntrend $D/ntrend2015tr.txt $D/ntrend2015-RecordsUsed_Metadata.txt events.tsv $D/evolv2k_v4.tab > results/target_ntrend.txt
python3 -I summer.py regional schneider $D/schneider2015mxd.txt $S events.tsv $D/evolv2k_v4.tab > results/regional_schneider.txt
python3 -I summer.py regional ntrend $D/ntrend2015tr.txt $D/ntrend2015-RecordsUsed_Metadata.txt events.tsv $D/evolv2k_v4.tab > results/regional_ntrend.txt
python3 -I window.py results/target_schneider.txt results/target_schneider_vssi3.txt results/target_ntrend.txt > results/window.txt
python3 -I fetch.py data/          # frost-ring files
python3 -I frostrings.py data/colofrlr.txt > results/frostrings.txt
```

Each `calibrate` run takes about 15 s; `regional` about 1 min. Standard
library only. 04's data files are read in place.

## Calibration months

Months are the month of the climactic phase. Each was checked against two
sources where possible: eVolv2k v4 (PRIMARY dataset) and the GVP table cached
in `sources/cache/` (SECONDARY). Details are in `events.tsv`.

- **Kept, extratropical early (XE):** Veiðivötn Feb 1477, Hekla Apr 1766,
  Laki Jun 1783, Sheveluch Feb 1854, Novarupta Jun 1912.
- **Kept, extratropical late (XL):** Tarumae Sep 1667, Shikotsu Aug 1739,
  Katla Oct 1755.
- **Kept, tropical early (TE):** Colima Jan 1585, Ruiz Mar 1595,
  Huaynaputina Feb 1600, Gamkonora May 1673, Tambora Apr 1815, Cosigüina
  Jan 1835, Agung Mar 1963, El Chichón Apr 1982, Pinatubo Jun 1991.
- **Kept, tropical late (TL):** Parker Dec 1640, Makian Dec 1861,
  Krakatau Aug 1883, Santa María Oct 1902.
- **No class:** Zavaritskii 1831. eVolv2k gives 1 July, which looks like a
  default. The Hutchison 2025 abstract puts the shards in "summer 1831";
  press releases say "spring–summer". It straddles the split. Samalas 1257:
  the month is ice-core-derived in GVP.
- **Single-source months:** Sheveluch, Novarupta, Santa María (GVP only).
  Agung, El Chichón and Pinatubo climaxes come from 02's sources. All three
  sit in January–June whether the GVP start or the climax is used.
- **Boundary case:** Parker. GVP and eVolv2k both start it on 26 Dec 1640.
  The loudest blasts were on 4 Jan 1641 (Wikipedia, SECONDARY). The
  sensitivity run moves it to January 1641.

## Result

**1. The eruption-year summer does not separate season or class.**
(`results/calibrate_*.txt`.) Background: 606 years, 10th percentile
M = −0.55 (Schneider) and −0.46 (N-TREND).

| Class | n | median M_E (Schneider) | cooled in E | median M_E (N-TREND) | cooled in E |
|---|---|---|---|---|---|
| XE | 5 | −0.21 | 2/5 (Laki −1.71, Novarupta −1.22) | −0.34 | 2/5 |
| XL | 3 | −0.12 | 1/3 (Tarumae −1.15) | −0.02 | 1/3 |
| TE | 9 | −0.38 | 2/9 (Colima, Cosigüina) | −0.07 | 2/9 |
| TL | 4 | −0.03 | 1/4 (Santa María) | +0.10 | 0/4 |

- P1, XE versus the rest: AUC 0.56, permutation p 0.36 (Schneider);
  AUC 0.61, p 0.25 (N-TREND). LOO balanced accuracy 0.57 (p 0.37) and
  0.58 (p 0.34).
- P2, XE versus TE: AUC 0.53, p 0.44 (Schneider); 0.58, p 0.35 (N-TREND).
- Sensitivities: Parker as early 1641, AUC 0.54, p 0.42. VSSI ≥ 3 Tg S
  (drops Hekla 1766 and Katla 1755), AUC 0.68, p 0.15.
- Laki and Novarupta cool their own summer, as expected. Veiðivötn
  (−0.21), Hekla (+0.54) and Sheveluch (+0.13) do not. Tarumae's summer of
  1667 was cold (−1.15) although the eruption came in September. A
  pre-eruption summer can be cold by chance.

**2. Summer 1452 was normal.** (`results/target_*.txt`, reference 1442–1451.)

| Year | Schneider M | percentile | sites ≤ −1 | N-TREND M | percentile | sites ≤ −1 |
|---|---|---|---|---|---|---|
| 1452 | +0.30 | 73 | 0/14 | −0.25 | 24 | 8/36 |
| 1453 | −2.01 | 0 (below all 606) | 12/14 | −1.69 | 0.3 (2 of 606 lower) | 26/36 |
| 1454 | −0.53 | 11 | 6/14 | −1.19 | 1.0 | 22/36 |

- Schneider: 1452 is warmer than 4 of 5 XE values. Only Hekla 1766
  (2.5 Tg S, +0.54) is warmer, so "Jan–Jun 1452, extratropical" stays
  allowed under the rule (p = 0.33). Without Hekla (VSSI ≥ 3), 1452 is warmer
  than every XE event, and the rule says *disfavored* (p = 0.20).
- 1452 is warmer than 8 of 9 TE events. Jan–Jun 1452, tropical, stays
  allowed (p = 0.20). In N-TREND, 1452 sits mid-class for both.
- 1452 is not cooled, so the summer gives no case against a late-1452
  eruption.
- 1453 is below every background year in the primary network. Under the
  rule, an eruption after June 1453 is disfavored. In N-TREND two background
  years are lower, so the rule does not fire there.

**3. Timing window.** (`results/window.txt`.) 02's ice windows intersected
with the summer verdicts:
- Extratropical: 1452.9–1453.7 becomes **1452.9–1453.5** (primary). The
  upper bound moves because 1453 was cold. The lower bound is 02's. The
  1452 summer removes nothing that 02 had not already removed.
- Tropical: **1452.0–1453.1**, unchanged.
- N-TREND: no change to either window.

The summer evidence adds one thing. It moves the extratropical upper bound
from mid-1453 to the end of June 1453, and that rests only on 1453 being the
coldest summer in the primary network. It does not narrow the season of a
1452 eruption, because the calibration shows a normal eruption-year summer
is common in every class.

**4. No regional pattern.** (`results/regional_*.txt`.)
- 1452: Moran's I −0.24, p 0.42; lowest sector Urals–West Siberia,
  mean −0.09, p 0.29 (Schneider). N-TREND: I −0.04, p 0.83; lowest sector
  Europe, mean −0.39, p 0.89. No cluster. The lowest sector differs between
  datasets. The coldest single N-TREND sites in 1452 (Yakutia −2.12,
  Asian grid 43° N 94° E −2.00) are isolated.
- 1453: I +0.16, p 0.18 (Schneider); I +0.23, p 0.005 (N-TREND, spatially
  coherent). The lowest sector is not significant in either (p 0.80, 0.16).
- Calibration: the lowest sector contained the source in 2 of 8
  extratropical events (Schneider) and 1 of 8 (N-TREND). Chance is about
  1 in 3 or 1 in 4. A one-summer sector minimum does not locate a source.

**5. Frost and light rings (secondary).** (`results/frostrings.txt`.)
- Colorado bristlecone pines (Brunstein 1995, NOAA): **1453 has a latewood
  frost ring in 25 of 33 Almagre Mountain trees (75 %)**, 4 of 6 at Black
  Mountain and 6 of 7 at Mount Princeton. Mount Bross, Mount Goliath, the
  Snake Range (NV) and the White Mountains (CA) also record it. It is the
  highest Almagre share of any latewood frost-ring year 1250–1993 (next
  1408, 73 %; 1805, 64 %).
- **1452 has no frost or light ring at any of these sites.** Neither does
  1454. The nearest light ring is 1450 (4 of 33 trees).
- A latewood frost ring forms when frost hits while the latewood cells are
  still growing, which is late summer. So the 1453 freeze fell late in the
  1453 growing season in the US Southwest. That fits aerosol already in
  place by late summer 1453.
- Québec: Abbott 2021 (p. 566) cites Filion et al. 1986 and Delwaide et al.
  1991 for light rings "related to 1453 CE in more than 25 % of subfossil
  black spruce trees". The Filion abstract's list of high-frequency years
  does not include 1453 (seen via search). I did not reach either paper.
  Reported, not verified.
- Calibration caveat: the same Colorado table records known eruptions
  weakly. 1601 is one light ring, 1641 and 1783–84 are absent, 1817 is 21 %,
  1912 is 12 %. Frost rings are local weather. A 1453 frost ring is not a
  source fingerprint, and the absence of a 1452 ring is weak evidence.

## Limits

- **Sample size.** 3–9 events per class. A modest real season effect
  (AUC 0.6–0.7) would not reach p < 0.05. The VSSI ≥ 3 sensitivity points
  that way (AUC 0.68), so "no separation" is a power statement.
- **Size.** UE 1453 is about 10 Tg S. The XE class runs from 2.5 Tg S
  (Hekla) to 20.8 (Laki), and two members have no eVolv2k estimate. The
  decision rule ignores size. A size-matched early-1452 extratropical
  eruption would probably have cooled 1452 (Laki, Novarupta did). That is a
  judgment, not a test.
- **Reference window.** 1442–1451 for all three years. N-TREND has only 36
  sites in 1452, many of them Asian grid pseudo-sites, and its ring-width
  records carry persistence.
- **Growing season.** MXD responds mainly to June–August. A June eruption
  can cool its own summer (Laki) or not (Pinatubo +0.27). Splitting at
  1 July puts June eruptions with the early class. The class boundaries are
  conventions.
- **The upper bound of 1453.5** rests on one statistic in one network. In
  N-TREND it does not hold.
- **Frost rings.** Not analysed. One table, one region, transcribed by the
  contributor. No light-ring data file for Québec was fetched.

## Provenance

| File | URL | Fetched | sha256 | Changes |
|---|---|---|---|---|
| 04's data files (schneider2015mxd.txt, ntrend2015tr.txt, ntrend2015-RecordsUsed_Metadata.txt, evolv2k_v4.tab) | see `../04-cooling-fingerprint/README.md` | 2026-10-20 (by 04) | as in 04 | read in place |
| GVP eruptions table | `../../sources/cache/gvp_holocene_eruptions.csv` | 2026-10-20 (see `sources/PROVENANCE.md`) | df21b092a630c647d6f2c15174d299a8d43564118f3eefdbf4a9aeaff9cba86f | months copied into `events.tsv` |
| data/readme_frostring.txt | https://paleo.ltrr.arizona.edu/treering/chronologies/colo_frost_rings/readme_frostring.txt | 2026-10-20 | d7b13b2a932061f66bfbe16c69b6e4837248a5dbee9d704a355ed94859914a7a | none |
| data/colofrlr.txt | https://paleo.ltrr.arizona.edu/treering/chronologies/colo_frost_rings/colofrlr.txt | 2026-10-20 | 669e5b40684c1bebead7c35ff56aa724dbf3f1af30aafd2858fff7e2209163d8 | none |
| data/amlfr.txt | https://paleo.ltrr.arizona.edu/treering/chronologies/colo_frost_rings/amlfr.txt | 2026-10-20 | d4d7a5334edf5de23d527fefd83773860122975f2c928a22461db737497d6560 | none (read, not parsed) |
| Abbott 2021 text | `../02-ice-onset/data/lit/a21.txt` (from 02) | 2026-10-20 (by 02) | see 02 | quoted |

Code credit: `summer.py` imports 04's `fingerprint.py` (loading, anomaly,
SD, AUC, threshold and LOO functions) by path, unchanged.

Sources and tiers: Schneider 2015, Wilson 2016 (SCHOLARLY; data PRIMARY);
eVolv2k v4 (PRIMARY dataset); GVP (SECONDARY); Brunstein 1995, USGS OFR
95-63, data via NOAA/LTRR (PRIMARY data); LaMarche & Hirschboeck 1984,
Nature 307:121 (SCHOLARLY, not read; cited through the Brunstein table and
Abbott 2021); Abbott et al. 2021, Clim. Past 17:565 (SCHOLARLY); Hutchison et
al. 2025, PNAS 122:e2416699122 (SCHOLARLY, abstract via search only);
Filion et al. 1986, Quat. Res. 26:272, and Delwaide et al. 1991, Can. J.
For. Res. 21:1828 (SCHOLARLY, not read); Parker 4 Jan 1641 and Tambora,
Krakatau climax dates via Wikipedia and Discover (SECONDARY/POPULAR, used
only to confirm eVolv2k months).

## Walls

- **Power.** With 3–9 events per class, the eruption-year summer cannot
  separate seasons. More events with known month and size would help.
  Post-1900 sulfur estimates for Novarupta, Sheveluch and the 20th-century
  tropical events would allow a size-matched test.
- **Québec light rings.** Filion 1986 and Delwaide 1991 are not read. The
  data may be in ITRDB. Breached by library access or an ITRDB search.
- **Within-season timing.** Only the frost-ring position (latewood) dates
  anything inside 1453. Documentary dates (experiment 05) are the other
  route.
