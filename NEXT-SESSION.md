# NEXT-SESSION — what is in flight

**Last updated:** 2026-09-15 (bootstrap + first catalog sweep)

## State
Skeleton, rubric, templates, scripts, and slash commands exist. The first
catalog sweep landed **104 entries** (89 live, 15 calibration: solved, hoax,
noise) across six categories, plus ~30 rows in `catalog/EXCLUDED.md`.
`catalog/INDEX.md` is current. 27 entries carry `confidence = "low"`.

All first-sweep entries were verified by WebFetch only (the session's search
budget was exhausted before the agents started). Every entry says what it
could not verify under `## Unverified claims`. Treat scores as provisional.

## Active dives
None yet. Open one with `/focus <slug>`.

## Pick up next
1. **Second pass on the top 30 by attackable** (TK-002). Raise every `low`,
   and challenge every `compute = 5`. Specific facts the sweep flagged as
   most in need of checking:
   - Gospel of Thomas: does P.Oxy. 654 preserve the Greek of logion 7? If so, `material` and `verifiable` rise.
   - Bellaso 1555 set: Wikipedia says "purportedly solved" (Biermann 2018). Confirm or move status to `partial`.
   - Feynman ciphers: Vierra's 2023 solutions rest on blog sources; get a second confirmation.
   - Liber Loagaeth: two irreconcilable table counts (98 × 49×49 vs 96 grids); settle before any statistics.
   - Abramelin squares: total count and blanks per witness are unknown; both `material` and `compute` depend on it.
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
5. **Pick the first deep dive** (TK-004). Where the index points, with the
   sweep's own recommendations: Book of Abramelin squares (the Soyga
   analogue: six divergent witnesses, no collation, an internal check),
   Clavis Artis (three volumes of readable German, zero transcriptions,
   HTR-ready), Hisperica Famina (a glossary-parallel sweep nobody has
   quantified), Atalanta Fugiens, Book of Soyga, Hackness Cross (needs
   imaging first). Voynich is #3 but `crowding 1`.

## Vocabulary friction noted by agents
- The Old English elegies fit no `kind` cleanly (`riddle` for Wulf, `allegory`
  for the Wife's Lament). Consider adding `elegy` or `poem` to the vocabulary
  in `scripts/catalog_lib.py`.
