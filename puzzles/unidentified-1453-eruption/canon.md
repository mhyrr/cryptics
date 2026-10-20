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

## Sulfur isotopes and latitude
- TUNU2013 1453 sulfate has non-zero Δ33S: part of it reached the
  stratosphere, 54 ± 6 % (1σ). `established` for this core — Burke et al. 2023, PNAS.
- Burke 2023 classify 1453 as NH extratropical. Older work (Sigl 2013, via
  Abbott 2021) described a smaller low-latitude eruption, Krakatau-sized.
  `disputed`.
- No Antarctic sulfur-isotope data for 1453 found. The Dome C row at 1453.6
  shows no volcanic signal (fV 0.08, Δ33S 0.08). `likely`, from our reading
  of the raw rows in PANGAEA.895169, not a published statement.

## Climate response
- Summer 1453 is the coldest in Esper et al. 2017's tree-ring density
  network for about 800 years: mean −2.5 °C over 20 sites, 19 of them cold.
  Strongest at Polar Urals (−6.9 °C) and NW Canada (−4.9 °C), weak in the
  Alps (−0.4 °C); British Columbia +0.6 °C. `established` — Esper 2017.
- Abbott 2021 rank 1453 fifth-coldest NH summer since 500 CE (−1.3 °C).
  `established` — Abbott 2021.

## Source attribution
- Kuwae (Vanuatu) is not the 1453 source. `established` — Abbott 2021; Sigl 2013, 2015.
- No published paper names a candidate volcano for 1453. `likely` (absence
  across four surveys, 2026-10-20).
- No published tephra analysis of the 1453 layer in any Greenland core was
  found. `likely` — Abbott 2021 lists it as future work.
- GVP's current table lists Kuwae only at 1425 ± 5, VEI blank.
  `established` — `analysis/01-gvp-window/results/covers_1452.txt`.

## Structure and statistics (from `analysis/`, never from impression)
- GVP: 58 eruptions in 1420–1490 with VEI ≥ 4 or unknown; 59 with year ±
  uncertainty covering 1452; the only VEI-5 rows covering 1452 are Pinatubo
  1450 ± 50 and El Chichón 1360 ± 100. `established` for GVP as fetched
  2026-10-20 (sha256 df21b092…) — `analysis/01-gvp-window/`.
