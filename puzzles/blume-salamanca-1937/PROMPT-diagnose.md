# Session prompt: diagnose the BLUME SALAMANCA cipher from first principles

Paste everything below the line into a fresh session, from the repo root `/Users/mhyrr/work/cryptics`.

---

/focus blume-salamanca-1937 — diagnose the cipher type from the ciphertext, then attack only what survives

**Why this session exists.** Three sessions tested the families the prior work pointed at (Bourdeau's double
columnar, Bean's shared strings) and excluded every one we can test (`NEXT.md` table). We never asked the
ciphertext what it is. This session works as a cryptanalyst would on an unknown cipher of 1937: diagnose, rank,
validate, then attack. Its value is a fresh order of work, not a persona. Do not re-run anything canon lists as
excluded; take those exclusions as given and build on them.

**Read first:** `AGENTS.md`, then in this dive `NEXT.md`, `canon.md`, `hypotheses.md`, `analysis/README.md`, and
`analysis/08-letter-fit/README.md`. Search `research.md`, don't read it end to end. The texts are
`sources/telegram-1.txt` (615 letters) and `sources/telegram-2.txt` (160). Reuse the corpus, language model and
plaintext generator in `analysis/01-solver/` (`lm.py`, `plaintext.py`, `out/lm_*`). Python standard library;
`-I` on every run.

**The leads `08` left:**
- Spanish fits best (T1 p = 0.08, T2 p = 0.11) but not well. Italian is rejected for T1 (p = 0.004).
- T1 has **6 X's** where Spanish expects 1 (z +5.3), and U is low (16 vs 30).
- T2 has **7 F's** where Spanish expects 1 (z +4.6), and no X at all.
- The two telegrams share more 4–6-letter strings than chance (`02`, p ≈ 0.001), and no tested family explains it
  (`07`).
- Neither telegram has letter-pair structure of its own (`04`).

## Stage 1 — Diagnose (scripts only; one `analysis/NN-*/` folder per question)
Answer each from a script with its output checked in. Pre-register what each result would mean before running it.
1. **The odd letters.** Where are T1's X's and T2's F's? Look at their spacing and their positions modulo the
   factors of each length. Compare with what an X-as-stop convention, spelled digits, or nulls at fixed places
   would produce under a transposition. Build plaintext generators for each convention (X for PUNTO; digits by
   letter code; nulls) and refit `08` under each.
2. **One system or two?** Do T1 and T2 come from the same language, the same convention and the same system?
   Different odd letters (X against F) may mean different conventions.
3. **Cipher type.** Run the standard type diagnostics (the ACA statistics and their kin) against plants of each
   type at these lengths: transposition, fractionation (bifid / ADFGVX-like digraphs), a code or a jargon word list
   with natural-letter output, homophonic or nomenclator, and transposition with nulls. Is "plaintext letters in a
   new order" still the best reading? What do the lengths allow (615 = 3 · 5 · 41, 160 = 2⁵ · 5, 125 and 34 words
   on the forms)?
4. **The shared strings.** Recount them allowing reversed matches and gapped matches. Measure the chance level
   with a null that keeps each telegram's letter counts and the overlap of its own n-grams. Is p ≈ 0.001 robust,
   or an artefact of choosing n after looking?

## Stage 2 — Rank the key types
Write `sources/key-type-ranking.md`: each candidate type, the diagnostics it fits and fails, and its fit to the
user (a Swiss engineer's bureau in 1937; `sources/key-type-survey.md`). Rank by evidence, not plausibility alone.
Every candidate needs at least one prediction that separates it from the others.

## Stage 3 — Validate
For the top three, write a script that tests the separating prediction. Record each result in `research.md`, and
move hypotheses in `hypotheses.md` (new numbers from H6; never renumber). A candidate whose prediction fails is
refuted on the page.

## Stage 4 — Attack, step by step
For each survivor, write the attack as numbered steps in its analysis README before running anything: method,
planted control at the target's length, pass rule, score threshold, time budget. Run the control. Only if it
passes, run the target. A candidate reading must meet the criteria in the dive `README.md` (whole text reads;
telegram 2 decrypts under the same system; independent re-decrypt).

## Rules that bind this session
- LLMs interpret, code computes: no statistic from impression (AGENTS rule 6).
- Translate any Spanish, Italian or Portuguese you quote into English beside it.
- Subagents: Opus only, told not to spawn their own. Good fits are independent diagnostic scripts in stage 1.
  Judging what a result means stays on the main thread.
- Ask before anything external (email, posting, contacting authors). The Bochsler letter
  (`sources/outreach-bochsler.md`) is Greg's to send.
- Stop at a clean wall and name it. "Diagnosis says transposition of Spanish, every attackable form excluded" is a
  full result. So is "the X's are stops, and here is the constraint they put on the key".
- End with `/session-close`.
