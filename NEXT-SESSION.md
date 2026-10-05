# NEXT-SESSION — what is in flight

**Last updated:** 2026-10-04 (es. 132 session 4: the pre-murder letters read; H16 judged)

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
- **[vargas-mexia-es132](puzzles/vargas-mexia-es132/NEXT.md)**: BnF Espagnol 132, Philip II and
  Antonio Pérez to Vargas Mexía, 1577–80 (TK-007). Opened 2026-10-03. Tomokiyo's Cipher 4 key
  reads Pérez's letter of 15 April 1579 (provisional v1: Escovedo's suit, the King's refusal of
  leave, the Archbishop of Toledo and the Princess of Éboli). Two held-out letters confirm the key.
  2026-10-04 (session 3): both ciphers read. Cipher 4 v2 (two readers reconciled, five letters) plus held-out
  f. 154 (the King's secret inquiry into Guise's cipher with Don John and "800 mill ducados"); 2H, Σ, H and
  cross-doubling established. Cipher 3 guide v2.1 works (ff. 103/113, 105, 165/167 read; codes u., 108, 149, T).
  Overview published: https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2. Wall: transcription quality (Sonnet
  readers). Next: human paleographer review, second reader for f. 154, Simancas K 1550–55 by hand, the other
  Cipher 3 letters.
  2026-10-04 (session 4, exp 06): every letter of 16 Dec 1577 – 17 Mar 1578 read blind (Ciphers 1–3). No Don John–Guise
  league before the murder (H16a refuted), but a 24 Jan 1578 report of the Guises' dealings with Don John's envoy Sotomayor
  that the King took seriously (H16b weakened; Mignet missed it). Next: date Mignet's B.44 n° 89 via Simancas.
  2026-10-05 (session 5, exp 07, H17): every royal letter of 24 Aug 1579 – May 1580 read blind (two witnesses each). None
  names Pérez, Éboli or Escobedo; the countersignature passes from Pérez (to 13 Jul) to none (24 Aug) to Idiáquez (from 13 Sep);
  Vargas's letters go "a mis manos, como a las de Çayas"; two unnamed leak hunts (13 Sep, 29 Nov 1579). 28 Mar 1580 decode
  matches Teulet's printed minute. Next: republish the OVERVIEW, f. 273, Vargas's side in AGS Estado K 1553–1555.
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
