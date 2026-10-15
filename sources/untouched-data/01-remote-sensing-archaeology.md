# 01 — Remote sensing for archaeology and landscape history

*2026-10-15. Research agent, domain 01. Written to `BRIEF.md`.*

**How this was checked.** WebFetch failed with DNS errors on every host in this
session, and direct `curl` to most hosts (cambridge.org, substack.com, zenodo.org,
nasa.gov, historicengland.org.uk, environment.data.gov.uk) was refused by the egress
proxy. Every claim below was therefore checked through **search-engine result
snippets**, not by reading full texts. The session's web-search budget ran out
before every planned check was done. Treat page numbers, exact counts and DOIs as
needing one more look. Anything not confirmed in a snippet is listed under
`## Unverified claims`. Two data hosts *are* reachable from this container, and
I confirmed both with live listings: the USGS 1 m DEM bucket
(`prd-tnm.s3.amazonaws.com`) and the 3DEP point-cloud bucket (`usgs-lidar-public`).
That fact decides the pilot.

## Summary: best bets

1. **USGS 3DEP 1 m lidar × unrecorded earthworks (US Midwest/Southeast mounds, historic features).** About 99% national coverage, open, and reachable from this container. The gap is real because state site files are closed. The weakness is the same closed files: only a SHPO or state archaeologist can say "new", so the verifier is a person, not a database. Best pilot.
2. **England EA lidar / Netherlands AHN × barrows, Roman roads, field systems, checked against public registries.** These have the best *verifier* of any candidate: NHLE (England), Canmore (Scotland) and Archis (NL) are partly public. They are also the most crowded (Historic England NMP, Heritage Quest's ~3,000 finds, decades of amateur Roman-road work). Value: calibration and coverage gaps, not first discoveries.
3. **Environmental/carbon lidar in the tropics (NASA G-LiHT Mexico; Brazil's EBA transects on Zenodo) × earthworks and settlements.** This is the Valeriana pattern, and the precedent is real. Mexico G-LiHT is now partly swept by a 35,584 km² CNN (Q2000, 2025). The Gulf-coast and non-Maya tiles, and the Brazilian EBA transects, look less worked. The verifier is INAH or IPHAN plus a field team, which a hobbyist cannot supply.
4. **Declassified HEXAGON (KH-9) imagery × pre-development landscapes and qanats.** Declass-3 (14,000 rolls, ~670,000 scenes) is still being ingested by USGS. HEXAGON became practically usable only in 2020–22. Precedent is strong (396 Roman forts, Casana et al. 2023; a qanat detector, 2024). The cost is scan fees and georeferencing labour, not compute.
5. **Don't-bother-alone tier:** Nazca (AI precedent, but the 2015 imagery is not public and field confirmation is mandatory); Sentinel-2 crop marks (10 m pixels are too coarse for discovery, but good for monitoring); shipwrecks in bathymetry (the verifier exists, but most of the gain sits in industry survey data that is not public).

---

## The prompt, checked

### The Substack post: "I went looking for lost cities with Claude" (Nate, *bakerbench*)

- **Exists.** URL: <https://bakerbench.substack.com/p/i-went-looking-for-lost-cities-with>. It was indexed by search as published about three days before 2026-10-15, which fits the 11 Oct 2026 date in the brief. Tier: **CLAIMANT** (the finder reports his own finds). I could not fetch the full text (proxy refusal), so everything below comes from search snippets.
- **What it claims, as shown in the snippets:**
  - "A few hours and a few hundred dollars of tokens, plus free government lidar" turned up two things:
    - **Mexico:** "about 30 earthen mounds and a raised platform on the Gulf coast, hidden in cattle pasture." One snippet gives "at least 26 measured mounds, the tallest 4.4 m, plus a raised rectangular platform about 25 × 35 m with a rim". The data is lidar that "NASA collected … in 2013 to measure forests", i.e. **G-LiHT**.
    - **Arizona:** "nine stone ruins … that nobody seems to have mapped", from **USGS 1 m lidar**.
- **Method:** Claude wrote **two detectors**: one for rubble mounds, one for grids of small rooms. They were run first "over more than a dozen known public sites":
  - On known Arizona pueblos, the real site landed in the detector's top few percent of locations **12 of 14** times.
  - A Stonehenge calibration recovered **68% of 173 recorded barrows**. It "misses small barrows and finds most of the big ones."
- **Novelty check:** For Arizona, "Claude checked the list against other sources, and fifteen of the 26 match something already published." So the nine "unmapped" ruins are what is left of 26 candidates after a check against *published* sources. Arizona's state site file (AZSITE) is not public, so the post cannot have checked against it. "Unmapped" therefore means "not in anything public", not "unrecorded".
- **Reporting:** the post says he "wrote it all up **without locations**" and reported it "to a group of archaeologists, including Mexico's national heritage agency (**INAH**) and the **team that found Valeriana**." No snippet says whether INAH replied. I found no snippet saying the Arizona finds went to the Arizona SHPO, the Arizona State Museum (which runs AZSITE), or a tribal historic preservation office.
- **Independent confirmation:** none found. No press coverage or archaeologist response turned up in search.
- **Assessment.** This is a well-behaved claimant post:
  - Calibration came before the claim (Rule 7, applied by an amateur).
  - Coordinates were withheld.
  - INAH was told.
  - The claims are small: mounds and room blocks, not "a city".
  - Status: **reported, not established.** Earthen mounds in Gulf-coast pasture are a known false-positive zone: cattle tanks, spoil heaps, house platforms of recent ranches, and natural levee features. Only a field visit or an INAH registry check can settle it.
  - The Arizona result has the classic weakness of US work. The real registry is closed, so "nobody has mapped them" cannot be tested from outside.

### Valeriana (Auld-Thomas et al., *Antiquity*, 2024)

- **Paper:** "Running out of empty space: environmental lidar and the crowded ancient landscape of Campeche, Mexico", *Antiquity*, published **29 Oct 2024**. Lead author Luke Auld-Thomas (then a Tulane PhD student); supervisor and co-author Marcello Canuto. Colleagues from Tulane and **INAH** took part. URL: <https://www.cambridge.org/core/journals/antiquity/article/running-out-of-empty-space-environmental-lidar-and-the-crowded-ancient-landscape-of-campeche-mexico/FFDB435047017853F26CFC5D8804B08D>. Tier: **SCHOLARLY** (title and URL confirmed by search; full text not read).
- **Data:** a lidar survey **flown in 2013 for forest/carbon monitoring**. Auld-Thomas told the BBC he found it on about "page 16" of Google results, and that it was "a laser survey done by a Mexican organisation for environmental monitoring." The popular sources split on who flew it: one says The Nature Conservancy (Mexico). **I could not confirm the dataset was NASA G-LiHT.** The "Mexican organisation" wording suggests it was not. So the brief's line "public lidar collected for carbon measurement" is supported. A G-LiHT link for Valeriana specifically is *not* supported.
- **Claims:** a Classic Maya capital (temple pyramids, ballcourt, plazas, causeway, reservoir). Population estimate 30,000–50,000 for AD 750–850. Called the second-densest Maya site after Calakmul. Structure counts differ by outlet: 6,500 / 6,750 / ~7,000. Survey area is given as ~122 km² or "~50 sq mi".
- **Verification status:** as of the 2024 coverage, **no ground visit to Valeriana had been reported**. The identification rests on lidar alone. It is still well supported, because Maya monumental architecture has a very low false-positive rate in lidar. Tier for these facts: **POPULAR** (sci.news, archaeologymag.com, CNN, bigthink, thedebrief).
- **Lesson for this survey:** the gap was a dataset nobody had *found*, not one nobody had *processed*. "Discovery" here was mostly a literature and data search. A hobbyist's comparative advantage is the same: finding orphaned datasets.

---

## Candidates

### 1. USGS 3DEP lidar (CONUS) × unrecorded earthworks, mounds and historic-period features

- **Data:**
  - **Who and why:** USGS 3D Elevation Program, flown for flood mapping, infrastructure and geology.
  - **Coverage:** baseline is quality level 2 or better lidar. Coverage was 98.3% available or in progress at end of FY2024 and "99% acquired or in work" at end of FY2025. The target is 100% by end of FY2026. Alaska is mostly IfSAR, so not useful here.
  - **Formats:**
    - 1 m DEM GeoTIFFs, 10 km tiles, ~300 MB each: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/…`
    - Entwine point clouds: `s3://usgs-lidar-public/`
  - **Licence:** public domain (US federal).
  - **Reachability:** both buckets were listed live from this container on 2026-10-15.
- **Question:** detect earthen mounds, effigy and geometric earthworks, rock rings/room blocks (Southwest), charcoal hearths, kilns, mill races and homestead foundations that are not in the state site file. A find looks like:
  - a mound 0.3–3 m high, 5–30 m across, often in groups on bluff edges;
  - or a rectilinear rubble pattern (Southwest room blocks, as in the Nate post).
- **Gap evidence:**
  - Iowa's statewide inventory of precontact burial mounds (*American Antiquity*) used 3DEP-spec lidar. It reports that the lidar "occasionally revealed more mounds than were originally recorded."
  - A Minnesota study found 118 previously unknown potential mounds at twelve sites.
  - In Morrow County, Ohio, one researcher found five previously unrecorded earthworks.
  - In Ocala NF, Florida, a UCF thesis found two previously unknown mound sites.
  - These are all small, local efforts. **No nationwide systematic sweep was found.**
  - Counter-evidence: the Ohio researcher warns that the 3DEP-derived *national* 1 m DEM product "should not be used for archaeological site interpretation." He used finer county lidar instead. Work from the point cloud (EPT) or the project-level DEMs, not the seamless national product.
- **Verifier.** This is the binding constraint:
  - Site locations are **closed** by law:
    - NHPA §304 and ARPA §9 let federal agencies withhold site locations.
    - States exempt them from FOIA. Michigan's file is open only to archaeologists who meet the Secretary of the Interior's qualification standards. New Hampshire RSA 227-C:11 exempts site locations from public-access law. California exempts them from the Public Records Act.
  - So **no public registry can verify a US hit.** The National Register of Historic Places is public but restricts the addresses of archaeological listings, and it lists a tiny fraction of sites.
  - The real verifier chain:
    1. Calibrate recall on sites that are already public (national monuments, state parks, published site plans).
    2. Submit candidates *without coordinates in public* to the SHPO or state archaeologist (in Iowa, the Office of the State Archaeologist), who checks the closed file.
    3. A field check by a qualified archaeologist, and for burial mounds consultation with tribes and THPOs.
  - Expect weeks to months, with no obligation on them to reply.
- **Precedent:**
  - Iowa, Minnesota, Ohio and Florida, above (SCHOLARLY and theses).
  - The Nate post's Arizona result (CLAIMANT, unconfirmed).
  - Kalapuya mounds in Oregon: a predictive model plus field testing found 7 new mounds (SCHOLARLY, snippet).
- **Recipe:**
  1. Code pulls tiles by bounding box.
  2. Code computes a local relief model (DEM minus a 20–30 m smoothed DEM), sky-view factor and slope.
  3. Code runs blob detection with height and diameter thresholds, plus a regularity filter.
  4. Code removes features near roads, buildings and farmsteads using OSM/NHD/building footprints, which strips most modern false positives.
  5. Code measures recall against a public calibration set.
  6. The LLM writes and debugs the pipeline, and writes per-candidate notes from hillshade crops plus historical topo maps (USGS historicalmaps). The LLM never decides "archaeological".
- **Cost:**
  - CPU only, no GPU needed.
  - One 10 km tile is ~300 MB and takes a minute or two to process in numpy/scipy.
  - A county is ~10–30 tiles: an hour or two and a few GB.
  - A state is a cloud VM-day.
  - LLM tokens: tens of dollars.
- **Traps:**
  - Modern spoil heaps, terrace ends, manure piles, haybale stacks (in leaf-on returns), natural sand dunes and kame/esker hummocks, karst sinkhole rims, tree-throw mounds.
  - Southwest: natural rockfall, and modern stock tanks and corrals.
  - Historical crank history: the "Mound Builder" myth was 19th-century pseudo-archaeology about *who built* the mounds. Do not drift into attributing builders.
- **Crowding:** `PARTLY`. State-level academic inventories exist (Iowa, Ohio, Minnesota); the Iowa inventory may be largely done. CRM firms use lidar for Section 106 surveys. No national open sweep was found.
- **Ethics:**
  - **High looting sensitivity.** Pothunting of mounds and Southwest sites is a live federal crime problem.
  - Burial mounds fall under NAGPRA on federal and tribal land and state burial laws elsewhere. Do not publish coordinates, crops with recognisable landmarks, or even county-level "here be mounds" maps.
  - Report to the SHPO / state archaeologist and, for the Southwest, the relevant THPOs.
  - On private land, discovery creates no right of access. Do not trespass to "ground-truth".
- **Scores:** `data_ready` 5, `gap` 3, `verifier` 2, `cheapness` 5, `payoff` 3, `ethics_clear` 2
- **Sources:**
  - USGS 3DEP status, FY25 slide (NGAC): <https://www.fgdc.gov/ngac/meetings/march-2026/NGAC-Paper-3DEP-Subcommittee-of-3D-Elevation-Program-2026> — PRIMARY (agency)
  - USGS Circular 1553: <https://pubs.usgs.gov/publication/cir1553> — PRIMARY
  - Iowa burial mound inventory, *American Antiquity*: <https://www.cambridge.org/core/journals/american-antiquity/article/an-inventory-of-precontact-burial-mounds-of-iowa/0892DD366ACE7667A538A8F6942AD640> — SCHOLARLY
  - Ohio Archaeological Council, Morrow County earthworks: <https://ohioarchaeology.org/file_download/inline/e12a2e16-354e-41eb-986c-8ca1c113a521> — SECONDARY
  - UCF thesis, Ocala NF: <https://stars.library.ucf.edu/etd2020/840> — SCHOLARLY (thesis)
  - Kalapuya mounds: <https://pdxscholar.library.pdx.edu/anth_fac/246> — SCHOLARLY
  - ACHP FAQ on NHPA §304: <https://connect.ncdot.gov/resources/Environmental/EAU/CR/Archaeology/Documents/Frequently%20Asked%20Questions%20on%20Protecting%20Sensitive%20Information%20About%20Historic%20Properties%20Under%20Section%20304%20of%20the%20NHPA.pdf> — PRIMARY
  - Michigan SHPO site-file access: <https://www.miplace.org/4a03d5/globalassets/documents/shpo/programs-and-services/archaeology/crm-106-and-research/archaeo-standards-fact-sheets/archaeology-standards-guide-6.pdf> — PRIMARY
  - NH RSA 227-C:11: <https://gc.nh.gov/rsa/html/XIX/227-C/227-C-11.htm> — PRIMARY
  - Bucket listings (live, 2026-10-15): `https://prd-tnm.s3.amazonaws.com/?list-type=2&prefix=StagedProducts/Elevation/1m/Projects/IA_` and `https://s3-us-west-2.amazonaws.com/usgs-lidar-public/?list-type=2&delimiter=/` — PRIMARY

### 2. NASA G-LiHT and other forestry/carbon lidar (Mexico, Puerto Rico, Florida, Alaska, eastern US)

- **Data:**
  - **Who and why:** NASA Goddard's LiDAR, Hyperspectral and Thermal imager, flown for forest structure and carbon.
  - **Mexico:** transects flown in 2013 for Mexico's forest-carbon (MRV/REDD+) work. The 2020 archaeological evaluation used **458 tiles**.
  - **Puerto Rico:** 2017 and 2018 flights (NGEE-Tropics/FLARE).
  - **Florida:** 2017.
  - **Alaska:** 2014 onward, plus a 2022 campaign from Kodiak and Anchorage.
  - **Eastern US:** 2021 and others.
  - **Access:** G-LiHT webmap and `https://glihtdata.gsfc.nasa.gov/files/G-LiHT/` (wget/curl bulk), and via Earthdata/LP DAAC. Public, NASA open data.
  - **Not reachable from this container** (proxy 403 on `glihtdata.gsfc.nasa.gov` and `e4ftl01.cr.usgs.gov`).
- **Question:** settlement mounds, platforms, causeways, field systems and terraces in transect strips. A find looks like a platform/plaza group, a mound cluster, or a linear causeway crossing the strip.
- **Gap evidence:**
  - Golden et al. (2016) visually inspected only "a sample of the flight paths."
  - Golden et al. (2020) evaluated 458 tiles over southern Mexico.
  - Britton et al. (2025, *J. Archaeol. Method & Theory*) trained a broadscale CNN, "Q2000", over **~35,584 km²** of Maya-region G-LiHT. So **the Maya lowlands are now partly machine-swept.**
  - The remaining gaps are where Maya-trained models generalise worst:
    - the **Gulf coast** (Veracruz/Tabasco: Olmec/Huastec/Totonac earthen architecture in pasture, which is exactly the Nate find);
    - non-Mesoamerican G-LiHT strips (Puerto Rico; Alaska, for semi-subterranean house pits);
    - the US Southeast strips.
  - I found **no archaeological study of G-LiHT in Alaska or Puerto Rico**. Puerto Rico lidar archaeology (Caguana) used NOAA 2016 lidar instead.
- **Verifier:**
  - Mexico: **INAH's site registry is not public.** INAH is the legal authority, and Mexican law (Ley Federal sobre Monumentos y Zonas Arqueológicos…) directs finders to report to the nearest INAH office. Confirmation means an INAH or academic field visit.
  - Puerto Rico: the PR SHPO and the Instituto de Cultura Puertorriqueña (not verified this session).
  - Alaska: the state's AHRS (closed) plus Alaska Native corporations and tribes.
  - **No public verifier in any of these places.**
- **Precedent:**
  - Golden et al. 2016 and 2020 (SCHOLARLY).
  - Q2000 2025 (SCHOLARLY).
  - Alcover and Golden: G-LiHT reprocessed for archaeology, followed by drone work and excavation at El Palma and nearby sites (SCHOLARLY).
  - Valeriana is the pattern, though on a *different* environmental lidar set (see above).
  - Nate's Gulf-coast mounds (CLAIMANT).
- **Recipe:**
  1. Bulk-download DTM tiles per transect.
  2. Run an LRM/SVF visualisation.
  3. Run a mound/platform detector, or Q2000 (released as an ArcGIS model; DOI 10.7945/tbvg-8n31), as a baseline.
  4. Mask out modern ranch infrastructure using Sentinel-2 and OSM.
  5. Deduplicate against *published* site lists (Golden 2020 supplementary data; Q2000 outputs).
  6. Use the LLM for pipeline code and literature triage only.
- **Cost:** transects are narrow, so the total volume is modest (tens to low hundreds of GB for Mexico; unverified). CPU is enough. Q2000 needs ArcGIS Pro, so an open re-implementation would need a GPU-hours budget.
- **Traps:**
  - Ranch-era earthworks (bordos, jagüeyes/cattle tanks, spoil from canals).
  - Termite mounds in tropical forest.
  - G-LiHT ground-point density under dense canopy is lower than in purpose-flown archaeological lidar, so small features drop out.
  - A strip boundary can cut a site in half and fake a "linear" feature.
- **Crowding:**
  - Maya lowlands: `CROWDED` (Golden/Brown/Penn State; Cincinnati Q2000; Tulane).
  - Gulf coast and non-Mesoamerican strips: `OPEN` as far as I found.
- **Ethics:** Looting in Mexico is active and prosecuted (INAH has filed criminal complaints over the Chalco and Teotihuacán cases; Art. 52 carries 3–10 years for damaging a monument). Report to INAH. Do not publish coordinates. Note that Mexico has in the past restricted public lidar access over looting and security concerns (Chase et al. 2020).
- **Scores:** `data_ready` 4, `gap` 3, `verifier` 2, `cheapness` 4, `payoff` 4, `ethics_clear` 3
- **Sources:**
  - NASA Earthdata G-LiHT: <https://www.earthdata.nasa.gov/data/projects/g-liht> — PRIMARY
  - G-LiHT Puerto Rico: <https://glihtdata.gsfc.nasa.gov/puertorico> — PRIMARY
  - G-LiHT data portal: <https://gliht.gsfc.nasa.gov/index.php?section=34> — PRIMARY
  - NASA Alaska 2022 field blog: <https://science.nasa.gov/blogs/notes-from-the-field/2023/01> — PRIMARY
  - Golden et al. 2016, *JAS: Reports* 9:293–308: <https://www.sciencedirect.com/science/article/pii/S2352409X16304370> — SCHOLARLY
  - Golden et al. 2020: <https://www.sciencedirect.com/science/article/pii/S2352409X20303345> — SCHOLARLY
  - Britton et al. 2025, Q2000: <https://link.springer.com/article/10.1007/s10816-025-09741-5> — SCHOLARLY
  - Caguana lidar (NOAA, not G-LiHT): <https://core-cms.cambridgecore.org/core/services/aop-cambridge-core/content/view/AA570E1937221B9DF77C71CCB8E5368B/S1045663521000869a.pdf/lidar-inspection-for-indigenous-architecture-at-caguana-ceremonial-complex-boriken.pdf> — SCHOLARLY
  - INAH 2022 bulletin on reporting finds: <https://www.inah.gob.mx/images/boletines/2022/454/Boletin%20454.pdf> — PRIMARY
  - Excelsior on Chalco looting: <https://www.excelsior.com.mx/cultura/inah-denuncia-fgr-saqueo-sitio-arqueologico-tlalteles-chalco> — POPULAR

### 3. Brazilian EBA carbon-lidar transects (Amazon) × pre-Columbian earthworks

- **Data:** EBA ("Estimativa de Biomassa na Amazônia", INPE), discrete-return airborne lidar.
  - **Transects:** 12.5 km × 300 m (375 ha) each, flown 2016–2018. Some were random over forest, some random over the deforestation arc, some over field plots.
  - **Zenodo records:**
    - summary shapefile `10.5281/zenodo.4968706` (21 MB);
    - point clouds for MT/AM/PA (`zenodo.org/records/7636454`) and RR/AP (`zenodo.org/records/7689693`);
    - a Source Cooperative mirror.
  - **Transect count:** the ORNL DAAC derived product lists 545 transects for 2016. The total is unverified (≈900 is commonly cited). Licence unverified.
- **Question:** ditched enclosures (geoglyphs), ring villages, mound villages, causeways and fortified sites under canopy.
- **Gap evidence:** Peripato et al. 2023 (*Science* 382:103–109) reported **24 previously undetected earthworks** under canopy in basin-wide lidar. They modelled **10,272–23,648** sites still undiscovered, mostly in the southwest Amazon. That is a published, quantified gap. But Peripato's team (INPE) almost certainly used these same transects (unverified), so the *sampled* strips are partly worked. The model's prediction concerns *unsampled* forest.
- **Verifier:**
  - Brazil's IPHAN registry, the CNSA (Cadastro Nacional de Sítios Arqueológicos), is partly searchable online (not verified this session).
  - Then a field visit by a Brazilian team under an IPHAN permit.
  - Indigenous land (TIs) needs FUNAI and community consent.
- **Precedent:**
  - Peripato 2023 (SCHOLARLY).
  - OpenAI to Z Challenge (2025): >2,500 Kaggle teams used public lidar and satellite data with OpenAI models. The winning team ("Black Bean") flagged **67 ~1 sq mi patches**. Judges were Sarah Parcak and Chris Fisher. **No field verification of the 67 was found** (POPULAR).
- **Recipe:**
  1. Download transects.
  2. Classify ground and build a 0.5–1 m DTM (PDAL).
  3. Run LRM.
  4. Search for ditch-ring and rectilinear-enclosure templates.
  5. Compare against Peripato's published list and the CNSA.
- **Cost:** point clouds total hundreds of GB (unverified). CPU is enough; ground classification is the slow step (a VM-day per few hundred transects).
- **Traps:**
  - Modern ranch ditches, roads and logging skid trails on the deforestation arc.
  - Oxbow scars and natural palaeochannels.
  - Strip geometry fakes linearity.
- **Crowding:** `CROWDED`. INPE/Peripato; OpenAI to Z (2,500 teams on the *same public data* in 2025); the Walker, Iriarte and de Souza groups.
- **Ethics:**
  - Indigenous sovereignty: Public Seminar (2025) criticised OpenAI to Z on exactly this, including its anonymous winners and descendant communities not having been asked.
  - Land-grabbing risk: publicised archaeology can attract invasion of protected land.
  - Report to IPHAN; do not publish coordinates.
- **Scores:** `data_ready` 4, `gap` 2, `verifier` 2, `cheapness` 3, `payoff` 4, `ethics_clear` 2
- **Sources:**
  - Peripato et al. 2023, *Science*, doi:10.1126/science.ade2541, via repository: <https://research-portal.uu.nl/en/publications/more-than-10000-pre-columbian-earthworks-are-still-hidden-through/> — SCHOLARLY
  - EBA L3A: <https://zenodo.org/records/4968706> — PRIMARY
  - EBA L1A: <https://zenodo.org/records/7636454> — PRIMARY
  - National Geographic on OpenAI to Z: <https://www.nationalgeographic.com/science/article/amazon-openai-competition-archaeology-machine-learning-artificial-intelligence> — POPULAR
  - OpenAI challenge page: <https://openai.com/openai-to-z-challenge/> — PRIMARY
  - Public Seminar critique: <https://publicseminar.org/2025/10/ai-in-the-amazon/> — POPULAR

### 4. National lidar in Britain, the Netherlands and continental Europe × barrows, field systems, Roman roads and camps (public-registry verifier)

- **Data:**
  - **England:** EA National LIDAR Programme, 1 m, flown winter 2017–Feb 2023. The composite DTM covers >95% of England (there is a hole around RAF Fylingdales). Open Government Licence.
  - **Netherlands:** AHN (open).
  - **Scotland and Wales:** national lidar (Scottish Remote Sensing Portal; Welsh Government DataMapWales). Not verified this session.
  - **Spain:** PNOA, a first full national lidar 2008–2015, open (CNIG).
  - **Denmark, Estonia, Slovenia:** national ALS exists and is used archaeologically. I verified only Slovenia's archaeological use; open-licence status was not verified for any of the three.
- **Question:** Bronze Age barrows, Celtic fields, charcoal kilns, Roman roads and camps, hillforts, medieval field systems, WWII features.
- **Gap evidence:**
  - The NHLE holds only *designated* assets (scheduled monuments), a small fraction of known sites.
  - Most known sites sit in county HERs, which are queryable via Heritage Gateway but not bulk-downloadable everywhere.
  - Spain: Costa-García, Fonte and Vicente García (2020) found **66 Roman camps** from open aerial, satellite and lidar data in León/Palencia/Burgos/Cantabria. That shows large gaps remained a decade after PNOA's release.
  - Slovenia: one micro-region (Bled) yielded a new hillfort among >1,000 lidar features.
  - Nate's barrow calibration (68% recall of 173 Stonehenge barrows) gives a concrete baseline.
- **Verifier.** The best in the domain:
  - **Historic England NHLE:** public GIS, OGL, open data hub. Historic England Research Records (ex-Pastscape) and county HERs via Heritage Gateway, partly public.
  - **Canmore (Scotland):** public; Canmore Areas shapefile on data.gov.uk.
  - **Archis (NL):** the national archaeological database. Public read access is partial; not verified this session.
  - **Denmark's Fund og Fortidsminder:** reputedly public and downloadable; not verified this session.
  - Chain: check the hit against the public registry, then the HER officer (UK) or provincial archaeologist (NL), then a field visit.
  - Heritage Quest provides a measured benchmark for volunteer-consensus reliability: barrow IDs were checked against fieldwork at 380 locations.
- **Precedent:**
  - Heritage Quest / Erfgoed Gezocht (Leiden + Gelderland): ~3,000 previously unknown objects (barrows, Celtic fields, charcoal kilns) from AHN via ~6,500 Zooniverse volunteers on the Veluwe (2019) and Utrechtse Heuvelrug (2020). This fed the WODAN deep-learning detector. SCHOLARLY/SECONDARY.
  - David Ratledge (retired engineer) traced the Ribchester–Lancaster Roman road in EA lidar; site visits confirmed it. Hugh Toller and Bryn Gethin found at least 4 lost Roman roads. PRIMARY (gov.uk) / POPULAR.
  - Spain: 66 camps (SCHOLARLY).
  - Iberian mound YOLOv3 work: ~10,527 mounds over ~30,000 km² (Berganzo-Besga et al. 2021, SCHOLARLY).
- **Recipe:**
  1. EA DTM tiles plus the NHLE scheduled-monument polygons give a labelled set.
  2. Train or calibrate the detector on scheduled barrows.
  3. Sweep an under-recorded upland or arable county.
  4. Diff against the NHLE, then check survivors by hand against Heritage Gateway/HER.
  5. Send the residual list to the county HER.
  - The LLM writes code and drafts HER submissions; code does the diffing.
- **Cost:** England 1 m DTM is ~TB-scale nationally but a county is tens of GB. CPU is enough; a YOLO-style detector benefits from a GPU (a few hours of a cloud T4).
- **Traps:**
  - Post-medieval features (windmill mounds, rabbit warrens/pillow mounds, spoil, landscape-garden clumps) are routinely misread as barrows.
  - Ridge-and-furrow and drainage read as "roads".
  - Roman-road enthusiasm has its own crank fringe ("lost roads" that are field boundaries or turnpikes).
  - LRM artefacts at tile edges.
- **Crowding:** `CROWDED`.
  - England: Historic England's National Mapping Programme (aerial and lidar), RomanRoads research groups, county lidar projects, many PhDs.
  - Netherlands: Heritage Quest.
  - Spain: Galician/USC groups (Berganzo-Besga, Orengo, Carrero-Pazos/LiDARch).
- **Ethics:** Nighthawking (illegal detecting) is real in the UK. Scheduled monuments are legally protected, but unrecorded sites are not. Report to the HER, and do not publish a list of new barrows with grid references. Lower stakes than burial mounds in the US or Mexico, since these are not living descendants' graves in the same legal sense.
- **Scores:** `data_ready` 5, `gap` 2, `verifier` 4, `cheapness` 4, `payoff` 2, `ethics_clear` 4
- **Sources:**
  - EA National LIDAR Programme / Composite DTM 1m: <https://www.data.gov.uk/dataset/lidar-composite-dtm-2017-1m> — PRIMARY
  - OSM wiki on EA lidar coverage: <https://wiki.openstreetmap.org/wiki/English_Environment_Agency_LIDAR> — SECONDARY
  - Historic England Open Data Hub: <https://historicengland.org.uk/listing/the-list/open-data-hub/> — PRIMARY
  - Canmore Areas shapefile: <https://ckan.publishing.service.gov.uk/dataset/national-record-of-the-historic-environment-scotland-canmore-areas> — PRIMARY
  - gov.uk "Lasers reveal lost Roman roads": <https://www.gov.uk/government/news/lasers-reveal-lost-roman-roads> — PRIMARY
  - Heritage Quest: <https://eu-citizen.science/project/135> — SECONDARY
  - Heritage Quest barrow reliability vs fieldwork: <https://www.cambridge.org/core/product/AD514BA3713EFC518038EC9232C3B5AD/core-reader> — SCHOLARLY
  - 66 Roman camps, *Geosciences* 2020: <https://www.incipit.csic.es/en/research_outcomes/publication/artigo/following-the-roman-army-between-the-southern-foothills-of-the-cantabrian-mountains-and-the-northern5659> — SCHOLARLY
  - Berganzo-Besga et al. 2021, *Remote Sensing* 13(20):4181: <https://www.mdpi.com/2072-4292/13/20/4181> — SCHOLARLY
  - Slovenia, Bled micro-region: <https://ojs.zrc-sazu.si/av/article/download/7938/7437/20625> — SCHOLARLY

### 5. Declassified CORONA / HEXAGON imagery × pre-development landscapes (tells, forts, canals, qanats, roads)

- **Data:**
  - **CORONA (KH-4, 1960–72):** declassified 1995. Rectified and hosted for SW Asia by CORONA Atlas (University of Arkansas, Casana). Chicago ISAC/CAMEL holds scenes over Iran (Fars, Esfahan, Yazd, Kerman), catalogued via BTAA Geoportal.
  - **HEXAGON (KH-9, 1971–86):** "surveyed nearly all land surfaces" at metre to sub-metre resolution. Declassified 2011 (Hammer, FitzPatrick & Ur 2022; some popular sources say 2019). **Widely scannable and downloadable only from 2020–22.**
  - **USGS Declass-3:** 14,000 rolls, >670,000 scenes, transferred to EROS in 2019. **Ingest and browse generation still "ongoing"** per USGS.
  - **Access and licence:** USGS EarthExplorer. Public domain; scanning on demand carries a fee (fee and on-demand mechanics unverified this session).
- **Question:**
  - Settlement mounds, enclosures, canals, field systems and qanat shaft-lines visible before 1970s–80s dams, mechanised agriculture and urban sprawl erased them.
  - Also *change detection*: sites now destroyed, which matters for heritage records even if not "new".
- **Gap evidence:**
  - Declass-3 is not fully ingested.
  - HEXAGON has had only ~4 years of practical availability.
  - Casana et al. 2023 found 396 new forts in a region Poidebard had surveyed by air in the 1920s–30s.
  - A qanat detector exists (2024), but published coverage is regional (Morocco, Iraq, N. Iran, Turkmenistan, Afghanistan under *UnderTheSands*).
- **Verifier:**
  - **EAMENA database** (Endangered Archaeology in the Middle East & North Africa), publicly searchable with registration (access terms not verified this session).
  - National antiquities registries (Iraq SBAH, Syria DGAM, Iran ICHHTO): closed and access-limited.
  - Published survey gazetteers (e.g. the Ur, Wilkinson and Adams surveys).
  - Later high-resolution imagery (Google/Bing/Maxar) for persistence.
  - Field verification is often impossible (conflict zones), so "confirmed" usually means expert photo-interpretation plus a check against older survey records.
- **Precedent:**
  - Casana et al. 2023, *Antiquity*: 396 Roman-era fortified structures from CORONA/HEXAGON. Reinterprets Poidebard's "defensive line" as trade/travel infrastructure.
  - Ur's CORONA hollow-way mapping in N. Mesopotamia (from memory; unverified this session).
  - Buławka, Orengo & Berganzo-Besga 2024, *JAS* 171: universal qanat detector trained on HEXAGON.
- **Recipe:**
  1. Order or download scenes.
  2. Georeference (CORONA panoramic distortion is the hard part; the CORONA Atlas method or orthorectification with SRTM).
  3. Run a tell or qanat detector (YOLO).
  4. Diff against EAMENA and published gazetteers.
  - The LLM handles literature/gazetteer extraction from PDFs of old surveys, which is genuinely useful, plus code.
- **Cost:**
  - Imagery: free for already-scanned frames; scan-on-demand has a fee (amount unverified).
  - Compute: GPU helpful for detection.
  - **The dominant cost is human georeferencing time.**
- **Traps:**
  - Film grain, scratches and processing artefacts.
  - Shadows at low sun angles mimic mounds.
  - Modern (1960s) military earthworks.
  - Rectification error creates false "absences" when compared with gazetteers.
  - Qanat lines confused with modern well lines.
- **Crowding:** `PARTLY`.
  - CORONA in the Near East: `CROWDED` (Casana, Ur, CAMEL, EAMENA, Hammer).
  - HEXAGON outside the Near East (Central Asia, the Sahel, the Andes, South Asia), and Declass-3 generally: `OPEN`-ish.
- **Ethics:**
  - Conflict-zone looting (Syria and Iraq since 2011) is severe and well documented. Never publish coordinates.
  - Route finds to EAMENA, which works with national authorities.
  - US export control does not apply to declassified imagery.
  - Qanats are living water infrastructure in places, so mapping them has no looting angle but may touch water-rights disputes.
- **Scores:** `data_ready` 3, `gap` 4, `verifier` 3, `cheapness` 3, `payoff` 4, `ethics_clear` 3
- **Sources:**
  - USGS EROS Declass-3: <https://www.usgs.gov/centers/eros/science/usgs-eros-archive-declassified-data-declassified-satellite-imagery-3> — PRIMARY
  - Hammer, FitzPatrick & Ur 2022, *Antiquity*, via Esri StoryMap: <https://storymaps.arcgis.com/stories/4a9b3b59888746fa9390f7f1f9c5add9> — SCHOLARLY/SECONDARY
  - Casana et al. 2023, Roman forts, via PetaPixel: <https://petapixel.com/2023/10/26/declassified-cia-satellite-spy-program-reveals-lost-roman-forts> — POPULAR (the paper itself is SCHOLARLY, *Antiquity* 2023; not read)
  - University of Arkansas, CORONA restoration: <https://news.uark.edu/articles/14486/restored-films-reveal-archaeological-treasures> — SECONDARY
  - Qanat detector, Buławka et al. 2024: <https://giap.icac.cat/?p=6259> — SCHOLARLY (via project page)
  - UnderTheSands at EAA 2024: <https://icac.cat/difusio/activitats-dels-investigadors/activitat/underthesands-investigating-ancient-irrigation-landscapes-in-arid-climates-through-remote-sensing-and-deep-learning-methods/> — SECONDARY
  - CAMEL CORONA holdings: <https://geo.btaa.org/catalog/camel-1018145> — PRIMARY

### 6. Historical aerial photo archives × crop marks and vanished features

- **Data:**
  - **Historic England Aerial Photo Explorer:** >540,000 digitised photos online out of >6 million held; "many yet to be digitised".
  - **NCAP (Edinburgh):** a June 2026 agreement with Arcadia will digitise >100,000 MENA aerial photos (1930s onward, British and US intelligence and mapping).
  - **RCAHMW:** ~1 million images of Wales, including the RAF's post-war Operation REVUE; >100,000 being digitised with NCAP.
  - **UCL IoA:** RAF 1918–39 imagery of Iraq, Transjordan, Egypt and Sudan.
  - **Cambridge (CUCAP):** a pilot of 1,500 digitised out of ~500,000.
  - **USGS EarthExplorer:** aerial single frames (US, 1930s+), not checked this session.
- **Question:** crop marks, soil marks and earthworks photographed before ploughing or development. Also *re-reading* frames that were flown for other purposes (mapping, intelligence) and never examined archaeologically.
- **Gap evidence:** the digitised fraction is small (~9% of the Historic England archive; ~0.3% of CUCAP in the pilot), and NCAP's MENA tranche is brand new (2026). Most frames have never been looked at for archaeology outside the UK.
- **Verifier:** the same registries as candidates 4 and 5 (NHLE/HER/Canmore; EAMENA). For MENA, older survey gazetteers.
- **Precedent:**
  - The UK National Mapping Programme was built largely on these archives (SECONDARY).
  - Poidebard's 1920s–30s aerial survey is the precedent Casana's team re-ran (candidate 5).
- **Recipe:**
  - The **binding constraint is georeferencing** oblique/vertical frames with poor metadata. An LLM plus code can help match frames to modern imagery (feature matching, e.g. SuperGlue/LoFTR) and triage.
  - Detection of crop marks in historic B/W frames is weak with automated methods; human review dominates.
- **Cost:** low compute, high human time. Archive terms of service may restrict bulk download or reuse (Historic England licence terms not verified this session).
- **Traps:**
  - Natural periglacial polygons, geological crop marks, modern drainage, film defects.
  - Duplication: much UK material has already been mapped by NMP.
- **Crowding:**
  - UK: `CROWDED` (NMP, HE).
  - MENA NCAP tranche: `OPEN` but it is being digitised *for* EAMENA-type users. Coordinate with them.
- **Ethics:** same as candidate 5 for MENA. Rights and licensing on archive imagery.
- **Scores:** `data_ready` 2, `gap` 4, `verifier` 3, `cheapness` 3, `payoff` 3, `ethics_clear` 4
- **Sources:**
  - Historic England Aerial Photo Explorer: <https://historicengland.org.uk/aerialphotos> — PRIMARY
  - NCAP–Arcadia: <https://www.ncap.org/about-us/partners/arcadia> — PRIMARY
  - NCAP–RCAHMW: <https://www.ncap.org/about-us/partners/rcahmw> — PRIMARY
  - UCL IoA archive: <https://journals.uclpress.co.uk/ai/article/id/3128/> — SECONDARY

### 7. Sentinel-2 / Landsat time series × crop marks and site destruction

- **Data:** ESA Sentinel-2 (10 m, 5-day revisit, 2015+) and Landsat (30 m, 1984+), open, via Google Earth Engine / AWS / Copernicus.
- **Question:**
  - Discovery: crop marks in drought years.
  - Monitoring: which recorded sites are being destroyed by agricultural expansion, looting pits or construction.
- **Gap evidence:**
  - The literature has largely moved to **monitoring**:
    - AgriExp (Conesa et al. 2022): agricultural encroachment on mounds in Cholistan.
    - EAMENA change detection (Rayne et al.): 85–91% accuracy in Egypt and Libya.
  - Discovery attempts:
    - a Via Appia S1+S2 study for buried road sections;
    - a 2014 simulation found Sentinel-2 *could* reveal unknown crop-mark sites.
  - **I found no clear published new-site discovery from an automated S2 crop-mark sweep.** 10 m pixels resolve only large features.
- **Verifier:**
  - Monitoring: the input registry *is* the verifier (EAMENA, NHLE), and change is confirmed with high-resolution imagery. Strong.
  - Discovery: weak.
- **Precedent:** AgriExp; EAMENA (SCHOLARLY).
- **Recipe:**
  1. A GEE script computes NDVI anomaly per field per year.
  2. Flag persistent geometric anomalies in drought years.
  3. Diff against registries.
  - For monitoring, run AgriExp on a registry the user has access to.
- **Cost:** free GEE tier for non-commercial use; CPU.
- **Traps:**
  - Field-boundary effects, irrigation pivots, drainage tiles, geology.
  - 10 m mixed pixels.
  - A "drought crop mark" hunt by Google Earth users has produced many false claims (no specific citation found this session).
- **Crowding:** monitoring `CROWDED` (EAMENA, ICAC); discovery `OPEN` but probably for a reason.
- **Ethics:** monitoring outputs are benign and useful to heritage agencies. Discovery outputs carry the usual coordinate caution.
- **Scores:** `data_ready` 5, `gap` 2, `verifier` 3 (monitoring) / 1 (discovery), `cheapness` 5, `payoff` 2, `ethics_clear` 4
- **Sources:**
  - AgriExp, Conesa et al. 2022: <https://recercat.cat/handle/2072/530076> — SCHOLARLY
  - Leicester / EAMENA change detection: <https://figshare.le.ac.uk/articles/journal_contribution/Detecting_Change_at_Archaeological_Sites_in_North_Africa_Using_Open-Source_Satellite_Imagery/14661372> — SCHOLARLY
  - Sentinel-2 simulation 2014: <https://ktisis.cut.ac.cy/bitstream/20.500.14279/8607/1/remotesensing-06-02176.pdf> — SCHOLARLY

### 8. Nazca-style AI sweep (precedent, not a recommended candidate)

- **Data:** Sakai et al. used **high-resolution aerial photographs taken in 2015** (~10 cm). Their public availability is **not established**, and I believe they are not openly released (unverified).
- **What happened:**
  - Sakai et al., *PNAS* 2024 (doi:10.1073/pnas.2407652121): AI flagged ~1,300 candidates, all small relief-type.
  - Field survey (Sep 2022 – Feb 2023) **confirmed 303 new figurative geoglyphs**, nearly doubling the ~430 known.
  - Screening took >47,000 AI-flagged boxes and >2,600 labour-hours.
  - Reported speed-up is 16× (Yamagata release) or 20× (Smithsonian).
- **Lesson:** this is the gold standard of the method, and its verifier was **six months of fieldwork by the team holding the Peruvian permits**. The AI cut the search cost; it did not replace confirmation. Roughly 23% of AI candidates (303/1,300) were confirmed. That is a useful prior for the precision of any hobbyist detector, likely an upper bound.
- **Crowding:** `CROWDED` (Yamagata University / IBM; the Nazca–Peruvian Ministry of Culture arrangement).
- **Scores:** `data_ready` 1, `gap` 2, `verifier` 4 (for them), `cheapness` 1, `payoff` 4, `ethics_clear` 4
- **Sources:**
  - Yamagata release: <https://www.yamagata-u.ac.jp/en/download_file/view/1952/835> — PRIMARY
  - Smithsonian: <https://www.smithsonianmag.com/smart-news/see-newly-discovered-nazca-drawings-depict-llamas-human-sacrifices-more-180985133/> — POPULAR
  - Language Log: <https://languagelog.ldc.upenn.edu/nll/?p=66846> — POPULAR

### 9. Shipwrecks in public bathymetry (NOAA/NCEI multibeam, BOEM)

- **Data:**
  - NOAA NCEI multibeam archive and BAG hydrographic surveys: public, enormous, collected for nautical charting.
  - BOEM's Gulf 3D-seismic seafloor (water-bottom) grids: public.
  - NOAA ENC/AWOIS wreck records are the existing wreck registry (AWOIS details not verified this session).
- **Question:** wreck-shaped anomalies in charting surveys not in the ENC/wreck database.
- **Gap evidence:**
  - BOEM says **>600 shipwrecks and possible shipwrecks** in the Gulf were found "mostly through" mandated oil-and-gas side-scan/magnetometer surveys. That is industry data, largely *not* public.
  - NOAA Ocean Exploration relied on BOEM and industry for targets.
  - I found **no** documented case of a researcher finding a new wreck by sweeping public NCEI multibeam. One forum post describes using NOAA multibeam to *relocate* a lake wreck.
- **Verifier:**
  - NOAA ENC wrecks and obstructions, plus state underwater site files (closed).
  - Confirmation is an ROV/AUV or a dive, which is expensive.
  - Charting-resolution multibeam often fails to resolve wreck detail, and NOAA notes bottom detection can miss masts.
- **Precedent:** BOEM-driven Gulf finds, including the deepest known investigated Gulf wreck at 7,450 ft (PRIMARY, but on industry data).
- **Recipe:** download BAGs by region, run a residual-relief anomaly detector, mask known ENC wrecks, and triage by shape (length/width ratio, height).
- **Cost:** large data; CPU fine.
- **Traps:**
  - Rock outcrops, pipeline crossings, dumped debris, fishing reefs/artificial reefs (many are deliberately sunk vessels already recorded).
  - Sonar artefacts.
- **Crowding:** `PARTLY`. NOAA and BOEM do this internally; wreck-hunting hobbyists are active.
- **Ethics:**
  - War graves (WWI/WWII naval wrecks) are protected under the Sunken Military Craft Act (US) and similar laws.
  - Salvage-hunter interest means coordinates attract looters. Report to NOAA Office of National Marine Sanctuaries / BOEM / the state underwater archaeologist.
- **Scores:** `data_ready` 4, `gap` 2, `verifier` 3, `cheapness` 3, `payoff` 2, `ethics_clear` 3
- **Sources:**
  - BOEM Gulf shipwrecks: <https://www.boem.gov/node/1537> — PRIMARY
  - BOEM 2013 study of 11 wrecks: <https://boem.gov/Tech-2013-011110> — PRIMARY
  - BOEM GM-21-02: <https://boem.gov/environment/gm-21-02> — PRIMARY
  - NOAA Block Canyon wreck bathymetry: <https://oceanexplorer.noaa.gov/technology/development-partnerships/ex1904/logs/july26/media/bathy2.html> — PRIMARY

---

## Looting and ethics protocol (applies to every candidate)

1. **Never publish coordinates, recognisable image crops, or maps finer than a large region for an unconfirmed or newly recorded site.**
   - The evidence that publication causes looting is weak. Cohen et al. 2020 cite "no evidence of a relationship between publication … and terrestrial looting".
   - The legal and ethical duty to withhold is not weak: NHPA §304, ARPA §9 and state FOIA exemptions in the US; INAH law in Mexico.
   - Where a public figure is needed, use geomasking. Random-perturbation "donuts" performed best in the *Advances in Archaeological Practice* study.
2. **Who to report to.**

   | Where | Report to |
   |---|---|
   | Mexico | INAH, nearest Centro INAH (legal duty per INAH) |
   | US | State SHPO / state archaeologist; THPOs and tribes for burials and the Southwest; federal land manager if on federal land (ARPA) |
   | England | County/unitary HER officer; Historic England for potential scheduling |
   | Scotland | HES / Canmore |
   | Wales | RCAHMW / regional HER |
   | Netherlands | Provincial archaeologist / RCE (Archis) |
   | Brazil | IPHAN; FUNAI and the community on Indigenous land |
   | MENA | EAMENA, which liaises with national antiquities services |
   | Wrecks | NOAA ONMS / BOEM / state underwater archaeologist |

3. **Coordinate withholding with the recipient.** Tell them before any public write-up. Let them decide the release level. GlobalXplorer's rule: maps are released only if "deemed appropriate by the governments and protection agencies involved."
4. **Do not ground-truth on private or tribal land without permission.** Do not dig. Do not collect surface artefacts (illegal in Mexico, and on US federal land under ARPA).
5. **Publish method and calibration, not finds.** The Nate post does this: recall numbers on known sites, withheld locations. Cohen et al. 2020 (*JCAA*) propose a pre-acquisition checklist for lidar ethics, and Chase et al. 2020 note some countries restrict lidar access because of looting.
6. **Descendant communities.** The OpenAI to Z critique (Public Seminar, 2025) applies: a hobbyist sweep of Indigenous landscapes without consultation is extractive even if no coordinates leak.

Sources:
- Cohen et al. 2020, *JCAA*: <https://halshs.archives-ouvertes.fr/hal-02546576v1/file/Cohen%20et%20al%202020.pdf> — SCHOLARLY
- Chase et al. 2020, *JCAA* "Reflections on archaeological lidar": <https://journal.caa-international.org/articles/43> — SCHOLARLY
- "Ethics and best practices for mapping archaeological sites", *Advances in Archaeological Practice*: <https://www.cambridge.org/core/product/A7338404A56B73BB282C4A28B3B7264A> — SCHOLARLY
- INAH bulletin: see candidate 2.

## Calibration cases (Rule 7)

| Case | What happened | Lesson |
|---|---|---|
| **Gadoury, 2016** | A 15-year-old's star-map "lost Maya city" (K'aak Chi) from Canadian Space Agency imagery. David Stuart called it "junk science": the square feature was a fallow milpa. Thomas Garrison: "ground-truthing is the key." POPULAR. | A pattern-matching prior (constellations) plus one image gives a confident false positive. |
| **Nazca, 2024** | ~23% of AI candidates confirmed after 2,600 labour-hours. | Prior on detector precision, *with* expert screening. |
| **Nate's barrow test** | 68% recall on 173 Stonehenge barrows, biased toward large barrows. | Hobbyist detectors miss small features. A "none found" is not evidence of absence. |
| **OpenAI to Z, 2025** | 2,500 teams, 67 flagged patches, no field confirmation found. | Compute was abundant; verification was not. That is `ideas/pooled-compute.md` in miniature. |

---

## Pilot in a day

**Calibrate a mound detector on USGS 3DEP 1 m lidar at a public mound group, then sweep the surrounding tiles and stop before claiming anything.**

Why this one:
- It is the only candidate whose data is **confirmed reachable from this container**. I listed both USGS buckets on 2026-10-15; EA, AHN, G-LiHT and Zenodo all returned proxy 403.
- It needs no GPU.
- The output is a recall number (Rule 6, a statistic from a script), not a discovery.

**Calibration target:** Effigy Mounds National Monument, Allamakee/Clayton Counties, Iowa (~43.09 N, 91.19 W). The mounds are on NPS public land, publicly mapped and interpreted, so calibration leaks nothing. Tile choice:
- This lies in UTM zone 15N at about E ≈ 647 km, N ≈ 4,772 km.
- USGS 1 m tiles are named `x{E/10km}y{top N/10km}`, so the monument should fall in **x64y478**.
- **Confirm by reading the GeoTIFF bounds**: the tile arithmetic is mine, not checked against a footprint index.

Exact URLs (listed live; ~295–342 MB each):

```
https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/IA_EasternIA_2019_B19/TIFF/USGS_1M_15_x64y478_IA_EasternIA_2019_B19.tif
https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/IA_EasternIA_2019_B19/TIFF/USGS_1M_15_x64y477_IA_EasternIA_2019_B19.tif
https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/IA_EasternIA_2019_B19/TIFF/USGS_1M_15_x64y479_IA_EasternIA_2019_B19.tif
# neighbours: list with
https://prd-tnm.s3.amazonaws.com/?list-type=2&prefix=StagedProducts/Elevation/1m/Projects/IA_EasternIA_2019_B19/TIFF/USGS_1M_15_x6
# point cloud alternative (Entwine EPT, finer control):
https://s3-us-west-2.amazonaws.com/usgs-lidar-public/IA_Eastern_1_2019/ept.json   (also _2_, _3_; check which covers the tile)
```

Steps:

1. **Set up.** Make a `uv` env under `puzzles/<slug>/analysis/` (or `ideas/…/analysis/` if this never becomes a deep dive) with `rasterio numpy scipy scikit-image` (pypi is reachable). Download the three tiles into a fresh data directory and run Python with `-I`.
2. **Ground truth.** Hand-digitise mound centroids for the *public* NPS monument map. Do not use the closed Iowa site file. Store them as `calibration_effigy.csv` and cite the NPS map URL.
3. **Features.**
   - Local relief model = DEM minus a Gaussian- or median-smoothed DEM (σ ≈ 15 m).
   - Sky-view factor (optional).
   - Threshold LRM between 0.3 and 3 m. Keep connected components with area 20–700 m² and compactness above a cutoff.
   - Effigy mounds are elongate, so also run a ridge/elongation variant.
4. **Score recall** = calibration mounds within 10 m of a detection. **Precision proxy** = detections per km² on the monument versus on a control tile with no known mounds.
5. **Mask modern features** with OSM buildings/roads (Overpass may be blocked; check) and a slope mask.
6. **Sweep** neighbouring tiles and output a ranked candidate list.
7. **Stop.**
   - Do **not** publish candidates or coordinates.
   - Write method, recall and false-positive density to the analysis README.
   - Anything that survives triage goes privately to the **Iowa Office of the State Archaeologist** (Iowa burial mounds are protected under state law; statute not verified this session).

Success criterion for the day: a reproducible recall figure on a public mound group, compared with Nate's 68% barrow figure. That is a Rule 7 calibration, and it tells us whether hobbyist-grade 3DEP mound detection is worth a deep dive.

---

## Unverified claims

- **Nate post, full text:** not fetched (proxy refusal). Unconfirmed: the Gulf-coast location in more detail than "Gulf coast"; the "26 measured / 4.4 m / 25 × 35 m" figures (one search snippet only); whether the Arizona finds went to the AZ SHPO, the Arizona State Museum or tribes; any INAH reply; total spend. A GitHub repo `vgit-it/LostCitites` ("Repo to do stuff with Claude") came up in search. **Its link to the post is unconfirmed**, and access was denied from this session.
- **Valeriana:** DOI not confirmed. Whether its 2013 lidar is NASA G-LiHT or a different Mexican carbon-monitoring survey (The Nature Conservancy attribution appears in one popular source). Exact structure count (6,500 / 6,674 / 6,750 / ~7,000 all appear). Whether any ground visit has occurred since 2024.
- **G-LiHT:** total Mexico data volume; whether Q2000's 35,584 km² includes Gulf-coast (non-Maya) tiles; G-LiHT coverage in the US Southeast.
- **EBA:** total transect count (~900 commonly cited; 545 in one ORNL derived product), licence, and whether Peripato et al. used exactly these transects.
- **HEXAGON:** declassification year (2011 per Hammer et al. vs 2019 in popular sources); scan-on-demand fee and mechanics on EarthExplorer; fraction of Declass-3 ingested.
- **Registries:** public access terms for Archis (NL), Fund og Fortidsminder (DK), EAMENA, Brazil's CNSA; whether Estonia, Denmark and Slovenia national ALS are under open licences.
- **Scotland and Wales** national lidar portals and the Arran lidar survey: not checked this session.
- **Iowa** burial-mound statute; the number of mounds at Effigy Mounds NM.
- **Ur's CORONA hollow-way work:** from memory, not re-checked.
- **"6,674 structures" for Valeriana and "Nature Conservancy flew the lidar":** both phrases were in my search queries. Neither appeared in results except the TNC attribution in one outlet.
- **Search budget:** the session's web-search budget ran out before I could recheck the Valeriana DOI and author list or look up the Scottish, Welsh and Estonian lidar portals.
