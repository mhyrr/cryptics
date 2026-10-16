# Session prompt: open the BLUME SALAMANCA dive (Zurich → Salamanca, 8 January 1937)

Paste everything below the line into a fresh session, from the repo root `/Users/mhyrr/work/cryptics`.
When step 1 creates `puzzles/blume-salamanca-1937/`, move this file there as `PROMPT-open.md`.

---

/focus blume-salamanca-1937 — open the dive and run the first key search

**Goal.** Recover the transposition key of the two telegrams sent from Zurich to "Blume, Salamanca" on 8 January 1937,
or rule out a stated family of ciphers with controls that prove the search could have found it. Both outcomes are
results. This is a real key search: no key survives, and no reading exists.

**Catalog entry.** The telegrams are member 3 of `catalog/entries/early-20th-century-coded-telegrams.md`. The dive slug
differs from the entry slug, as `viete-f539` does from `viete-undeciphered-ciphertexts`. Copy the Zurich criteria from
"What a solution would have to do" into `README.md` and sharpen them into numbered tests.

## What we know (from the catalog entry; verify before relying on it)
- Telegram 1: 123 five-letter groups, 615 letters. Telegram 2: 32 groups, 160 letters.
- Bourdeau and Richard Bean transcribed both independently and agree letter for letter (SHA-256 published).
  An open issue says the common transcription is wrong in three places:
  https://github.com/dbourdeau/cyphersolver/issues/14
- IC ≈ 0.070, and there is no k, w or x. So the letters are probably plaintext letters in a new order. Spanish is
  Bourdeau's inference from statistics. It is not established. Italian and Portuguese also fit "no k, w, x".
- Prior exclusions (Bourdeau, Sept 2026, with planted controls): every single transposition, and every double columnar
  transposition whose second key has ten letters or fewer. Tomokiyo (2023) ruled out the British Government Telegraph
  Code. Open: double columnar with two long keys. As of 30 Sept 2026 Bourdeau was running a joint attack on both
  telegrams.
- Method reference: Lasry, Kopal and Wacker broke a published double-transposition challenge with long keys by
  divide-and-conquer hill-climbing (*Cryptologia*, 2014). Nobody has reported running it on these telegrams.
- Context: Regula Bochsler found the telegrams in Swiss Federal Police files on Werner Oswald, founder of the Emser Werke
  (*Nylon und Napalm*, 2022). Oswald told the police they concerned the wool business. Salamanca was Franco's
  headquarters in January 1937.

## Step 0: is it still open? (main thread, before anything else)
Read Bourdeau's notes (`https://github.com/dbourdeau/cyphersolver/tree/main/targets/blume/`), his recent commits, the
issue above, and `https://github.com/jfuentesibanez/sentinel-blume-salamanca`. Also run one web search for a claimed
solution after 30 Sept 2026.
- **If someone has a solution:** this session becomes an independent check of it. Re-decrypt with their key from our own
  transcription, test it against the criteria, and stop.
- **If not:** write down exactly which parameter space Bourdeau excluded, and how. Our search starts where his stops. We
  do not repeat his exclusions, except as a solver control.

Contacting Bourdeau or anyone else is an external action. Ask Greg first.

## Step 1: open the dive
Follow `/focus` for a new dive: copy the template, fill `README.md`, seed `canon.md` and `hypotheses.md` from the entry
and from Step 0, add the dive to `NEXT-SESSION.md`, and create a HIVE ticket.

## Step 2: fan out (subagents on Opus; no agent spawns agents; at most four at once)
AGENTS.md "Subagents" applies. Every dispatch prompt points at `AGENTS.md`, `rubric/RUBRIC.md` and the dive's
`README.md`. It does not re-brief. Run these two in parallel while the main thread starts Step 3.

**A. Sources and transcription.** Pull both transcriptions and the two telegram images (Schmeh's Facebook post; the
time-limited image URL may be dead, so record that). Settle the three disputed letters against the images, and record
each reading with its evidence. Write `sources/telegram-1.txt`, `sources/telegram-2.txt` (groups as sent) and
`sources/PROVENANCE.md` with a SHA-256 for each file. Also record the telegram headers: date, time, word count, office
marks and routing. The word counts check our letter counts.

**B. Context and cribs.** Find what the period offers as probable words and conventions:
- How 1937 commercial and Nationalist cipher telegrams were written: spelled-out numbers, "STOP"/"PUNTO", nulls,
  padding to five-letter groups, X as a separator.
- Which transposition systems the Spanish Nationalists, the Condor Legion's suppliers and Swiss trading firms are
  documented to have used in 1936–37. Sources only, tiered (AGENTS.md rule 1).
- Probable words with reasons: LANA, KILOS, PESETAS, FRANCOS, SALAMANCA, ZURICH, place and firm names linked to Oswald,
  and the Nationalist procurement agents of the time.
- Who "Blume" may be: a person, a cover address, or a firm.
Output `sources/context-cribs.md`. Every crib carries a source and a reason. A crib without one is a guess, and the
solver must not use it.

## Step 3: the solver and its controls (main thread; this is the verifier, so it stays here)
Build in `analysis/01-solver/`. Use the standard library first, and add a `uv` environment only if it is needed (say why
in the README). Measure the speed of Python first. If the search needs it, write the inner loop in C or Rust, and keep
the Python driver.

1. **Language model.** Build letter n-gram tables (4-grams or 5-grams) from Spanish prose of the 1920s–30s, written in
   telegraph style: uppercase, no spaces or accents, numbers spelled out. Build a second model for Italian and a third
   for Portuguese. Record the corpus sources.
2. **Double columnar engine.** Support complete and incomplete columns, and both read-out conventions. Test it against
   hand-worked examples.
3. **Divide-and-conquer search.** Read the Lasry–Kopal–Wacker 2014 paper before you write the search. Do not rebuild it
   from memory. Implement its two phases, or state where the design differs and why.
4. **Matched control (the Viète lesson).** Generate 615 letters of period-style Spanish plaintext. Encrypt it with random
   double columnar keys whose lengths are in the range still open after Step 0 (for example, 11–25 for each key). Run
   the solver exactly as it will run on the target: same time budget, same restarts.
   Report the recovery rate for each key-length band. Also run the control at 160 letters, and run it jointly at 615 +
   160 letters with shared keys.
   **No target run happens before the control passes.** Agree a pass threshold with yourself and record it in the README
   before the run (for example, at least 80% full recovery in a band). A band that fails its control is not searched; it
   is recorded as "not testable with this method".
5. **Score threshold.** Use the controls to set the score that a correct decryption reaches and a wrong one does not.
   Record it before the target run.

## Step 4: target runs (fan out by hypothesis, one subagent each)
After the control passes, dispatch one Opus subagent per hypothesis, each in its own `analysis/NN-name/` folder, using
the shared engine. Each agent runs its own planted control first, then the target. Each writes a README with the frozen
parameters, the control result, the target result and a checked-in log.
- **H1:** double columnar, both keys long, Spanish, telegram 1 alone.
- **H2:** the same keys on both telegrams (joint attack). This has more constraint per key.
- **H3:** language is not Spanish (Italian and Portuguese models). Run it only if H1's control passes and H1's target
  fails.
- **H4:** a different transposition family that Bourdeau did not cover. Choose from Step 0 and agent B's evidence
  (disrupted columnar, Nihilist, route, or nulls inserted before transposition). One family per agent. Do not run a
  family that has no documented use in 1937.

Long runs go in the background. Set a compute budget per hypothesis before the run, and stop at it.

## How a hit is judged (main thread)
- A hit must turn all 615 letters into continuous text in one language, with no unexplained residue. Then it must read
  telegram 2 with the same keys, or with keys it explains. README criteria apply in full.
- Confirm it with a separate re-decrypt script that does not share code with the solver.
- A fragment of fluent text is not a hit. The annealer makes fluent fragments from noise. Bourdeau's control on the
  Garbino code shows this.
- Record the plaintext with an English translation beside it (Greg does not read Spanish). Check the content against
  Oswald's documented business and Nationalist procurement in 1937.
- Do not publish, post or contact anyone about a hit. Tell Greg.

## How a miss is judged
If the controls pass and the target fails, that is a result: "double columnar with keys of lengths X–Y is excluded for
telegram 1, at a control recovery rate of Z%". Write it in `hypotheses.md` and `research.md`. Name the next family, or
name the wall in `NEXT.md` (AGENTS.md rule 8). Do not widen the search without a reason recorded first.

## Rules that bite here
- LLMs interpret, code computes. Every rate, score and exclusion comes from a script with checked-in output.
- Findings land in the right file as they happen (`canon.md` / `research.md` / `hypotheses.md`).
- Stage files by name. Commit in small steps: transcription, solver, controls, and each hypothesis run.
- End with `/session-close`.
