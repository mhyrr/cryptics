# 17 — Distal tephra sweep, 1440–1470 CE

**Question.** Is there a published distal tephra or cryptotephra in the Northern
Hemisphere, dated to about 1440–1470 CE, that is unsourced or only tentatively
sourced? Is there one already sourced to a named candidate (Aniakchak Half
Cone, Shiveluch, Kamchatka/Kuril calderas, Grímsvötn, Katla, Hekla)? And do
well-dated records that should have caught a candidate's ash show nothing in
that window (an informative absence)? This is consequence test 5 ("distal
glass") in PLAN.md and the second half of experiment 07.

**Short answer.** No layer was found that is both well dated to 1440–1470 and
unexplained. Three leads deserve a glass comparison in 07; none is decisive.

1. **Ahklun "0.4-ka tephra", SW Alaska, 353 km from Aniakchak (H10).** Kaufman
   et al. 2012. It is bimodal (andesite plus rhyodacite), and its glass is
   indistinguishable from Aniakchak CFE II (screen SC6 0.98 for both modes).
   Two dates disagree:
   - The soil-pit maximum age (wood and leaves below the tephra) is 1435–1468
     CE, so 1453 is allowed.
   - The Lone Spruce Pond age model gives 1511–1635 CE, which excludes 1453.

   The rhyodacite mode, 71.3 wt% SiO₂, lies outside the published Half Cone
   Pink Pumice glass range (68.3–69.8). As far as the screen can tell, it is
   not Pink Pumice.
2. **Loch Portain B, Scotland (H5, H6).** An unassigned rhyolitic
   cryptotephra at the same depth as Hekla 1510. Peat directly below it dates
   to 1304–1447 CE, and peat inside the interval to 1428–1660. Its glass
   (74–77 wt% SiO₂, K₂O 3–5) matches none of the North Pacific or Cascade
   references in hand (SC6 ≤ 0.89). It is the only well-placed unsourced
   layer in Europe.
3. **Kenai Peninsula microtephras and MP 39 (H10, H6).** Payne & Blackford
   2008. The layers date to about 1360–1520 CE by extrapolation from a single
   bulk-peat date. MP 39 is andesite, and the screen cannot separate Crater
   Peak from Aniakchak andesite.

A sourced hit outside the candidate list: **MOR-T2** at An Loch Mór, Ireland.
It is trachyte, and Ramalho et al. (EGU 2023) correlate it to **Furnas I,
Azores, 1439–43 CE**. A VEI-4 NH-extratropical Atlantic eruption therefore
reached Ireland about ten years before 1453.

Absences that carry information:
- An Loch Mór has nothing between MOR-T2 (1439–43) and MOR-T1 (V1477,
  tentative).
- Garry Bog (N. Ireland) has nothing between Öræfajökull 1362 and Hekla 1510.
- Tephrabase lists **no occurrence outside Iceland** for Grímsvötn 1432 or
  1457. Veiðivötn 1477 has 2 and Hekla 1510 has 13.
- On Simushir, soil directly below Zav-1 (1831) dates to 1258–1426 cal CE.
- The South Kurils show no local tephra between 1420 cal BP and 1973.
- 42 Pacific-coast sites in western Hokkaido have no visible tephra between
  B-Tm (946) and Ko-d (1640).

On the Grímsvötn dating basis (a NEXT.md item), Tephrabase dates Grímsvötn
1457 ± 5 by sediment-accumulation rate in 141 south-Iceland soil sections
(Streeter & Dugmore 2014). That is not an ice date. Whether it is the same
event as GVP's ice-core-labelled rows is unverified.

## Run

```
python3 -I fetch17.py                      # re-download into data/ (gitignored); appends sha256 to results/fetch_sha256.txt
python3 -I calib17.py ../06-candidate-ranking/data/intcal20.14c > results/calib17.txt
python3 -I glass17.py > results/glass17.txt
python3 -I kushu17.py data/kushu_supp.xlsx > results/kushu_layers.txt
python3 -I tb_sites.py data/tb_eu_tephra*.html > results/tb_distal_sites.txt
python3 -I tb_profile.py data/tb_site*.html > results/tb_profiles.txt
python3 -I hits17.py ../06-candidate-ranking/data/gvp_holocene_volcanoes.csv > results/hits.tsv
```

All of these are standard library only. `calib17.py` imports 06's IntCal20
code unchanged. Four PDFs came through WebFetch, because the host serves a bot
challenge to urllib. They are in `data/` with these sha256 values:

| File | sha256 |
|---|---|
| hutchison2025_si.pdf | 18df8b58…5218 |
| jpgu2013_svc53p18.pdf | 5e2faa1d…3e03 |
| bousai_siryou4.pdf | 5889adc0…c124 |

The Kaufman 2012 and Browne 2022 texts used here are 11's copies, in
`../11-aniakchak-date/data/`.

## Method: what was searched (for judging coverage)

**Databases queried directly (raw responses saved in `data/`):**
- Tephrabase calendar-date search, tephra layers and eruptions, 1400–1520 CE.
  It returns Katla 1416, Grímsvötn 1432, Grímsvötn 1457, Katla 1440 (eruption
  only), Veiðivötn 1477, Torfajökull 1477 (eruption only), Katla 1500 and
  Hekla 1510.
- Tephrabase radiocarbon-dated tephra search, 250–700 ¹⁴C BP. It returns one
  layer: Loch Portain B.
- Tephrabase all-Europe distribution pages for 27 layers: every local or
  unsourced name in the layer list (BMR-90, GB4-50, QUB-570/571, MOR-T4,
  PMG-5, SLU-5, SN-1, Penifiler, Breakish, Kebister, L3574, DOM-*, JAM-*,
  Layer K/L), plus Grímsvötn 1432/1457, V1477 and Hekla 1510. Results are in
  `results/tb_distal_sites.txt`.
- Tephrabase site profiles for every distal site that holds V1477, Hekla 1510
  or an unsourced late-Holocene layer (17 sites). Results are in
  `results/tb_profiles.txt`.
- OpenAlex, used only to find open copies. Mendeley Data (Lake Kushu glass,
  Chen et al. 2019).

**Papers read in full or in the relevant part:**

| Source | What was read | Tier | Access |
|---|---|---|---|
| Mackay et al. 2016, QSR 132, https://doi.org/10.1016/j.quascirev.2015.11.011 | text, Tables 1–2 | SCHOLARLY | CC BY PDF (Newcastle) |
| Payne & Blackford 2008, Arctic 61, https://doi.org/10.14430/arctic22 | text, Table 1 | SCHOLARLY | eprint PDF |
| Kaufman et al. 2012, JQS 27, https://doi.org/10.1002/jqs.1552 | Tables 2, 4–6 | SCHOLARLY | 11's copy |
| Davies, Jensen & Kaufman 2022, GChron 4, https://doi.org/10.5194/gchron-4-121-2022 | text (WebFetch), not the supplement | SCHOLARLY | open |
| Hutchison et al. 2025 PNAS SI, https://oceanrep.geomar.de/61217/ | Zav-1 stratigraphy, Table S1 | SCHOLARLY | open |
| Matsumoto, Razzhigaeva & Nakagawa 2013 JpGU abstract SVC53-P18 | full | SCHOLARLY (abstract) | open |
| Nakanishi, Ashi & Okamura 2020, Data in Brief 33, https://doi.org/10.1016/j.dib.2020.106565 | text (WebFetch) | SCHOLARLY | open |
| Chen et al. 2019 Kushu glass supplement, https://doi.org/10.17632/bf76cyncdj.1 | sample list | SCHOLARLY (data) | CC BY |
| Ramalho, Pimentel & Pacheco 2023, EGU23-541, https://doi.org/10.5194/egusphere-egu23-541 | full abstract | SCHOLARLY (abstract) | open |
| Cabinet Office (Japan), Hokkaido tephra table (siryou4) | table | SECONDARY | open |
| GVP Holocene eruptions (06/01 cache) | Hokkaido, Azores rows | SECONDARY | cache |

**Searched but not readable (coverage gaps, in priority order):**

1. Jensen et al. 2021, QSR 272. This is the northeastern North America
   framework, with 21 new tephras and re-modelled Nordan's Pond Bog. All three
   copies refused (ScienceDirect, Southampton and QUB return 403/500, even
   through a browser). This is the biggest single gap for region 3.
   Pyne-O'Donnell et al. 2012 (Nordan's Pond) is closed.
2. Kuril soil-tephra papers. These are Razzhigaeva et al. 2013 (Simushir),
   Razzhigaeva, Matsumoto & Nakagawa 2016 (Quat. Int. 397, S. Kurils),
   MacInnes et al. 2016 (QR 86) and the KBP tDAR archive (id 376298). All are
   paywalled or behind a login. Only summaries were read.
3. Chen 2019 PhD thesis and Chen et al. 2019 QSR (Lake Kushu, Rebun). Both
   refused (403). The supplement was read: no analysed layer is shallower than
   B-Tm. Whether the top of RK12 was counted is unknown.
4. Kamchatka distal records. These are Plunkett et al. 2015 (three lakes),
   Kyle et al. 2011 and Ponomareva et al. 2015 Online Resource 3. They are not
   read here; 13 read what was open.
5. Dugmore, Larsen & Newton 1995 (Loch Portain B), Chambers et al. 2004
   (An Loch Mór), Davies et al. 2007 (Getvaltjärnen), Engels et al. 2025
   (Lontjørnane), Hall & Mauquoy 2005 (PMG-5), Watson et al. 2016, 2017
   (Cors Fochno CF-3). All are paywalled or unfound. Only Tephrabase's
   transcription was read.
6. Streeter & Dugmore 2014 (St Andrews repository). The connection was
   refused twice, so the ±5 definition and the bracketing tephras are unread.
7. Blockley et al. 2015 (Norse-site cryptotephra, Greenland). Closed. There is
   no open Greenland lake record for the last millennium.
8. Sakhalin: nothing found in English or Japanese. Russian-language searches
   were not run.

**Search queries used (web, 2026-10-21).** Kuril soil tephra Razzhigaeva 15th
century; Hokkaido peat cryptotephra B-Tm Ko-c2 Us-b; Newfoundland Mackay
Aniakchak NDN; Swindles Irish tephra review BGMT/BMR-90/GB4-57; Yukon/Alaska
peat cryptotephra Aniakchak 1400s; Jensen 2021 northeastern North America
framework; Pyne-O'Donnell 2012 Nordan's Pond; Chen 2019 Lake Kushu; Razzhigaeva
2016 S. Kurils; Shiveluch Commander/Bering/Karaginsky tephra; Ponomareva 2015
Online Resource; Faroe/Shetland/Scotland peat cryptotephra 15th century;
Getvaltjärnen V1477; An Loch Mór MOR-T1; Furnas 1439–1443; Chambers 2004
trachytic Azores; Johansson Furnas Ireland; 北海道 15世紀 テフラ 未同定 泥炭;
Hokkaido Ko-d / B-Tm / Ko-c2 sequence; 羅臼岳 Ra-2; Kamchatka lake cryptotephra
last millennium; Greenland lake cryptotephra last 1000 years; Alaska peatland
cryptotephra 400–600 cal BP; Davies 2016 interior Alaska keybeds; MacInnes 2016
Kuril tephra; Sakhalin peat tephra; Engels 2025 Lontjørnane.

## Hits (`results/hits.tsv`)

Each row has the dating evidence, proposed source, glass availability, URL,
tier and distance to each candidate vent. The table below is a summary.

| id | layer, site | dating evidence → age (CE) | proposed source | glass | bears on |
|---|---|---|---|---|---|
| AHK04 | Ahklun 0.4-ka tephra, Lone Spruce Pond + soil pit, SW Alaska (353 km from Aniakchak) | soil pit: ¹⁴C 435±15 on wood & leaves **below**, 1435–1468 (max); LSP model 1511–1635 | Aniakchak, "indistinguishable from CFE II", maybe redeposited (authors) | yes, bimodal | **H10** |
| KEN-MP39 | MP 39, Moose Pass, Kenai | one bulk-peat ¹⁴C 510±100 (1282–1633); extrapolated c. 1520 | "previously unidentified eruption" (Crater Peak-like) | yes, andesite | H10, H6 |
| KEN-ST24 | ST 24, Sterling, Kenai | interpolated c. 1480 | Katmai/Augustine-like, unresolved | yes, rhyolite 76.9 | H10 (against Pink) |
| KEN-micro | microtephras c. 510, 550, 590 cal BP, Kenai | interpolation from single bulk dates | none | no | H10, H6 |
| CL7 | CL-7, Cascade Lake, Brooks Range (1291 km) | Bayesian model, 1325–1875 (2σ) | Aniakchak (eruption not specified) | yes (supplement) | H10 |
| FBB12-47 | Framboise Bog, Nova Scotia | Bacon model 1374–1677 | MSH W? (n=2) | yes | none (screen: MSH We 0.98) |
| SCH10-57 | Saco Heath, Maine | Bacon model; age in Fig. 2/App. D only | uncorrelated | yes (n=4) | H6, H10 |
| VDB12-53 | Villagedale Bog, Nova Scotia | Bacon model; age in Fig. 2/App. D only | "similarities with Japanese tephra" (n=2) | yes | H6 |
| LPB | Loch Portain B, North Uist + Lairg, Scotland | peat ¹⁴C 540±50 **below** (1304–1447) and 360±70 **inside** (1428–1660); same interval as Hekla 1510 | unassigned | yes, rhyolite | H5, H6 |
| MOR-T2 | An Loch Mór, Ireland | Chambers 2004 model, c. 1400 | **Furnas I, Azores, 1439–43** (EGU23 abstract) | yes, trachyte | H3 (NHET), Azores (no H) |
| GRIM1457 | Grímsvötn 1457 Tephra, 141 soil sites, S Iceland | sediment-accumulation-rate date 1457±5 | Grímsvötn | 9/141 sites | H5 / Grímsvötn |
| GRIM1432 | Grímsvötn 1432 Tephra, 88 soil sites | as above, 1432±5 | Grímsvötn | Tephrabase | H5 |
| RA1 | Ra-1, Rausudake, E Hokkaido | GVP ¹⁴C cal 1350±100; govt table "500–700" BP | Rausudake | not found | H6 (VEI 3) |

`results/calib17.txt` holds the radiocarbon calibration. The column
"covers_1453" in hits.tsv uses it. Kaufman 2012's own "mean age 441 ± 64 cal
BP" (1445–1573) averages a model age with a maximum age. It is restated in
calib17 but should not be used.

**Glass screen (`results/glass17.txt`).** This is a Borchardt similarity
coefficient on normalised means. The reading rule was fixed before the run:
≥ 0.95 consistent, 0.90–0.95 same family, < 0.90 different. It is a screen,
not a correlation. Only references already in hand were used: Aniakchak
CFE II, Cascades, Ksudach KS1, Tarumai Ta-c2, WRAe, Ceboruco, Katmai 1912,
Augustine and Crater Peak. **No Kuril low-K, Shiveluch, Grímsvötn, Katla or
Half Cone glass was in hand**, so no hit could be scored against those. That
is 07's job.

## Informative absences

Each item names the record, what it caught, and the gap. The caveat applies
to all of them. Tephrabase lists layers found, not intervals counted. An
absence holds only if the authors counted the interval contiguously, and that
was checked in none of the closed papers.

1. **An Loch Mór, W Ireland** (Chambers et al. 2004 via Tephrabase).
   MOR-T1 (basaltic, the tentative V1477) is at 24.16 m. MOR-T2 (trachyte,
   Furnas I 1439–43) is at 24.38 m. No layer lies between them. If the
   interval was counted, this lake recorded a VEI-4 Azores eruption and a
   tentative V1477, but nothing from 1443–1477. It bears against an Icelandic
   or Atlantic source of 1453 that dispersed ash south-east. It says nothing
   about the North Pacific.
2. **Garry Bog, N. Ireland** (Hall & Pilcher 2002; Pilcher et al. 1996).
   Öræfajökull 1362 is at 0.40 m and Hekla 1510 at 0.30 m, with nothing
   between. It bears on H5 the same way.
3. **Tephrabase distal count.** Grímsvötn 1432 has 88 sites and Grímsvötn
   1457 has 141, all in Iceland. V1477 has 2 sites outside Iceland and Hekla
   1510 has 13. A Grímsvötn eruption of ≥ 4.7 Tg S (14) would be the largest
   Icelandic event since 1477, yet neither Grímsvötn layer of the period has
   been found outside Iceland. This weakens the Grímsvötn branch of H5. It
   does not refute it: basaltic shards are under-reported distally, and the
   V1477 count is also low.
4. **Lontjørnane, Norway** (Engels et al. 2025) and **Getvaltjärnen, Sweden**
   (Davies et al. 2007). Both caught V1477 as their deepest listed layer;
   Lontjørnane also caught Hekla 1510. Nothing is listed below V1477. The
   counted depth is unknown at both, so this absence is unverified.
5. **NE North America** (Mackay 2016, four bogs). JRB12-71 (1404–1578)
   correlates with MSH We 1482, and FBB12-47 (1374–1677, n = 2) screens as MSH
   We. No horizon is assigned to ~1453. The authors say low-concentration
   horizons went uncharacterised. This absence is weak.
6. **Simushir, central Kurils** (Hutchison 2025 Table S1, from Razzhigaeva
   2013). Zav-1 (1831) is the youngest pumice. Soil directly below it gives
   1258–1414 and 1282–1426 cal CE (bulk soil). No other Zavaritskii pumice
   lies between, so the Zavaritskii caldera itself is unlikely to have
   erupted in 1453. This bears on H12 for Zavaritskii only, not for the other
   central-Kuril calderas.
   **Calibration warning from the same table.** Before ice glass fixed Zav-1
   at 1831, charcoal within it dated 1479–1679 and 1496–1788 cal CE, and wood
   in its syn-eruptive mudflow 1382–1714 and 1413–1657. A Kuril tephra
   "¹⁴C-dated to the 15th century" can be 300+ years too old.
7. **South Kurils** (Matsumoto, Razzhigaeva & Nakagawa 2013). Of 22 Holocene
   tephras, the only local ones younger than 9 ka are Mendeleev (~2.5 ka) and
   Tyatya (1420 cal BP and 1973). No local tephra lies between them. This
   weakens Kunashir, Shikotan and Habomai volcanoes as sources.
8. **W Hokkaido Pacific coast** (Nakanishi et al. 2020, 42 sites, 431
   samples). Visible tephras are Ko-c2 1694, Ta-b 1667, Us-b 1663, Ko-d 1640,
   B-Tm 946 and Ta-c2. There is nothing between 946 and 1640. This bears
   against a large SW-Hokkaido source; it says nothing about cryptotephra.
9. **Greenland ice** (already in canon). Plunkett 2023 Table 1 has no tephra
   between 1254/5 and 1477.

## What each hit or absence bears on

- **H10 Aniakchak Half Cone.** The relevant evidence is AHK04, CL7, KEN-MP39,
  KEN-ST24 and KEN-micro.
  - AHK04 is the strongest lead in the sweep. It is 353 km from the vent, its
    glass is Aniakchak-type, and the dated material lies just below it at
    1435–1468.
  - Two things cut against it. The second site's model puts the layer at
    1511–1635. And its rhyodacite glass (71.3 wt%) is more silicic than Half
    Cone Pink matrix glass (68.3–69.8).
  - If 07 shows AHK04 **is** Half Cone, the LSP model age argues against 1453.
    The soil-pit maximum still allows it, so the two ages would have to be
    reconciled, and that would be the deciding test for H10.
  - ST24 is not Pink glass. MP39 cannot be told apart from Crater Peak.
  - Canon line 184–186 says Davies 2022's Cascade Lake layer "matches CFE II".
    The paper says only "Aniakchak", with younger eruptions not ruled out.
    That Cascade Lake (Brooks Range, 68.4° N) is a different lake from
    Kaufman's (Ahklun, 60.1° N).
- **H11 Shiveluch unit 5.** Nothing found. No distal record read here dates a
  Shiveluch layer to 1397 ± or 1440–1470. Kushu (Rebun) has a Shiveluch
  cryptotephra (SH#12), but its age was not readable.
- **H12 uncatalogued Kuril caldera.** Zavaritskii is weakened as the 1453
  source (absence 6), and so are the South Kurils (absence 7). The other
  central and northern calderas are untested (gap 2). The Zav-1 ¹⁴C history
  shows how easily a Kuril eruption is mis-dated by centuries.
- **Grímsvötn (H5).** Tephrabase's Grímsvötn 1457 ± 5 is a
  sediment-accumulation-rate date in south-Iceland soils (Streeter & Dugmore
  2014). It is not from ice. GVP's four Grímsvötn rows are labelled
  "Sidereal: Ice Core". Whether they are the same eruptions as Tephrabase's
  1432 and 1457 is unverified, so 06's leakage worry stands until the GVP
  references are read. 1453 lies at or just outside the ±5. There is no distal occurrence
  (absence 3). Loch Portain B is rhyolitic, which would not be expected of
  Grímsvötn basalt. That needs Grímsvötn reference glass to state, so it is
  listed as unverified below.
- **H3 / H2 (latitude).** MOR-T2 shows a NH-extratropical Atlantic eruption
  (Furnas I, 37.8° N, VEI 4 in GVP, 1441 ± 2) dispersing to Ireland. Its
  historical date is ten years early for 1453. It is not on the hypothesis
  list, and nothing here suggests the date is wrong. Nothing found bears on
  H7 (Pinatubo).

## What would make a hit decisive (07 and beyond)

1. **AHK04 vs Half Cone glass.** Use Kaufman 2012 Table S1 (single shards)
   against Browne 2022 appendix G (Pink and Brown matrix glass) and the Ash C
   analyses (Riehle 2000). Compare both modes: AHK04's andesite against Brown
   Pumice, and its rhyodacite against Pink.
   - If AHK04 is Half Cone, date it from the Lone Spruce Pond model (1511–1635
     argues against H10). Ask Kaufman whether the soil-pit wood was in situ.
   - If it is not Half Cone, the soil-pit bracket bears only on whatever it is.
2. **Loch Portain B.** Get Dugmore et al. 1995 for the authors' attribution.
   Compare its shards with Icelandic silicic references (Öræfajökull 1362,
   Torfajökull, Hekla) and with 1453-window candidates once 07 has them. If
   it is Icelandic and not a known eruption, it becomes the first distal
   1440s–1450s Icelandic candidate.
3. **Kenai MP 39.** Run a trace-element or full single-shard comparison
   against Crater Peak and Half Cone Brown Pumice. Re-date the site with
   macrofossils instead of bulk peat.
4. **Mackay SCH10-57 and VDB12-53.** Read their ages from Appendix D, which
   is in the supplement and not downloaded. If either falls in 1440–1470, add
   it to 07's queue.
5. **Jensen 2021.** Get it by request or library. It re-models Nordan's Pond
   and adds Michigan, New York and Maine bogs. This is where an ultra-distal
   North Pacific 1453 shard would most likely already be published.
6. **Kuril sections** (Razzhigaeva 2013/2016, MacInnes 2016, KBP tDAR). These
   would show whether any central or northern Kuril caldera has a tephra
   between Zav-1 and the previous dated marker.

## Unverified claims

- That Tephrabase's site lists are complete for each paper, and that empty
  intervals were counted. Every absence above depends on this.
- MOR-T2's age, "c. 1400 AD". It comes from the EGU abstract's restatement of
  Chambers 2004; the depth-age model is unread. The Furnas I correlation is a
  conference abstract, not peer-reviewed. Its method is stated only as "glass
  compositions and age constraints".
- That Furnas I is dated 1439–43 from settlement-era documents. GVP gives
  "Observations: Reported", but the primary chronicle was not read.
- The definition of Grímsvötn 1457's "± 5", and which historical tephras
  bracket it. Also unverified: that GVP's "Ice Core" Grímsvötn rows
  (1430–1470) are the same eruptions as Tephrabase's 1432 and 1457.
- That Loch Portain B is Icelandic, as Tephrabase's grouping implies.
  Dugmore 1995 is unread. Its high K₂O (3.5–4.9) and low CaO make
  Grímsvötn/Katla basalt implausible as the source. That inference rests on
  general knowledge of those systems, and no Grímsvötn or Katla reference
  glass was in hand.
- That the Ahklun soil-pit wood was in situ and contemporary with the surface
  the tephra fell on. Kaufman 2012 gives only "wood & leaves" below the
  tephra.
- The Rausudake Ra-1 age, "500–700". The Cabinet Office table gives no unit.
  Reading it as years BP is consistent with GVP's 1350 ± 100 (¹⁴C
  calibrated), but the AIST database page was not reachable.
- That Lake Kushu's top section (above B-Tm) was counted.
- Davies 2022 CL-7 shard counts and individual analyses (supplement Table S7,
  not downloaded).
- Coordinates for the Mackay sites, parsed from garbled PDF text
  (±0.02°). Kenai site coordinates are not given; only "Moose Pass" and
  "Sterling".
