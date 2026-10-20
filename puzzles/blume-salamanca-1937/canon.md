# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` / `disputed`), and a source pointer.

## Scope of the negative results (audit, 2026-10-18)
- "Excluded" below means a negative result under the stated model, plant distribution, recovery rule and
  search budget, unless the test was exhaustive or a direct alphabet constraint. It does not prove that every
  key or historical variant is impossible. The latest long-key controls recover 20/20 full-length plants and
  29/30 trimmed plants; they do not establish uniform recovery for every text and width. **established**
  (`analysis/23-method-audit`, recomputed from checked-in 21/22 logs)
- Experiment 12 favors transposition over its simulated alternatives. It does not test all possible
  nomenclators, codebooks, restricted substitution keys, or substitution combined with transposition. Its
  diagonal-Gaussian score gaps are not calibrated probabilities of historical systems. **established** about
  the experiment's scope (`analysis/12-type-diagnostics/diagnose.py`; audit `23`). Transposition remains the
  **likely** family; the earlier blanket non-transposition exclusion is narrowed here.
- Experiment 11 finds no significant difference in letter distributions (p = 0.21); it does not establish
  that the two telegrams use the same system or key. **established** about the test's scope (audit `23`).
- The solver controls use modified held-out literary text, including PUNTO and spelled quantities, rather than
  independent period business telegrams. Sensitivity to the actual message's preparation remains unmeasured.
  **established** (`analysis/01-solver/plaintext.py`; audit `23`).
- Experiments 21/22's four target-body sweeps cost 26.278 process CPU hours in total, with no candidate. This
  is the cost of those runs only, not the full dive. **established** (`analysis/23-method-audit/result.txt`).
- A phrase-seeded solver recovers exact plaintext in 10/10 exact-list-key and 9/10 one-rank-swap held-out plants
  (615 letters; first width 12–22, second length 18–28; 5,284 contextual numeric second-key guesses). Two swaps
  recovers 6/10 and fails the pre-registered 8/10 gate. All five failures discard the base seed at the true
  first width before refinement. This is conditional recovery on literary-proxy plants, not evidence that the
  historical key is a phrase on this list. **established** (`analysis/24-phrase-seeded/results/holdout24.jsonl`,
  `results/failure-diagnostics.json`; scripts `run.py`, `summarize.py`, `diagnose_failures.py`).
- The frozen phrase-seeded run on full 615-letter T1 gives no candidate: best -5.8023 against -5.10, 37.563
  process CPU seconds. One own-letter shuffle gives -5.9946, also no candidate. These are finite-list negative
  results, not exclusions of double columnar, off-list keys, two-swap keys or other preparation. **established**
  (`analysis/24-phrase-seeded/results/target24.jsonl`; `summarize.py` → `results/summary.md`).
- On the five old failed controls from 24, explicitly supplying both the true first width and base phrase to
  the original refinement recovers 0/5; the bases rank 394–4,876 at the true widths. These are assisted
  development diagnostics, not blind results. Shortlist loss was a symptom and does not establish that wider
  retention would fix these cases. **established** (`analysis/25-seed-retention/diagnose.py` →
  `results/development.json`; diagnostic source/hash archived there).
- Directly enumerating the original keys and all one-swap neighbours (1,286,188 unique keys) recovers exact
  plaintext in 10/10 exact-list, 10/10 one-swap and 9/10 two-swap fresh plants; conditioned random keys recover
  0/10. Distances are minimum distances from the original list. The true first width is supplied per control,
  so this is per-width recovery, not full unknown-width recovery. Fresh controls cost 3,242.504 process CPU
  seconds. **established** (`analysis/25-seed-retention/results/holdout25.jsonl`; `summarize.py` →
  `results/summary.md`; independent `verify_results.py` → `results/verification.txt`).
- Experiment 25 fails its acceptance gate: one missed two-swap plant scores -4.5505 above the -5.10 threshold,
  with only 0.4683 shift-tolerant plaintext agreement. It recovers the exact second key but a wrong first key.
  First-key refinement and the score -only stop remain unreliable on these controls. No new target run was
  made; no threshold or budget was changed after the failure. **established** (`analysis/25-seed-retention/diagnose_gate.py` → `results/gate-diagnostic.json`; complete gate checked in `results/verification.txt`).

- With K2 supplied and locked, experiment 26's full-neighbourhood K1 stage recovers 30/30 fresh positive
  controls (ten each at first widths 12–15,16–18,19–22); twenty-nine are exact and one is a complete cyclic
  shift allowed by the declared rule. Ten wrong-width and ten own-letter-shuffle negatives give zero
  candidates. The fifty-case isolated gate passes independent reconstruction/decryption/rescoring at
  14.0 recorded process CPU seconds. This is supplied-K2 calibration, not blind double-columnar recovery.
  **established** (`analysis/26-k1-recovery/results/iso26.jsonl`; `verify_results.py` → `results/verification.txt`).

- Earlier validated double-columnar target regions at second lengths 12–17 have first width <=15; they do
  not cover first widths >=16 with those second lengths. Contextual phrase experiments 24–26 activate only
  second lengths 18–28 and first widths 12–22 for their target protocols. Wider phrase metadata and other
  first widths are not thereby covered. **established about recorded scope** (`analysis/26-k1-recovery/scope-audit.md`;
  `analysis/03-target-h1/README.md:19`, `analysis/21-dc-method/README.md:12`, `analysis/24-phrase-seeded/README.md:52`).

- Experiment 26's forty fresh end-to-end controls give exact-list10/10, one-swap 10/10, two-swap9/10 and
  conditioned-random 0/10 recoveries; every recovery is exact. All four retained seeds are processed. The
  missed two-swap case (-5.8084) and every random-key case stay below threshold, giving zero false
  candidates and a passing gate. First width is supplied; this is conditional calibration on literary-proxy
  plaintext. Recorded CPU cost 2,916.034 seconds excludes isolated/development work. **established**
  (`analysis/26-k1-recovery/results/holdout26.jsonl`; independent `verify_results.py` → `results/verification.txt`).

- Experiment 26's complete target grid yields zero candidates for both full 615-letter T1 (best -5.9141,
  792.058 recorded CPU seconds) and one own-letter shuffle (best -5.9484,764.828 CPU seconds), against -5.10.
  All eleven first widths 12–22 run per body, second lengths 18–28, all four retained seeds per width.
  Independent verification checks all 22 cells/all 88 refinements and protocol pins. This finite-band,
  model/budget-dependent negative does not exclude every contextual phrase or double-columnar key.
  **established** (`analysis/26-k1-recovery/results/target26.jsonl`; `verify_results.py` → `results/verification.txt`).

- Experiment 27 freezes the existing phrase metadata at second lengths 12–17: 1,480 original numeric keys,
  expanded to 160,327 unique original/one-swap keys. Its unchanged26 optimizer passes forty fresh controls
  with first widths 16–22 supplied: exact 9/10, one 10/10, two 9/10, random (minimum original distance >3) 0/10.
  All 28 recoveries are exact, with zero false candidates. All forty cases/all 160 refinements and candidate
  bytes are independently verified. Cost 511.967 recorded process CPU seconds. This remains literary-proxy,
  conditional per-width calibration; arbitrary keys are not covered. **established**
  (`analysis/27-short-k2/expanded-manifest.json`; `results/holdout27.jsonl`;
  independent `verify_results.py` → `results/pre-target-verification.txt`).

- Experiment 27 completes all fourteen target cells: first widths 16–22, second lengths 12–17, full
  615-letter T1 and one own-letter shuffle, four refinements per cell. T1 best -5.9662 (86.510 CPU seconds),
  shuffle best -5.9317 (90.994 CPU seconds), zero candidates against -5.10. The finite phrase-neighbourhood
  search is negative. With forty controls, recorded solver work is 689.471 CPU seconds (11.491 minutes).
  This does not exclude arbitrary keys in the short-K2/long-K1 band. **established**
  (`analysis/27-short-k2/results/target27.jsonl`; `summarize.py` → `results/summary.md`;
  independent `verify_results.py` → `results/verification.txt`).

## The object
- Two cipher telegrams, Zurich to "BLUME SALAMANCA", 8 January 1937, are in the Swiss Federal Archives,
  E4320B#1974/47#277 (*Spanische Revolution (Passvisas etc.)*), subdossier 0000066, Unterlagen_0000072, canvases 9
  (telegram 1) and 13 (telegram 2). These are PTT copies sent to the Federal Police on 15 Jan 1937. **established**
  (PRIMARY: IIIF scans, `sources/images/`, `sources/headers.md`)
- Telegram 1: printed form, serial 1381, Zurich office 797, handed in 11:31, sent on to London at 11:42, fee 49.90,
  125 words (= 123 groups + 2 address words), routed "Angleterre Eastern". A typed "(VIA VIGOEMDENKABEL)" is struck
  through. Margin note "als Chiffriert aufgegeben" ("handed in as cipher"). Red note: "Aufgabe: Oswald Viktor,
  geb. 15.11.1909, in Burgos" ("handed in by Viktor Oswald, born 15 Nov 1909, in Burgos"). **established** (PRIMARY,
  `sources/headers.md`)
- Telegram 2: plain sheet, serial 1486, Zurich office 910, "Cde" stamp, handed in 17:34, sent on 17:40, fee 14.00.
  The reverse has 47 × 34 = 15.98, and 34 = 32 groups + 2. **established** (PRIMARY, `sources/headers.md`)
- The charges do not separate the two telegrams' systems. T1 pays 0.399 per word and T2 0.412 (stamped), within 3%.
  Under the 1932 Madrid Regulations (Art. 10) a code word may be any group of five letters or fewer, so five-letter
  cipher groups qualify as code language (CDE). **likely** (PRIMARY regulations; arithmetic in
  `analysis/11-one-or-two`; `sources/conventions-survey.md`)
- The sender block names "Dr. ing. W. E. Oswald, Bureau Bahnhofstr 12, Zürich". **established** (PRIMARY)
- The dossier holds no key, no plaintext and no third ciphertext. **likely**: the telegram unit was viewed in full,
  and the other 219 files were checked by the archive's OCR only (agent A, 2026-10-16). Bourdeau read all 42 images
  and agrees (CLAIMANT, NOTES.md, 11 Oct 2026).

## The text
- Telegram 1 has 123 five-letter groups, 615 letters; SHA-256 of the letters e266615d…434c55. Telegram 2 has
  32 groups, 160 letters; SHA-256 8fd5cfb8…e17a644. Our blind reading from the archive scans agrees letter for letter
  with Bourdeau's and Bean's. **established** (`sources/PROVENANCE.md`)
- The three formerly disputed groups are SOLRS (38), ACCEL (48) and FTULX (122). On this typewriter the L has a top
  serif on the left and a long foot; the I has serifs at both ends. **established** (issue 14; our reading)
- Group 113 RBEEP is counted and legible. The red stroke is the underline of the red note, not a deletion.
  **established** (PRIMARY)

## Dating, provenance, authorship
- Werner Oswald told the police (28 Apr 1937) that his brother Viktor sent the telegrams while passing through Zurich.
  He said they concerned reopening an office in Nationalist Spain and a wool deal to unfreeze Swiss export credits,
  kept from Hisma (Seville) until it had been put to the authorities in Burgos. He said he did not know the content
  or the key. **established** that he said so (PRIMARY via Bourdeau's and agent B's reading of the interrogation);
  the content of the claim is unverified.
- Viktor Oswald (BAR records give "Moritz Victor", "Victor M.", born 15 Nov 1909) ran an import–export business
  "seit Dezember 1936 auf Seite Francos" ("on Franco's side since December 1936"), per a letter of 18 Jan 1939 to
  Federal Councillor Motta. The firm's name and partners are not given. **established** that the letter says so
  (PRIMARY, machine OCR: BAR E2001E#1000/1571#787*, Dokument_0000003; `sources/historical-evidence/viktor-oswald-legation-file.md`)
- France expelled him on 28 Oct 1937 for activities "se rattachant aux évènements actuels d'Espagne" ("connected with the
  present events in Spain"); a French consular report relayed in 1939 said he was in constant contact with German agents
  in San Sebastián, with no precise accusation made. **established** that the records say so (PRIMARY, OCR, same file)
- In April 1937 his address was c/o "Banco Guipuzoano" [sic], San Sebastián, and a separate Zurich telegram about him is
  mentioned, text absent. No other cipher traffic by either brother was found in BAR. **likely**, as an absence in the
  records searched (PRIMARY, BAR E4320B#1974/47#277, Dokument_0000071 image 513; `sources/historical-evidence/search-log.md`)
- Givierge (1925) numbers keyword letters with ties left to right and leaves the columnar table unpadded; his printed
  MARSEILLE cryptogram reproduces under that rule. **established** (SCHOLARLY; `analysis/28-historical-evidence`). This is
  period availability, not evidence of the Oswalds' practice.
- Who or what "Blume" is: unknown. **established** (agent B, `sources/context-cribs.md`; still unknown after the 2026-10-20 pass, `sources/historical-evidence/`)

## Structure and statistics (from `analysis/`, never from impression)
- Letter counts against telegraph-style references (corrected 2026-10-17, after a glossary in one held-out book was
  found to fatten the null): no candidate language fits T1 well (Spanish p = 0.014, Portuguese 0.022, Italian
  0.004). T2: Spanish 0.024, Italian 0.074, Portuguese 0.108. The misfits: X in T1 (6 vs 1 expected, z +5.0), P in
  T1 (35 vs 23, and vs 16 when the stop word has no P, z +4.8), U low in T1; F in T2 (7 vs 1, z +4.7).
  **established** (`analysis/08-letter-fit`, `analysis/10-convention-fit`)
- The telegrams most likely contain a natural-letter text in a new order: plain transposition, transposition
  with nulls, transposition of mixed text, or a jargon code then transposed. Statistics cannot distinguish these
  reliably at these lengths. Experiment 12 disfavors its simulated substitution, fractionation, homophonic,
  nomenclator and artificial-codebook generators (40–1,137 classifier log-score units below its best type),
  rather than excluding every historical variant or combination. **likely** family; **established** measured
  comparison (`analysis/12-type-diagnostics`; scope corrected by `analysis/23-method-audit`)
- T1 is slightly flatter than transposed Spanish telegraph text: IC 0.0695 at the 5th percentile and MIC at the 2nd
  of plain-transposition plants, inside the bands of transposition with nulls or mixed text. **established**
  (`analysis/12-type-diagnostics`, `analysis/10-convention-fit`)
- T1 and T2 fit one letter source (homogeneity p = 0.21) and both rank Spanish first. The F difference is borderline
  (7 vs 2.5 expected in T2; adjusted for 26 letters p = 0.056). Neither telegram shows structure by position inside
  the five-letter group (p ≥ 0.32). **established** (`analysis/11-one-or-two`)
- X in T1 and F in T2 sit where any other letter of the body could sit: residues and gaps at chance (p = 0.73 and
  0.28). Position cannot tell X-as-stop from X-as-null-before-transposition. X as a stop at every sentence end would
  give about 12.5 X in 615 letters, twice the count. **established** (`analysis/09-odd-positions`,
  `analysis/10-convention-fit`)
- T1's last 20 letters (`AXLNKIPLANFTULXREFLX`) hold 3 of 6 X, 1 of 2 K and 2 of 5 F. A scan over every window
  finds this end at every window length; corrected for window position and length, p = 0.019, and 1.8–3.1% of
  transposition plants reach it. T2 shows nothing comparable (p = 0.38). **established** as measured; what it
  means is open (H6). (`analysis/09-odd-positions`)
- Index of coincidence: T1 0.0695, T2 0.0710, natural-language level. **established** (computed 2026-10-16;
  agrees with Bourdeau)
- Letter counts. T1: E73 O69 A58 N53 I43 R40 S39 T36 P35 C30 M24 D24 L20 U16 B12 G9 H8 X6 F5 Z4 V3 Q2 Y2 J2 K2,
  W0. T2: no K, W, X, Q or Y. The catalog entry's "no k, w or x" holds for T2 only. **established** (computed)
- T1 and T2 share 9 distinct 4-grams where shuffles give 2.2 (p = 0.001), and the 6-gram APMOEP (p = 0.011).
  Repeats within T1 are at chance. **established** (`analysis/02-shared-repeats`). After correcting for the choice
  of n and statistic, the excess is suggestive, not established: family-wise p = 0.008 against letter shuffles,
  0.020 against transposed Spanish plants, 0.052 against bigram-preserving shuffles. Reversed matches show no
  excess. Both final groups begin REF (`REFLX`, `REFUD`), seen after looking. **established** as measured
  (`analysis/13-shared-strings`)
- Forward double columnar (CC) is excluded for telegram 1 with w1 ≤ 15 and w2 12–15, and the CR convention with
  w1 2–15 and w2 12–15, for Spanish, Italian or Portuguese plaintext. If both telegrams share keys, CC is also excluded
  for w1 8–15 and w2 16–17. **established** (`analysis/03-target-h1`; controls in `analysis/01-solver/controls/`)
- Every columnar exclusion holds only for the full 615 (or 160) letters. With 5–20 untransposed letters at either
  end, our double columnar solver recovers 0/10 plants (10/10 without), and a single columnar solver 0/40 (39/40
  without). The same mechanism, wrong column lengths, applies to Bourdeau's full-length searches. **established**
  for our solvers, **likely** for Bourdeau's (`analysis/15-tail-robustness`)
- On bodies with the end cut off the cheap families still do not read. T1 with 1–5, 10, 15 or 20 letters cut:
  single columnar w 5–30 (and w 31–45 for 10–20 cut) best −5.50 against thresholds near −4.9; double columnar CC
  w1 2–15 × w2 2–15 best −5.94 against −5.10. T2 with its last group cut: single columnar w 5–30 best −4.79 against
  −4.41. T2 after a 1–15-letter preamble is not a 4 × 4 grille (best −5.86). Controls pass at each length and band
  reported. **established** (`analysis/17-truncated-bodies`)
- Head trims and two-sided trims change nothing (tier 2 of `17`). T1[a : 615 − b] for every a, b in {0, 5, 10, 15,
  20}: single columnar w 5–30 (w 31–45 at four lengths) and double columnar CC w1 2–15 × w2 2–15 give no candidate
  (best −5.92 against −5.10). T2[a : 160 − b], 23 bodies: single columnar w 5–8, and w 9–30 at four lengths, below
  every recovered control's true text. Joint CC w1 8–15 × w2 16–17 on T1 + T2[0:155]: best −6.08. **established**
  (`analysis/17-truncated-bodies`, tier 2)
- At 615 letters the IDP score of a second key has a usable gradient only within about 3–4 swaps of the true key.
  Lasry-style search therefore fails beyond w2 ≈ 15 (alone) or 17 (jointly). **established** for this solver
  (`analysis/01-solver`, probe and band controls)
- No period source ties any transposition to the Oswalds, to Swiss commerce, or to Spain in 1936–37. The Swiss
  army's hand cipher of the time (Réglette, about 1918–39) is a Vigenère-type substitution. **likely**, as an absence
  of evidence (`sources/key-type-survey.md`)
- The 2020 attempt by Heinzmann, Matteotti, Liniger and Viveksanth is recorded only in Bochsler's note 44 (print);
  nothing of it is online. **likely** (`sources/key-type-survey.md`; Bourdeau NOTES.md)
- Neither telegram has bigram structure of its own, forward or reversed (T1 p = 0.53, T2 p = 0.61 against own
  shuffles). So word transposition, row and serpentine routes (width 5–30) and block moves (sets 3–12) are
  excluded, and the shared strings are not surviving plaintext runs. **established** (`analysis/04-run-keeping`,
  plants 20/20)
- No reversed-direction transposition fits (lag scan). **likely** (CLAIMANT: Bourdeau; not rerun here)
- Letters permuted within sets of n, and the Nihilist rectangle read by rows (any row order, so n × n squares
  under one key included), are excluded for T1 at n 8–50 and for T2 at n 8–15, with any untransposed preamble or
  tail, and with one key on both telegrams at n ≤ 50. A solver built on the families' structure (cipher position
  mod n gives the plaintext column, so the key is a path through column-pair bigram scores; every offset scanned)
  recovered 117/120 T1 plants and 35/40 T2 plants in the passing bands, seeded apart from the plants. The target is
  below every band threshold by 0.36–1.08 log units per quadgram. **established** (`analysis/18-periodic-solver`)
- The Nihilist transposition read by columns in n × n squares (rows in any order) is excluded for T1 at n 5–24 and
  T2 at n 5–11, with a preamble of 0–20 letters and any tail. Each square, rearranged, is the rows problem `18`
  solves; controls 65/70 across seven bands; target below every threshold by 0.57–1.09. **established**
  (`analysis/20-nihilist-columns`)
- Not covered by `18`: T2 at n 16–30 (at 160 letters a wrong key outscores the right one, so no budget would pass a
  control), n > 50, and Nihilist squares whose partial last row the row key moves into the middle. **established**
  (`analysis/18-periodic-solver`)
- `05`'s controls (78/78 sets, 72/72 Nihilist) were invalid: the solver reused the plant's seed, so its first restart
  was the planted key. With independent seeds that hill climb recovers sets of 20 in 1/20 plants and Nihilist rows
  at n = 8 in 14/20; every failure scores below its own true text. **established** (`analysis/15-tail-robustness`,
  `check05-seed.txt`). Separately, sets of 5–12 at any alignment leave vowel/consonant contact structure that T1
  lacks (`14`).
- T2 is not a 4 × 4 turning grille in either use (all 1,024 keys), alone or with one key on T1. **established**
  (`analysis/06-grille`, controls 10/10). This holds with untransposed letters at the end (20/20 recovered), not
  with a preamble (0/20). (`analysis/15-tail-robustness`)
- A phrase shared by both telegrams under one key produces the observed excess of shared 4-grams only under
  single columnar and Nihilist read by rows. Under double columnar (8–25) and Nihilist read by columns it stays at
  chance. **established** (`analysis/07-shared-model`). Single columnar does not explain them even with
  untransposed ends: the seven shared runs fit no common column geometry (best 2 runs, where chance gives 2,
  p 0.37 and 0.23; planted geometries recovered in 99.6%, w 5–30), and a shared phrase under one single columnar
  key gives more runs than observed (median 8–33 by width). **established** (`analysis/16-run-geometry`). Nihilist by
  rows does not explain them either: under `07`'s model it gives 22–74 shared 4-grams against 9 observed, and T1 is
  excluded under it for n 8–50 (`18`). So no tested family with a shared phrase under one key produces the shared
  strings. **established** (`analysis/07-shared-model`, `analysis/18-periodic-solver`)
- Neither telegram carries Spanish letter-pair association at any single lag beyond its own shuffles (T1 lags
  1–100, max z 2.53 at lag 50, family-wise p 0.40; T2 lags 1–50, p 0.54), and the multi-lag sums lie inside 200
  long-key double columnar plants. **established** (`analysis/19-lag-profile`)
- Under `18`'s offset scan T1 beats its own shuffles (20/20 at n 20 and 30). Most of that comes from offsets that
  leave T1's rare-letter end unscored; at fixed offsets that keep the end, T1 lies inside its shuffles (90th
  percentile). It is not evidence about the cipher family. **established** (`analysis/18-periodic-solver`, checks 1–4)
- Neither telegram has vowel/consonant contact structure or uneven vowel density beyond what long-key double
  columnar plants give (T1 p 0.56, 0.87; T2 0.84, 0.17; power 0.78–0.98 at 615). The two telegrams' bigram profiles
  overlap beyond their letter counts (+70; p ≈ 0.003 under those plants), a statistic found after looking.
  **established** as measured (`analysis/14-contact`)

## Prior scholarship: settled points
- Tomokiyo (2023) excluded the British Government Telegraph Code. **likely** (SECONDARY, Cryptiana)
- Bourdeau's exclusions, all with planted controls: every single transposition (single columnar to width 45),
  all reversed-direction systems, forward double columnar with w2 ≤ 11 (w1 ≤ 41), both mixed conventions with
  w2 ≤ 10, and K2 a dictionary word or 1–5-word phrase. **likely** (CLAIMANT; table in `README.md`)
- No source documents any transposition system in use by any party in Spain in 1936–37. Documented Spanish Civil
  War systems are substitution-based (Enigma from Nov 1936, strip ciphers, LUCI). German army double transposition
  is documented for WWI and from 1940. **likely**, as an absence of evidence (agent B, `sources/context-cribs.md`)
- The German army separated sentences with X by 1930 (its Enigma test message). No Swiss or Spanish source for X as
  a stop was found; French and Spanish telegrams of the period used STOP. Givierge (1925) leaves an incomplete
  columnar table as it is, with no filler, and puts indicators at the head of a message. No final reference group
  or "REF" convention was found. **likely** (SCHOLARLY: Weierud; Givierge; `sources/conventions-survey.md`)
- Bourdeau's statement that German Doppelwürfel users were told to take key phrases of 15–25 letters has no source.
  **likely** (agent B; Bean, issue 37)
- Lasry's IDP method solved Schmeh's 599-letter challenge (keys 21 and 23; 599 = 26 × 23 + 1), from a partial
  solution (a spotted word, then a known-plaintext search), not from a converged hill climb. Lasry reports over 60%
  success at keys 19 × 20 and 90% at 18–19 on simulations, without stating text length, language, trial count or
  budget. **established** that he reports it (SCHOLARLY: Lasry thesis 2018, ch. 9,
  https://kobra.uni-kassel.de/handle/123456789/15274; re-read in `analysis/21-dc-method`). Our earlier notes'
  "599 letters, English" for those simulations was an inference, not his statement.
- Our IDP reproduces Lasry's fitness-distance curve at his challenge geometry (D at 1–4 swaps, as a share of the
  random-key level: 0.43, 0.73, 0.86, 0.93 against his fig. 9.2's 0.46, 0.70, 0.84, 0.90). In his presumed setting
  (English, 599 letters) it finds no K2 at 18 × 19 or 19 × 20 (0 of 6 runs of 8 M evaluations). A climb returns to
  the true K2 only from within 2–4 swaps, and the share of keys inside that basin falls about tenfold per unit of
  w2. Rectangle completeness, language, 599 vs 615 letters, the closing link and the move set each widen the basin
  by at most one swap. **established** for this implementation (`analysis/21-dc-method`)
- With Lasry's full-neighbourhood K2 climb and a budget of 50 M IDP evaluations per length pair, forward double
  columnar is recovered at 615 letters for w1 2–15 × w2 16–17: 20/20 planted trials (two pre-registered controls,
  the corner w1 12–15 × w2 17 included). On T1 at full length that method gives no candidate in w1 2–15 × w2 16–17
  (best −6.00 against −5.10), so forward CC on T1 at full length is excluded for w1 ≤ 15 and w2 ≤ 17 (with `03`
  and Bourdeau). **established** (`analysis/21-dc-method`). The same holds on T1[0:595], T1[5:615] and T1[10:615]
  (controls 10/10, 10/10, 9/10; target bests −5.94, −6.00, −6.01). The margin is thinnest at 15 × 17 on the trimmed
  bodies, where plants recovered at 28 M and 48 M of the 50 M budget and one failed. **established**
  (`analysis/22-dc-trimmed`)
