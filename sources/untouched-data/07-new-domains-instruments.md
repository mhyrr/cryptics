# 07 — New domains: physical-science and instrument archives, public sensor networks

*Survey, 2026-10-15. Brief: `sources/untouched-data/BRIEF.md`. Rules 1, 2, 3, 6, 7 of
`AGENTS.md` apply. No discovery was attempted (Rule 9). Searches were run through the
WebSearch tool. Several `.gov` hosts (ntrs.nasa.gov, ares.jsc.nasa.gov, gwosc.org) did
not resolve from this container, so some facts rest on search-result snippets. Those
are marked where they drive a score. Two S3 buckets were checked live with `curl`
(USGS historical topo GeoTIFFs and NEXRAD Level II); both list without credentials.*

## Summary (best bets)

1. **Historical USGS topo maps → undocumented orphaned oil/gas wells.** About 190k free georeferenced scans. One published sweep covered four counties in CA/OK and flagged 1,301 candidates. The registry diff is the verifier and the payoff is methane abatement. This is the pilot.
2. **NEXRAD × GOES-GLM → unrecovered meteorite falls.** Radar detection still starts from a known fall time. Fries counts 33 "unrecovered probable falls" already. GLM provides trigger times that need no eyewitness. Both archives are free on AWS.
3. **Unattributed ice-core eruptions × glass-geochemistry databases.** The 1831 "mystery eruption" was solved in 2025 by matching tephra chemistry. Dozens of sulfate spikes still have no source.
4. **Public metabolomics MS/MS repositories (GNPS/MassIVE).** Roughly 90–95% of spectra are unannotated. Repository mining has already found 139 previously undescribed bile-acid conjugates. The verifier is a synthetic standard, which is a real bottleneck.
5. **Reflection-seismic archives released for oil and gas (NLOG, UK, USGS NAMSS) → buried impact craters.** Nadir and Silverpit came out of exactly this data. Payoff is high, but the verifier (drill core) is slow.

---

### 1. Historical USGS topographic maps → undocumented orphaned wells (UOWs)

- **Data**: USGS Historical Topographic Map Collection (HTMC). It holds every edition and scale of USGS quads from 1884–2006, about 190,000 scans, georeferenced. It was made for general mapping. The GeoTIFFs are in a public S3 bucket, `s3://prd-tnm/StagedProducts/Maps/HistoricalTopo/GeoTIFF/<STATE>/`, and I checked that it lists without credentials (≈14 MB per 1:24k sheet). As a federal work it is presumably public domain (license not confirmed, see Unverified). The registries to diff against are state well databases, e.g. PA DEP "Oil Gas Locations – Conventional Unconventional" (PASDA dataset 1088).
- **Question / what a find looks like**: a well symbol printed on a historical quad that sits more than 100 m from any registered well, persists across editions, and shows a surface expression (a clearing, a pipe, a magnetometer anomaly).
- **Gap evidence**: Ciulla et al. (ES&T, Dec 2024, LBNL/CATALOG) ran a U-Net over **four counties** in California and Oklahoma. It flagged 1,301 potential UOWs. They confirmed 29 by satellite imagery and 15 by field magnetic survey. US UOW estimates run from 310k to 800k, and a LANL slide estimates about 340k undocumented unplugged wells in Pennsylvania alone. Most historical oil states (PA, NY, OH, WV, KY, KS, TX, IL) have no published map sweep.
- **Verifier**: (a) mechanical: the distance to the nearest registered well. (b) Independent imagery: NAIP or older aerials at the candidate. (c) The authoritative check is a state agency field visit (magnetometer, methane sniff). Federal orphan-well plugging money (DOE/NETL, CATALOG consortium) gives the result somewhere to go.
- **Precedent**: Ciulla et al. 2024, above (SCHOLARLY via LBNL news; POPULAR coverage).
- **Recipe**: code downloads the quads for target counties, then detects well symbols (template matching for the open-circle and sunburst well glyphs; a small CNN is optional). Next it geolocates each detection from the GeoTIFF transform, diffs against the registry with a 100 m buffer, and requires the symbol to persist across two or more editions. An LLM reads map legends and edition notes (symbol conventions changed over time), triages ambiguous crops, and drafts the agency report. The LLM does not decide what is a well.
- **Cost**: CPU only. One county is about 20–60 quads × editions, about 1–3 GB, a few hours. A whole state is days on one VM, about $10–50.
- **Traps**: digits "0", "9" and "o" misread as well symbols (named in the LBNL work). Water wells and windmills share glyphs on some editions. Registry coordinates can be off by more than 100 m, so a "new" well may be a mislocated registered one. Wells plugged but never mapped. Map-scan stains.
- **Crowding**: `PARTLY`. The CATALOG consortium (LBNL, LANL and others under DOE) owns the method and mentions PA in its slides. Published results cover CA/OK only. Coordinate with them; do not compete.
- **Ethics**: wells sit on private land. Do not publish coordinates; report them to the state agency. Trespass risk if hobbyists go "verifying". No privacy issue.
- **Scores**: data_ready 5 · gap 4 · verifier 4 · cheapness 4 · payoff 5 · ethics_clear 4
- **Sources**:
  - https://newscenter.lbl.gov/2024/12/04/ai-helps-researchers-dig-through-old-maps-to-find-lost-oil-and-gas-wells/ (SECONDARY, institutional summary of SCHOLARLY paper)
  - https://www.popsci.com/technology/ai-oil-wells/ (POPULAR)
  - https://catalog.energy.gov/wp-content/uploads/2024/08/DOE-UOWP-Slides-July_2024.pdf (PRIMARY, program slides)
  - https://pubs.usgs.gov/fs/2011/3009/pdf/fs2011-3009.pdf (PRIMARY, HTMC fact sheet)
  - https://prd-tnm.s3.amazonaws.com/?list-type=2&prefix=StagedProducts/Maps/HistoricalTopo/GeoTIFF/PA/ (PRIMARY, checked live 2026-10-15)
  - https://geo.btaa.org/catalog/pasda-1088 (PRIMARY, PA well registry metadata)

### 2. NEXRAD Level II × GOES-GLM bolides → unrecovered meteorite falls

- **Data**: NEXRAD Level II, about 160 WSR-88D radars, collected for weather. The archive starts in the 1990s and is free on AWS at `s3://unidata-nexrad-level2/YYYY/MM/DD/SITE/`. It moved from `noaa-nexrad-level2` in Sept 2025; I checked it live. GOES-16/17/18 GLM is a lightning mapper whose bolide pipeline publishes more than 3,300 bolides at neo-bolide.ndc.nasa.gov (readable with the `bolides` Python package). The Global Meteor Network has more than 1,600 cameras and CC BY 4.0 trajectories.
- **Question**: a radar return in the dark-flight column below a bolide's terminal point, at the right time, falling at the right rate. That gives a strewn field.
- **Gap evidence**: the 2017 AMSNEXRAD paper says detection is "manual and dependent on prior accurate knowledge of the fall time and estimated ground track". It is triggered by eyewitness fireball reports. A 2024 Fries NTRS review counts **34 recovered falls and 33 unrecovered probable falls** since the late 1990s (from a search snippet; full text not reachable). So falls with no eyewitness (daytime, rural, overcast, pre-AMS-app) are under-searched. GLM detections are independent of eyewitnesses.
- **Verifier**: radar signatures at multiple sites and sweeps with a consistent fall-speed profile, plus a GLM or GMN light curve. The definitive check is a recovered meteorite, confirmed by a meteoriticist and a Meteoritical Bulletin entry. Fries (ARES) and the AMS are the people to hand candidates to.
- **Precedent**: Park Forest 2003 searches were guided by radar. Sutter's Mill, Cranfield MS 2022 (four radars, more than 10 stones), McDonough GA (12 radars, 53 sweeps) and Amo IN 2025 (six radars) all followed. Jenniskens et al. 2018 used GLM to recover a fall. All SECONDARY/SCHOLARLY, see sources.
- **Recipe**: code takes GLM bolide times and positions over CONUS from 2017 on, plus AMS events with no radar check. For each one it pulls ±15 min of Level II from the 3–6 nearest radars and masks precipitation with a dual-pol correlation coefficient. It then searches for compact, low-reflectivity returns descending along the projected dark-flight path. Calibrate on Fries's known falls first (Rule 7): the pipeline must recover them blind. An LLM writes the candidate dossiers and cross-reads AMS witness text. It does not judge the radar returns.
- **Cost**: CPU only. One event is about 6 radars × 4 volumes × 5 MB. Py-ART handles decoding. Hundreds of events take a day on a laptop.
- **Traps**: birds, insects and chaff (bioscatter is the dominant false positive). Aircraft, ground clutter and anomalous propagation. Precipitation. Space-debris re-entries and rocket stages that look like bolides in GLM. GLM's false-detection history: early precision was about 1.5%, later about 80%.
- **Crowding**: `PARTLY`. Fries/ARES and AMS run this for reported events. A systematic GLM-triggered back-sweep is not published as far as I found (see Unverified).
- **Ethics**: strewn fields often fall on private land, and meteorites are property of the landowner in the US. Release coordinates to recovery teams, not to the public, at first. No privacy issue.
- **Scores**: data_ready 5 · gap 4 · verifier 4 · cheapness 4 · payoff 4 · ethics_clear 4
- **Sources**:
  - https://registry.opendata.aws/noaa-nexrad/ (PRIMARY)
  - https://mailinglists.unidata.ucar.edu/archives/data-service-announce/2025/msg00005.html (PRIMARY, bucket move)
  - https://karmaka.de/?p=11760 (abstract mirror of Hankey et al. 2017, *Planet. Space Sci.*, SCHOLARLY)
  - https://ntrs.nasa.gov/citations/20240005795 (SCHOLARLY, Fries 2024 review; snippet only)
  - https://ares.jsc.nasa.gov/meteorite-falls/events/cranfield-ms (PRIMARY)
  - https://arxiv.org/pdf/2106.09189 (SCHOLARLY, GLM pipeline)
  - https://bolides.readthedocs.io/ (PRIMARY, tooling)
  - https://cisess.umd.edu/update-geostationary-lightning-and-meteor-mapper/ (SECONDARY, Jenniskens 2018 GLM recovery)
  - https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-92.html (SCHOLARLY abstract, GMN)

### 3. Unattributed ice-core eruptions × volcanic-glass geochemistry databases

- **Data**: eVolv2k v4 (500 BCE–1900 CE): 256 eruptions from 3 Greenland and 18 Antarctic cores, on PANGAEA. D4i (Sigl, McConnell & Toohey 2023, PANGAEA). Published cryptotephra glass analyses are in paper supplements. GEOROC holds open glass, whole-rock and mineral compositions; curation moved from MPIC to the IAG in 2025. The Smithsonian GVP eruption list is the eruption catalogue. These were collected for climate forcing and petrology, not for source attribution.
- **Question**: for each bipolar or NH sulfate spike with no source, is there a volcano whose glass composition (major elements, and trace elements where available) matches published ice-core shards? Or, failing that, a short list that tells field volcanologists where to sample?
- **Gap evidence**: D4i alone adds 35 eruptions (1733–1895) not in eVolv2k. Only 21 of its events match eVolv2k entries, and 11 more are "tentatively attributable" to GVP VEI-4 events. eVolv2k handles unidentified events probabilistically (split into tropical and extratropical), which shows how many lack sources. The 1831 event was misattributed (to Ferdinandea) until 2025.
- **Verifier**: geochemical match statistics such as similarity coefficients and multivariate distance on oxides, which a script computes. Then radiocarbon or historical dating of the candidate deposit, and new microprobe analyses by a tephra lab (the final authority).
- **Precedent**: Hutchison et al. 2025, *PNAS* 122(1) e2416699122. Low-K andesite-dacite glass shards in summer-1831 ice match the youngest Plinian eruption of Zavaritskii caldera (Kurils), and the match is consistent with about 13 Tg S and the 1831–33 cooling (SCHOLARLY).
- **Recipe**: code builds a table of every published ice-core glass analysis with depth, age and shard count. It normalises oxides and matches against GEOROC glass and whole-rock data, filtered to volcanoes active in the age window per GVP, using statistical distance and a check against analytical uncertainty. Calibrate on known matches (Tambora 1815, Laki 1783, Zavaritskii 1831) before trusting new ones (Rule 7). An LLM extracts tables from paper supplements (the PDF→table step) and drafts hypotheses, with every value checked against the source.
- **Cost**: CPU, hours. The main labor is curating published shard data, which is the LLM-assisted part.
- **Traps**: geochemical non-uniqueness. Many arc andesites look alike in major elements, so one match is not an identification. Ice-core shards are tiny and alkali loss under the microprobe distorts Na. Whole-rock compositions are not glass compositions. Dating mismatches.
- **Crowding**: `PARTLY`. Tephra groups at St Andrews, Bern and DRI do this event by event. I found no published database-wide automated cross-match (see Unverified).
- **Ethics**: clear.
- **Scores**: data_ready 3 · gap 4 · verifier 3 · cheapness 4 · payoff 4 · ethics_clear 5
- **Sources**:
  - https://research-portal.st-andrews.ac.uk/en/publications/the-1831-ce-mystery-eruption-identified-as-zavaritskii-caldera-si/ (SCHOLARLY)
  - https://doi.pangaea.de/10.1594/PANGAEA.971968 (PRIMARY, eVolv2k v4)
  - https://doaj.org/article/1b6913a7267d41d8890e3db711fab89f (SCHOLARLY, D4i/eVolv2k comparison, *Clim. Past* 2022)
  - https://uni-goettingen.de/en/georoc/643472.html (PRIMARY)

### 4. Public metabolomics MS/MS repositories (GNPS / MassIVE / MetaboLights) → unknown natural molecules

- **Data**: hundreds of millions of tandem mass spectra deposited by thousands of unrelated studies. One 2023 analysis used 521 million spectra from 1,335 public projects. They were collected for each study's own question. The data are open, with MassIVE and GNPS hosting mzML files.
- **Question**: a recurring unannotated spectrum family that is widespread across studies or specific to a phenotype (e.g. IBD stool), whose fragments suggest a nameable structure. Or "reverse metabolomics": propose a structure, predict or synthesise its spectrum, and search every repository for it.
- **Gap evidence**: typically only about 5% of MS/MS spectra are annotated (about 10% in human samples). A 2025 preprint finds more than half of the high-confidence compounds in 61 public blood datasets are unknown.
- **Verifier**: matching against an authentic standard (synthesis or purchase) on retention time and MS/MS. Until then, a spectral match is a hypothesis, not an identification. That verifier costs a chemist and money. For a hobbyist, the realistic endpoint is a well-evidenced candidate handed to a lab such as the Dorrestein group.
- **Precedent**: Quinn et al. 2020 *Nature* 579:123 (new microbial bile-acid conjugates). Gentry et al. 2024 *Nature* 626:419, "Reverse metabolomics": 145 synthetic bile acids found in public data, 139 never described before, with Crohn's associations.
- **Recipe**: code uses the GNPS/MASST tooling and spectral networking over repository subsets, clusters unannotated spectra, and ranks clusters by cross-study prevalence and metadata association (ReDU metadata). An LLM proposes candidate structure classes from fragment patterns and literature, flagged as hypotheses. Code runs in-silico fragmentation (SIRIUS/CSI:FingerID) to score them.
- **Cost**: a laptop for MASST queries. Clustering a large repository slice needs a cloud VM with tens of GB of RAM, so tens of dollars. Wet-lab confirmation is out of hobby reach.
- **Traps**: in-source fragments and adducts look like new compounds (disputed share; one claim said more than 70% in METLIN, a 2025 preprint says under 10%). Contaminants and plasticizers. Batch effects across studies make "phenotype association" spurious. Isomers are not distinguished by MS/MS.
- **Crowding**: `PARTLY`. The Dorrestein and Wang labs (UCSD) and the GNPS community lead this. The space is vast, so the gap is real.
- **Ethics**: human-sample data are de-identified, but do not link spectra back to individuals (drug use and disease markers are sensitive). Respect each dataset's terms.
- **Scores**: data_ready 4 · gap 4 · verifier 3 · cheapness 3 · payoff 4 · ethics_clear 4
- **Sources**:
  - https://ideas.repec.org/a/nat/nature/v626y2024i7998d10.1038_s41586-023-06906-8.html (SCHOLARLY, Gentry 2024)
  - https://authors.library.caltech.edu/101682 (SCHOLARLY, Quinn 2020)
  - https://www.biorxiv.org/content/10.1101/2025.02.04.636472v2 (SCHOLARLY preprint, dark matter)
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10733301 (SCHOLARLY, repository-scale suspect library; the attribution of the 521M figure to this paper comes from a search snippet)

### 5. Released reflection-seismic surveys (NLOG, UK NDR, USGS NAMSS) → buried impact structures

- **Data**: 2D and 3D seismic reflection surveys shot for hydrocarbon exploration and released after confidentiality expires. The Netherlands (NLOG/TNO) offers non-confidential processed 3D surveys as free downloads from its map; raw field data must be requested. The UK National Data Repository and the USGS NAMSS hold many US offshore 2D lines in SEG-Y. Some web copies omit the trace files.
- **Question**: a circular structure with a central uplift, a terraced or faulted rim and an ejecta or tsunami horizon. Separately, a check of whether known "crater candidates" survive 3D imaging.
- **Gap evidence**: both recent confirmations came from someone looking at exploration data for another purpose. Nadir was found "somewhat by accident" during a seafloor-spreading project. Silverpit was disputed (largely rejected at a 2009 debate) until newer seismic and well samples. Thousands of released surveys have never been screened for impact morphology. This is my inference; I found no systematic screen.
- **Verifier**: morphology criteria are necessary but not sufficient. Shocked quartz or feldspar in a well that penetrated the structure is the field standard, and Silverpit used an existing well. Released well cuttings and logs (also in NLOG and NDR) make that check sometimes possible without new drilling.
- **Precedent**: Nadir crater, Nicholson et al. 2022 *Sci. Adv.* (2D industry seismic), confirmed with 3D in *Commun. Earth Environ.* 2024. Silverpit was confirmed in *Nature Communications* (2025 or June 2026, see Unverified) with shocked quartz from a nearby oil well.
- **Recipe**: code reads SEG-Y (segyio) and extracts horizon time-slices and coherence/curvature attributes. It runs a circular-feature detector, cross-checks against salt-diapir, pockmark and volcanic-edifice catalogues, and lists wells within the structure. An LLM reads well completion reports for "shocked", "breccia" or "suevite" mentions and drafts interpretations. A structural geologist must review.
- **Cost**: 3D surveys run to tens–hundreds of GB each. A cloud VM with 1–2 TB of disk is about $50–200 per country sweep. Interpretation skill is the real cost.
- **Traps**: salt domes, dissolution collapse, pockmark clusters, igneous intrusions and mud volcanoes all make circular structures. The crank history is long: the Deniliquin claim, many "impact" circles that turned out salt-related, and the 2009 Silverpit rejection itself (which went the other way).
- **Crowding**: `OPEN` to `PARTLY` (Nicholson/Heriot-Watt, Gulick/UTIG).
- **Ethics**: clear. Check each repository's licence before publishing images (some UK/NL data carry attribution terms).
- **Scores**: data_ready 3 · gap 3 · verifier 3 · cheapness 2 · payoff 4 · ethics_clear 5
- **Sources**:
  - https://repository.arizona.edu/handle/10150/666081 (SCHOLARLY, Nadir 2022)
  - https://doaj.org/article/d660d4870cc042db88e2cd14120e7fdd (SCHOLARLY, Nadir 3D 2024)
  - https://www.birmingham.ac.uk/news/2025/scientists-find-proof-that-an-asteroid-hit-the-north-sea-over-43-million-years-ago (SECONDARY)
  - https://earthsky.org/space/evidence-ancient-asteroid-impact-north-sea-silverpit-crater/ (POPULAR)
  - https://www.nlog.nl/en/nieuws/new-free-3d-seismic-data-download-map (PRIMARY)
  - https://pubs.usgs.gov/ds/620/html/download.html (PRIMARY, USGS SEG-Y access pattern)

### 6. Annual-resolution tree-ring ¹⁴C (IntCal raw archive) → Miyake-event candidates

- **Data**: the IntCal20 database archive of constituent measurement sets (intcal.org/data.html, also bundled in the R package `rintcal`), plus newer annual ¹⁴C series published since 2020. These were collected for radiocarbon calibration. Ice-core ¹⁰Be and ³⁶Cl records (NOAA Paleo) are the independent check.
- **Question**: a one-year ¹⁴C jump of about 1% or more, replicated in independent trees, that marks an extreme solar particle event. Each one is an exact-year tie point for floating chronologies (Rule 7: a calibrator of datings).
- **Gap evidence**: weak for existing annual data. The `ticktack` package (Zhang, Sharma, Pope et al., *Proc. R. Soc. A* 2022) already fitted "all public annual ¹⁴C tree data". The open gap is screening lower-resolution (5–10 yr) IntCal blocks for step-shaped anomalies, to direct where new annual measurements should go. That is how 12350 BCE and 14300 BP were targeted. A hobbyist produces a ranked target list, not a discovery.
- **Verifier**: strong but external. New annual ¹⁴C measurements on independent trees, plus a coincident ¹⁰Be spike in ice. The 2024 *Radiocarbon* non-replication paper shows the verifier works and kills false candidates.
- **Precedent**: 774/5 and 993/4 CE (Miyake 2012/2013). 664–663 BCE (Panyushkina et al. 2024). 5259 BCE, 7176 BCE, 12350 BCE (Bard et al.) and about 14300 BP (SCHOLARLY, see sources).
- **Recipe**: code fits the `ticktack` carbon box model to each IntCal measurement block. It computes the likelihood of a step injection versus smooth production at each epoch and accounts for the smoothing that decadal blocks impose. It cross-correlates with ¹⁰Be. An LLM compiles the literature list of already-measured windows so the target list excludes them.
- **Cost**: laptop, hours.
- **Traps**: small anomalies that fail to replicate (2024 paper). Inter-lab offsets. Decadal averaging hides or creates steps. Calendar-age errors in floating chronologies.
- **Crowding**: `PARTLY` to `CROWDED` (Miyake, Bard, Brehm/Wacker, Pope groups).
- **Ethics**: clear.
- **Scores**: data_ready 4 · gap 2 · verifier 4 · cheapness 5 · payoff 4 · ethics_clear 5
- **Sources**:
  - https://www.intcal.org/data.html (PRIMARY)
  - https://arxiv.org/abs/2210.13775v1 (SCHOLARLY, ticktack)
  - https://doaj.org/article/b827ec01962f487697f590671ec721f5 (SCHOLARLY, 664–663 BCE)
  - https://www.cambridge.org/core/services/aop-cambridge-core/content/view/87D0F4D228E5F8F856F33B58351935F4/S0033822224000523a.pdf (SCHOLARLY, non-replication)
  - https://www.sci.news/astronomy/strongest-miyake-event-13911.html (POPULAR, 14300 BP)
  - https://arxiv.org/pdf/2603.10345 (SCHOLARLY preprint, SOCOL:14C-Ex, seven events)

### 7. Legacy spacecraft fields-and-particles data (NASA PDS PPI) → overlooked transient structures

- **Data**: magnetometer, plasma-wave and particle data from Pioneer, Voyager, Galileo, Ulysses, Cassini and others, archived at the PDS Planetary Plasma Interactions node. Each mission collected the data for its own science goals. Public domain (NASA).
- **Question**: short transients that the original teams averaged over, such as plasmoids, plume crossings or flux ropes, found at full resolution and checked against MHD models.
- **Gap evidence**: two headline results came from re-reading at higher cadence. The 1997 Galileo E12 Europa pass had a roughly 3-minute, about 200 nT field rotation, explained 21 years later as a plume crossing (Jia et al. 2018). A 60-second plasmoid sat in Voyager 2's 45-hour 1986 Uranus pass, found by plotting at 1.92 s (DiBraccio & Gershman, GRL 2019/2020).
- **Verifier**: weak to moderate. Consistency with simulations and other instruments on the same pass. The real check is a future mission (Europa Clipper, JUICE, a Uranus orbiter), which is years away.
- **Precedent**: above. For calibration, the Pioneer anomaly was resolved by recovered telemetry (Turyshev et al. 2012, PRL 108:241101): data rescue killed an "anomaly" rather than finding one.
- **Recipe**: code runs a systematic high-cadence transient search (wavelet or minimum-variance analysis) over every close flyby in PPI and ranks events by deviation from a background field model. An LLM reads the original mission papers to check whether each event was already reported.
- **Cost**: laptop, days.
- **Traps**: instrument artifacts such as spacecraft maneuvers, range changes and telemetry glitches. Without a model, "anomaly" means nothing. Mike Brown's comment that Europa plume evidence remains "hopeful, rather than truly convincing" is the right prior.
- **Crowding**: `PARTLY`, since mission teams revisit their own data.
- **Ethics**: clear.
- **Scores**: data_ready 4 · gap 3 · verifier 2 · cheapness 4 · payoff 3 · ethics_clear 5
- **Sources**:
  - https://www.jpl.nasa.gov/news/old-data-reveal-new-evidence-of-europa-plumes (SECONDARY)
  - https://news.umich.edu/europas-plumes-new-evidence-from-an-old-mission (SECONDARY)
  - https://www.jpl.nasa.gov/news/revisiting-decades-old-voyager-2-data-scientists-find-one-more-secret/ (SECONDARY)
  - https://www.nature.com/articles/nphys2428 (SECONDARY, Nature News on Pioneer)

### 8. Scanned analogue magnetograms (BGS, Kyoto COMPASS) → historic geomagnetic-storm record

- **Data**: BGS has photographed more than 300,000 analogue magnetograms from UK observatories (1846–1987), all viewable and downloadable. Kyoto WDC's COMPASS serves IIIF images of magnetograms from microfilm and fiche. These were recorded for navigation and geomagnetism; most are **images, not numbers**.
- **Question**: digitise the traces to minute-scale values. Find and size storms between 1850 and 1950 that are missing from or underestimated in existing indices, which feeds the extreme-storm statistics behind grid-risk planning.
- **Gap evidence**: BGS says converting traces to values is "difficult and time consuming". It has been done event by event: 1859 Carrington, 1872 and others (Beggan et al. 2022, 2024, with Hayakawa).
- **Verifier**: mechanical. Hourly means printed in observatory yearbooks, agreement between observatories, and aurora records.
- **Precedent**: Beggan et al. 2024 *Space Weather*, 1859 Greenwich and Kew traces digitised to quasi-minute values (SCHOLARLY).
- **Recipe**: code does trace extraction (colour and contrast segmentation, baseline and scale from the printed calibration), then a yearbook cross-check. An LLM OCRs and reads yearbook tables and scale-value notes; every number it reads is checked against the trace-derived hourly means.
- **Cost**: CPU. About 300k images is about TB scale. A pilot on one observatory-decade takes about a day.
- **Traps**: crossing and overlapping traces during storms (exactly when it matters), off-scale excursions, sign inversions (BGS names these), and paper shrinkage.
- **Crowding**: `PARTLY` (BGS, Hayakawa and coauthors, Kakioka).
- **Ethics**: clear.
- **Scores**: data_ready 4 · gap 3 · verifier 4 · cheapness 3 · payoff 3 · ethics_clear 5
- **Sources**:
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10078682/ (SCHOLARLY, Beggan 2022 GDJ)
  - https://nora.nerc.ac.uk/id/eprint/537008/ (SCHOLARLY, 1859 digitisation)
  - https://wdc.kugi.kyoto-u.ac.jp/iiif_magnetogram/ (PRIMARY)

### 9. Crystallography Open Database → missed symmetry and mis-assigned structures (seed)

- **Data**: COD has about 535k entries (cod.psdi.ac.uk mirror, last deposit 2026-08-10) under CC0. CSD is not open. Materials Project and GNoME are computed, not measured.
- **Question**: structures in a space group too low (missed inversion centre and similar), wrong atom types, or implausible geometry.
- **Gap evidence**: weak. Marsh's surveys found 279 of about 1,300 P1 entries wrong (1999) and 156 of about 100k recent entries in inappropriate space groups (2014). Spek (2018) says such errors are now waning because checkCIF and PLATON ADDSYM run at deposition. COD was never curated as heavily as CSD, so its error rate may be higher, but I have no measured figure.
- **Verifier**: mechanical and strong: PLATON ADDSYM, pymatgen/spglib symmetry finding, bond-valence sums. Corrections are published as IUCr letters.
- **Precedent**: Marsh series (SCHOLARLY). For the computed-database side, Cheetham & Seshadri 2024 found GNoME "new materials" mostly trivial or implausibly ordered. That paper is a **trap** calibration for any "AI found N new crystals" claim.
- **Recipe**: code runs spglib over all COD CIFs at a loose tolerance and flags entries whose detected group is higher than the declared one, plus bond-valence outliers. An LLM triages the flagged entries against the source paper text.
- **Cost**: laptop, a day.
- **Traps**: pseudo-symmetry is real (a lower group can be correct). Disorder modelling. Tolerance choice manufactures hits.
- **Crowding**: `CROWDED` for CSD, `PARTLY` for COD.
- **Ethics**: clear.
- **Scores**: data_ready 5 · gap 2 · verifier 4 · cheapness 5 · payoff 2 · ethics_clear 5
- **Sources**:
  - https://journals.iucr.org/a/issues/2018/a1/00/a56582/a56582.pdf (SCHOLARLY, Spek 2018 abstract)
  - https://authors.library.caltech.edu/records/1p37b-1wg03 (SCHOLARLY, Marsh & Henling 2014)
  - https://cod.psdi.ac.uk/ (PRIMARY)
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265 (SCHOLARLY, Cheetham & Seshadri 2024)

### 10. LIGO/Virgo/KAGRA open strain (GWOSC) → marginal compact-binary events (seed)

- **Data**: O1–O3 strain, plus O4a (24 May 2023–16 Jan 2024; LIGO only), released 26 Aug 2025 with GWTC-4.0 (128 new candidates). GWTC-4.1/5.0 pages now cover O4b. Collected for gravitational-wave astronomy, so this is not "other-purpose" data. The gap is in methods, not purpose.
- **Question**: events below the collaboration's thresholds, or outside its template banks (higher harmonics, eccentric, precessing, sub-solar mass).
- **Gap evidence**: the IAS group found 10 new BBHs in O3a (2201.02252) and 14 more with higher-harmonic templates (Wadekar et al., 2312.06631, p_astro 0.53–0.88). I found no published outsider O4a search (see Unverified).
- **Verifier**: weak per event. A p_astro of 0.5–0.9 is a probability, not a confirmation. Only population-level consistency and future detector sensitivity help.
- **Precedent**: IAS (Venumadhav, Zackay, Wadekar, Mehta et al.) and 4-OGC (Nitz et al.) (SCHOLARLY).
- **Recipe**: matched filtering with PyCBC or GstLAL over O4a, plus a custom template bank. The LLM is not useful except for bookkeeping.
- **Cost**: high. A full-run search needs roughly 10⁵–10⁶ CPU-core-hours, my order-of-magnitude estimate (Unverified). Not hobby scale.
- **Traps**: glitches (blips, scattered light). Background estimation from time slides. Trials factors from template-bank expansion.
- **Crowding**: `CROWDED` (LVK, IAS, OGC).
- **Ethics**: clear.
- **Scores**: data_ready 5 · gap 2 · verifier 2 · cheapness 1 · payoff 4 · ethics_clear 5
- **Sources**:
  - https://arxiv.org/html/2508.18079v1 (PRIMARY, O4a open-data paper)
  - https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/ (SECONDARY)
  - https://arxiv.org/html/2312.06631v1 (SCHOLARLY)
  - https://arxiv.org/pdf/2311.06061 (SCHOLARLY, O3b IAS)

### 11. CERN Open Data (CMS) → outsider searches (seed)

- **Data**: CMS 2015 and 2016 13 TeV data. The 2016 release is about 16 fb⁻¹ (about half of that year), with more than 70 TB of collision data and 830 TB of simulation, in NanoAOD (about 95% smaller) and MiniAOD, with containers.
- **Question**: a narrow resonance or kinematic corner that CMS's own searches did not cut on.
- **Gap evidence**: the outsider precedent shows corners exist. Cesarotti, Soreq, Strassler, Thaler & Xue (arXiv 1902.04222) searched for 14–66 GeV dimuons at high pT in 7 TeV open data and set limits up to 9× stronger than inclusive ones. CMS later did its own 11.5–45 GeV scouting search and found nothing.
- **Verifier**: poor for outsiders. Systematics, trigger efficiency and luminosity calibration live in the collaboration. A "bump" from open data can only become a request to CMS. Limits are publishable; discoveries are not.
- **Precedent**: above, plus Thaler-group jet-substructure measurements (SCHOLARLY).
- **Recipe**: coffea or uproot analysis on NanoAOD. The LLM writes boilerplate only.
- **Cost**: moderate. Hundreds of GB to a few TB of NanoAOD per analysis on a cloud VM.
- **Traps**: look-elsewhere effect, mis-modelled backgrounds, and forgetting the validated-runs list (CMS requires it).
- **Crowding**: `PARTLY`.
- **Ethics**: clear.
- **Scores**: data_ready 4 · gap 2 · verifier 2 · cheapness 2 · payoff 3 · ethics_clear 5
- **Sources**:
  - https://arxiv.org/pdf/1902.04222 (SCHOLARLY)
  - https://openscience.web.cern.ch/node/441 (PRIMARY)
  - https://ep-news-wp.web.cern.ch/cms-releases-extensive-13-tev-collision-data-open-science/ (PRIMARY)

---

## Pilot in a day

**Candidate 1: orphaned wells on historical topo maps, one Pennsylvania county (Venango, the 1859 Drake-well region).**

1. List the quads: `curl "https://prd-tnm.s3.amazonaws.com/?list-type=2&prefix=StagedProducts/Maps/HistoricalTopo/GeoTIFF/PA/&max-keys=1000"`. Page with `continuation-token` and filter by quad names covering Venango County (e.g. Oil City, Franklin, Titusville, Pleasantville, Kennerdell). Download every edition: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/PA/<file>_geo.tif`. Expect about 30–80 files, about 1 GB.
2. Download the registry: PA DEP "Oil Gas Locations – Conventional Unconventional" from PASDA (`https://www.pasda.psu.edu/uci/DataSummary.aspx?dataset=1088`), plus the broader PASDA well inventory that FracTracker notes has more points. The PASDA host returned a proxy 403 from this container. If that persists, use the NETL EDX mirror (`https://edx.netl.doe.gov/dataset/pennsylvania-spatial-data-oil-gas-locations-conventional-unconventional`).
3. Set up `puzzles/`-style analysis in a `uv` env (rasterio, numpy, opencv-python-headless, pyproj, shapely). Crop 200 symbol exemplars by hand from two quads using the map legend. Calibrate template matching, then measure recall on registered wells: what fraction of DEP wells within mapped areas sit under a detected symbol (Rule 7)?
4. Detect symbols on all quads, convert to lat/lon, and keep detections more than 100 m from any registry point that also appear on two or more editions.
5. Spot-check 20 candidates against NAIP imagery and estimate precision. Write `analysis/output/candidates.csv` (kept private) and a summary with recall and precision numbers.
6. Do not publish coordinates. Contact the PA DEP orphan-well program and the CATALOG consortium (LBNL) with the method and the summary.

Success criterion for the day: a measured recall/precision and a count of persistent unregistered symbols. Precision has to be measured, not asserted (Rule 6).

## Raw ideas considered

1. NEXRAD meteorite falls: **kept** (#2).
2. NEXRAD bioscatter, bird and insect migration: dropped. Crowded (BirdCast, aeroecology groups) and no discovery verifier.
3. GOES-GLM bolides: **merged** into #2 as the trigger source.
4. Global Meteor Network trajectories: **merged** into #2 (CC BY 4.0).
5. GWOSC strain: **kept** (#10), `CROWDED`.
6. CERN Open Data: **kept** (#11), low verifier.
7. COD/CSD crystallography: **kept** (#9), gap weak.
8. Materials Project/GNoME computed stability: dropped. Computed, not observed; serves as the trap example in #9.
9. Historical maps, phantom islands: dropped. Long since resolved by hydrographic offices; no payoff.
10. Historical maps, lost villages and georeferenced change detection: dropped here. Archaeology belongs to file 01.
11. Historical topo maps → orphaned wells: **kept** (#1).
12. Historical topo maps → abandoned mine openings (USGS mine-symbol work exists): dropped as a near-duplicate of #1, but the same pipeline transfers.
13. Mapillary street imagery → survey benchmarks, milestones, ghost signs: dropped. Low payoff. NGS benchmark recovery is a verifier but finds no new knowledge. Not verified.
14. Argo floats: dropped. No anomaly-discovery precedent found.
15. NDBC/CDIP buoys → rogue waves: dropped as `CROWDED`. FOWD (Häfner et al. 2021) already processed more than 4 billion CDIP waves (https://arxiv.org/pdf/2011.12071, SCHOLARLY).
16. ENF dating of recordings: dropped. Public long-baseline grid-frequency archives were not found (the Met Police lab database is not public). It leans toward forensic use on private recordings, which raises an ethics flag.
17. USGS stream gauges: dropped. No discovery verifier. Earthquake hydrology overlaps file 04.
18. Volcanic gas networks: dropped. Monitored by observatories in real time; little hidden.
19. Old spectral libraries (USGS splib): dropped. Reference data, not discovery data.
20. PurpleAir network: dropped. ToS limits bulk historical use, and it leans toward pinpointing private emitters. The Tonga pressure-wave precedent sits in file 04.
21. Tree-ring widths (ITRDB) → dating undated timbers: dropped. The cross-dating community already does this routinely, and Miyake events need ¹⁴C, not ring widths.
22. Radiocarbon annual data → Miyake events: **kept** (#6).
23. Ice cores → unattributed eruptions: **kept** (#3).
24. Geomagnetic observatory records: **kept** (#8).
25. Neutron monitors (NMDB) → historic ground-level enhancements: dropped. Small archive, well studied.
26. Radiation networks (EURDEP, Safecast CC0, EPA RadNet) → unreported releases: dropped. EURDEP's historical feed appears restricted to authorities. Safecast is mobile and sparse. The 2017 Ru-106 detection was a state-agency effort. It also borders on security-sensitive attribution.
27. Industry reflection seismic → impact craters: **kept** (#5).
28. Aeromagnetic and gravity grids → buried craters and kimberlites: folded into #5's traps. Crank-prone (Deniliquin) and the verifier needs drilling.
29. Metabolomics repositories: **kept** (#4).
30. Proteomics (PRIDE) unassigned spectra: dropped. Biology, file 03's territory.
31. Natural-product NMR misassignment (NP-MRD, DP4/DU8ML): dropped as a candidate. NP-MRD's 5.5M spectra are mostly *predicted*, and raw experimental FIDs are rare. Kutateladze estimates 12–20% of published structures contain a misassignment (https://www.chemistryworld.com/research/controversy-surrounds-corrected-chemical-structures/4016494.article, POPULAR; https://pubs.rsc.org/en/content/articlelanding/2026/np/d5np00088b, SCHOLARLY). The verifier is DFT plus total synthesis, and even revisions get revised (dichrocephone A). Worth a separate look if raw NMR becomes public.
32. Legacy spacecraft PPI data: **kept** (#7).
33. Fermi GBM terrestrial gamma-ray flashes: dropped. Astronomy instrument (file 02) and crowded.
34. IceCube and ANITA public events: dropped. Astronomy. ANITA's anomalous events are a good trap example for file 02.
35. GOES-GLM lightning as an explosion detector: dropped. Overlaps file 04 and edges into military attribution.
36. GNSS/CORS ionospheric TEC (rocket launches, bolides): dropped. Overlaps file 04 and has missile-test ethics.
37. Radiosonde archive (IGRA): dropped. No discovery precedent found.
38. Lab-instrument patent datasets: dropped. No public raw instrument data in them.
39. Seismic-reflection-adjacent well logs (NLOG, NDR) → shocked-quartz mentions: folded into #5's recipe.
40. CMS/ATLAS jet substructure measurements: folded into #11.
41. Smart-meter and citizen weather station (Netatmo) data: dropped on privacy grounds.

## Unverified claims

- **Fries 2024 count** ("34 recovered, 33 unrecovered probable falls"). Seen only in a search snippet of NTRS 20240005795; ntrs.nasa.gov did not resolve from this container. It drives the #2 gap score.
- **Whether ARES/AMS already cross-check every GLM bolide against NEXRAD.** Not found either way. If they do, #2's gap drops to 2–3.
- **Public-domain status of HTMC scans.** Presumed for a federal work, not confirmed on a USGS page.
- **That CATALOG has not already swept Pennsylvania.** Its slides list PA as a study state. No PA results were found, but the work may be in progress.
- **The neo-bolide.ndc.nasa.gov download/API format.** The host was blocked by the container proxy; the `bolides` package documentation says it can read the site's data.
- **Silverpit confirmation date.** A Birmingham news URL says 2025; a ScienceDaily item is dated June 2026. The paper was not opened.
- **The NAMSS portal's current SEG-Y availability.** Only individual USGS Data Series pages were seen, some without trace files.
- **The O4a strain licence** (believed CC BY 4.0) and the **CPU-hour cost** of a full O4a search (my estimate). gwosc.org did not resolve.
- **Bard et al. primary papers for 5259/7176/12350 BCE.** Seen via a preprint listing and popular coverage only.
- **No automated database-wide ice-core tephra cross-match exists.** Absence of evidence from two searches.
- **COD error rate.** No measured figure found; the gap score for #9 is inferred.
- **Quinn et al. 2020 used repository-scale MASST search specifically.** Not confirmed from the methods section.
- **The 521M-spectra / 1,335-projects figure.** Attributed to a 2023 paper via snippet; the repository mix was not confirmed.
