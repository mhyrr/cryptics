# 11 — Aniakchak date

**Question.** If the Aniakchak Half Cone Plinian eruption made UE 1453 (H10),
its own deposits must date to about 1452–53 CE. Do they? We test this from
the deposits alone. No polar-ice date enters.

## Pre-registration (written 2026-10-20, before any bracketing date was collected)

What I knew when I wrote this: the four Half Cone ages and three New Cone
ages in `../06-candidate-ranking/lab_ages.csv` (Bacon et al. 2014, Tables 1–2),
06's result (two wood ages, 95 % 1442–1636 CE), and Bacon's Figure 5C, which
puts New Cone tephra below the Pink Pumice. I had not looked for any distal
or archaeological bracket.

**Age model.** One event, T (calendar year CE of the Half Cone Pink Pumice
fall). Flat prior on T over the model range 1300–1800 CE, 0.1-yr grid. Each
date i has a calendar age t_i with an IntCal20 likelihood and a flat prior.
Its stratigraphic relation sets a constraint:

- `below` (dated material formed before the tephra fell): t_i ≤ T.
  Marginalised, it multiplies p(T) by F_i(T), the cumulative of its
  calibrated pdf.
- `above` (formed after): t_i ≥ T, factor 1 − F_i(T).
- `same` (killed by the eruption, e.g. outer rings of a tree in growth
  position, or a modelled tephra age): factor L_i(T), its calibrated pdf.

p(T) ∝ Π below F_i(T) · Π above (1 − F_i(T)) · Π same L_i(T). Depth gaps
are ignored. This keeps the brackets loose, never too tight. A published
age-depth model's tephra age enters as a separate line, never multiplied
with the raw dates it was built from.

**Material rules (fixed now).**
- Wood or charcoal inside the fall deposit, with no statement that it is
  outer rings or in growth position: `below` (inbuilt age makes it a
  maximum age for the eruption). This is the main model. Sensitivity S1
  treats Bacon's two wood ages as `same`, as Bacon and 06 do.
- Charcoal, wood, plant macrofossils, peat: used in the main model in any
  position.
- Bulk lake sediment and soil humic fractions: old carbon makes them too old.
  Below the tephra, that is still a valid `below`. Above the tephra, a too-old
  date would wrongly push T early. Bulk or humic `above` dates are excluded
  from the main model and enter only in sensitivity S2.
- Archaeological charcoal: used as charcoal. Hearth charcoal above the tephra
  can carry old wood; the leave-one-out check below handles it.
- Marine material (shell, marine mammal, fish, mixed-diet human bone):
  excluded from all models and listed. No ΔR is defensible without a local
  study, and the Alaska Peninsula ΔR varies by hundreds of years.
- Undated-position dates ("associated with the tephra") enter as `below`
  if on terrestrial organics, else listed only.
- 210Pb and varves cannot reach the 15th century in these lakes unless a
  paper says so. A varve-counted tephra age enters as `same` with a uniform
  pdf over its stated error.
- Unit identity. A date enters only if the paper names the late-Holocene
  Aniakchak Half Cone / Pink Pumice / "~400 14C BP Aniakchak" tephra, or a
  correlation the paper itself makes to it. Ambiguous units are listed, not
  used.

**Leave-one-out.** For each date, P(its constraint holds | the others). Any
date below 0.05 is flagged; sensitivity S3 drops all flagged dates. The main
result does not change after seeing the flags.

**Decision rule.** Let H be the 95.4 % HPD of p(T), W its width in years, and
P = P(1451.0 ≤ T < 1454.0). Baseline B = 3 / W (a flat date over the HPD).
- **refuted** if H excludes all of 1452.0–1454.0;
- **weakened** if H includes it but P < 0.5 · B;
- **supported** only if W ≤ 30 yr and H contains 1453;
- otherwise **not excluded** (status unchanged).
The verdict uses the main model. S1–S3 and the "two proximal ages only"
result are reported beside it and cannot change the verdict.

**Known-case test (before reading the Half Cone result).** The same code
runs on (a) synthetic brackets made from IntCal20 at a known date (seed
1453, ages drawn as the curve mean + N(0, σ), σ = 40) and (b) one real
dated tephra with published 14C brackets, chosen as the first one found
with brackets on both sides. Pass: the known date lies inside H.

**New Cone.** Run the same model for the New Cone tephra with its three
Bacon ages and the stratigraphic order New Cone < Pink Pumice.

## Which unit is which

All three proximal sources agree. Bacon et al. (2014) Fig. 5C is the composite caldera section.

| Unit | Age (14C BP) | Order | Size | Source |
|---|---|---|---|---|
| Half Cone lower light pumice | 840 ± 30 | oldest | — | Bacon 2014 Table 1 p. 17 |
| Half Cone upper light pumice | 570 ± 40 | | — | same |
| New Cone tephra (flank of Vent Mountain) | 400 ± 30 | below the Pink Pumice | surges in the caldera, fall to N and NE; no volume given | Bacon 2014 Fig. 5C, p. 24; Neal 2001 p. 6 |
| **Half Cone Pink Pumice + Brown Pumice** (the "~400 yr B.P. eruption") | 380 ± 50 | younger | Plinian; ≥ 5.4 km³ tephra, ~1.5 km³ DRE | Browne 2022 abstract p. 1; Bacon 2014 p. 27 |

- The Pink Pumice (dacite) and the overlying Brown Pumice (andesite) are two
  phases of one eruption. The Brown Pumice is the larger: ≥ 3.5 km³ of fall
  against ~1.3 km³ for the Pink (Browne 2022, abstract and p. 42).
- Neal et al. (2001, p. 6) give 0.75–1.0 km³ for the same eruption. Browne
  (2022) raised it to ≥ 5.4 km³ bulk tephra. Both name Half Cone as the vent
  and the Half Cone event as "one of the most violent" since the caldera.
- "Ash C" at Brooks River (Katmai, ~230 km NE) is the Brown Pumice phase
  (Browne 2022 pp. 41–42, after Riehle et al. 2000).
- Not the same unit: the "0.4-ka tephra" of Kaufman et al. (2012) in the
  Ahklun Mountains. Its glass is bimodal (59 and 71 wt% SiO2) and
  "indistinguishable from" the 3.6 ka caldera-forming (CFE II) tephra; the
  authors say it may be redeposited. Half Cone Pink glass is dacite. Also not
  the same: Cascade Lake's late-Holocene Aniakchak cryptotephra (Davies et
  al. 2022), which matches CFE II.

## What was found (`brackets.csv`)

Nine 14C ages are usable or listed. Every one is a `below` date.

- **Half Cone, 5 ages, all below the Pink Pumice.** Browne et al. (2022, p. 10)
  settle the position of the two ages Bacon used: "wood collected within soil
  below the distinctive Pink Pumice fall deposit". GX-29531 360 ± 80 and
  B-76809 390 ± 60 (wood). Three older ages (I-14222 500 ± 80 wood; two
  USGS-2358 bulk soil, 590 ± 90 and 590 ± 160) are also below; their data
  sheets are lost.
- **New Cone, 3 ages** "associated with" the tephra (Bacon 2014 p. 24), two of
  them on a queried unit ("New Cone?").
- **Ahklun 0.4-ka tephra, 1 age** below it (UCIAMS-23856 435 ± 15, wood and
  leaves; Kaufman 2012 Table 2). Listed, not used: the unit is not Half Cone.
- **Above the tephra: none.** No dated material above the Half Cone deposits
  was found in any open source. The only upper bound is physical: the 1931
  tephra overlies the Half Cone deposits (Bacon 2014 p. 27).
- **Archaeology: none usable.** Barton et al. (2018) and their open dataset
  (CADB, 92 + 394 dates, Chignik–Meshik) do not record position relative to
  the Half Cone tephra. The Brooks River Ash C brackets are in Riehle et al.
  (2000) and Dumond (2004); both are paywalled. VanderHoek & Myron (2004) is
  restricted by NPS. VanderHoek & Nelson (2007) concerns the 3.4 ka eruption.
- **Lake cores: none on the Half Cone unit.** Lone Spruce Pond and the Cascade
  soil pit (Ahklun) carry the 0.4-ka tephra above. Kodiak peat (Frontiers
  2019) has no late-Holocene tephra.
- **Marine dates: none.** No ΔR was needed.

## Method

`bracket_model.py` is the pre-registered one-event model. It imports 06's
IntCal20 code (`../06-candidate-ranking/pipeline.py`, written for
`recal14c.py`). `run11.py` runs MAIN, the sensitivities and the post hoc
runs. `knowncase.py` runs the known-case tests. Grid 0.1 yr.

## Run

```
python3 -I fetch11.py data       # optional: the papers, with sha256 (Bacon 2014 is in 06/data/lit)
python3 -I knowncase.py ../06-candidate-ranking/data/intcal20.14c knowncase.csv > results/knowncase.txt
python3 -I run11.py ../06-candidate-ranking/data/intcal20.14c brackets.csv > results/run11.txt
```

IntCal20 comes from 06 (`python3 -I fetch.py data` there). Runtime about 10 s.
Standard library only. `data/` is gitignored.

## Known-case test (`results/knowncase.txt`)

Run before the Half Cone result was read, as pre-registered.

- **Synthetic, 2 below + 2 above:** the 95 % HPD covers the true date in
  58/60 trials (mean width 133 yr). Pass.
- **Synthetic, 3 below only:** covers it in **13/60**. Fail. With no `above`
  date, the posterior rises to the top of the prior range and stays flat.
  The true date sits at the lower edge, which the HPD trims off. This is the
  Half Cone data configuration.
- **Loch Portain, Hekla 1510** (Dugmore et al. 1995, Fig. 1): the first real
  case found with dates on both sides. Two peat dates sit inside a diffuse
  tephra zone, one 10 cm below.
  - K1, zone dates taken as contemporaneous: HPD 1328–1336, 1396–1480. Fail.
    Peat in the zone dates ~100 yr too old.
  - K2, zone order (lower date below, upper above): HPD 1331–1622. Pass.
  - K3, the deep date only (below-only): HPD 1300–1777. Pass, but uninformative.

Reading. The model works when a tephra has dates on both sides. It does not
work below-only. Treating dated material as contemporaneous can exclude the
truth.

## Result (`results/run11.txt`)

| Run | Status | 95 % HPD (CE) | P(1451–1454) | P/B | Rule |
|---|---|---|---|---|---|
| MAIN: 5 below, flat 1300–1800 | pre-registered | 1550–1800 | 0.0001 | 0.01 | refuted |
| MAIN, prior to 1700 / 1930 | sensitivity | 1527–1700 / 1571–1930 | 0.0001 / 0.0000 | ≤ 0.01 | refuted |
| S1: two wood ages as `same` (= 06) | pre-registered | 1442–1530, 1537–1636 | 0.014 | 0.89 | not excluded |
| S2, S3 | pre-registered | = MAIN (no bulk `above` dates; no LOO flag) | | | |
| S4: New Cone ≤ Half Cone, all below | pre-registered | 1627–1800 | 0.0000 | 0.00 | refuted |
| S6: wood ages T − U(0, G), G = 25 | post hoc | 1460–1551, 1553–1650 | 0.004 | 0.23 | refuted |
| S6: G = 50 / 100 / 200 | post hoc | 1470–1664 / 1487–1699 / 1512–1774 | ≤ 0.0014 | ≤ 0.09 | refuted |

The pre-registered rule, applied to MAIN, returns **refuted**. I do not adopt
it. MAIN is a below-only model, and that configuration failed its own
known-case test (13/60). Its "refutation" comes from the open top of the
prior, not from the dates.

What the dates do say (post hoc, `run11.py` last two blocks):

- If Half Cone erupted in 1453, both clear-context wood pieces died before
  1454. IntCal20 gives P = 0.080 (GX-29531) and 0.112 (B-76809) for that.
- IntCal20 falls steeply just before 1453: 423 ± 10 BP at 1453.0, 454 at
  1443, 491 at 1428, 561 at 1403. The two woods read 379 ± 48 combined.
- Absolute fit of both woods to an eruption in 1453, if they died g years
  earlier: g = 0, p = 0.64; g = 10, p = 0.29; g = 25, p = 0.07; g ≥ 50,
  p < 0.01.
- So 1453 survives only if the wood died within about 10–20 years of the
  eruption. The fit at g = 0 is good (0.9σ). Any realistic inbuilt age or
  soil residence time makes it poor.

**Verdict on H10 (my judgment; the mechanical rule is set aside above):
weakened, not refuted.** The deposit's own dates prefer about 1460–1650.
They allow 1453 only if the dated wood was killed by the eruption or died
within ~20 years of it. Nothing in the record says either way. A refutation
would need a dated `above` bracket, or the outer-ring age of the wood.

**New Cone.** It cannot be the 1453 candidate on present evidence.
- Its three ages taken as one event allow 1453 (HPD 1439–1522, 1575–1624; P/B
  1.45). Below-only, they do not constrain it.
- It lies below the Pink Pumice, so it predates Half Cone. If B-77038
  (340 ± 50, wood, "New Cone?") is New Cone material, it died before
  1454 with P = 0.015 only, so New Cone, and Half Cone above it, are later (S4, S6 joint: Half Cone
  1492–1667 at G = 50).
- Size: no published volume. Neal (2001, p. 6) describes surges inside the
  caldera and fallout to the N and NE. Nobody calls it Plinian. It is not a
  plausible 10 Tg S source without a volume.

## Limits

- No `above` date exists in open sources. Every Half Cone constraint is a
  maximum age. This is the wall.
- The gap model (S6) is post hoc. Its G is not known. Shrub wood at the
  ground surface could be very young when buried; it could also be decades
  old.
- Wood "within soil below" pumice could be a root that grew down later. A root
  reads too young, and is not a valid `below` date. That would remove the
  tension with 1453, but also remove the constraint. The papers do not say
  how the wood was identified.
- The Bacon/Browne lab ages were run 1985–2002 in four labs. No lab offset is
  modelled.
- 06 combined the two wood ages as `same`. Browne (2022) shows they are
  `below`. 06's HPD (1442–1636) is the most generous reading, not the
  neutral one.

## Ancillary facts for later tests

- **Melt inclusions (Pink Pumice dacite):** Bacon (2000, 2002, Eos abstracts)
  measured dissolved volatiles in plagioclase-hosted melt inclusions. Bacon
  et al. (2014, p. 67): the dacite "partially degassed, losing any CO2 and
  some sulfur but retaining ~3 weight percent H2O, before erupting"; storage
  ~110 MPa. No sulfur concentrations are given in PP 1810 or PR 126. The
  Eos abstracts are unread. `SCHOLARLY`, abstract-level.
- **Δ33S / sulfur isotopes on Aniakchak:** none found in the sources read.
- **Glass:** Browne 2022 appendix G (cited p. 40) holds matrix-glass major
  elements for Pink and Brown Pumice and Ash C. DGGS offers ASCII appendices
  for download (A–C seen; G not checked). Pink Pumice
  matrix glass is dacite to trachydacite; Brown Pumice is mostly andesite.
  This is the reference test 07 needs.
- **Dispersal:** the Pink plume went N and NE, the Brown NE to ≥ 230 km
  (Brooks River). Column heights ~15–20 km (Pink) and ~20–24 km (Brown)
  (Browne 2022, abstract). K. Wallace (USGS, oral commun. in Browne 2022
  p. 42) reports the tephra may occur across Cook Inlet.
- **Pre-eruption temperatures:** Fe-Ti oxides 944–997 °C (Pink), 959–985 °C
  (Brown) (Browne 2022 abstract).

## Unverified claims

- VanderHoek & Nelson (2007): the brief recalled it as an archaeological
  bracket for the late-Holocene tephra. Searches find only their work on the
  3.4 ka eruption (a 2002 GSA abstract; NPS summaries). Not found.
- Riehle et al. (2000): Browne (2022 p. 41) says "radiocarbon ages for Ash C
  indicated an age of ~400 yr B.P.". The dates themselves are behind a
  paywall. Unverified.
- Dumond (2004): the abstract says the Brooks River ashes' timing "matches only
  imperfectly" Aniakchak ages. The dates are unread.
- NPS Brooks River cutbank page (`POPULAR`): an ashfall "about A.D. 1350"
  under houses occupied A.D. 1400–1650. Unit not named. Not used.
- The wood is shrub wood, not driftwood: likely from the inland sites, not
  stated.

## Provenance

| Source | URL | Tier | Read how | sha256 |
|---|---|---|---|---|
| Browne, Neal & Bacon 2022, DGGS PR 126 | https://doi.org/10.14509/30839 | SCHOLARLY | full PDF | 7c0ead25…aa86 |
| Bacon et al. 2014, USGS PP 1810 | https://pubs.usgs.gov/pp/1810/ | SCHOLARLY | full PDF (06 copy) | d87fa742…35c9 |
| Neal et al. 2001, USGS OFR 00-519 | https://pubs.usgs.gov/of/2000/0519/ | SCHOLARLY (agency) | full PDF | ae708b16…21a4 |
| Kaufman et al. 2012, J. Quat. Sci. 27 | https://doi.org/10.1002/jqs.1552 | SCHOLARLY | author PDF | fbe3a62e…10fc |
| Davies, Jensen & Kaufman 2022, GChron 4 | https://gchron.copernicus.org/articles/4/121/2022/ | SCHOLARLY | WebFetch, no file | — |
| Dugmore et al. 1995, Radiocarbon 37(2) | https://doi.org/10.1017/S003382220003085X | SCHOLARLY | full PDF; Fig. 1 read as image | c800bf6f…f683 |
| Barton, Shirar & Jordan 2018 dataset (CADB) | https://www.cadb.pitt.edu/bartoncarbon/ | SCHOLARLY (data) | master.txt, carbon.txt | 68b30034…c9de, 7a9de638…8b5a |
| Barton et al. 2018, Radiocarbon 60(2) | https://www.cambridge.org/core/journals/radiocarbon/article/holocene-human-occupation-of-the-central-alaska-peninsula/F9082314B32783E550CAD8D64F6A41C9 | SCHOLARLY | abstract only (paywall) | — |
| Riehle et al. 2000, GSL SP 171 | https://doi.org/10.1144/GSL.SP.2000.171.01.19 | SCHOLARLY | abstract only (403) | — |
| Dumond 2004, Arctic Anthropology 41(2) | https://doi.org/10.1353/arc.2011.0023 | SCHOLARLY | abstract only (paywall) | — |
| Kodiak peat, Frontiers Earth Sci. 2019 | https://doi.org/10.3389/feart.2019.00061 | SCHOLARLY | WebFetch, no file | — |
| AVO Vent Mountain tephra page | https://avo.alaska.edu/eruption/aniakchak-vent-mountain-tephra | SECONDARY | WebFetch | — |
| NPS Brooks River cutbank page | https://www.nps.gov/articles/brooks-river-cutbank-project.htm | POPULAR | WebFetch | — |
| IntCal20 (Reimer et al. 2020) | via 06 `fetch.py` | PRIMARY (curve) | 06 data | 974a6664…168e |
