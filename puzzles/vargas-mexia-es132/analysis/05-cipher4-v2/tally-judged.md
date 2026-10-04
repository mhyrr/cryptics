# Extension tally, judged by reading (step 4, 2026-10-04)

Source listing: `tally.txt` (`tally.py`; frozen rules: `../02-key-extensions/extensions.tsv` + cross-above
doubling in `decode_v2.py`, frozen `8fafd88`). Each occurrence was read in its ±6-token context and judged
"fits" if the extension's value makes the surrounding decoded text Spanish, "misfit" if another value reads
better, "unclear" if the context is unreadable. Rule (frozen in exp 02/03): ≥ 80% of held-out occurrences;
fewer than 3 = untested.

## Held-out: f. 154 (Philip II, 4 Dec 1578; one blind reader, transcribed after the v2 freeze)
| Extension | n | fits | misfit | unclear | Verdict | Examples |
|---|---|---|---|---|---|---|
| 2H = que | 70 | 70 | 0 | 0 | **PASS** | lo que, aunque, aquello, se queda, no he querido, parece que queda |
| Σ = o | 36 | 36 | 0 | 0 | **PASS** | otras, os, relación, confusión, ocasión, oficios, obligación, unión, orden |
| cross above doubles | 29 | 29 | 0 | 0 | **PASS** | assí, esse, dello, Arras, desengañasse (ñ = doubled n), llegó, correspondencia, Lorrena, mill ducados, correos |
| H = ne | 12 | 10 | 0 | 2 | **PASS** (83%; 100% of clear cases) | ternéys, proponer, tienen, dineros, tener, en esto, conviene; l. 48–49 unclear |
| 21. = que | 1 | 0 | 1 | 0 | untested (n < 3) | "el 21. l llegó" reads "el qual" under the base key (21 + dot = qa) |
| 21_ = qui | 0 | – | – | – | untested | – |

## v2 letters (reconciled from two blind readers)
f. 198 is in-sample for the five f. 198 extensions; f. 123 is in-sample for cross-doubling. ff. 87, 157, 179
are held-out for all of them (their v1 tests were on single readers).

| Extension | f. 198 (in) | f. 123 | f. 87 | f. 157 | f. 179 |
|---|---|---|---|---|---|
| 2H = que | 7/7 | 12/12 | 2/2 | 7/8 (1 unclear: "es re-que-dado") | 4/4 |
| Σ = o | 9/9 | 6/6 | 0/1 (unclear) | 1/1 (correo) | – |
| cross doubles | 12/12 | 7/7 (in) | 2/2 (aquellas, honrrar) | 4/4 (correo, mill, esse, -asse) | 1/1 (llevo) |
| H = ne | 4/4 | 4/4 | – | 3/3 (manejo, dinero ×2) | 1/1 (general) |
| 21. = que | 19/19 | – | – | 1/2 (pero que esto; "en lo del que tr-m-ui-ra-to" unclear) | – |
| 21_ = qui | 7/7 (Quiroga, aquí ×2, quiere, quitar, quiete, quiriendo) | – | 1/2 (no quiere; "qui-sto" reads "visto") | – | – |

## Verdicts across all held-out occurrences (ff. 87, 154, 157, 179)
| Extension | Held-out fit | Verdict |
|---|---|---|
| 2H = que | 83/84 (1 unclear) | **established** |
| Σ = o | 37/38 (1 unclear) | **established** |
| cross above doubles (Devos's rule) | 36/36 | **established** (H8) |
| H = ne | 14/16 (2 unclear) | **pass** (88%) |
| 21. = que | 1 fit, 1 misfit (f. 154 "qual"), 1 unclear | **fails** (n = 3, 33%); holds only on f. 198. Outside it, 21. behaves as Tomokiyo's base value (qa → "qua") |
| 21_ = qui | 1/2 | untested (n < 3) |
