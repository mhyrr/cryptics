# Pilot 02: unidentified long-period seismic sources

*Opened 2026-11-10 on Greg's machine. `FEASIBILITY.md` (2026-10-18) called this a no-go from
the cloud container because the inputs were unreachable. From here they are reachable, and
Poli's catalog is public.*

## Question

Poli (SRL 2024) detected long-period (25–100 s) seismic sources worldwide for 2010–2022 that
are not in earthquake catalogs. Which of them are large landslides that nobody has tied to
the seismic signal, and can a before/after satellite image prove it?

## What a solution would have to do

Unchanged from `FEASIBILITY.md` §4: a before/after image pair bracketing the origin time with
a fresh scar and deposit; two control dates showing no change; a volume that fits the seismic
size; no catalogued earthquake or eruption in the window; no second scar inside the error
disk. A detection with a plausible image and none of the controls is a lead, not a find.

## Data (in `data/`)

| File | Source | Tier | Note |
|---|---|---|---|
| `poli-2023-catalog.csv` | Poli, "Global long period earthquake catalog", Zenodo, doi:10.5281/zenodo.8181257, CC-BY 4.0 | PRIMARY | 1,766 rows: 0.5° grid lat/lon, origin time, Md, Mw_d. Fetched 2026-11-10. |
| `esec-v4-Events.csv` | USGS, "Seismogenic Landslides and other Mass Movements" ver. 4.0 (Oct 2026), ScienceBase item 68221c34d4be02673d76ba1d | PRIMARY | 338 attributed mass movements. The calibration set. |
| `comcat-m4-2010-2023.csv.gz` | USGS ComCat via FDSN, M ≥ 4.0 | PRIMARY | 194,058 events. Rebuilt by `02-triage/fetch.py`. |
| `ne_110m_admin_0_countries.geojson` | Natural Earth 1:110m | SECONDARY | Coarse land/country mask only. |

## Experiments

### 01 — Poli × attributed landslides (`01-poli-x-esec/`)

Does Poli's detector record landslides whose place and time are known, and how far off is it?

- 19 ESEC events match 16 Poli detections (three detections each cover a main and a secondary
  event). Chance control, 200 whole-day shifts: mean 0.02 matches.
- **Location error: 29–317 km, median 93 km.** Time offset (Poli minus ESEC start) for single
  events: about +50 to +180 s.
- Recall is low: 14 of 44 ESEC events ≥ 10⁶ m³ in the time span. Taan Fjord 2015, Lamplugh
  2016, Nuugaatsiaq 2017 and Bingham Canyon 2013 are absent. The catalog is not a complete
  landslide detector. Why those are absent is not known (see Open points).
- Poli's first row is the Attabad landslide (Hunza, 4 Jan 2010), 150 km from its grid cell.

### 02 — Triage of all 1,766 detections (`02-triage/`)

Thresholds fixed from exp 01 before the run: location disk 350 km; earthquake rule ComCat
M ≥ 4 within ±600 s and 1,000 km.

| Class | Count |
|---|---|
| Greenland or Arctic Canada in the disk | 1,035 |
| Open ocean (no land in the disk) | 413 |
| Antarctic | 215 |
| Land | 103 |
| — of land: ESEC-known landslide | 16 |
| — of land: catalogued earthquake coincident | 6 (18 over all classes; chance rate 2.8) |
| **— of land: residual** | **81** (55 in the Sentinel-2 era, from July 2015) |

- At least 16 of 103 land detections are already-attributed landslides. ESEC is incomplete,
  so this is a floor on the landslide share of the residual.
- No known landslide has more than 4 other detections within 150 km. No residual detection has
  more than 8. The repeat count does not separate classes at this size.
- Full table: `02-triage/triage.tsv`. The residual is the rows with `region=land`, empty
  `eq_id` and empty `esec_known`.

### 03 — Reference sweep of the residual (`03-reference-sweep/`)

**03a, bulletin and eruptions (`sweep.py`).** ISC bulletin, any magnitude, ±600 s and 9°: 26 of
81 detections have an event (7.5 expected from day-shifted windows); 5 are M ≥ 4. GVP eruption
onset within ±30 days and 350 km: 4, all the Mayotte (Fani Maore) cluster. Offshore (grid point
and a 120 km ring all sea on the 1:110m mask): 31.

**03b, timed bulletin events (`timed.py`).** Rule fixed from exp 01: an ISC origin 30–180 s
before the Poli time. **17 detections have one; 2.0 expected by chance.** For those 17 the
bulletin epicentre replaces Poli's grid point (`timed.tsv`).
- Nine are at sea or on the coast: Gulf of California (7, 792, 1286), the Panama fracture zone
  (209, 1084, 1118), Rivera (1500), Chile Rise (1188), off Vancouver Island (750). Bulletin
  magnitudes 3.4–4.9.
- Iceland: 178 (Krýsuvík, MS 3.6) and 315 (64.07° N 21.40° W, ML 3.9). Afar: 1592 (ML 3.7).
  Botswana: 781 (ML 2.0). Kamchatka offshore: 385 (no magnitude).
- **Three in the BC and Yukon ranges have ML 2.0–2.9 against Mw_d 4.7–4.8:**
  77 (9 Jul 2010 18:47:21, 51.697° N 126.539° W, ML 2.9; 11 h after the Sheemahant Glacier
  landslide), 1712 (16 Oct 2022 20:18:44, 60.076° N 137.475° W, ML 2.4), 1735 (9 Dec 2022
  15:03:39, 54.299° N 129.002° W, ML 2.0). A long-period size far above the short-period
  magnitude is what a landslide gives, and also what other slow sources give. Untested.

**03c, literature (`lit/`, five Opus agents, 50 on-land detections).** 42 nothing found;
5 reported landslide; 2 volcanic; 1 earthquake. Verdict table: `lit/summary.tsv`; evidence and
searches: `lit/batch-N.md`. Each batch file has its own Unverified claims.
- **29, Peru, 20 Feb 2010 18:03 UTC, Mw_d 5.17.** Rodeopampa landslide and Sócota river dam,
  Cajamarca, about 99 km from the grid point (IGP/INGEMMET technical report, see
  `lit/batch-2.md`). The report gives 20 Feb in its conclusions and witness annex and 22 Feb
  in a header; a congress abstract says 22 Feb. Reported time "about 12:40" local; the
  detection is 13:03 local. Not in ESEC. No published link to a global seismic detection found.
- **807, 808, 809, Myanmar, 31 Jul – 1 Aug 2015.** Ekström and Stark reported three signals.
  Figure filenames in Petley's 29 Oct 2015 post read as two of their times: 31 Jul 15:47 and
  1 Aug 02:28 UTC (agent's inference). Poli 809 is at 02:28:29, the same minute. Poli has no
  detection at 15:47; Poli 807 (11:28) and 808 (17:05, Mw_d 5.14) are not in those two. The
  Tonzang landslide (about 395 Mt) has no published time that the agents found.
- **1609, Ecuador, 2 Dec 2021.** Sangay explosion at 09:02 UTC, 2–3 min before the detection
  (Hidalgo et al. 2022, *Volcanica*). The same paper reports an untimed 6.6 km² flank landslide
  between 29 Nov and 2 Dec.
- **1219, Vanuatu, 15 Dec 2018.** Inside the Ambrym dike intrusion (Shreve et al. 2019).
- 178 is the Krýsuvík event that 03b also finds. 315's reported debris slide is one day off and
  small; 03b's ML 3.9 event 49 s earlier is the better match.

### 04 — Imagery (`04-imagery-calibration/`, `uv` environment)

**04a, detector v1 on known scars (`s2.py`, `calib.py`).** Earth Search's Sentinel-2 L2A
archive starts in 2017, so the positives are 28 ESEC events from July 2017 with ≥ 10⁶ m³; 27
had imagery. Result (`result.txt`, `calib.tsv`):
- Blobs per event tile: median 1,314. Blobs per no-event control tile (same windows one year
  earlier): median 1,308. The detector fires as often when nothing happened.
- A blob lay within 5 km of 26 of 27 scars, but **that hit rate carries no information**: at
  1,300 blobs per 110 km tile, about 8 blobs fall inside any 5 km circle by chance.
- Rank of the nearest blob in its tile: 1st once (Matai'an), top 5 three times, top 20 seven
  times of 27.
- **Detector v1 fails.** It cannot search a 350 km disk, and it does not reliably single out
  a scar even inside one tile. Causes not separated: snowline and illumination change between
  windows, cloud-mask leakage, 80 m pixels against scars of 6–700 pixels.

**04b, chips at bulletin locations (`chip.py`, `chips/`).** Summer 2022 against summer 2023 at
the 03b epicentres for 1712 (24 km and 90 km squares) and 1735 (30 km square). Read by eye
(Fable, main thread): no fresh scar or deposit seen in any of the three. This is weak: 90 m
pixels in the wide chip, cloud over part of the 2022 scene, and the bulletin epicentres of
ML 2 events in these ranges may be tens of km off.

### 05 — Regional relocation (`05-regional-relocation/`, `uv` environment)

Back-projection of 1–5 Hz envelopes at BHZ/HHZ stations within 5° (EarthScope FDSN), 0.1° grid,
3.3 km/s. Method v1 is stated in `locate.py` and was not changed after the first calibration run.

**05a, calibration (`calib.py`).** 53 ESEC events 2010–2025 with ≥ 10⁶ m³; each search centred
139–190 km from the true location. 41 had ≥ 5 usable stations. **Median error 17 km; 26 within
25 km; 33 within 50 km; 7 gross misses (109–585 km).** No quality score in the output separates
the misses, so about one location in six is badly wrong without warning. Twelve events had too
few open stations (Tibet, Sikkim, Pakistan, Indonesia, Turkey, Iceland, New Zealand, Chile,
parts of Greenland).

**05b, the residual (`target.py`, `target.tsv`).** 24 of 81 detections located. Cross-check
against the independent ISC epicentres of exp 03b for the three low-ML detections: 25 km (1712),
45 km (1735), 67 km (77). For the two Iceland earthquakes the two locations disagree by
138–176 km; the method assumes one slow emergent source and is not calibrated on earthquakes.

### Candidate A — Poli 1683, 29 Jul 2022 02:33 UTC (reported here, not established)

- **Seismic:** Poli grid 61.5° N 144.0° W, Mw_d 4.69. Exp 05b: 60.50° N 143.37° W from 49
  stations, nearest 9 km, 116 km from Poli's grid point. No ISC event, no ComCat M ≥ 4, no
  eruption (exp 02, 03a).
- **Imagery (`04-imagery-calibration/chips/poli1683-*.png`), read by eye on the main thread:**
  a small valley glacier about 6 km from the 05b location, near 60.52–60.55° N 143.28° W, is
  snow-white on 4 Jul 2022 (S2B_6VXN_20220704) and carries a uniform grey tongue roughly 1 km
  by 3 km on 3 Aug 2022 (S2B_6VXN_20220803). The same glacier is clean crevassed ice on 21 Aug
  and 7 Sep 2021 and is grey, debris-covered, down its length on 23 Aug 2023.
- **What this meets from "What a solution would have to do":** a before/after pair bracketing
  the origin time (25 days before, 5 days after); two control dates before and one after.
- **What it does not meet yet:** the area and volume are not measured. `measure.py` could not
  isolate the tongue: its seasonal filter used the Sep 2021 scene, where the glacier is mixed
  ice and rock, and the result fragmented. No check for a second scar inside the error disk.
  No force-history direction. The image reading is one reader's.
- **Novelty:** not in ESEC v4. The literature agent found nothing for this date; one extended
  search for a July 2022 rock avalanche at Mount Steller, the Bagley Icefield, Bering Glacier or
  Waxell Ridge found nothing, and the Alaska Earthquake Center's July 2022 monthly report lists
  icequakes but no landslide (SECONDARY, https://earthquake.alaska.edu/earthquakes/reports/monthly/july-2022).
  The Alaska group detects landslides in near real time, so "unreported" is unlikely to mean
  "unknown to them". Unverified: the place name; Mount Steller's coordinates were recalled, not sourced.

Other 05b chips read by eye with no change seen: 1433 (Prince William Sound, the tile edge cuts
the north half), 1712 and 1735 at their ISC epicentres. 1109 (Alaska Range) was made and not read.

## Leads (not findings)

These are readings of `triage.tsv` by eye plus two web searches. None has been tested.

1. **Chin State, Myanmar, 31 Jul – 1 Aug 2015** (ids 807, 808, 809; 808 has Mw_d 5.14).
   Ekström and Stark reported three large seismic landslide signals there after Cyclone Komen,
   one of 395 Mt (NASA Earth Observatory, SECONDARY,
   https://earthobservatory.nasa.gov/images/86924/satellite-spots-massive-tonzang-landslide).
   Petley later wrote that the seismic events "do not appear to correspond" to the mapped
   Tonzang slide (POPULAR, https://blogs.agu.org/landslideblog/2015/11/09/tonzang-landslide/).
   Whether that mismatch was ever resolved is not known. Sentinel-2A began acquiring in late June 2015;
   Landsat 8 covers the dates.
2. **Eastern Himalayan syntaxis, 15 Jun, 3 Jul and 13 Jul 2018** (ids 1144, 1155, 1161), near
   28–28.5° N, 94.5–95.5° E. The published Sedongpu collapses on the Yarlung Tsangpo are dated
   16–17 and 29 October 2018 (An et al. 2022; Zhao et al. 2022, SCHOLARLY,
   https://tc.copernicus.org/articles/16/1333/2022/tc-16-1333-2022.pdf), 170 km north. One
   search found no published June or July 2018 event. A JpGU 2020 talk on seismic recordings
   of ice collapses along the canyon was not read.
3. **Southern Patagonia, 6 Feb 2018** (id 1106; Mw_d 5.33, the largest in the residual),
   50.5° S, 72.5° W. Not searched.
4. **Second detections on the day of a known landslide:** id 103 (Karakoram, 12 Sep 2010,
   9 h before the Siachen Glacier event) and id 77 (BC Coast Mountains, 9 Jul 2010, 11 h after
   Sheemahant Glacier). Not searched.
5. **Known non-landslide clusters inside the residual**, to be removed by a rule, not by eye:
   offshore Mayotte 2018 (four detections), Vanuatu 15 Dec 2018 (two), a repeating source
   offshore Chile near 45.5° S 78° W (eight), a repeating source off Cape Hatteras (nine).
   The identifications of Mayotte and Vanuatu are from memory and are unverified.

## Open points

- The Zenodo record says only "long period earthquakes recorded between 2010 and end of 2022".
  Whether its 1,766 rows are exactly the paper's ">1,700 previously unidentified sources" has
  not been confirmed against the paper (GeoScienceWorld returns 403 to scripts).
- The land mask is 1:110m and classes are assigned from a 37-point sample of the disk.
  "Land" means land somewhere within 350 km, so offshore sources are in the residual.
- ComCat only. ISC is more complete below M 4.5 and has not been used.
- No volcano rule yet (Smithsonian GVP eruption dates).

## Next

1. **Candidate A.** Measure the deposit with a mask built from the 2021 and 2023 scenes; sweep
   the rest of the 50 km error disk for a second scar; ask the Alaska Earthquake Center or USGS
   landslide group whether the 29 Jul 2022 event is in their list. Greg sends any email.
2. **The other located Alaska and Canada detections** (782, 906, 997, 1109, 1433, 1712, 1713,
   77, 1160, 1735): chips at the 05b locations, 60 km squares, with the four-date rule.
   2016 and early-2017 events need Landsat (Planetary Computer) for the before image.
3. **Peru 29.** Landsat before/after at Rodeopampa; read the IGP/INGEMMET report in full.
4. **Myanmar 807/808.** Ekström's origin time for Tonzang.
5. **Patagonia 1106 and 1551** located with 5–6 stations (weak). Chilean and Argentine
   networks through other FDSN centres may add stations.

## How to run

```
python3 01-poli-x-esec/crossmatch.py
python3 02-triage/fetch.py      # ComCat and Natural Earth, about a minute
python3 02-triage/triage.py
python3 03-reference-sweep/sweep.py    # ISC, about 40 minutes uncached
python3 03-reference-sweep/timed.py
(cd 04-imagery-calibration && uv run python calib.py)
(cd 05-regional-relocation && uv run python calib.py && uv run python target.py)
```

Python 3.11+. Experiments 01–03 use the standard library only; 04 uses the `uv` environment in its folder.
