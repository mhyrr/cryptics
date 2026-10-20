# Provenance

One line per file in this folder: filename, origin URL or citation, date
fetched, and what (if anything) was changed from the original.

| File | Origin | Fetched | Changes |
|---|---|---|---|
| cache/gvp_holocene_eruptions.csv (gitignored) | GVP WFS `GVP-VOTW:Smithsonian_VOTW_Holocene_Eruptions`, outputFormat=csv: https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0&request=GetFeature&typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Eruptions&outputFormat=csv | 2026-10-20 | None. 11,089 rows. sha256 df21b092a630c647d6f2c15174d299a8d43564118f3eefdbf4a9aeaff9cba86f |
| gvp-eruptions-1400-1500.csv | Filtered from the file above by `analysis/01-gvp-window/window.py` | 2026-10-20 | Rows with start year 1400–1500; lat/lon columns split out of GeoLocation |
| survey-2026-10-20/*.md | Four Opus survey agents (ice cores, volcano databases, climate and documentary proxies, tephra), 2026-10-20 | 2026-10-20 | None. Model-written reports; every claim is tiered and cited, and each has an Unverified claims section |
