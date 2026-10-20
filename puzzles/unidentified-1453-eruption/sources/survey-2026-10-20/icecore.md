# Ice-core survey: the UE 1453 sulfate event

Survey date 2026-10-20. Budget: about 15 searches and fetches. Every number below
comes from a page or file fetched in this session. Tiers follow AGENTS.md.

## 1. Which records show the event, and how much

**Core network.** Abbott et al. 2021 (Fig. 1) plot the 1440–1490 CE sub-annual
non-sea-salt sulfur from these cores:
- Greenland: **NEEM-2011-S1** (Sigl et al. 2013), **TUNU2013** (Sigl et al. 2015),
  **NGRIP** (Plummer et al. 2012), all on the NS1-2011 chronology.
- Antarctica: **WAIS Divide (WDC)** on the WD2014 timescale (Sigl et al. 2016).

All of these show two separate peaks in the 1450s. The bipolar flux totals rest on
"a network of polar ice cores" (Sigl et al. 2014; Toohey & Sigl 2017). For 1458 the
Antarctic network is "16 ice cores all over Antarctica". I did not fetch the list of
cores behind that figure (B40, South Pole, Plateau Remote, DML and others).
[SCHOLARLY, https://doi.org/10.5194/cp-17-565-2021]

**Deposition and asymmetry.**

| Source | Greenland (kg km⁻²) | Antarctica (kg km⁻²) | NH share (ASY) |
|---|---|---|---|
| Abbott 2021, citing Sigl 2014 and Toohey & Sigl 2017 | 25 | 5 | 83 % |
| eVolv2k v4 (Sigl & Toohey 2024), 1453 row | 24.8 | 5.1 | 0.829 |
| For comparison, 1458 (v4) | 35.3 | 63.6 | 0.357 |

The v4 column header gives the unit as "kg/m²". Abbott gives these same numbers in
kg km⁻². The kg/m² is almost certainly a header mislabel; check it against the file.
[SCHOLARLY, Abbott 2021; PRIMARY dataset, https://doi.org/10.1594/PANGAEA.971968]

**Onset timing.** The event is named for the year sulfate first rises, 1453 CE. The
eruption itself happened "either in the same year or the previous year", so 1452 or
early 1453. In TUNU2013 the record has roughly monthly resolution, with about 1 cm
samples in about 12 cm annual layers, and seasonal precision of about 2 months.

Abbott et al. found Veiðivötn 1477 tephra in TUNU2013 at 78.515–78.655 m. That gives
a fixed tie point with zero age uncertainty. Counting annual layers back from it
confirms the NS1-2011 ages of 1453 and 1458 for the starts of the two peaks. WDC's
independently counted timescale agrees on the ages, the separation between the peaks
and their durations. The paper does not name the season of onset; that would need
the data file. [SCHOLARLY, Abbott 2021]

**Dome C, Antarctica (Gautier 2019 dataset).** No sample in the 1450s rows sits on a
1453 peak. The row dated 1453.6 has [SO4] 97.6 µg/kg, volcanic fraction fV 0.08 and
Δ33S 0.08. The volcanic sulfate there starts at about 1458 (rows Ev 13.0-6 to -3,
fV 0.62–0.81, [SO4] up to 460 µg/kg). This is my reading of the raw rows: the small
Antarctic 1453 signal (about 5 kg km⁻²) is not resolved as a separate event at Dome C.
[PRIMARY dataset, https://doi.org/10.1594/PANGAEA.895169]

## 2. Open datasets

- **eVolv2k v4** (Sigl & Toohey 2024, PANGAEA), which replaces v3. Tab file:
  https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile (fetched).
  Columns: year, month, day, latitude, Greenland and Antarctic cumulative deposition,
  VSSI in Tg S with 1σ, asymmetry ASY, attributed volcano, tephra detected Y/N,
  and reference. CC-BY-4.0. [PRIMARY]
- **eVolv2k v3**: doi:10.26050/WDCC/eVolv2k_v3, NetCDF of about 22 MB at WDC-Climate
  (DKRZ). It includes the stratospheric aerosol optical depth (SAOD) fields.
  **v2**: doi:10.1594/WDCC/eVolv2k_v2. Paper: Toohey & Sigl 2017, ESSD 9, 809,
  https://essd.copernicus.org/articles/9/809/2017/. I did not fetch file-level URLs
  for v3. [SECONDARY catalog records, via b2find and geodatenkatalog search results]
- **NEEM-2011-S1** aerosol record at 2 cm resolution, 86–1997 CE, NS1-2011
  chronology, including S, Na and Ca (Sigl & McConnell 2022):
  https://doi.org/10.1594/PANGAEA.940553, tab-delimited download from the page. [PRIMARY]
- **Six Greenland cores**, sulfur and volcanic sulfate deposition (Sigl, McConnell &
  Hörhold 2024), parent https://doi.org/10.1594/PANGAEA.967071. The one child I
  checked, PANGAEA.967094 (NEEM-S1 and NGRIP1 flux in kg km⁻² a⁻¹), covers only
  699–1002 CE. I did not check whether another child covers 1453. [PRIMARY]
- **Dome C sulfur and oxygen isotopes** (Gautier, Savarino & Farquhar 2018):
  https://doi.org/10.1594/PANGAEA.895169, parent https://doi.org/10.1594/PANGAEA.896238. [PRIMARY]
- **Burke et al. 2023** Dataset S01 (XLSX) in the PNAS supplement. Code:
  https://github.com/St-Andrews-Isotope-Geochemistry/Burke_2023_PNAS. [SCHOLARLY]
- **Abbott 2021** data in its supplement: https://doi.org/10.5194/cp-17-565-2021-supplement. [SCHOLARLY]
- **NOAA NCEI.** I did not reach a WDS-Paleo page for Sigl 2015 or eVolv2k (the
  study/22057 fetch came back empty). Not verified.

## 3. Inferred latitude and magnitude

- **eVolv2k v4 row:** `1453 1 1 lat 45.0, DG 24.8, DA 5.1, VSSI 9.97 ± 3.07 Tg S (1σ), ASY 0.829, location N/A, tephra N, ref "eVolv2k (Toohey & Sigl 2017; Burke et al. 2023)"`.
  Latitude 45.0 is the dataset's default for a Northern Hemisphere extratropical
  source, not a located vent. v4 says it now uses sulfur isotopes to constrain
  plume heights, so this row probably carries Burke's classification. [PRIMARY]
- **Burke et al. 2023 (PNAS 120, e2221810120).** They class 1453 as a **Northern
  Hemisphere extratropical** eruption. The initial sulfate has Δ33S ≈ 0 and low δ34S,
  consistent with transport below the ozone layer, and it falls off the tropical
  Δ33S–δ34S slope. **54 ± 6 % (1σ)** of the deposited sulfate came from the
  stratospheric overworld. NH summer cooling about 1 ± 0.3 °C, against 0.5 ± 0.2 °C
  for 1458. The revised stratospheric load for 1453 appears only in their Fig. 2B
  and is not given in the text. Their main result: for extratropical eruptions,
  stratospheric loads were lower than earlier estimates, by up to a factor of two.
  [SCHOLARLY, https://pmc.ncbi.nlm.nih.gov/articles/PMC10666123]
- **Earlier framing (Sigl 2013, via Abbott 2021).** A "comparatively smaller" eruption
  in the low latitudes, with a sulfate burden similar to Krakatau 1883. So the
  latitude call moved from tropical or low-latitude (bipolar) toward NH extratropical
  after Burke 2023. Record this as a revision, not a settled fact. Abbott 2021 also
  ranks 1453 fifth in its reconstruction of NH summer cooling, at −1.3 °C. [SCHOLARLY]
- I did not verify eVolv2k v2/v3's own latitude and VSSI for 1453. A v3 tropical
  default of 0° would be the usual rule for bipolar events, but I have not checked it.

## 4. Tephra

- **I found no published tephra result in the 1453 layer.** In TUNU2013, Abbott 2021
  sampled tephra only at 1477 (positive: about 126 shards, Veiðivötn) and at 1478/79
  (a few brown shards under 20 µm, not analysed). They name tephra work on "both
  events in the 1450s" as future work. The work was done at Queen's University
  Belfast (sample codes QUB-19xx; Plunkett and Abbott) and DRI (McConnell, Sigl).
  The eVolv2k v4 row for 1453 has tephra detected = **N**. [SCHOLARLY; PRIMARY]
- The 1458 event has tephra, and the attributions conflict. Hartman et al. 2019
  (South Pole) found glass distinct from Kuwae, possibly Reclus. Petit, Savarino,
  Delmonte, Gautier, Ginot and Batanova (EGU25-2329; IGE Grenoble, Milano-Bicocca,
  ISTerre) report dacite and rhyolite from Vostok and Dome C that matches proximal
  Kuwae and an ash layer on Efate. **EGU25-2329 does not mention 1453.**
  [CLAIMANT-ish conference abstract, https://meetingorganizer.copernicus.org/EGU25/EGU25-2329.html]
- Samples: TUNU2013 archive ice at DRI/QUB. Dome C 100 m cores processed at IGE.
  WDC is in the US national ice core archive (not verified in this session).

## 5. Sulfur isotopes (Δ33S, MIF)

- **Greenland: yes.** Burke 2023 cut 1453 samples from **TUNU2013** and found
  non-zero Δ33S, with a stratospheric fraction of 54 ± 6 %. Abbott 2021 also says
  sulfur-isotope analysis of both 1450s peaks in Greenland shows stratospheric
  injection (citing Baroni 2008, Cole-Dai 2013, Gautier 2019). [SCHOLARLY]
- **Antarctica: none found for 1453.** Burke sampled B40 for 540 and 1458 only. At
  Dome C the 1453.6 row shows nothing anomalous (Δ33S 0.08 ± 0.02, fV 0.08). The
  MIF there belongs to 1458 (Δ33S from +0.73 to −0.67).

## Other items checked

- **egusphere-2024-1322** is Marshall, Schmidt et al., "Last Millennium Volcanic
  Forcing and Climate Response using SO2 Emissions", final version Clim. Past 21,
  161–184 (2025). Its abstract does not mention 1453. A reviewer (Robock) asked why
  1458 was "Undefined". This is of marginal relevance: it is a forcing-dataset paper.
  [SCHOLARLY, https://egusphere.copernicus.org/preprints/2024/egusphere-2024-1322/]

## Unverified claims

- The kg/m² versus kg/km² unit in the eVolv2k v4 header.
- eVolv2k v2/v3 values for 1453 (latitude, VSSI, SAOD) and their file-level URLs.
- The list of Antarctic cores (B40, South Pole, Plateau Remote, DML and others) that
  carry 1453, and the per-core fluxes. Sigl 2014 (Nature Climate Change) and the
  Toohey & Sigl 2017 tables were not fetched.
- The onset season of the 1453 rise, and Burke's Fig. 2B revised load.
- Whether PANGAEA.967071 has a child dataset covering 1453.
- The NOAA NCEI pages for Sigl 2015 and eVolv2k.
- Gautier 2019 lists 1453 as one of its stratospheric events: the Wikipedia summary
  implies it, but the Dome C rows do not support it.
- Plummer 2012 NGRIP/Law Dome values for 1453.
- Where the WDC, B40 and South Pole archive ice is held.
