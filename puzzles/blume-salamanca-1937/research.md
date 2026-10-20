# Research log — append-only, newest first

## 2026-10-20 — session 12: historical evidence for solver inputs

Brief `PROMPT-historical-evidence.md`. Research only; no solver run, no outreach. Four Sonnet research agents ran
in parallel (BLUME identity, Oswald paper trail, the 2020 report, procedure and calibration); the main thread read
their notes and one further BAR file. Everything is in `sources/historical-evidence/`; the report is its README.

**BLUME: still unidentified.** 31 logged searches. PARES and Prensa Histórica returned 429 throughout, the BNE
Hemeroteca and HathiTrust Cloudflare walls; none were bypassed. BOE Gazeta has no Blume 1936–39 (index text);
DGFP D III has none (OCR). One snippet: "Blume Otto" in a Condor Legion decorations list (Hidalgo Salazar 1975,
p. 223), adjacency to Salamanca unverified, no Oswald link. The Salamanca telegraphic-address lists were not reached.

**Oswald trail.** The whole dossier's OCR holds Oswald only in subdossier 66 (units 68–71). Image reads add the
Hunziker letter of 19 Apr 1937 to "Osswald in Burgos, Banco Guipuzoano, San Sebastian" and a mention of another
Zurich telegram (April 1937, text absent). The BAR catalogue gives Viktor's expulsion file E2001E#1000/1571#787*,
digitised; the agent took it for a namesake because of a "1912" in the title. The main thread read its full OCR:
it is Viktor ("OSWALD (Moritz Victor) né le 15 Novembre 1909"). It dates his import–export business "auf Seite
Francos" to December 1936, records the French expulsion (28 Oct 1937) and the French consul's report of contact
with German agents, and holds one plain German telegram of his from 1938. No cipher, key, BLUME or Salamanca.
Two undigitised files remain: Legation Madrid "Oswald, Viktor" (E2200.38-04#1000/483#415*, open) and "Oswald,
Madrid" (E2001D#1000/1551#5627*, review needed).

**2020 report.** Note 44 not reached (ebook preview excludes it); no report under new routes. Unsent request drafts
extended in `agent-prior-research.md` §5.

**Procedure.** Nothing ties a method to the Oswalds. Available-only: Givierge's left-to-right tie rule and unpadded
table (MARSEILLE reproduced, `analysis/28`); Givierge and Hitt use "double transposition" for a one-table system with
keyed columns and one keyed row order. `28` shows that on complete rectangles it reduces exactly to `18`'s family
after a fixed rearrangement (200/200 keys, both directions). `18` ran on raw text and `20` on squares only, so the
family is untested: new H14. Hitt's Spanish alphabet lacks K (T1 has 2); FRUS reports a Burgos ban on code at Vigo
(Sep 1936).

**Calibration.** 14 texts, 5,929 letters, from three sources; none commercial; M1–M8 in modern orthography.

**Solver options.** `solver-options.jsonl`, seven records. Key shortlist empty. Ranked: HE-P01 (H14, complete
rectangles) and HE-C01 (calibration). HE-K01's new names are contextual guesses, not recommended. Best next test:
HE-P01 under a separately frozen plan with fresh plants. Barrier: BLUME's identity via the 1936–37 Salamanca
registered telegraphic-address lists (print, BNE).

## 2026-10-20 — session 11: short second keys with longer first keys

Greg authorized the uncovered band after 26: first widths 16–22, second lengths 12–17. Experiment
`analysis/27-short-k2` reuses 26's optimizer unchanged. Only scanner reference/input bounds change;
all four retained seeds are still completed, with the same 20,000 IDP budget, twelve restarts, Spanish
model, CC convention, full 615-letter body and -5.10 screen. No new phrases or assisted development
are used. The written README design precedes implementation; source/build/control plan freeze in
`fa32d99` precedes fresh controls. The final build passes 100 independent C/Python transposition checks.

Candidate generation filters 24's full metadata rather than its 18–28 active TSV: 1,480 numeric keys,
expanded by exact/all single rank-position swaps to 160,327 unique keys. The manifest records per-length
counts and radius-three permutation-ball union bounds. Those bounds establish that the off-list random
stratum exists for each second width. Independent verification reconstructs the sorted binary and bounds.

All forty fresh controls complete: exact 9/10, one 10/10, two 9/10, random conditioned on minimum
original-list distance >3 gives 0/10. All 28 recoveries are exact; zero false candidates. True first width
is supplied per control, with both keys and plaintext withheld. The exact miss is trial 5 (22×14), score
-5.7614; its true key does not reach the four-seed shortlist, which retains no 14-column key. Two-swap
trial 4 also misses below threshold (-5.9982). No plants, thresholds or budgets are replaced. Recorded
cost is 511.967 CPU seconds (8.533 minutes), including 354.967 scanning and 157.000 refinement. Prep,
build and verification are excluded. All forty plants and 160 refinements pass independent checks.

The full gate passes. `freeze_protocol.py` verifies control bytes independently before freezing their
hashes. Commit `5d99fe0` fixes controls/protocol before the dependent fourteen-cell target run.

All fourteen target cells finish under the frozen caps: seven first widths 16–22 for T1 and seven for
its own-letter shuffle, second lengths 12–17. All four seeds complete per cell. T1 gives zero candidates,
best -5.9662; shuffle gives zero, best -5.9317. T1 costs 86.510 CPU seconds, shuffle 90.994, target total
177.504. With forty controls, total recorded solver work is 689.471 CPU seconds (11.491 minutes), excluding
preparation, build, hashing and verification. One shuffle supplies no p-value estimate. Final independent
checks verify all fourteen cells, all 56 target refinements, protocol pins and the two freeze commits.
The main thread reruns the verifier; its report matches the agent's saved report byte-for-byte.

This fills a finite phrase-neighbourhood test in the previously uncovered short-K2/long-K1 band. It does
not close that band for arbitrary keys. The exact-list miss also shows the shortlist can lose a planted
key, so this is probabilistic negative evidence even within the list. No further solver change, extra
phrase, altered preparation or T2 search follows from the negative. The next useful work needs independent
period-text calibration or historical key/system evidence. The handoff names those remaining walls.

## 2026-10-20 — session 10: isolate the first-key stage

Greg said go after experiment 25's acceptance failure. Experiment `analysis/26-k1-recovery` makes one
optimizer change: K1 quadgram climbing now scans the existing full transformation neighbourhood instead of
stopping after stochastic patience. K2 quadgram refinement stays stochastic, with the same model, twelve
K1 restarts, 20,000 IDP evaluations and -5.10 threshold. The pipeline also removes the score -triggered stop
between seeds: every run completes all four retained seeds before choosing its best result. No exact-solver
claim follows from local optimization.

The developed experiment 25 two/trial8 plant is recovered exactly when given true K2 and first width 21, but
no K1 or plaintext. Score -4.0688, recorded 0.6 process CPU seconds. This assisted diagnostic is excluded
from fresh gates. Development commit `e27f692` and `development-build-manifest.json` preserve its build.
Before fresh controls, static review checked K1-only switching, K2 locking and all-four-seed evaluation.
Plan/build/tag guards were added and the assisted-mode source comment corrected; no optimizer changed.
One hundred independent C/Python transposition checks pass. The fresh plan was frozen in `698e38f`.

`iso26` completes fifty supplied-K2 controls: ten positive plants per width band 12–15,16–18,19–22, plus
ten wrong-width and ten own-letter-shuffle negatives. All thirty positives recover; twenty-nine are exact
and one is a complete cyclic shift allowed by the predeclared rule. Both negative strata produce zero
candidates. Recorded process CPU cost 14.0 seconds. This calibrates the first-key stage with K2 known,
not a blind double-columnar solver.

Fresh forty-case end-to-end controls `holdout26` complete all cases under the frozen caps. They repeat
experiment 25's minimum-distance strata with a new 26 seed stream and the same 1,286,188-key scanner.
Exact-list keys recover 10/10, one swap 10/10, two swaps 9/10, conditioned random keys 0/10; every recovery is
exact. The missed two-swap trial 2 scores -5.8084, below threshold. All random-key cases also stay below
threshold. Zero false candidates: the full gate passes. Each run completes all four retained seeds.
Recorded process CPU cost 2,916.034 seconds (48.60 CPU minutes), excluding isolated/development work.
Independent reconstruction/decryption/rescoring verifies all forty plants and retained-seed diagnostics.
Both complete gates now pass. `freeze_protocol.py` independently verifies the exact control bytes before
pinning them and the build in `protocol.json`; `results/pre-target-verification.txt` records this check.
The protocol is committed before the dependent target run. No target-guided tuning has occurred.

Protocol/control commit `6d6b4f0` precedes `target26`. All twenty-two cells complete: full T1 best -5.9141,
matched own-letter shuffle best -5.9484, zero candidates for both against -5.10. First widths 12–22, second
lengths 18–28, full 615-letter body and Spanish model remain fixed. Every cell completes all four seeds.
Independent verification checks all twenty-two decryptions, all 88 seed refinements, best selection,
protocol/input hashes and cost sums. T1 costs 792.058 CPU seconds; shuffle 764.828, target total 1,556.886.
Including ninety fresh controls, recorded solver CPU cost is 4,486.920 seconds (74.782 CPU minutes),
excluding development, preparation, compilation and verification. `timing.py` preserves descriptive wall
times from result/cache timestamps, with host-load limitations.

No reading, no post-target tuning and no independent T2 search. The K1 repair passes the fixed controls;
the actual system, preparation and key material remain unresolved. This is a conditional finite-band
negative, not an exhaustive key/cipher exclusion. The one shuffled body is descriptive, not a p-value.

While the controls ran, a bounded web follow-up on the reported 2020 attempt did not locate a matching
report. Queries and scope are retained in `sources/heinzmann-search-2026-10-20.md`. The possible cnlab
identity remains unconfirmed; no outreach was sent and no search input changed.

A separate coverage review found that first widths >=16 with second lengths 12–17 remain outside our
validated target region. Experiment24's actual target activated only second lengths 18–28 and first
widths 12–22 from its wider phrase metadata. `26/scope-audit.md` records the earlier source lines; H1/H2
scope wording is corrected. This does not change the frozen experiment 26 target grid or establish that every
contextual phrase has been tested.

Stop at this completed attempt. The next bounded engineering test is the short-K2/long-K1 gap under a new
declared plan and fresh controls. External key evidence and independent period-telegram calibration remain
separate open routes; no wider blind campaign is started.

## 2026-10-19 — session 9: diagnose the missed seeds and enumerate their neighbours

Greg said to proceed with the solver weakness measured in experiment 24. Experiment
`analysis/25-seed-retention` first reconstructed all five old failed plants. Their base-key ranks at the
true first width are 1,717; 2,916; 4,876; 3,336; and 394. Giving the old refinement both that base key and the
true first width recovers **0/5**, with plaintext agreement 0.10–0.17. These are assisted development
diagnostics, never blind controls. Losing the base seed was a symptom; wider retention alone is not a fix.
The diagnostic source and hashes are archived with `results/development.json`.

The revised search enumerates the original 5,284 numeric keys plus every one-rank-swap neighbour,
deduplicated to 1,286,188 keys. It streams the list and retains four seeds per stated first width. The
20,000-evaluation refinement budget, twelve K1 restarts, Spanish model and -5.10 candidate threshold stay
fixed. A development benchmark recovers the old one-swap failure at its supplied true width 22 in 44.868
process CPU seconds; width 19 is a cost check (83.309 seconds, no candidate), not a recovery test.
`benchmark-build-manifest.json` pins the development build. Neither result enters the fresh gate.

The frozen `holdout25` plan has ten plants each at minimum distances 0, 1 and 2 from the original list,
plus ten uniform-random permutations conditioned on minimum distance >3. The true first width is supplied
in each control; keys and plaintext are withheld. This calibrates per-width recovery, not a full unknown-width
blind attack. Exact and one-swap groups must each recover >=8/10, with zero false candidates across all
forty plants, before another T1 run. Per-process caps are 180 CPU seconds for a scan and sixty for a
refinement. Cap hits leave an incomplete result; no replacement plants or higher cap are allowed.

Review caught a post-search diagnostic comparing keys of different lengths. The corrected diagnostic uses
same-length seeds only, or null if none are retained. The source-hash guard stopped the original run after
the edit. Seven partial records, the old driver/build/plan and a restart notice are preserved. The corrected
run repeats the same forty plants and seeds under commit `3eeac16`; the archived seven do not enter its
gate. The independent verifier checks the exact diagnostic-only AST change and plan/search equivalence.

All forty fresh controls completed. Exact-list keys recover 10/10, one swap 10/10, two swaps 9/10 and
conditioned random keys 0/10. Every recovery is exact. These minimum-distance, supplied-width controls
differ from experiment 24's base-relative perturbations and full unknown-width search; their percentages
are not a direct comparison. Fresh-control work costs 3,242.504 process CPU seconds: 3,157.804 scanning and
84.700 refinement. This excludes development and the archived aborted run.

The gate **FAILS**: the missed two-swap trial 8 (21x22) scores -4.5505 above -5.10, despite only 0.4683
shift-tolerant plaintext agreement (0.0390 in-place). `diagnose_gate.py` → `results/gate-diagnostic.json`
reconstructs it without search. The winning second key is exactly correct; the first key is wrong. The true
plaintext scores -4.068789. The pipeline stops after its first seed because the imperfect output passes the
score-only stop. The immediate failure is first-key refinement/acceptance, not failure to obtain K2.

I initially told Greg there were no false candidates by inferring that the missed plant was below threshold.
That was wrong. The independent verifier exposed it; I corrected the update immediately. No target protocol
was frozen and no experiment 25 T1/shuffle run was made. The threshold, seeds and budget were not changed.
`verify_results.py` reconstructs all forty plants and checks every recorded decryption/score, recovery and
cached retention diagnostic, along with the restart provenance. The failed gate is the result, not an
incomplete control batch. See `results/verification.txt` and `results/summary.md`.

H13 retains experiment 24's finite-list negative; this experiment adds no target evidence. Direct neighbourhood
enumeration is CPU-feasible, but random-key coverage is absent here. Next engineering wall: validate the
first-key stage with known-correct K2 and a reliable acceptance rule on fresh controls before more target
work. System, preparation and historical trade-language calibration remain open. No wider blind campaign
is started.

## 2026-10-19 — session 8: phrase-seeded solver, passing conditional controls, no T1 reading

Greg requested a new scripted solver attempt, then explicitly authorized subagents. Implemented a bounded
phrase-seeded attack in `analysis/24-phrase-seeded`: contextual phrase generation, C IDP scan/seeded refinement,
Python driver, fixed controls/target protocol and result summaries. Reuses 21's C engine without editing it.
The 8,534 generated numeric guesses give 5,284 active second keys of lengths 18–28. First widths 12–22.
Both repeated-letter tie directions are covered. This is a key hypothesis, not a plaintext crib.

Development: three plants recovered (exact, one swap, two swaps). After independent code review, narrowed the
actual scan to the calibration region, separated exact/in-place/shift metrics and pinned all plant/model/key
inputs. Frozen code and control plan committed `0c21bf7` before the holdout. No true key or plaintext is passed
to C; Python independently checks each reported decryption and score. C/reference transformation checks 100/100.

Holdout: **10/10 exact-key, 9/10 one-swap and 6/10 two-swap exact recoveries**, with no extra shift-only successes.
The two-swap stratum fails the >=8/10 gate. All five failures omit the base phrase seed at the true first width
in the top-four shortlist (`diagnose_failures.py` and checked-in output). This establishes seed loss, not that
retaining each omitted seed guarantees recovery. An independent verifier reconstructed all 30 plants and
confirmed the reported scores/metrics, hashes and gate. Controls remain modified literary plaintext.

Protocol `7bdf882` pins the complete holdout/build and the passing distance-0/1 strata before any target run.
**Full T1: no candidate**, best -5.8023 versus -5.10, 37.563 CPU seconds; own-letter shuffle -5.9946, 34.909 CPU
seconds, no candidate. One shuffle is not a p-value. No list expansion, trimming or parameter changes after the
target. T2 was not independently searched; there was no T1 key to transfer and no 160-letter calibration here.

H13 is weakened for this finite list, body and pipeline; other key material, two-swap coverage, unrestricted
long keys and historical preparation remain open. The scripts now provide a practical way to test externally
supported key material. If pursuing method work, measure/improve seed retention on blind controls (including
off-list keys) before another target run. No broader campaign started; no outreach or push.

## 2026-10-18 — session 7: feasibility and method audit (Greg's review request)

Read the research state, current search code, control generators and checked-in results; re-read Lasry chapter 9
from the cached thesis and checked the public implementation/prior work. No new target search. Full report and
reproducible arithmetic: `analysis/23-method-audit/{README.md,audit.py,result.txt}`.

**CPU:** 21/22's four T1 body sweeps used 26.278 process CPU hours, 112 length-pair runs at 50 M IDP evaluations
each, zero candidates. At w1 12–15 / w2 16–17 the median was 29.40 CPU minutes per run. Those runs are practical;
exhaustive long-key enumeration is not. The existing C/Python transformation check was rerun: 300/300 matches.
The longer-key pilots do not establish a completion budget; swap-ball sizes are not a runtime law for the
segment-move search.

**Scope corrections:** "excluded" by a probabilistic search means a negative result conditional on its plant
distribution, widths, system and budget. 21's controls are 20/20, 22's 29/30, rather than uniform guarantees.
Controls are modified novels (PUNTO, dropped articles, spelled quantities), not independent period commercial
telegrams. Experiment 12's generators do not cover all codebooks, nomenclators, restricted keys or hybrid
systems; its classifier score gaps are not calibrated historical odds. H12 changes from blanket refutation to
weakened. Transposition remains the best working hypothesis. Experiment 11's p = 0.21 does not establish one
system or shared keys. Historical dead-end entries above/below remain as the record of what was concluded then.

**Content criterion corrected:** Werner's wool story is testimony. A valid decryption may contradict it; it is
not known plaintext and must not be imposed on a candidate.

**Audit recommendation; no new campaign started:** pause wider blind target sweeps. Pursue the reported 2020
attempt, identify BLUME via address/directories/receiving records, and seek drafts/replies/more traffic or a key
instruction. Before another long search, calibrate recognition and recovery on independently sourced period
telegrams, then vary preparation/null/error assumptions one at a time. A dossier-derived key list or crib attack
is a bounded next test only with a planted control. No outreach sent; existing draft remains unsent.

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
