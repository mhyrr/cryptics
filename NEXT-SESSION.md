# NEXT-SESSION — what is in flight

**Last updated:** 2026-10-17 (BLUME SALAMANCA session 6: periodic and Nihilist families excluded; double columnar wall moved to w2 ≥ 18)

## State
Skeleton, rubric, templates, scripts, and slash commands exist. The first
catalog sweep landed **104 entries** (89 live, 15 calibration: solved, hoax,
noise) across six categories, plus ~30 rows in `catalog/EXCLUDED.md`.
`catalog/INDEX.md` is current. Abramelin has had a second pass; the remaining
first-sweep scores are provisional.

The original first-sweep entries were verified by WebFetch only (the session's search
budget was exhausted before the agents started). Every entry says what it
could not verify under `## Unverified claims`. Treat scores as provisional.

## Active dives
- **[blume-salamanca-1937](puzzles/blume-salamanca-1937/NEXT.md)**: two cipher telegrams, Zurich to "BLUME
  SALAMANCA", 8 Jan 1937 (TK-008). **Session 6 (2026-10-17):** every family with a solver is now excluded. Sets of
  n and the Nihilist transposition (rows and columns) are excluded (`18`, `20`), and so are trimmed bodies (`17`
  tier 2). Double columnar on T1 at full length is excluded for w1 ≤ 15 and w2 ≤ 17 (`21`: Lasry's climb at 50 M
  evaluations). The wall is w2 ≥ 18, or w1 ≥ 16 with w2 ≥ 16, where the IDP's basin is 2–4 swaps. **Next: Greg
  sends or drops the Bochsler letter; overnight w2 16–17 on trimmed T1 bodies; a dossier-built K2 key list.**
- **[papal-ciphers-vatican-challenges](puzzles/papal-ciphers-vatican-challenges/NEXT.md)**: opened 2026-10-16 on
  Barb.lat.6960 (Pallotto, Vienna 1629, free on DigiVatLib, 28 letters "non-decrypted" in DECODE). The 1628 key
  probably reads it (one line, one reader), and Kiewning 1897 prints the Rome decipherment of the letter tested. Next:
  map all 28 letters to Kiewning's "dechiffr." entries (H2); any letter without one is the only possible unread content.
- **[vargas-mexia-es132](puzzles/vargas-mexia-es132/NEXT.md)**: BnF Espagnol 132, Philip II and Antonio Pérez
  to Vargas Mexía, 1577–80 (TK-007). Essay updated 2026-10-16: Pérez's late-April French channel at the center;
  Lalaing, fleets/Bordeaux/Ayala, Walloon terms and the Lansac leak preserved. Exp 09 inventory corrected to twelve
  distinct letters (fourteen sectional comparisons), with no earlier decipherment found in the recorded search.
  F. 34 provenance resolved; exact quotation still credited to cabinet-noir. New calibration and transcription
  limits stated. Narrative 4,462 words, specialist 1,478; 378 checked claim mappings, 47 quote entries, 32 notes.
  **Next: Greg's full-draft review, then page/document choice under `PROMPT-essay.md`.** No essay publication.
  OVERVIEW v7 remains published. H17 judged; H18 Longlée open; H19 supported by one letter, whose French ambassador
  says he had no commission. Walls: paleography, Vargas's original dispatches and f. 213 show-through. Research queue
  and evidence cautions are in the puzzle handoff.
- **[viete-f539](puzzles/viete-f539/NEXT.md)** — Joyeuse to Villars, 1594 (catalog
  `viete-undeciphered-ciphertexts`). Opened 2026-10-01 and stopped at a named wall. Two blind
  transcriptions give 344 sign tokens over ~145 signs. The matched annealing control fails
  (0.093 vs 0.986 positive); the target was not run. Breach: more same-key text (Villars's
  cipher letter to Joyeuse; Aubery 1654; DECODE R2281, which needs Greg's login) or known values.
  2026-10-03: seeded-value controls also fail (50 known signs or an 80-letter crib still leave
  ~50% wrong), so no crib breaks it. Only a key sheet or more same-key text will.
- **[book-of-abramelin-squares](puzzles/book-of-abramelin-squares/NEXT.md)** —
  TK-005. Blind test passed 2026-09-26: frozen Mathers predictions scored once
  on 119 squares of Dresden N 111 Book IV (223 grids, pages 246–272, two
  isolated Opus readers). Symmetry 0.88, checkerboard class 0.85, best letter
  0.25; recipe holds, every forecast inside its interval, independently
  recomputed. No seed-closed types (exp 23), no square palette (exp 24).
  Next: paper scope and venue, a second reader family, the Kollatsch novelty
  check with a login.

## Pick up next
1. **Second pass on the top 30 by attackable** (TK-002). Raise every `low`,
   and challenge every `compute = 5`. Specific facts the sweep flagged as
   most in need of checking:
   - Gospel of Thomas: does P.Oxy. 654 preserve the Greek of logion 7? If so, `material` and `verifiable` rise.
   - Bellaso 1555 set: Wikipedia says "purportedly solved" (Biermann 2018). Confirm or move status to `partial`.
   - Feynman ciphers: Vierra's 2023 solutions rest on blog sources; get a second confirmation.
   - Liber Loagaeth: two irreconcilable table counts (98 × 49×49 vs 96 grids); settle before any statistics.
   - Abramelin: active manuscript collation; follow its handoff. Source/score review updated 2026-09-26.
   - Rök: no published response to Holmberg et al. 2020 was found; check Futhark 11–15, ANF, Scripta Islandica.
   - Solomon and Saturn: check the rune-letter scheme against Anlezark 2009; if explained there, lower `compute` and `crowding`.
   - Sola Busca: card legends unverified against a facsimile; `crowding 4` rests on absence of evidence.
2. **Write `rubric/CALIBRATION.md`** (TK-003). Observations already in hand:
   - `attackable` is additive, so hoax/noise cases with high `compute` (Oera Linda, Baconian ciphers) outrank real puzzles. They are now shown separately, but the composite should probably gate on `solvable` (multiply, or weight it 2). Decide and change `scripts/rank.py`.
   - Chaocipher and Kryptos K4 both fell to a document, not to analysis. `compute` must ask whether the hypothesis space is enumerable, not only whether data is ready and a check exists. Berg's Lyric Suite is the musical twin.
   - Man'yōshū poem 9: `material 2` vs `compute 5`. A tiny target with a huge supporting corpus may be undercounted.
   - Mene mene tekel: a solved humanistic puzzle scores only `verifiable 3`; low `verifiable` is not evidence of unsolvability.
   - Golden Dawn cipher manuscripts: `solvable 5` with `status partial` is the rubric behaving correctly.
3. **Candidates the sweep could not verify but rated stronger than several it wrote.** Each needs a session with search budget:
   - Getty Hexameters / Ephesia Grammata (Faraone & Obbink 2013). Best unfilled slot in antiquity.
   - Silk dress cryptogram (solved 2022 by codebook identification): promote from EXCLUDED to a calibration entry.
   - Dresden Codex Serpent Series and the 819-day count: pure arithmetic, digitized, real unresolved scholarship.
   - Qumran Cryptic B and C scripts: if genuinely undeciphered, a determinate-Hebrew cipher with a digitized corpus.
   - Debosnys cipher (1882) and the Scorpion ciphers: uncrowded, digitized.
   - Geheime Figuren der Rosenkreuzer (1785–88): unknown compiler, fully digitized, near-zero scholarship.
   - Picatrix: 200+ unidentified sources make a mass source-parallel sweep; re-admit as `attribution` if wanted.
   - Tabula Cortonensis and Cippus Perusinus as separate Etruscan entries.
   - Birhatiya oath in the Būnī corpus.
4. **Cut to 50.** Greg decides; the index proposes. Removed by Maya without
   asking: the Elena Ferrante entry (living subject, stated wish for
   anonymity). Row in EXCLUDED.md; reversible.
5. **First deep dive opened** (TK-004): Greg selected Abramelin. Continue through
   TK-005 and the puzzle handoff. Soyga remains a methodological analogy; a
   comparable generation rule and independent total verifier have not been found.

## Pooled compute thread
`ideas/pooled-compute.md` argues for verifier-first pooled search and says the
`compute` axis should split into a readiness component. `rubric/COMPUTE-MODES.md`
classifies every live entry by compute mode and brute-force fit (11 HIGH of 89).
Fold both into TK-003 (calibration) and use the HIGH list when choosing the first
deep dive (TK-004): D'Agapeyeff or Abramelin as the pooling test case.

## Vocabulary friction noted by agents
- The Old English elegies fit no `kind` cleanly (`riddle` for Wulf, `allegory`
  for the Wife's Lament). Consider adding `elegy` or `poem` to the vocabulary
  in `scripts/catalog_lib.py`.
