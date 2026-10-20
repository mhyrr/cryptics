# Historical evidence for solver inputs: report, 2026-10-20

Brief: `../../PROMPT-historical-evidence.md`. One research pass. No solver run, no outreach, no money spent, no
access restriction bypassed. Tiers follow AGENTS.md rule 1. English is given beside foreign quotations.

## Result in one paragraph

No document found gives a key, a key source, encryption instructions, a plaintext passage, or more cipher traffic
for these telegrams. BLUME is still unidentified. **The key shortlist is empty.** Two options survive, neither of
them a key. (1) A **cipher procedure**: two period handbooks use "double transposition" for a one-table system
with a keyed column order and a keyed row order. Our dive has not tested that system on the whole text, and on
complete rectangles it reduces exactly to a problem experiment 18's existing solver handles. (2) **Calibration
text**: fourteen real Spanish telegrams, none commercial. The procedure option is attested as available in Europe,
not as used by the Oswalds.

## Files

| File | What it holds |
|---|---|
| `solver-options.jsonl` | Seven records, stable IDs `HE-*`; validated by `analysis/28-historical-evidence/check.py` |
| `search-log.md` | Coverage by catalogue, main-thread searches, gaps |
| `viktor-oswald-legation-file.md` | Main-thread reading of BAR E2001E#1000/1571#787* (Viktor's expulsion file) |
| `bar-E2001E-1000-1571-787/` | Its IIIF manifest and machine OCR, as downloaded |
| `agent-blume-identity.md` | BLUME identity search (two passes) |
| `agent-oswald-trail.md` | BAR dossier sweep, other Oswald files, Bochsler sample |
| `agent-prior-research.md` | Note 44 and the 2020 report; unsent request drafts |
| `agent-procedure.md` | Period key rules and preparation |
| `calibration-telegrams.md` | Calibration texts only; not evidence about BLUME |

The agent files are working notes by research agents. Where they conflict with this report, this report governs.
One correction applies: `agent-oswald-trail.md` row 10 calls E2001E#1000/1571#787* a probable namesake. It is
Viktor's own file (decree names "OSWALD (Moritz Victor) né le 15 Novembre 1909").

## What was established

**About the people (PRIMARY, BAR).**
- Viktor ran an import–export business "seit Dezember 1936 auf Seite Francos" ("on Franco's side since December
  1936"), per a 1939 letter of recommendation (E2001E#1000/1571#787*, Dokument_0000003; OCR). So a Nationalist-side
  trading business existed a month before the telegrams. Its name and partners are not given.
- France expelled him on 28 October 1937 for "agissements … se rattachant aux évènements actuels d'Espagne"
  ("activities connected with the present events in Spain"). A French consular report, relayed in 1939, said he was
  "in ständigem Verkehr mit deutschen Geheimagenten" ("in constant contact with German secret agents") in San
  Sebastián. No precise accusation was ever made (same file; OCR).
- In April 1937 his postal address was c/o "Banco Guipuzoano [sic], San Sebastian". A Zurich telegram of April
  1937 about him is mentioned, with no text (E4320B#1974/47#277, Dokument_0000071, image 513; agent).
- His only surviving telegram in his own words is plain German telegraphese, Hendaye to Bern, May 1938 (OCR). No
  other cipher traffic by either brother was found.
- Werner's office was searched on 28 April 1937. No seizure inventory was found in the pages read.

**About BLUME.** Nothing ties any person, firm or registered address named Blume to Salamanca and the Oswalds.
One unverified snippet names a "Blume Otto" in a Condor Legion decorations list (Hidalgo Salazar 1975, p. 223).
The main Spanish catalogues (PARES, Prensa Histórica, BNE Hemeroteca) refused access throughout (429/403).

**About the 2020 attempt.** Note 44 was not reached. The book's ebook preview does not include it, and no
report surfaced under new routes. Bochsler doubts the wool explanation (Cryptiana 2023, re-read).

**About procedure (available-only).** Givierge (1925) numbers keyword letters with ties left to right and leaves
the table unpadded. We reproduced his printed MARSEILLE cryptogram by script. He and Hitt (1916) both describe a
row-and-column one-table system under the name "double transposition". Hitt gives a Spanish cipher alphabet
without K or W and terminal X in examples; T1 has 2 K. FRUS reports a Burgos ban on code messages at Vigo
(September 1936).

## Ranked shortlist

| Rank | ID | Type | Status | Consequence |
|---|---|---|---|---|
| 1 | HE-P01 | cipher procedure | available-only; untested family | One-table row-and-column transposition. On complete rectangles (T1: 15 × 41, 41 × 15; T2: 8 × 20, 10 × 16, 16 × 10, 20 × 8), a fixed rearrangement turns it into experiment 18's sets-of-n problem, checked on 200/200 random keys in both writing directions (`analysis/28`). Experiment 20 covered only n × n squares and lists the whole-text rectangle as not covered |
| 2 | HE-C01 | calibration | thin, non-commercial | Tests whether real 1937 telegraphese clears the −5.10 threshold that every negative result relies on |
| — | HE-P02 | procedure | no change | Left-to-right ties already in 24–27; right ties are undocumented and could be dropped |
| — | HE-P03 | preparation | weak | No-K/W alphabet, terminal X, code ban: no target consequence now |
| — | HE-K01 | key material | contextual guess | New names (MORITZ VICTOR OSWALD, BANCO GUIPUZCOANO, MIRACONCHA). Not keys; not recommended |
| — | HE-T01 | traffic | no cipher text | No additional ciphertext exists in reach |
| — | HE-B01 | identity | unverified snippet | Otto Blume; no link |

**Documented keys: none. Contextual guesses: HE-K01 only, labelled as such. Possible plaintext: none.** Werner's
wool account remains testimony; Viktor's December 1936 business makes a trading subject plausible but supplies no
words.

## Single best next computational test

**HE-P01 on complete rectangles**, under a separately frozen plan:
1. Apply the two fixed rearrangements (chunks of h read across; every w-th letter) to T1 at w ∈ {15, 41} and to T2
   at w ∈ {8, 10, 16, 20}.
2. Run experiment 18's solver unchanged, with fresh seeded-apart plants made in the row-and-column system itself
   (not in 18's family), at least 10 per band, pass rule ≥ 8/10, thresholds fixed before the target.
3. Add one own-letter shuffle per cell.

It is cheap because the solver exists and the reduction is exact. A negative excludes only those widths under 18's
model and budget. It says nothing about incomplete rectangles, which need a long-column search and their own
design. Nothing makes this family more likely than double columnar. It is the one sourced system the dive has
not tested. Folding HE-C01's two long texts (P1, M1) into the plants would also test real telegraphese at the same
cost.

## The barrier that would most improve our position

**BLUME's identity at the receiving end.** A key or plaintext would sit with the recipient or the Salamanca
telegraph office, not in Swiss police files. The gate is the Salamanca list of registered telegraphic addresses for
1936–37: the "Telegramas:" entries of the Anuario Bailly-Baillière / Anuario General de España, or the Cuerpo de
Telégrafos register. These are in print at the BNE. Online, Prensa Histórica and the BNE Hemeroteca refused us.

Nearer and orderable, both Greg's call because ordering is an external action: BAR **E2200.38-04#1000/483#415***
(Swiss Legation Madrid, "Oswald, Viktor", open access, not digitised), for the Madrid firm and its partners. And
BAR **E2001D#1000/1551#5627*** ("Oswald, Madrid", 1936–38, access review). Bochsler's note 44 needs a print copy
or the unsent publisher request (`../outreach-bochsler.md`; the extra questions are in `agent-prior-research.md` §5).

## Uncertain claims

- All E2001E#1000/1571#787* quotations are machine OCR; no image was viewed.
- The Givierge and Hitt passages were read by the procedure agent from translation/Gutenberg text. Only the
  MARSEILLE example was re-verified here, by script.
- The FRUS code ban is a fetch-tool paraphrase of a report about one port, not the order.
- "Blume Otto" is a snippet whose adjacency to "Salamanca" is unverified.
- That E2200.38-04's "Oswald, Viktor" is our Viktor is likely but not documented.
- Every access failure is a failure to look, not a negative.
