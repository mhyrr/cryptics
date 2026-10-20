# 10 — Grape-harvest dates

**Question.** Was the 1452 or 1453 growing season abnormally cold in
Burgundy? The grape-harvest date (GHD) tracks spring–summer temperature, and
its calendar date is exact. If known eruptions push the harvest late, a late
or normal harvest in 1452 and 1453 bounds the eruption timing. Bears on
README criteria 2 and 5.

## Pre-registration (written 2026-10-20, before any anomaly was computed)

What I knew when I wrote this: 02, 04, 05 and 08 (canon). While reading the
file formats I saw raw values for the 1450s in three files: the Labbé 2019
reconstructed April–July temperature (B_linear) for 1450–1459, the Chuine
2004 Burgundy GHD and temperature for 1440–1459, and a few Daux 2012 Jura and
Southern Rhône rows. By eye, the 1453 values look later or colder than 1452.
I had computed no anomaly, no reference median and no calibration number.
Everything below is fixed before the first run. Changes are listed under
"Deviations".

**Series (primary).** Beaune GHD, Labbé et al. 2019. The supplement does not
hold the observed GHD column. It holds the temperature reconstructed from GHD
with model B_linear, T = 31.59 − 0.061 × GHD (paper, Sect. 3). B_linear is
linear in GHD, so I invert it: GHD = (31.59 − T) / b, where b is the modal
step between sorted distinct T values (one day). Ranks and day differences do
not depend on the intercept. Absolute dates carry the intercept's rounding
(about ±1 day).

**Exclusion list.** As in 04/08: every eVolv2k v4 event with VSSI ≥ 3 Tg S,
plus every event in `../08-summer-1452/events.tsv` (this includes the
post-1900 eruptions and the UE 1453 row at 1452). Exclusion years are
[E′, E′+2] for every listed start E′.

**Anomaly.** For response year Y and eruption year E:
A(Y; E) = GHD(Y) − median of GHD over the 10 most recent years before E that
are not exclusion years and not missing, searching back to E−25. At least 7
reference years, or the event is dropped. Positive A = late = cold.

**Background.** Every year Y in 1364–2018 that is not an exclusion year,
with A(Y; Y). The threshold for "late" is the background 90th percentile, P90.

**Calibration events.**
- *S_large (primary):* events in `../08-summer-1452/events.tsv` (role `cal`
  or `nomonth`) within the series, with eVolv2k VSSI ≥ 8 Tg S, or with no
  eVolv2k value and GVP VEI 6. That is Colima 1585, Ruiz 1595, Huaynaputina
  1600, Parker 1640, Laki 1783, Tambora 1815, Zavaritskii 1831, Cosigüina
  1835, Krakatau 1883, Santa María 1902, Novarupta 1912, Pinatubo 1991.
  UE 1453 (≈ 10 Tg S) is size-matched to this set.
- *S_all (secondary):* every `cal` or `nomonth` event in that file within
  the series (21 events; Samalas 1257 predates it).
- *Check, not in any test:* Kuwae / UE 1458 (E = 1458).

**Hit.** An event is a hit if max(A(E; E), A(E+1; E)) ≥ P90.

**Test.** One-sided. Statistic: the hit count in S_large. Null: draw n
distinct background start years Y0 such that neither Y0 nor Y0+1 is an
exclusion year, score max(A(Y0; Y0), A(Y0+1; Y0)) ≥ P90, count hits.
10 000 draws, seed 1453. p = (#null ≥ observed + 1) / 10 001. The same for
S_all. Secondary statistic (superposed epoch): the event-mean A at lag 0 and
at lag +1, each against the same null draws.

**Season (descriptive).** Labbé's model uses March–July temperature. An
eruption after about June of year E can act only on E+1. I report the lag-0
hit rate of Jan–Jun events (08's early classes) and the lag-1 rate of all
events. These rates give the likelihood ratios below.

**Target.** UE 1453 with E = 1452: reference = the 10 eligible years before
1452. Report GHD, A and background percentile for 1452, 1453 and 1454.

**Decision rule.**
- If the S_large test has p > 0.05, the target is reported but no timing
  inference is drawn.
- If p ≤ 0.05:
  - A hit in 1452 favours aerosol over Burgundy by spring–summer 1452
    (eruption before about July 1452).
  - A normal 1452 (A < P90) disfavours a Jan–Jun 1452 eruption by
    LR = (1 − h0) / 0.90, where h0 is the lag-0 hit rate of early-season
    S_large events. The LR is reported, not turned into a verdict.
  - A hit in 1453 is consistent with an eruption before mid-1453 and
    adds nothing to 02/08 unless 1452 is also a hit.

**Fill check.** Labbé fill 61 pre-1645 gaps from a corrected Dijon series
shifted by the mean offset, and do not list the years. For 1371–1506 I print
D(Y) = Beaune GHD − Chuine 2004 Burgundy GHD (Dijon-based). A filled year
should sit at the fill offset. This is descriptive. It cannot prove a year
was observed.

**Secondary (descriptive, no test).** Chuine 2004 Burgundy GHD and its
April–August temperature reconstruction; Daux 2012 regional composites with
data in 1452–1454. Same anomaly rule; fewer than 7 reference years is
flagged, not dropped.

## Deviations

- S_all has 22 events, not 21. I miscounted: 21 `cal` rows plus
  Zavaritskii (`nomonth`). The rule did not change.
- `fillcheck` gained a post hoc scan after the first run. It finds runs of
  identical Beaune − Chuine differences and gives a shuffle p. This was not
  registered. It is descriptive.
- One exploratory import of `ghd.py` from the shell left a `__pycache__/`
  in this folder. Delete it before committing. No number changed.

## Run

```
python3 -I fetch.py data/      # then unzip the supplement:
python3 -I -m zipfile -e data/labbe2019-supplement.zip data/supp/
S=data/supp/Supplement_dataset_Labbe_et_al_2019.txt
E=../08-summer-1452/events.tsv; V=../04-cooling-fingerprint/data/evolv2k_v4.tab
python3 -I ghd.py calibrate $S $E $V > results/calibrate_beaune.txt
python3 -I ghd.py target    $S $E $V > results/target_beaune.txt
python3 -I ghd.py fillcheck $S data/burgundy2004.txt > results/fillcheck.txt
python3 -I ghd.py secondary data/burgundy2004.txt data/europe2012ghd.txt $E $V > results/secondary.txt
```

Standard library only. Each command runs in under 5 s. eVolv2k is read
from 04's `data/`.

## Result

**Series.** Beaune has a value for every year 1354–2018 except 1460 and
1571 (`results/calibrate_beaune.txt`). Inverting B_linear gives integer
dates with a constant offset (−0.07 d), so the inversion is exact up to the
rounded intercept. The 1354–1987 mean is DOY 270.7. The paper gives
28 September. For 1354–1506 the dates come from grape pickers' wage accounts,
"almost without any lacunae" for 1371–1506 (paper, Sect. 2). But see
result 4.

**1. Calibration: a late harvest is not a reliable eruption marker.**
Background: 562 years. P90 = +12.4 days. Because a hit can fall in E or
E+1, a random pair of years hits 18 % of the time.

| Set | n | hits (E or E+1 ≥ P90) | null mean | p | SEA lag 0 | p | SEA lag +1 | p |
|---|---|---|---|---|---|---|---|---|
| S_large (primary) | 12 | 3 (25 %) | 2.2 (18 %) | **0.37** | +2.0 d | 0.24 | +6.0 d | 0.019 |
| S_all | 22 | 8 (36 %) | 4.0 (18 %) | 0.031 | +2.2 d | 0.15 | +5.3 d | 0.007 |

- The primary test fails. Of 12 large eruptions, 3 gave a late harvest:
  Huaynaputina (1600, +18 d), Ruiz (1596, +19 d), Tambora (1816, +28 d).
  Laki (1783 −7, 1784 −9) and Pinatubo (1992 −9) gave early harvests.
  Krakatau, Parker, Cosigüina, Colima, Novarupta, Zavaritskii and
  Santa María were within the normal range.
- On average the harvest is about 6 days late in E+1 (p 0.019). The year E
  itself shows +2 days (p 0.24). The effect is a shift of the mean, not a
  dependable extreme.
- Season. Of 8 large Jan–Jun events, 1 was late in E itself (Huaynaputina).
  No large Jul–Dec event was late in E or E+1.
- Check: Kuwae / UE 1458 gave 1458 −5 d and 1459 +5 d (29th and 71st
  percentiles). The largest bipolar event of the century did not delay the
  Beaune harvest.

**2. 1452 normal, 1453 late, 1454 late-ish.** (`results/target_beaune.txt`.)
Reference 1442–1451, median DOY 275.4 (about 2 October, Julian).

| Year | GHD (DOY) | approx. date (Julian) | A (days) | background percentile | ≥ P90 |
|---|---|---|---|---|---|
| 1452 | 272 | 29 Sep | −3.5 | 37 | no |
| 1453 | 287 | 14 Oct | +11.5 | 89 | no (P90 = +12.4) |
| 1454 | 284 | 11 Oct | +8.5 | 80 | no |

1453 is the 26th-latest of 663 Beaune harvests. It ties with the 1442
reference year (287). It misses the pre-registered "late" threshold by one
day.

**3. Timing: no inference.** The primary test has p 0.37, so the decision
rule draws none. For the record, the rule's likelihood ratio for a normal
1452 against a Jan–Jun 1452 eruption would be (1 − 1/8) / 0.90 ≈ 0.97.
That is no information. The pattern (1452 normal, 1453–54 late) fits every
window in 02/08: 1452.9–1453.5 if NHET, 1452.0–1453.1 if tropical. Harvest
dates cannot narrow it.

**4. Is 1453 a Beaune observation? Possibly not.** (`results/fillcheck.txt`.)
Beaune minus the Chuine 2004 Burgundy series (Dijon-referenced) is exactly
+6 days in each of 1453, 1454, 1455 and 1456. That is the only run of four
identical differences in 1370–1644. A shuffle gives p 0.046 (post hoc).
Labbé fill 61 pre-1645 gaps with a corrected Dijon series shifted by the
mean offset. A constant offset over four years is what such a fill looks
like. The paper does not list the filled years. So 1453–1456 may be Dijon
dates, not Beaune wage-account dates. If so, the Beaune and Burgundy series
are one witness there, not two.

**5. Secondary series.** (`results/secondary.txt`.)
- Chuine 2004 Burgundy GHD: 1452 −8.5 d (19th percentile), 1453 +4.5 d
  (69th), 1454 +1.5 d (57th). Their April–August temperature: 1452 +0.66 °C,
  1453 −0.35 °C, 1454 −0.11 °C against 1442–1451. 1453 is cool, not extreme.
- Daux 2012 Burgundy composite (same dates as Chuine in 1452–56, so not
  independent): 1453 +10 d (86th percentile) against a gappier reference.
- Daux 2012 Jura: values in 1449, 1450, 1453, 1454 only. 1453 is 28 days
  *earlier* than a 2-year reference. Flagged, not used.
- No Daux series for Switzerland (from 1481), Ile-de-France (1479), Germany
  (1612) or any other region covers 1452–1454. Bordeaux and Southern Rhône
  have values in the 1440s but none in 1452–1454.

**What this means.** Burgundy's 1453 growing season was cool: the
harvest came about 12 days late, in the top 11–12 % of years. 1452 was
normal. That fits a large eruption whose aerosol was in place by spring or
summer 1453. But known large eruptions delay the Beaune harvest past P90 no
more often than random years do (3 of 12). So the series cannot date the
eruption, and a normal 1452 rules nothing out. It agrees with Esper 2017's
weak Alpine signal for 1453 (canon): western Europe was cooled mildly.

## Limits

- **Power.** 12 large events. The E+1 mean shift (+6 d) is real at
  p 0.02, but one event's harvest is dominated by local weather (SD about
  10 days).
- **What GHD measures.** Labbé's models use March–July temperature. Harvest
  dates also depend on rain, disease and the decision to pick. A cold
  August–September does not show.
- **Reconstructed column.** The observed GHD column is not in the
  supplement. I recovered it from B_linear. Day differences are exact.
  Absolute dates carry about ±1 day from the rounded intercept. Pre-1718
  dates include Labbé's +7-day homogenisation.
- **Possible Dijon fill in 1453–1456.** See result 4. Breach: Labbé &
  Gaveau 2013 (Revue historique 666:333), which lists the source of each
  date, or the authors.
- **Missing 1460.** Labbé has no value for 1460. It does not affect
  1452–1454 but shortens Kuwae's E+2.
- **Calendar.** All 15th-century dates are Julian. Anomalies do not care.
- **Exclusion windows.** 1452–1456 and 1458–1460 are exclusion years, so
  they are not in the background. This is the rule, not an omission.

## Provenance

Fetched 2026-10-20 by `fetch.py`. Files live in `data/` (gitignored).

| File | URL | Fetched | sha256 |
|---|---|---|---|
| data/labbe2019-supplement.zip | https://cp.copernicus.org/articles/15/1485/2019/cp-15-1485-2019-supplement.zip | 2026-10-20 | f9457e3796adc2494812715558bd9648735a458fe4fd632732834803e4f6dca7 |
| data/supp/Supplement_dataset_Labbe_et_al_2019.txt (from the zip) | as above | 2026-10-20 | 248df43e90128be0c1053bdda66256b32d9e67de692dd25bd2c8a599dce93986 |
| data/supp/Supplementary_figures_Labbe_et_al_2019.docx (from the zip; read, not used) | as above | 2026-10-20 | 6005f937a7d92dc7300d8dfa3469916967fe6ba61fb23be97bef5fab9f186c69 |
| data/burgundy2004.txt | https://www.ncei.noaa.gov/pub/data/paleo/historical/europe/france/burgundy2004.txt | 2026-10-20 | 635ca10d65bf77bd508377067a15dfab40dc50abf39e91b7b79f198b08257477 |
| data/europe2012ghd.txt | https://www.ncei.noaa.gov/pub/data/paleo/historical/europe/europe2012ghd.txt | 2026-10-20 | f940f576d69ee049286f75995a22b6a183009a08398cd7ee08470f8570824260 |
| eVolv2k v4 | `../04-cooling-fingerprint/data/evolv2k_v4.tab` (see 04) | by 04 | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 |
| events | `../08-summer-1452/events.tsv` | — | read in place |
| GVP VEI 6 for Novarupta 1912, Santa María 1902, Pinatubo 1991 | `../../sources/cache/gvp_holocene_eruptions.csv` | by 01 | df21b092a630c647d6f2c15174d299a8d43564118f3eefdbf4a9aeaff9cba86f |

Paper facts (B_linear coefficients, wage-account sources, the 61 Dijon
fills, March–July window) were read from the article HTML,
https://cp.copernicus.org/articles/15/1485/2019/cp-15-1485-2019.html,
on 2026-10-20.

Sources and tiers: Labbé, Pfister, Brönnimann, Rousseau, Franke & Bois
2019, Clim. Past 15:1485–1501, doi:10.5194/cp-15-1485-2019 (SCHOLARLY; data
PRIMARY). Chuine et al. 2004, Nature 432 (18 Nov 2004), data NOAA WDC contribution
2005-007 (SCHOLARLY; data PRIMARY). Daux et al. 2012, Clim. Past
8:1403–1418, doi:10.5194/cp-8-1403-2012, data NOAA study 13194 (SCHOLARLY;
data PRIMARY). eVolv2k v4 (PRIMARY dataset). GVP (SECONDARY).
Labbé & Gaveau 2013, Revue historique 666:333–367 (SCHOLARLY, not read).

## Walls

- **Method.** One vineyard's harvest is too noisy to date an eruption: 3 of
  12 large eruptions crossed P90. More long series from the 1450s would
  help, but none in Daux 2012 covers 1452–1454 outside Burgundy and Jura.
- **Source of the 1453 date.** Whether 1453–1456 are wage-account dates
  or Dijon fills. Breach: Labbé & Gaveau 2013 or the authors.
