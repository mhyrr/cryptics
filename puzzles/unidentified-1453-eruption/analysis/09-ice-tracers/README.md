# 09 — Non-sulfur tracers in Greenland ice

**Question.** Do non-sulfur tracers in Greenland ice say what kind of eruption
UE 1453 was? Did its ash arrive before its sulfate?

Two parts. Part A tests the open NEEM-2011-S1 record. Part B looks for other
open sub-annual element or particle data for 1450–1455.

## Pre-registration (written 2026-10-20, before any feature was computed)

Fixed before running `tracers.py` on anything. Changes after the first run are
listed under "Changes after the first run" with the reason.

**Data.** NEEM-2011-S1 CFA, PANGAEA.940553 (the 02 download, read by path).
About 10 samples a year. Columns used: Cond, Acidity, Na, S, Ca, Mn, Sr, Ce.

**Calibration events.** Every eVolv2k v4 row with a named source, in the NEEM
range 86–1899 CE, Greenland deposition > 0, grouped by that row's location:

- ICE (Iceland): 751, 757, 763, 782, 823, 877, 939 (Eldgjá, listed as Katla),
  1477, 1510, 1721, 1755, 1766, 1783, 1873, 1875.
- NHX (other NH extratropical): 452 Shiveluch, 853 Churchill, 946
  Changbaishan, 1667 Tarumae, 1707 Fujisan, 1739 Shikotsu, 1831 Zavaritskii,
  1853 Toya, 1856 Hokkaido-Komagatake.
- TROP: 432 Ilopango, 1257 Samalas, 1585 Colima, 1595 Ruiz, 1600
  Huaynaputina, 1640 Parker, 1673 Gamkonora, 1815 Tambora, 1822 Galunggung,
  1835 Cosigüina, 1861 Makian, 1883 Krakatau.
- Left out: 1458 Kuwae (attribution contested, Ro 2025; and it is UE 1453's
  neighbour), 236 Taupō and 1886 Tarawera (Southern Hemisphere), and 87
  "Unidentifed". Katmai 1912 is not in eVolv2k (it ends in 1900). It runs as
  an extra, outside the calibration, because industrial sulfate swamps the
  background (02).

Hekla 1104 and Öraefajökull 1362 have no eVolv2k v4 row, so they have no
sulfate event to anchor. They are not used. Shiveluch 1854 has no v4 row
either and 02 found no sulfate onset. Not used.

**Event window.** Y is the eVolv2k year. nssS = S − 0.084 Na (as 02).
Background is the samples in [Y − 8, Y − 0.5). One pass drops background
samples above the background's own threshold, to remove earlier eruptions.
Threshold = median + 3 × 1.4826 MAD. Sulfate onset = first sample in
[Y − 0.5, Y + 2) that starts three consecutive samples above threshold. Event
interval = onset until three consecutive samples fall below threshold, at
most 3 yr. Events with no onset are reported and dropped.

**Seasonal cycle.** Two methods, both fixed here.
1. *Ratio residuals* (no seasonal model needed). Fit OLS log10(X) = a + b
   log10(Ca) on background samples. The residual has the dust cycle removed,
   because dust drives X and Ca together. Pairs: Ce|Ca, Mn|Ca, Mn|Ce, Ce|Sr.
2. *Load anomalies.* Subtract from log10(X) the background median of its
   NS1-2011 two-month bin (six bins). Species: Ce, Mn, Ca.

Each series becomes a z-score against the background (median, 1.4826 MAD),
then a 3-sample running mean.

**Features per event.**
- `r_CeCa`, `r_MnCa`, `r_MnCe`, `r_CeSr`: the running-mean z of the ratio
  residual with the largest absolute value in [onset − 1, onset + 1], signed.
- `a_Ce`, `a_Mn`, `a_Ca`: the largest running-mean load z in the same window.
- `acid`: ΣΔAcidity / (2 ΣΔnssS / 32.06) over the event interval, Δ being
  the excess over the background median. 1 means acidity equals sulfuric acid
  alone. Above 1 means extra acid (HCl, HF, HNO3). Below 1 means
  neutralisation (ash, NH4) or an acidity gap.
- `cond`: ΣΔCond / ΣΔnssS over the event interval.
- Lithic timing: the first sample in [onset − 1, onset + 1] where the
  running-mean load z of Ce (and separately Mn) exceeds 3. Lag = that time −
  sulfate onset, in years. Negative means ash before sulfate.

**Tests, in this order.**
1. Per feature: AUC, ICE vs DISTANT (NHX + TROP), with a two-sided
   permutation p (10,000 label shuffles, seed 1453). Holm correction across
   the nine features.
2. Combined: nearest-centroid classifier on all nine features, z-scored
   inside each leave-one-out fold. Report LOO balanced accuracy and a
   permutation p (2,000 shuffles, LOO rerun on each).
3. Decision rule. **Iceland separates** if LOO balanced accuracy ≥ 0.75 and
   permutation p < 0.05. Otherwise it does not, and the UE 1453 placement is
   reported as a description only.
4. Sensitivity: the same tests on events after 1500 only. Most of the early
   Icelandic attributions come from tephra found by sampling particle peaks
   (Plunkett 2023), which could bias them toward a lithic signal.
5. Secondary: NHX vs TROP, same tests.
6. Only after 1–5 are printed: UE 1453 with Y = 1453. Its features, its
   rank in each class, the classifier's label, and its five nearest
   calibration neighbours.

**Expected from the literature, written down so a surprise is visible.**
Plunkett 2023 (abstract) reports Icelandic particles synchronous with
sulfate, Alaskan particles before sulfate, and tropical particles delayed a
year or more. The 1831 Zavaritskii glass came at the particle peak in early
1831, ahead of the sulfate (Plunkett 2023 §2.2.3; Hutchison 2025).

## Pre-registration, part B: TUNU2013 (written 2026-10-20, after the NEEM run, before any TUNU2013 feature was computed)

**Data.** Arctic Data Center doi:10.18739/A2ZD34, `Tunu13_database_111816_Arctic_Data_Center.csv`
(McConnell, DRI; CC-BY 4.0; marked preliminary). CFA averaged to 20 mm, on
the Sigl 2015 chronology, 268–2013 CE. About 6 samples a year in the 1450s.
It has Cl, Br, Tl, Cd, Pb, Al, Ce, Mn, Ca, Na, S, acidity and more. There is
no depth column.

**Events, background, onset, interval.** As in part A, with the same
calibration list and the same exclusions.

**Features.**
- Lithic, with Al as the crustal reference: ratio residuals `r_CeAl`,
  `r_MnAl`, `r_CaAl`. Load anomalies `a_Al`, `a_Ce`, `a_Mn`. Same z,
  running-mean and window rules as part A.
- Volatile, per unit of volcanic sulfur, over the event interval:
  ΣΔX / ΣΔnssS for X in nssCl (Cl − 1.80 Na), nssBr (Br − 0.0062 Na), Tl, Cd,
  Pb. Plus `acid` as in part A. Seawater ratios are standard mass ratios, not
  fitted.
- Lithic timing: first running-mean z > 3 of Al and Ce load within onset ± 1
  yr, lag from sulfate onset.

**Tests.** Per-feature AUC and permutation p (10,000 shuffles), Holm over the
12 features. Nearest-centroid LOO on all 12 features, with each feature
turned into its percentile rank inside the training fold (the ratios have
heavy tails). Permutation p from 2,000 shuffles. The same decision rule:
**separates** if LOO balanced accuracy ≥ 0.75 and p < 0.05. The same
sensitivity (after 1500) and secondary (NHX vs TROP) runs. UE 1453 last.

**Expected.** Icelandic fissure eruptions are halogen-rich and close, so
ΔCl/ΔS and volatile metals per S should be higher for ICE. This expectation
is from the general literature, not a verified source (see Unverified
claims). The run tests it. It does not assume it.

## Changes after the first run

- `tracers.py`: an optional `force_onset` argument, used only by `null.py`.
  The NEEM output was checked byte-identical before and after.
- `tracers.py`: the lithic lag was computed only for Ce, Mn and Ca, so the
  pre-registered TUNU2013 Al lag came out empty. Fixed so every load gets a
  lag. NEEM output unchanged (byte-identical).
- `null.py` (new, post-hoc). The NEEM features are window maxima, so they
  need a null. Pseudo-events: every year 200–1890 with no eVolv2k v4 event in
  [Y − 9, Y + 3], onset forced to Y + 0.5. An event "has a lithic excess" in a
  feature if it beats the null 95th percentile.
- `tunu.py --deseason-onset` (new, post-hoc). On TUNU2013 at about 6 samples
  a year the pre-registered onset rule misfires. It finds Krakatau at
  1882.48, on a winter sea-salt high before the eruption. It also loses
  Huaynaputina, Hekla 1766 and Katla 1755, whose backgrounds hold earlier
  events or large seasonal peaks. The variant detects onsets on nssS minus
  the ±10 yr median of its two-month bin. It is reported beside the
  pre-registered run, not instead of it.

## Run

```
python3 -I -B tracers.py ../02-ice-onset/data/neem2011s1.tab > results/tracers.txt
python3 -I -B null.py ../02-ice-onset/data/neem2011s1.tab ../02-ice-onset/data/evolv2k_v4.tab > results/null.txt
python3 -I -B tunu.py data/tunu/Tunu13_database_111816_Arctic_Data_Center.csv > results/tunu.txt
python3 -I -B tunu.py data/tunu/Tunu13_database_111816_Arctic_Data_Center.csv --deseason-onset > results/tunu_deseason_posthoc.txt
python3 -I -B null.py data/tunu/Tunu13_database_111816_Arctic_Data_Center.csv ../02-ice-onset/data/evolv2k_v4.tab --tunu > results/null_tunu.txt
python3 -I -B dist.py > results/dist.txt
```
Each `--calibration-only` run stops before UE 1453. The first NEEM and
TUNU2013 runs used it. Standard library only. Each full run takes 1–3
minutes (permutations).

The TUNU2013 file comes from
`https://arcticdata.io/metacat/d1/mn/v2/object/arctic-data.9798.1`. Its md5
matches the EML record (d924dc84…).

## Result

### Part A: NEEM-2011-S1 (`results/tracers.txt`, `results/null.txt`)

- 27 of 36 calibration events have a sulfate onset under the rule: 10 ICE,
  7 NHX, 10 TROP. Nine have none (Katla 757, 823, 1721; Hekla 1510; Askja
  1875; Shiveluch 452; Fujisan 1707; Ruiz 1595; Gamkonora 1673).
- **Iceland does not separate.** Nearest-centroid LOO balanced accuracy
  0.31, permutation p 0.92. No feature survives Holm. The best raw one is
  Mn|Ca: AUC 0.26, p 0.047 (ICE lower), Holm p 0.42. After 1500: balanced
  accuracy 0.36, p 0.79. NHX vs TROP: 0.56, p 0.35.
- **The CFA lithic channels do not see ash at the eruptions.** Against 355
  non-volcanic windows, Laki 1783, Eldgjá 939 and Veiðivötn 1477 beat the
  95th percentile in none of seven lithic features. Over all 27 events, the
  share above p95 is 0–1 per class per feature, about what chance gives
  (5 %). The Ce load crosses z = 3 in 23 % of empty windows, so lithic
  timing at NEEM carries no information.
- Distance from NEEM does not predict any feature (|Spearman ρ| ≤ 0.18).
- **UE 1453** (onset 1453.13, as in 02): no lithic feature above the null
  p95. Its highest is Mn|Ca at the 87th percentile. The classifier says
  "not ICE" (three-way: NHX). Under the rule this is a description, not a
  classification. Its acid ratio is 1.47 (acidity beyond sulfuric acid),
  above 9 of 10 ICE and all 10 TROP events, but acid does not separate the
  classes (AUC 0.59).

### Part B: TUNU2013 (`results/tunu.txt`, `results/tunu_deseason_posthoc.txt`, `results/null_tunu.txt`)

- Pre-registered run: 21 events with onsets (8 ICE, 6 NHX, 7 TROP).
  **Iceland does not separate**: LOO balanced accuracy 0.70, permutation
  p 0.081. No feature survives Holm. Best raw: a_Ce, AUC 0.81, p 0.021,
  Holm 0.25. After 1500 (3 ICE), a_Ce has AUC 1.00, p 0.005, Holm 0.056.
  Post-hoc variant: 0.67, p 0.089. Same verdict.
- **Halogens and volatile metals do not separate either** in this file.
  nssCl/S AUC 0.65 (p 0.27); Br 0.39; Tl 0.59; Cd 0.75 (p 0.068); Pb 0.25.
- **Lithic excess, post-hoc.** Against 334 empty windows, the Al load beats
  the null p95 in 4 of 8 ICE events (Veiðivötn 877, Veiðivötn 1477, Laki,
  Grímsvötn 1873), 0 of 6 NHX and 1 of 7 TROP (Samalas). Hypergeometric
  P(≥ 4 of the 5 in ICE) = 0.047. This was found after looking. It is a
  lead, not a result. **Zavaritskii 1831, whose TUNU2013 shards Plunkett
  2023 analysed, shows no lithic excess here** (Al load at the 15th
  percentile). The CFA lithic channel misses fine (~10 µm) distal ash.
- **UE 1453 in TUNU2013.** Onset 1452.89 (pre-registered) or 1453.08
  (variant). Abbott S9 gives 1453.00 (02).
  - Al load z +4.2 (variant +3.9), at the **97th percentile of empty
    windows**. Above 7 of 8 ICE, 6 of 6 NHX and 6 of 7 TROP events.
  - Al crosses z = 3 **0.29 yr after** the sulfate onset (variant 0.10 yr).
    That is one or two samples, synchronous within resolution. **No ash
    before sulfate.** ICE Al lags run −0.09 to +0.64 yr; TROP +0.07, +0.09.
  - nssCl/S is −0.28, the lowest of all 21 events in both runs. Cd/S is
    the lowest or near it. Acid/S 0.36, near the bottom. The negative nssCl
    falls on the winter Na maximum (Na 75–82 ng/g at the onset), so it may be
    a sea-salt correction artefact (Cl/Na fractionation). Not tested.
  - Classifier: "not ICE"; three-way: TROP. Under the rule, description
    only.

### What this says about UE 1453

- Open CFA tracers in NEEM and TUNU2013 cannot tell an Icelandic eruption
  from a distant one, by the pre-registered test in either core. So they
  cannot move H5 or H6.
- TUNU2013 shows a lithic (Al) pulse at the 1453 onset, as large as the
  largest Icelandic and Samalas pulses. It is synchronous with the sulfate,
  not ahead of it. It comes with no excess chloride. The post-hoc pattern
  (lithic excess mostly at Icelandic events) would place 1453 with
  Iceland. Its halogen deficit points the other way. Neither is a
  calibrated discriminator.
- The 1831 test (ash before sulfate) cannot be run on these data. The 1831
  positive control itself shows nothing in CFA.

## Part B: data inventory (1450–1455, sub-annual, Greenland)

| Record | What | 1450s? | Access | Used |
|---|---|---|---|---|
| TUNU2013 CFA, McConnell (Arctic Data Center doi:10.18739/A2ZD34, 2016-11-18) | 20 mm CFA: cond, H2O2, NH4, HNO3, δ18O, BC, acid, MSA, Na, Mg, S, Cl, Ca, V, Cr, Mn, Br, Rb, Sr, Pb, Al, Cd, Cs, Ba, La, Ce, Nd, Tl, U; 268–2013 CE | yes, ~6–7 samples/yr | **open**, CC-BY 4.0, "preliminary" | yes |
| TUNU2013 CFA, second version (doi:10.18739/A2ZQ1G, 2016-12-06, `Tunu13_database_120216.csv`) | same plus CO | yes | EML open; the data object `autogen.2016120911232026822.1` returned **404** | no |
| TUNU2013 "TUNUredo" reanalysis with continuous microparticles (Plunkett 2023 Fig. 2; Abbott 2021) | particles, nssS | yes | **not archived**; Plunkett 2023: "Data will be made available on request" | no |
| Abbott 2021 Table S9 | TUNU2013 monthly nssS, Ca, Na, 1440–1490 | yes | open (used in 02) | no new tracers |
| NEEM-2011-S1 (PANGAEA.940553) | 12 species incl. Ce, Mn, Sr, acidity | yes | open | yes (part A) |
| NGRIP DRI CFA (Arctic Data Center arctic-data.9831.3) | McConnell continuous chemistry | **no**: sections ~1535–1719, ~741–1004, ~−848 to −1175 CE | open | no |
| NGRIP2 lead (McConnell 2018 PNAS) | Pb, 1100 BCE–800 CE | no | not located | no |
| B19 / TUNU2013 LA-ICP-MS (PANGAEA.967063) | trace elements | no, 751–763 CE | open | no |
| EGRIP / NEGIS CFA | — | not found in this session | — | no |
| Coulter 2012 particle/tephra intervals | three Greenland cores | unknown | Wiley 403 (02) | no |

## Limits

- NEEM is at 77.45 N 51.06 W: 1,790–1,890 km from the Icelandic vents,
  3,470–7,450 km from NHX, 7,030–12,300 km from TROP. TUNU2013 (78.04 N
  33.88 W) is 1,550–1,680 km from Iceland (`dist.py`, `results/dist.txt`). Distance is confounded with class, yet no feature
  tracks distance at NEEM.
- The CFA elements are acid-leachable fractions of melted ice, not shard
  counts. Fine distal glass contributes little. The 1831 case shows this.
- The calibration classes are small: 8–10 ICE, 6–7 NHX, 7–10 TROP. Many
  early ICE attributions come from tephra found by sampling particle peaks
  (Plunkett 2023), so they may be biased toward a lithic signal. The after-1500
  sensitivity runs address this, with n = 3–4 ICE.
- The TUNU2013 file is marked preliminary by its PI. Abbott 2021 used a
  later reanalysis.
- Onset detection transfers poorly to TUNU2013. Different rules drop
  different events. The verdict does not change between them.
- Vent coordinates in the scripts are approximate, from memory of GVP. They
  are used only for the descriptive distance check.

## Walls

- **No discriminating tracer in open CFA data.** Neither core separates
  Icelandic from distant eruptions under a pre-registered, permutation-tested
  rule. Breached by a tracer that does (glass, or shard counts and size
  distributions), or by a larger calibration set from a reanalysed record.
- **Particle data are gated.** The TUNU2013 continuous microparticle record,
  which shows ash-before-sulfate for Alaska and 1831, is "available on
  request" (Plunkett 2023). Asking DRI or QUB is Greg's decision. That
  record would answer the 1453 ash-timing question directly.
- **Glass.** Criterion 7 still needs shards from 1452.5–1453.5 ice. The
  TUNU2013 Al pulse at the onset says where to cut.

## Unverified claims

- That halogens and volatile metals (Tl, Bi, Cd, Pb, Br, Cl) separate
  basaltic Icelandic from arc andesite eruptions in Greenland ice. Search
  found Mason, Edmonds & McConnell 2022 (Antarctic, volatile metals carried
  as chloride aerosol) and Green et al. 2025 PLOS ONE (Tl and Bi with an 8th-
  century Katla eruption, figure caption only). Neither full text was read
  (PMC CAPTCHA). Hutchison 2024 (Eldgjá, JGR) abstract does not mention
  metals. In this test the claim does not hold for the TUNU2013 file.
- An older study reports a Laki chloride peak in Greenland not matched by
  Na (search snippet; source not opened).

## Provenance

| File | URL | Fetched | sha256 | Changes |
|---|---|---|---|---|
| data/tunu/Tunu13_database_111816_Arctic_Data_Center.csv | https://arcticdata.io/metacat/d1/mn/v2/object/arctic-data.9798.1 (doi:10.18739/A2ZD34) | 2026-10-20 | a426ac47b5f92f75d952199439d8109e1032a0763dc413f0f52981af034ee65f | none |
| data/A2ZD34.eml.xml | https://arcticdata.io/metacat/d1/mn/v2/object/doi%3A10.18739%2FA2ZD34 | 2026-10-20 | 574c6cf49b8692ea823f49d416cc08e1e36746c4101e2ba73423c4dae96c1602 | none |
| data/A2ZQ1G.eml.xml | https://arcticdata.io/metacat/d1/mn/v2/object/doi%3A10.18739%2FA2ZQ1G | 2026-10-20 | ca53b85ea98c342950b9fc41b8ce9e84df769aed7674b9ce505b9bf13f29e98e | none |
| data/ngrip_9831.eml.xml | https://arcticdata.io/metacat/d1/mn/v2/object/arctic-data.9831.3 | 2026-10-20 | f0d301b3ada61c25d686866f14ef3eeb83be9802c06d88ad3a3c687c7abc0b1b | none |
| ../02-ice-onset/data/neem2011s1.tab | https://doi.pangaea.de/10.1594/PANGAEA.940553?format=textfile | 2026-10-20 (02) | 0ab79ea5c956d36a57768280fc1239e1d8c5911abb78e6fd41ab3e2fb9e5105d | none |
| ../02-ice-onset/data/evolv2k_v4.tab | https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile | 2026-10-20 (02) | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 | none |

`data/` is gitignored.

## Addendum (2026-10-20, post hoc): annual TUNU2013 particles, Abbott 2021 Table S7

Part B missed this. Abbott 2021 Table S7 (already downloaded by 02:
`../02-ice-onset/data/abbott_supp/tsv/sheet7.tsv`, from the supplement
xlsx with sha256 7b9f4b43…) gives **annual** insoluble particle mass
(4.5–9.5 µm) for TUNU2013, 1450–1500. The sub-annual record Plunkett 2023
holds is still on request only.

Run: `python3 -I particles_s7.py ../02-ice-onset/data/abbott_supp/tsv/sheet7.tsv > results/particles_s7.txt`

Result: 1453 is 1.23× the 1450–1500 median (robust z 0.46, rank 17 of 51);
1454 is 1.07×. Veiðivötn 1477, with similar nssS (83 vs 73 ng/g) and
glass found in this core, is 8.1× (rank 1). 1479 is 5.3× (rank 2).
1453 therefore shows no coarse-particle fallout at annual resolution. That
is evidence against a proximal Icelandic source like V1477, from one
calibration case only. Annual means dilute short pulses, but V1477
survives the averaging. Fine distal ash (< 4.5 µm) is not measured here.
