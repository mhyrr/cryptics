# 06 — Candidate ranking

**Question.** Which named volcanoes could have made UE 1453? Can a scorer
built from open data rank the true source of known eruptions highly, blind?

## Pre-registration (written 2026-10-20, before any 1453 score was computed)

What I knew when I wrote this: the 01 candidate lists (`covers_1452.txt`),
the 03 band likelihoods, the 02 and 08 windows, and the eVolv2k v4 table.
I had not scored any candidate. The code is `pipeline.py`; its constants are
this pre-registration.

**Score.** For candidate eruption c:

score(c) = P(date | window) × P(band | 03) × P(size | VEI, class)

1. **P(date | window)** = ∫ p_c(t) L(t) dt. p_c is the candidate's
   calendar-date pdf (0.1-yr grid). L(t) = 1 inside the band window, 0.2
   elsewhere in the wide prior, 0 outside it. Windows are offsets from the
   Greenland sulfate onset (1453.05 for UE 1453):
   - NHET (also SHET): 1452.9–1453.5 (08). Calibration uses the ice-only
     window 1452.9–1453.7 (02), because 08's summer trim is 1453-specific.
   - tropical: 1452.0–1453.1 (02, 08).
   - wide prior: 1451.5–1453.6.
   - sensitivity: L = 1 over the whole wide prior (window ignored).
2. **Date pdf of a GVP row** (`row_pdf`).
   - `Sidereal: Ice Core`: dropped (leakage rule). Sensitivity: included.
   - Reported, dendro, varve with ± ≤ 1: uniform over the month if given,
     else over the year; uniform over [start, end] if the row has an end year
     (GVP gives eruption start, not climax: Tambora starts in 1812).
   - `14C (uncalibrated)`: IntCal20 calibration of 1950 − year ± unc (unc 0 → 50).
   - `14C (calibrated)`: normal(year + 0.5, unc), unc 0 → 50. GVP does not
     say whether ± is 1σ or 2σ; I take 1σ (the wider choice).
   - tephrochronology, anthropology, other: normal(year + 0.5, unc), unc 0 → 50.
   - no method: normal(year + 0.5, max(unc, 100)).
   - Primary lab ages, where extracted (`lab_ages.csv`), replace the GVP pdf.
     Ages are multiplied (combined) only if the paper says they date the same
     deposit or event. Otherwise the youngest-event age that the paper ties to
     the eruption is used, and the others are listed but not combined.
     Ages on bulk soil, peat or wood the paper flags as old are marked
     `maximum`; a maximum age gives a one-sided pdf (eruption after the
     calibrated age), implemented as the cumulative of its calibrated pdf.
3. **P(band)**: the normalised band likelihood from 03, by the candidate's
   GVP latitude. Variants: A1 (asymmetry [0.75, 1) × isotope), A6
   (asymmetry [0.70, 0.95) × isotope), A5 (asymmetry × out-of-sample isotope),
   E1 (emulator Jan/Jul × isotope), and ASY (asymmetry KDE only, the variant
   that calibration can reproduce).
4. **P(size)**: P(VSSI ≥ obs − 1σ | VEI, class), counted from data
   (`size_map.py`): (eVolv2k v4 named events 1500–1899 with that GVP VEI and
   class and VSSI above threshold + 0.5) / (GVP confirmed eruptions 1500–1899
   with that VEI and class + 1). Class: `rift-basalt` (GVP major rock basalt
   and rift setting, i.e. Iceland-type) or `other`. Cells with < 3 GVP
   eruptions pool both classes. P is capped to be non-decreasing in VEI.
   For UE 1453 the threshold is 9.97 − 3.07 = 6.90 Tg S.
   - **Missing VEI:** a mixture over VEI with weights equal to the VEI
     distribution of known-VEI GVP eruptions 1000–1899 dated by 14C or
     tephrochronology. Sensitivity: missing VEI treated as VEI 4.
   - Sensitivity: two-sided size window [obs/2, 2·obs].
5. **Candidate list**: GVP rows (confirmed or uncertain) with VEI ≥ 4 or
   blank, whose year ± unc overlaps onset year −13 … +17 (1440–1470 for
   UE 1453), any latitude (the band term weights them). For UE 1453 I add
   regional-catalog rows that GVP lacks.

**Blind calibration.** Every eVolv2k v4 named event with VSSI ≥ 3 Tg S
(Kuwae 1458 excluded as contested). For each: the candidate list is built
the same way from GVP around its onset; the band likelihood is the 03
asymmetry KDE (h = 0.05) trained leave-one-out on the other named events; the
size model is refitted without it; its own VSSI − 1σ is the threshold.
Onsets are the NEEM-2011-S1 onsets measured in 02 where they exist; otherwise
a synthetic onset (true date − 0.25 yr for NH extratropical, + 0.5 yr for
tropical, mid-window of the 02 lag ranges). Two modes:
- **as-is:** GVP dates as stored, ice-core rows dropped.
- **degraded:** every precise (reported, dendro, varve) date in the list,
  including the truth, becomes a synthetic 14C age: the IntCal20 mean at its
  date plus N(0, 40) noise, error 40 14C yr, recalibrated. 200 draws,
  seed 1453.

Reported: the rank of the best row of the true volcano, or "absent" if no
row of it survives the filter and leakage rule. Success criterion, fixed now:
the shortlist carries weight only if, in degraded mode, the true source is in
the top 5 for at least half of the cases where it is present, and the
absent rate is reported beside it.

Two additions made after the first calibration run, before any 1453 score
was read, and labelled as post hoc in the output: (1) a "VEI hidden" stress
mode, in which the true volcano's VEI is blanked, because almost every 1453
candidate has no VEI; (2) the rank of the true GVP subregion by summed score.
One bug fix after the first run: a month-long uniform date fell between grid
points and got zero mass (`pdf_uniform` now weights by cell overlap).

## Run

```
python3 -I fetch.py data                     # IntCal20, GVP volcano table; prints sha256
python3 -I size_map.py ../../sources/cache/gvp_holocene_eruptions.csv data/gvp_holocene_volcanoes.csv ../03-latitude-posterior/data/evolv2k_v4.tab > results/size_map.txt
python3 -I calibrate.py ../../sources/cache/gvp_holocene_eruptions.csv data/gvp_holocene_volcanoes.csv ../03-latitude-posterior/data/evolv2k_v4.tab data/intcal20.14c 200 > results/calibration.txt
python3 -I recal14c.py data/intcal20.14c lab_ages.csv > results/recal14c.txt
python3 -I rank1453.py ../../sources/cache/gvp_holocene_eruptions.csv data/gvp_holocene_volcanoes.csv ../03-latitude-posterior/data/evolv2k_v4.tab data/intcal20.14c ../03-latitude-posterior/results > results/prior_filter.txt
python3 -I rank1453.py ../../sources/cache/gvp_holocene_eruptions.csv data/gvp_holocene_volcanoes.csv ../03-latitude-posterior/data/evolv2k_v4.tab data/intcal20.14c ../03-latitude-posterior/results lab_ages.csv regional.csv vei_overrides.csv > results/rank1453.txt
```

Standard library only. `pipeline.py` holds the shared code. `data/` is
gitignored. Runtime is about a minute.

Checked-in inputs written by hand from papers (an LLM read them; the scripts
only compute):
- `lab_ages.csv`: 21 lab ages for four GVP eruptions, with table and page.
- `vei_overrides.csv`: VEI taken from a primary paper where GVP has none or differs.
- `regional.csv`: five AIST events that GVP lacks.

## Step 1. Candidate list and the leakage check

**GVP Grímsvötn and Katla rows (H5), checked.**
- Katla 1450 ± 50 is `Correlation: Tephrochronology` in the current table,
  not ice core. The survey note that called it ice-core-dated is wrong. It
  stays in the list. Its source paper could not be read (GVP volcano pages
  and timarit.is return 403).
- Grímsvötn has four `Sidereal: Ice Core` rows in the window: 1430 ± 10,
  1450 ± 10, 1469, 1470 ± 10. The leakage rule drops them. GVP's reference
  for them is unreadable (403). The likely source is the Vatnajökull
  glacier-tephra record, not polar ice. Larsen, Gudmundsson & Björnsson
  (EGU 2005) describe tephra layers in Vatnajökull outlet glaciers as "the
  most detailed eruption record" of Grímsvötn, "roughly 70" eruptions in the
  last millennium. If so, the date is not circular with Greenland. This is
  `likely`, not verified. With the rows included, Grímsvötn 1450 ± 10 ranks
  first (share 0.25). But Grímsvötn's known GVP VEIs are mostly 2 (27 of 48),
  so the generic missing-VEI mixture flatters it.
- Katla 1440 (VEI 4, `Observations: Reported`) falls outside the wide prior
  and scores zero.

**List.** 90 GVP rows overlap 1440–1470 with VEI ≥ 4 or blank (any
latitude), plus 5 AIST rows. The four Grímsvötn ice-core rows are dropped,
so 91 rows are scored.

**Regional catalogs.**
- AIST/GSJ eruptive-event catalog v2.5 (Japan and the southern Kurils),
  queried for 1400–1500 CE: 98 events. None has VEI ≥ 5 or magnitude ≥ 5.3.
  The largest is Sakurajima 1471–76 (Bunmei, M 5.3, VEI 4), which is
  historical and outside the window. Five magmatic events with no VEI that GVP
  lacks (Tiatia Ty-Sa, Ty-Sb, Ty-Na; Moyorodake Pereval; Oshima-Oshima
  Os-b) enter as uniform catalog ranges. Iwate T1-a/T1-b and Kuchinoerabujima
  f-1/f-2/N-1 match GVP rows; AIST calls most of them phreatic.
- AVO / USGS Alaska: read for Aniakchak only (Bacon et al. 2014, PP 1810).
- TephraKam (Portnyagin 2020): its tables sit on ResearchGate, not fetched. Wall.
- Icelandic catalogue (icelandicvolcanoes.is): the pages render by script,
  and the fetch returned no records. Wall.

## Step 2. Primary dates (`lab_ages.csv`)

| Candidate | Ages used | Source |
|---|---|---|
| Pinatubo, Buag | W-6314 460 ± 30 (charcoal in pyroclastic flow, event); Beta 470 ± 50 (tree in growth position in post-flow soil, minimum) | Newhall et al. 1996, Table 1 rows 4–5 |
| El Chichón unit B | 7 charcoal ages 550–700 BP, combined | Espíndola et al. 2000 via Nooren et al. 2009, Table 2, p. 102 |
| Aniakchak Half Cone (Pink Pumice, the Plinian phase) | GX-29531 360 ± 80, B-76809 390 ± 60 (wood), combined as the paper does | Bacon et al. 2014, PP 1810, Tables 1–2, pp. 17–18 |
| Aniakchak New Cone | WW212 390 ± 60, B-77038 340 ± 50, B-77039 460 ± 50, combined as the paper does | same |

Five other Pinatubo Buag ages and two Half Cone ages are listed but not used.
The paper does not tie them to the eruption, or they are not in its weighted
mean.

Not found, with GVP dates used instead: Katla 1450 (tephrochronology),
Karymsky ~1450 (Braitseva & Melekestsev 1990 give "about 500 B.P." on a
calibrated scale for the start of the IIKM cycle; Table 1 did not extract),
Iwate, Kuchinoerabujima, Rainier, Akutan, Kanaga, Khangar, Maly Semyachik,
Kikai, Sashiusudake, Hekla, Yakedake, Terceira, Jan Mayen.

**VEI from papers (`vei_overrides.csv`).**
- Aniakchak Half Cone: VEI 5, not GVP's 4. Browne, Neal & Bacon (2022) give
  "at least ~5.4 km3 of tephra" and 1.3 km³ DRE dacite–andesite.
- Karymsky: VEI 4 used as an upper bound. Its strongest IIKM eruptions were
  0.15 and 0.12 km³, "moderate-strength".
- El Chichón B: Nooren et al. (2009, p. 108) give "VEI ~4", but GVP gives 5.
  Used for sensitivity only.

## Step 3. IntCal20 recalibration (`results/recal14c.txt`)

| Candidate | 95.4 % HPD (CE) | P(NHET window 1452.9–1453.5) | P(tropical window 1452.0–1453.1) | uniform-rate baseline |
|---|---|---|---|---|
| Pinatubo Buag (event + minimum) | 1410–1457 | 0.006 | 0.012 | 0.024 (tropical) |
| Pinatubo Buag (W-6314 alone) | 1412–1470 | — | 0.020 | |
| El Chichón B (7 ages, T = 4.25 < 12.59) | 1306–1363, 1385–1409 | 0.000 | 0.000 | 0.014 |
| Aniakchak Half Cone (T = 0.09) | 1442–1530, 1537–1636 | 0.0029 | 0.005 | 0.0032 (NHET) |
| Aniakchak New Cone (T = 2.90) | 1439–1522, 1575–1624 | 0.0068 | 0.012 | 0.0045 (NHET) |

Reading. A 15th-century 14C date cannot pick a year. Each live candidate's
probability of falling in the window is close to what a flat date over its
HPD would give. The date term says "not excluded", nothing more. The one
exclusion: **El Chichón unit B ends by 1409 at 95 %**. Charcoal can carry
inbuilt age, which pushes the true date *younger* than the 14C age, so this
is strong but not final.

Old wood. Newhall's W-6314 is charcoal in a pyroclastic flow. Inbuilt age
could make it decades too old, which would move Buag later, towards 1453.
Braitseva (1990) note that charcoal in hot pyroclastic deposits can date
too old because it absorbs CO from hot, gas-saturated deposits (citing
Masurenkov 1980). Bacon's Half Cone ages are on wood, and the paper
does not flag them.

## Step 4. Calibration result (`results/calibration.txt`)

24 eVolv2k v4 named events with VSSI ≥ 3 Tg S. Katmai 1912 and Shiveluch
1854 cannot be used: eVolv2k v4 ends in 1900 and has no 1854 row. Ranks are
those of the true volcano, out of 53–116 candidates. The top-5 rate by chance
is about 0.05–0.09.

| Mode | true source present | rank 1 | top 5 (of present) | median rank, 1477–1883 cases |
|---|---|---|---|---|
| as-is | 20 / 24 | 15 | 18 | 1 |
| degraded (synthetic 14C, median of 200 draws) | 20 / 24 | 9 | 16 | 2 |
| degraded + true VEI hidden (post hoc) | 20 / 24 | 1 | 8 | 7 |

- **Pre-registered criterion met:** degraded median rank ≤ 5 in 16 of 20
  present cases.
- **Absent in 4 of 24** (17 %): Samalas 1257 (GVP dates it from ice and the
  rule drops it); Zavaritskii 1831 (not in GVP for 1831); Grímsvötn 751 and
  Katla 757 (no GVP row near the date). An identification of 1453 may lie
  outside the catalog altogether.
- **What carries the rank is VEI, not the date.** Once dates are degraded to
  14C, the truth stays near the top only when GVP gives it a large VEI. With
  its VEI hidden, as for almost every 1453 candidate, it is top 5 in 8 of 20
  and rank 1 once. The historical-era median rank is 7.
- Failures: Colima 1585 (rank 56) and Makian 1861 (39). They are NH tropical
  with Greenland-heavy asymmetry, and the asymmetry likelihood sends them
  north, as 03 found. Ruiz 1595 ranks 13.
- **Region does better than volcano.** The true GVP subregion is top 3 by
  summed score in 18 of 24 cases (degraded) and 12 of 24 (VEI hidden), out of
  about 32 subregions. This counts the absent cases.
- Caveat: pre-1477 tephrochronology dates in GVP (e.g. Bárðarbunga 870 and
  880, Katla 780) may themselves come from tephra tied to ice-core
  chronologies. I could not check this. The 1477–1883 rows above are the
  clean ones.

**Verdict.** The scorer works when the source is a catalogued eruption with
a known large VEI. For UE 1453 no such candidate exists. In the matching
stress test it puts the truth in the top 5 about 40 % of the time. **A named
1453 shortlist therefore carries little weight. The region-level result
carries more.**

## Step 5. UE 1453 ranking (`results/rank1453.txt`)

Headline: band A1, window on, missing VEI as a mixture, one-sided size, ice
rows dropped. "Share" is the score over the sum for all 91 scored rows.

| # | Candidate | P(date) | P(band) | P(size) | share |
|---|---|---|---|---|---|
| 1 | Aniakchak, Half Cone (Alaska, 56.9° N), VEI 5 (paper), 14C 379 ± 48 BP | 0.0043 | 0.80 | 0.119 | 0.105 |
| 2 | Katla 1450 ± 50 (Iceland), tephrochronology, VEI ? | 0.0072 | 0.80 | 0.052 | 0.075 |
| 3 | Pinatubo, Buag (15.1° N), VEI 5, 14C | 0.0144 | 0.13 | 0.119 | 0.055 |
| 4 | Aniakchak, New Cone, VEI ?, 14C 397 ± 30 BP | 0.0100 | 0.80 | 0.024 | 0.048 |
| 5 | Terceira 1400 ± 50 (Azores), VEI ? | 0.0041 | 0.80 | 0.052 | 0.044 |

Next: Karymsky 0.039, Hekla 1440, Yakedake, Kuchinoerabujima (two rows) at
0.03 each.

**Sensitivity** (top candidate and its share):
- band A6: Pinatubo 0.11.
- band A5, out-of-sample isotope: Pinatubo 0.28.
- band ASY, asymmetry only: Pinatubo 0.23.
- band E1: Aniakchak HC 0.10.
- window off: Aniakchak HC 0.11.
- missing VEI = 4: Katla 0.12.
- two-sided size: Aniakchak HC 0.13.
- GVP VEI instead of paper VEI: Katla 0.08.
- ice-core rows included: Grímsvötn 1450 0.25.

The order of the top five shuffles under every variant. No candidate takes
more than 0.13 of the score except Pinatubo, and Pinatubo does so only when
the isotope test is discounted (A5, ASY).

**Region.** North Pacific rim north of 30° N: 0.57 of the score (A1), 0.50
(A6), 0.24 (A5). Iceland and Jan Mayen: 0.16. By subregion: Alaska Peninsula
0.22, Iceland 0.13, Ryukyu 0.09, E Kamchatka 0.06, Luzon 0.06, NE Japan 0.06.
These shares mostly count catalogued unknown-VEI rows per region. They are a
catalog-density prior more than evidence.

**Answer.** No named candidate stands out. The defensible T2 statement:
**an unidentified NH extratropical eruption, most likely on the North
Pacific rim (Alaska Peninsula–Aleutians, Kamchatka–Kurils, Japan), with
Iceland second.** Aniakchak's Half Cone eruption is the best named
candidate. It is a VEI 5 Plinian eruption at 57° N whose 14C date
(1442–1636 at 95 %) does not exclude 1453. It is worth a glass comparison
(07). Pinatubo Buag survives only if the isotope test is wrong. El Chichón
unit B is excluded by date.

## Limits

- P(size) rests on 8 numerator events (1500–1899) and GVP VEI counts that
  are incomplete before 1800. The class split (rift basalt vs other) is
  crude. Terceira's 1400 row is a trachyte dome but inherits its volcano's
  "basalt, rift" class.
- The missing-VEI mixture is global. A volcano-specific VEI history would
  demote Grímsvötn (mostly VEI 2) and probably Kuchinoerabujima and Yakedake
  (AIST calls their events phreatic).
- GVP `14C (calibrated)` rows enter as normal(year, ±). I do not know
  whether ± is 1σ or 2σ.
- Calibration uses GVP-only candidate dates. 1453 adds primary ages for four
  rows. The comparison is fair for the other 87.
- The calibration's synthetic onsets use the true date plus a band-typical
  lag. That leaks band and season at the sub-year level only.
- I had budget for primary papers on 4 of the top ~15 candidates.
- The asymmetry band likelihood misplaces NH tropical eruptions with
  Greenland-heavy deposition (Colima, Makian). If UE 1453 is one, this
  scorer will not find it.

## Unverified claims

- The GVP Grímsvötn "Ice Core" dates come from Vatnajökull glacier tephra
  (inferred from Larsen et al. EGU 2005; GVP references unreadable).
- Larsen (2000, Jökull 50) records up to three Katla eruptions in the 15th
  century. Seen only as a search snippet (timarit.is 403).
- The Karymsky IIKM start "about 500 B.P." is on Arslanov's calibrated scale
  (IIKM-cycle section). Table 1, with the lab ages, did not extract.
- Charcoal in hot pyroclastic deposits can date too old (Braitseva 1990,
  citing Masurenkov 1980). Not checked for the Pinatubo or El Chichón samples.
- Laki: 15 km³ of basalt and 61 Tg S (ACP 3:487, 2003, via search snippet).
  Not opened.
- From memory, not checked: Pinatubo 1991 emitted about 15–20 Mt SO₂ from
  about 5 km³ DRE.

## Provenance

Fetched 2026-10-20 with Python urllib or WebFetch. Files are under `data/`
(gitignored) unless noted.

| File | URL | sha256 | Tier |
|---|---|---|---|
| intcal20.14c | https://intcal.org/curves/intcal20.14c | 974a66649f2ac8a53e6c99e256b019ac6982f999b12dcf7193162d4c1c09168e | PRIMARY (Reimer et al. 2020) |
| gvp_holocene_volcanoes.csv | GVP WFS, typeName GVP-VOTW:Smithsonian_VOTW_Holocene_Volcanoes, outputFormat=csv | d2a5aba7638dd02f91986267630b9ed4bc33e50063dd2ed35243b187adece0e0 | PRIMARY (compilation) |
| ../../sources/cache/gvp_holocene_eruptions.csv | see sources/PROVENANCE.md | df21b092a630c647d6f2c15174d299a8d43564118f3eefdbf4a9aeaff9cba86f | PRIMARY (compilation) |
| ../03-latitude-posterior/data/evolv2k_v4.tab | https://doi.pangaea.de/10.1594/PANGAEA.971968 | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 | PRIMARY |
| lit/pp1810.pdf | https://pubs.usgs.gov/pp/1810/downloads/pp1810.pdf | d87fa742c61a9ec9590c9988e31a58cd4678c25af25480eb987756d6480e35c9 | SCHOLARLY |
| lit/pp1810_appendixA_tablesA1A2.xlsx | https://pubs.usgs.gov/pp/1810/downloads/pp1810_appendixA_tablesA1A2.xlsx | df75d5d6c9adbd73354c8f3a0df0634320f81882c72fdf04b6505ac4d7456dd8 | SCHOLARLY (glass, unused) |
| lit/redalyc_56813222008.pdf | https://www.redalyc.org/pdf/568/56813222008.pdf (Nooren et al. 2009) | d0248273914efad5ac7f2cc587f69788aa259014dedaddf02c4ced5b43042857 | SCHOLARLY |
| lit/braitseva1990_karymsky.pdf | https://repository.geologyscience.ru/bitstreams/8306d117-730f-40a8-9f2b-ccbbbf50d4d9/download | a187dfa48a23e6b347debd1ea39738396286d2d3abe6fc45f7774292fd5962d8 | SCHOLARLY |
| lit/egu05_10066.pdf | https://www.meetings.copernicus.org/www.cosis.net/abstracts/EGU05/10066/EGU05-J-10066.pdf | 1c8bd6cac2479c328f23cfeeb7d9fec1899720c77cebca9db4240c38ee9ff324 | SCHOLARLY (abstract) |
| lit/aist_result_1400_1500.html, _p2.html | https://gbank.gsj.jp/volcano/cgi-bin/result.cgi (POST, CE 1400–1500) | 90ec6929…be32ee, 76527bac…8f28d | PRIMARY (catalog) |
| (not saved) Newhall et al. 1996 Table 1 | https://pubs.usgs.gov/pinatubo/newhall/table1.html | WebFetch, no file | SCHOLARLY |
| (not saved) Browne et al. 2022 abstract | https://pubs.usgs.gov/publication/70230513 | WebFetch, no file | SCHOLARLY |
| (not saved) AVO New Cone page | https://avo.alaska.edu/eruption/aniakchak-new-cone-tephra | WebFetch, no file | PRIMARY (agency) |

Refused or unusable: volcano.si.edu (403), timarit.is (403), dspace.library.uu.nl
(403), icelandicvolcanoes.is (script-rendered), TephraKam tables (ResearchGate).
