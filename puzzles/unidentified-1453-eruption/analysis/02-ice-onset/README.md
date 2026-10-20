# 02 — Ice onset, Antarctic significance, structure

**Questions.**
1. Has anyone published a tephra search of the 1453 layer in a Greenland core?
2. Where in the annual cycle does the 1453 sulfur rise begin, and what eruption
   window does that imply, calibrated on eruptions of known date in the same core?
3. Is the Antarctic 1453 sulfur above background, core by core? (H4)
4. Is the 1453 rise one pulse or several? (H9)

## 1. Shard search (literature)

| Core | 1453 layer searched for tephra? | Evidence | Tier |
|---|---|---|---|
| TUNU2013 | **Not searched, as published.** | Abbott 2021 sampled only 78.315–78.655 m (1477–1479; Sect. 3.2 and Fig. 3, p. 570). Sect. 5.2, p. 577: "Further studies of sulfur isotopes coupled with attempts to identify tephra associated with both events in the 1450s CE ... could aid in conclusively identifying their sources." Plunkett 2023 Table 1 (p. 6) lists every Common Era tephra reported from Greenland ice, with 2.2 adding new TUNU2013 samples; between 1254/5 and 1477 it lists none. Its sampling followed microparticle peaks. | SCHOLARLY |
| NEEM-2011-S1 | **Not searched, as published.** | Sigl 2015 SI (MOESM47) has tephra for 536 CE only. Plunkett 2023 Table 1 has no NEEM 1450s entry. | PRIMARY / SCHOLARLY |
| NGRIP, GRIP, Dye-3, GISP2 | **Unknown.** | Coulter et al. 2012 (JGR 117, doi:10.1029/2012JD017698) sampled "sub-sections of three Greenland cores" for chosen eruptions. Plunkett 2023 Table 1 carries its positives (none in the 1450s), but the list of negative intervals is in the full text, which Wiley refused (403). | — |
| Summit cores (Cole-Dai 2013) | **Unknown.** | Cole-Dai et al. 2013, JGR 118:7459–7466, studied "recently obtained West Antarctica and central Greenland ice cores" (abstract, via Crossref): WAIS Divide plus central Greenland. The abstract does not mention tephra. The "lack of tephra discoveries" sentence comes from Wikipedia, citing this paper. Full text refused (403, pdfdirect and abstract page), so **the passage and its page are not verified.** | SECONDARY for the attribution |
| Antarctic (Vostok VK22, Dome C, South Pole) | Searched at 1458 only. | Ro 2025 (Commun. Earth Environ. 6:828) analyses 1458/59 glass and does not report 1453 shards. EGU25-2329 is also about 1458 (survey). | SCHOLARLY |

eVolv2k v4 gives tephra detected = N for 1453. In this file N cannot tell
"searched, none found" from "not searched".

**Verdict.** No published work reports a tephra search of the 1453 layer in
TUNU2013 or NEEM-2011-S1. Abbott 2021 lists it as future work. For NGRIP and the
Summit cores it is unknown: the two papers that might hold a negative result
are behind Wiley's 403.

## 2. Onset season — `onset.py`

**Method** (in the script docstring, fixed before 1453 was run).
nssS = S − 0.084 Na (the sea-salt ratio in the Sigl 2014 SI). Background is
[Y−8, Y), with Y the eruption year (1452 for UE 1453). The threshold is median
+ 3 × 1.4826 MAD. Onset is the first of three consecutive samples above the
threshold, reported at the midpoint of the gap before it. Sensitivity runs use
k = 2–4 and L = 2–4. Two alternative definitions: 20 % of the peak excess, and
a residual with the seasonal cycle removed. Seasonal markers are the nearest Na
(winter–spring), Ca (spring) and NH4 (summer) maxima either side of the onset.
Calibration lag = onset (NS1-2011 decimal age) − eruption date.

Quality rules added **after** the first run: drop events after 1900, because
industrial sulfate triples the background (Agung, El Chichón and Pinatubo were
lost in it). Drop events with peak excess under 1.5 × the threshold excess.
Both runs are reproducible from the script.

**Result** (`results/onset.txt`).
- UE 1453 onset in NEEM-2011-S1: **1453.13 ± 0.05** (NS1-2011), 143.11 m. It
  is stable across all nine (k, L) settings and all three definitions. It sits
  **0.05 yr after the Na maximum, at the Ca maximum, and 0.43 yr after the
  preceding NH4 maximum**, so it falls in the winter–spring layer.
- TUNU2013 (Abbott S9, monthly): onset 1453.00 ± 0.04, also 0.04 yr after the
  Na maximum. The two cores agree within 0.13 yr.
- Calibration onsets, measured from the preceding Na maximum: Laki 0.06
  (erupted June), Tambora 0.05 (April), Krakatau 0.02 (August), Huaynaputina
  0.13 (February), Hekla 1766 0.40, Katla 1755 0.31. **Large eruptions of
  every month begin at the winter–spring Na maximum.** The position of an onset
  in the layer does not give the eruption month.
- Lags in NS1-2011 age (onset − eruption), clean events only. NH extratropical:
  Laki −5.8, Katla −6.4, Hekla +2.8 months. Tropical: Krakatau +0.7, Tambora
  +8.9, Huaynaputina +13.5 months. The negative Laki lag shows that the
  NS1-2011 fraction of a year is not a calendar.
- Implied eruption date for 1453 (onset − lag range, widened by onset
  sensitivity): **NH-extratropical analogues 1452.9–1453.7; tropical
  analogues 1452.0–1453.1.** Together: early 1452 to mid-1453. This brackets
  Abbott's "1452 or early 1453". It does not narrow the season.

## 3. Antarctic significance (H4) — `antarctic.py`

**Data.** Sigl 2015 SI MOESM46: per-core annual nssS for 15 cores covering 1453
(AVS-2k, WD2014 years), WDC06A monthly nssS, and the AVS-2k event and
composite tables. **Test.** Background years 1420–1446 and 1464–1476. Robust
z for 1453 and 1454. Empirical p = 2 × the share of background years at or
above max(1453, 1454).

**Result** (`results/antarctic.txt`).
- Five of 15 cores are above background at p < 0.05: WDC06A (z1454 6.7),
  SP01 (6.5), SP04 (7.5), EDC96 (5.5), DFS10 (4.2). Chance predicts 0.8; the
  binomial P(≥ 5) = 0.0006. Three more have z ≥ 3.5 but p = 0.05–0.10: B40,
  NUS07-2, DML07. Talos Dome, Taylor Dome, NUS07-5 and DF01 show nothing.
- Network mean z: 1454 is +3.64, higher than all 40 background years; 1453 is
  +2.36, beaten by 1 of 40. (The 1464–1476 background still carries the 1458
  tail, so this is conservative.)
- WDC06A monthly: one smooth rise from 1453.6, peaking at about 30 ng/g at
  1454.0, back to background by 1454.8 (WD2014). That is about half a year after
  the Greenland onset, on an independent timescale.
- Event-only records: Law Dome DSS, Siple, Dyer, Plateau Remote and Dome A list
  no 1453 event. AVS-2k composite: 5.12 ± 0.78 kg km⁻² (s.e.m.), rank 55.
  Sigl 2014 SI Table S4 gives detection in ne = 10 cores.
- Dome C isotopes (Gautier): the one sample at 1453.6 has fV 0.08, but EDC96
  sulfate in the same region is at z 5.5. The isotope sample probably sits off
  the peak. These are separate records on separate timescales.

**Verdict.** The Antarctic 1453 deposit is real. It is not background. The test
cannot tell whether it is the same plume or a separate small event. Its
half-year delay behind Greenland fits stratospheric cross-equator transport.

## 4. Structure (H9) — `structure.py`

**Rule** (in the docstring, fixed before counting): bin monthly, subtract the
background seasonal climatology, take a 3-month running mean, threshold at
3 sMAD. Two maxima count as separate pulses only if the trough between them
falls below 50 % of the smaller one.

**Result** (`results/structure.txt`). There is one episode and one pulse in each
high-resolution core.
- TUNU2013: 1453.00–1453.92, peak +78 at 1453.33, smooth decay.
- NEEM-2011-S1: 1453.17–1454.25. Main peak +27 at 1453.42, then a second
  maximum of +23 at 1454.00 over a trough of +17. That fails the rule, and the
  second maximum coincides with the 1454 Na/Ca seasonal maximum.
- WDC06A: 1453.50–1454.83, a single peak.
- NGRIP (5 cm, about 4 samples a year): 50, 46, 28, 53, 47 ppb. The one-sample
  dip is below what the rule can resolve.
- Burke 2023 TUNU2013 Δ33S: +0.14, +0.12, +0.18, +0.32, +0.31, +0.18, then
  −0.04 to −0.18. That is one positive-then-negative excursion, the signature
  of a single stratospheric pulse.

**Verdict.** No evidence for more than one eruption. Two eruptions weeks apart
would not separate in sulfate at this resolution; only glass could show that.

## Run

```
python3 -I fetch.py data            # downloads; prints sha256
python3 -I xlsx2tsv.py "data/abbott_supp/x/Supplementary Data Tables S1-S10.xlsx" data/abbott_supp/tsv
python3 -I xlsx2tsv.py data/burke2023/Burke_2023_PNAS.xlsx data/burke2023/tsv
python3 -I xlsx2tsv.py data/sigl2015/moesm45.xlsx data/sigl2015/t45
python3 -I xlsx2tsv.py data/sigl2015/moesm46.xlsx data/sigl2015/t46
python3 -I xlsx2tsv.py data/sigl2015/moesm47.xlsx data/sigl2015/t47
python3 -I onset.py data/neem2011s1.tab data/abbott_supp/tsv/sheet9.tsv > results/onset.txt
python3 -I antarctic.py data/sigl2015/t46/sheet7.tsv data/sigl2015/t46/sheet4.tsv data/sigl2015/t46/sheet8.tsv data/sigl2015/t46/sheet9.tsv data/domec_isotopes.tab > results/antarctic.txt
python3 -I structure.py data/neem2011s1.tab data/abbott_supp/tsv/sheet9.tsv data/sigl2015/t46/sheet4.tsv data/sigl2015/t45/sheet13.tsv data/burke2023/tsv/sheet1.tsv > results/structure.txt
```
`data/` is gitignored (62 MB).

## Limits
- Onset is a depth-domain threshold crossing. CFA dispersion and uneven
  seasonal snowfall make within-year timing coarse. The calibration has only
  three clean events per class, so the lag ranges are wide and could be wider.
- The NS1-2011 age model is tied at Laki, Tambora and Krakatau. Lags for those
  events are measured on ages partly set by them. The year is fixed, but the
  fraction within the year is not.
- Eruption dates used: GVP cache for Katmai, Hekla 1766, Katla 1755, Cosigüina,
  Santa María, Shiveluch. Climactic dates for Pinatubo (15 Jun, USGS via
  search), Agung (17 Mar) and El Chichón (4 Apr) (GMD table via search), and
  Laki (8 Jun, POPULAR lecture notes). Tambora 10 Apr 1815 and Krakatau 27 Aug
  1883 were not verified this session. Month-level errors would not change the
  result.
- Antarctic annual means sit on WD2014 through volcanic synchronisation, so
  cores can be a year off. That is why the max of 1453 and 1454 is used. Cores
  are not independent (SP01/SP04, DF01/DFS10), so the binomial overstates
  significance somewhat.
- TUNU2013 depths differ about 0.2 m between Abbott S9 (1453 peak at 81.81 m)
  and Burke S01 (82.02–82.05 m). Different depth registrations; ages agree.
- The Sigl 2015 class for 1453 is "1, tropical" (MOESM47). eVolv2k v4 has
  45° N after Burke. These are records of the revision, not results here.

## Walls
- **Cole-Dai 2013 and Coulter 2012 full texts** (Wiley 403). Breached by
  library access or a repository copy. Needed to settle whether NGRIP or the
  Summit cores were ever searched at 1453.
- **Unpublished sampling.** Whether DRI or QUB have sampled TUNU2013 or NEEM
  at 1452.5–1453.5 is unknowable from the literature. Asking them is Greg's
  decision.
- **Season.** Sulfate onset sits at the winter–spring maximum whatever the
  eruption month, so ice sulfate alone cannot give the eruption season.
  Breached only by glass timing (shards before the sulfate, as for 1831) or by
  documentary dates (experiment 05).

## Provenance

| File | URL | Fetched | sha256 | Changes |
|---|---|---|---|---|
| neem2011s1.tab | https://doi.pangaea.de/10.1594/PANGAEA.940553?format=textfile | 2026-10-20 | 0ab79ea5c956d36a57768280fc1239e1d8c5911abb78e6fd41ab3e2fb9e5105d | none |
| evolv2k_v4.tab | https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile | 2026-10-20 | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 | none |
| domec_isotopes.tab | https://doi.pangaea.de/10.1594/PANGAEA.895169?format=textfile | 2026-10-20 | 6361944e0fcac45ff509814fa75477263c3b770b9bae501fbf30d7b52ac78763 | none |
| abbott_supp/supp.zip | https://cp.copernicus.org/articles/17/565/2021/cp-17-565-2021-supplement.zip | 2026-10-20 | 00a4055f0e22526dfaf2c1d5c2f9bdb9072d91a71f4351b6b73cff164591a4f7 | unzipped; xlsx → TSV |
| burke2023/Burke_2023_PNAS.xlsx | https://github.com/St-Andrews-Isotope-Geochemistry/Burke_2023_PNAS | 2026-10-20 | 45c88c976ab9bdf72b24fd505f846f74dc8f55052f04657febd7f5d8a70b967e | xlsx → TSV |
| sigl2015/moesm45.xlsx (Greenland SI) | Sigl 2015 Nature SI, MOESM45 (URL in fetch.py) | 2026-10-20 | 0d280cbb6149b07bd156db3d6659c7f49b7f5d95688f8d13c784c172d18b22e8 | xlsx → TSV |
| sigl2015/moesm46.xlsx (Antarctic SI) | Sigl 2015 Nature SI, MOESM46 | 2026-10-20 | 5cd8096c6c1198366e78c97fb1bc6301b407c069722be436f0ae4a2476fb5c54 | xlsx → TSV |
| sigl2015/moesm47.xlsx (forcing, tephra) | Sigl 2015 Nature SI, MOESM47 | 2026-10-20 | 7a056c2a630bbd16efa7eb936c457e04895edfb2067aa2771e44244961d78b23 | xlsx → TSV |
| lit/abbott2021.pdf | https://cp.copernicus.org/articles/17/565/2021/cp-17-565-2021.pdf | 2026-10-20 | 46077bbefdfa4a2559e51d82e1790efff8221846b53e4e0eb142a4a9efd8333e | pdftotext |
| lit/plunkett2023_qsr.pdf | https://par.nsf.gov/servlets/purl/10456052 | 2026-10-20 | 81eab84a2e7e990c8aa28314e5529e638dc204631f6db46b125d40822c56f9e2 | pdftotext |
| lit/sigl2014_si.pdf | Sigl 2014 Nat. Clim. Change SI, MOESM272 (URL in fetch.py) | 2026-10-20 | 4b81361cf1f143c28541c83b21c2465efbe8158ec94f81677f0da29b1244d651 | pdftotext |

Checked and not used: PANGAEA.974172 (19 Antarctic cores, annual, but only
1530–1760). PANGAEA.995655 returned 401 (gated). Other files left in `data/`
from exploration are not inputs.
