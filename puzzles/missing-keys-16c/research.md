# Research log — append-only, newest first

## Dead ends
- 2026-11-16 — The key census as a product of its own (plan Track 2, Q1). Bourdeau's "How keys changed" already
  covers 783 systems. Closed before it started; see the entry below.

---

## 2026-11-17 — No. 1336, Speciano and Borromeo: 17 values built and confirmed on a second pair

Greg's instruction after the 2911 bench: take the method to a message with no key and no decipherment.
Record, bars and every figure: `items/1336/README.md`, `items/1336/results/`.

- **Material.** Cipher slip F 47 inf. c. 269r (15 lines, about 795 signs) with its period translation on
  c. 270r; cipher slip F 49 inf. c. 44r (102 signs) with a two-line clear note under it; one bare cipher line
  inside a clear letter of 4 July 1574, F 131 inf. c. 14r.
- **Readers** (six Opus cipher readers in two rounds, two plain readers, isolated). c. 44r: 0.941. c. 269r:
  0.779, then 0.807 after one guide revision. Under the 0.85 bar: **wall for the registered plan, sign
  legibility of c. 269r at 750 px.** The archive serves no larger size.
- **Plan B, registered before any build:** build on the c. 44r pair, test on c. 269r. The plain build stopped
  on the new null check; `--abridged` gave 17 values (16 letters, one two-letter value).
- **First test failed as written**: accuracy 0.712 (bar 0.55), signs valued 0.597 (bar 0.60), shuffled
  control 0.457 (bar 0.30). The control bar came from calibrations with nearly full tables; with 40% of signs
  unvalued the scorer forgives a shuffled table. My bar, wrong for the case, left failed.
- **Second test, registered after that and labelled post hoc: pass.** Exact matches at the pointer with the
  table held: 263 of 373 places; twenty shuffles 110–141.
- **Reading of it.** The cipher is a simple substitution, one sign per letter, with at least three signs for
  `a`. The two slips share a table, and the note on c. 44r is its slip's decipherment. The clear text on
  c. 270r is a report to "lei" on the Pope's choice of three deputies for the jurisdiction case, with
  Monsignor Carniglia told to keep silent; the note names "the castellan of Milan" and an officer "of the
  Senate". No reading of c. 14r is claimed.
- **Method notes.** `--abridged` works on a 101-sign pair. The null stop in plain `build` caught a degenerate
  table on its first real use. A control that shuffles values needs a scorer that does not forgive unvalued
  signs.

## 2026-11-17 — No. 2911 bench reopened on Fable: a blind builder meets the H6 bars

Greg ran the bench prompt again in a session on Fable. Record and every row: `items/2911/bench/README.md`,
`runs/results.tsv`. The bars, the sealing and the held-out inputs were not changed. No sign value was read.

**Trials, all on `p1` first.**
- `v7_beam`: read the cipher in order with a pointer in the plain text; a hypothesis is one table plus one
  pointer; a beam keeps 4,000. Passed a planted pair (`bench/synth.py`: precision 0.91 and 0.97). As registered
  it failed `p1` (0 of 3 rows right; every unit in one gap).
- Why (`variants/vx_beam_oracle.py`, counts only; `bench/spelling.py`): with the true table held, a sign spells
  the print at the pointer at 55% of places. Of the print's 1,893 letters on `p1`, 1,265 sit in blocks equal to
  the true decode; 714 decode letters have no print, in 68 blocks; 228 small differences of 158 kinds. The
  plain side is a loose abridgement, cut and reworded every 20 signs or so, not a copy with 20 holes.
- Costs refitted to that (a miss 0.4 of a letter, three settings tried): 8 rows right, 5 wrong, precision 0.72.
- `v8_handoff`: the beam's path and table start the `v1_gap` passes in a ±15-letter corridor, no null:
  precision 0.924, recall 0.245, 9 right, 3 wrong.
- `v9_rounds`: corridor re-centred each round: 0.928, 0.320, 12 right, 1 wrong.
- `v10_mark`: rows marked by evidence against chance, not by a 60% share: **0.964, 0.629, 36 right, 0 wrong.
  Passes the bar on `p1`.**

**Full pair.** `v10_mark`, the one registered run: precision 0.921, recall 0.579, 33 right, 4 wrong. Fails
narrowly (recall bar 0.60; wrong rows 10.8% against 10%). Its log showed the path still moving in the last
round. `v11_settle` runs rounds until the path settles: `p1` unchanged; `full` 0.935, 0.617, 33 right, 3 wrong
(8.3%), 1 `certain` wrong, no null. **`v11_settle` meets the four bars on `p1` and `full`**, with `full`
looked at twice.

**Bare letters** (never used in a build; `score.py <key.tsv> inputs/bare-*.txt`). Table from the full pair
under `v10_mark`, scored before `v11` existed: V/134 66.2% of signs valued, 94.1% of those agree with the
period key; V/125 (another hand) 62.9% and 79.2%. Table from `p1` alone: 70.1% and 96.0%; 57.1% and 93.3%.
The period key itself values 83% and 77%.

**Port.** `line/align.py` has the builder as `build --abridged` (`build_abridged`: `beam_read`, `GapSegment`,
`mark_by_evidence`), and the plain `build` now stops when over half the valued places are null. The ported
code rebuilds the `p1` table to the same score. `line/test_line.py`: 26 tests pass, two new. Calibration 03
rerun: R1–R3 pass, figures unchanged. Calibration 02 rerun: S1a, S2 and S3 pass on all five seeds; `result.tsv` is byte-identical to the
checked-in one (the plain `build` path is unchanged).

**Limits found.** (1) On a short planted pair the beam finds either most of the table or half of it,
depending on beam size and seed (2,000: 26 of 26 common signs; 600 or 1,200: 13 of 26). No wrong row in any of
those runs: it fails by saying less. (2) 14 of 44 frequent signs on `p1` stay unmarked. (3) One cipher, one
plain side; the costs (a right value hits at 55%) were fitted to this pair's looseness.

## 2026-11-17 — Next item gate: Speciano and Borromeo

Greg opened the scope for another missing-key item. The Florence retry
for Baldovino no. 2345 timed out. Acciaiuoli no. 2351 has a reported
same-day cipher, clear copy and bare letter. Its Florence endpoint
also timed out outside the sandbox. Keep both queued for access.

Castaldo no. 1332 has usable Ambrosiana scans and visible glosses. I opened
sample images before checking `line/taken.tsv`, which already lists it.
The open catalogue entry is stale. Bourdeau merged a reconstruction in
[PR 224](https://github.com/dbourdeau/cyphersolver/pull/224), and
[issue 746](https://github.com/dbourdeau/cyphersolver/issues/746) records
an independent reconstruction. Drop it as a target. Biglia no. 1338
also has a [published reconstruction](https://dbourdeau.github.io/cyphersolver/biglia1565.html).
For Luppi no. 1549, the [catalogue vetting](https://cyphersolver.com/solve/1549.html)
reports the V/140 repertoire and substitution. This puts it behind a
proven missing-key candidate. No test of that connection was run here.

**Proceed with the access and transcription gate for no. 1336.**
Ambrosiana F 47 inf. no. 131 c. 269r bears a cipher slip and an instruction
to see the next folio. C. 270r bears the Italian text. The three OPAC
records and the inspected transfer leaves are recorded in
`items/1336/gate.md`. The c. 269r image is cramped and blotched.
The smaller slips in the other files are separate tests of shared values.
The direct images were fetched and hashed before transcription. A short
independent legibility sample is the first decision. The requested
Opus and Fable assignments are unavailable in this harness. Model
substitutions await Greg.

## 2026-11-17 — Reopened 2911: merged seeds recover some syllables

Greg asked for a key after the first bench stop. Three registered blind p1
trials tested whether a broader start would carry the exact-lock method.
The H6 bars and the held-out inputs stayed frozen.

- `v4_islands` allowed adjacent unresolved signs between fixed letters.
  Its synthetic segmentation checks passed. It added no values to any
  shortlisted start. The output marked five rows, three right.
- `v5_cribs` searched for exact letter-or-open-syllable segmentations that
  obey repeats inside a longer window. The synthetic check passed. The
  restricted search produced no seed on p1.
- `v6_merge` assembled compatible starts when the union decoded an exact
  span using values unique to each parent. The selected table carried 15
  provisional values from four starts. The multi-sign extension added
  none. It marked eight rows right and two wrong. It got 206 places
  right, 152 wrong, and left 974 silent. Of the syllable places, 105 were
  right and 57 wrong. See `items/2911/bench/runs/v6_merge-p1-errors.tsv`.

The combined table reached 0.575 precision and 0.155 recall. A cross-seed
match verifies only the values needed for that match. Errors carried in
from a parent can remain even when the match is real. A broader start
did not make the exact locks productive on p1. The synthetic checks
tested local segmentation and merging, not a letter with 40% abridgement.

The bench reached its registered variant limit including the oracle diagnostic.
H6 is still weakened and H7 open. Full and both bare letters stayed held out.

## 2026-11-17 — No. 2911 bench: correct seeds found, extension stalled

Registered and ran `v3_seed` once on the frozen first page against the print
(`items/2911/bench/README.md`, `runs/results.tsv`). The cipher-only group
rule proposed one pair and the sealed scorer rejected it. Neither clear unit
occurs in the print. No sign met the two-context null rule. The repeated-span
seeds and exact locks left no marked values. The provisional table reached six
of 44 frequent signs, below the threshold for the gap passes.

The aggregate post-run audit (`runs/v3_seed-p1-seed-audit.tsv`) found 16
all-right seeds of 3,255. The best-ranked all-right seed was second. Neither
of the two all-right seeds in the shortlist gained any value from the lock
rule. The builder chose seven provisional values, five right. Two distinct
problems remain: extending a sparse correct table and choosing it from among
plausible starts.

The strongest blind table remains `v2_boot` at 0.566 precision and 0.065
recall. Its 86 right places are all letters from the most frequent band
(20+ uses). Of its 66 wrong places, 64 are letters in that band and two are
syllables in the 1–4 band. `runs/v2_boot-p1-errors.tsv` gives the full tally.
The oracle remains a diagnostic. The p1 failure triggered the stop rule.
Full and both bare letters were left held out. No code was ported to
`line/align.py`. The 24 line unit tests passed. The calibrations were not rerun.

To breach the wall, first test extension from sparse, spatially distributed
anchors on the same kind of synthetic abridgement prescribed by H6. A lock
over several adjacent unresolved signs can use every legal segmentation
between two independently fixed anchors and count only the values they agree
on. This would test extension where the single-sign lock has no foothold.
Require independent evidence when ranking competing starts.

## 2026-11-17 — Pilot on no. 2911 (known answer): stage 4 failed; the outside check says why
Greg approved no. 2911 as a test of the line against a known answer (the period key VI/82 survives), with the key
rebuilt blind. Record: `items/2911/README.md`; diagnosis: `items/2911/outside/README.md`.

**Stages 1–2.** A Fable item agent cut strips, wrote the sign guide (56 base shapes, 6 marks, three picture
sheets) and the stage 4 bar; all committed before any reader ran (46d7d46). Ten isolated Opus readers.
Cipher agreement (`items/2911/results/agreement.tsv`): 0.893, 0.912 and 0.745 by token on the three pages, 0.896
in all. Plain side: Machiavelli's autograph defeated the readers; the two-reader consensus kept 57% of the words.
An Opus agent then fetched the printed text of the same copy (Passerini–Milanesi, Opere VI, 1877, pp. 54–55 n. 1).

**Stages 3–4.** Primary run as registered (cipher consensus against plain consensus): accuracy 0.333, coverage
0.782, control 0.333. Side runs, the printed text among them: accuracy 0.250, control 0.250. The built table is
all nulls: 2,486 of 2,552 valued places. Failed; no bare letter read. `items/2911/results/heldout.tsv`.

**After the failure** (main thread; "after a fix"). Joining doubled signs (a a: 80 pairs where 7.9 are expected)
and making null and skip dear at the start still gave 61–69% nulls and no letter value. Stopped after that one try.

**Outside check** (isolated Fable agent with the key sheets; cut off by a usage limit after its scripts ran).
- The true key values 99.5% of the tokens the readers read: the transcription is usable.
- The cipher is 53% syllable signs, 41% letter signs, 0.2% nulls; it decodes to 4,619 letters. The printed plain
  text has 3,145.
- 41.7% of the cipher tokens have no counterpart in the plain text, in 20 interior stretches (longest 626 tokens):
  Machiavelli abridged throughout.
- The true key itself scores 0.735 by the held-out scorer on the covered stretches. The 0.85 bar was out of reach.
- Reader error where the other reader is right: 1.8% and 1.5% of covered tokens.

**What broke: the aligner's assumption that both sides of a pair hold the same text end to end.** The calibration
pairs were complete on both sides and had few syllable signs, so they could not show it. The plain side is the
second cause. The transcription is not a cause.

**Cost of the pilot** (tokens as the harness reported them per agent; wall time per agent).
| Stage | Agents | Tokens | Wall |
|---|---|---|---|
| 0 gate, four candidates | 3 Opus scouts, 1 Fable key-sheet check | 79k + 122k + 232k + 173k | 3–19 min each |
| 1–2 prep (strips, guide, prompts, bar) | 1 Fable | 207k | 17 min |
| 2 readers | 10 Opus | 1,456k in all (87k–195k each) | 4–17 min each, in parallel |
| 2 printed plain text | 1 Opus | 108k | 6 min |
| 3–4 align and held-out | same Fable agent, second call | about 270k as reported | 16 min |
| 7 outside check | 1 Fable | not reported (cut off) | about 30 min |
Readers are the largest cost and worked. The four plain readers (about 540k) bought little, since a print existed.

**Where it stuck.** (1) The gate: catalogue race state, a dead host, a login, a surviving key. (2) The plain side:
a hard autograph and an abridged copy. (3) The aligner: complete-pair assumption; no stop for a degenerate table;
float underflow at 3,400 unanchored units (worked round in `items/2911/align_log.py`).

## 2026-11-16 (night) — Pilot gate: four candidates, none through
After no. 2192 (below), in the order the prompt gives:
- **No. 2345** (Baldovino del Monte, ASF): race passes. Images, pair and size not checked: the ASF host
  (`archiviodistatofirenze.cultura.gov.it`) timed out for the scout over 30 minutes and for the main thread twice,
  two hours apart; the web-fetch network got "connection refused". The scout found that DECODE lists the Cosimo I
  key volume (`ASFi_SIVol3_*`, records 6087–6097 dated 1554–55, login needed), which the catalogue entry denies.
  `items/2345/gate.md`. Ledger: `queued`.
- **No. 1468** (head of the queue): not gated. Scans need a reader account at CEHM. It is also a 1913 telegraph code.
- **No. 2911** (Dieci di Balìa to Machiavelli, 17 Aug 1510; with 2910 and 1549): race passes; BNCF Teca serves
  300 dpi masters (`…ImageViewer?idr=<id>&azione=showImg&usage=2`), not the 900 px the catalogue reports; a real
  period pair exists (V/140, the Dieci's cipher copy of Niccolini's letter from Rome of 5 Aug 1510, with
  Machiavelli's autograph decipherment V/139 cc. 1v–2r). **Gated out on check 5:** a Fable agent, isolated so that
  the main thread stays blind, compared the period key sheets BNCF Carte Machiavelli VI/82 with the letters by sign
  inventory and by six glossed signs on V/139 c. 1r. Units 1–4 are one cipher and it is this one; unit 5 ("Cifera di
  messer Goro", cipher of Messer Goro) is another. So the item is a key lookup. A 19th-century sheet in VI/82 and
  the modern clear text of V/136 suggest someone has read these letters with it. Not verified: whether the Edizione
  Nazionale prints V/134 and V/125. `items/2911/gate.md`, `items/2911/keysheet-check.md`.

**What the gate cost.** Four scouts and one check. The four that ran to the end: 79k, 122k, 232k and 173k tokens
(3, 17, 19 and 8 minutes). No item reached stage 1.

**What is left in the queue for 1450–1700 that can be worked today** (`line/queue.tsv`, main-thread scan of
access notes): nothing clean. ASF holds 13 of the candidates and is down. The 33 Sforza items and no. 880 need a
DECODE login. BnF fr. 15567–15568 (nos. 2838–2841) are in ciphers Tomokiyo has keys for, and Bourdeau's
contributors are reading them now (`canon.md`). The rest are German, Swedish or one line long.

## 2026-11-16 (later) — Key line, phase 0: tools and calibration; pilot gate
Ran `PROMPT-key-line.md`. Built `line/` (`align.py`, `compare.py`, `fluency.py`, `queue.py`, `taken.py`,
`ledger.tsv`, 24 tests). One Opus agent wrote the support tools; the aligner and both calibrations are main-thread.

**Differences from `PIPELINE.md`, as the prompt asks to be noted.**
- *Real calibration pair.* Saint-Goard's letter of 23 Dec 1579 cannot test the aligner: its cipher side exists
  only as letter values read with the key, and the Longlée table only as an image. Used es. 132 f. 255 (blind sign
  transcription) against Teulet's print of the Simancas minute, scored on Cp.30. `analysis/03-calibration-real/`.
- *Control bar.* The edit-distance scorer gives a shuffled table 0.25 by chance. A bar of "≤ 25%" is that chance
  level. Calibration used ≤ 0.30; stage 4 should say "control ≤ 0.30 and at least 25 points under the accuracy".
- *Composite signs.* The design treats a token as one sign. Cp.30 needs base, mark after and marks above as
  separate units (`25:curl^bar` → `25`, `:curl`, `^bar`). `align.py` does that; a sign guide chooses the split.
- *Status rule.* `probable` needs four supporting places, not three (calibration run 4).
- *Queue size.* The catalogue gives 132 class A desk-workable items, not 76. 43 of them are named in a target
  folder of Bourdeau's repository. Queue after `--taken`: 89.

**Calibration.** Both pass after three fixes to the aligner; each failure and fix is in the experiment README.
The failures: (1) on the real pair every sign went to null and rare signs took whole phrases; (2) the first cure
cut code words to a syllable on the synthetic pairs; (3) a code sign and its mark split one word. Final figures:
synthetic, five seeds, 0 wrong among 41–44 marked values, held-out 0.93–0.95, control 0.25; real, 26 of 29
frequent signs right, 0 of 13 `certain` wrong, held-out 0.83 against a true-key ceiling of 0.79.
The five seeds and the real pair were used to fix the aligner, so they are spent as tests.

**Pilot gate, no. 2192: gated out, race lost.** The scout found `targets/sosa1554/` in Bourdeau's repository
(commit cbd93dbe, merged 12 Nov 2026): a contributor rebuilt the letter-1 key from the Panama 29 clear copy and ran
a held-out test (their figure: 447 of 587 letters). Verified by the main thread on the repository tree.
`catalogue.json` shows none of this: no `reserved`, no `writeup`. `items/2192/gate.md`.
The scout read that project's notes, which summarise sign values; it is exposed and was not used again.
PARES returned HTTP 429 to every image request, so no image recipe was verified.

**Consequence for the queue.** Work in progress is visible only in `targets/*/profile.json`. `line/taken.py`
reads the 879 profiles (fetched 2026-11-16) and `queue.py --taken` drops the ids they name. A profile may name
an id as a cross-reference, so 43 is an upper bound on items truly taken.

## 2026-11-16 — Race check and target choice
Merged the plan branch. Greg redirected: recover a missing key, easiest first, using Tomokiyo's unsolved list and
the existing keys as leverage. Fetched and read `unsolved.htm` and `henryiii.htm` (cached, `sources/cache/cryptiana/`),
then Bourdeau's site and `catalogue.json`.

Found:
- Nearly every item on Tomokiyo's list in our period is solved or has been attempted by Bourdeau's group
  (Birago 1571, Blancmesnil offline, Moncada, Segur, Throckmorton margin, f. 151 too short).
- Bourdeau's project has grown into a collective with a 1,388-item open catalogue and a published key census.
  Both planned tracks sit inside it. `canon.md`, "The field".
- `analysis/01-gaps/`: 56 desk-workable items of 1550–1620 in his catalogue (17 A, 22 B, 17 C).
- Among them, the Terranova → Sfondrati set (nos. 2077, 2518) has the most same-key ciphertext with no key
  claimed, is Spanish of 1583 (the family we hold four keys for), and is not attempted. Chosen as target.
- Viewed one page (SCMisc 50207). Its features match Tomokiyo's description of the general cipher Cg.12 (1582).
  Recorded as H1. If H1 holds, this target yields a reading, not a new key.
- Passed over: Añover 1610 (key already rebuilt by a contributor, 13 Nov); Bazin 1573 (probably Monluc's cipher,
  H5); Nevers 1595 and Duplessis-Mornay (attempted and failed there).

No transcription and no decoding was done.

## 2026-11-18 — no. 1336: table widened to 26; the bare line's test fails on reader disagreement
- **Widening (registered first).** Blind `build --abridged` on the C-and-D consensus of c. 269r against c. 270r:
  41 rows, 23 marked. Of 14 marked signs shared with the c. 44r table, 13 have the same value (bar: 80% of at
  least 8). Nine new letters; `key-v1.tsv` has 26 values. The differing sign (one witness against 22) takes
  the better-witnessed value under an amendment written before any run on c. 14r.
- **Bare line (registered first).** Readers E and F (guide revision 1) agree at 0.806; clear readers PC and PD
  at 0.759 on the four lines round it. Word-coverage test against 200 shuffled tables: E above 194, F above
  167; both had to pass. Fails. No reading claimed.
- **Observation, untested.** The four decodes share `con`, `icipa`, `rum?nto`; F's gives `delfrumonto`. The
  clear line before it ends "il tutto e". About ten signs under a stain are the wall, not the table.
- Files: `items/1336/README.md` (third stage), `results/w-*.tsv`, `results/c14-*.t*`, `results/agreement-c14.tsv`.
- **Later the same day: four readers combined (post hoc, registered first).** `items/1336/lattice.py`: the
  readers' rows as columns of votes, best path by vote share plus an Italian letter-trigram model (Machiavelli
  *Opere* vol. 3 OCR). Self-check on planted lines: 16 of 20 Italian pass, 1 of 20 random. On c. 14r the true
  table scores above 199 of 200 shuffles. Proposed reading `?con?participa???u?ne??de?rum?ntoe`. Six open
  places hold signs the readers agree on that the table does not value yet.
- **Evening: four readers on the main slip.** `line/merge.py` halves the unread places on c. 269r (143 to 77).
  A blind build on the merge agrees with the 26-value table on 23 of 24 shared signs; `key-v2.tsv` has 28
  values. The bare line's test is now above 200 of 200 shuffles; the reading is unchanged. About 11 cipher
  signs between "monsignor" and "Frumento" have no counterpart in the translation. Method written up in
  `line/METHOD.md`; result in `items/1336/READING.md`.
