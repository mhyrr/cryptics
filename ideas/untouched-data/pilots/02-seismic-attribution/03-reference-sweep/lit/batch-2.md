# Reference sweep — batch 2 (10 detections)

Input: `batch-2-input.tsv`. Method: WebSearch, then WebFetch or PDF text extraction (`pdftotext`) on the best hit. I did not use the AGU Landslide Blog post pages: they returned "under construction" on 2026-11-10. The blog's `wp-json` endpoint did work.
Distances are great-circle distances from the grid point, using the coordinates noted in each entry. Time-zone conversions are noted where used.

---

### 29 — 2010-02-20T18:03:29Z — -7.0, -78.0 — Peru (Cajamarca)
- **Verdict:** REPORTED-LANDSLIDE
- **Event:** Rodeopampa (Cerro Calabozo-Rodeopampa) landslide and the Sócota river landslide dam, districts of Anguía (Chota) / San Luis de Lucma (Cutervo), Cajamarca. The joint IGP/INGEMMET technical report gives UTM 764,869 E / 9,298,456 N, elev. 2630 m. That converts (zone 17S, WGS84 assumed) to about -6.341, -78.606. **Saturday 20 February 2010, ~12:40 local time (PET = UTC-5) → ~17:40 UTC.** One witness says "más o menos la una de la tarde" (about one in the afternoon), which is ~18:00 UTC. The report describes it as a reactivated rotational slide. Crown at 2300 m, toe at 1200 m, height ~1000 m. Width 300 m at the top and 1000 m at the bottom. Run-up 100 m on the opposite bank. Dammed lake 1640 m long, 70–90 m high, impounding ~25 million m³. One person missing, two houses buried, 72 families affected.
- **Distance from grid point:** ~99 km
- **Already linked to a seismic detection by someone?** Partly. The report says the main mass movement registered as a magnitude 3.5 event at the IGP Cajamarca station: "registró en una de las estaciones sísmicas un movimiento sísmico de magnitud 3.5 en la escala de Ritcher en la estación Cajamarca de la Red Sísmica del IGP" ("recorded at one of the seismic stations a seismic movement of magnitude 3.5 on the Richter scale, at the Cajamarca station of the IGP seismic network"). No one has linked it to a long-period global detection, as far as I found.
- **Sources:**
  - https://sigrid.cenepred.gob.pe/sigridv3/documento/710/descargar (PRIMARY: IGP/INGEMMET technical report, Gómez, Zavala & Herrera 2010, "Deslizamiento del cerro Rodeopampa y embalse del río Sócota"). Conclusions: "El evento geológico ocurrido el sábado 20 de febrero de 2010 a las 12:40 horas aproximadamente, corresponde a un deslizamiento de tierras tipo rotacional" ("The geological event of Saturday 20 February 2010, at about 12:40, was a rotational earth slide"). Annex 3, the residents' testimony, also dates the main event to "20 de febrero del 2010 durante la tarde" ("20 February 2010, in the afternoon"). It records precursor slides on 13 and 17 Feb. It gives the UTM coordinates and the M3.5 IGP station note. Confusingly, the report's own section header says "Evento geológico del 22 de febrero".
  - https://app.ingemmet.gob.pe/biblioteca/pdf/CPG15-252.pdf (SCHOLARLY: Zavala, Gómez & Lu, XV Congreso Peruano de Geología 2010, extended abstract). Dates the slide to **22 February 2010** throughout and gives the same dimensions and the 25 Mm³ impoundment.
  - https://www.lacapital.com.ar/edicion-impresa/parte-un-cerro-cayoacute-peruacute-n771518.html (POPULAR: press, 22 Feb 2010). "Parte de un cerro cayó en Perú" ("Part of a hill fell in Peru"). Not fetched; the search-engine summary says it reports a hill collapse in Cajamarca.
- **Searches run:** "landslide Peru 20 February 2010 Amazonas Cajamarca huaico"; "deslizamiento Rodeopampa Socota febrero 2010 Cutervo fecha"; "\"20 de febrero de 2010\" deslizamiento OR huaico Cajamarca OR Amazonas OR \"La Libertad\" OR \"San Martín\""
- **Notes / near-misses:** The sources disagree on the date. The primary technical report's conclusions and testimony annex say 20 Feb ~12:40 local. Its section header and the later congress abstract say 22 Feb. The 22 Feb date may be the report date or a typo that propagated; this is not resolved. The 12:40 local time (17:40 UTC) is ~23 min before the detection, not the expected 1–3 min. "Aproximadamente" (approximately) and the witness's "about one o'clock" (~18:00 UTC) leave room. A volume for the slide itself is not stated. The ~25 Mm³ figure is the impounded lake, not the slide mass.

### 315 — 2011-10-15T09:46:48Z — 63.5, -19.5 — Iceland
- **Verdict:** REPORTED-LANDSLIDE (weak: one day off, and probably too small)
- **Event:** Torfufell debris slide, Eyjafjörður / Eyjafjarðarsveit, north Iceland. Fell on **14 October 2011**; no time given. Started on a 200 m fissure at ~800 m a.s.l., NW-facing slope, with frozen sediment blocks. Volume 700,000–1,000,000 m³ (Landslide Blog, citing Icelandic reports).
- **Distance from grid point:** ~215–220 km. The coordinates for Torfufell, ~65.38 N, 18.25 W, are my estimate and were not taken from a source.
- **Already linked to a seismic detection by someone?** No. Petley asked whether the Icelandic network recorded it; I found no answer.
- **Sources:**
  - https://opac.geologie.ac.at/ais312/dokumente/EGU/EGU2014-12930.pdf (SCHOLARLY: Sæmundsson, Helgason & Pétursson, EGU2014-12930 abstract). "The Torfufell debris slide fell on the 14th of October 2011, after exceptionally warm summer and unusually rainy fall."
  - https://blogs.agu.org/landslideblog/wp-json/wp/v2/posts/3793 (POPULAR: Petley, AGU Landslide Blog, 20 Oct 2011). "On Friday" a landslide of 700,000–1 million m³ occurred at Eyjafjarðarsveit. It appears to have dammed the valley. No time given; no seismic record mentioned.
- **Searches run:** "Mýrdalsjökull Katla 15 October 2011 earthquake"; "Iceland landslide OR rockfall OR jökulhlaup October 2011 skriða"
- **Notes / near-misses:** The detection is at 09:46 UTC on the 15th. The slide is dated 14 Oct, so it falls just outside the same UTC day but within ±1 day. Iceland uses UTC. A volume of ≤1 Mm³ is well under the ~5–10 Mm³ the detection's magnitude implies. Separately, Katla (Mýrdalsjökull, ~63.63 N, 19.1 W, ~25 km from the grid point) was in seismic unrest in Oct 2011. One blog (POPULAR, low reliability) mentions a "14–15 Oct" Katla swarm. The IMO says the largest earthquake of the 5 Oct swarm was ML ~3.7 (https://en.vedur.is/about-imo/news/nr/2360, not fetched). I did not confirm a specific Katla event on 15 Oct near 09:46 UTC.

### 672 — 2014-08-05T20:46:06Z — 78.5, -90.5 — Canada (Axel Heiberg / Ellesmere, Nunavut)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report an event on this date.
- **Searches run:** "August 2014 Ellesmere Island landslide OR glacier OR ice shelf collapse"; "landslide seismic detection Ekström 2014 Ellesmere OR \"Axel Heiberg\" OR \"Nunavut\" August 2014"; "\"August 2014\" Axel Heiberg OR Eureka OR \"Ellesmere\" glacier calving OR landslide OR rockfall OR \"ice island\" event"
- **Notes / near-misses:** Milne Ice Shelf collapse, Ellesmere, 30–31 July **2020**: wrong year. Ayles Ice Shelf calving, 13 Aug **2005**: wrong year. Nothing for Aug 2014. A remote, sparsely reported region; glacier calving or an iceberg capsize would likely go unreported.

### 807 — 2015-07-31T11:28:38Z — 22.0, 93.5 — Myanmar (Chin State)
- **Verdict:** REPORTED-LANDSLIDE (generic: landslides reported on the date, but no single dated and timed event)
- **Event:** Hakha landslides, Chin State, during the Cyclone Komen rains. Nine landslides were recorded between 28 and 31 July 2015, damaging 732 houses. The main one was a rotational slide at Rhung Taung (Rung Tlang) hill. Slide length averaged ~500 m. The Hakha study area is 22°30'–22°45' N, 93°30'–93°45' E. No clock time or volume found for any individual slide.
- **Distance from grid point:** ~60–85 km (Hakha town ~73 km)
- **Already linked to a seismic detection by someone?** no / unknown
- **Sources:**
  - https://universepg.com/public/img/storage/journal-pdf/Rainfall%20and%20landslide%20susceptibility%20in%20Hakha%20environ.pdf (SCHOLARLY, low-tier journal: May Thu Naing et al. 2022, Br. J. Arts & Humanities). "During the period 28-31 July 2015, 9 landslides were recorded, 732 houses caused property damage". The cyclone brought heavy rain on 30–31 July. The Rhung Taung slide was "triggered … under the continuous rain of 21st–30th July 2015".
  - https://www.chinlandguardian.com/?p=4551 (POPULAR: Chinland Guardian, 31 July 2015). Ongoing landslides and floods in Hakha; ~1,000 families evacuated; ~700 buildings evacuated. No times or sizes given.
  - https://www.fujipress.jp/jdr/dr/dsstr001300010099/ (SCHOLARLY: J. Disaster Research 13(1), 2018). Not fetched; the search snippet calls it the most devastating landslide on record in Myanmar, July 2015.
- **Searches run:** "Hakha landslide Chin State July 2015 date"; "Hakha landslide \"31 July 2015\" OR \"July 31\" Rung Tlang large landslide time"
- **Notes / near-misses:** The Hakha landslides were rainfall-driven and largely progressive (rotational). Nothing found gives a catastrophic single failure at ~11:25 UTC (~17:55 local, MMT = UTC+6:30). The same cyclone caused landslides across Chin State, Manipur and Bangladesh, all within the 350 km disk. Petley's posts on Hakha and Tonzang (blogs.agu.org/landslideblog/2015/09/27/tonzang-1/) could not be fetched; the site was under construction.

### 990 — 2017-02-19T14:51:37Z — 26.0, -83.0 — Gulf of Mexico (W of Florida)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report an event on this date.
- **Searches run:** "February 19 2017 Gulf of Mexico seismic event offshore Florida"; "\"19 February 2017\" OR \"February 19, 2017\" Gulf of Mexico explosion OR earthquake OR \"submarine landslide\" OR boom Florida Cuba"
- **Notes / near-misses:** The American Meteor Society logged fireball reports on 18 Feb 2017 at ~21:14 local, about 02:14 UTC on 19 Feb (https://amsmeteors.org/members/imo_view/report/108382 and /108301). The location was not seen, and the time is ~12.5 h off. Not a match. Gulf earthquakes of 10 Sep 2006 and Feb 2024 (Atlantic side): wrong years.

### 1106 — 2018-02-06T20:06:21Z — -50.5, -72.5 — Argentina/Chile (Southern Patagonian Icefield, Lago Argentino)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report an event on this date.
- **Searches run:** "Perito Moreno OR Upsala OR \"Southern Patagonian Icefield\" February 2018 calving landslide event"; "\"February 2018\" glacier OR landslide OR GLOF Patagonia Chile Aysén OR \"Lago Argentino\" OR \"El Chaltén\" OR \"Torres del Paine\""; "\"6 February 2018\" OR \"February 6, 2018\" Patagonia glacier OR landslide …"; "febrero 2018 desprendimiento glaciar OR derrumbe OR aluvión \"Lago Argentino\" OR \"El Calafate\" OR \"Última Esperanza\" OR \"Lago Viedma\"" (February 2018 glacier calving OR collapse OR mudflow …)
- **Notes / near-misses:**
  - Perito Moreno ice-bridge rupture, 11–12 **March** 2018, ~50 km from the grid point. Five weeks off (https://www.thejakartapost.com/life/2018/03/13/ice-bridge-in-argentine-glacier-collapses-no-witnesses, POPULAR).
  - Upsala Channel (Agassiz) landslide and tsunami, 10 Feb **2013**: wrong year.
  - Villa Santa Lucía debris flow, 16 Dec 2017: ~800 km north and seven weeks off.
  - This is one of the largest detections in the batch (Mw_d 5.33) with no report found. Big calving or iceberg-capsize events at Upsala, Viedma, or the Pío XI / Chilean tidewater glaciers would go unreported.

### 1161 — 2018-07-13T15:02:59Z — 28.5, 94.5 — China (SE Tibet, Nyingchi) / India (Arunachal)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report an event on this date.
- **Searches run:** "Sedongpu glacier collapse July 2018 Yarlung Tsangpo"; "Nyingchi OR Medog OR Arunachal landslide 13 July 2018"; "2018年7月13日 西藏 林芝 OR 墨脱 OR 米林 滑坡 OR 泥石流 OR 冰崩" (13 July 2018, Tibet, Nyingchi OR Medog OR Mainling, landslide OR debris flow OR ice avalanche); "Arunachal Pradesh landslide July 13 2018 OR \"13 July 2018\" Siang OR Dibang OR Lohit OR Tawang"
- **Notes / near-misses:**
  - Sedongpu ice-rock avalanches, 16/17 Oct and 29 Oct 2018 (~130 Mm³), ~80 km from the grid point (29.8 N, 94.9 E approx.). Three months off (https://tc.copernicus.org/articles/17/2533/2023/, SCHOLARLY).
  - Debris flow on G318 between Lulang and Tongmai, 21 July 2018 (https://society.huanqiu.com/article/3z96r64mi7h, POPULAR; per search summary, not fetched). Eight days off.
  - A Tawang labour-camp landslide reported "on Friday" (13 July 2018 was a Friday): article year not shown, unverified (see Unverified claims).
  - Sedongpu had repeated smaller failures before Oct 2018 per the later literature, but I found no dated July 2018 event.

### 1433 — 2020-08-06T08:59:10Z — 61.5, -147.0 — USA (Alaska, Chugach / Prince William Sound)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:**
  - https://www.pwsrcac.org/wp-content/uploads/filebase/board_meetings/2021-01/4-09-Presentation-on-Barry-Arm-Landslide-and-Tsunami-Risks.pdf (SECONDARY: PWSRCAC board briefing, Jan 2021). "During the summer of 2020, there were three massive alpine landslides detected in the Sound – something that is historically unusual." No dates, names or locations given. This is the closest lead.
  - https://earthquake.alaska.edu/new-detection-method-aims-warn-landslide-tsunamis (SECONDARY: Alaska Earthquake Center). Karasözen & West (The Seismic Record, 2024) found three Barry Arm landslides in 2020–2021 by retrospective seismic analysis. No dates given on the page. Barry Arm is ~75 km from the grid point.
- **Searches run:** "Alaska landslide August 6 2020 seismic detected Chugach"; "Prince William Sound OR Copper River OR Valdez landslide OR \"rock avalanche\" August 2020"; "2020 Prince William Sound alpine landslides glacier seismic detected …"; "Petley landslide blog August 2020 Alaska rock avalanche glacier Chugach"; "\"August 6, 2020\" OR \"6 August 2020\" Alaska landslide …"; "Karasözen West Barry Arm landslides 2020 2021 seismic detection dates"
- **Notes / near-misses:** The "three massive alpine landslides in summer 2020" in Prince William Sound are a live lead with no dates. The Karasözen & West 2024 supplement, or the Alaska DGGS / USGS Barry Arm reports, may date them. Lituya Glacier outburst flood, 15 Aug 2020: ~550 km away and nine days off.

### 1584 — 2021-10-15T15:01:23Z — 27.0, 89.5 — Bhutan / Sikkim / Tibet
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report a matching event.
- **Searches run:** "Bhutan landslide OR glacial lake outburst October 15 2021"; "Bhutan OR Sikkim OR Tibet landslide \"October 2021\" Yadong OR Haa OR Paro OR Thimphu large landslide"; "2021年10月15日 西藏 亚东 OR 山南 OR 日喀则 滑坡 OR 冰崩 OR 地震" (15 Oct 2021, Tibet, Yadong OR Shannan OR Shigatse, landslide OR ice avalanche OR earthquake); "Bhutan landslide \"15 October 2021\" OR \"October 15, 2021\" OR \"16 October 2021\" Kuensel"
- **Notes / near-misses:**
  - EMSC M4.2, "Western Xizang", 2021-10-15 10:35:41 UTC, at 29.50 N, 87.76 E (https://www.emsc-csem.org/Earthquake/earthquake.php?id=1048591, PRIMARY catalogue; per search summary, not fetched). ~320 km away and **4.4 h before** the detection. Not a match on time.
  - "Massive landslide" at Namling, Bumthang–Monggar highway, Bhutan (~150 km E). The BBS article (https://www.bbs.bt/atleast-three-more-days-to-clear-the-block-at-namling-along-bumthang-monggar, POPULAR) says the road had been closed "since Wednesday evening". It shows no publication date; its image path is /2021/10/. If it is from Oct 2021, "Wednesday" is probably 13 Oct, two days off. Not a match as it stands.
  - A low-pressure system brought severe rain and landslides to the region from ~5 Oct 2021 (search summary only).

### 1683 — 2022-07-29T02:33:08Z — 61.5, -144.0 — USA (Alaska, Chugach / Wrangell–St. Elias, Copper River)
- **Verdict:** NOTHING-FOUND
- **Event:** —
- **Distance from grid point:** —
- **Already linked to a seismic detection by someone?** unknown
- **Sources:** none that report an event on this date.
- **Searches run:** "\"July 29, 2022\" OR \"July 28, 2022\" landslide OR \"rock avalanche\" Alaska Wrangell OR Chugach OR glacier"; "\"July 29, 2022\" OR \"29 July 2022\" Alaska landslide OR \"glacier\" OR \"rock avalanche\" OR \"outburst\" Copper River OR McCarthy OR Valdez OR Cordova"
- **Notes / near-misses:**
  - Klutlan Glacier tributary paraglacial landslide (Wrangell–St. Elias, Yukon side) "began developing in July 2022", with no day given (https://blogs.agu.org/landslideblog/2023/03/23/klutlan-glacier-1/, POPULAR; search summary, not fetched). Klutlan is ~61.5 N, 140.5 W per my recollection, unverified, so roughly 190 km away. This is a slow, developing slide with no date; not a match. Worth a follow-up with imagery.
  - Hidden Creek Lake outburst, Kennicott Glacier, 13–14 July 2022: ~100 km and two weeks off.
  - Barry Arm: the DGGS statement (2022-08-05) reports deceleration between 3 and 27 July 2022; no failure.
  - Warning: a search summary attributed a "July 25" Wrangell–St. Elias landslide to 2022. The Columbia article (https://news.climate.columbia.edu/?p=39232) is dated Sept 2013, so that landslide is the 25 July **2013** event. Not a near-miss for 2022.

---

## Unverified claims

- **Rodeopampa date conflict (29):** the primary report says 20 Feb 2010 ~12:40 local in its conclusions and testimony annex. Its section header and the 2010 congress abstract say 22 Feb. I could not find an independent dated news report (INDECI or Peruvian press for 20–21 Feb) to settle it. The lacapital.com.ar piece is headed 22 Feb 2010, but I did not read it.
- **Rodeopampa M3.5 IGP station recording:** stated in the report's footnote 4; I did not see the waveform or the IGP catalogue entry.
- **Torfufell coordinates (~65.38 N, 18.25 W):** from my own recollection, not a source; the distance (~217 km) depends on them.
- **Katla swarm "14–15 Oct 2011":** seen only in a low-reliability blog snippet; not confirmed with IMO data.
- **Tawang labour-camp landslide "on Friday" (possible 13 July 2018):** the snippet (thequint.com) shows no year. My recollection is that the deadly Tawang labour-camp landslide was in April 2016, which would make it irrelevant; not verified.
- **Namling (Bhutan) landslide date:** the October 2021 date is inferred from the image path only.
- **EMSC M4.2 Western Xizang, 2021-10-15 10:35 UTC:** from the search summary of the EMSC page; I did not fetch the page.
- **Klutlan Glacier location:** from recollection.
- **Sedongpu coordinates (~29.8 N, 94.9 E):** approximate, from recollection.
