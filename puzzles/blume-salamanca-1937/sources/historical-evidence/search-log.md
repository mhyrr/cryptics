# Search log: historical-evidence pass, 2026-10-20

One documented research pass. Four read-only research agents (Sonnet) ran in parallel, and the main thread read the
results and one further archive file. Row-level logs live in each agent's notes file. This file gives coverage,
what was inspected, and what failed. A failed search is not evidence that a document or person does not exist.
An OCR negative is not an image-verified negative.

| Thread | Notes file | Searches / fetches | Row-level log |
|---|---|---|---|
| BLUME identity | `agent-blume-identity.md` | 31 logged (two passes) | §3 |
| Oswald paper trail | `agent-oswald-trail.md` | ~60 incl. image reads | §4 |
| 2020 report, note 44 | `agent-prior-research.md` | ~50 tool calls, new queries only | §4 |
| Procedure and calibration | `agent-procedure.md`, `calibration-telegrams.md` | 40 logged | "Search and fetch log" |
| Main thread | this file, `viktor-oswald-legation-file.md` | below | below |

## Coverage by catalogue

| Catalogue / route | Range | Covered how | Result |
|---|---|---|---|
| BAR dossier E4320B#1974/47#277, all 219 OCR files | 1936–38 | OCR text, broad term list (Oswald/Osswald, Viktor/Victor, Patvag, Hovag, Wolle, Lana, Burgos, Hisma/Hsma, Code, Schlüssel, chiffr, Telegramm, Depesche, Salamanca, Blume, Madrid, Kompensation, Clearing, Verrechnung) | Oswald only in subdossier 66, units 68–71 |
| BAR subdossier 66, images | 1937 | Images 491–494, 499, 507, 509, 511–513, 517 viewed by agent; unit 72 viewed in full in session 1 | No key, plaintext, codebook, BLUME. New: Hunziker letter (19 Apr 1937) addressed c/o Banco Guipuzcoano; a separate April 1937 telegram from Zurich referred to, text absent |
| BAR online catalogue, "Oswald Victor", "Oswald, Madrid", "Patvag" | all | Catalogue entries | E2001E#1000/1571#787* digitised (read, below); E2001D#1000/1551#5627* "Oswald, Madrid" 1936–38, not digitised, access review needed; E2200.38-04#1000/483#415* Legation Madrid "Oswald, Viktor", open, not digitised; E2001D#1000/1551#7346* destroyed; Patvag page 1 of 6 only (all post-1941) |
| BAR E2001E#1000/1571#787* | 1937–48 | Full OCR, four units, main thread; no images | Viktor's expulsion file. No cipher material. Dates his Nationalist-side import–export business to Dec 1936 |
| dodis.ch | 1937 | — | Access failure (bot wall, not bypassed). dodis.ch/46295 known from a search summary only |
| PARES | — | WebFetch, Playwright, urllib (main thread, twice) | Access failure: HTTP 429 every time |
| Prensa Histórica (Salamanca papers 1936–37) | 1936–37 | WebFetch, Playwright | Access failure: HTTP 429 |
| BNE Hemeroteca Digital | 1936–37 | WebFetch, Playwright | Access failure: 403 / Cloudflare challenge, not bypassed |
| HathiTrust full text | any | Playwright | Access failure: Cloudflare, not bypassed |
| BOE Gazeta text search "Blume" | 1661–1959 | Page-checked results list | 9 hits, none 1936–39 (index/OCR only) |
| ABC Sevilla | 1937 | Date browse | Search behind consent/paywall step; not crossed |
| DGFP Series D vol. III (Germany and the Spanish Civil War) | 1936–39 | Full archive.org OCR text | No Blume (OCR only) |
| Google Books / web | any | ~20 queries | One weak snippet: Hidalgo Salazar 1975, p. 223, "Blume Otto" (Condor Legion decorations) |
| Anuario Bailly-Baillière / Anuario General de España, Salamanca "Telegramas:" lists | 1935–37 | archive.org metadata only | Not found online; not read |
| Bochsler, *Nylon und Napalm* | 2022 | Google Books preview search (80 pp.), e-bookshelf front matter (30 pp.), publisher sample | Note 44 not reached. Telegram chapter probably "Bilder für Hitler, Bomben für Franco" (inference from contents) |
| Schmeh blog; Bourdeau issues; Fuentes repo | 2023–26 | Site searches | No 2020 report; Fuentes lists BAR 1689905 only |
| Heinzmann, Matteotti, Liniger, Viveksanth | any | New name/affiliation queries | Nothing; no namesakes attached |
| Givierge 1925, Hitt 1916, Langie 1922, Lasry 2018 | — | Full text | Procedure findings (available-only) |
| Sacco 1936, Lange & Soudart 1925 | — | — | Not reachable (lending-restricted / catalogue only) |
| FRUS 1936 vol. II doc. 719 | Sep 1936 | Fetch summary | Burgos code ban reported for Vigo |
| Calibration telegrams | 1937 | Olivar 2008; Quirantes site (Historia y Vida 1994) | 14 texts, 5,929 letters, three sources, none commercial |

## Main-thread rows

| # | Query / action | Site | Range | Result |
|---|---|---|---|---|
| M1 | PARES catalogue search `texto=Blume`, `texto=Oswald` | pares.mcu.es (urllib) | — | HTTP 429 both; logged as access failure, no retry loop |
| M2 | Simple search "Oswald Victor" | BAR online access (Playwright) | all | 5 hits: E5330-01#1000/894#15325* (1932 theft case, "Oswald Victor 1912"), E2001E#1000/1571#787* (digitised), E2001D#1000/1551#7346* (destroyed, cross-refers B.31.51.F.), two unrelated |
| M3 | Manifest and OCR zip of E2001E#1000/1571#787* | BAR (urllib) | 1937–48 | Downloaded; copied to `bar-E2001E-1000-1571-787/`; full OCR read; terms Blume, Salamanca, chiffr, Schlüssel, Code, Wolle/lana, Patvag negative (OCR) |

## Gaps left open

1. Salamanca telegraphic-address lists (Anuario Bailly-Baillière / Anuario General de España 1935–37; Spanish
   telegraph registers of registered addresses). Print or BNE reading room.
2. La Gaceta Regional and El Adelanto, Salamanca, 1936–37, image-level. Prensa Histórica blocked.
3. PARES / Centro Documental de la Memoria Histórica (Salamanca) / AGA catalogue queries for Blume, Oswald, Patvag.
4. BAR E2200.38-04#1000/483#415* (Legation Madrid, "Oswald, Viktor"): open access, not digitised; needs an order.
5. BAR E2001D#1000/1551#5627* ("Oswald, Madrid", 1936–38): access review required.
6. Bochsler, note 44 and the chapter "Bilder für Hitler, Bomben für Franco": print copy.
7. Hidalgo Salazar 1975, p. 223: library copy, to check whether "Blume Otto" is tied to Salamanca.
8. Sacco 1936; Lange & Soudart 1925 (for period key rules): library copies.
