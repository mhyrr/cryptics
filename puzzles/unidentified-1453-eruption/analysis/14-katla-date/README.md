# 14 — Katla and the other Icelandic window rows: own date, annals, size, ash

**Question.** If an Icelandic eruption made UE 1453 (H5), its own deposits
must date to about 1452–53 CE, the annals must not contradict it, it must be
able to make the sulfate seen in Greenland and Antarctica, and its ash should
have reached TUNU2013. Do any of the Icelandic rows in 1440–1470 survive?
No polar-ice date enters the date test (leakage rule).

## Pre-registration (written 2026-10-20, before any Icelandic date was collected)

What I knew when I wrote this: GVP rows from `../../sources/gvp-eruptions-1400-1500.csv`
(Katla 1416 VEI 4 reported, Katla 1440 VEI 4 reported, Hekla 1440 tephrochronology,
Katla 1450 ± 50 tephrochronology, Grímsvötn 1430 ± 10, 1450 ± 10, 1469, 1470 ± 10
"Sidereal: Ice Core", Veiðivötn 1477 reported, Katla 1500 tephrochronology);
06's ranking; 09's particle result (1453 is 1.23× the 1450–1500 median for
4.5–9.5 µm particles in TUNU2013, V1477 8.1×); and the eVolv2k v4 Icelandic
rows used in 03 (all named Icelandic sources have zero Antarctic deposition
except Hrafnkatla 763). I had not read any Icelandic tephrochronology paper.

**Candidates.** Every Icelandic row (GVP or found in the primary literature)
with a date range overlapping 1440–1470 CE.

**Test a (own date).** For each candidate, record the dating basis:
`historical` (an annal year), `marker` (bracketed between dated marker
tephras, e.g. H1300/H1341/H1389/Ö1362/V1477/H1510), `soil-rate`
(interpolated by soil accumulation between markers), `14C`, or `ice`
(Greenland ice or a date tuned to it). Ice-only dates do not count. Glacier
(Vatnajökull) layer counting counts if its chronology is not tied to Greenland.
The implied range is the bracket for `marker`, the stated error (2σ if given,
else as stated) for `soil-rate`, the annal year ± 0 for `historical`.
- a = **fail** if the implied range excludes all of 1452.0–1454.0.
- a = **pass** if the range contains 1452–53 and is ≤ 30 yr wide.
- a = **neutral** otherwise (contains 1452–53 but wider than 30 yr, or no
  primary source read).

**Test b (annals).** A recorded eruption of this volcano in 1452 or 1453 is
a **pass**. Silence is **neutral** if the annals for 1452–53 are sparse or
missing (the gap), and counts as weak against only if the annals are shown to
be continuous and detailed for those years. A recorded eruption in a
different year that the candidate's row is based on makes a = fail by the
`historical` rule.

**Test c (size and pattern).** Scale from eVolv2k v4 (ice-derived, the same
method that gives 1453 its 9.97 Tg S) for named Icelandic eruptions, plus
petrologic S yields where found.
- c = **fail** if the candidate's eruption type has no published
  (petrologic or ice) S yield ≥ 3.8 Tg S (the 1453 value minus 2σ) in the
  last 2000 years at that volcano or volcanic system, *or* the published
  volume/type of the candidate itself makes ≥ 3.8 Tg S implausible.
- Pattern: count named Icelandic eruptions in eVolv2k with Antarctic
  deposition > 0. If none reaches 5.1 kg km⁻² (1453's Antarctic value), the
  1453 Antarctic signal needs a second eruption or a bipolar transport that
  no Icelandic event shows; this is recorded as **pattern against** and
  counts with c (c = fail if both the size test fails and the pattern is
  against; c = weak if only the pattern is against).
- c = **pass** otherwise.

**Test d (ash).** Compute great-circle distance from the vent to TUNU2013
(78.0° N, 33.9° W) for the candidate and for Veiðivötn. Record eruption
season and plume height where published.
- d = **fail** if the candidate is within 1.5× V1477's distance, is an
  explosive eruption with a plume height ≥ that of V1477 or a tephra volume
  ≥ 0.5 km³, and no published reason (season, wind) makes Greenland fallout
  unlikely: then 1453's 1.23× particle level argues against it.
- d = **neutral** if the comparison is unfair (much smaller tephra volume,
  low plume, or effusive) — then particles say nothing.

**Verdict per candidate.**
- **refuted**: a = fail; or c = fail and d = fail.
- **weakened**: exactly one of c, d = fail, or c = weak and d = fail.
- **supported**: a = pass and c = pass and d not fail and b not against.
- **open**: everything else.
H5 as a whole moves to refuted only if every Icelandic candidate is refuted
and no undated or unlisted Icelandic eruption in the window can be excluded
by the annals; otherwise it stays or moves to weakened.

Fetch budget ~35. Downloads in `data/` (ignored).

## How to run

```
python3 -I katla14.py dates.csv ../03-latitude-posterior/data/evolv2k_v4.tab \
    ../02-ice-onset/data/abbott_supp/tsv/sheet7.tsv > results/katla14.txt
python3 -I annals_gap.py data/vedur_annalar.txt > results/annals_gap.txt
python3 -I fetch14.py data <name> <url>      # re-download any source in the provenance table
```
`dates.csv` was written by hand from the sources below (an LLM read them; the
scripts only compute). Standard library only.

## Sources read

- **Larsen, G. 2000.** Holocene eruptions within the Katla volcanic system,
  south Iceland. *Jökull* 49: 1–28. `SCHOLARLY`. Page images and OCR text
  from timarit.is `/files/` (the `/page/` viewer returns 403; `/files/<id>`
  does not). Table 1, p. 5, read from the page image.
- **Icelandic Volcanoes Catalogue (IVC)**, icelandicvolcanoes.is, JSON API
  `api/eruptions/search?country_name=Iceland` (99 eruptions; Katla, Hekla,
  Grímsvötn, Bárðarbunga, Eyjafjallajökull) and `api/catalog/KAT/en`.
  Maintained by the Icelandic Met Office and University of Iceland, with
  Larsen 2000/2010 as its Katla references. `SECONDARY` (expert-curated database).
- **Abbott et al. 2021**, *Clim. Past* 17: 565 (cached by 02). `SCHOLARLY`.
  p. 568 on how V1477 was dated; p. 569 TUNU2013 position; p. 571 particle timing.
- **Gudmundsson, Larsen, Höskuldsson & Gylfason 2008**, Volcanic hazards in
  Iceland, *Jökull* 58: 251. `SCHOLARLY`. Table of fatal eruptions.
- **Larsen, Gudmundsson & Björnsson, EGU 2005** abstract 10066. `SCHOLARLY` (abstract).
- **Guðjónsson, S. Þ.** (transcriber), *Íslenskir annálar og aðrar gamlar
  veðurheimildir* ("Icelandic annals and other old weather sources"),
  vedur.is. `SECONDARY` (a transcription of the annals' weather entries,
  with a source introduction after Árni Hjartarson, Hermann Pálsson and Astrid Ogilvie).
- **Einarsson, Larsen & Thorarinsson 1980**, The Sólheimar tephra layer and
  the Katla eruption of ~1357, *Acta Naturalia Islandica* 28. `SCHOLARLY`.
  Read for annal practice only.
- **eVolv2k v4** (PANGAEA.971968, cached by 03) and **Abbott 2021 Table S7** (cached by 02). `PRIMARY` (data).

## Results

### a. Own date (`dates.csv`, `results/katla14.txt`)

**Which GVP row is which layer.** Larsen 2000 Table 1 (p. 5) lists the
historical Katla eruptions, youngest first. For the 15th century it gives
four lines: "Katla~ 1500\*", "Katla 15. cent", "Katla~ 1440\*", "Katla
1416○". The key reads: "○ as summarized by Thorarinsson (1975) … \* Larsen
(1984)". The "~" marks an approximate date. So 1416 is a documented
(annal) eruption. ~1440 and ~1500 are tephra layers that Larsen dated in
1984. The "15. cent" layer is undated, and Table 1's order puts it between
~1440 and ~1500. The text (p. 6) says: "The maximum observed frequency is
three eruptions in the 15th and 17th centuries." GVP has four Katla rows in
the century: 1416 (reported), 1440 (VEI 4, "Observations: Reported"),
1450 ± 50 (tephrochronology) and 1500 (VEI 4, tephrochronology). Matching
them to Larsen's lines leaves **GVP 1450 ± 50 = Larsen's undated "15th
century" layer**. The ± 50 is the century itself, not a measurement.
IVC carries the same layer as **KAT_1480, 1480 ± 20, Tephrochronology,
"Small"** (ref. Larsen 2000), and ~1440 as **KAT_1440, 1440 ± 20,
Tephrochronology, "Small"**. The mapping is an inference (`likely`). No source
read states it.

**How the dates were made.** Larsen 1984 (*JVGR* 22, not read) dated
tephra layers by soil accumulation rates between dated markers. Abbott 2021
(p. 568) says this gave V1477 "an age of 1480 CE ± 11 years based on soil
accumulation rates between dated tephra layers (Larsen, 1984)". A
documentary date later replaced it: a votive letter of 11 March 1477. That
is the method's one calibration we have: off by 3 years with a stated ± 11.
The same method is inferred for K~1440 and K~1500, but not read.

GVP's "Observations: Reported" and VEI 4 for Katla 1440 conflict with
Larsen 2000 (the date comes from tephra, not a document) and with IVC
("Small", no VEI). I treat the GVP label as an error (`likely`).

| Candidate | Basis | Implied range | a |
|---|---|---|---|
| Katla ~1440 | soil-rate (Larsen 1984 via Larsen 2000; IVC ± 20) | 1420–1460 | neutral (contains 1452–53, 40 yr wide) |
| Katla 15th-c layer = GVP 1450 ± 50 | marker/catalogue (IVC 1480 ± 20) | 1460–1500 | **fail** |
| same, Larsen's stratigraphy only (sensitivity) | between K~1440 and K~1500 | 1420–1505 | neutral |
| Hekla 1440 | GVP row only; no primary source; absent from IVC (Hekla 1389, then 1510) | none | neutral |
| Grímsvötn 1450 ± 10 | "Sidereal: Ice Core", probably Vatnajökull glacier tephra, basis unread | 1440–1460 | neutral (would be pass if the glacier chronology is independent of Greenland) |
| Grímsvötn 1430 ± 10, 1469, 1470 ± 10 | same | 1420–1440, 1469, 1460–1480 | neutral (each would be fail) |

No Icelandic tephra between 1440 and 1470 has a published date that puts
it at 1452–53 to better than ± 20 years.

### b. The annals (`results/annals_gap.txt`)

No record of any 1452–53 Icelandic eruption was found. That silence carries
almost no weight:

- **The annals stop in 1430.** Nýi annáll (the "New Annal") "er
  samtímaheimild 1393-1430" ("is a contemporary source for 1393–1430").
  Gottskálksannáll, written in Skagafjörður in the 16th century, reaches 1578,
  but "lítið er um veður í honum fyrr en um 1560" ("there is little about
  weather in it before about 1560"). It is "fyrsti annállinn eftir að ritun
  annála hefst að nýju eftir eyðu fimmtándu aldar" ("the first annal after
  annal-writing resumes after the fifteenth-century gap"). (Guðjónsson,
  introduction.) The transcription's weather entries: 16 of 31 years in
  1400–1430, **0 of 42 years in 1431–1472**, and 5 of 48 in 1473–1520.
- **Calibration: the largest eruption of the century is missing from the
  annals too.** V1477 (10–11 km³ of tephra, VEI 5–6, "Largest known" in IVC)
  "was thought to have not been mentioned in written sources". It is dated
  only by a votive letter about ash fall in Eyjafjörður (Abbott 2021 p. 568).
  The Larsen 2000 Table 1 entries ~1440, 15th c. and ~1500 are tephra-only.
  They are known from the ground, not from the annals.
- Gudmundsson et al. 2008 (Table, Jökull 58): "Pre–1500 AD record highly
  uncertain"; for 900–1500, "Indirect evidence and annals".

So b = neutral for every candidate. Wall: Storm's 1888 edition of
Gottskálksannáll for 1450–55 was not reached (archive.org search did not
find it). Its eruption entries, if any, are unread.

### c. Size and pattern (`results/katla14.txt`)

eVolv2k v4 lists 15 named Icelandic eruptions (ice-derived, the same method
that gives 1453 its 9.97 Tg S).
- Every unipolar Icelandic row has S = 0.190 × Greenland deposition (n 14,
  range 0.188–0.191). Treated as Icelandic, with no Antarctic part, 1453's
  Greenland 24.8 kg km⁻² gives **4.7 Tg S**, not 10. The 10 Tg figure
  assumes the bipolar pattern is real.
- Icelandic eruptions at ≥ 3.8 Tg S (the pre-registered bar): Laki 1783
  (20.8), Eldgjá 939 (16.2), Grímsvötn 751 (6.8), Veiðivötn 1477 (5.1),
  Hrafnkatla 763 (4.8), Katla 823 (3.9). All six carry "Tephra lay = Y"
  in eVolv2k: their glass has been found in Greenland ice. 1453 is "N", and
  canon says nobody has searched the 1453 layer.
- **Katla scale.** Katla 1755 was the largest historical Katla eruption
  (≤ 1.5 km³; Larsen 2000 abstract). It gave 1.18 Tg S and 6.2 kg km⁻² in
  Greenland. 1453's Greenland deposition is 4.0× that. Katla 1625
  (0.5–0.7 km³) and 1918 (0.7 km³, 14 km column) are not in eVolv2k at all.
  Neither are Hekla 1104 (VEI 5), Hekla 1300 or Öræfajökull 1362. IVC
  defines a "Small" Katla eruption as "tephra fallout <0.1 km³ … The height
  of the eruption column unlikely to exceed 11 km". Both 15th-century Katla
  candidates are "Small". **c = fail for both Katla candidates.**
- **Hekla.** The system's maximum in eVolv2k is 2.52 Tg S (1766), below the
  bar. **c = fail.**
- **Grímsvötn.** Excluding the Laki flood-lava type, the system maximum is
  6.8 Tg S (751). The size clause passes, but this is lenient, because GVP
  gives the window rows no size.
- **Pattern.** 1 of 15 Icelandic rows has any Antarctic deposition
  (Hrafnkatla 763, 1.0 kg km⁻²). 1453 has 5.1. An Icelandic source needs
  1453's Antarctic signal to be a second eruption or noise. Pattern against
  → c = weak where it would otherwise pass.

### d. Ash: is the V1477 comparison fair for Katla? (`results/katla14.txt`)

- **Distance:** fair. Katla is 1678 km from TUNU2013, against 1587 km for
  Veiðivötn (1.06×). Hekla is 1.03× and Grímsvötn 1.02×.
- **Size and plume:** not fair for the dated Katla candidates. V1477 erupted
  10–11 km³ with a main-phase column "> 18 km" (Abbott 2021 p. 568, after
  Larsen 2005). A "Small" Katla eruption is < 0.1 km³, with a column unlikely
  to exceed 11 km. That is about 100× less tephra. A V1477-sized particle
  spike is not expected, so d = neutral.
- **Season:** different, direction unknown. V1477 was in winter
  (February). All Katla eruptions with a known season began May–November
  (Larsen 2000 p. 5). No source read gives seasonal wind statistics toward
  NE Greenland, so season is noted, not weighed.
- **Post hoc, not in the verdict.** Abbott 2021 Table S7 gives a second,
  rougher calibration. 1497 has nssS 44 ng/g (2.4× median) and particles
  2.89×. Its date fits Katla ~1500 ± 5 (IVC "Large", 0.5–0.7 km³). The
  eruption is not attributed in eVolv2k and the match is unproven. 1453 has
  more sulfate (73 ng/g, 4.0×) but particles of only 1.23×. If 1497 is
  Katla ~1500, then even a mid-sized Katla eruption leaves ~3× particles at
  TUNU2013 with less sulfate than 1453. That argues against any Katla
  eruption large enough to supply 1453's sulfate. Particle peaks of ~3× with
  no sulfate are common (1468, 1485, 1490), so one coincidence proves little.
- The only open way round the particle result: an eruption sulfate-rich but
  tephra-poor, like a flood-lava fissure (Laki-type), or one whose plume went
  away from NE Greenland. A Laki-type 15th-century lava would be a large,
  mapped flow. None appears in the lists read (unverified; Thordarson &
  Larsen 2007 not read).

### Verdicts (pre-registered rule; `results/katla14.txt`)

| Candidate | a | b | c | d | Verdict |
|---|---|---|---|---|---|
| Katla ~1440 (GVP Katla 1440) | neutral | neutral | fail | neutral | **weakened** |
| Katla 15th-c layer (GVP Katla 1450 ± 50), IVC date | fail | neutral | fail | neutral | **refuted** |
| — same, stratigraphy only (sensitivity) | neutral | neutral | fail | neutral | weakened |
| Hekla 1440 | neutral | neutral | fail | neutral | **weakened** |
| Grímsvötn 1450 ± 10 | neutral (pass if basis independent) | neutral | weak | neutral | **open** |
| Grímsvötn 1430 ± 10, 1469, 1470 ± 10 | neutral (fail if basis independent) | neutral | weak | neutral | open (each would be refuted on its own date) |

The "refuted" for GVP Katla 1450 ± 50 rests on IVC's 1480 ± 20, whose basis
is not published in anything read. On Larsen's stratigraphy alone it is
weakened. Either way, the rule cannot return open for a Katla candidate:
both are "Small", and Katla's largest historical eruption gave a quarter of
1453's Greenland sulfate.

**H5 as a whole:** per the pre-registered H5 clause, not refuted. The named
Katla and Hekla rows fail on size. Grímsvötn 1450 ± 10 stays open because its
date basis and size are unknown. An unlisted Icelandic eruption cannot be
excluded, because the annals are silent for 1431–1472. On the evidence, an
Icelandic source must meet four conditions:
(i) ≥ ~4.7 Tg S, larger than any Icelandic eruption since 1477;
(ii) unrecorded in the tephra catalogues for the window;
(iii) little coarse ash at TUNU2013;
(iv) a separate source for the Antarctic 5.1 kg km⁻².

## Limits

- Larsen 1984 (*JVGR* 22), Larsen 2010 (DQS 13), Thordarson & Larsen 2007
  (*J. Geodyn.* 43), Óladóttir et al. 2005/2008, Larsen et al. 1998
  (*Geology* 26), Thorarinsson 1975 (*Annáll Kötlugosa*, "An annal of Katla
  eruptions") and Storm 1888 were not read: they are paywalled or
  403, or no copy was found. The soil-rate errors for K~1440 and the
  15th-century layer are IVC's, not a paper's.
- The GVP 1450 ± 50 → "15th century" layer mapping is by elimination.
- The size test uses eVolv2k's ice-based S, which already depends on Greenland
  deposition. It is a scale check, not a dating input, so there is no leakage.
- One soil-rate calibration case (V1477), one particle calibration (V1477),
  and one post hoc, unattributed second case (1497).
- Hekla 1440 has no primary source at all. Its "weakened" rests on the
  Hekla system's eVolv2k maximum.

## Unverified claims

- Larsen 1984 dated K~1440 and K~1500 by soil accumulation rates (inferred
  from Abbott 2021's description of the same paper's V1477 date).
- GVP's Grímsvötn "Sidereal: Ice Core" rows are Vatnajökull glacier tephra
  (Larsen et al. 1998) dated independently of Greenland (from 06; the paper is unread).
- No Laki- or Eldgjá-type flood lava erupted in Iceland in the 15th century.
  From memory; Thordarson & Larsen 2007 not read.
- Laki 122 Mt SO₂ and Eldgjá 219 Mt SO₂ petrologic yields. IVC gives "219"
  as `volatile_content_so2` for KAT_939 with no unit; Laki is from memory.
  Not used in the tests.
- Gottskálksannáll has no eruption entry for 1450–55 (only the weather
  transcription was read).

## Provenance

| File (data/, ignored) | URL | sha256 (first 12) |
|---|---|---|
| larsen2000/t_450195NN.txt (OCR, 29 pages), p5.jpg (Table 1), tim_45019502.jpg (p. 1) | https://timarit.is/files/45019505 … 45019645 step 5; /files/45019522; /files/45019502 | p5.jpg 014f8dd20443; t_45019520 ac509f1bf0c4; t_45019525 048721d9d3bb; t_45019545 58075e83999b; t_45019595 0423594a17ea; p1 8d9c757b1a9f |
| ivc_eruptions_iceland.json | https://icelandicvolcanoes.is/api/eruptions/search?country_name=Iceland | 7954de0d30bf |
| ivc_cat_KAT.json | https://icelandicvolcanoes.is/api/catalog/KAT/en | 8674dd5e1b99 |
| vedur_annalar.pdf | https://www.vedur.is/media/vedurstofan/utgafa/hlidarefni/annalar_sig-th.pdf | c77c2db1b12b |
| gudmundsson2008_jokull58.pdf | https://people.wou.edu/~taylors/gs104/2008jokull58_mtgetal_volchaz.pdf | e0d833bd3cf1 |
| egu05_10066.pdf | https://www.meetings.copernicus.org/www.cosis.net/abstracts/EGU05/10066/EGU05-J-10066.pdf | 1c8bd6cac247 |
| ani28.pdf (Einarsson et al. 1980) | https://utgafa.ni.is/Acta-Naturalia-Islandica/Acta-Naturalia-Islandica-28.pdf | 2c95c1ab795f |
| (02) abbott2021.pdf | cached in ../02-ice-onset/data/lit/ | 46077bbefdfa |
| (03) evolv2k_v4.tab | cached in ../03-latitude-posterior/data/ | 468deb979038 |
| (02) abbott_supp/tsv/sheet7.tsv | cached in ../02-ice-onset/data/ | — (02's xlsx 7b9f4b43…) |

Failed: timarit.is `/page/` (403, also through WebFetch), Springer
Óladóttir 2011 (HTML paywall), GSW *Geology* 26:943 (403), Edinburgh Pure
Thordarson & Larsen 2007 (no file), opinvisindi.is bitstream (timed out),
Tephrabase (no 15th-century records), archive.org (Storm 1888 not found).
About 34 fetches.
