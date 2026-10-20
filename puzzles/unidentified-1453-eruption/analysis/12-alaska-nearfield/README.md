# 12 — Alaska near-field tree rings

**Question.** If Aniakchak Half Cone (56.9° N, 158.2° W) erupted around
winter 1452/53 (H10), trees within a few hundred km should show a local shock
in 1453 or 1454 on top of the hemispheric cooling: ring-width suppression,
missing rings, or abrupt release, stronger near the vent. Do they? This is
consequence test 2 in PLAN.md. Test 1 (11) left 1453 possible only if the
dated wood died within ~20 years of the eruption.

## Step 1 — Coverage (done before any ring value was read)

Source: NCEI paleo-search API, tree-ring data type, box 50–72° N, 170–128° W
(`data/search_ak.json`, 445 studies). `coverage.py` lists every data table
with its distance from Aniakchak. Full list: `results/coverage_all.txt`;
tables starting before 1500: `results/coverage_pre1500.txt`. The start year
is the first year of any sample, not of adequate sample depth.

Nearest series, by region:

| Region | Code | Site | Species | Start | km from Aniakchak |
|---|---|---|---|---|---|
| Katmai (V. 10,000 Smokes) | V10K2016 | isotopes | PCGL | 1971 | 235 |
| Afognak / Kodiak | AK014 | Settlement Point | PCSI | 1690 | 353 |
| Kodiak | AK17, AK108, AK12, AK14 | | PCSI | 1721–1789 | 362–365 |
| Iliamna / Lake Clark | AK086, AK087, AK089, AK088 | Fish Trap, Portage L., Lower Twin L., Telaquana | PCGL | 1600–1769 | 456–515 |
| Kenai lowlands / Kachemak | AK018, AK017, AK023, AK026 | | PCSI | 1615–1790 | 502–566 |
| Kenai mountains | AK191, AK016 | Upper Fuller L., Exit Glacier | TSME, PCSI | 1525, 1574 | 613, 620 |
| **Kenai / Prince William Sound** | **AK030** | **Wolverine Glacier** | **TSME** | **1247** | **661** |
| Prince William Sound | AK120, AK094, AK167, AK208, AK028, AK001, AK227, AK224, AK091, AK096, AK107 | | TSME, TSHE | 873–1431 | 693–792 |
| Seward Peninsula | AK115, AK058, AK062, AK065, AK067 | | PCGL | 1358–1406 | 944–950 |
| Wrangells / Copper R. / Yakutat | AK020, AK169, AK171, AK076, AK121, AK021 | | TSME, PCSI, PCGL | 838–1428 | 830–1116 |
| Brooks Range / Yukon | AK110, AK046, AK106, AK104, AK033, CANA354, CANA326 | | PCGL | 913–1303 | 1132–1494 |

There are no trees on the Alaska Peninsula south-west of Katmai or on the
Aleutians in the archive, and no open series in Cook Inlet west shore,
Bristol Bay, Kodiak or the Katmai coast reaches back past 1600.
The published Katmai white-spruce sites (Sherriff et al. 2011; Miller,
Sherriff and Berg 2012) hold trees 130–170 years old, the oldest 235 years.

**Coverage wall.** Nothing within 600 km of Aniakchak reaches 1453. The
nearest series that does is AK030 Wolverine Glacier (mountain hemlock,
1247–1991) at 661 km. The rest of the 1453-reaching ring is Prince William
Sound mountain hemlock at 693–792 km.

The brief says to stop at this wall. 661 km is "about 600 km", so I run one
bounded feasibility test on that band, gated by a Novarupta 1912
calibration on the same trees. Those trees lie ~430–550 km from Novarupta,
closer than they are to Aniakchak, and Novarupta was larger (VEI 6, ~13 km³
magma) than Half Cone (VEI 5). If they cannot see Novarupta, they cannot see
Half Cone, and the wall stands.

## Step 2 — Pre-registration (written 2026-10-20, before any ring value was downloaded)

What I knew: the coverage table above; the NPS summary of Miller et al. 2012
(Katmai sites show a short suppression then a release after 1912; the
suppression was seen only in Katmai stands, "not in other locations
sampled"; Kodiak showed suppression and later release); 04 and 08's
hemispheric results (1453 is the cold year network-wide). I had not seen any
Alaskan ring value for 1453, 1454 or 1912.

**Sites (fixed now).** Raw measurements (`.rwl`) from ITRDB.
- *Band* (the only sites that could test 1453): TSME/TSHE sites 650–800 km
  from Aniakchak that reach 1453: AK030, AK094, AK167, AK028, AK001, AK227,
  AK091, AK096. Where several tables share one location I take one
  (AK120 = AK094 location; AK107, AK224 = AK096/AK091 location; AK208 is a
  blue-intensity version of Tebenkof).
- *Close-1912* (calibration only, ≤ 400 km from Novarupta, reach 1900): Kodiak
  and Afognak AK014, AK17, AK108; Iliamna AK086, AK089; Kenai lowlands AK018,
  AK023; Exit Glacier AK016.
- *Control*: Alaska and Yukon sites > 1000 km from Aniakchak reaching 1453:
  AK110, AK046, AK104, AK033, AK076, AK121, AK021, CANA354.

**Site chronology.** Each series: index = width / its own centred 31-year
running mean (window truncated at the ends, ≥ 15 values). Site index = mean
over series. A site-year needs ≥ 3 series. Missing rings (width 0) stay as 0.

**Anomaly.** 04's definition, by import of `../04-cooling-fingerprint/fingerprint.py`
(`site_sd`, `anomalies`, `exclusion_years`), unchanged: value(Y) minus the
mean of E−10 … E−1, leaving out [E′, E′+2] for every other eruption in the
exclusion list (eVolv2k VSSI ≥ 3 Tg S plus every event in `events.tsv`), ≥ 5
reference years, divided by the site's high-pass SD (1250–1990).

**Statistic.** For an eruption in year E with response years R:
D(Y) = mean z over *near* sites − mean z over *control* sites, and
D_min = min over Y in R of D(Y) (a local suppression in either year).
D_max (release) is reported but is not used in a decision.
- Novarupta (June 1912): E = 1912, R = {1912, 1913}.
- UE 1453: E = 1452 (reference 1442–1451, as 08), R = {1453, 1454}.

**Background.** D_min computed the same way for every year Y with no
exclusion-list start in [Y−2, Y], with E = Y and R = {Y, Y+1}, over years
where every group has ≥ 3 sites: 1500–1985 for the calibration, and the
same for the target (the 1453 value is compared with the same background).
An event's percentile is its rank in this background (one-sided, low).

**Calibration rule (step 3).** The band "detects" Novarupta if D_min(1912)
with near = Band is at or below the background 5th percentile. If not: the
band cannot test 1453. 1453 is then not computed as a test; I write that and
stop. Close-1912 is run the same way to show whether *any* open ring-width
group sees 1912 locally. Secondary events (descriptive only; same groups):
Aniakchak May 1931, Spurr Jul 1953, Augustine Jan 1976 and Mar 1986,
Redoubt Dec 1989 (R = 1990, 1991), Okmok Mar 1817 and 1945 (if covered).
Also a regression of per-site z (min over R) on distance from the source
across all sites, slope and permutation p (10 000 shuffles, seed 1453).

**Decision rule for 1453 (step 4, only if the band detects 1912).**
- D_min(1453/54) ≤ background p5: near-field signal present. Consistent with
  H10 but equally with any south-central Alaska source.
- D_min > background p5: no near-field signal detected. H10 is weakened only
  slightly, because the band is farther from Aniakchak than from Novarupta and
  Half Cone was smaller.

**Reverse test.** Per-site z for 1453 and 1454 (min), grouped by region
(Kenai/PWS band, Wrangells/Yakutat, Brooks/Kobuk, Yukon). Lowest region mean,
one-sided permutation p (shuffle z over sites). Reported, no decision.

## Deviations

All three were made before the calibration was run, except 3.

1. **Duplicate series.** AK096 ("Coastal Alaska") is a composite. It repeats
   83 series from AK094, 73 from AK091 and 21 from AK030; AK167 repeats 12
   from AK094. `nearfield.py` reads sites in `sites.tsv` order and drops any
   series identical to one already used (AK096 −180, AK167 −12). Without
   this the band would count the same trees twice.
2. **Sample depth.** With ≥ 3 series per site-year, AK030 (2 series in 1453),
   AK028 (2), AK001 (1) drop out of the band for 1453; AK076 (1) and AK021 (1)
   drop out of the control. The nearest site with ≥ 3 series in 1453 is
   AK094 Prince William Sound at 693 km, not AK030 at 661 km.
   After deduplication AK167 has no living trees, so it is absent in 1912.
3. **Post hoc check (not pre-registered).** After the gate failed I ran the
   same statistic with near = the three Kodiak/Afognak sites
   (`nearfield.py posthoc`). It is labelled post hoc everywhere and does not
   enter any decision.

## Calibration (step 3)

`results/calibrate.txt`. Background: 384 years (1500–1984) for the band,
249 (1658–1984) for Close-1912.

| Group | km from Novarupta | D(1912) | D(1913) | D_min | Background pctl | Detects (≤ p5)? |
|---|---|---|---|---|---|---|
| Band (7 sites in 1912) | 425–553 | +1.04 | −0.87 | −0.87 | 31.2 | **no** |
| Close-1912 (8 sites) | 146–383 | −0.33 | −1.50 | −1.50 | 10.8 | no |
| Kodiak trio, post hoc | 146–183 | −1.47 | −3.24 | −3.24 | 2.2 (4th of 186) | yes, post hoc |

Per-site 1912/13 minimum z, by distance from Novarupta: the three Kodiak and
Afognak sites at 146–183 km sit at −2.7 to −3.0. From 250 km outward the
values (−1.7 to +0.4) look like the control sites (−0.2 to −2.7), which
carry the hemispheric 1912 cooling. The distance slope over all 23 sites is
flat (+0.01 z per 100 km, p = 0.82).

**Rule outcome: the band does not detect Novarupta.** The Kenai and Prince
William Sound mountain hemlocks sit 425–553 km from the largest eruption of
the 20th century and record nothing beyond the hemispheric cooling. A local
shock shows only on Kodiak and Afognak, downwind and under ~30 cm of ash
(NPS summary of Miller et al. 2012), and even there it is fourth of 186
background years, not first. This matches Miller et al., who found the
1912 suppression only in Katmai stands and on Kodiak.

Secondary events (descriptive): no group reaches p5 for Aniakchak 1931,
Augustine 1883, 1976 or 1986, Redoubt 1989 or Okmok 1817. Close-1912 reaches
p2 for Spurr 1953 (D_min −2.21, in 1954). That is one hit in 14 group-event tests, about what chance gives at p5. I
do not read it as a detection.

## Result (step 4)

**Not computed.** The pre-registered gate failed, so the band cannot test
1453 and the 1453/1454 value was not computed. No reverse test was run
either: the only trees reaching 1453 lie 690–790 km from Aniakchak, and
Cook Inlet's west shore and the Aleutians have no tree series that old
(the Aleutians have no trees).

What this does to H10: nothing. Test 2 is uninformative with open data. It
neither supports nor weakens Half Cone.

## The wall

A local ring-width shock from a VEI 5–6 Alaskan eruption shows within about
200 km downwind of the vent (Kodiak in 1912), not at 400–550 km. No open
tree-ring series within 600 km of Aniakchak reaches 1453. The nearest with
≥ 3 series in 1453 is AK094 Prince William Sound (mountain hemlock) at
693 km. Near the vent, the oldest open series start in 1600–1790
(Iliamna 1600, Kodiak 1690–1789) and living Katmai trees are ≤ 235 years old.

What would breach it:
- Subfossil or buried wood within ~200 km of Aniakchak, crossdated through
  1453: snags or stumps under or in the Half Cone tephra on the Alaska
  Peninsula, or archaeological wood from Bristol Bay or Kodiak sites. The
  buried wood behind 11's ages is the obvious first place to look. If it
  could be crossdated against the Prince William Sound master (AK094, AK096,
  back to 662), its outer ring would date the eruption to the year. That
  would also close test 1.
- Wood-anatomy damage marks (frost or light rings, traumatic resin ducts)
  in 1453 at the PWS sites would need the physical samples, not `.rwl` files.

## Limits

- Ring width only. Density (MXD) responds more sharply to summer cooling,
  but no Alaskan MXD series reaches 1453 here.
- Ring-width memory spreads a shock over several years. A two-year response
  window may miss a slow suppression. The post hoc Kodiak values for 1914
  (−1.8) show the 1912 shock lasting into a third year.
- Direction matters. Ash fall depends on the wind on the day. Kodiak was
  downwind in 1912. The band was not, and the same could hold for any 1453
  plume.
- Moving-mean detrending dilutes a one-year anomaly by about 1/31. That is
  small next to the observed differences.
- The control group is not free of local effects: it spans Brooks Range,
  Wrangells, Yakutat and the Yukon, with their own climate.
- 1812/13 rank lowest in the Kodiak background (Augustine erupted in July
  1812, VEI 3, by GVP). Not followed up; it is post hoc.

## Proposed canon lines (for the main thread; not written to canon.md)

- No open tree-ring series within 600 km of Aniakchak reaches 1453. The
  nearest with ≥ 3 series in 1453 is ITRDB AK094 Prince William Sound
  (mountain hemlock) at 693 km. `established` (for the ITRDB archive as of
  2026-10-20) — `analysis/12-alaska-nearfield/results/depth.txt`.
- In open ring-width data, Novarupta 1912 shows a local suppression on Kodiak
  and Afognak (146–183 km, z ≈ −2.8 in 1912 and 1913) and none at the Kenai
  and PWS sites (425–553 km) beyond the hemispheric cooling. `likely`
  (Kodiak part post hoc; agrees with Miller et al. 2012) —
  `analysis/12-alaska-nearfield/results/calibrate.txt`, `posthoc_kodiak1912.txt`.
- Consequence test 2 (near-field tree rings) cannot be run for Aniakchak with
  open data. `established` — same.

## Run

```
python3 -I coverage.py data/search_ak.json > results/coverage_all.txt
python3 -I coverage.py data/search_ak.json 1500 > results/coverage_pre1500.txt
python3 -I fetch.py data/search_ak.json sites.tsv data/ > results/fetch_sha256.txt
python3 -I nearfield.py depth sites.tsv data/ > results/depth.txt
E=../04-cooling-fingerprint/data/evolv2k_v4.tab
python3 -I nearfield.py calibrate sites.tsv data/ events.tsv $E > results/calibrate.txt
python3 -I nearfield.py posthoc sites.tsv data/ events.tsv $E > results/posthoc_kodiak1912.txt
```

The search dump came from
`https://www.ncei.noaa.gov/access/paleo-search/study/search.json?dataTypeId=18&minLat=50&maxLat=72&minLon=-170&maxLon=-128&limit=500`
(fetched 2026-10-20; save it as `data/search_ak.json`). Each `calibrate` or
`posthoc` run takes under a minute. Standard library only. The anomaly code
is imported from 04 (`../04-cooling-fingerprint/fingerprint.py`), and the
group-difference, background and percentile logic follows 08's pattern;
credit to both.

## Provenance

| Item | Source | Tier |
|---|---|---|
| Site list, coordinates, species, spans | NCEI paleo-search API (above) | PRIMARY (archive metadata) |
| Ring widths | ITRDB `.rwl` files; URLs and sha256 in `results/fetch_sha256.txt` | PRIMARY |
| AK094, AK167 | Barclay, Wiles — https://www.ncei.noaa.gov/access/paleo-search/study/8494, /27410 | PRIMARY |
| AK096, AK091 | D'Arrigo, Wiles, Wilson — /study/8600, /8602 | PRIMARY |
| AK227 | Wiles, Wiesenberg — /study/44494 | PRIMARY |
| AK030, AK028, AK016, AK018, AK023, AK021 | Wiles, Calkin (and Frank) — /study/5252, 5251, 5241, 5243, 5247, 5244 | PRIMARY |
| AK001 | Fritts — /study/3264 | PRIMARY |
| AK014 | Harlan et al. — /study/3480 | PRIMARY |
| AK17 | Kaiser — /study/3654 | PRIMARY |
| AK108 | Wiles, D'Arrigo, Jacoby — /study/12466 | PRIMARY |
| AK086, AK089 | Wiles, Driscoll, D'Arrigo — /study/5561, /5562 | PRIMARY |
| AK110, AK033 | Jacoby, D'Arrigo, Buckley — /study/12468, /3607 | PRIMARY |
| AK104, AK076 | Jacoby, Davi (Wiles) — /study/12451, /3590 | PRIMARY |
| AK121 | Barclay, Van Loan, Jacoby — /study/13714 | PRIMARY |
| AK046 | King, Graumlich — /study/3706 | PRIMARY |
| CANA354 | Luckman et al. — /study/13785 | PRIMARY |
| Katmai 1912 response (suppression only in Katmai stands; Kodiak suppression then release; Kodiak ash up to 30 cm; trees ≤ 235 yr) | Miller, Sherriff, Berg 2012, Alaska Park Science 11(1), https://www.nps.gov/articles/aps-v11-i1-c12.htm | SCHOLARLY (agency journal summary) |
| Eruption dates, VEI | GVP Holocene table, `../../sources/cache/gvp_holocene_eruptions.csv` | SECONDARY |
| Novarupta magma volume ~13 km³ | not fetched here; Hildreth & Fierstein 2012 (USGS PP 1791) | Unverified in this experiment |

## Unverified claims

- Kaiser-Bernhard (1987) on Katmai 1912 and the 1964 earthquake in Kodiak
  Sitka spruce: citation seen in search results only, not read.
- Half Cone being smaller than Novarupta rests on VEI (5 vs 6, GVP) and
  06's ≥ 5.4 km³ (Browne 2022). Novarupta's ~13 km³ is from memory.
