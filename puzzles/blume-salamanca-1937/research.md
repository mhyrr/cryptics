# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry that killed it. Nothing here is deleted.

- 2026-10-17 (session 6): letters permuted within sets of n and the Nihilist rectangle read by rows, T1 n 8–50
  and T2 n 8–15, any preamble or tail (`18-periodic-solver`). H5 for every tested family.
- 2026-10-18 (session 6): forward double columnar CC, w1 2–15 × w2 16–17, on T1[0:595], T1[5:615] and T1[10:615]
  (`22-dc-trimmed`).
- 2026-10-17 (session 6): forward double columnar CC on T1 at full length, w1 2–15 × w2 16–17 (`21-dc-method`).
- 2026-10-17 (session 6): T1 with 5–20 letters cut at the head, or at both ends: single columnar, double columnar
  CC w ≤ 15; T2 with head, tail or two-sided cuts: single columnar where controls pass; joint CC w2 16–17 at full
  length (`17-truncated-bodies`, tier 2).
- 2026-10-17 (session 6): the Nihilist transposition read by columns in n × n squares, T1 n 5–24, T2 n 5–11,
  preamble 0–20 (`20-nihilist-columns`).
- 2026-10-17 (session 6): the "T1 beats its shuffles under `18`'s solver" lead against K1, withdrawn by its own
  fourth check (`18`, post hoc checks 1–4; `19-lag-profile`).
- 2026-10-17 (session 5): H12, every non-transposition type tested: substitution, Vigenère, bifid, ADFGX/ADFGVX,
  Playfair, homophonic, nomenclator, codebook (`12-type-diagnostics`).
- 2026-10-17 (session 5): H7, single columnar with one key, a shared phrase and trimmed ends, w 5–30
  (`16-run-geometry`).
- 2026-10-17 (session 5): T1 with 1–5, 10, 15 or 20 letters cut from the end: single columnar w 5–30 (w 31–45
  for 10–20), double columnar CC w1 2–15 × w2 2–15; T2 with 5 cut: single columnar w 5–30; T2 grille after a
  1–15-letter preamble (`17-truncated-bodies`).
- 2026-10-16 (session 3): 4 × 4 turning grille on T2, all keys (`06-grille`).
- 2026-10-16 (session 3): Nihilist read by rows, w 5–40 (`05-periodic/nihilist_control.py`). **Withdrawn
  2026-10-17**: the controls reused the plant's seed (`15`); the family is untested.
- 2026-10-16 (session 3): H5 in its weaker form, for every tested family (`07-shared-model`).
- 2026-10-16 (session 2): word transposition, row and serpentine routes (width 5–30), block moves (sets 3–12):
  neither telegram has bigram structure (`04-run-keeping`).
- 2026-10-16 (session 2): letters permuted within sets of 2–40, alone or one key on both (`05-periodic`).
  **Narrowed 2026-10-17** to n ≤ 10: the controls reused the plant's seed (`15`).
- 2026-10-16 (session 2): H5 as stated (shared strings are surviving plaintext runs), refuted by `04`.
- 2026-10-16: forward double columnar w1 ≤ 15 × w2 12–15; joint w2 16–17; CR w2 12–15 (`03-target-h1`).

---

## 2026-10-17 (session 6) — `18`: a solver for sets of n and Nihilist by rows; both excluded for T1 n ≤ 50

**Method.** In both families the ciphertext position mod n gives the plaintext column, so the columns need no search.
Neighbouring plaintext columns make a bigram in every row whatever the row order, so the key is the heaviest path
through an n × n table of column-pair bigram scores: annealing on that table, then a quadgram climb within rows, then
every rotation of the row. `05`'s hill climb had recovered sets of 20 in 1/20 plants once its seeds were fixed
(`15`); the new solver read n 11–50 on development plants in seconds. Every offset is scanned, so any preamble is
covered; letters outside full rows are not scored, so any tail and any partial-set convention is covered.

**Pre-registered** (commit a4e2427) before any control. Controls with seeds apart from the plants, random preamble
and tail of 0–20: T1 117/120 over n 8–50 (worst band 8/10), T2 35/40 over n 8–15. T2 at n 16–30 is not testable: at
160 letters a wrong key outscores the right one. Thresholds fixed and committed (7e4b61e) before the target.
**Target: no candidate.** T1 at every n 8–50 and T2 at n 8–15 below threshold by 0.36–1.08 per quadgram. Excluded:
sets of n and Nihilist read by rows, T1 n 8–50 and T2 n 8–15, any preamble or tail, and with one key on both at
n ≤ 50. With `07` (Nihilist by rows over-produces shared 4-grams), H5 is refuted for every tested family.

**A post hoc thread, closed by its own fourth check.** T1 scored 0.07–0.12 above all three noise shuffles at n 15–50.
Check 1: T1 above 20/20 own shuffles at n 20 and 30; inside K1 plants, but the plant comparison mixes order with
letter content. Check 2 (letter content removed): T1's excess +0.106 against K1 plants' −0.10 to +0.09, above all 20
(p ≈ 0.05), a lead against K1. `19-lag-profile` found no letter-pair association at any lag (family-wise p 0.40,
0.54) and multi-lag sums inside 200 K1 plants. Then the mechanism: for n ≥ 15 T1's best offset leaves 15 or more end
letters unscored at 31 of 36 widths (17 expected), dropping the rare-letter end `09` found. Check 3: cutting 20
letters still left T1 above its shuffles, but the solver dropped the next 18. Check 4, at fixed offsets: with the end
kept, T1 sits at its shuffles' 90th percentile (excess +0.054), inside the central 90%. **Lead withdrawn.** Lesson,
recorded in `18`'s README: a solver that may choose which letters not to score lets a text with a poor end beat
its own shuffles; compare at fixed offsets.

**`20`: Nihilist read by columns.** In n × n squares read by columns every output column holds one plaintext
column with the square's rows in one shared order, so each square, rearranged, is `18`'s rows problem. Plan committed
(9a352fe) before any run. One amendment during the controls (815cefd): T2 plants at n = 12 could hold no full square
(144 letters in 160 with up to 40 of preamble and tail), so the T2 band became 9–11; no T2 plant of the old band had
finished, and T1's plants were unchanged. Controls 65/70, every band passes (two misses found the true key but a
clear partial square counts against the measure). Thresholds committed (a217e60) before the target. **No
candidate:** T1 n 5–24 and T2 n 5–11 below threshold by 0.57–1.09.

**Tier 2 of `17`** (head and two-sided trims, T2 bodies, the joint attack): an Opus agent wrote `step_t2.py`, ran
controls and thresholds (committed c60d81a before any target run). All double columnar bands pass (575 w2 12–15 at
90 s). Single columnar w 31–45 fails at T1 610, 600, 590, 580, and at every T2 length; T2 w 9–30 fails at 155, 145,
140, 130. Joint controls pass only at 615 + 155. The target chain ran 11:20–18:40. **No candidate:** T1 double columnar
best −5.92 over 3,920 runs (threshold −5.10); every T1 single columnar body ≤ −0.46 below its threshold; T2 single
columnar below every recovered control's true text at each length (thinnest −0.16 at 125 letters), which settles the
agent's threshold-overlap flag; joint best −6.08. Head and two-sided trims change nothing.

**`21-dc-method`: the double columnar wall, method research** (Opus agent, plants only). Lasry's thesis does not
state how his 60% at 19 × 20 and 90% at 18–19 were measured (length, language, trials, budget); our session-3 note
"simulations, 599 letters, English" was an inference, corrected in canon. Our IDP reproduces his fitness-distance
curve at his challenge geometry, and in his presumed setting finds no K2 at 18 × 19 or 19 × 20 (0 of 6). The climb's
basin is 2–4 swaps in every setting tried; no tested factor widens it by more than about one swap, and the share of
keys inside it falls tenfold per unit of w2. But Lasry's full-neighbourhood climb with 50 M IDP evaluations per pair
(budget counted in evaluations, not seconds) passed two pre-registered controls at w1 2–15 × w2 16–17: 20/20.
Target run on T1 at full length (plan committed edac73f before any run): **no candidate**, all 28 pairs −6.22 to −6.00. Wall now: w2 ≥ 18, or
w1 ≥ 16 with w2 ≥ 16. Also found: `01`'s K2 climb stops at about 17% of the neighbourhood (noted in `01`'s README;
its controls measured it as it is, so `03` stands).

**`22-dc-trimmed`** (Opus agent, overnight 2026-10-17/18; plan committed 402e561 as controls started). `21`'s method
on three trimmed bodies: T1[0:595] (the rare-letter end cut) and T1[5:615], T1[10:615] (a head indicator cut).
Controls 10/10, 10/10, 9/10 at 595, 610, 605 letters, at least 4 of 10 in the corner w1 12–15 × w2 17. **No
candidate:** bests −5.94, −6.00, −6.01 against −5.10. Caveat: at 15 × 17 the trimmed plants needed 28 M and 48 M of
the 50 M budget (one failed), against 6 M at 615 = 15 × 41; the exclusion is weakest there.

**Outreach.** The Bochsler draft's exclusion list ("periodic transpositions", "Nihilist read by rows") is accurate
again after `18`. A possible direct route: Prof. Peter Heinzmann (cnlab, formerly HSR Rapperswil), identity not
confirmed; the 2020 report is not in the OST thesis archive (`sources/outreach-bochsler.md`).

## 2026-10-17 (session 5) — stage 4: `17` truncated bodies; no candidate

Plan committed before any run (`17-truncated-bodies/README.md`, commit 92bf3cc); thresholds written to file before
any target run; plant and solver seeds in separate streams, asserted in code.
- **Single columnar** (`colsolve.py`), T1[0 : 615 − b], b = 1–5, 10, 15, 20, and T2[0:155]. Controls pass at
  w 5–30 everywhere and at w 31–45 for 600 and 595 letters; w 31–45 fails at 611 (7/10) and 155 (2/10). Best target
  −5.50 against thresholds −4.88 to −4.94 (T2: −4.79 vs −4.41). Every body tracks the noise ceiling of its width.
- **Double columnar CC** (`dtsolve`, 30 s), w1 2–15 × w2 2–15 on T1 with b = 1–5, 10, 15, 20: 1,568 runs. Controls
  at 611 and 595 pass in both bands (39/40). Best −5.94 against −5.10. The six best runs sit on T1[0:600] at
  w1 = 15 (a complete rectangle); shuffles of that body at 15 × 15 score −5.96 to −6.01, so it is the solver, not
  the text (`noise_600.py`, reading fixed before it ran).
- **4 × 4 grille on T2 after a preamble of 1–15 letters**: controls 30/30; best target −5.86, one unit below every
  control score. The pre-registered threshold formula overlapped (a true grille started at another quarter-turn
  scores −4.21 to −4.89); the main thread rules the grille excluded however the threshold is drawn.
- **Reading.** H6's tail trims do not open a readable body in any family we can solve. H6 stays open only for
  untested trims (head, two-sided, letter-level beyond 1–5) and for families without a working solver.

## 2026-10-17 (session 5) — stage 3: `15` tail robustness, `16` run geometry; `05` controls invalid

**`15` (K2, H6).** Planted texts with t untransposed letters at an end, solvers run at full length as each exclusion
was. Single columnar (new `colsolve.py`, w 5–45): 39/40 at t = 0, 0/40 at every t = 5–20, both ends. Double
columnar CC (`dtsolve`, 90 s, 10 × 13 and 14 × 14): 10/10 → 0/10 at every t, both ends. Sets of n: robust at the end;
a preamble breaks n = 10 unless t is a multiple of n. 4 × 4 grille: robust at the end, 0/20 with a preamble. **Reading:
H6 is consequential.** If T1 carries even five untransposed letters, every columnar exclusion in canon (ours and
Bourdeau's) is void for its body. The families re-enter stage 4 on truncated bodies (`17`).

**`05` controls invalid.** `15` found that `05`'s plant drew its key from `Random(seed)` and `solve()` reseeded with
the same seed, so the first restart was the planted key in 78/78 periodic and 72/72 Nihilist controls
(`check05-seed.txt`). Verified by the main thread in `05-periodic/periodic.py` (lines 36–38, 52–54). With independent
seeds: sets of 5 20/20, 10 18/20, 20 1/20, 35 0/20; Nihilist by rows n 8 14/20, n 15 2/20, n 25 0/20. The `05` target
runs were honest searches, so sets of n ≤ 10 stay excluded; sets of n ≥ 20 and Nihilist by rows are untested. This
also reopens Nihilist by rows as `07`'s second mechanism for the shared strings. Lesson for every control: draw plant
and solver seeds from separate streams, and assert that the first restart is not the planted key.

**`16` (K3, H7).** Exact search over single columnar geometries (w 5–60, body starts 0–20, end trims 0–20, row
offset −10…10, column tops or bottoms). Best fit: 2 of the 7 runs, and every fitting pair contains NOCU (T2
position 0 fits the first column top at almost any width). Null: 2 at the 95th percentile (random sets; shuffle
pairs), p 0.37 and 0.23. Control: planted geometries recovered in 99.6% (w 5–30); no plant scored below 5. K3 plants
also give more runs than observed (median 8 at w 5 to 33 at w 30; 3.1% give ≤ 7). **H7 refuted** for w 5–30 with a
control, and for w 31–60 by the search alone.

## 2026-10-17 (session 5) — stage 3: `14` contact test for K1 (long-key double columnar)

K1's prediction: neighbours are plaintext letters far apart, so no class-contact structure, no uneven vowel density,
and no cross-telegram bigram overlap beyond chance. Nulls: 20,000 shuffles; 10,000 long-key (16–25) double columnar
plants per length; 2,000 plant pairs under shared keys with a shared phrase. Controls (sets of 5–12, row routes):
power 0.78 (contact) and 0.98 (vowel density) at 615; 0.57 and 0.64 at 160.
- Contact (V1a) and vowel density (V1c): T1 0.56 and 0.87, T2 0.84 and 0.17 under the plants. K1 survives.
- Overlap (V1b), pre-registered raw Σ c1·c2: 0.41 under independent plants, 0.45 under shared keys and phrase. The
  raw statistic mostly measures the plants' letter-count spread (519 ± 35 against the telegrams' 471). The
  count-adjusted excess, declared in Method before the run as a diagnostic: +69.9, p = 0.0028 (independent) and
  0.0035 (shared keys and phrase). **Ruling (main thread): the count-adjusted form answers the question V1b was
  written to ask, so the "weakened, not refuted" reading applies.** The overlap was found on this data in `13`,
  so it cannot refute anything. It is the second weak sign, after the shared strings, that T1 and T2 are not
  independent rearrangements of their own letters.

## 2026-10-17 (session 5) — diagnosis restart, stage 1 (`09`–`13`) and the conventions survey

Run from `PROMPT-diagnose.md`. Each experiment's readings were fixed in its dispatch prompt before it ran and are
copied verbatim into its README. Observations made before the tests (T1's rare letters near the end; both final
groups beginning REF; T2's opening holding three shared runs) are flagged in `09` and `13`.

**Type** (`12`). Against plants of 12 types at 615 and 160 letters, only the transposition family fits: plain,
with nulls, of text mixed with code words, or a jargon code then transposed. The other eight types are 40–1,137
log units below and outside their 1–99% bands. H12 refuted. The pre-registered "stands" reading missed one
condition: leave-one-out accuracy for transposition vs the rest was 95.2% at 615 but 93.9% at 160, the misses being
plain transposition against transposed jargon code (letter-identical by construction). T1 is slightly flat (IC 5th,
MIC 2nd percentile of plain transposition). 160 = 2 × 80 also fits a 9 × 9 grille without centre (H11, untested).

**One system** (`11`). Homogeneity p = 0.21; both rank Spanish first; the F difference is borderline (adjusted
p = 0.056). No group-position structure (p ≥ 0.32). Its positive controls, added after the first result: the test
catches pronounceable codewords and fixed-place nulls in 99–100% of T1-length plants, random-letter codewords in
62% (T1) and 13% (T2). The charges (survey, §4) do not split the system either: 0.399 and 0.412 per word, and
five-letter cipher groups qualify as CDE under Art. 10.

**Odd letters** (`09`, `10`). X as a stop at every sentence end overshoots (12.5 expected vs 6). X nulls at T1's
own rate fit (p ≈ 0.2), which is built in. X and F positions are at chance (p 0.73, 0.28), so position cannot tell
stop from null. Without PUNTO, P is T1's largest misfit (35 vs 16, z +4.8). F in T2 fits only F-as-stop, which has
no source. T1's last 20 letters hold half its X's: scan p = 0.019 corrected for window place and length; the
ends-only test gives 0.0001 but tests the place seen first. **Ruling: the scan governs, so by the pre-registered
text the end cluster is "suggestive only and changes nothing" for the target.** It becomes H6 with a test (`15`).

**Shared strings** (`13`). Family-wise over 25 statistics: p = 0.008 (shuffles), 0.020 (transposed Spanish
plants), 0.052 (bigram-preserving). Reading: suggestive, not established. Reversed matches show no excess. Found
after looking: the two telegrams' bigram profiles overlap more than shuffles allow (p = 0.0013, vowel pairs EE,
EA, OA), spread through T2 rather than in the runs. `14` tests it with a pre-registered null.

**Correction to `08`.** `09` found that held-out book 27738 (Palacio Valdés, *José*) ends in an English–Spanish
glossary; `10`'s sensitivity run removed the book. The glossary fattened the plants' tails, so `08`'s p values were
inflated: Spanish T1 0.08 → 0.014, T2 0.11 → 0.024; z-scores move by 0.8 at most. The book is now excluded in
`01-solver/plaintext.py` and `08` is rerun. Plants drawn before 2026-10-17 (controls in `01`, `03`, `05`–`07`,
and `09`–`13` here) include it. It made planted texts slightly less Spanish, so the solver controls were, if
anything, harder; no exclusion depends on it.

**Conventions** (`sources/conventions-survey.md`). X as a sentence separator: German army by 1930 (Weierud,
SCHOLARLY), by example; no Swiss or Spanish source; French and Spanish used STOP. Givierge leaves incomplete
columnar tables unfilled and puts indicators at the head. No final reference group or "REF" convention found.

## 2026-10-16 (session 4) — letter fit; strategy reset to diagnosis first

**Letter fit** (`08-letter-fit`). The dive had assumed Spanish from the IoC alone. Against telegraph-style
references built from 40 random corpus chunks: Spanish T1 p = 0.08, T2 p = 0.11; Italian T1 p = 0.004; Portuguese
T1 p = 0.03. Misfit letters: X in T1 (6 vs 1, z +5.3), F in T2 (7 vs 1, z +4.6; T2 has no X). A first inline look
used one 400,000-letter window and was not stable (Spanish p moved from 0.08 to 0.43 between runs); chunked
references are stable across seeds.

**Strategy.** Greg asked for a fresh start that diagnoses the cipher before choosing families. Written as
`PROMPT-diagnose.md`: diagnose, rank key types, validate with separating predictions, then attack survivors with
controls. The Nihilist wording in the Bochsler draft is narrowed to "read by rows".

## 2026-10-16 (session 3) — grille, shared-string model, Nihilist by rows; dive at its wall

**Grille** (`06-grille`). T2 = 10 blocks of 16. All 1,024 keys of a 4 × 4 turning grille (256 hole patterns × 2
directions × read by rows or columns), both uses. Controls 10/10 exact. T2 best −6.30 (inverse −6.33); same keys
on T1 −6.76 or lower. **Excluded.**

**Shared-string model** (`07-shared-model`). A shared opening or closing of 30–100 letters under one key: double
columnar 8–25 and Nihilist read by columns stay at chance (mean 2.2–3.0 shared 4-grams; observed 9). Single
columnar (4.3–35) and Nihilist read by rows (22–74, 60/60 reach 9) reproduce the excess.

**Nihilist read by rows** (`05-periodic/nihilist_control.py`). The periodic solver recovers the exact column key in
72/72 plants (615 alone, and 615 + 160 under one key), n 5–40, scores −4.03 to −4.47. The 05 target best is −5.86,
so this family is **excluded**. With single columnar excluded by Bourdeau, no tested family explains the shared
strings: they are chance (p ≈ 0.001, statistic chosen after looking) or the system is outside everything modelled.

**Outreach.** Draft letter to Bochsler for the 2020 report, through the publisher (`sources/outreach-bochsler.md`).
Not sent; Greg sends.

## 2026-10-16 (session 2) — key-type survey; run-keeping families and periodic sets excluded

**Survey** (`sources/key-type-survey.md`, one Opus agent, about 25 fetches, Langie 1922 and Givierge 1925 read in
full text). No source ties any transposition to the Oswalds, Swiss commerce or Spain 1936–37. The Swiss army's hand
cipher (Réglette, about 1918–39) is a substitution. The period handbooks describe word transposition, route tables,
block sets, the turning grille, single and double columnar. The 2020 Heinzmann / Matteotti / Liniger / Viveksanth
attempt was not found online; only Bochsler's note 44 (print) records it. One correction to the agent's reading:
same-key single columnar is not open as a joint mechanism. APMOEP as a column top needs T2 columns of at least 6
letters, so w ≤ 26, inside Bourdeau's exclusion for T1 (w ≤ 45).

**Run-keeping test** (`04-run-keeping`). Bigram structure of the raw ciphertext, forward and reversed, against own
shuffles. Plants: word transposition, row permutation, serpentine rows and block moves all detected 20/20 at 615 and
160 letters; single and double columnar controls 0–1/20. T1 p = 0.53, T2 p = 0.61. **Excluded** for both telegrams:
word transposition, row-permutation and serpentine routes (width 5–30), block moves (sets of 3–12). Not testable this
way: letters permuted within sets (13/20, 11/20), turning grille (17/20, 2/20). So neither telegram keeps plaintext
runs, and the shared strings of `02` are not surviving runs.

**Offsets.** T1 − T2 offsets of the seven shared runs: 17, 258, 34, 531, 187, 36, 326. Three are multiples of 17;
look-elsewhere p = 0.054 over moduli 2–40 (`04/offsets.py`). Not evidence alone.

**Periodic sets** (`05-periodic`). Letters permuted within sets of n by one key, n = 2–40, T1 alone and T1 + T2
under one key. Plants 78/78 recovered. Target best −5.86 alone, −5.87 joint, against −5.10; readings are noise.
**Excluded** for sets aligned from the first letter. Two perfect plants scored −5.22 and −4.92: the −5.10
threshold is not a hard floor, and the verdict also rests on the readings.

## 2026-10-16 — dive opened; Step 0; solver built; IDP landscape measured

**Step 0: is it still open?** Yes. Checked: Bourdeau's `targets/blume/NOTES.md` and his commits to 13 Oct; cyphersolver
issues 14 and 37; Fuentes's `sentinel-blume-salamanca` (README of 14 Oct: "unsolved", 0/4 synthetic K2 recoveries);
one web search for a claimed solution after 30 Sept (nothing). Findings:
- Issue 14 (Bean): three letters, I → L, in groups 38, 48 and 122. Bourdeau accepted on 30 Sept, and both hashes now
  agree. Our agent A re-read the archive scans blind and agrees letter for letter (one slip of its own, ANIPS for
  ANLPS, corrected on zoom).
- Issue 37 (Bean, 15 Oct): double transposition unlikely because of repeated strings shared by the two telegrams;
  Bourdeau's 15–25-letter key-phrase claim called an AI hallucination. We measured the first point
  (`analysis/02-shared-repeats`): real at about the 1% level. Agent B found no source for the second.
- Bourdeau's excluded region is wider than the catalog entry said (table in `README.md`). His swap-based IDP local
  search failed on plants at 19 × 23 ("a needle"), and he could not reach the Lasry paper.
- The catalog entry's "no k, w or x" is true of T2 only. T1 has 6 X and 2 K.

**Lasry's method, from the source.** The thesis full text is open via the Kobra DSpace API (bitstream
`kup_9783737604598.pdf`). Read ch. 9.4. Points that matter here: the IDP (best alignment per column pair, greedy
neighbour assignment); K2 hill climbing with segment slides, segment swaps and 3-partite swaps after a left-to-right
pre-pass; K1 solved on n-grams, then K2 refined on the full decryption. Reported success: over 60% at 19 × 20 and 90%
at 18–19 (simulations, 599 letters, English). The challenge itself fell by a fragment ("pernicious") spotted in a
partial solution, then a known-plaintext search, with a K2 dictionary hit as independent confirmation. Its K2
rectangle was nearly complete (599 = 26 × 23 + 1).

**Solver** (`analysis/01-solver`). Corpus: Gutenberg, es 13.6 M / it 8.2 M / pt 6.0 M training letters, with every
5th book held out for control plaintexts. Python reference engine with hand-worked tests; C solver; C decryption
equals Python on 300/300 random cases. IDP checked against an independent Python implementation (equal to 4
decimals). Pilots at 120 s: 15 × 17 recovered in 48 s; 13 × 14 recovered with a one-letter cyclic displacement
(an equivalent key in an incomplete rectangle; accuracy is now measured shift-tolerantly); 18 × 20 and 20 × 21
failed. At 600 s, 16 × 18, 17 × 19, 18 × 20 and 20 × 21 all failed.

**Fitness-distance probe.** At 615 letters the IDP is selective (true K2 −33.35 against climb optima −36.8 to −37.3,
plant 16 × 18) but has almost no gradient beyond three or four swaps. Swaps between columns of equal length, which
move no segment, are barely smoother. So the shift caused by mixing long and short columns is not the main cause.
The margin per link is small: a K1 column of about 38 letters crosses two K2 rows, so each wrong K2 column corrupts
a share of every column pair. This confirms Bourdeau's "needle" with a different implementation and Lasry's own move
set. A probe on the probe was needed first: three parallel probes had shared one temporary file. Fixed.

**Pass rule pre-registered** before the band controls (`analysis/01-solver/README.md`).

**Band controls** (`01-solver/controls/`). 30 of 30 recovered in w1 2–15 × w2 12–15, mostly within 10 s of a
180 s budget. w1 16–17 × w2 16–17: 0/10. w1 8–15 × w2 16–17: 7/10 (fails the 80% rule). Asymmetric probes:
w2 ≥ 20 fails the K2 search; w1 ≥ 20 is unreliable at the K1 stage. Threshold frozen at −5.10 before the target
(commit 3379632).

**H1 target** (`03-target-h1`). 56 runs over w1 2–15 × w2 12–15, CC, Spanish model: best −6.004, no candidate.
**Excluded:** forward double columnar with w1 ≤ 15 and w2 12–15 (with Bourdeau, w2 ≤ 15 whenever w1 ≤ 15),
at a control recovery rate of 30/30.

**H3 language control.** The Spanish model recovers Italian (5/5) and Portuguese (5/5) plants, so the H1 exclusion
covers them too.

**H2 joint.** Telegram 2 under the same keys moves the cliff by about one key length: w2 16–17 passes (8/10), w2
18–20 fails (1/5). Joint target over w1 8–15 × w2 16–17: best −6.085, no candidate.

**CR convention.** Control 8/10 in w1 2–15 × w2 12–15 (the two failures at w1 = 2 score as their true plaintexts).
Target: best −6.023, no candidate.

**Where this leaves double columnar.** Excluded for telegram 1 (Spanish, Italian or Portuguese plaintext): CC with
w1 ≤ 15 and w2 ≤ 15 (with Bourdeau); CR with w1 ≤ 15 and w2 12–15; and, if the telegrams share keys, CC with
w1 8–15 and w2 16–17. Open: w2 ≥ 16 alone, w2 ≥ 18 jointly, and w1 ≥ 16. No method known to us passes a control
there at 615 letters. The shared strings (`02`) point away from double columnar in any case.
