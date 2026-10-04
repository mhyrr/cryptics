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

## v2 letters (in-sample for ff. 198, 123 where the extensions were found; held-out for 87, 157, 179)
To be completed when the reconciled v2 texts of ff. 157 and 198 are committed.
