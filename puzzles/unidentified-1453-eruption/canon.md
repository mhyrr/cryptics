# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` /
`disputed`), and a source pointer. Survey detail is in `sources/survey-2026-10-20/`.

## The record
- Greenland cores NEEM-2011-S1, TUNU2013 and NGRIP show two separate sulfate
  peaks in the 1450s, starting in 1453 and 1458. Ages are tied by layer
  counting to Veiðivötn 1477 tephra in TUNU2013 (78.515–78.655 m).
  `established` — Abbott et al. 2021, Clim. Past 17:565.
- WAIS Divide's independent WD2014 timescale agrees on both ages.
  `established` — Abbott 2021.
- 1453 deposition: Greenland 24.8, Antarctica 5.1 kg km⁻²; asymmetry 0.829;
  9.97 ± 3.07 Tg S (1σ); tephra not detected; location N/A; latitude 45.0
  (the dataset's NH-extratropical default, not a located vent).
  `established` as dataset values — eVolv2k v4, PANGAEA.971968. Header unit
  reads kg/m²; Abbott gives kg km⁻². Unit `likely` a header mislabel.
- For comparison, 1458: Greenland 35.3, Antarctica 63.6, asymmetry 0.357.
  `established` — eVolv2k v4.
- The eruption occurred in 1452 or early 1453. `likely` — Abbott 2021.
- Greenland sulfate onset is 1453.13 ± 0.05 (NEEM, NS1-2011) and
  1453.00 ± 0.04 (TUNU2013), in the winter–spring layer. Large eruptions
  start at the Na maximum whatever their month, so onset position does not
  give the season. The window calibrated on known eruptions is early 1452 to
  mid-1453. `likely` — `analysis/02-ice-onset/`.
- One sulfate pulse in each high-resolution core (TUNU2013, NEEM, WAIS
  Divide), and one Δ33S excursion. `likely` — `analysis/02-ice-onset/`.
- Antarctic 1453 sulfate is above background in 5 of 15 cores (WDC06A, SP01,
  SP04, EDC96, DFS10); network binomial p = 0.0006. WAIS Divide monthly
  onset is 1453.6, half a year after Greenland. `established` from
  `analysis/02-ice-onset/`.

## Sulfur isotopes and latitude
- TUNU2013 1453 sulfate has non-zero Δ33S: part of it reached the
  stratosphere, 54 ± 6 % (1σ). `established` for this core — Burke et al. 2023, PNAS.
- Burke 2023 classify 1453 as NH extratropical. Older work (Sigl 2013, via
  Abbott 2021) described a smaller low-latitude eruption, Krakatau-sized.
  `disputed`.
- No Antarctic sulfur-isotope data for 1453 found. The Dome C isotope sample
  at 1453.6 shows no volcanic fraction (fV 0.08, Δ33S 0.08), but EDC96
  sulfate at Dome C does show the event (z 5.5). The isotope sample likely
  missed the layer. `likely` — PANGAEA.895169; `analysis/02-ice-onset/`.
- Hemispheric asymmetry and the Marshall 2021 emulator exclude an SH
  extratropical source. They do not separate NHET from 0–30° N.
  `likely` — `analysis/03-latitude-posterior/`.
- The isotope class matched the true band in 7 of 7 known cases. Only 2 were
  out of sample, both NHET; no tropical case is out of sample.
  `established` as a count — `analysis/03-latitude-posterior/`.
- P(NHET) is 0.69–0.94 under ordinary priors, 0.44 with out-of-sample
  isotope cases only, about 0.5 under a tropics-heavy prior. The NHET
  result depends on the isotope test. `likely` — `analysis/03-latitude-posterior/`.

## Climate response
- Summer 1453 is the coldest in Esper et al. 2017's tree-ring density
  network for about 800 years: mean −2.5 °C over 20 sites, 19 of them cold.
  Strongest at Polar Urals (−6.9 °C) and NW Canada (−4.9 °C), weak in the
  Alps (−0.4 °C); British Columbia +0.6 °C. `established` — Esper 2017.
- Abbott 2021 rank 1453 fifth-coldest NH summer since 500 CE (−1.3 °C).
  `established` — Abbott 2021.
- The ≥ 60° N vs < 60° N summer-cooling contrast does not separate 7
  extratropical from 14 tropical calibration eruptions in Schneider 2015
  MXD, N-TREND2015 sites or the N-TREND 2017 grid (AUC 0.39–0.49,
  permutation p 0.55–0.81). 1453 sits in a tail both classes share. The
  pattern is not diagnostic of source latitude. `established` for these
  networks and this statistic — `analysis/04-cooling-fingerprint/`.
- Summer 1452 shows no cooling: MXD network-mean z +0.30 (73rd percentile
  of 1442–1451-referenced background), 0 of 14 sites ≤ −1; N-TREND −0.25
  (24th percentile). Summer 1453 is colder than all 606 background years in
  the MXD network. `likely` — `analysis/08-summer-1452/`.
- At these sample sizes the eruption-year summer does not separate eruption
  season or latitude class (AUC 0.53–0.61, p ≥ 0.25). Only Laki and
  Novarupta cooled their own summer. A normal 1452 therefore excludes little.
  `likely` — `analysis/08-summer-1452/`.
- Eruption window combining ice (02) and summers (08): 1452.9–1453.5 if
  extratropical (upper bound from the MXD network only), 1452.0–1453.1 if
  tropical. `likely` — `analysis/08-summer-1452/results/window.txt`.
- 1453 is the strongest latewood frost-ring year at Almagre Mountain,
  Colorado, 1250–1993 (25 of 33 trees); also Black Mountain 4/6, Mount
  Princeton 6/7. No frost ring in 1452 or 1454 at any site. Latewood position
  means frost late in the 1453 growing season. `established` for the
  Brunstein 1995 table — `analysis/08-summer-1452/results/frostrings.txt`.
- Québec light rings in 1453 are reported through Abbott 2021 (citing
  Filion 1986, Delwaide 1991). Originals unread. `disputed` (unverified).
- Beaune grape harvest (inverted from Labbé 2019's reconstruction): 1452
  normal (−3.5 d, 37th percentile); 1453 late (+11.5 d, 89th; 26th-latest of
  663); 1454 +8.5 d. Western Europe cooled mildly in 1453. `likely` —
  `analysis/10-harvest-dates/`.
- Known large eruptions push the Beaune harvest past the 90th percentile no
  more often than random years (3/12, p 0.37); mean E+1 delay ~+6 d
  (p 0.02). Harvest dates do not narrow the eruption window. `established`
  for this series and statistic — `analysis/10-harvest-dates/`.
- Beaune 1453–1456 may be Dijon fills: Beaune minus Chuine 2004 is exactly
  +6 d in all four years, the only such run 1370–1644 (post hoc, p 0.046).
  `disputed` (unverified; Labbé & Gaveau 2013 would settle it).

## Documentary record
- Cold reaches Korea on 2 Aug 1453 (snow at Hamheung, 39.9° N) and 17 Aug
  1453 (three days' frost at Gapsan, "寒氣如十月", "the cold was like the
  tenth month"). Julian dates. `established` as record — Danjong Sillok
  vol. 6 p. 602, vol. 7 p. 605; `analysis/05-documentary-onset/`.
- The Ming winter cold disaster begins 15 Dec 1453. Cold/snow reports in
  lunar 1453–54 are 22 against 3.5 expected (p = 4×10⁻¹¹), 19 of them in
  winter 1453/54. `established` (computed) — Ming Shilu; `analysis/05`.
- No dimmed, red or hazy sun is recorded in Korea, China or Poland in
  1452–55. The Mingshi records one on 25 Mar 1458. `likely`. The Sillok
  method detected only one of three testable known eruptions (Parker 1641).
- The 1454 Mexican famine follows a drought that began by 1450–52. The
  "1453 frost" is one reading of a pictograph. `likely` — Therrell 2004.

## Source attribution
- Kuwae (Vanuatu) is not the 1453 source. `established` — Abbott 2021; Sigl 2013, 2015.
- No published paper names a candidate volcano for 1453. `likely` (absence
  across four surveys, 2026-10-20).
- No published tephra search of the 1453 layer in TUNU2013 or NEEM-2011-S1.
  Abbott 2021 sampled 1477–1479 only and lists the 1450s as future work;
  Plunkett 2023 Table 1 has no Greenland tephra between 1254/5 and 1477.
  NGRIP and the Summit cores are unknown (Cole-Dai 2013, Coulter 2012 not
  read). `likely` — `analysis/02-ice-onset/`.
- Open continuous-flow tracers in NEEM-2011-S1 (Ce, Mn, Ca, Sr, acidity) and
  TUNU2013 (30 species incl. Cl, Br, Tl, Cd, Pb, Al) do not separate 15
  Icelandic from 21 distant calibration eruptions in a pre-registered test
  (LOO balanced accuracy 0.31 and 0.70; permutation p 0.92 and 0.081).
  NEEM's lithic channels miss even Laki and Eldgjá. `established` for these
  data — `analysis/09-ice-tracers/`.
- TUNU2013 shows an Al pulse at the 1453 sulfate onset (97th percentile of
  empty windows; 0.10–0.29 yr after onset) with the lowest nssCl/S of 21
  events. The Al test is post hoc (ICE 4/8, NHX 0/6, TROP 1/7; p 0.047);
  the chloride may be a sea-salt-correction artefact. `likely` as
  measurement, uninterpreted — `analysis/09-ice-tracers/`.
- No open record shows 1453 ash arriving before its sulfate. TUNU2013's
  particle record (Plunkett 2023) is "available on request". `likely`.
- GVP Katla 1450 ± 50 is dated by tephrochronology, not ice core.
  `established` — current GVP table; `analysis/06-candidate-ranking/`.
- GVP's four Grímsvötn rows in 1430–1470 are "Sidereal: Ice Core". They
  probably come from Vatnajökull glacier tephra, not Greenland, so they are
  probably not circular. `likely` (GVP references unread).
- El Chichón unit B: 95% range 1306–1409 CE from 7 consistent charcoal
  ages (IntCal20). Inbuilt age would push it younger. `likely` —
  `analysis/06-candidate-ranking/`.
- Aniakchak Half Cone Plinian (Pink Pumice; ≥ 5.4 km³, VEI 5 per Browne
  2022): two 14C ages calibrate to 1442–1636 CE (95%), which includes 1453.
  `established` for the dates — `analysis/06-candidate-ranking/lab_ages.csv`.
- AIST lists no VEI ≥ 5 Japanese eruption in 1400–1500. `established` for
  the catalog.
- The 06 scorer, tested blind on 24 known sources with dates degraded to 14C
  uncertainty, ranks the truth top 5 in 16 of 20 present cases. With VEI
  hidden (the 1453 situation) it does so in 8 of 20. 4 of 24 true sources are
  missing from GVP or dropped by the leakage rule. Named rankings carry
  little weight; region-level shares carry more. `established` for this set.
- 1453 score shares (headline variant): North Pacific rim north of 30° N
  0.57 (0.24 with out-of-sample isotopes only); Iceland and Jan Mayen 0.16.
  No named candidate exceeds 0.13. Shares partly reflect catalog density.
  `likely` — `analysis/06-candidate-ranking/results/rank1453.txt`.
- GVP's current table lists Kuwae only at 1425 ± 5, VEI blank.
  `established` — `analysis/01-gvp-window/results/covers_1452.txt`.

## Structure and statistics (from `analysis/`, never from impression)
- GVP: 58 eruptions in 1420–1490 with VEI ≥ 4 or unknown; 59 with year ±
  uncertainty covering 1452; the only VEI-5 rows covering 1452 are Pinatubo
  1450 ± 50 and El Chichón 1360 ± 100. `established` for GVP as fetched
  2026-10-20 (sha256 df21b092…) — `analysis/01-gvp-window/`.
