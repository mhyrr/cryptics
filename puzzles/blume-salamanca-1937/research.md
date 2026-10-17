# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry that killed it. Nothing here is deleted.

- 2026-10-16 (session 3): 4 × 4 turning grille on T2, all keys (`06-grille`).
- 2026-10-16 (session 3): Nihilist read by rows, w 5–40 (`05-periodic/nihilist_control.py`).
- 2026-10-16 (session 3): H5 in its weaker form, for every tested family (`07-shared-model`).
- 2026-10-16 (session 2): word transposition, row and serpentine routes (width 5–30), block moves (sets 3–12):
  neither telegram has bigram structure (`04-run-keeping`).
- 2026-10-16 (session 2): letters permuted within sets of 2–40, alone or one key on both (`05-periodic`).
- 2026-10-16 (session 2): H5 as stated (shared strings are surviving plaintext runs), refuted by `04`.
- 2026-10-16: forward double columnar w1 ≤ 15 × w2 12–15; joint w2 16–17; CR w2 12–15 (`03-target-h1`).

---

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
