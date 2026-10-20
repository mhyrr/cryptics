# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

- H1 Kuwae as the 1453 source. Refuted by the literature before this dive
  opened (Abbott 2021; Sigl 2013, 2015). Recorded 2026-10-20.

---

## 2026-10-20 — 14 Katla and Iceland (tests 1, size, annals, ash)
14 (Opus agent, pre-registered). Larsen 2000 (Jökull 49, not 50 as in
06) lists 15th-century Katla layers as 1416 (annals), ~1440, ~1500 and an
undated layer. GVP 1450 ± 50 is probably the undated one, catalogued as
KAT_1480 ± 20 and Small. Its soil-rate dating gave V1477 as 1480 ± 11, so
it is accurate to about ±10–20 yr. The annals are blank 1431–1472 and miss
even V1477. Size: Greenland-only conversion gives 4.7 Tg S; Katla 1755 gave
1.18. Only 1 of 15 Icelandic events shows any Antarctic sulfate. Verdicts:
Katla 1450 refuted, Katla 1440 and Hekla 1440 weakened, Grímsvötn rows open
(basis and size unknown; Grímsvötn's max in eVolv2k is 6.8 Tg S). The
particle comparison is fair on distance but not on size for Small Katla,
so 09's addendum is neutral for those rows. A post-hoc note kept out of the
verdict: 1497 has 2.9× particles with 2.4× sulfate, possibly Katla ~1500.

Round result (11–14): every named candidate from 06 is now refuted or
weakened. What survives is Aniakchak Half Cone (weak; needs wood dead
within ~20 yr), Grímsvötn (open, unknown basis), Shiveluch unit 5 (weak),
and an uncatalogued North Pacific / Kuril eruption (H12). The regional
answer holds; the named list has thinned.

## 2026-10-20 — 13 Kamchatka and Kurils (test 1 + size)
13 (Opus agent, pre-registered). Karymsky 1450 is the onset of the IIKM
cycle (KM3), not a KRM unit. Its only dates are three humic dates from one
buried-soil top; the 450 BP may be too young from modern roots. The
below-only setup fails the known-case test again (13/60), so the date
verdict is "uninformative but compatible": the authors' own reading gives
1414–1479. Size settles it. The whole 500-year cycle produced 0.13–0.15 km³
and the prehistoric part 0.07–0.09 km³, so VEI ≤ 3, and P(≥ 6.9 Tg S |
VEI 3) = 0.0015. Karymsky is refuted. Khangar, Maly Semyachik and
Sashiusudake have no volume, deposit or bracket, so they are weakened.
"SH1450" is 1450 14C BP, which kills a possible confusion. No regional
marker exists between SH2 and the historic eruptions. Shiveluch unit 5
(~1397 CE, volume unknown) is the one large-looking Kamchatka unit near
the window, now H11. The Zavaritskii precedent makes "an uncatalogued Kuril
caldera" a real hypothesis (H12). It is untestable without glass, but the
shared North Pacific score supports it.

Pattern after 11–13: own-date tests on 15th-century 14C keep failing their
known-case check, because the brackets lie only below the tephra. Size and
deposit checks are what kill candidates.

## 2026-10-20 — 12 Alaska near-field tree rings (Aniakchak test 2)
12 (Opus agent, gated pre-registration). No open series within 600 km
reaches 1453. The nearest, AK030 Wolverine Glacier at 661 km, has only 2
series in 1453. The gate failed: the 661–693 km band places Novarupta 1912
at the 31st percentile, and Kodiak + Iliamna + Kenai at the 10.8th. Only
Kodiak and Afognak (146–183 km, under the ash fall) show suppression; post
hoc, Kodiak alone is at the 2.2nd percentile. So 1453 was not computed.
Test 2 is uninformative, not negative. One lead from the walls: 11's buried
wood below the Pink Pumice, if it survives and has rings, could be
crossdated against the Prince William Sound master (back to 662). Its
outer ring would give a maximum date to the year, which would settle test
1. That is a sample request, not open data.

## 2026-10-20 — consequence tests; 11 Aniakchak own date
Greg's direction: when data cannot separate candidates, assume each one in
turn and test what must then be true, one test at a time. Written into
PLAN.md as "Consequence tests" (a standard six-test list per candidate).

11 (Opus agent, pre-registered). Bacon 2014, Neal 2001 and Browne 2022 agree
that the Half Cone Plinian (Pink then Brown Pumice) lies above New Cone.
There are 9 dates, all below the tephra and none above. The two key Half
Cone woods are from soil below, so they are maximum ages. The pre-registered
below-only model gives 1550–1800 CE and P(1451–54) = 0.0001, so the rule
says "refuted". But that model failed its own known-case test: 13/60
coverage with 3 dates below and none above, against 58/60 with brackets on
both sides. Its posterior runs to the open top of the prior. I accepted the
agent's override to "weakened". The usable statistic is the wood-death lag:
1453 fits at 0–20 yr, not at ≥ 50 yr. New Cone is older, so it is not a
candidate. Walls: no dated layer above the tephra (archaeology paywalled or
NPS-restricted); no published Half Cone sulfur data; no Aniakchak Δ33S.
Tests 3 and 4 for Aniakchak therefore hit walls at once. Browne 2022
appendix G has the Pink, Brown and Ash C glass that 07 needs.

## 2026-10-20 — 09 addendum: TUNU2013 annual particles (Table S7)
Greg added the Abbott 2021 supplement to `sources/`. It is byte-identical
to 02's copy (sha256 7b9f4b43…). Re-reading the sheet titles showed that
Table S7 holds annual TUNU2013 coarse-particle mass for 1450–1500. 02 used
only its sulfate, and 09 Part B wrongly listed the particle record as
unarchived; only the sub-annual version is unarchived. Post hoc,
`particles_s7.py`: 1453 is 1.23× median (rank 17/51); Veiðivötn 1477 is
8.1× at similar sulfate. H5 is weakened (one calibration case). Lesson:
check every sheet title of a downloaded supplement, not only the one the
experiment needed.

## 2026-10-20 — experiment 06, candidate ranking (T2 attempt)
06 (Opus agent, pre-registered, about 35 fetches). The survey was wrong
about Katla 1450 ± 50: it is tephra-dated, not ice-dated. The four
Grímsvötn 1430–1470 rows are ice-dated and were dropped by the leakage
rule. They probably come from Vatnajökull glacier tephra (Larsen 2005), not
Greenland, but this is unverified. In a sensitivity run, Grímsvötn 1450
ranks first only because the missing-VEI prior flatters a volcano whose
eruptions are mostly VEI 2.

21 lab ages for 4 eruptions, recalibrated with IntCal20 (`lab_ages.csv`).
El Chichón B ends by 1409, which nearly kills H8. Pinatubo Buag 1410–1457
and both Aniakchak units span 1453. Each date term sits near the flat
baseline, so dates only mean "not excluded": 15th-century 14C cannot
resolve a year.

Blind calibration on 24 known sources: with degraded dates, the truth is
top 5 in 16 of 20 present cases (pre-registered criterion met). But that
rank comes from VEI. With VEI hidden, as for nearly every 1453 candidate,
it is top 5 in 8 of 20. Four true sources are absent from the catalog,
including Samalas, which the leakage rule drops, and Zavaritskii.

1453: Aniakchak Half Cone 0.105, Katla 0.075, Pinatubo 0.055, Aniakchak
New Cone 0.048, Terceira 0.044. The order shuffles under every variant.
Region: North Pacific > 30° N holds 0.57, Iceland + Jan Mayen 0.16.
Verdict: the T2 named shortlist is weak. The region-level answer (an
unidentified NH extratropical eruption, most likely North Pacific, Iceland
second) stands. New H10 Aniakchak Half Cone gives 07 a first glass target.
Not reached: TephraKam tables, the Icelandic catalogue, and the Katla 1450
and Iwate primary papers.

## 2026-10-20 — experiment 10, harvest dates; Euro-Climhist and PANGAEA closed
Greg registered for Euro-Climhist and PANGAEA. Euro-Climhist holds about
1,500 records for all Europe in 1451–1500. Its 15th-century content is long
series, not searchable chronicles, so it is dropped. PANGAEA.995655 (the
401 in 02) is Ōruanui 25.3 ka glass in Antarctic cores (Mattin, Barker,
Burke, Hutchison et al.; moratorium to 2026-12-23), so it is not relevant.

10 (Opus agent, pre-registered): Beaune grape-harvest dates come from
inverting Labbé 2019's T = 31.59 − 0.061 × GHD, ±1 d. Primary calibration:
3/12 large eruptions give a harvest at or above the 90th percentile in E or
E+1, against 2.2 expected (p 0.37). Laki and Pinatubo gave early harvests.
1452 −3.5 d, 1453 +11.5 d (89th percentile), 1454 +8.5 d. No timing
inference under the pre-registered rule. A post-hoc check found that
1453–56 may be Dijon fills. Daux 2012 has no independent series for
1452–54.

## 2026-10-20 — experiment 09, ice tracers
09 (Opus agent, pre-registered). Calibration: every named eVolv2k v4 source
in range (15 Iceland, 9 other NHX, 12 tropical). NEEM lithic and acidity
features: LOO 0.31, p 0.92. NEEM's Ce/Mn/Ca miss Laki, Eldgjá and
Veiðivötn 1477 against 355 empty years. A Ce rise above z = 3 occurs in 23%
of empty windows. TUNU2013 (Arctic Data Center doi:10.18739/A2ZD34, open,
preliminary, 30 species): LOO 0.70, p 0.081. Halogens and volatile metals
do not separate. Zavaritskii 1831, with known shards in TUNU2013, shows no
lithic excess, so continuous-flow chemistry misses fine distal ash.

UE 1453, read after the tests: no NEEM lithic excess. TUNU2013 Al pulse at
the 97th percentile, 0.1–0.3 yr after sulfate onset. Lowest nssCl/S of all
events, possibly an Na-correction artefact. Post hoc, Al beats empty
windows for 4/8 ICE, 0/6 NHX, 1/7 TROP (p 0.047). That is a lead to
pre-register on new data, not a result. The literature claim that halogens
separate Icelandic eruptions is unverified (Mason 2022, Green 2025 unread).

Data inventory: TUNU2013 particle record "available on request" (Plunkett
2023); NGRIP DRI chemistry misses the 1450s; EGRIP nothing. H5 and H6 do
not move. The Al pulse gives the depth to cut for glass: ~1452.9–1453.4.

## 2026-10-20 — experiment 08, summer 1452
Greg asked whether open data could test the year before. Two checks run in
the scratchpad (not results): NEEM Ce/Mn raw peaks are 2–4× for Icelandic,
tropical and UE 1453 alike, because spring dust dominates (handed to 09).
Summer 1452 in NEEM carries a large NH4 + BC fire plume (35×, 6×), top ten
of 3,030 samples 1300–1600, not volcanic.

08 (Opus agent, pre-registered): summer 1452 is normal in MXD and N-TREND.
The eruption-year response does not separate season or class at these
sizes (AUC 0.53–0.61), so a normal 1452 excludes little. Combined with 02,
the extratropical window is 1452.9–1453.5 and the tropical window is
1452.0–1453.1. No regional pattern in 1452 (Moran's I p 0.42, 0.83). The
coldest sector found the source in 2 of 8 calibration cases. Frost rings:
1453 is the top latewood frost year at Almagre Mountain 1250–1993 (75% of
trees); none in 1452 or 1454. These pines miss 1783 and barely show 1601
and 1641, so this is weather, not a fingerprint.

Date bounds now: earliest from the ice (no sulfate by 1452.55 in Burke's
TUNU2013 background sample; 02's window); latest from the cold summer of
1453 and Korean cold on 2 Aug 1453.

## 2026-10-20 — experiments 02–05 (session 2)
Four Opus agents ran 02, 03, 04 and 05 in parallel. I spot-checked each
headline number against its `results/` file.

**02-ice-onset.**
- *Shard search.* Abbott 2021 sampled TUNU2013 only at 1477–1479
  (Sect. 3.2, p. 570) and lists the 1450s as future work (Sect. 5.2,
  p. 577). Plunkett 2023 Table 1 lists no Greenland tephra between 1254/5
  and 1477, including its new TUNU2013 samples. So there is no published
  search for TUNU2013 or NEEM-2011-S1. NGRIP and Summit are unknown:
  Cole-Dai 2013 and Coulter 2012 returned Wiley 403. The "no tephra" line
  traces to Wikipedia citing Cole-Dai, and that line is unverified.
- *Onset.* NEEM onset 1453.13 ± 0.05; TUNU2013 1453.00 ± 0.04. Both sit at
  the Na maximum. Large calibration eruptions also start at the Na maximum
  whatever their month (Laki Jun, Tambora Apr, Krakatau Aug,
  Huaynaputina Feb). Onset position therefore cannot give the season.
  Calibrated eruption window: early 1452 to mid-1453. The quality rules
  were added after the first run; the README says so.
- *Antarctica.* 5 of 15 cores are above background at p < 0.05 (chance:
  0.8; binomial p = 0.0006, overstated by correlated cores). WAIS Divide
  monthly onset 1453.6, half a year after Greenland. The canon line
  "Dome C shows nothing" holds only for the isotope sample; EDC96 sulfate
  has z 5.5. H4 is weakened.
- *Structure.* One pulse per high-resolution core and one Δ33S excursion.
  H9 is weakened, but sulfate cannot separate eruptions weeks apart.

**03-latitude-posterior.**
- Asymmetry, calibrated on 39 named eVolv2k events (217 dropped for
  leakage), excludes SHET but does not separate NHET from 0–30° N. Its
  likelihood ratio at 0.83 is 0.3–3 depending on the window.
- The Marshall 2021 emulator is open (CEMAC GitHub JSON). It reproduces
  Marshall Table 1 and keeps 17° S–67° N for 1453. Its own calibration
  ranks the true band first for only 7 of 15 events, and its injection
  floor is 15 km.
- The isotope class is 7/7 on known cases, but only 2 cases are out of
  sample, both NHET. No tropical case is out of sample.
- P(NHET) is 0.69–0.94 under ordinary priors, 0.44 with out-of-sample
  isotopes only, and about 0.5 under a tropics-heavy prior. H3 now rests
  on the isotopes.

**04-cooling-fingerprint.** The ≥ 60° N vs < 60° N cooling contrast does not
separate 7 extratropical from 14 tropical eruptions in any of three
networks (AUC 0.39–0.49, permutation p 0.55–0.81). Makian, Parker and
Huaynaputina cool the far north as hard as Laki. Esper 2017's
high-latitude maximum no longer counts for H3.

**05-documentary-onset.**
- The Sillok and the full Ming Shilu were searched on sillok.history.go.kr.
  Dates were fixed astronomically: 98% match the record's own day names.
- Cold reaches Korea on 2 and 17 Aug 1453 (Julian): snow at Hamheung, and
  three days of frost at Gapsan "like the tenth month".
- The Ming winter disaster begins 15 Dec 1453. Cold/snow reports in lunar
  1453–54 are 22 against 3.5 expected; 19 of them fall in winter 1453/54.
- No dim or red sun is recorded in 1452–55 in any source reached. The
  Mingshi does record one on 25 Mar 1458.
- Calibration: frosts after Parker 1641 are detected (p = 8×10⁻⁶);
  Huaynaputina and Kuwae are not. The method sees about one case in three.
- Therrell 2004's Mexican famine is drought-led and began by 1450–52.
- Walls: Euro-Climhist login, Japanese diaries, Constantinople narratives.

**Where this leaves the dive.** The hemisphere is settled (NH). The band
(NHET vs 0–30° N) rests on one isotope test. Neither ice nor documents give
the season. Next: 08 tests whether summer 1452 was already cold, and 09
tests lithic and halogen tracers in the ice.

## 2026-10-20 — opening survey and research path
Opened as the repo's first `natural-record` dive. Added the kind to
`scripts/catalog_lib.py`, `catalog/TEMPLATE.md` and the admission rule to
`rubric/RUBRIC.md`.

Four Opus agents surveyed open data in parallel. Reports are in
`sources/survey-2026-10-20/`. What changed my picture:
- Burke et al. 2023 reclassify 1453 as NH extratropical from TUNU2013 sulfur
  isotopes. eVolv2k v4 carries that classification (latitude 45.0 default).
- Esper 2017's cooling maximum sits at high northern latitudes. That fits
  Burke but has not been tested as a discriminator.
- Abbott 2021 sampled TUNU2013 for tephra only at 1477 and 1479. We found no
  published shard search of the 1453 Greenland layer. If that holds, the
  "lack of tephra" in the popular account is absence of search, not a negative result.
- The Greenland/Antarctic ratio constrains latitude weakly, because season
  trades against latitude (Marshall 2021). The season of onset is the missing variable.
- No paper names a candidate. GVP's only VEI-5 rows covering 1452 are both
  tropical (Pinatubo, El Chichón), which conflicts with Burke.
- Documentary evidence (Ming snow, Constantinople fog) reaches the
  literature only through Pang 1993 (CLAIMANT). Primary chronicles are unchecked.

Analysis: `analysis/01-gvp-window/` reran the survey's GVP filter
(58 / 59 rows). Wrote `PLAN.md`: success tiers T1–T3, the calibration set,
the ice-core leakage rule, experiments 02–07, and the wall (1453 ice shards).
