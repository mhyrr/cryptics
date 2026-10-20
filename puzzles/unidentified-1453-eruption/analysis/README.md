# analysis/

One subfolder per experiment: `NN-short-name/` with its own `README.md`
stating the question, the method, how to run it, and the result. Heavy
outputs go in `out/` (gitignored); check in a summary. If the experiment
needs more than the standard library, it gets a `pyproject.toml` here and is
run with `uv run`.

| # | Experiment | Question | Result | Bears on |
|---|---|---|---|---|
| 01 | gvp-window | Which GVP eruptions could have produced UE 1453 by date and size? | 58 in 1420–1490 with VEI ≥ 4 or unknown; 59 cover 1452; only VEI-5 rows covering 1452 are Pinatubo 1450 ± 50 and El Chichón 1360 ± 100 | H5–H8 |
| 02 | ice-onset | Was the 1453 layer searched for shards? When does the sulfate start, and is the Antarctic signal real? | No published search of TUNU2013 or NEEM; onset 1453.0–1453.1 at the Na maximum, which cannot give the season; window early 1452–mid 1453; Antarctic signal in 5 of 15 cores (p = 0.0006); one pulse | H4, H5, H9 |
| 03 | latitude-posterior | How well do asymmetry, isotope class and the Marshall emulator predict latitude, and what do they give for 1453? | Asymmetry and emulator exclude SHET only; isotope class 7/7 but 2 out of sample; P(NHET) 0.69–0.94, 0.44 out of sample | H2, H3 |
| 04 | cooling-fingerprint | Does the latitude gradient of summer cooling separate extratropical from tropical eruptions? | No: AUC 0.39–0.49 in three networks; 1453 not classified | H2, H3 |
| 05 | documentary-onset | What do dated documents record in 1452–54? | Cold in Korea from 2 Aug 1453; Ming winter disaster from 15 Dec 1453 (6× baseline); no dimmed sun anywhere; method detects 1 of 3 known eruptions | H3, criterion 2, 6 |
| 08 | summer-1452 | Was summer 1452 already cold, and does that bound the season? | 1452 normal (MXD 73rd percentile, 0/14 sites ≤ −1); eruption-year response does not separate season (AUC 0.53–0.61); window 1452.9–1453.5 if NHET, 1452.0–1453.1 if tropical; 1453 top frost-ring year at Almagre 1250–1993 | H2, H3, criterion 2 |
| 09 | ice-tracers | Do non-sulfur tracers say Icelandic or distant, and did ash precede sulfate? | No: pre-registered LOO 0.31 (NEEM), 0.70 p 0.081 (TUNU2013); TUNU2013 Al pulse at 1453 onset, post hoc; no ash-before-sulfate evidence; particle record on request | H5, H6 |
| 10 | harvest-dates | Do grape-harvest dates show when the 1452/53 cooling arrived? | No: known large eruptions hit the 90th percentile 3/12 (p 0.37); 1452 normal, 1453 late (89th percentile); 1453–56 may be Dijon fills | criterion 2 |
