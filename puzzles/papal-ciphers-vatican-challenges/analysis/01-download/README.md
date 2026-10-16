# 01 — Download Barb.lat.6960 from DigiVatLib

`python3 -I fetch.py Barb.lat.6960 ../../sources/cache/barb-lat-6960 full`

Fetches the IIIF manifest and every canvas at native size into the gitignored
cache, with `index.tsv` (canvas number, label, file). 194 canvases.

Native size is small: single pages ~748×1088, spreads ~1400×1142 (about 700 px
per page). These are black-and-white microfilm scans, not colour photography.
Barb.lat.6956, by comparison, serves spreads at 2292×1808.
