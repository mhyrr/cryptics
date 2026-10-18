# Key-type ranking after diagnosis (stage 2 of `PROMPT-diagnose.md`)

**Audit caveat, 2026-10-18:** this is the historical session-5 ranking. `analysis/23-method-audit` narrows its
claims: experiment 12 ranks its simulated generators, not every historical system; a shared system is unproved;
negative key searches are conditional. The current action priorities are in `NEXT.md`.

Written 2026-10-17 from experiments `09`–`13`, the corrected `08`, and `sources/conventions-survey.md`. Ranked by
evidence first, then by fit to the user: a Swiss engineer's bureau in Zurich in 1937, writing to Nationalist Spain
(`key-type-survey.md`). Each candidate states the prediction that separates it from the others. Stage 3 tests the
top three (`14`, `15`, `16`).

## What the diagnosis fixed
- **The family.** The letters are a natural-letter text in a new order (`12`). Every substitution, fractionation,
  homophonic, nomenclator and codebook type is excluded (H12). So the open question is which transposition, and
  what the plaintext holds besides plain Spanish.
- **One system.** T1 and T2 fit one letter source and one language ranking (`11`), and the charges do not split
  them (survey §4). A candidate that needs two systems starts behind.
- **Two plaintext constraints, not key types.** T1 holds X and P beyond Spanish (X 6 vs 1; P 35 vs 16 without a
  P-bearing stop word), and T2 holds F (7 vs 1). Neither position nor any sourced convention explains them (`09`,
  `10`). Every attack plants text with these in it: X as an occasional stop (German army practice by 1930) or as
  nulls.
- **Two anomalies, both suggestive.** T1's last 20 letters are rare-letter rich (p = 0.019, location-corrected;
  `09`). The shared strings are in excess at family-wise p = 0.008–0.052 (`13`). Neither is established; either
  one would rank the candidates differently if it became so.

## Candidates

| rank | candidate | fits | fails or strains | fit to the user | separating prediction | test |
|---|---|---|---|---|---|---|
| 1 | **K1: double columnar, whole text, long keys** (w1 or w2 ≥ 16; the residual of H1/H2) | `12` (transposition family; T1 inside the with-nulls band); `11` (one system, no group structure) | Both anomalies are chance under K1: the end cluster (1.8–3.1% of plants reach it) and the shared strings (family-wise 0.008–0.052) | Good. Double transposition was the German army's WWI field cipher (Übchi) and is in Givierge (1925, "retranspositions"); a German-Swiss engineer could know it. No source ties it to the Oswalds | Ciphertext neighbours are plaintext letters about w1·w2 apart, so vowel/consonant class has no short-lag structure, segments do not differ in vowel density, and the two telegrams' bigram profiles overlap only at chance. `13` found such an overlap after looking (p = 0.0013) | `14` |
| 2 | **K2: a transposed body plus untransposed letters at an end** (indicator, reference, or nulls added after transposition; H6) | `09` (end cluster, p = 0.019; T1's ends-only 0.0001, post hoc); `13` E4 (REF in both final groups, post hoc) | Survey: indicators went at the head, and no final-group or REF convention was found. T2's end is not unusual (p = 0.32). Fillers after transposition would sit consecutively at the very end; T1's X's are at 596, 609, 614 | Plausible for a commercial user who adds a reference or check group, but unsourced | K2 has teeth only if a few untransposed letters break the full-length searches that excluded the cheap families. If they do, those exclusions are void for bodies shorter than 615 or 160, and the cheap families come back | `15` |
| 3 | **K3: one single-stage columnar transposition, one key on both telegrams, a shared phrase, bodies shorter than 615/160** (H7) | `07`: the only modelled mechanism for the shared strings; `09` via K2 | Single columnar is excluded at full length (Bourdeau, to w 45). A shared phrase under single columnar gives about one shared run per column, so seven runs suggest a narrow table | Good. Single columnar is "the standard kind" in Givierge and Langie, the handbooks a Swiss reader could buy | The seven shared runs fit one column geometry (one width, body offsets, a common column order) beyond chance | `16` |
| 4 | **Jargon code under transposition** (H10) | `12`: letter-identical to plain Spanish | — | Plausible for commercial secrecy | None from letter statistics. A decryption would read as Spanish words with odd sense | — |
| 5 | **Turning grille of side 9 (or 3) on T2** (H11) | `12` length: 160 = 2 × 80 = 20 × 8 | `11` finds one system, and no complete grille fits T1 | In Langie (Lausanne) and Givierge | T2 reads under a 9 × 9 grille key | not this session |
| 6 | **Disrupted columnar, Myszkowski, Nihilist read by columns, sets offset by a preamble** (open in H4) | `12` (transposition family) | `07`: Nihilist by columns does not produce the shared strings. No period source for disrupted columnar | No source ties any to 1937 | None that separates them from K1 at this length | not this session |
| — | **Non-transposition types** (H12) | — | `12`: all outside their bands by 40–1,137 log units; `11` C4 | — | — | **refuted** |

## Why this order
K1 ranks first because nothing measured contradicts it beyond the "suggestive" level, and it fits a German-speaking
user. But it cannot be attacked at 615 letters (the named wall), so its ranking says where the truth most likely is,
not where the work goes. K2 and K3 rank lower on evidence but are cheap to test, and each would explain one of the
anomalies. K3 depends on K2: without untransposed ends, single columnar stays excluded. Candidates 4–6 have no
separating prediction we can test from the ciphertext this session.

## What each stage-3 result would do
- `14` refutes K1 (for that telegram) if T1 or T2 shows class-contact or vowel-density structure that long-key
  double columnar plants do not produce, provided the positive controls show power.
- `15` gives K2 teeth if the full-length searches lose most of their recovery when 5–20 untransposed letters sit at
  an end. Then stage 4 reruns the affected families on truncated bodies, each with its own control.
- `16` supports K3 if the shared runs fit one geometry beyond the null, with a control that recovers planted
  geometries. The geometry then fixes the width and the trims for a stage-4 attack, and the runs become a crib.
