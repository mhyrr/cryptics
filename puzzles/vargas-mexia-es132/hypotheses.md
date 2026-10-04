# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` /
`refuted` / `superseded by Hn`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H1 | Tomokiyo's Cipher 4 table, applied mechanically, reads f. 198–199 as continuous Spanish that joins the clear text. | supported (with 5 extensions; held-out test pending) | Decode both blind transcriptions in code; measure the share of tokens decoded and of joins to clear text that are grammatical; list unknowns. | 2026-10-03: both blind readings decode to Spanish joining the clear text (`analysis/01-decode-f198/`, `analysis/02-key-extensions/`). Five extensions needed: 21.=que, 21_=qui, 2H=que, H=ne, Σ=o. |
| H2 | The digit runs written together (e.g. "176", "246") are a base number 1–23 followed by the vowel mark "6" (-o), so a deterministic parse resolves them. | open | Parse rule frozen before decoding; count runs it cannot parse; check parses against clear-text joins. | Key structure. |
| H3 | F. 198 contains Pérez's defence against the Escobedo accusations ("mi inocencia", "falso testimonio") and names the Marqués de los Vélez. | supported (provisional reading v1) | A full decoded reading of the passages around those words (README criterion 5). | `analysis/02-key-extensions/reading-f198-v1.md`: Escovedo's lawsuit ended in Pérez's favour, but the delay cost him the office "de Vargas"; the King refused him leave to retire; the Archbishop of Toledo had the Princess of Éboli urge him to stay. |

| H4 | The five f. 198 extensions are real features of Cipher 4 (not reader errors or one-letter quirks). | open | Held-out Cipher 4 letter (Pérez, 13 Sept 1578), transcribed blind after the freeze (`11985aa`): each extension consistent at ≥ 80% of its occurrences. | In-sample fit 19/19, ~6/7, 6/7, 4/4, 9/9. |
| H5 | "21_ = qui" makes l. 9 read "el Marqués de los Vélez [y] Quiroga", i.e. Cardinal Gaspar de Quiroga, Archbishop of Toledo (named by office on f. 199r). | open | Reconciled transcription of l. 9; other occurrences of the name in the volume. | One occurrence. |

## Notes
-
