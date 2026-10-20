# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

- H1 Kuwae as the 1453 source. Refuted by the literature before this dive
  opened (Abbott 2021; Sigl 2013, 2015). Recorded 2026-10-20.

---

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
