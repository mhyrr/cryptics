# 04 — Cooling fingerprint

**Question.** Does the latitude gradient of Northern Hemisphere summer
cooling separate extratropical from tropical eruptions? If it does, where
does 1453 fall? Bears on README criterion 5 and on H2/H3.

## Pre-registration (written 2026-10-20, before any event anomaly was computed)

What I already knew when I wrote this: Esper 2017's published 1453 pattern
(canon: Polar Urals −6.9 °C, NW Canada −4.9 °C, Alps −0.4 °C, British
Columbia +0.6 °C). I had not computed any anomaly, for 1453 or any other
event, in any dataset below. Everything in this section is fixed before the
first run. Changes after the first run are listed under "Deviations".

**Datasets.**
- *Primary:* the 15 MXD site chronologies of Schneider et al. 2015
  (`schneider2015mxd.txt`, NOAA). They are the long-record core of Esper
  2017's network. Coordinates come from Esper 2017 Table 1. Zhaschiviersk
  (Zha) is excluded because Esper 2017 lists it as lacking a temperature
  signal. That leaves 14 sites: 7 at ≥ 60° N (Ala, Cam, Jae, Man, Nsc, Pol,
  Tor) and 7 below (Alt, Ath, Lau, Loe, Pyr, Que, Tyr).
- *Replication 1:* the 54 N-TREND2015 site records (Wilson 2016,
  `ntrend2015tr.txt`), coordinates from the NOAA metadata table (box centre).
- *Replication 2:* the N-TREND 2017 gridded field (Anchukaitis 2017,
  `ntrend2017grid.nc`, `t_filtered`, RE > 0 only), each 5° cell treated as a
  site at its centre latitude. Cells are interpolated from the same trees, so
  this is not independent of replication 1.

**Calibration events and labels.** All eVolv2k v4 events that carry an
attributed volcano and VSSI ≥ 3 Tg S, 1250–1900, plus the named post-1900
eruptions with VEI ≥ 5 in GVP, plus Sheveluch 1854 (in PLAN.md; VEI 5 in GVP;
no eVolv2k sulfur). Label X (extratropical NH) if source latitude > 30° N;
T (tropical) if |latitude| < 30°. Kuwae 1458 is excluded: its attribution
is disputed and its reference window contains the 1453 aftermath. Bipolar
events without an attributed volcano (1286, 1345, 1695, 1809) are excluded:
their label is a convention, not a fact. The list is in `events.tsv`.

**Year of the response.** For an eruption in year E, the response year Y is
whichever of E and E+1 has the lower network-mean standardized anomaly in
that dataset. The same rule applies to UE 1453 with E = 1453 (the eVolv2k
deposition year), so its candidates are 1453 and 1454. Sensitivity runs fix
Y = E and Y = E+1.

**Anomaly.** Per site: value(Y) minus the mean of years E−10 … E−1, leaving
out every year in [E', E'+2] for any other eruption in the exclusion list
(all eVolv2k events with VSSI ≥ 3 Tg S, plus the post-1900 eruptions).
At least 5 reference years must remain. The anomaly is divided by the site's
interannual standard deviation: the SD of (value − centred 11-year running
mean) over all its years 1250–1990. A site enters an event only if it has
data in Y and the reference years.

**Statistic (primary).** G = mean standardized anomaly of sites ≥ 60° N
minus mean of sites < 60° N. Negative G means the cooling is concentrated
at high latitudes. The prediction is that X events have more negative G
than T events. An event needs ≥ 3 sites in each group, else it is dropped
for that dataset.

**Secondary statistics.** S = OLS slope of standardized anomaly on latitude
(per 10°). F = G / (|mean_hi| + |mean_lo|), a size-free shape index in
[−1, 1].

**Tests.**
- Separation: AUC = P(G_X < G_T) over all X–T pairs. One-sided
  permutation test on the labels, 10 000 permutations, seed 1453.
- Leave-one-out: hold out each event, choose the threshold on G that
  maximizes balanced accuracy on the rest (midpoints between sorted values,
  ties broken toward the median midpoint), classify the held-out event.
  Report LOO balanced accuracy and its permutation p (same permutations).
- Effect size: difference of class medians and Hedges' g.

**Classifying 1453.** Only after the calibration result is written down.
Report G(1453) with a 95 % bootstrap interval (resample sites within each
latitude group, 2 000 draws, seed 1453), its rank inside each class, and the
side of the full-data threshold, with the share of bootstrap draws on the
X side. If the calibration does not separate (permutation p > 0.05 on the
primary dataset), 1453 is reported but not classified.

## Deviations

- After the first run I added one reporting line to `calibrate`: the 95th
  percentile of the null AUC, to show the test's power. No test, statistic,
  event or site changed.
- N-TREND has 53 usable records, not 54. The SCOT (Scotland) column is
  empty in the NOAA file.

## Run

```
uv sync                                    # numpy + h5py, only for the grid
python3 -I fetch.py data/                  # or use the files already in data/
uv run python -I grid_to_tsv.py data/ntrend2017grid.nc out/
python3 -I fingerprint.py calibrate schneider data/schneider2015mxd.txt sites_schneider2015.tsv events.tsv data/evolv2k_v4.tab > results/calibrate_schneider.txt
python3 -I fingerprint.py calibrate schneider data/schneider2015mxd.txt sites_schneider2015.tsv events.tsv data/evolv2k_v4.tab --year-rule E  > results/calibrate_schneider_yE.txt
python3 -I fingerprint.py calibrate schneider data/schneider2015mxd.txt sites_schneider2015.tsv events.tsv data/evolv2k_v4.tab --year-rule E1 > results/calibrate_schneider_yE1.txt
python3 -I fingerprint.py calibrate ntrend data/ntrend2015tr.txt data/ntrend2015-RecordsUsed_Metadata.txt events.tsv data/evolv2k_v4.tab > results/calibrate_ntrend.txt
python3 -I fingerprint.py calibrate grid out/grid_values.tsv out/grid_sites.tsv events.tsv data/evolv2k_v4.tab > results/calibrate_grid.txt
python3 -I fingerprint.py classify schneider data/schneider2015mxd.txt sites_schneider2015.tsv events.tsv data/evolv2k_v4.tab > results/classify_1453_schneider.txt
python3 -I fingerprint.py classify schneider data/schneider2015mxd.txt sites_schneider2015.tsv events.tsv data/evolv2k_v4.tab --target-year 1454 > results/classify_1454_schneider.txt
python3 -I fingerprint.py classify ntrend data/ntrend2015tr.txt data/ntrend2015-RecordsUsed_Metadata.txt events.tsv data/evolv2k_v4.tab > results/classify_1453_ntrend.txt
python3 -I fingerprint.py classify grid out/grid_values.tsv out/grid_sites.tsv events.tsv data/evolv2k_v4.tab > results/classify_1453_grid.txt
```

Each `calibrate` run takes about 30 s (10 000 permutations of a
leave-one-out loop).

## Result

**The cooling gradient does not discriminate source latitude in these
networks.** All 21 calibration events were kept in all three datasets
(7 extratropical, 14 tropical). None was dropped for coverage.

| Dataset | Sites (≥60° N / <60° N) | AUC P(G_X < G_T) | perm. p | LOO bal. acc. | perm. p | median G, X vs T | Hedges g |
|---|---|---|---|---|---|---|---|
| Schneider 2015 MXD (primary) | 14 (7/7) | 0.39 | 0.81 | 0.11 | 0.99 | +0.30 vs −0.23 | +0.36 |
| N-TREND2015 sites | 53 (19/34) | 0.49 | 0.55 | 0.36 | 0.86 | +0.17 vs +0.16 | −0.01 |
| N-TREND 2017 grid | 490 cells (267/223) | 0.44 | 0.68 | 0.57 | 0.39 | +0.02 vs −0.36 | +0.29 |

With 7 and 14 events, p < 0.05 needs AUC ≥ 0.72. All three are below 0.5:
if anything, the extratropical events cool the high latitudes *less*
relative to the mid-latitudes than the tropical ones do. The secondary
statistics (shape index F, latitude slope S) and the fixed-year rules
(Y = E, Y = E+1) give the same answer: AUC 0.28–0.51, lowest permutation p 0.25.

Examples from `results/calibrate_schneider.txt`. Laki 1783 (G −1.23) and
Sheveluch 1855 (−0.88) cool the north hardest, but so do Makian 1862
(−1.84), Parker 1641 (−0.97) and Huaynaputina 1601 (−0.95). Novarupta 1912
(+1.40), Shikotsu 1740 (+1.12) and Veiðivötn 1477 (+1.06) cool the
mid-latitudes harder. Tambora 1816 is +0.92 and Samalas 1258 is +1.96.

**1453, reported but not classified** (the pre-registered rule, since p > 0.05).
The response year chosen by the rule is 1453 in every dataset.

| Dataset | G(1453) | 95 % bootstrap | events with lower G |
|---|---|---|---|
| Schneider MXD | −1.57 | [−2.71, −0.65] | 0/7 X, 1/14 T (Makian) |
| N-TREND sites | −0.89 | [−1.66, −0.04] | 0/7 X, 1/14 T |
| N-TREND grid | −1.04 | [−1.34, −0.76] | 1/7 X, 1/14 T |

1453's cooling is more concentrated at high latitudes than almost any
calibration event. The tail it sits in holds both classes. In the primary
network, events at or below the full-data threshold (G < −0.86) are 2 of 7
X events and 3 of 14 T events, a likelihood ratio near 1.3. That number is
read off the printed values. It is not a test. Summer 1454 reverses
(G +1.11): the high latitudes recover first.

The per-site 1453 anomalies reproduce Esper 2017's pattern (Athabasca the
only warm site, the Alps weakest, Torneträsk, Jämtland and N-Scan among the
coldest). That checks the parsing. It adds no evidence.

**What this means.** A high-latitude cooling maximum is what NH summers do
after a large aerosol load, whatever the source latitude. It cannot be read
as a source-latitude fingerprint in these networks. Esper 2017's map is
evidence that 1453 was a large and early event. It is not evidence for H3
over H2.

## Limits

- **Sample size.** 7 extratropical events: three of 3.4–5.1 Tg S, and
  Sheveluch with no sulfur estimate. 14 tropical. A weak real effect (AUC 0.6) would not be
  detected. The result is "no usable signal at this sample size", not proof
  that no signal exists.
- **Size.** The extratropical class is mostly smaller than the tropical
  class. Small events are near the noise, so their G is noisy. The large
  extratropical events alone (Laki −1.23, Zavaritskii −0.36, Veiðivötn
  +1.06, Novarupta +1.40) do not point one way either.
- **Season.** Only one summer per event is scored. The eruption month moves
  aerosol arrival relative to the growing season, and the extratropical
  events span February to September.
- **Coverage.** The site set is the same for nearly every event in the
  primary network (6/6 for Samalas, 5/5 for Pinatubo). N-TREND and the grid
  thin out before about 1500 and after about 1990.
- **Not independent.** The grid is interpolated from the N-TREND sites. The
  Schneider sites are a subset of Esper 2017 and overlap N-TREND.
- **Circulation and ENSO.** One summer's regional pattern is dominated by
  circulation noise (Esper 2017 notes the British Columbia outlier). No ENSO
  or NAO state was removed.
- **Standardization.** MXD indices are in z-units of each site's
  interannual SD, not °C. The grid is in °C before standardization.
- **Labels.** The 1250–1900 labels are eVolv2k v4 attributions. Post-1900
  dates and latitudes are from GVP. Sheveluch 1854 has no ice-core sulfur
  estimate.
- **Not used.** Esper 2017's per-site temperature series (the 20-site
  network) are not in an open archive I found. Only the 15 Schneider 2015
  MXD chronologies are. Guillet 2017 per-site series were not looked for.

## Provenance

All fetched 2026-10-20. Files live in `data/` (gitignored). `fetch.py`
re-downloads them and prints hashes.

| File | URL | sha256 | Changes |
|---|---|---|---|
| schneider2015mxd.txt | https://www.ncei.noaa.gov/pub/data/paleo/treering/reconstructions/schneider2015mxd.txt | a521010f3e5f70187f11eda90da6049e9f86ac65d6037ccdbce1144a75921aa7 | none |
| ntrend2015tr.txt | https://www.ncei.noaa.gov/pub/data/paleo/treering/reconstructions/n_hem_temp/ntrend2015tr.txt | 56edbe049b5b1f8b4a0257ddcfa6f532832743c21b441deff438debea71cbff8 | none (SCOT column empty at source) |
| ntrend2015-RecordsUsed_Metadata.txt | https://www.ncei.noaa.gov/pub/data/paleo/treering/reconstructions/n_hem_temp/ntrend2015-RecordsUsed_Metadata.txt | 7d9ba42612199f09810bc327d76a43d79f3a224587dc2f29da13f40d4cbfb2ac | none |
| ntrend2017grid.nc | https://www.ncei.noaa.gov/pub/data/paleo/treering/reconstructions/n_hem_temp/ntrend2017grid.nc | c9ca70aed9cca657ecb977f7be154d8ba5b9fc1694af319528bcf7964160a3e9 | flattened to `out/` by `grid_to_tsv.py` |
| evolv2k_v4.tab | https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 | none |
| Esper_2017_BullVolc.pdf | https://www.climatology.uni-mainz.de/files/2016/03/Esper_2017_BullVolc.pdf | 5deac5c455bf65188c521477e8442b597179880074dbe24fecb4bfab206e720e | Table 1 coordinates transcribed into `sites_schneider2015.tsv` |
| GVP eruptions | `../../sources/cache/gvp_holocene_eruptions.csv` (see `sources/PROVENANCE.md`) | df21b092a630c647d6f2c15174d299a8d43564118f3eefdbf4a9aeaff9cba86f | dates and latitudes of post-1900 events and Sheveluch 1854, copied into `events.tsv` |

Sources and tiers: Schneider et al. 2015, GRL, doi:10.1002/2015GL063956
(SCHOLARLY; data PRIMARY); Wilson et al. 2016, QSR 134:1 and Anchukaitis
et al. 2017, QSR 163:1 (SCHOLARLY; data PRIMARY); Esper et al. 2017, Bull
Volcanol 79:41 (SCHOLARLY); eVolv2k v4, Sigl & Toohey 2024, PANGAEA
(PRIMARY dataset); GVP (SECONDARY database).
