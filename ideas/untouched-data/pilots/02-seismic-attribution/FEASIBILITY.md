# Pilot 02 feasibility: attributing published unidentified long-period seismic sources with imagery

*2026-10-18. Scope: candidate 1 of `sources/untouched-data/04-signals-geophysics-osint.md`,
the attribution half only (no waveform pulls). This is a desk check of feasibility. No
attribution was attempted (Rule 9).*

## Summary

1. **No-go for a pilot from this container as it stands.** The imagery side is reachable:
   Sentinel-2 L2A COGs on AWS (`sentinel-cogs`), the Sentinel-2 and Landsat archives on Google
   Cloud Storage, and Copernicus DEM all answer, with byte-range reads working. The **input side
   is not reachable**. None of the event catalogs can be fetched: the Poli catalog's location is
   unknown and GeoScienceWorld is blocked; ScienceBase (ESEC), Zenodo, PANGAEA, EarthScope SPUD,
   Wiley and OUP are all blocked; GitHub search is blocked, though raw files are reachable.
2. **No public, downloadable copy of Poli's ">1,700 unidentified sources" was found.** It may sit
   in the SRL supplement, but that could not be checked. The only clearly downloadable list of
   seismogenic mass movements is ESEC/USGS (SQLite + `Events.csv` on ScienceBase). Those events
   are *already attributed*, so they are a calibration set, not a source of finds.
3. **Crowding is higher than the survey said.** IPGP now holds 6,263 previously undocumented
   Greenland glacial earthquakes for 2013–2024 (EGU26). Poli says his unidentified sources are
   *mostly polar and glacial*, so imagery shows terminus change, not a scar. Takano & Poli 2025
   took one leftover (a Canadian Arctic signal) and left it as "likely glacier dynamics". USGS
   and the Alaska Earthquake Center already detect landslides in Alaska and confirm them with
   imagery in near real time.
4. **What would flip it to go:** either (a) the user hand-carries Poli's SRL supplement (or an
   emailed table) into the repo, or (b) the proxy allows `pubs.geoscienceworld.org`,
   `zenodo.org`, `www.sciencebase.gov` and `ds.iris.edu`/`data.earthscope.org` (SPUD/ESEC). Add
   `earth-search.aws.element84.com` or `planetarycomputer.microsoft.com` for proper STAC search.
   Without STAC, a script can still find scenes by listing S3 tile prefixes or the GCS
   `index.csv.gz`, so STAC is a convenience, not a blocker.
5. **Shape of the pilot once inputs exist:** a calibration run first. Rule 7: do ESEC events
   with known scars come back as "scar found"? Then a run over the *non-polar, non-volcanic*
   remainder of Poli's list, where a rock-avalanche scar of at least 10⁶ m³ is visible at 10 m.
   Expect a low yield and a ~100 km search radius per event.

---

## 1. Are the unidentified-source lists downloadable?

| Catalog | What it is | Downloadable table? | Where / format | Reachable here? |
|---|---|---|---|---|
| **Poli 2024, SRL 95(3):1486, doi:10.1785/0220230148** | 2010–2022, 25–100 s Rayleigh-wave delay-and-stack; >36,000 detections, **>1,700 previously unidentified**, each with location, uncertainty and Mw | **Not found.** The abstract says every source has a location, an uncertainty and a Mw, so the table exists. No Zenodo/GitHub/"Data and Resources" link turned up in three searches. Most likely in the SRL electronic supplement, or available from the author (piero.poli@unipd.it, per search result). See Unverified claims. | GeoScienceWorld (paywalled supplement?) | No (GSW DNS/proxy blocked; WebFetch also fails) |
| Takano & Poli 2025, GRL, doi:10.1029/2024GL113290 | Coherence-based characterization of long-period monochromatic signals. Gulf of Guinea, Vanuatu, a submarine volcano, and one "previously unidentified" Canadian Arctic signal, "likely associated with glacier dynamics" | A handful of named events, not a table | Wiley; ESS Open Archive preprint | No |
| **Ekström / Lamont (Ekström & Stark 2013, Science 339, doi:10.1126/science.1232887)** | Long-period surface-wave landslide detector; 29 teleseismic landslides in the paper; ~50 landslides analysed by 2015, "several never reported" | **No public rolling catalog found.** The NSF/Columbia project pages are marked inactive, with the last grant ending in 2016. | Paper tables only | No (ldeo.columbia.edu blocked) |
| **ESEC (Bahavar et al. 2019 SRL, doi:10.1785/0220180402) / USGS "Seismogenic Landslides and other Mass Movements"** | Compilation of seismically recorded landslides, debris flows and avalanches; 121 → 242 events after the major update | **Yes.** SQLite `lsseis.db` + `Events.csv` on ScienceBase, plus an EarthScope SPUD web interface. **All events are already attributed**, so this is the calibration set. | ScienceBase (CSV/SQLite); ds.iris.edu/ds/products/esec | No (sciencebase.gov, ds.iris.edu blocked) |
| **Pirot, Hibert & Mangeney 2024, GJI 236:849, doi:10.1093/gji/ggad402** | Greenland glacial earthquakes, STA/LTA + Random Forest over 844 days; **1,633 new events** | Data-availability statement not reached; no Zenodo deposit found | OUP | No |
| **Wetter, Mangeney, Hibert, Stutzmann (EGU25-9652; EGU26-14626)** | Greenland 2013–2024, Random Forest; **6,263 previously undocumented glacial earthquakes**, MSW 4.1–5.4 (EGU26) | Abstract only; no release found | Copernicus Meetings | No |
| **GEUS / Svennevig et al. 2024 (Science 385:1196) and Koelemeijer et al. EGU24-5821** | Dickson Fjord 2023 plus a 10.85–11.02 mHz archive search: 5 earlier events, of which ≥4 of 6 tie to Dickson landslides in optical/SAR archives and **2 remain unresolved** | The events are listed in the papers; no separate catalog | Science supplement / EGU abstract | No |
| Phạm et al. 2025 GRL, doi:10.1029/2025GL118885 | Thwaites/Pine Island glacial earthquakes 2010–2023, 362 events, mostly uncatalogued | **Yes, on Zenodo** (per search result) | Zenodo | No (zenodo.org blocked) |

**Bottom line for Q1:** the two lists that would yield finds (Poli; the two unresolved
Dickson-family events) are not in any form this container can fetch. The one clean
downloadable list (ESEC) contains attributed events only.

## 2. Who has already worked the leftovers with imagery since 2023? (Crowding)

- **Svennevig, Koelemeijer, Widmer-Schnidrig et al. (GEUS/Oxford/BFO).** They searched the
  Dickson-type 10.9 mHz signal back through the archive and checked each hit against optical and
  SAR archives. Four of six events were attributed and two left open. This is exactly the
  attribution task, done by the people best placed to do it, for that one signal family.
- **Takano & Poli (2025).** A follow-up on Poli's own unidentified signals. Their one new
  attribution ("Canadian Arctic, likely glacier dynamics") is not a scar-type attribution.
- **IPGP glacial group (Pirot 2024 → Wetter EGU25/EGU26).** They are systematically building
  catalogs of undocumented Greenland glacial earthquakes. Most of Poli's polar leftovers fall
  in their domain. Glacial earthquakes are calving events that a geologist would check against
  terminus position, and the group does this professionally.
- **USGS / Alaska Earthquake Center (Karasözen & West; Toney, Allstadt et al. JGR 2026).** They
  detect landslides in coastal Alaska in near real time, locate them "within a couple of
  kilometers" with a dense network, and confirm them by overflight or satellite. Barry Arm
  2023: seven landslides flagged and later confirmed. SE Alaska is one of Ekström's two
  "unreported landslide" hotspots, so it is crowded.
- **Not found:** any public effort, professional or amateur, that walks Poli's full non-polar
  remainder against Sentinel-2/Landsat. The Himalaya-Karakoram, Ekström's other hotspot, has
  satellite-only landslide inventories, for example a 30-year deep-learning Himalayan study, but
  I found no seismic-plus-imagery sweep there. **Revised crowding: `PARTLY`, leaning crowded.**
  Polar and glacial: crowded. SE Alaska: crowded. Remote non-polar mountains (HKH, Andes,
  Kamchatka, New Zealand Alps, Pamir): apparently open, but that rests on searches that could
  not reach the paywalled literature.

## 3. Imagery and catalog routes from this container (tested 2026-10-18, `curl -m 15`)

`000` = proxy refused CONNECT (`curl: (56) CONNECT tunnel failed, response 403`).

| Endpoint | HTTP | Note |
|---|---|---|
| Copernicus Data Space STAC `https://catalogue.dataspace.copernicus.eu/stac` | 000 | blocked |
| CDSE STAC v1 `https://stac.dataspace.copernicus.eu/v1/` | 000 | blocked |
| Element84 earth-search `https://earth-search.aws.element84.com/v1` | 000 | blocked |
| Microsoft Planetary Computer STAC | 000 | blocked |
| USGS M2M `https://m2m.cr.usgs.gov/api/api/json/stable/` | 000 | blocked |
| NASA CMR `collections.json?keyword=sentinel` | 000 | blocked |
| Landsat Look STAC `https://landsatlook.usgs.gov/stac-server` | 000 | blocked |
| **`https://sentinel-cogs.s3.us-west-2.amazonaws.com/`** | **200** | Bucket listing works (`?list-type=2&prefix=sentinel-s2-l2a-cogs/27/W/VM/2023/9/` returned scenes). **Range reads of item JSON and `B04.tif` → 206.** |
| `https://sentinel-s2-l2a-stac.s3.amazonaws.com/` | 200 | static STAC item bucket |
| `https://storage.googleapis.com/gcp-public-data-sentinel-2/` | 200 | S2 L1C archive (2015–) |
| **`https://storage.googleapis.com/gcp-public-data-landsat/index.csv.gz`** | **206** | Landsat archive back to the 1980s, with a scene index; this replaces STAC search |
| `https://copernicus-dem-30m.s3.amazonaws.com/` | 200 | DEM for slope/relief checks |
| `https://sentinel-s1-l1c.s3.amazonaws.com/` | 200 | listed; S1 is requester-pays in practice (untested for objects) |
| `https://usgs-landsat.s3.us-west-2.amazonaws.com/` | 403 | requester-pays bucket (expected) |
| `https://raw.githubusercontent.com/...` | **200** | raw files reachable if a catalog is on GitHub at a known path |
| `https://api.github.com/search/...` | 403 | "sessions are bound to their configured repositories", so you cannot *discover* repos |
| `https://zenodo.org/` (and `/api/records`) | 000 | blocked |
| sciencebase.gov, usgs.gov, ds.iris.edu, data.earthscope.org, earthquake.usgs.gov FDSN | 000 | blocked: no ESEC, no ComCat to rule out known quakes |
| pangaea.de, datadryad.org, figshare.com, osf.io, GFZ data services, huggingface.co | 000 | blocked |
| pubs.geoscienceworld.org, academic.oup.com, Wiley, science.org, essopenarchive.org, ipgp.fr, pub.geus.dk | 000 | blocked to curl; WebFetch also failed (DNS) for GSW, ResearchGate, ipgp.fr |

**Reading:** a script *can* pull before/after Sentinel-2 (2015–) and Landsat (1980s–) chips
for any lat/lon/date, and a DEM, without any STAC API. It does this by mapping lat/lon to MGRS
tile or WRS path/row, then listing the bucket prefix or the GCS index. Two things it cannot do:
get the event list, and check ComCat to exclude catalogued earthquakes. The ComCat check is
part of the crank filter (see false positive 3 below).

## 4. What a confirmed find looks like

**Size.** Landslides that a *global* long-period network records:
- Dickson Fjord 2023: 25.5 × 10⁶ m³ (Svennevig et al. 2024).
- Denali ice–rock avalanche: 6.1 × 10⁶ m³ (Toney et al. 2026).
- Tyndall Glacier 2015: ~200 Mt, about 7 × 10⁷ m³ at ~2.7 t/m³ (Lamont/NASA).

Ekström's own threshold for "unreported" was >10 Mt. So a real find is a source zone and
deposit **hundreds of metres to several km long**, which is tens to hundreds of Sentinel-2
pixels. A glacial earthquake instead shows up as a **km-scale calving or terminus retreat**
between two cloud-free scenes days apart.

**Location error.**
- Dense regional network: "within a couple of kilometers" (Karasözen & West).
- Teleseismic long-period: Lamont says "within a few kilometers" for its landslide inversions,
  which are refined events.
- A global 25–100 s grid search is far coarser. Poli's per-event uncertainties exist but could
  not be read.
- **Plan on a 50–150 km search radius** for Poli-class detections (inference; see Unverified).
  Inside that radius, the timing has to do the attribution: one 10–20 day before/after image
  window, cut by cloud and, at polar latitudes, polar night.

**What the geologist would want to see**, the "what a solution would have to do" list (Rule 4):
1. A before/after image pair bracketing the seismic origin time as tightly as cloud allows,
   showing a fresh source scar *and* a deposit or runout path. Two dates the change is not
   visible in are also needed (before-before and after-after) to rule out seasonal snow and
   shadow.
2. A volume estimate (area × plausible depth, or DEM differencing where a post-event DEM
   exists) consistent with the seismic Mw or force amplitude. A 10⁵ m³ scar cannot explain a
   teleseismic detection.
3. Runout direction consistent with the force-history azimuth, if a single-force inversion
   exists.
4. Exclusion of every catalogued earthquake (ComCat/ISC) in the window, and of volcanic
   activity (Smithsonian GVP).
5. No *second* candidate scar inside the error ellipse in the same window. If there is one, the
   attribution is ambiguous and is recorded as such.
6. Where water is involved, a tsunami trimline or seiche evidence.

**Top three false-positive modes**
1. **Seasonal and illumination change mistaken for a scar.** This is the largest risk for an
   LLM triaging image pairs. Snowmelt exposing rock, new snowfall, shadow length changing
   between dates, cloud shadow, and debris-covered glacier surface changes all look like
   fresh scars. They are controlled with matched-season pairs and the four-date rule above.
2. **Wrong or old scar inside a large error ellipse.** A 100 km radius in active mountains
   holds many landslides per year. An older scar, or one that failed on a different date
   (rockfall seasons, debris flows after rain), gets pinned on the seismic event. That is the
   look-elsewhere effect, and the imagery cadence (5 days at best, often weeks of cloud) cannot
   always break it. Dickson's "2 of 6 unresolved" shows that even experts hit this wall.
3. **A non-landslide source that the input list mislabelled as unidentified.** Glacial
   earthquakes and calving (most of Poli's polar sources), volcanic VLP, an earthquake missing
   from the catalog searched, microseism or storm bursts, or instrument artefacts. Poli removed
   spurious detections, but Ekström's detector ran at roughly 10 false positives per real
   landslide (Petley commentary). A clean image of *some* change near such a detection does not
   make it a landslide.

## Sources

- Poli, SRL 95(3):1486 (2024), doi:10.1785/0220230148. Abstract: https://www.citedrive.com/en/discovery/continuation-of-events-detection-with-global-long-period-seismic-data-an-analysis-from-2010-to-2022/ (SCHOLARLY, abstract only); article page https://pubs.geoscienceworld.org/ssa/srl/article/95/3/1486/627619 (SCHOLARLY, not reached)
- Takano & Poli 2025, GRL, doi:10.1029/2024GL113290: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL113290 ; preprint https://essopenarchive.org/users/849895/articles/1236755-coherence-based-characterization-of-a-long-period-monochromatic-seismic-signal (SCHOLARLY, abstract via search)
- Ekström & Stark 2013, Science 339, doi:10.1126/science.1232887: https://academiccommons.columbia.edu/doi/10.7916/D8TQ610D (SCHOLARLY); Petley commentary on overdetection https://blogs.agu.org/landslideblog/2013/03/22/a-very-important-new-paper-detecting-large-landslides-using-seismic-data/ (POPULAR); Lamont, "within a few kilometers", Tyndall ~200 Mt https://news.climate.columbia.edu/2015/12/18/detecting-landslides-from-a-few-seismic-wiggles/ (SECONDARY); project status https://people.climate.columbia.edu/projects/view/685 (SECONDARY)
- ESEC: https://ds.iris.edu/ds/products/esec (PRIMARY); https://pubs.usgs.gov/publication/70203412 (SCHOLARLY); USGS data release https://www.usgs.gov/data/seismogenic-landslides-and-other-mass-movements (PRIMARY); update abstract https://meetingorganizer.copernicus.org/EGU22/EGU22-3172.html (SCHOLARLY)
- Pirot, Hibert & Mangeney 2024, GJI 236:849: https://academic.oup.com/gji/article/236/2/849/7328939 (SCHOLARLY, abstract via search)
- Wetter et al., EGU25-9652 https://meetingorganizer.copernicus.org/EGU25/EGU25-9652.html and EGU26-14626 https://meetingorganizer.copernicus.org/EGU26/EGU26-14626.html (SCHOLARLY, abstracts)
- Phạm et al. 2025 GRL, Thwaites glacial earthquakes, Zenodo catalog: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL118885 (SCHOLARLY)
- Svennevig et al. 2024, Science, doi:10.1126/science.adm9247: https://www.science.org/doi/10.1126/science.adm9247 (SCHOLARLY); Koelemeijer et al. EGU24-5821, "at least four out of six", https://meetingorganizer.copernicus.org/EGU24/EGU24-5821.html (SCHOLARLY, abstract)
- Karasözen & West, "within a couple of kilometers": https://seismosoc.org/news/seismic-data-detects-alaskan-landslides-that-could-trigger-tsunamis (SECONDARY); https://scholarworks.alaska.edu/uaf_earthquake_reports/42 (SCHOLARLY, report)
- Toney et al. 2026, JGR Earth Surface, Denali 6.1 × 10⁶ m³: https://www.usgs.gov/publications/rapid-seismic-and-infrasound-assessment-large-landslides-a-case-study-denali-national (SCHOLARLY)
- Barry Arm near-real-time detection and confirmation: https://pubs.geoscienceworld.org/ssa/tsr/article/4/1/43/634286/Toward-the-Rapid-Seismic-Assessment-of-Landslides (SCHOLARLY, via search summary)
- Endpoint HTTP codes: measured from this container, 2026-10-18 (PRIMARY, this file)

## Unverified claims

- **Where Poli's table lives.** It is likely the SRL electronic supplement, but not confirmed;
  GeoScienceWorld, ResearchGate and Zenodo were unreachable. The author contact address
  (piero.poli@unipd.it) comes from a search-engine summary only.
- **Poli's per-event location uncertainty.** The 50–150 km working radius above is an inference
  from a 25–100 s global grid search, not a number read from the paper.
- **"Mostly polar / glacier dynamics" for Poli's unidentified sources.** This rests on the
  abstract wording as relayed by a search summary.
- **Pirot 2024 data availability.** Whether the 1,633 events are deposited, and where, is
  unknown.
- **The Thwaites catalog Zenodo deposit** (Phạm et al. 2025) comes from a search summary only.
- **EGU25 "4,500" vs EGU26 "6,263" undocumented Greenland glacial earthquakes.** Only the EGU26
  figure was seen in a result snippet; the EGU25 count is unconfirmed.
- **ESEC file names** (`lsseis.db`, `Events.csv`) and the current USGS data-release version: a
  search result mentioned "ver 4.0, October 2026", which was not verified.
- **Absence of any seismic-plus-imagery sweep of the HKH or Andes leftovers.** This is an
  absence-of-evidence result from open-web search that could not reach the paywalled
  literature.
- **The ~10 false positives per real landslide figure** traces to a popular summary (SciDev,
  per the survey file) and Petley's "order of magnitude" blog line, not to the paper itself.
- **Sentinel-1 on `sentinel-s1-l1c`:** the bucket root answered 200, but object reads were not
  tested and are requester-pays in practice.
