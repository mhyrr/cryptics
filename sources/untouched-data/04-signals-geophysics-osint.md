# 04 — Signals, geophysics, and open-source intelligence

*Survey for `BRIEF.md`, 2026-10-15. Domain: seismic, infrasound, hydroacoustic,
fiber, radio, AIS/ADS-B, and the orbital and atmospheric remote sensing used in
public-interest OSINT. Survey only (Rule 9): no candidate here was run.*

## Summary: the best bets in five lines

1. **Long-period seismic sweep for unexplained sources (landslides, calving, fjord seiches).** This is the strongest fit for the brief. Archive searches already turned up five earlier Dickson Fjord events that nobody had noticed, and a published sweep lists more than 1,700 long-period sources it could not identify. Satellite imagery is a cheap, decisive check.
2. **Attributing those unidentified sources** with free Sentinel-2/Landsat image archives is the hobbyist-sized piece. Nobody has publicly worked through Poli's list (see Unverified claims).
3. **Methane plumes (EMIT, TROPOMI, Sentinel-2)** and **oil slicks (SkyTruth Cerulean)**: the data is excellent and the checks are real, but both are `CROWDED`. A hobbyist's realistic contribution is attributing plumes or slicks to sources, not detecting them.
4. **Dead and "zombie" satellites** in open SatNOGS radio data: three amateur finds give real precedent (LES-1, IMAGE, LES-5), and Doppler matching against public orbits is a mechanical check. The payoff is small.
5. **Traps worth recording:** WSPR-for-MH370 (contested), the Bloop (an icequake), numbers stations, and "dark vessel" counts read as illegality. ELINT in the strict sense is out of scope (see below).

### What "ELINT" can and cannot mean here

Electronic intelligence, in the strict sense, means collecting and analyzing other parties' non-communication emissions (radars, data links, emitter fingerprints), usually against military or security systems. For a hobbyist, that path leads to profiling military radars, locating defense systems, decoding encrypted links, or tracking named people's aircraft and phones. That is either illegal (intercept statutes, export control) or defeats security, so this survey drops it. What remains, and what the rest of this file covers, is the public-interest end. That means emissions and signals which are broadcast to everyone for safety reasons (ADS-B, AIS, satellite beacons), environmental signals (seismic, acoustic, atmospheric), and aggregate patterns (GNSS interference regions, flaring volumes). In every case the target is a place, a facility, a vessel class, or a natural event, never a private person.

---

### 1. Global long-period seismic archive: unexplained monochromatic and VLP sources

- **Data:** The FDSN-federated continuous waveform archive, mainly the EarthScope (formerly IRIS) DMC. It holds the Global Seismographic Network and hundreds of regional networks, collected for earthquake monitoring and Earth structure. For this purpose the 1-sample-per-second `LH?` channels are enough, at roughly 100 KB per station-day of miniSEED. Access is through the FDSN web services at `service.iris.edu` / `service.earthscope.org`, under the NSF SAGE terms of service, and publications should cite data by network. Some regional centers ask users to keep to 3 concurrent sessions (SCEDC).
- **Question / what a find looks like:** A narrowband (for example 5–20 mHz) signal lasting hours to days, seen coherently at many stations, that matches no catalogued earthquake. Each one is a candidate unrecorded landslide, rock avalanche, glacial calving event, tsunami seiche, or submarine eruption.
- **Gap evidence:** The best gap evidence in this domain.
  - Poli's SRL paper (DOI 10.1785/0220230148) swept 2010–2022 global long-period data, found more than 36,000 detections, and after classification still reports **more than 1,700 previously unidentified sources**. That is a published list of unexplained events.
  - After the 2023 Dickson Fjord signal, a search of historical data found **five other previously undetected events** at 10.85–11.02 mHz. Satellite archives tie at least four of the six to Dickson Fjord landslides (Koelemeijer, Widmer-Schnidrig, Svennevig et al., EGU 2024).
  - Ekström and Stark's near-real-time detector concluded that "several" landslides above 10 Mt go **unreported each year**, mostly in SE Alaska and the Himalaya-Karakoram.
  - Other studies report unclassified waveform families in Greenland data and a "previously unidentified" Canadian Arctic long-period source.
- **Verifier:** Strong and independent.
  - Before/after optical imagery (Sentinel-2 at 10 m, about 5-day revisit since 2017; Landsat back to the 1980s) shows a fresh scar or deposit, or a calving front retreat.
  - SWOT altimetry was used to confirm the Dickson seiche (Monahan et al., Nat. Commun. 2025).
  - Local reports of tsunami damage are a third check.
  - A wrong attribution fails visibly: no scar.
- **Precedent:**
  - Dickson Fjord 2023: a 9-day global 10.88 mHz signal from a 25×10⁶ m³ rock-ice avalanche and a 200 m tsunami (Svennevig et al., *Science* 2024).
  - Mayotte 2018: a ~20-minute monochromatic global signal, first flagged by a Twitter user (@matarikipax) on USGS's public live seismograms. It led to the discovery of the largest documented submarine eruption, a new edifice about 800 m tall.
  - Ekström et al. 2003 discovered glacial earthquakes by surface-wave detection. Pirot et al. (GJI 2024) added 1,633 new glacial events with STA/LTA plus a Random Forest classifier.
- **Recipe:**
  1. Code: pull `LHZ` data for high-latitude and GSN stations with ObsPy's FDSN client.
  2. Code: compute daily spectrograms, then flag narrowband peaks with Q ≫ normal surface-wave decay that persist across at least 3 stations. Remove free-oscillation windows after large earthquakes using the USGS ComCat event catalog.
  3. Code: back-project or grid-search the location with phase velocity matching fundamental-mode Rayleigh waves.
  4. Code: for each candidate location and date, fetch Sentinel-2/Landsat scenes before and after the event.
  5. LLM role: triage image pairs, draft the write-up, and search for local news. A geomorphologist confirms the scar.
  - Alternative route: obtain Poli's catalog of unidentified sources (see Unverified claims) and skip steps 1–3.
- **Cost:** CPU-only. One year × 30 stations of LH data is about 1 GB. Imagery comes through the free AWS/Copernicus STAC. Hours for a pilot, days for a decade.
- **Traps:**
  - Earth's free oscillations ring for days after M7+ earthquakes.
  - Microseism storms produce ocean-wave noise.
  - Instrument glitches and calibration pulses look like signals.
  - Ekström's detector reportedly gives ~10 false positives per real landslide (SciDev summary).
  - Mislocation in fjord-rich terrain.
  - Calling a known catalogued quake "unknown" because you searched the wrong catalog.
  - The "Unidentified Seismic Object" label invites mystery-mongering; most of these turn out to be mundane once found.
- **Crowding:** `PARTLY`. Detection is done by professional groups (Poli, Lamont/Ekström, GEUS, IPGP). **Attributing the published leftovers** with imagery looks open; I found no public effort working through it.
- **Ethics:** Clear. These are natural hazards in mostly remote terrain. If a find implies a continuing tsunami hazard (as in Dickson Fjord, which sits on cruise routes), report it to the national geological survey before publishing.
- **Scores:** data_ready 5 · gap 4 · verifier 5 · cheapness 5 · payoff 4 · ethics_clear 5
- **Sources:**
  - Svennevig et al. 2024, *Science* 385:1196, doi:10.1126/science.adm9247: https://www.usgs.gov/publications/a-rockslide-generated-tsunami-a-greenland-fjord-rang-earth-9-days (SCHOLARLY); GEUS press release https://eng.geus.dk/about/news/news-archive/2024/september/climate-change-triggered-landslide-caused-earth-to-vibrate-for-9-days (SECONDARY)
  - Koelemeijer, Widmer-Schnidrig, Svennevig et al., EGU 2024 abstract, "five other previously undetected events": https://pub.geus.dk/en/publications/global-observation-of-an-up-to-9-day-long-recurring-monochromatic/ (SCHOLARLY, abstract only)
  - Monahan et al. 2025, *Nat. Commun.*, SWOT seiche: https://www.ox.ac.uk/news/2025-06-03-first-direct-observation-trapped-waves-shook-world (SECONDARY); https://eos.org/articles/new-satellite-adds-evidence-of-an-earth-shaking-wave (POPULAR)
  - Poli, SRL, doi:10.1785/0220230148, ">1700 previously unidentified sources": https://www.citedrive.com/en/discovery/continuation-of-events-detection-with-global-long-period-seismic-data-an-analysis-from-2010-to-2022/ (SCHOLARLY, abstract only)
  - Ekström & Stark landslide detection; "several massive landslides go unreported each year": https://www2.jpgu.org/meeting/2016/session/PDF/H-DS05/HDS05-08.pdf (SCHOLARLY); https://www.scidev.net/global/news/giant-landslides-identified-by-seismic-fingerprints/ (POPULAR)
  - Pirot, Hibert, Mangeney, GJI 2024: https://www.ipgp.fr/~mangeney/pirot-etal-gji-2024.pdf (SCHOLARLY)
  - Canadian Arctic unidentified LP signal: https://essopenarchive.org/users/849895/articles/1236755-coherence-based-characterization-of-a-long-period-monochromatic-seismic-signal (SCHOLARLY, preprint)
  - Mayotte, Twitter user and USGS live seismograms: https://bigthink.com/hard-science/mystery-seismic-wave/ (POPULAR); volcano https://www.gfz.de/en/press/news/details/formation-of-a-huge-underwater-volcano-offshore-the-comoros (SECONDARY)
  - FDSN services and terms: https://service.iris.edu/fdsnws (PRIMARY); https://ds.iris.edu/ds/nodes/dmc/data/federation/ (PRIMARY)

### 2. Seismic and infrasound detection of undeclared explosions and industrial accidents

- **Data:**
  - The same FDSN archive (#1), at higher sample rates (`BH?`/`HH?`).
  - Raspberry Shake community stations, which are public through FDSN.
  - Infrasound channels (`BDF`) at stations that have them.
  - The CTBTO IMS, which is **not** public: access is through vDEC under a confidentiality contract, generally for organizations rather than individuals, with 2–4 week review.
- **Question:** Short impulsive events with explosion-like character (strong P, weak S, shallow, infrasound coupling) that match no reported quake, quarry blast, or accident. In public-interest terms that means unreported industrial explosions, dam failures, or munitions-depot fires.
- **Gap evidence:** A local Ukrainian network detected more than 1,200 explosions in three oblasts between February and November 2022, **far exceeding publicly reported attacks**. Most regional catalogs still label explosions only where mines report them.
- **Verifier:** Medium.
  - Satellite thermal anomalies (FIRMS) or optical imagery of the site.
  - News reports.
  - Quarry-blast schedules.
  - Seismic location error is often 10–30 km (as at Kakhovka), so the imagery has to do the pinpointing.
- **Precedent:**
  - NORSAR timed an explosion at the Kakhovka dam on 6 June 2023 at 02:54 local time from Ukrainian and Romanian stations. It could not establish cause.
  - The Ukraine conflict catalog (PMC10533404).
- **Recipe:**
  1. Code: STA/LTA or a pretrained picker (e.g. PhaseNet) on regional data.
  2. Code: associate picks into events, then apply explosion/earthquake discriminants (P/S ratio, depth).
  3. Code: cross-match with ComCat and mining catalogs, then with FIRMS fire pixels.
  4. LLM role: news search and report drafting.
- **Cost:** CPU, days. Regional density is the limit: public stations are sparse where events of interest happen.
- **Traps:**
  - Quarry and mine blasts dominate.
  - Sonic booms and meteors.
  - Mislabelling small earthquakes as explosions.
  - Political capture: seismic timing narrowed Kakhovka without settling blame, and claimants on both sides used it.
- **Crowding:** `CROWDED` for nuclear and military events (CTBTO, NORSAR, national labs). `PARTLY` for civilian industrial accidents.
- **Ethics:** Mixed. Detecting strikes in an active war can give targeting or battle-damage feedback to a combatant. Do not publish near-real-time conflict detections. Historical industrial-accident work is fine.
- **Scores:** data_ready 4 · gap 3 · verifier 3 · cheapness 4 · payoff 3 · ethics_clear 2
- **Sources:**
  - Ukraine explosion catalog: https://pmc.ncbi.nlm.nih.gov/articles/PMC10533404 (SCHOLARLY)
  - Kakhovka/NORSAR: https://www.wnyc.org/story/seismic-stations-detected-explosion-at-ukrainian-dam/ (POPULAR)
  - CTBTO vDEC terms: https://www.ctbto.org/resources/for-researchers-experts (PRIMARY)

### 3. Methane super-emitters: EMIT, TROPOMI, Sentinel-2, Carbon Mapper

- **Data:**
  - NASA EMIT L2B methane plume complexes (V002 released 5 Feb 2026). These are 60 m COGs plus GeoJSON with an emission-rate estimate, listed as public with no restriction on reuse.
  - Carbon Mapper's portal (about 27,700 CH₄ plumes, airborne plus EMIT plus Tanager), free for **non-commercial** research. A third-party catalog describes a modified CC BY-SA licence.
  - Sentinel-5P TROPOMI (7 km, daily, global).
  - Sentinel-2 (20 m SWIR, 2–5 day revisit) via Copernicus/AWS.
  - EMIT was built to map surface minerals for dust studies, so methane is a secondary use. Sentinel-2 was built for land monitoring, so the same applies.
- **Question:** A recurring point-source plume at a facility that is not in an emissions inventory, or whose operator reports zero.
- **Gap evidence:** Sentinel-2's 2016+ archive over oil and gas basins has only partly been swept: Varon et al. 2021 for method, and a 2021 preprint reporting more than 1,200 detections over known infrastructure. EMIT and Carbon Mapper flag plumes but do not always **attribute** them to an operator or check them against reported emissions. That attribution is where an outsider can help.
- **Verifier:** Good. Re-observation on later passes, persistence, and tasking by higher-resolution instruments. The UNEP IMEO MARS notifies operators. EMIT plumes are already manually reviewed before release.
- **Precedent:** Schuit et al. 2023 found 2,974 TROPOMI plumes in 2021 with a CNN plus SVC and published weekly. Amateur precedent: **none found** (see Unverified claims).
- **Recipe:**
  1. Code: download EMIT plume GeoJSONs for a basin.
  2. Code: join them to OpenStreetMap or national well and facility registries (e.g. US EPA GHGRP).
  3. Code: flag plumes with no registered facility, or with a facility that reports below-threshold emissions.
  4. Code: check persistence on Sentinel-2 using the Varon band-ratio method.
  5. LLM role: facility and operator research and the write-up. It does not judge plumes.
- **Cost:** CPU. Hours for one basin.
- **Traps:**
  - Retrieval artifacts over bright or dark surfaces (the reason for Schuit's SVC stage).
  - Albedo edges.
  - Mistaking a flare for a vent.
  - Landfills that look like gas sites.
  - Overstating rates from a single overpass.
- **Crowding:** `CROWDED`. SRON, Carbon Mapper, IMEO MARS, Kayrros, GHGSat, and EDF/MethaneSAT have all been active.
- **Ethics:** Clear. These are facilities and companies. Name operators only with evidence, because of defamation risk.
- **Scores:** data_ready 5 · gap 2 · verifier 4 · cheapness 4 · payoff 3 · ethics_clear 5
- **Sources:**
  - EMIT V2 release: https://www.earthdata.nasa.gov/data/alerts-outages/emit-methane-carbon-dioxide-plume-version-2-data-products-released (PRIMARY); dataset https://data.nasa.gov/dataset/emit-l2b-estimated-methane-plume-complexes-60-m-v002 (PRIMARY)
  - Carbon Mapper product guide: https://carbonmapper.org/articles/product-guide (PRIMARY); licence per https://gee-community-catalog.org/projects/cmapper (SECONDARY)
  - Schuit et al. 2023 ACP: https://acp.copernicus.org/articles/23/9071/2023/ (SCHOLARLY)
  - Varon et al. 2021 AMT: https://amt.copernicus.org/articles/14/2771/2021/ (SCHOLARLY); Sentinel-2 global tracking preprint https://arxiv.org/pdf/2110.11832v2 (SCHOLARLY, preprint)

### 4. Sentinel-1 SAR oil slicks matched to AIS

- **Data:**
  - Sentinel-1 GRD (ESA, built for land and ocean monitoring) on the AWS Open Data Registry.
  - SkyTruth **Cerulean** slick polygons through a free OGC API (`api.cerulean.skytruth.org`), with open code and the top three probable sources for each slick from AIS and platform matching.
  - AIS arrives about 72 hours late.
- **Question:** A slick with no reported spill, attributable to a vessel track or platform.
- **Gap evidence:** Weak. Cerulean already runs globally and in near real time (from 2026). What remains is the **unattributed** slicks (no AIS match, so a dark vessel) and anything before Cerulean's start.
- **Verifier:** Medium. A second SAR pass, optical Sentinel-2, and port-state records. Look-alikes are common.
- **Precedent:** SkyTruth's slick work has fed enforcement and press stories (record unverified here). Cerulean itself is the existence proof.
- **Recipe:** Code: pull Cerulean polygons with low source-confidence, then cross-match with the Global Fishing Watch SAR vessel detections (#5) to find a non-AIS vessel at the slick head. The LLM drafts the summary.
- **Cost:** CPU, hours.
- **Traps:**
  - Biogenic films.
  - Low-wind areas.
  - Rain cells.
  - Upwelling.
  - Ship wakes.
  - All of these look dark on SAR.
- **Crowding:** `CROWDED` (SkyTruth, Skylight/AI2, EMSA CleanSeaNet).
- **Ethics:** Clear for vessels and companies. Naming a vessel is a legal claim, so state the evidence and uncertainty.
- **Scores:** data_ready 5 · gap 2 · verifier 3 · cheapness 5 · payoff 2 · ethics_clear 4
- **Sources:** https://skytruth.org/cerulean/methods (PRIMARY); https://skytruth.org/cerulean-api/ (PRIMARY); https://skytruth.org/2026/03/near-real-time-coming-to-cerulean/ (PRIMARY)

### 5. Dark vessels: AIS plus SAR (Global Fishing Watch)

- **Data:** Global Fishing Watch APIs, free and **non-commercial only**, with a short impact statement at registration. They include the SAR vessel detections from Sentinel-1, classified by deep learning, 2017 to roughly the present (`public-global-sar-presence:latest`), plus AIS-derived activity, with bulk CSV/JSON export.
- **Question:** Industrial vessels operating without AIS inside closed areas, MPAs, or EEZs where they have no licence.
- **Gap evidence:** Paolo et al. (*Nature* 2024) found that **72–76% of industrial fishing vessels are not publicly tracked**. The global sweep has therefore been done. Gaps remain only at the local, MPA-by-MPA level.
- **Verifier:** Medium. Repeat detections, optical imagery, and coast-guard records. As Paolo says, "untracked" does not mean illegal: small vessels and poor AIS coverage also produce it.
- **Precedent:** Paolo et al. 2024, about 2 PB of imagery.
- **Recipe:** Code: pull SAR detections inside one MPA polygon (WDPA), then subtract AIS-matched detections and flag clusters that repeat. The LLM works on legal context (licensing, closures).
- **Cost:** CPU, hours.
- **Traps:**
  - Fixed infrastructure counted as vessels.
  - Detection-rate differences by latitude and orbit.
  - The jump from "dark" to "illegal".
- **Crowding:** `CROWDED` (GFW, Skylight, OceanMind, TMT).
- **Ethics:** Fine at vessel level. Do not chase crew identities.
- **Scores:** data_ready 5 · gap 1 · verifier 3 · cheapness 5 · payoff 2 · ethics_clear 4
- **Sources:**
  - Paolo et al. 2024 *Nature* 625, doi:10.1038/s41586-023-06825-8: https://ideas.repec.org/a/nat/nature/v625y2024i7993d10.1038_s41586-023-06825-8.html (SCHOLARLY); https://techcrunch.com/2024/01/03/satellite-imagery-analysis-shows-immense-scale-of-dark-fishing-industry/ (POPULAR)
  - GFW SAR dataset: https://globalfishingwatch.org/platform-update/2024-may-data-download-portal-new-dataset-released-featuring-vessel-detections-from-sentinel-1-sar/ (PRIMARY); https://globalfishingwatch.org/our-apis (PRIMARY)

### 6. VIIRS Nightfire gas flaring versus reported flaring and venting

- **Data:** VIIRS Nightfire (VNF) from the Earth Observation Group, Payne Institute, Colorado School of Mines. It detects flares and fires in VIIRS night-time short-wave infrared bands, a secondary use of a weather sensor. Daily CSV/KMZ (V3.0 operational, V4.0 listed), annual global flare tables from 2012, and an ORNL DAAC 2012–2019 flare survey. Users must cite EOG and Elvidge et al. 2013.
- **Question:** Flares at sites whose operator or regulator reports no flaring. Also persistent flares at sites recorded as shut in.
- **Gap evidence:** Moderate. EOG publishes per-country totals, but site-level reconciliation against permit or regulatory data (for example US state flaring reports) is patchy. SkyTruth's site-level flaring map was being migrated (status unclear). A 2025 preprint (Zhizhin et al.) builds a 2012–2025 super-resolved site catalog, which would make the join easier.
- **Verifier:** Good. High-resolution optical imagery shows the flare stack. Regulatory filings are public in many US states.
- **Precedent:** World Bank GGFR country estimates are built on VNF. Site-level accountability findings: unverified here.
- **Recipe:** Code: cluster VNF detections into sites, then join them to state well and facility databases and reported flared volumes, and rank by discrepancy. The LLM reads the regulations and drafts.
- **Cost:** CPU, hours.
- **Traps:**
  - Steel mills, refineries, and wildfires.
  - VIIRS saturation.
  - Volume estimates carry large uncertainty.
  - Sites with legal exemptions.
- **Crowding:** `PARTLY` (EOG, SkyTruth, EDF, academic groups).
- **Ethics:** Clear.
- **Scores:** data_ready 5 · gap 3 · verifier 4 · cheapness 5 · payoff 3 · ethics_clear 5
- **Sources:** https://eogdata.mines.edu/products/vnf/ (PRIMARY); https://eogdata.mines.edu/products/vnf/global_gas_flare.html (PRIMARY); https://data.ornldaac.earthdata.nasa.gov/public/cms/Methane_Flaring_Sites_VIIRS/comp/Methane_Flaring_Sites_VIIRS.pdf (PRIMARY); https://skytruth.org/flaring/methods (SECONDARY)

### 7. Lost and "zombie" satellites: SatNOGS radio archive plus public orbits

- **Data:**
  - SatNOGS Network observations (waterfalls, audio, decoded frames) from a global volunteer ground-station network, all **CC BY-SA 4.0** through the API.
  - SatNOGS DB of transmitters, which allows entries with no NORAD ID.
  - Public general-perturbation orbits (CelesTrak; Space-Track, whose user agreement historically restricted redistribution. Libre Space signed a 2026 redistribution agreement with USSPACECOM).
- **Question:** Recorded signals that match no active transmitter but whose Doppler curve fits the orbit of a satellite listed as dead.
- **Gap evidence:** SatNOGS holds millions of observations that are scheduled against known satellites. Unexpected carriers in the waterfalls are not systematically mined (no published sweep found).
- **Verifier:** Mechanical. The Doppler curve must match one object's TLE across passes and stations. A second station confirms. The operator, or its successor, can confirm.
- **Precedent:**
  - Phil Williams (Cornwall) heard **LES-1** (silent since 1967) in 2013.
  - Scott Tilley found NASA's **IMAGE** (lost 2005) in January 2018 while hunting Zuma. NASA verified it with five antennas.
  - Tilley found **LES-5** in March 2020.
- **Recipe:**
  1. Code: pull waterfalls for passes, then detect carriers off the expected frequency.
  2. Code: fit a Doppler curve and grid-match it against the TLEs of every catalogued object above the horizon.
  3. The LLM helps with archival research on the matched satellite (frequencies, history).
- **Cost:** CPU. Waterfall images add up, but one band (for example 230–240 MHz, or 2.2 GHz S-band) is a few GB.
- **Traps:**
  - Terrestrial interference.
  - Harmonics.
  - Several objects with near-identical passes.
  - Confusing debris with payloads.
- **Crowding:** `PARTLY`, a small amateur community (Tilley, SatNOGS volunteers).
- **Ethics:** Keep to dead civil and scientific spacecraft. Characterizing classified or active military satellites (orbit, maneuvers, emissions) is the ELINT line above. It is legal in many places, but out of scope here as security-adjacent. **Unannounced-maneuver detection from TLE histories** is dropped for the same reason, except for debris-safety framing done by established groups.
- **Scores:** data_ready 4 · gap 3 · verifier 5 · cheapness 4 · payoff 2 · ethics_clear 3
- **Sources:**
  - IMAGE and LES-5, Tilley: https://www.npr.org/2020/04/24/843493304/long-lost-u-s-military-satellite-found-by-amateur-radio-operator (POPULAR); NASA re-contact details conflict across sources (see Unverified claims)
  - LES-1, Williams: https://iflscience.com/nearly-half-a-century-after-being-lost-zombie-satellite-les-1-began-sending-signals-to-earth-81164 (POPULAR)
  - SatNOGS licence: https://satnogs-network.readthedocs.io/en/latest/api.html (PRIMARY); https://wiki.satnogs.org/DB (PRIMARY)
  - Space-Track redistribution: https://spaceflightnow.com/news/n0503/02observing/index2.html (POPULAR, 2005); Libre Space agreement https://community.libre.space/t/libre-space-signs-agreement-with-us-space-command/8175?page=2 (CLAIMANT/forum)

### 8. Ocean passive-acoustic archives for unattributed sounds

- **Data:**
  - NOAA NCEI Passive Acoustic Data archive, free on Google Cloud bucket `noaa-passive-bioacoustic` through NODD. It includes SanctSound, the NOAA Noise Reference Stations, and Glacier Bay, collected for marine-mammal and noise monitoring.
  - OOI Regional Cabled Array hydrophones.
  - PubDAS: about 90 TB of public fiber DAS from 8 experiments, including OOI seafloor cables that record fin and blue whale calls.
  - CTBTO hydroacoustic data is vDEC-only.
- **Question:** Recurrent sound types with no attribution, matched later to a species, ice, volcano, or vessel.
- **Gap evidence:** These archives are many years of audio, mostly analysed for target species. Off-target sound types go uncatalogued.
- **Verifier:** Weak to medium. You need a simultaneous visual sighting (as with the biotwang), a seismic or volcanic correlate, or ice imagery. Most "unknown" sounds stay unknown.
- **Precedent:** The **Western Pacific biotwang**, recorded 2014 near the Marianas and named in 2016 (Nieukirk et al., JASA). NOAA attributed it to Bryde's whales after 9 of 10 sightings in 2018 coincided with the call, then searched historical recordings for its seasonal range.
- **Recipe:** Code: compute spectrogram embeddings (e.g. a pretrained bioacoustic model), cluster them, and remove known classes. A human expert labels the leftovers. The LLM does literature lookup only.
- **Cost:** Cheap to sample, expensive to sweep (TB of audio). A GPU helps for embeddings.
- **Traps:** The **Bloop** (1997), recorded by hydrophones nearly 4,800 km apart, became a "sea monster" meme until NOAA attributed it to an icequake. Most unknowns are ice, ships, or instrument self-noise.
- **Crowding:** `PARTLY` (NOAA/PMEL, OSU, Scripps, bioacoustics ML groups).
- **Ethics:** Clear. Precise locations of endangered whale aggregations are mildly sensitive.
- **Scores:** data_ready 4 · gap 3 · verifier 2 · cheapness 3 · payoff 2 · ethics_clear 5
- **Sources:**
  - NCEI: https://www.ncei.noaa.gov/products/passive-acoustic-data (PRIMARY)
  - PubDAS, Spica et al. 2023 SRL: https://pure.psu.edu/en/publications/pubdas-a-public-distributed-acoustic-sensing-datasets-repository-/ (SCHOLARLY)
  - OOI DAS whales: https://par.nsf.gov/biblio/10483132-distributed-acoustic-sensing-recordings-low-frequency-whale-calls-ship-noise-offshore-central-oregon (SCHOLARLY)
  - Biotwang: https://www.sciencedaily.com/releases/2016/12/161214151649.htm (POPULAR); https://repository.library.noaa.gov/view/noaa/66329 (SCHOLARLY)
  - Bloop: https://en.wikipedia.org/wiki/List_of_unexplained_sounds (SECONDARY)

### 9. ADS-B historical data: GNSS interference and public-agency flight patterns

- **Data:** ADS-B Exchange `readsb-hist`. Snapshots every 5 s since May 2020 and every 60 s since July 2016. The **1st of each month is free** at `samples.adsbexchange.com/readsb-hist/yyyy/mm/dd`, and other days require a paid licence. No bulk redistribution is allowed. The service has been owned by JETNET since January 2023 and does not honour FAA LADD filtering. ADS-B itself is broadcast for air-traffic safety.
- **Question:**
  - (a) Regions and periods of GNSS jamming or spoofing, inferred from NIC/NACp degradation across many aircraft.
  - (b) Persistent orbit patterns by government aircraft over cities, the BuzzFeed method.
- **Gap evidence:**
  - (a) gpsjam.org (John Wiseman, 2022) already maps this daily, so the gap is only historical (2016–2022) or in sparse regions. Empty areas are not evidence of clean airspace.
  - (b) BuzzFeed covered August to December 2015 only.
- **Verifier:**
  - (a) NOTAMs, pilot reports, and the multi-aircraft coincidence rule. One false-positive mode is documented: aerobatic military trainers in Texas and Oklahoma reporting low NIC while neighbours were fine.
  - (b) Registration records (FAA registry), FOIA, agency confirmation.
- **Precedent:** BuzzFeed News, "Spies in the Skies" (Aldhous and Seife, 6 April 2016): about 200 FBI/DHS aircraft from Flightradar24 data. Agencies confirmed the programmes but not individual flights.
- **Recipe:** Code: parse the free monthly days, compute per-cell low-NIC fractions, and difference them against gpsjam (a) or find circling tracks by registration owner (b). The LLM drafts and looks up registrations.
- **Cost:** CPU. One free day is about tens of GB uncompressed.
- **Traps:**
  - Single-aircraft avionics faults.
  - Sparse coverage that reads as absence.
  - The jump from "orbiting" to "surveilling".
- **Crowding:** (a) `CROWDED` (gpsjam, Flightradar24, SkAI). (b) `PARTLY` (journalists).
- **Ethics:** **Hard limit.** Government and agency aircraft as institutions are fair public-interest targets. **Tracking private aircraft back to individuals (celebrity jets, "ElonJet"-style) is out of scope and dropped.** Mapping current jamming in active war zones has operational value to combatants, so publish only historical, aggregated maps. Respect the ADS-B Exchange ToS (no redistribution).
- **Scores:** data_ready 3 · gap 2 · verifier 3 · cheapness 4 · payoff 2 · ethics_clear 2
- **Sources:**
  - ADS-B Exchange samples: https://www.adsbexchange.com/data-products/sample-data/ (PRIMARY, via search snippet; direct fetch blocked from this container)
  - JETNET acquisition: https://jetnet.com/news/jetnet-acquires-ads-b-exchange.html (PRIMARY)
  - gpsjam: https://gpsjam.org/about (PRIMARY); false positive https://www.gpsworld.com/one-gps-mystery-solved-another-remains/ (POPULAR)
  - BuzzFeed 2016: https://clips.cato.org/sites/default/files/Bates%20Buzzfeed%20Surveillance.pdf (POPULAR, archived copy); https://flowingdata.com/2016/04/08/us-surveillance-flight-paths-for-the-fbi-and-homeland-security (POPULAR)

### Not promoted to candidates

- **oldWeather / ship-log weather rescue.** Volunteers transcribed about 1.6 million Royal Navy observations, and oldWeather3 (US Arctic) transcribed 1.3 million and counting. Valuable work, but it is document transcription, so it belongs with the documents/archives survey. It is also already crowdsourced (`CROWDED`). Source: https://en.wikipedia.org/wiki/Old_Weather (SECONDARY); https://brohan.org/transcription_methods_review/case_studies/oldweather/oldweather3/oldweather3.html (SECONDARY).
- **WSPR for MH370 (trap).** Richard Godfrey's WSPR "aircraft scatter" analysis is `contested`. Critics (Iannello, Gilbert, Kent; an RTL-SDR critique) point to dependence on long-path propagation, duplicate-discarding that biases toward the hypothesis, a reported AUROC of about 58.66%, and results that shifted between versions. A University of Liverpool team ran validation on known 777 flights; I did not find their result. Record this as a cautionary case: a weak signal plus a flexible model plus a desired location. Sources: https://www.airlineratings.com/articles/critics-of-wsprnet-tracking-mh370-been-answered (POPULAR); https://www.rtl-sdr.com/nils-critiques-the-mh370-wspr-aircraft-scatter-theory/ (POPULAR); https://news.liverpool.ac.uk/?p=118153 (SECONDARY).
- **Numbers stations.** A trap. The only "solve" is the operator's key, and the messages are intelligence traffic, so decrypting them would be intercepting communications. Out of scope.
- **Lightning networks.** Blitzortung is community-run with restrictive reuse terms. WWLLN and GLD360 are academic or commercial. No discovery-shaped gap found. Not researched further.
- **Ionosonde / SuperDARN.** Open to researchers, but no unanswered question with a verifier found in budget. Dropped.

---

## Pilot in a day

**Candidate #1: find past fjord-seiche / landslide signals in long-period seismic data and check them against satellite imagery.**

The aim is to rerun the method that found five extra Dickson Fjord events, on a different region (for example West Greenland, Svalbard, or SE Alaska fjords), and test each detection with imagery. The pipeline is CPU-only; the check is visual and decisive.

1. **Environment:** `uv venv && uv pip install obspy numpy scipy pystac-client rasterio`. Note: this container's egress proxy returned 403 for `service.iris.edu` and `adsbexchange.com`, so the pilot needs a VM whose egress allows `service.iris.edu`, `earthquake.usgs.gov`, `earth-search.aws.element84.com`, and `sentinel-cogs.s3.us-west-2.amazonaws.com`.
2. **Stations:** run `https://service.iris.edu/fdsnws/station/1/query?minlatitude=55&channel=LHZ&level=channel&starttime=2017-01-01&endtime=2023-12-31&format=text`. Pick about 25 stations with long uptime, including the GSN plus the Greenland GLISN stations. Check codes from this output rather than from memory.
3. **Waveforms:** loop day by day with `https://service.iris.edu/fdsnws/dataselect/1/query?net=XX&sta=YYY&cha=LHZ&starttime=…&endtime=…`. Keep to 3 or fewer concurrent requests. Two years × 25 stations is about 2 GB.
4. **Known-event mask:** pull M ≥ 6.5 events from `https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&minmagnitude=6.5&starttime=2017-01-01&endtime=2023-12-31` and mask 5 days after each one, to remove free-oscillation ringing.
5. **Detector (code, not LLM):** compute 6-hour Welch spectra from 3 to 30 mHz and flag peaks more than 10 dB above that station's monthly median, with a −3 dB width under 0.2 mHz. Keep a detection only if the same frequency (±0.1 mHz) appears at 3 or more stations within 2 hours. Grid-search the location by fitting arrival-time or phase differences with a Rayleigh-wave group velocity of about 3.8 km/s. Calibrate on 16 September 2023 and 11 October 2023 (Dickson Fjord, ~10.88 mHz). **If the detector does not recover those, stop and fix it** (Rule 7).
6. **Verifier:** for each candidate, query STAC `https://earth-search.aws.element84.com/v1` (collection `sentinel-2-l2a`) for low-cloud scenes within ±30 days, inside a 50 km box around the location. An LLM can triage the image pairs for fresh scars or deposits; a human confirms. Then search GEUS and NVE news, local news, and Petley's Landslide Blog for a prior report.
7. **Output:** put scripts and a CSV of candidates with spectra, location, image-pair links, and verdict under a future `analysis/` directory. Report "N candidates, M confirmed by imagery, K previously unreported". A result of zero is a valid finding about the detector's sensitivity.

A shortcut worth trying first: email Piero Poli (now at Padova, per the unipd record) for the SRL catalog's list of unidentified sources, then skip to step 6.

## Unverified claims

- **Whether Poli's catalog of more than 1,700 unidentified long-period sources is public.** No data-availability statement or Zenodo record was found. Only the abstract was checked; author list and year are unconfirmed from the abstract page (full text not fetched).
- **The EGU 2024 "five other previously undetected events" wording.** It comes from an abstract and differs between versions; the final peer-reviewed count may differ.
- **Whether citizen scientists first flagged the 2023 Dickson Fjord signal.** Sources say seismologists found it; Mayotte 2018's Twitter-user origin is reported only in popular press.
- **Ekström's "~10 false positives per real landslide".** Taken from a SciDev summary, not the paper. Also unknown: whether a maintained public global landslide-detection catalog exists today.
- **IMAGE (2018).** Sources conflict on whether NASA re-established commanding or only received telemetry before the signal faded.
- **LES-1.** 2013 is the year Williams heard it; some sources say identification took until 2016.
- **Amateur or independent discoveries of methane super-emitters** with public satellite data: none found. The brief's precedent question remains open.
- **Carbon Mapper's licence** (modified CC BY-SA, non-commercial) is from a third-party catalog. Plume counts are from the homepage at time of search.
- **Space-Track's current redistribution terms.** The 2005 restrictions and a 2026 secondary claim that "all GP data is publicly available" conflict.
- **SkyTruth Cerulean or flaring findings leading to enforcement:** not checked.
- **WSPR/MH370.** The University of Liverpool validation result was not found.
- **ADS-B Exchange sample page.** Details are from search snippets; direct fetch was blocked by this container's proxy (403). It is unknown whether JETNET changed historical-data access.
- **BuzzFeed's "Spies in the Skies".** The original article was not fetched; details come from secondary summaries.
