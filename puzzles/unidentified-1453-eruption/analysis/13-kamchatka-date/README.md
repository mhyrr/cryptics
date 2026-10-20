# 13 — Kamchatka and Kurils: own date and size

**Question.** If a Kamchatka or Kuril volcano made UE 1453 (~10 Tg S, onset
about 1452.9–1453.5), then (a) its own tephra must date to about 1452–53
from brackets in Kamchatka sections, with no polar ice in the chain, and
(b) its volume and magma must allow ~10 Tg S. Do the candidates in 06's top
30 pass either test?

## Pre-registration (written 2026-10-20, before any model in this folder was run)

What I knew when I wrote this: 06's ranking and README; 11's model, its
known-case failure for below-only data, and its verdict; GVP rows for
Kamchatka and the Kurils 1300–1600; and, from the reading in step 1, the
dates and volumes listed in "What was found" below. I had not run any model
or size calculation.

**Candidates** (06 headline, Kamchatka/Kurils rows in the top 30):
Karymsky 1450 (rank 6), Khangar 1500 ± 40 (12), Maly Semyachik 1400 ± 50
(13), Sashiusudake [Baransky] 1460 ± 30 (23, Iturup, Kurils). The AIST
southern-Kuril rows (Tiatia Ty-Sa/Sb/Na, Moyorodake Pereval) carry uniform
700-yr ranges and fall below rank 25; they are listed, not modelled.

**Date model.** 11's one-event model (`../11-aniakchak-date/bracket_model.py`,
reused unchanged), IntCal20, flat prior 1300–1800 CE, 0.1-yr grid. 11's
material rules apply, with one addition for Kamchatka soil-pyroclastic
sections: an age on the humic (alkaline-extract) fraction of a buried soil
directly under the tephra is a `below` date (soil carbon accumulates before
burial; root intrusion can make it too young, which the paper flags where it
applies). MAIN: every such date `below`. S1: the soil-top date treated as
`same` (the authors' own reading: soil top ≈ eruption). S2: drop dates the
authors flag as contaminated. S3: gap model, each `below` date at T − U(0, G),
G = 50 and 200 yr (pre-registered here, unlike in 11).

**Date decision rule.** 11's rule on MAIN (refuted / weakened / supported /
not excluded, with P = P(1451 ≤ T < 1454) and B = 3 / HPD width). But: if the
data configuration (below-only) fails its known-case test, the rule's output
is reported and **not adopted**; the date test is then "uninformative", and
the verdict rests on the size test and on the absence of a dated unit.

**Known-case test** (run before the candidate result is read): (a) 11's
synthetic below-only and two-sided cases, re-run; (b) a synthetic case built
to mimic the Karymsky configuration: one soil-top humic date, true calendar
offset U(0, 100) yr before the event, 14C error 30, scored as MAIN (below)
and as S1 (same). Pass = 95 % HPD covers the true date in ≥ 90 % of trials.

**Size rule.** P(VSSI ≥ 6.90 Tg S | VEI, class "other") from 06's size model
(`../06-candidate-ranking/pipeline.py`, `SizeModel`), recomputed here.
- **refuted on size**: a primary source gives the eruption (or the whole
  eruptive cycle that contains it) a volume < 0.1 km³ of tephra (VEI ≤ 3),
  and the magma is not a rift basalt;
- **weakened on size**: VEI 4 (0.1–1 km³), or no published volume and no
  mapped regional tephra for the unit;
- otherwise not excluded.

**Verdict per candidate**: the worse of the date and size outcomes, except
that an uninformative date test cannot weaken anything by itself.

## Run

```
python3 -I knowncase13.py ../06-candidate-ranking/data/intcal20.14c ../11-aniakchak-date/knowncase.csv > results/knowncase13.txt
python3 -I run13.py ../06-candidate-ranking/data/intcal20.14c brackets.csv > results/run13.txt
python3 -I size13.py ../../sources/cache/gvp_holocene_eruptions.csv ../06-candidate-ranking/data/gvp_holocene_volcanoes.csv ../03-latitude-posterior/data/evolv2k_v4.tab > results/size13.txt
python3 -I fetch13.py <outfile> <url>      # downloads used here; prints sha256
```

Standard library only. IntCal20 and the GVP volcano table come from 06
(`python3 -I fetch.py data` there). The bracket model is 11's
`bracket_model.py`, imported unchanged; the size model is 06's
`pipeline.SizeModel`, imported unchanged. `data/` is gitignored. Runtime ~15 s.

## Sources and what was found (step 1–2)

### Karymsky "1450" = onset of the IIKM cycle (no named unit)

- **What the GVP row is.** Braitseva & Melekestsev (1990, Bull. Volcanol. 53,
  p. 199 Table 1 and IIKM section): "New activity of the volcano (the IIKM
  cycle) started about 500 B.P.", on "a calibrated time scale based on the
  tables of Arslanov (1978)" (p. 2). 500 cal BP = 1450 CE. GVP's separate
  1550 row is "Tephra layer PM7"; the 1450 row names no unit. It is the first
  tephra of the cycle, above a thick buried soil. `SCHOLARLY`.
- **Not a KRM unit.** KRM is the ~7700–7900 14C BP caldera-forming tephra
  (8–10 km³; Braitseva 1995 Table 2; 1997 Table 1). The ~1450 event is a
  cone eruption, far smaller.
- **The dates.** Braitseva, Egorova & Sulerzhitsky (1979, Vulkanologiya i
  Seismologiya 1979(1): 48–58, p. 56; Figs. 1 and 3), section 283 at the
  south foot. The period the 1979 paper calls KM3 is the 1990 paper's IIKM. Quotation and translation:
  > «Для образца из верхней части почвы по трем последовательным щелочным
  > вытяжкам получены даты 450 ± 30, 770±90, 870±50 лет. Возможно, дата по
  > первой вытяжке (450 ± 30 лет) несколько омоложена за счет проникновения
  > современных корней в верхнюю часть разреза.»
  > "For a sample from the upper part of the soil, three successive alkaline
  > extracts gave dates of 450 ± 30, 770 ± 90 and 870 ± 50 years. The date from
  > the first extract (450 ± 30) may be somewhat too young because modern
  > roots penetrated the upper part of the section."
  The soil lies under the first KM3 tephra (Fig. 1, column 283; Fig. 3). A
  thin black-sand layer ("ч") sits between the dated soil top and the KM3
  pumice. No lab codes are printed. The radiocarbon co-author is Sulerzhitsky
  (GIN Moscow, inferred). **No date above the unit exists in the open sources.** Fig. 3
  has no age inside or above KM3. `SCHOLARLY`.
- **Size.** Braitseva & Melekestsev (1990, p. 199 text; Table 3, p. 203):
  IIKM eruptions are "separate moderate-strength eruptions". "The strongest
  eruptions occurred at 400 and 200–250 B.P., and historically in 1961–1981
  ... with eruptive volumes of 0.15; 0.12, and 0.19 km3". Table 3 (read as
  image): pre-historic IIKM (PM7–PM10, lavas VIII, IX) pyroclastics
  **0.07–0.09 km³ in total**; the whole 500-yr IIKM cycle, 0.13–0.15 km³.
  Composition: andesite (57–64 % SiO2). So the ~500 BP onset eruption had
  < 0.09 km³ of pyroclastics: VEI ≤ 3. Dispersal of the onset tephra is not
  mapped. `SCHOLARLY`.

### Khangar 1500 ± 40

- Primary source not found. Khangar's key marker is KHG, 6900–7000 14C BP,
  > 10 km³ dacite (Braitseva 1995 Table 2; 1997 Table 1: 6957 ± 30, 12–13 km³;
  Kyle 2011: 6850 14C BP crater). KHG is not the 1500 CE event. A secondary
  site (VolcanoDiscovery, `POPULAR`) calls ~500 yr ago "the youngest known
  eruption from the Sredinny Range volcanoes". No volume, unit or
  dispersal for it is published in what I read. The JPL AVA page
  (`SECONDARY`, via search) notes that Sredinny volcanoes are less mantled
  by Holocene tephra, so their young ages are poorly fixed.

### Maly Semyachik 1400 ± 50 (Crater V, Kaino-Semiachik)

- Primary source not opened: Braitseva et al. (1978a, b), Selyangin &
  Braitseva (1991, Active Volcanoes of Kamchatka vol. 2, pp. 160–179);
  repo.kscnet.ru/1402 holds a record with no file. Maly Semyachik is not
  among the 15 regional key markers (Braitseva 1997). GVP gives its later
  Troitsky-crater eruption (1550) VEI 4 and the volcano's rock type as basalt.
  No volume for the 1400 event.

### Sashiusudake [Baransky] 1460 ± 30 (Iturup, Kurils)

- GVP method "14C (uncalibrated)"; source unknown (GVP pages 403 in 06).
- JMA *National Catalogue of Active Volcanoes of Japan*, Sashiusudake
  (agency, `SECONDARY`): "Tephra stratigraphy of the volcano base has
  identified 10 layers of eruption deposits, from Ba-1 (1770 cal. yBP) to
  Ba-10 (7500 cal. yBP)" (citing Razzhigaeva et al., submitted). The only
  historical event is a possible small explosion in 1951. So no tephra younger
  than ~180 CE has been recognised at the volcano's own base. A 1460 eruption,
  if real, left no mapped fall.

### Is there a "1450" marker, and how is it dated? (leakage check)

- **SH1450 is a Shiveluch tephra of 1450 14C yr BP**, not 1450 CE. Kyle et
  al. (2011, IGR 53, Table 1 header "Age (14C BP) ... SH1450 1450"). This is
  about 600 CE calendar. Its age comes from 14C on Shiveluch proximal
  sections (Ponomareva et al. 2007b). Kamchatka marker codes of the form
  SHnnnn give 14C ages, except where a historic year is meant (SH1964, SH1854).
  `SCHOLARLY`.
- **No polar ice in any chain used here.** The Karymsky dates are soil
  humics. The Shiveluch chronology (Ponomareva et al. 2015) is an OxCal
  Bayesian model of 113 proximal plus 76 marker-tephra 14C dates on IntCal13.
  It does not import ice ages. The leakage rule removes nothing.

### Step 4: any Kamchatka tephra of ~VEI 5 or > 1 km³, 1350–1550 CE?

- **Regional key markers: none.** Braitseva et al. (1997, Quat. Res. 47,
  Table 1) list 15 Holocene key-marker tephras. The youngest prehistoric one is
  SH2, 965 ± 16 14C BP (≥ 2 km³; about the 11th–12th c. CE). Then come
  historic SH1964, B1956 and KSht3 (1907). Braitseva (1995, Table 2) gives the
  same list with volumes; the only other young unit, Ksudach-Shtyubel KS-SHT
  (1000–1100 14C BP, 0.8 km³), is also older. `SCHOLARLY`.
- **Shiveluch, not in 06's list: unit 5.** Ponomareva et al. (2015, IJES 104,
  Table 1 p. 1465): unit 5, fall + ignimbrite ("f, i"), **553 cal BP ≈ 1397
  CE** (modelled; uncertainty is in Online Resource 3, not obtained),
  dispersal N. Bracketed by SH1 (unit 4, 310 cal BP ≈ 1640 CE) and SH2 (unit 6,
  764 cal BP ≈ 1186 CE). Shiveluch Plinian eruptions of ≥ 0.6 km³ "have
  occurred at least 23 times during the Holocene" (Kyle 2011, p. 1063). Unit 5
  has no published volume. Its modelled age is 56 yr before 1453. GVP's
  "Sheveluch 1430, VEI 4, Tephra layer SH2a" may be the same eruption, but I
  have not verified that. 06's filter (1440–1470) excluded it.
- **Krasheninnikov, 15th century** (Wikipedia, `POPULAR`, via search):
  1423–1503 or 1463 ± 40. GVP's 1550 row is basalt and effusive. Not a 10 Tg S
  candidate on present evidence.
- **Analogue from the Kurils.** eVolv2k v4 lists "Zavaritskii-Simushir Island
  (Kurils)" 1831, VSSI 12.0 Tg S, with **no GVP row** (`results/size13.txt`).
  Hutchison et al. (2025, PNAS 122(1)) identified it from ice-core glass
  (`SCHOLARLY`, read at search-summary level only). Together these show that a
  ~10 Tg S eruption in the central Kurils can be missing from every
  volcano catalogue until glass finds it.

## Known-case test (`results/knowncase13.txt`, run before `run13.py`)

| Test | Coverage of 95 % HPD | Pass? |
|---|---|---|
| 11 synthetic, 2 below + 2 above | 58/60 | pass |
| 11 synthetic, 3 below only | 13/60 | **fail** |
| Karymsky-like: 1 soil-top date, offset U(0,100), scored `below` | 52/60 | fail (< 54) |
| same, scored `same` (Braitseva's reading) | 29/60 | **fail** |
| same, scored `gap50` / `gap200` | 43/60 / 58/60 | fail / pass |
| Loch Portain, Hekla 1510 (11, K2) | HPD 1331–1622 contains 1510.56 | pass |

Reading. The Karymsky configuration (one soil sample, below only, no upper
bracket) fails its known-case test as MAIN. Read as contemporaneous, the
soil top excludes the truth half the time. Only the wide gap model (G = 200)
is calibrated, and it is post hoc in spirit. As pre-registered, the date
rule's output is reported and **not adopted**.

## Results

### Date (`results/run13.txt`), Karymsky IIKM onset

| Run | 95 % HPD (CE) | P(1451–1454) | P/B | Rule output |
|---|---|---|---|---|
| MAIN, 3 below | 1460–1800 | 0.006 | 0.72 | "refuted" (not adopted: known case fails) |
| S1, 450 ± 30 as `same` | 1414–1479 | 0.073 | 1.59 | not excluded |
| S2, drop 450 ± 30 | 1326–1800 | 0.006 | 0.97 | not excluded |
| S3, G = 50 | 1330–1334, 1405–1438 | 0.000 | 0.00 | "refuted" (mis-specified: the three extracts of one soil span ~400 14C yr by design, so a 50-yr gap cannot hold for the deeper two) |
| S3, G = 200 | 1419–1469 | 0.086 | 1.41 | not excluded |

- The soil-top humic fraction (450 ± 30) is older than 1454.0 with P = 0.78
  (IntCal20 at 1453.0 = 423 ± 10 BP). A 1453 burial is fully consistent with it.
- Reading: the Karymsky date test is **uninformative but compatible**. The
  authors' own reading (S1) puts the onset at 1414–1479 CE, with 1453 inside.
  Nothing in the date excludes it.

### Size (`results/size13.txt`)

P(VSSI ≥ 6.90 Tg S | VEI, class other), counted from eVolv2k v4 named
events 1500–1899 against GVP (06's model, recomputed):

| VEI | P | numerator events |
|---|---|---|
| 3 | 0.0015 | none of 324 |
| 4 | 0.027 | Colima 1585 (8.5), Ruiz 1595 (8.9), both tropical |
| 5 | 0.119 | Cosigüina 1835, Parker 1640 |
| 6 | 0.50 | Krakatau 1883, Huaynaputina 1600 |

Likelihood ratio VEI 3 : VEI 5 = 0.013. VEI 4 : VEI 5 = 0.22. A VEI 4
andesite is not impossible: two of 93 reached the threshold. A VEI 3 has no
precedent.

### Verdict per candidate

| Candidate | Unit | Date test | Size test | Verdict |
|---|---|---|---|---|
| **Karymsky 1450** | IIKM/KM3 onset tephra, unnamed (andesite) | uninformative; compatible (S1 1414–1479) | < 0.09 km³ pyroclastics (whole cycle 0.13–0.15 km³): VEI ≤ 3 → **refuted on size** | **refuted** |
| Khangar 1500 ± 40 | unnamed (not KHG) | no brackets found | no volume, no mapped tephra → weakened | **weakened** |
| Maly Semyachik 1400 ± 50 | Crater V, Kaino-Semiachik (basalt per GVP) | no brackets found | no volume, not a key marker → weakened | **weakened** |
| Sashiusudake 1460 ± 30 | none mapped | no brackets; no tephra < 1770 cal BP at base (JMA) | no fall deposit known → weakened | **weakened** (close to refuted: the eruption has no deposit at its own base) |
| AIST S. Kurils (Tiatia, Moyorodake) | Ty-Sa/Sb/Na, Pereval | 700-yr catalogue ranges | not assessed | unchanged |

**Strongest surviving Kamchatka/Kurils candidate:** none among 06's named
rows. The best open lead is **Shiveluch unit 5** (modelled ~1397 CE, fall +
ignimbrite, dispersal N, volume unknown), which 06 did not score. Its
modelled age sits 56 yr early. Whether 1453 lies inside its 95 % range
depends on Online Resource 3, which I could not get. The other open lead is
regional: **an unmapped central-Kuril caldera**, on the Zavaritskii-1831
precedent.

## Limits

- Karymsky has one dated soil sample, three humic fractions, no lab codes, no
  upper bracket. The size test does all the work for Karymsky. If Table 3's
  volumes are badly underestimated (distal ash missing), the verdict would
  weaken. The paper mapped 40 sections and calls the eruptions
  "moderate-strength".
- The size model counts VEI against VSSI. The rule also leans on GVP VEIs for
  1500–1899; an unrecognised VEI 3 high-S event would raise P(VEI 3).
- Khangar, Maly Semyachik and Sashiusudake verdicts rest on the *absence* of
  published volumes or deposits. That is weaker than a measured small volume.
- Shiveluch unit 5's age uncertainty and volume were not obtained. OceanRep
  served a bot challenge for the supplementary archive (`data/si/` holds that
  HTML, not data).
- TephraKam (Portnyagin et al. 2020) tables were not read, as in 06.

## Unverified claims

- GVP's Karymsky 1450 row derives from Braitseva & Melekestsev (1990). Inferred from the matching "500 B.P." and
  calibrated scale; the GVP reference page is unreadable (403).
- The Arslanov (1978) calibration turns the 450 ± 30 soil-top age into
  "about 500 B.P." (inference: the paper does not show the step).
- Lab is GIN (Sulerzhitsky): inferred from authorship.
- GVP "Sheveluch 1430 SH2a" = Ponomareva 2015 unit 5: not checked.
- Hutchison et al. (2025): read as a search summary only. The eVolv2k v4 row
  (12.0 Tg S) is checked data.
- Krasheninnikov 15th-century dates: Wikipedia via search, not opened.
- Khangar "~500 years ago, youngest Sredinny eruption": VolcanoDiscovery only.

## Provenance

Fetched 2026-10-20 with `fetch13.py` (Python urllib) or WebFetch. Files in
`data/lit/` (gitignored).

| Source | URL | Tier | Read how | sha256 |
|---|---|---|---|---|
| Braitseva, Egorova & Sulerzhitsky 1979, Vulkanol. Seismol. 1979(1):48–58 | http://repo.kscnet.ru/2582/1/st1979-%E2%84%961.pdf | SCHOLARLY | full PDF; text p. 56; Figs. 1, 3 as images | 425a128b…1859e5b2 |
| Braitseva & Melekestsev 1990, Bull. Volcanol. 53:195–206 | 06 copy (`../06-candidate-ranking/data/lit/braitseva1990_karymsky.pdf`) | SCHOLARLY | text; Tables 1, 3 read as images | a187dfa4…5962d8 (06) |
| Braitseva et al. 1995, Bull. Volcanol. 57:383–402 | https://repository.geologyscience.ru/bitstreams/ee81ac5d-e751-4cc7-a3c2-20d5c54317d8/download | SCHOLARLY | full PDF, Table 2 | 167b716f…cf367329 |
| Braitseva et al. 1997, Quat. Res. 47:125–139 | https://repository.geologyscience.ru/bitstreams/e7383aec-b697-4916-8219-a1d4a21a8ab7/download | SCHOLARLY | full PDF, abstract and Table 1 | 08234f19…8edf3e2d |
| Kyle, Ponomareva & Rourke Schluep 2011, IGR 53:1059–1097 | https://repository.geologyscience.ru/bitstreams/11ab8044-cee2-428d-be60-b84ccf9d2b46/download | SCHOLARLY | full PDF, Shiveluch section, Table 1 | ae55a7e5…0680e049 |
| Ponomareva et al. 2015, IJES 104:1459–1482 | https://repository.geologyscience.ru/bitstreams/c8e7fde7-fc2e-419d-a573-9fac2e1bcb9a/download | SCHOLARLY | full PDF, Table 1 | abd4dc99…ae95c154 |
| JMA catalogue, 102 Sashiusudake | https://www.data.jma.go.jp/vois/data/filing/souran_eng/volcanoes/102_sashiusudake.pdf | SECONDARY (agency) | full PDF | 7983240d…34e31582 |
| Hutchison et al. 2025, PNAS 122(1) | https://research-portal.st-andrews.ac.uk/en/publications/the-1831-ce-mystery-eruption-identified-as-zavaritskii-caldera-si/ | SCHOLARLY | search summary only | — |
| VolcanoDiscovery Khangar, Baransky | https://www.volcanodiscovery.com/6081.html | POPULAR | search summary only | — |
| IntCal20; GVP tables; eVolv2k v4 | via 06 and 03 | PRIMARY | 06/03 data | see 06 README |

Fetched but not useful: the Gorshkov 1973 gravimetry paper on Maly Semyachik
(repository bitstream 38fae162…); Volynets et al. 2020, Sredinny Range K–Ar
(sibran.ru); repository landing pages (no files) for "Ages of active
volcanoes" 1995 and repo.kscnet.ru/1402.
Refused: oceanrep.geomar.de supplementary zip (bot challenge); Radiocarbon
archive at journals.uair.arizona.edu (HTTP 500).
