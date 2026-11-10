# 18 — Is the Ahklun "0.4-ka" tephra the Aniakchak Half Cone eruption? (07, H10 slice)

**Question.** Kaufman et al. (2012) found a "0.4-ka tephra" in the Ahklun
Mountains, SW Alaska. Is its glass the Half Cone ~400 yr BP eruption (Pink
Pumice and Brown Pumice; Browne et al. 2022)? Or is it Aniakchak II (CFE II,
~3.6 ka), another Aniakchak unit, or a different Alaskan source? This is
NEXT.md "Do first" item 1, the H10 slice of experiment 07.

RESULT: see the bottom of this file, which was written after the run.
Everything above "Result" was written before the target was scored.

## Data

All three datasets were obtained, as single-shard analyses. Nothing was typed
from figures or from memory.

| Dataset | What | URL | Accessed | Tier | sha256 (download) |
|---|---|---|---|---|---|
| Browne, Neal & Bacon 2022, DGGS PR 126, appendix G | 192 matrix-glass EPMA analyses, unnormalised: Pink Pumice (40), Brown Pumice (77), proximal and distal mixed Brown/Pink (53, incl. Ash C at Brooks River), pre-400 yr BP Half Cone tephra (12), and Riehle et al. 2000 Ash C (10). Lab: UAF Advanced Instrumentation Lab and UCLA (PR 126 p. 10); Riehle's 10 rows are USGS. | https://dggs.alaska.gov/webpubs/data/pr126_Appendix-G.zip (landing page https://doi.org/10.14509/30839) | 2026-11-10 | PRIMARY (data) | 47c09d54…0f80 |
| Kaufman et al. 2012, JQS 27(4):344–359, Supporting Table S1 | 1373 single-grain analyses, normalised by the authors; all Ahklun tephras plus the Aniakchak CFE II reference UA 1602 (Zagoskin Lake, T. Ager). The 0.4-ka tephra is UA 1966 (Lone Spruce Pond core 09-LSP-4A) and UA 1779 = UA 1974 (soil pit near Cascade Lake). Lab: U Alberta, JEOL 8900. | https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fjqs.1552&file=JQS_1552_sm_SupplTabS1.pdf | 2026-11-10 | PRIMARY (data) / SCHOLARLY | 198f9972…2845 |
| Davies, Jensen & Kaufman 2022, Geochronology 4:121, SI Table S2 | Single-shard reference glass from the same U Alberta lab: Novarupta-Katmai 1912 (UA 1364), Redoubt 1989–90 (UA 2754), Hayes set H unit F2 (UA 2614), Ruppert tephra (UA 2557), White River Ash north (UA 1044), Opala (Kamchatka, UA 3286), and two more sessions on Aniakchak CFE II UA 1602. | https://gchron.copernicus.org/articles/4/121/2022/gchron-4-121-2022-supplement.zip | 2026-11-10 | PRIMARY (data) / SCHOLARLY, CC BY 4.0 | b30e235d…64d7 |
| (also fetched) Bacon et al. 2014, USGS PP 1810, appendices A and B | Fe-Ti oxides and whole-rock chemistry only, **no glass**. Not usable here. | https://pubs.usgs.gov/pp/1810/ | 2026-11-10 | SCHOLARLY | — |

Full sha256 values are in `results/fetch_sha256.txt`.

**How the Kaufman supplement was obtained.** Wiley returns HTTP 403 to urllib
and to WebFetch. The publisher page was opened in a Playwright browser, and the
supplement links were read from it. The PDFs were then fetched with `fetch()`
inside that browser session. They are not open access. The checked-in
`data/kaufman2012_tableS1.txt` is `pdftotext -layout` (poppler 26.07.0)
applied to the PDF. `fetch18.py` re-downloads the two open datasets. The
Kaufman PDF has to be fetched by hand in a browser.

**Not obtained (record of attempts):**
- **Aniakchak 1931 glass.** Nicholson 2003 (UAF MS thesis) and Nicholson et
  al. 2011 (JVGR 207) are the sources. The AVO geochemical database
  (avo.alaska.edu/geochem) lists the 1931 samples (ANI-01A …, reference 3658).
  But its sample pages show metadata only, and the "Open Geochem Search
  Application" link (/geochemsearch/search) returns 404, both to urllib and in
  a browser. No open table was found.
- **Vent Mountain, New Cone and Blocky Cone glass.** None was found in any
  open source. Bacon 2014 has whole rock only.
- **The AVO copy of Kaufman 2012's samples** (UA1966-P1/P2, UA1974-P1/P2,
  UA1779-P1/P2 exist as records) shows no analyses on its pages. Table S1
  supersedes it in any case.

So **Half Cone cannot be tested against 1931, Vent Mountain, New Cone or
Blocky Cone glass**. That was known before scoring, and it is stated in the
rule below as "no power" for those alternatives.

## Decision rule (frozen 2026-11-10, before the target was scored)

**Disclosure.** The rule is not blind to everything. Kaufman's Table 6
population means for the 0.4-ka tephra were already in hand (17's
`glass17.py`), and Browne's 68.3–69.8 Pink range was known. While locating
blocks in Table S1, I saw printed rows of the 0.4-ka block, including a few
shards near 69 wt% SiO2 in UA 1966. No distance or classification was
computed on the target before this section was written. The false-positive
control below (shards from pre-Half-Cone Ahklun tephras) exists to guard
against reading meaning into a handful of shards.

**Oxides.** SiO2, TiO2, Al2O3, FeOt, MgO, CaO, Na2O and K2O, normalised
anhydrous to 100 over those 8 (MnO, Cl and P2O5 dropped). SC6 drops TiO2 and
MgO, as in glass17.

**Statistics.**
1. **SC (Borchardt)** on population means, taken unchanged from
   `../17-distal-tephra/glass17.py` (`sc`, `norm`). Both SC8 and SC6 are
   reported, and SC8 is the one used in the verdict.
2. **Per-shard standardised distance to a reference population R:**
   d² = Σ over the 8 oxides of ((x − μ_R)/s)², where
   s² = SD_R² + (f·μ_R)² + 0.05². This is a diagonal Mahalanobis distance;
   closure makes the full covariance singular. The f term is an inter-lab
   allowance. f = 0 when the shard and R come from the same lab; f = 0.05 (5%
   relative) across labs, which is primary; f = 0.10 is the sensitivity case.
   A shard is **consistent with R** if d² ≤ 20.09 (the χ²₈ 0.99 quantile, used
   as a convention, not as an exact p-value).
3. **frac(T, R)** is the share of shards in target population T that are
   consistent with R.

**Population verdict, T against R:**
- `match`: SC8 ≥ 0.95 **and** frac ≥ 0.80.
- `no match`: SC8 < 0.90 **or** frac < 0.20.
- `family only`: anything else.

**Reference populations.** All are normalised by me, and the split into
modes follows the authors.
- **Half Cone** (Browne 2022; lab UAF/UCLA):
  - HC_PINK: ANI-02-04 + ANI-02-06 (Pink Pumice).
  - HC_BROWN_DAC: ANI-02-01, 02-02a, 02-03 (Brown Pumice, dacitic glass).
  - HC_BROWN_AND: ANI-01-08, 01-09 (Brown Pumice, andesitic glass).
  - HC_PRE400: ANI-06-01. This is older Half Cone tephra below the Pink
    Pumice, so it is a different post-caldera Aniakchak unit.
- **Aniakchak II / CFE II** (Kaufman S1, lab U Alberta):
  - CFE2_AND: UA 1602 pop 1.
  - CFE2_RHY: UA 1602 pop 2.
- **Non-Aniakchak Alaskan** (Davies S2, lab U Alberta):
  - NK1912_RHY and NK1912_DAC (Novarupta-Katmai 1912, both modes).
  - REDOUBT (1989–90).
  - HAYES_F2.
  - RUPPERT.
  - WRA_N (White River Ash, Mt Churchill).
  - OPALA (Kamchatka) as an extra.
- **Unnamed Alaska Peninsula sources** (Kaufman S1):
  - TEPHRA_B_AND (main mode, all sites).
  - TEPHRA_C.
  - LSP_4.7 (UA 1965).

**Target.** AHK04 is every Table S1 shard of UA 1966, UA 1779 and UA 1974.
That includes the authors' outliers and their "mid-SiO2" and "Tephra B?"
grains. The population verdicts use the authors' two populations:
- AHK_POP1: the low-SiO2 blocks.
- AHK_POP2: the high-SiO2 blocks.

Every shard is also classified individually as one of:
- `HC-only`: consistent with ≥ 1 HC reference and with neither CFE2
  reference.
- `CFE2-only`.
- `both`.
- `neither`.

Here "HC" means HC_PINK, HC_BROWN_DAC or HC_BROWN_AND. HC_PRE400 is reported
separately.

**Controls.**
- (a) **Positive controls.**
  - Split-sample: ANI-02-04 against ANI-02-06 (Pink against Pink) and ANI-01-08
    against ANI-01-09 (Brown andesite against itself).
  - Same material, different session: CFE2 in Kaufman against CFE2 in Davies
    (UA 1602, two other sessions).
  - Distal Half Cone (ANI-32-01, Dumond Ash C, and Riehle Ash C): what share
    of these shards the shard rule calls `HC-only` or `both`.
- (b) **Negative controls.**
  - AHK04 against CFE2. This is "negative" for the Half Cone question.
  - AHK04 against the Davies non-Aniakchak references and Tephra B and C.
  - HC_PINK and HC_BROWN_DAC against NK1912_DAC, the nearest non-Aniakchak
    dacite.
- (c) **Discrimination (power).**
  - HC_PINK and HC_BROWN_DAC against CFE2_RHY, both directions, at f = 0.05
    and f = 0.10.
  - HC_BROWN_AND against CFE2_AND, likewise.
  - HC_PINK against HC_PRE400.
- **False-positive base rate.** Apply the shard classification to the shards
  of three Ahklun tephras from the same lab that are older than Half Cone:
  Tephra A (CFE II at Ahklun sites; UA 1780, 1963, 1967, 1968, 1970,
  1975–1977, excluding the Tephra B population in UA 1977), the 3.1-ka tephra
  (UA 1964, 1793) and the 5.8-ka tephra (UA 1783). Any `HC-only` shard there
  is a false positive.

**Power rule.**
- The rule **has power** at the silicic end if three things hold:
  - both silicic positive controls return `match`;
  - CFE2 Kaufman against Davies returns `match`;
  - HC_PINK and HC_BROWN_DAC against CFE2_RHY return `no match` in both
    directions at both f values.
- The same three conditions apply at the andesitic end, using HC_BROWN_AND
  and CFE2_AND.
- At an end without power, that end's target result is reported but carries
  no weight.
- **For 1931, Vent Mountain, New Cone and Blocky Cone there is no power**,
  because there is no reference glass.

**Target verdicts (fixed in advance):**
1. **"AHK04 is Half Cone"** if AHK_POP2 returns `match` with HC_PINK or
   HC_BROWN_DAC and not `match` with CFE2_RHY. The andesitic end is read the
   same way if it has power.
2. **"AHK04 is CFE II-composition glass, not Half Cone"** if AHK_POP2 returns
   `match` with CFE2_RHY and `no match` with both HC_PINK and HC_BROWN_DAC.
   That means the glass is CFE II itself (reworked) or an eruption tapping
   the same magma. Major elements cannot separate those two.
3. **Otherwise**, "unresolved", with the reason.
4. **Minor Half Cone component.** It is "detected" if AHK04 has ≥ 3
   `HC-only` shards **and** the HC-only share in AHK04 exceeds the pooled
   pre-Half-Cone control share, by one-sided Fisher exact test p < 0.01.
   Otherwise it is "not detected beyond background". Even if detected, such
   shards cannot be told apart from 1931, Vent Mountain or New Cone glass, for
   which there is no reference. So a detection means "Half Cone-like
   post-caldera Aniakchak glass", not "Half Cone".

**Inter-lab check (reported, not part of the verdict).** Novarupta 1912
rhyolite from U Alberta (Davies) is compared with the Begét et al. 1994 mean
quoted by Payne & Blackford 2008 (`glass17.py`). The per-oxide relative
offsets show whether f = 0.05 is a reasonable allowance.

## Run

```
python3 -I fetch18.py            # re-download Browne app. G and Davies SI into data/ (gitignored); Kaufman S1 needs a browser, see above
python3 -I glass18.py > results/glass18.txt
```

Standard library only. `load18.py` holds the three loaders, which do
transcription only. `glass18.py` imports `sc` and `norm` from
`../17-distal-tephra/glass17.py`.

---

## Result (written after the run; output in `results/glass18.txt`)

### Formal verdict under the frozen rule: no power

The frozen power rule returned **NO POWER at both ends**, so by the rule the
target verdict is "stop". The reason is not that Half Cone and CFE II glass
look alike. It is that the rule failed one of its own positive controls.

- **Pink against Pink failed.** ANI-02-06 scored against ANI-02-04 gave
  `family only` (SC8 0.971, frac 0.36). ANI-02-04 has 12 very tight shards
  (SD SiO2 0.13). The two Pink samples differ by about 0.3 wt% SiO2 and
  0.2 Na2O. With f = 0 inside one lab, 18 of the 28 ANI-02-06 shards fall
  outside d² 20.09. The other direction gave `match`, and so did all the
  other positive controls:
  - Brown andesite split;
  - CFE II between Kaufman and Davies sessions;
  - Brown dacite against Pink.
- **The shard rule misses distal Half Cone.** Only 15 of 53 distal Half Cone
  shards (ANI-32-01 at Mother Goose Lake and the Dumond Ash C) come out
  HC-consistent. Dacitic distal shards at 69.3–69.5 SiO2 sit at d² 54–73
  from Pink, because the proximal reference is too tight for them. The rule
  is biased toward false negatives.
- **At the andesitic end the rule truly has no power.** HC_BROWN_AND against
  CFE2_AND gives `family only` (SC8 0.931) at both f values. Half Cone
  andesite glass cannot be told from CFE II andesite glass here.
- **1931, Vent Mountain, New Cone and Blocky Cone:** no power, because no
  reference glass exists.

### What the numbers show (non-binding: the rule failed a control)

The discrimination tests themselves are not close. Neither failed control
can turn a false negative into the pattern below.

| Comparison | f | SC8 | frac | verdict |
|---|---|---|---|---|
| HC_PINK vs CFE2_RHY (both directions) | 0.05 / 0.10 | 0.816 | 0.00 | no match |
| HC_BROWN_DAC vs CFE2_RHY (both) | 0.05 / 0.10 | 0.817 | 0.00–0.02 | no match |
| HC_PINK vs HC_PRE400 | 0 | 0.826 | 0.00 | no match |
| HC_PINK vs NK1912 dacite | 0.05 | 0.886 | 0.00–0.12 | no match |
| **AHK_POP2 (n=96) vs CFE2_RHY** | 0 (same lab) | **0.979** | **0.88** | **match** |
| **AHK_POP2 vs HC_PINK** | 0.05 / 0.10 | **0.828** | 0.04 / 0.06 | **no match** |
| AHK_POP2 vs HC_BROWN_DAC | 0.05 / 0.10 | 0.829 | 0.05 / 0.09 | no match |
| AHK_POP2 vs Katmai 1912, Redoubt, Hayes F2, Ruppert, WRA, Opala, Tephra B and C | — | — | — | no match |
| AHK_POP2 vs LSP 4.7 ka | 0 | 0.938 | 0.95 | family only |
| AHK_POP1 (n=27) vs CFE2_AND / HC_BROWN_AND | — | 0.975 / 0.923 | 0.74 / 0.41–0.78 | family / family (no power) |

1. **The bulk of the Ahklun 0.4-ka bed is CFE II-composition glass, not Half
   Cone glass.** Its rhyodacite mode, 96 shards, matches the CFE II reference
   from the same lab and does not match Pink or Brown dacite. Pink and Brown
   glass carry about 40% more FeO, 50% more TiO2, 60% more MgO and 45% more
   CaO than CFE II rhyodacite; CaO is closer to 50%. Pink also has 2 wt%
   less SiO2. The inter-lab check (Novarupta 1912) found U Alberta reading
   13–24% lower than Begét in TiO2, FeO, MgO and CaO, and +0.2% in SiO2.
   Suppose Browne's lab read high by that much. Pink measured at U Alberta
   would still carry FeO about 3.0, CaO 2.2, TiO2 0.64 and SiO2 69.4. CFE II
   is 2.5, 1.75, 0.49 and 71.4. So the gap survives the largest offset
   observed. Even SC on means alone puts AHK_POP2 at 0.83 to Pink, below the
   0.90 "different" line.
2. **A minor Half Cone-like component is present above background.**
   - Six of 135 0.4-ka shards are `HC-only`. All six are dacite at 68.3–70.0
     SiO2 with FeO 3.0–4.0 and CaO 2.3–3.0. Two sit within d² 5 of Pink at
     f = 0.05, and four at f = 0.10.
     In the three older Ahklun beds (Tephra A, 3.1 ka, 5.8 ka) the rate is
     2 of 516. One-sided Fisher p = 1.4×10⁻³, so the frozen test returns
     "detected". At f = 0.10 the count is 11/135 against 4/516.
   - About five more shards at 65.7–67.5 SiO2 are closest to the
     **pre-400 yr BP Half Cone tephra** (ANI-06-01), at d² 1–17. These
     include Kaufman's "mid-SiO2 pop – on trend" and UA1974-19.
   - Four of the six HC-like dacite shards, and four of the five pre-400-like
     shards, are in UA 1966 at Lone Spruce Pond. Kaufman notes that this
     sample "contains abundant detrital glass".
   - Because the frozen rule failed a positive control, this detection is
     provisional. And even if it holds, it says only "post-caldera Aniakchak
     dacite of Half Cone type". The rule cannot exclude New Cone, Vent
     Mountain or 1931 glass, which had no reference.
3. **A mirror case is in Browne's own data.** The distal Half Cone deposit
   ANI-32-01 (Mother Goose Lake) contains 2 of 28 shards that are CFE II
   rhyodacite: SiO2 71.7 and FeO 2.4, at d² 6 from CFE2_RHY. A known Half
   Cone fall can therefore carry a few percent of reworked CFE II glass. The
   Ahklun bed is the reverse: about 90% CFE II glass with a few percent of
   Half Cone-type glass.

**Reading.** The Ahklun 0.4-ka tephra is not a Half Cone fall bed in the
sense H10 needs. Its glass is overwhelmingly CFE II composition. That fits
the authors' own first explanation: CFE II glass reworked during "landscape
destabilization", or an eruption tapping the same magma, which major
elements cannot separate. Their trace-element data (Fig. 9) also call it
indistinguishable from CFE II. A few percent of the shards are younger
post-caldera dacite, which could be Half Cone. So the soil-pit maximum age
(wood and leaves below the bed, 1435–1468 CE) dates the bed, not the Half
Cone eruption. Any Half Cone shards in it constrain Half Cone only as
"no later than the bed". The lead that NEXT.md hoped for, "Brown + Pink
match puts Half Cone in Ahklun; the soil-pit date becomes H10's first
own-date evidence", **did not materialise**.

### Ages in the literature (quoted)

**Half Cone eruption**
- **Bacon et al. 2014, USGS PP 1810.**
  - Table 1 (p. 17): "Pink Pumice fall 380±50 [14C yr BP] … MSWD 0.09 …
    310–510 [cal yr BP 2σ] … 350±20 / 470±40 [preferred ±1σ] … Weighted mean
    of 2 dates." That is 1440–1640 CE (2σ).
  - p. 27: "We consider the weighted mean of 380±50 yr B.P. (table 1) for the
    two youngest dates, which are for wood and for which stratigraphic
    context is clear, to provide the most accurate constraint on the Pink
    Pumice eruption."
  - Also in Table 1: "New Cone tephra 400±30 … 430–510 … Weighted mean of
    3 dates."
  - SCHOLARLY, https://pubs.usgs.gov/pp/1810/ (pdftotext of pp1810.pdf,
    sha256 d87fa742…c35c9).
- **Browne, Neal & Bacon 2022, DGGS PR 126.**
  - Abstract: "The largest eruption from Aniakchak volcano since the ~3,400
    yr B.P. caldera-forming eruption occurred ~400 yr B.P. from Half Cone".
  - p. 7: "emplaced 380±50 14C yr B.P. (310–510 calibrated 2σ age range
    calendar yr B.P.; Bacon and others, 2014)".
  - p. 10: "The most recent radiocarbon analyses presented here are from wood
    collected within soil below the distinctive Pink Pumice fall deposit.
    One standard and one AMS date of these wood fragments returned median
    probability calibrated ages of 400 and 424 yr B.P., respectively."
    Also: "In the mid 1980s, three dates that were older by more than a
    century were obtained from both wood and soil below the Pink Pumice.
    Unfortunately, the data sheets … are missing".
  - Table 1 (p. 11):
    - GX-29531: 360 ± 80, 1411–1670 cal AD.
    - B-76809: 390 ± 60, 1405–1661 cal AD.
    - I-14222: 500 ± 80, 1297–1523 cal AD.
    - USGS-2358 (soil): 590 ± 90, 1261–1475 cal AD.
  - PRIMARY/SCHOLARLY, https://doi.org/10.14509/30839.
- **Neal et al. 2001, USGS OFR 00-519.**
  - p. 6: "Two young, but prehistoric, explosive events at Aniakchak
    occurred closely spaced in time about 400 years BP. The first is inferred
    to have originated from the flank of Vent Mountain … The second, and
    younger, eruption occurred at Half Cone".
  - Timeline figure: "390 Major explosive eruption and lava flow; destruction
    of Half Cone"; "400 Explosive eruption from New Cone"; "560 Explosive
    eruption (from Half Cone?)".
  - Fig. 13 caption: "last violent eruption of Half Cone (about 390 years
    ago)".
  - SCHOLARLY (USGS), text in `../11-aniakchak-date/data/neal2001.txt`.
- All three are maximum ages: every dated sample lies below the Pink Pumice
  (canon). Nothing dated lies above it.

**Kaufman et al. 2012 on the 0.4-ka tephra** (text in
`../11-aniakchak-date/data/kaufman2012_jqs_ahklun.txt`)
- Abstract: "The 3.1 and 0.4 ka tephras have glass major- and trace-element
  geochemical compositions indistinguishable from prominent Aniakchak tephra,
  and might represent redeposited beds."
- Results: "This tephra was sampled from Lone Spruce Pond (UA 1966) and from
  the soil pit near Cascade Lake (UA 1779 = 1974). The mean of the two ages
  is 0.4 ± 0.1 (1σ) ka. Similar to the 3.1-ka tephra, the major- and
  trace-element geochemistry of this tephra is indistinguishable from
  Aniakchak tephra. The tephra layer appears to be widespread across the
  landscape, directly below the surface organic mat and capping a buried A/B
  soil horizon. It is typically separated from the underlying Aniakchak
  tephra by centimeters to decimeters of loess or other non-volcanic
  sediment. The sample from Lone Spruce Pond (UA 1966) also contains
  abundant detrital glass (Table S1)."
- Discussion, on the source: "These beds overlie the Aniakchak tephra, and
  they may comprise shards reworked from it. On the other hand, the beds
  comprise relatively pure tephra, appear to be conformable in the
  sedimentary sequence and are of indistinguishable age in different lakes.
  If they are reworked, then we speculate that they date to an interval of
  landscape destabilization … Alternatively, the 3.1- and 0.4-ka tephra beds
  could be primary deposits erupted from Aniakchak volcano subsequent to the
  3.7 ± 0.2 ka eruption of Tephra A, even though their major and
  trace-element geochemistry is indistinguishable. Neal et al. (2001)
  recognized at least six widespread tephra deposits from explosive
  eruptions of Aniakchak volcano that occurred following the
  caldera-forming eruption, including two events that occurred around
  0.4 ka. The SiO2 data presented by Browne et al. (2004) indicate that the
  geochemistry of the 0.4-ka tephra from Half Cone is similar, but not
  identical, to the Aniakchak tephra."
- Age constraints:
  - Table 4: Lone Spruce Pond 377 ± 62 cal BP (age-depth model); Cascade
    test pit 505 ± 20 cal BP, footnoted "14C age from below tephra bed";
    "mean age" 441 ± 64.
  - Table 2, soil pit near Cascade Lake: UCIAMS-23856 435 ± 15 14C BP, 505 ±
    20 cal BP, "Wood & leaves", at 6 cm.
  - Table 2, Lone Spruce Pond core 09-LSP-4A: UCIAMS-72311 360 ± 60 14C BP,
    406 ± 86 cal BP, on "Terrestrial leaf fragments; moss stems and leaves",
    at 35.1 cm. AVO's sample record puts UA1966-P2 at "34.2 cm bottom depth
    in core (tube depth, not tephra-free depth)". So this date appears to lie
    about 1 cm below the tephra, but whether the two depths are on the same
    scale is unverified. 17 did not use this date.
- Kaufman never attributes the bed to Half Cone. The sources they name are
  CFE II (reworked) or an unspecified post-caldera Aniakchak eruption.

## Unverified claims

- That UCIAMS-72311 (35.1 cm) and the UA1966 tephra depth (34.2 cm, AVO
  record) are on the same depth scale.
- That the "pre-400 yr BP Half Cone" tephra (ANI-06-01) is representative of
  older Half Cone glass in general. It is one sample, with 12 shards.
- That New Cone, Vent Mountain and 1931 glass differ from Half Cone dacite.
  No reference glass was obtained, so the HC-like Ahklun shards could be any
  of them.
- The inter-lab allowance f = 0.05–0.10 rests on one comparison (Novarupta
  1912, U Alberta against Begét 1994). That comparison showed offsets up to
  24% in low-abundance oxides. So f = 0.05 is not generous for MgO, TiO2,
  FeO or CaO. A shared secondary standard was not available.

## What would settle it

1. Re-run with a rule that passes its positive controls: reference SD pooled
   across samples of one unit, plus a between-sample term. Pre-register it
   **before** looking at the target again. This is a rule-design fix. Because
   the target has now been seen, a rerun is confirmatory only for the
   bulk-CFE II result, which does not depend on the rule's tightness.
2. Glass for New Cone, Vent Mountain and the 1931 eruption: the AVO geochem
   database (search app currently 404), Nicholson 2003/2011, or a request to
   ADGGS/AVO.
3. Trace elements on the six HC-like dacite shards (Kaufman/Jensen lab), to
   test whether they are Half Cone and not reworked older post-caldera glass.
