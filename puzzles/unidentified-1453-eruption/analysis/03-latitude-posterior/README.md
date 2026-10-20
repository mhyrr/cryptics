# 03 — Latitude posterior

**Question.** Which latitude band did UE 1453 come from? We use three kinds of
evidence: hemispheric asymmetry (ASY 0.829), the Burke 2023 sulfur-isotope
class, and the Marshall et al. 2021 deposition emulator. Each one is scored on
eruptions with known sources before it is applied to 1453.

Bands: NHET (> 30° N), NTROP (0–30° N), STROP (0–30° S), SHET (> 30° S).
H2 is NTROP. H3 is NHET.

## Method

**1. Asymmetry (`calib_asymmetry.py`).** We take the eVolv2k v4 rows that name
a source volcano and join each one to its GVP latitude by volcano number.
The name map is in the script. Three GVP names differ from eVolv2k's:
Makian is Kie Besi, Mount Parker is Melebingoy, and Zavaritskii is the Kurils
Zavaritzki Caldera, not the Kamchatka Zavaritsky. Classifier: two ASY
thresholds (SHET < t1 ≤ TROP < t2 ≤ NHET), fitted to maximise training
accuracy and scored leave-one-out. Likelihood for 1453: the Jeffreys-smoothed
share of each band with ASY in a window around 0.829, plus a Gaussian KDE
(h = 0.05). The SHET set has only two events, so its pool adds the NHET events
mirrored (ASY → 1 − ASY). That assumes an SH extratropical source is at least as
southward-biased as an NH one is northward-biased.

**Leakage.** We dropped 217 of 256 eVolv2k rows:
- 214 rows have no source. Their latitude (45° N, 0° or 45° S) is set *from* the
  ice asymmetry, so using them would be circular.
- 2 rows say "Unidentifed" (87 CE; 45 BCE "Iceland").
- 1 row is Kuwae 1458. Its source is contested (Hartman 2019 against EGU25-2329).

That leaves 39 events: 25 NHET, 12 TROP, 2 SHET. Of these, 18 are attributed
by glass in the ice and 21 by documentary date. GVP and eVolv2k latitudes agree
to within 1° for all 39. GVP dates some of these eruptions from ice (Samalas
1257 is "Sidereal: Ice Core"). That does not leak latitude, because the volcano
was identified by glass. Leakage we could not remove: for the 21
documentary-date attributions, the ice-core team may have used the
bipolar/unipolar pattern to choose among eruptions of the same year.

**2. Isotope class (`isotope_cases.csv`, `calib_isotope.py`).** The CSV lists
every known-source eruption we found with a published tropical or
extratropical sulfur-isotope pattern, with line and section cites. An LLM read
the papers. The script only counts.
- Method-development cases: Tambora, Samalas, Katmai (Burke 2019).
- Snow-pit references: Pinatubo, Agung (Baroni 2007, via Burke 2019).
- Out-of-sample cases: Aniakchak II (Pearson 2022) and Zavaritskii 1831
  (Hutchison 2025). Both were published after the method, and both sources
  were identified by glass.

We excluded Huaynaputina 1600, because Burke 2023 assigned its peak *from* the
isotopes. We excluded 1458, 536, 540, 626 and 1182 because their sources are
unknown or contested.

**3. Emulator (`emulator.py`).** The code is open. The CEMAC online tool
(github.com/cemac/volcanic-forcing-deposition, commit 6201f4e, Zenodo
10.5281/zenodo.4038013) ships the emulator mean and SD as JSON. The grid is
26 latitudes (80° S–80° N) × 26 plume-middle heights (16.5–26.5 km) × 26 SO₂
masses (10–100 Tg), for 1 January and 1 July eruptions. Ensemble design:
Marshall 2021 p. 4 (§2.1: "SO2 emissions ranged between 10 and 100 Tg… bottom injection height
varied between 15 and 25 km with a plume depth of 3 km"). Noise terms of 10
and 2.5 kg km⁻² (Greenland, Antarctica): p. 6. Detection thresholds of 20 and
5 kg km⁻²: p. 8 and Fig. 1.

We did not rebuild the Gaussian process. We query the published grid.
- Retention rule: keep a grid cell if the emulator mean ± 1 SD overlaps the
  observed range on both ice sheets. This is the tool's `site.js` rule and
  Marshall 2021 p. 8.
- Likelihood: a Gaussian on each ice sheet. Uniform over SO₂ and height, and
  uniform in latitude within each band.
- 1453 observation error: we assume 26 % (Greenland) and 12 % (Antarctica),
  1σ. These are the typical fractions in Marshall 2021 Table 1 (from Sigl 2015).
  eVolv2k v4 gives no per-sheet error. We also run 50 % / 50 %.

Self-check: the script reproduces the latitude ranges in Marshall 2021
Table 1 (p. 9) for all eight events to within about one grid step (6.5°).
Calibration: we run the same query on the 15 named eVolv2k events inside the
emulator domain (5–50 Tg S, above the detection thresholds).

**4. Combine (`combine.py`).** Posterior ∝ prior × L(deposition) × L(isotope).
The asymmetry likelihood and the emulator likelihood use the same two numbers,
so we never multiply them together. Each is paired with the isotope likelihood
in turn.

Six priors:
- uniform, which is also equal surface area per band;
- GVP confirmed eruptions, VEI ≥ 5, Holocene (n = 239);
- the same, CE only (n = 86);
- GVP VEI ≥ 6, Holocene (n = 58);
- eVolv2k v4's own class shares (ice-derived, so partly double-counted);
- a deliberately tropics-heavy 10/40/40/10.

## Run

```
python3 -I fetch.py data                      # downloads; prints sha256 (compare with the table below)
python3 -I calib_asymmetry.py data/evolv2k_v4.tab ../../sources/cache/gvp_holocene_eruptions.csv results/lik_asymmetry.json > results/calib_asymmetry.txt
python3 -I calib_isotope.py isotope_cases.csv results/lik_isotope.json > results/calib_isotope.txt
python3 -I emulator.py data/cemac data/evolv2k_v4.tab ../../sources/cache/gvp_holocene_eruptions.csv results/lik_emulator.json > results/emulator.txt
python3 -I combine.py results/lik_asymmetry.json results/lik_isotope.json results/lik_emulator.json ../../sources/cache/gvp_holocene_eruptions.csv > results/posterior.txt
```

Standard library only. `data/` is gitignored (9 MB).

## Result

**Asymmetry predicts the band mostly where it is trivial.** LOO accuracy is
35/39 (0.90). That number is carried by 24 unipolar events with ASY = 1.000.
On bipolar events (0 < ASY < 1) accuracy is 12/15, against a majority-class
baseline of 11/15. The fitted NHET threshold is 0.800, and 1453 (0.829) sits
just above it. That is why the classifier calls 1453 NHET. But six known events
sit in the 0.70–1.0 window:
- NHET: Okmok 0.867, Zavaritskii 0.890, Katla 763 0.930.
- NH tropical: Kie Besi/Makian 0.706, Melebingoy/Parker 0.734, Colima (19.5° N) 0.914.

The likelihood ratio NHET : NTROP at ASY ≈ 0.83 ranges from 0.31 to 0.92 on
all events, depending on the window. Restricted to VSSI ≥ 4 Tg S it ranges from
1.0 to 3.0. Asymmetry rules out SHET (likelihood ≤ 0.06 in every variant). It
does not separate NHET from the NH tropics.

**The emulator says the same.** Retained latitudes for 1453: January 17° S–67° N,
July 2° N–67° N. The likelihood peaks near 2° N for a January eruption and near
22–28° N for a July one. Normalised band likelihoods (Jan/Jul 50:50): NTROP
0.60, NHET 0.31, STROP 0.09, SHET 0.00. The calibration on 15 known events is
poor:
- argmax band correct 7/15;
- true latitude retained 14/15 when deposition is halved for the model's known
  low bias, 11/15 when it is not;
- three NH-tropical eruptions (Cosigüina, Parker, Ruiz) come out south of the
  equator;
- Okmok (53° N) comes out NTROP.

The emulator also cannot represent the tropospheric half of a 1453 plume. Its
lowest plume is 15–18 km. So its NHET likelihood is probably too low.

**Isotopes do the separating.** All 7 known-source isotope classes match the
true band (3 NHET, 4 tropical). Likelihood ratio for an extratropical pattern
is 8.75 (Jeffreys). Only 2 of the 7 are out-of-sample, both NHET. **No
tropical eruption has been tested out-of-sample**, and no NH-tropical
eruption has ever been measured in Greenland ice. Out-of-sample only, the
ratio is 1.67.

**Posterior P(NHET)** (full tables in `results/posterior.txt`):

| Likelihoods | uniform prior | GVP VEI ≥ 5 | tropics-heavy prior | range, 6 priors |
|---|---|---|---|---|
| asymmetry [0.75, 1) × isotope | 0.80 | 0.94 | 0.52 | 0.52–0.94 |
| asymmetry [0.70, 0.95) × isotope | 0.69 | 0.89 | 0.36 | 0.36–0.89 |
| asymmetry, VSSI ≥ 4 × isotope | 0.92 | 0.98 | 0.76 | 0.76–0.98 |
| emulator Jan/Jul × isotope | 0.80 | 0.94 | 0.49 | 0.49–0.94 |
| asymmetry × isotope (out-of-sample only) | 0.44 | 0.74 | 0.17 | 0.17–0.74 |
| asymmetry alone | 0.32 | 0.63 | 0.11 | 0.11–0.63 |
| emulator alone | 0.31 | 0.63 | 0.10 | 0.10–0.63 |

P(SHET) is ≤ 0.04 in every row. Almost all of the rest is NTROP.

**Reading.** Under any prior that is not deliberately tropics-heavy, NHET
is favoured, 0.69–0.98. The number rests on one test: the Burke isotope
class, calibrated on 3 extratropical and 4 tropical known cases, most of them
the cases that defined the method. Without the isotopes, the deposition data
lean slightly toward the NH tropics under a uniform prior (P(NHET) ≈ 0.3). The
honest band is "NH, probably extratropical; NH tropics not excluded".

## Limits

- Small samples throughout: 2 SHET, 3 bipolar NHET and 7 NTROP events in the
  asymmetry set; 7 isotope cases. Window and bandwidth choices move the
  NHET : NTROP ratio by a factor of 3. We picked the VSSI ≥ 4 variant after
  seeing the data, so it is a sensitivity run, not the headline.
- eVolv2k may set Antarctic deposition for NH-attributed events to zero by
  construction. We could not check this. If it does, it inflates the ASY = 1.000
  mass for NHET.
- The isotope class tests "some sulfate reached Greenland below the ozone
  layer". A large eruption at 20–30° N might do that too. No case tests it.
- The emulator was trained on 15–28 km injections only, for 1 January and
  1 July. Marshall 2021 report a low bias of about ×2 against Tambora (p. 9),
  and our calibration shows a southward bias for NH-tropical eruptions.
- 1453's per-sheet errors are assumed. The Antarctic 5.1 kg km⁻² equals the
  emulator's detection threshold (H4, experiment 02).
- Season is unknown. July favours NHET more than January (P(NHET) 0.85 against
  0.74 under a uniform prior). Experiment 02 should fix it.

## Unverified claims

- Baroni et al. 2007 (Pinatubo, Agung): known only as cited by Burke 2019.
  Not read.
- The CEMAC tool's `sd` field is assumed to include the noise term from
  Marshall 2021 p. 6. The tool's code uses it as is.
- Gautier et al. 2019 (Dome C) and other Δ³³S series were not mined for
  latitude classes. They classify stratospheric vs not, not tropical vs
  extratropical, as far as we read.

## Provenance

All fetched 2026-10-20 by `fetch.py` (Python urllib). No changes made to the files.
Text extracted locally with `pdftotext -layout` (PDFs) or by stripping XML tags; the extracts are not checked in.

| File (under `data/`) | URL | sha256 | Tier |
|---|---|---|---|
| evolv2k_v4.tab | https://doi.pangaea.de/10.1594/PANGAEA.971968?format=textfile | 468deb97903816df90f1fd6bc810afdcb928d3ef463ba4a341318932d09f8b40 | PRIMARY |
| cemac/data_axes.json | https://raw.githubusercontent.com/cemac/volcanic-forcing-deposition/6201f4e13401dfdeee4dee33c391056d718b3acf/data/axes.json | cf36a2fb463d29c5a69a64b4e14ca1806d2bf2d17fcb336f07b225e3faddf4ba | SCHOLARLY (model output) |
| cemac/data_greenland_jan.json | same repo, data/greenland_jan.json | da9f3a994f0243888faa7db9cc32b8db6ca7e6bdfd0b3d9968ad45f467f54241 | SCHOLARLY |
| cemac/data_greenland_jul.json | same repo, data/greenland_jul.json | 8595f69f68c5f78560a8c3d66ecd83d61b8f9f212d6ab3a68ed16cc5cb71e81c | SCHOLARLY |
| cemac/data_antarctica_jan.json | same repo, data/antarctica_jan.json | 5fa9e9db148a0ecb8c194db7c9caa5345ebc8befbd3f8754f5c7770a42a7d9c9 | SCHOLARLY |
| cemac/data_antarctica_jul.json | same repo, data/antarctica_jul.json | 9c9236640ef032adcc510d6861c5ddec7b6e01fcc87748f921c2ae72047e38f6 | SCHOLARLY |
| cemac/data_forcing_{jan,jul}.json, data_null.json, js_site.js, README.md | same repo | see `fetch.py` output | SCHOLARLY (unused except site.js, read for the retention rule) |
| papers/marshall2021.pdf | https://shura.shu.ac.uk/28799/1/2020JD033578.pdf | 6fe0f22a9618679437c825efe6e3461ef58e9e9a71c26a46409cc3c058074b57 | SCHOLARLY |
| papers/marshall2019.pdf | https://shura.shu.ac.uk/26683/1/Marshall2019.pdf | 6b9d17ac58b0aa0997bbe464cadbf8ee8bf86170ab0ed04d4136b3fc007f8d7b | SCHOLARLY |
| papers/burke2019.pdf | https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/20111/Burke_2019_EPSL_S_ice_accepted.pdf | d0981bad5e560a005c2d5bc36115788e624e6de00a0525751d42bdabf11d16c0 | SCHOLARLY (accepted ms) |
| papers/burke2023.xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10666123/fullTextXML | 679231fd99326ee5f9957f1affbe5918af644282f0b46b2d7886bc0fb5ca8e69 | SCHOLARLY |
| papers/hutchison2025.xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11725861/fullTextXML | ef2aef313c9a1636ad3ff6f573c8f873805a9026f08052f806c1f64db1cf3b2f | SCHOLARLY |
| papers/pearson2022.xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9802406/fullTextXML | f0a618ad0a68599856530a89473325af2ec04ca4711dbfa96ba988b59f7fc5f2 | SCHOLARLY |
| GVP eruption table | `../../sources/cache/gvp_holocene_eruptions.csv` (see `sources/PROVENANCE.md`) | df21b092… | PRIMARY (compilation) |

The PMC web page for Burke 2023 returned a reCAPTCHA wall; the Europe PMC XML is the same article.
The CEDA simulation archive (catalogue.ceda.ac.uk/uuid/89cb57d9191b4b81965acb7f154c66df) was not needed and not fetched.
