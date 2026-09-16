# NEXT-SESSION — what is in flight

**Last updated:** 2026-09-16 (Abramelin first deep dive)

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
- **[book-of-abramelin-squares](puzzles/book-of-abramelin-squares/NEXT.md)** —
  TK-005. First pass: 242 exported Mathers records, 232 analyzable; elementary
  generators fail; symmetry fills remain conditional. Wall: facsimile audit and
  uncorrected German targets. Kollatsch already has an edition, a 2024 symmetry
  study and a 2025 manuscript inventory. Catalog corrected: partial,
  compute 4, crowding 3. Read its NEXT.md first.

## Pick up next
1. **Second pass on the top 30 by attackable** (TK-002). Raise every `low`,
   and challenge every `compute = 5`. Specific facts the sweep flagged as
   most in need of checking:
   - Gospel of Thomas: does P.Oxy. 654 preserve the Greek of logion 7? If so, `material` and `verifiable` rise.
   - Bellaso 1555 set: Wikipedia says "purportedly solved" (Biermann 2018). Confirm or move status to `partial`.
   - Feynman ciphers: Vierra's 2023 solutions rest on blog sources; get a second confirmation.
   - Liber Loagaeth: two irreconcilable table counts (98 × 49×49 vs 96 grids); settle before any statistics.
   - Abramelin: first digital-Mathers count and structural pass now in the dive;
     per-witness counts still need facsimile collation. Do not reuse the original
     "no prior structural study" premise.
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
