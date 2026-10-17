# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry that killed it. Nothing here is deleted.

- (none yet)

---

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
