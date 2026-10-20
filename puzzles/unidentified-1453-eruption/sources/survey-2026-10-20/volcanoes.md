# Survey: eruption databases and candidate volcanoes for UE 1452/53

Slice: eruption catalogs (GVP, LaMEVE, regional) and proposed source volcanoes.
Compiled 2026-10-20. About 15 web calls used. Rule 2 applies: anything taken from memory is under "Unverified claims".

## 1. Smithsonian GVP, Volcanoes of the World (VOTW)

**Bulk access that works (checked 2026-10-20):** the GVP GeoServer WFS. It returns CSV without authentication when called with Python urllib. Source tier: PRIMARY for the catalog itself, though the catalog is a compilation.

- Capabilities: `https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0&request=GetCapabilities`
- Eruptions, as one CSV of 11,089 rows (2.1 MB): `https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0&request=GetFeature&typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Eruptions&outputFormat=csv`
- Other layers: `GVP-VOTW:Smithsonian_VOTW_Holocene_Volcanoes`, `GVP-VOTW:Smithsonian_VOTW_Pleistocene_Volcanoes`, and `GVP-VOTW:E3WebApp_*` (emissions, eruptions since 1960). A CQL_FILTER parameter should allow server-side filtering, but I did not test it.
- Eruption fields: `Volcano_Number, Volcano_Name, Eruption_Number, Activity_Type` (Confirmed 9,916 / Uncertain 1,173), `ExplosivityIndexMax` (VEI; blank means unknown), `ExplosivityIndexModifier, ActivityArea, ActivityUnit` (tephra layer name), `StartEvidenceMethod` (the dating method), `StartDateYearModifier` ("?" or similar), `StartDateYear` (negative = BCE), `StartDateYearUncertainty` (one symmetric ± value in years), month/day fields, the matching End* fields, and `GeoLocation` as `POINT (lat lon)`.
- **How the dating method is recorded:** `StartEvidenceMethod` uses a fixed vocabulary. Values found in the full table: `Observations: Reported` (6,468), blank (1,101), `Correlation: Tephrochronology` (1,043), `Isotopic: 14C (uncalibrated)` (984), `Isotopic: 14C (calibrated)` (869), `Sidereal: Varve Count`, `Sidereal: Ice Core` (45), `Sidereal: Dendrochronology` (11), `Correlation: Anthropology`, and others. A radiocarbon-dated eruption gets one central year plus one ± value. The calibration curve and the full calibrated probability distribution are not stored, so years such as "1450 ± 50" are rounded central values.
- The web pages (`volcano.si.edu/database/webservices.cfm`, `volcano.cfm?vn=...`) returned HTTP 403 to both WebFetch and urllib. That means I could not read GVP's own documentation of the Excel export or its citation and version text. The WFS endpoint answered normally.

**Files pulled:**
- Full eruption table: `/private/tmp/claude-501/-Users-mhyrr-work-cryptics/33026e17-9aef-4705-96fa-02d118b29688/scratchpad/gvp_dl/holocene_eruptions.csv`
- Start years 1400–1500 CE (149 rows, with lat/lon columns added): `/private/tmp/claude-501/-Users-mhyrr-work-cryptics/33026e17-9aef-4705-96fa-02d118b29688/scratchpad/gvp_eruptions_1400_1500.csv`
- Scripts: `/private/tmp/claude-501/-Users-mhyrr-work-cryptics/33026e17-9aef-4705-96fa-02d118b29688/scratchpad/scripts/filt.py` and `cover.py`. Rerun with `python3 -I scripts/filt.py gvp_dl/holocene_eruptions.csv out.csv`.

**Counts (from filt.py output):**
- 58 eruptions have a start year in 1420–1490 CE with VEI ≥ 4 or no VEI recorded. Only 10 of them have VEI ≥ 4; 48 have no VEI.
- Dating methods for those 58: 14C calibrated 17, 14C uncalibrated 10, reported 9, tephrochronology 7, blank 6, ice core 6, dendrochronology 2, anthropology 1.
- VEI ≥ 4 in 1420–1490: Izu-Oshima 1421 (4, reported); Sheveluch ?1430 (4, 14C cal); Katla 1440 (4, reported); Furnas 1441 ± 2 (4, reported); Sete Cidades ?1444 (4, reported); **Pinatubo 1450 ± 50 (VEI 5, 15.13 N 120.35 E, 14C calibrated)**; Aira (Sakurajima) 1471 (5, reported); Bardarbunga/Veiðivötn 1477 (6, reported); St Helens 1480 Wn (5, dendro); St Helens 1482 We (5, dendro).
- **Northern Hemisphere eruptions with no VEI whose dates sit near 1452:** Iraya (Batanes, 20.5 N) ?1454, reported; Karymsky ?1450, 14C cal; Iwatesan 1450 ± 100, 14C uncal; Rainier 1450 ± 100; Acatenango 1450 ± 50, anthropology; Katla 1450 ± 50 and Grimsvötn 1450 ± 10 (ice core); Pelée 1460 ± 20 (14C uncal); Sashiusudake 1460 ± 30.
- **Coverage test (cover.py):** 59 eruptions with VEI ≥ 4 or unknown have a year ± uncertainty interval that contains 1452. Only three have VEI ≥ 5: Pinatubo 1450 ± 50 (VEI 5), El Chichón 1360 ± 100 ("Tephra unit B", VEI 5, 17.4 N), and nothing else at VEI 6 or above. Aniakchak 1540 ± 100 and Augustine 1540 ± 100 are VEI 4. Melebingoy 1380 ± 75 (Mindanao, 6.1 N) is VEI 4.
- **Kuwae in the current table:** the only pre-1897 Kuwae entry is **1425 ± 5, VEI blank, 14C calibrated**. The table has no 1452/53 Kuwae eruption. GVP's own entry therefore no longer supports the old Kuwae-1452 link.

**For the dive:** the Pinatubo row (VEI 5, 15 N, 1450 ± 50) and the El Chichón Unit B row (VEI 5, 17 N) are the only VEI ≥ 5, low-latitude NH rows whose stated intervals cover 1452. Both rest on 14C. A rough calibrated range for the Buag-age Pinatubo charcoal (USGS Newhall table, ~318–511 cal BP) also overlaps 1452. That is a database coincidence, not a candidacy: I found no paper that proposes either volcano for 1453. Burke et al. 2023 (below) also argue against a tropical source.

## 2. LaMEVE and other catalogs

- **LaMEVE** (BGS, part of VOGRIPA): covers magnitude ≥ 4 Quaternary eruptions, with 1,883 records in 2014. It is searchable at `http://www.bgs.ac.uk/vogripa` (now `www2.bgs.ac.uk/vogripa`) and exports to spreadsheet. Fields include magnitude, VEI, deposit volume, date and rock type. Paper: Crosweller et al. 2012, *J. Appl. Volcanol.* 1:4, https://link.springer.com/doi/10.1186/2191-5040-1-4 (SCHOLARLY). I did not confirm that the portal still works in 2026, and I did not pull 1400–1500 records.
- **TephraKam** (Kamchatka glass geochemistry): 7,049 EPMA analyses covering about 300 explosive eruptions, CC-BY. Portnyagin et al., *ESSD* 12:469 (2020), https://essd.copernicus.org/articles/12/469/2020/ (SCHOLARLY). It is useful for fingerprinting cryptotephra if a 1453 glass shard is ever found.
- Avachinsky/Koryaksky/Kozelsky Holocene tephra dataset, Mendeley, DOI 10.17632/68n8sfcggh.1 (SCHOLARLY data deposit).
- I did not check the Japan (AIST), Alaska (AVO GeoDIVA), Mexico, Central America, Indonesia or Philippines regional databases. See Unverified claims.

## 3. Candidate sources for 1452/53, as the literature has them

**No published paper names a source volcano for UE 1453.** The sources I checked all say the source is unidentified.

| Candidate | Status | Basis | Source (tier) |
|---|---|---|---|
| Kuwae (Vanuatu, 16.8 S) for 1452/53 | **Rejected for 1453.** It belongs to the 1458 discussion, and even there it is disputed. | The 1452/53 dating was an artefact of Antarctic chronologies tied to the 1453 tree-ring minimum. Accurately dated cores give 1458. The 1453 sulfate is weighted toward Greenland. | Abbott et al. 2021, *Clim. Past* 17:565, https://cp.copernicus.org/articles/17/565/2021/ (SCHOLARLY); Sigl et al. 2013 and Cole-Dai et al. 2013 cited via https://en.wikipedia.org/wiki/1452/1453_mystery_eruption (SECONDARY) |
| Kuwae for 1458 | Disputed | SPICEcore 1459 glass is rhyolitic (~75 wt% SiO2, FeO ~2); similarity coefficient ~0.5 against Kuwae; "inconsistent with any known Kuwae eruptive products" | Hartman et al. 2019, *Sci. Rep.* 9:14437, https://pmc.ncbi.nlm.nih.gov/articles/PMC6783439/ (SCHOLARLY) |
| Kaharoa/Tarawera (NZ), El Misti (Peru), Malta Plateau (Antarctica) | Rejected for 1458 | Kaharoa dates to 1314; El Misti's SiO2/K2O does not match; Malta Plateau FeO is too high | Hartman et al. 2019 (SCHOLARLY) |
| Mt Reclus (Patagonia) | Tentative for 1458 only | Similarity coefficient 0.7–0.8; "possibly an unknown Reclus eruption" | Hartman et al. 2019 (SCHOLARLY) |
| "NH low-latitude volcano" | Older inference | Greenland deposition 25 kg/km² against Antarctica 5 (~83% stayed in the NH) | Abbott et al. 2021 (SCHOLARLY) |
| "NH extratropical volcano" | **Current best constraint** | Tunu2013 δ34S/Δ33S: nonzero Δ33S (the plume reached the stratosphere); the initial 1453 sulfate has Δ33S ≈ 0 and low δ34S, like Katmai 1912 and Aniakchak II; only ~54 ± 6% of the 1453 sulfate came from the stratospheric overworld | Burke et al. 2023, *PNAS* 120(47):e2221810120, https://pmc.ncbi.nlm.nih.gov/articles/PMC10666123/ (SCHOLARLY) |

The latitude question is contested in a mild way. Wikipedia and older work say "low-latitude NH". Burke et al. 2023 argue for the NH extratropics, citing an earlier reference (their ref. 50, which I did not identify). That favours an Alaska, Aleutian, Kamchatka, Kuril, Japan, Cascades or Iceland source over Mexico or the Philippines. If it holds, it cuts against the two GVP VEI-5 coincidences above.

Tephra: none has been found for the 1450s peaks. Abbott et al. 2021 list a tephra search in the 1450s as future work. Cole-Dai et al. 2013 likewise report no tephra (via SECONDARY). Sulfur injection is about 11 Tg S per Sigl et al. 2022, *ESSD* 14:3167 (via SECONDARY; not checked against the paper).

Superseded figures: Gao et al. 2006 (*JGR* 111:D12107) gave a single 1452/53 Kuwae deposition of 93 kg/km² (Antarctica) and 45 kg/km² (Greenland). That merges two events and is superseded (via SECONDARY).

## 4. Radiocarbon-dated eruptions whose ranges cover 1452

The GVP stores 14C dates as one central year plus one ± value, with the method tag `Isotopic: 14C (calibrated)` or `(uncalibrated)`. The calibration curve and the calibrated range are not stored. Rows with ranges covering 1452 and VEI ≥ 4 or unknown include:

- **14C calibrated:** Pinatubo 1450 ± 50 (VEI 5); El Chichón 1360 ± 100 (VEI 5); Merapi 1440 ± 100 and Sambisari Ash 1380/1480 ± 300; Akutan 1420 ± 100; Aniakchak 1470 ± 20; Rainier 1450 ± 100; Akita-Yakeyama 1390 ± 75; Ichinsky 1300 ± 200; Kuchinoerabujima 1440/1470 ± 50; Soufrière Hills 1480 ± 50; Melebingoy 1380 ± 75 (VEI 4).
- **14C uncalibrated:** Iwatesan 1450 ± 100; Kikai 1430 ± 75; Pelée 1460 ± 20; Sashiusudake 1460 ± 30; Kusatsu-Shirane 1470 ± 150; Soufrière St Vincent 1395 ± 75 and 1480 ± 150.

The uncalibrated rows matter. Around 1450 CE a raw 14C year can sit decades away from the calendar year, so each would need recalibration from the original lab age before it could be ruled in or out. The full list of 59 is printed by cover.py.

## Unverified claims

- From memory: GVP formerly listed Kuwae 1452 as VEI 6. The current table shows only 1425 ± 5. I did not check when or why it changed.
- From memory: the GVP website offers an Excel export of search results, and there is a VOTW version/DOI citation string (e.g. "VOTW v5.x"). Those pages returned 403, so this is unchecked.
- My reading that `Isotopic: 14C (uncalibrated)` years are simply 1950 − BP is an inference from memory, not GVP documentation.
- The identity of Burke et al. 2023's ref. 50 (the earlier "NH extratropical" proposal) is unknown.
- The Buag-period identification and VEI 5 for the Pinatubo 1450 ± 50 row are unchecked. The USGS Newhall table (https://pubs.usgs.gov/pinatubo/newhall/table1.html, SCHOLARLY/PRIMARY) was seen only through a search snippet, and its column layout was ambiguous.
- Pang 1993 (JPL press release, POPULAR/CLAIMANT): Kuwae in early 1453, seen via SECONDARY only.
- I did not survey the regional databases (AIST Japan, AVO GeoDIVA, Mexican, Central American, Indonesian or Philippine catalogs), the Global Holocene tephra compilations (e.g. Tephrabase), or LaMEVE's 1400–1500 rows. I found no sourced claim that any Mexican, Central American, Indonesian, Philippine, Kamchatkan, Alaskan or Icelandic volcano has been proposed for 1453.
- I did not find, in the sources fetched, any 2024–2026 paper that identifies the source. One search turned up an EGU26 abstract on cryptotephra methods (https://meetingorganizer.copernicus.org/EGU26/EGU26-18473.html), but I did not read it.
