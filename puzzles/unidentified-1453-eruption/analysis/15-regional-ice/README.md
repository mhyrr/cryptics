# 15 — Regional ice cores near the candidate sources

**Question.** Do ice cores close to the candidate source regions tell where
the 1453 sulfate came from?
- (a) North Pacific. If the source was Aniakchak (H10), Kamchatka (H11) or
  the Kurils (H12), 1453 should be strong in Alaskan and Yukon ice relative to
  Greenland.
- (b) Iceland side. A Grímsvötn source (H5) should be strong in Svalbard and
  Eurasian Arctic ice relative to a North Pacific source.

## Step 1 — Availability

Searched: the NCEI paleo-search API, ice-core data type (`dataTypeId=7`),
boxes 45–72° N 150° E–125° W (North Pacific) and 70–85° N 0–110° E
(Eurasian Arctic). Dumps are in `data/ncei/`; the list is in
`results/coverage_all.txt` (`search.py`, `coverage.py`). Also searched: the
PANGAEA search API (`pangaea_search.py`; "Akademii Nauk", "Lomonosovfonna",
"Ushkovsky OR Kamchatka ice core"), and the web for supplements.

| Core | Lat, lon | Open chemistry reaching 1440–1470? | Variable, resolution near 1450 | Dating near 1450 | Source | Tier |
|---|---|---|---|---|---|---|
| **Begguya (Mt Hunter, Denali), DEN-13B** | 62.94 N, 151.09 W | **Yes**, 801–2013 | IC SO4, Na (ppb); 98 samples in the 1400s (~1/yr); 1700s 2.3/yr, 1900s 11.7/yr | Annual layer counting by three counters. Volcanic peaks were used only to *check* the count, and only for 1750–2013. From 1500 to 800 CE the count rests on conductivity and dust alone. Laki and Pavlof 1763 come out 1 yr off; there is no stated uncertainty for 1450. **Not tied to 1453.** | NCEI study 38023, https://www.ncei.noaa.gov/pub/data/paleo/icecore/northamerica/usa/osterberg2017/osterberg2017-den13b.txt ; Winski et al. 2017, Sci. Rep. 7:17869, https://pmc.ncbi.nlm.nih.gov/articles/PMC5736703/ | PRIMARY (data); SCHOLARLY (method) |
| Eclipse Icefield core 2 (2002) | 60.51 N, 139.47 W | Yes, 1011–2002 | IC SO4, Na; 225 samples in the 1400s. Core 2 was resampled at 2–6 cm "around select high sulfate horizons", so density is uneven | **Tied to 1453 by construction.** The header lists "Kuwae (AD 1453)" among the sulfate reference horizons, and the error is "up to ±5 years from AD 1453–1783". The core is "not annually resolved prior to AD 1450". | NCEI study 30877, https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/eclipse/eclipse2002core2ion.txt ; method text in NCEI 6079 `eclipse-volcanic.txt` (Yalcin et al. 2007, JGR 112, D08102) | PRIMARY |
| Eclipse volcanic SO4 loading reconstruction | same | Yes, 1450–2001, annual | Derived EOF-5 volcanic sulfate loading | As above (tied to 1453) | NCEI 6079, https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/eclipse/eclipse-volcanic.txt | PRIMARY |
| Mt Logan PR Col (2001) | 60.58 N, 140.50 W | Yes, 2-yr bins 1401–1997; annual bins only from 1700 | Total SO4 (no Na in the file) | Layer counting for the top ~500 yr, then a flow model. The ties are the "largest known volcanic acid signatures". Whether 1453 is one of them is not verified (see Unverified). | NCEI 6181, https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/mtlogan/mtlogan2008-2yr-noaa.txt ; Fisher et al. 2008 Holocene 18(5), via https://climatechange.umaine.edu/?p=13596 | PRIMARY / POPULAR (method summary) |
| Mt Logan NW Col / older Logan cores | 60.58 N, 140.5 W | Not open as annual SO4 near 1453 | — | — | NCEI 2436/2467 (from 1736, d18O only) | PRIMARY |
| Bona-Churchill | 61.4 N, 141.7 W | No: d18O only (1200–2001) | — | — | NCEI 27810 | PRIMARY |
| Ushkovsky (Kamchatka) K2 1998 | 56.07 N, 160.47 E | **No: analysed section 1736–1997** | δD, accumulation; no open sulfate found | Isotope layer counting, 1–3 yr | Sato et al. 2014, Clim. Past 10:393, https://cp.copernicus.org/articles/10/393/2014/ | SCHOLARLY |
| Lomonosovfonna 1997 (Svalbard) | 78.86 N, 17.43 E | **No open sulfate found.** The ion record covers ~800 yr but is published as decadal running means because of melt percolation; no data file is on NCEI or PANGAEA | — | Moore 2012 Table 2 lists the volcanic markers it was dated with (identifications only, no fluxes) | Kekonen et al. 2005, JGR 110, doi:10.1029/2004JD005223 (abstract via https://brage.npolar.no/npolar-xmlui/handle/11250/174334); PANGAEA.817166 | SCHOLARLY |
| Lomonosovfonna 2009, Austfonna 1999 | Svalbard | No: black carbon (2009), d18O (1999) only | — | — | NCEI 25510, 11173 | PRIMARY |
| Austfonna 1987 | 79.85 N, 24.13 E | No: pH, HCO3, Cl by depth, no age column, no sulfate | — | — | NCEI 2433 `aust87chem-noaa.txt` | PRIMARY |
| Holtedahlfonna 2005 | 79.14 N, 13.27 E | **No: reaches ~1700 CE** | — | — | Moore et al. 2012, JGR 117, D03306 (PANGAEA.817167) | SCHOLARLY |
| Akademii Nauk (Severnaya Zemlya) | Severnaya Zemlya (coordinates not checked) | **No: open major ions cover 1883–1998 only.** Open 900–1998 series hold layer thickness, δ18O and Na, but no sulfate | — | AN 2012 chronology | PANGAEA.871279, PANGAEA.824732 | PRIMARY |
| Windy Dome (Franz Josef Land) | 80.78 N, 63.65 E | No: d18O and melt only | — | — | NCEI 22543 | PRIMARY |

**Availability verdict.**
- *(a) North Pacific:* one core reaches 1453 with an independent chronology:
  Begguya / Denali, at about one sample per year. Eclipse and probably Logan
  reach 1453 but were dated with a 1453 tie, so their 1453 peak sits there
  by construction.
- *(b) Iceland side:* **no open sulfate record from Svalbard or the Eurasian
  Arctic reaches 1453.** Side (b) cannot run. That is the wall for (b); see
  below.

## Step 2 — Pre-registration (written before any 1450s value from Begguya was read)

**Disclosure: two leaks, before this was written.**
1. While reading the Eclipse reconstruction header I ran `tail` on the file
   and saw its last four rows: 1450 0, 1451 0.23, 1452 0.55, 1453 2.38
   (loading units, at the base of the record).
2. A header `grep` for "1453" on the Logan 2-yr file returned one data row:
   1453.5 SO4 = 122.75 ppb. I had seen no other Logan value, so I could not
   say whether that is high.

I have seen **no Begguya value** from any year. Begguya is therefore the
primary test. Eclipse and Logan are secondary and flagged: they are
contaminated by these leaks and by their 1453-tied dating.

**Events.** `events.tsv`, fixed now. Greenland reference G (kg km⁻²): eVolv2k
v4 for events up to 1890; Sigl et al. 2015 SI MOESM47 for 1912 and 1991.
Classes:
- NP (North Pacific rim, n = 9): Novarupta 1912; Komagatake 1856; Toya
  1853; Zavaritskii 1831; Shikotsu 1739; Fuji 1707; Tarumae 1667;
  Changbaishan 946; Churchill WRAe 853.
- IS (Iceland, n = 11): Askja 1875; Grímsvötn 1873; Laki 1783; Hekla 1766;
  Katla 1755; Katla 1721; Hekla 1510; Veiðivötn 1477; Katla 939; Veiðivötn
  877; Katla 823.
- TR (tropical, n = 12): Pinatubo 1991; Krakatau 1883; Makian 1861;
  Cosigüina 1835; Galunggung 1822; Tambora 1815; Gamkonora 1673; Parker
  1640; Huaynaputina 1600; Ruiz 1595; Colima 1585; Samalas 1257.

Shiveluch 1854 is not in eVolv2k. 1853 Toya and 1856 Komagatake stand in its
place.

**Contamination rule.** A calibration event is dropped if any other event in
eVolv2k v4 or Sigl 2015 with G ≥ 5 kg km⁻² lies within ±3 yr and is not
known to be of the same class. Unattributed events ("N/A") count as
different. The dropped list is printed.

**Series.** nssSO4 = SO4 − 0.252 Na (seawater mass ratio). Logan has no Na,
so it uses total SO4. Samples are binned to calendar years by `floor(avg_year)`
and each bin is the mean of its samples. Logan's 2-yr bins are assigned to
their centre year.

**Excess.** For event year E:
- Background is the median of the annual values in [E−20, E−4] ∪
  [E+4, E+20].
- Scale is 1.4826 × MAD of the same values.
- z = (max annual value in [E−3, E+3] − background) / scale.
- The 1453/1458 pair is split at the midpoint: 1453 uses [1450, 1455] and
  1458 uses [1456, 1461]. Both drop [1450, 1461] from their background.

**Metric.** L = log10(max(z, 1)) − log10(G), the regional signal per unit
of Greenland deposition. Expectation: NP high, IS and TR low.

**Gate (is the test informative?).**
- AUC(L; NP vs IS ∪ TR) ≥ 0.80, with one-sided permutation p ≤ 0.05
  (10,000 shuffles, seed 15).
- At least 3 events in each class after contamination drops.
- For the Iceland question also report AUC(NP vs IS). An AUC near 0.5 there
  means Denali cannot tell Alaska from Iceland.
- Sensitivity: the same AUC using only events before 1800 (resolution of
  2.3 samples/yr or less, closer to the 1450s).

**Classification (only if the gate passes).**
- Threshold t* is the Youden-optimal cut on L in the calibration set.
- 1453 is "NP-like" if L₁₄₅₃ > t*, otherwise "not NP-like".
- Also report L₁₄₅₃'s empirical percentile within each class, and whether
  the [1450, 1455] maximum is the same year as the [1456, 1461] maximum
  (one merged peak, so no separate 1453 reading).
- If the gate fails, the test is uninformative and 1453 is reported for
  completeness only, with no classification.

**What this can and cannot say.**
- A pass with "NP-like" supports H6 (H10/H11/H12) over H5 and H3, but does
  not pick among the North Pacific candidates.
- "Not NP-like" weakens H10, H11 and H12 in proportion to the calibration's
  sensitivity.
- No result here identifies a volcano. Criterion 7, glass, still stands.

## Method

- `search.py` and `coverage.py` find the cores (Step 1).
- `fetch.py` downloads the files (sha256 in `results/fetch_sha256.txt`).
- `inspect.py` prints headers and per-century sample counts without values.
- `regional.py` does the Step 2 computation; its constants match the text
  above.

## Run

```
cd puzzles/unidentified-1453-eruption/analysis/15-regional-ice
python3 -I search.py data/ncei/npac_w.json 45 72 150 180      # and npac_e, eurarc (see README)
python3 -I coverage.py data/ncei/*.json > results/coverage_all.txt
python3 -I fetch.py data/ncei osterberg2017-den13b.txt eclipse2002core2ion.txt mtlogan2008-2yr-noaa.txt -- data/ncei/*.json
python3 -I regional.py data/ncei events.tsv ../02-ice-onset/data/evolv2k_v4.tab ../02-ice-onset/data/sigl2015/t47/sheet2.tsv > results/calibrate.txt
# --classify adds 1453/1458; NOT run, because the gate failed (see Result)
```

## Result (`results/calibrate.txt`)

**Calibration gate: FAIL in all three cores. The test is uninformative, and
1453 was not scored.** The brief says to stop at a failed calibration, so
`--classify` was never run. That overrides the "report 1453 for completeness"
line in my own pre-registration. No Begguya value from 1440–1470 has been
looked at.

The contamination rule dropped four events (Parker 1640, Veiðivötn 1477,
Samalas 1257, Veiðivötn 877), each for an unattributed G ≥ 5 event within
±3 yr. That left NP 9, IS 9, TR 10.

| Core | n scored (NP / IS / TR) | AUC NP vs IS+TR (perm p) | AUC NP vs IS (p) | AUC pre-1800 | Gate |
|---|---|---|---|---|---|
| Begguya DEN-13B (primary) | 9 / 9 / 10 | 0.51 (0.48) | 0.58 (0.29) | 0.40 | FAIL |
| Eclipse core 2 (secondary) | 7 / 7 / 10 | 0.50 (0.50) | 0.55 (0.38) | 0.48 | FAIL |
| Mt Logan 2-yr (secondary) | 7 / 7 / 10 | 0.55 (0.37) | 0.35 (0.84) | 0.67 | FAIL |

Why it fails, from the per-event lines (descriptive, not a new test):
- Large eruptions of every class show up in Alaskan and Yukon ice.
  Novarupta 1912 is clear (Begguya z 10.1, Eclipse 7.5), and so are Laki
  1783 (Begguya z 8.9), Tambora 1815 (6.1) and Pinatubo 1991 (4.4).
- Several known North Pacific events are weak or absent: Tarumae 1667 z 0.5,
  Shikotsu 1739 z 1.7, Churchill WRAe 853 z 0.8, Changbaishan 946 z < 0 at
  Begguya. Meanwhile Katla 1721 (z 5.7) and Makian 1861 (z 10.6) score as
  high as anything North Pacific.
- Per unit of Greenland deposition, the NP class (median L −0.96) does not
  sit above IS (−0.89) or TR (−0.73) at Begguya.

So a 1453 regional/Greenland ratio, whatever its value, would not move the
odds between H6 and H5/H3.

## Caveats

- **Small and uneven n.** Only two calibration events are Alaskan (1912,
  853) and one is Kuril (1831). The NP class is mostly Japanese (5 of 9),
  south and west of the candidates. A pure Alaska/Kamchatka class cannot be
  calibrated: it has 2–3 events.
- **Resolution.** Begguya has about 1 sample per year at 1450, against 12
  per year in the 1900s. Annual means of single samples are noisy, and the
  pre-1800 subset (closer in resolution) separates no better (AUC 0.40).
- **Dating.** Begguya before 1750 has no volcanic check, and its count in
  800–1500 rests on conductivity and dust. A ±3-yr window may miss offsets.
  The peak years for 1600 (1597), 1721 (1724) and 1739 (1741) suggest
  offsets of 2–3 yr.
- **Concentration, not flux.** Begguya and Eclipse are concentrations
  (ppb). Accumulation changes (Winski 2017 report a doubling since ~1840)
  change the background and its spread over time. The z normalisation
  absorbs some of this, not all.
- **Mixed Greenland references.** eVolv2k v4 up to 1890 and Sigl 2015 for
  1912 and 1991. These are not the same composite.
- **Leaks.** Two disclosed in Step 2 (the Eclipse reconstruction 1450–1453,
  one Logan 1453.5 row). They do not affect a failed gate.
- **Eclipse and Logan circularity.** Their chronologies use 1453 as a tie
  (Eclipse: stated; Logan: not verified). Even with a passing metric, their
  1453 peak could be any eruption within the ±5-yr dating error.

## The walls

1. **(b) Iceland side: data wall.** No open sulfate record from Svalbard,
   Franz Josef Land or Severnaya Zemlya reaches 1453.
   - Lomonosovfonna 1997 has an ~800-yr ion record (Kekonen 2005), but it is
     published only as decadal running means, and no data file was found on
     NCEI or PANGAEA.
   - Holtedahlfonna stops at ~1700.
   - Akademii Nauk's open ions start in 1883.

   Breach: Lomonosovfonna 1997 annual sulfate from the Uppsala/Oulu/NPI
   group (Kekonen, Pohjola, Isaksson, Moore), or Akademii Nauk sulfate from
   AWI (Fritzsche, Opel). Either would also need its own Iceland vs North
   Pacific calibration, and the Begguya result suggests that will be hard.
2. **(a) North Pacific: method wall.** The one independently dated core,
   Begguya, reaches 1453, but its regional/Greenland ratio does not separate
   known North Pacific eruptions from Icelandic or tropical ones (AUC 0.51).
   This is not a data gap: big eruptions from anywhere show up there.
   Breach: possibly sub-annual Begguya sulfate in the 1450s, or non-sulfate
   tracers (tephra, which the Begguya group is already searching for
   pre-1500 events: Brooks et al., IEDA doi:10.60520/IEDA/113910). That
   points back to criterion 7, glass.

## What this means for H-numbers

H10 (Aniakchak), H11 (Shiveluch), H12 (Kuril caldera), H5 (Grímsvötn) and
H3 (NHET vs tropical / H7 Pinatubo): **no change.** The regional-ice test
cannot run on the Iceland side (no data) and is uninformative on the North
Pacific side (calibration AUC ≈ 0.5). Uninformative, not negative.

## Sources

| Claim | URL | Tier |
|---|---|---|
| Core inventory, spans, variables | NCEI paleo-search API, `dataTypeId=7` (dumps in `data/ncei/`) | PRIMARY (archive metadata) |
| Begguya data | https://www.ncei.noaa.gov/pub/data/paleo/icecore/northamerica/usa/osterberg2017/osterberg2017-den13b.txt (DOI 10.25921/6cpm-kr44) | PRIMARY |
| Begguya dating method, volcanic checks 1750–2013 only, 1500–800 by conductivity/dust | Winski et al. 2017 Sci. Rep., https://pmc.ncbi.nlm.nih.gov/articles/PMC5736703/ | SCHOLARLY |
| Begguya tephra work in progress | Brooks, Kurbatov, Winski, Kreutz, https://par.nsf.gov/biblio/10616968 | PRIMARY (dataset record) |
| Eclipse dating tied to "Kuwae (AD 1453)", ±5 yr 1453–1783, not annual before 1450 | header of https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/eclipse/eclipse-volcanic.txt (Yalcin et al. 2007 JGR 112 D08102) | PRIMARY |
| Eclipse core 2 ions | https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/eclipse/eclipse2002core2ion.txt | PRIMARY |
| Logan PR Col SO4 | https://www.ncei.noaa.gov/pub/data/paleo/icecore/trop/mtlogan/mtlogan2008-2yr-noaa.txt | PRIMARY |
| Logan timescale: counted years plus largest volcanic acid signatures | https://climatechange.umaine.edu/?p=13596 (summary of Fisher et al. 2008) | POPULAR |
| Ushkovsky span 1736–1997 | Sato et al. 2014 Clim. Past 10:393, https://cp.copernicus.org/articles/10/393/2014/ | SCHOLARLY |
| Lomonosovfonna ion record, decadal running means | Kekonen et al. 2005 JGR, https://brage.npolar.no/npolar-xmlui/handle/11250/174334 | SCHOLARLY |
| Holtedahlfonna to ~1700; Svalbard volcanic markers | Moore et al. 2012 JGR 117 D03306, https://doi.pangaea.de/10.1594/PANGAEA.817167 | SCHOLARLY |
| Akademii Nauk open datasets | https://doi.pangaea.de/10.1594/PANGAEA.871279 , https://doi.pangaea.de/10.1594/PANGAEA.824732 | PRIMARY |
| Greenland references | eVolv2k v4 (PANGAEA.971968; repo copy); Sigl et al. 2015 Nature SI MOESM47 (repo copy) | PRIMARY |

## Unverified claims

- Whether the Mt Logan PR Col timescale uses 1453 as a volcanic tie. The
  summary says "largest known volcanic acid signatures"; Fisher et al. 2008
  was not read.
- Begguya dating uncertainty at 1450: not stated in Winski 2017 as read.
  The newer chronology (annual layers, volcanic sulfate peaks, 14C, per the
  Brooks et al. record) may tie 1453/1458. If the archived file uses it, the
  1450s would be circular there too. Not checked: the NCEI file cites
  Osterberg 2017 and Winski 2017.
- Whether Lomonosovfonna 1997 annual sulfate exists in any open archive
  beyond what NCEI and PANGAEA searches returned. Kekonen's 2006 Oulu thesis
  (https://urn.fi/URN:ISBN:9514281853) may tabulate it. Not opened.
- Whether any Akademii Nauk sulfate or conductivity series through 1453 is
  published (an EGU2008 abstract reports a ~1,500-yr age model for the upper
  530 m). Not found as data.
- The attribution of Sigl 2015's 1912 deposit (28.6 kg km⁻²) to Novarupta
  rests on the documented June 1912 date and the NH class flag, not on
  tephra in Greenland.
