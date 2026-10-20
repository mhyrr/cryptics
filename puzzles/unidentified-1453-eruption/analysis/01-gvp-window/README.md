# 01 — GVP eruption window

**Question.** Which eruptions in the Smithsonian GVP table could, by date
and size alone, have produced UE 1453?

**Method.** The full Holocene eruption table, via the GVP WFS endpoint
(see `../../sources/PROVENANCE.md`). `window.py` lists start years 1400–1500
and counts eruptions in 1420–1490 with VEI ≥ 4 or unknown VEI.
`covers_1452.py` lists eruptions whose year ± stated uncertainty contains 1452.

**Run.**
```
python3 -I window.py ../../sources/cache/gvp_holocene_eruptions.csv ../../sources/gvp-eruptions-1400-1500.csv > results/window.txt
python3 -I covers_1452.py ../../sources/cache/gvp_holocene_eruptions.csv > results/covers_1452.txt
```

**Result.** 58 eruptions in 1420–1490 (10 with VEI ≥ 4, 48 unknown). 59
eruptions cover 1452. The only VEI ≥ 5 rows covering 1452 are Pinatubo
1450 ± 50 and El Chichón 1360 ± 100 (unit B), both 14C-dated. Kuwae appears
only at 1425 ± 5.

**Limits.** GVP stores one central year and one ± value. It does not store
calibrated ranges, and "14C (uncalibrated)" rows can be decades off. Rows
dated "Sidereal: Ice Core" are circular for this problem. This is a filter,
not a ranking; experiment 06 does the ranking. Scripts written by the
2026-10-20 survey agent and rerun here unchanged.
