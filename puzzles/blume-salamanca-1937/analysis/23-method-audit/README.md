# 23-method-audit — what the negative searches establish, and what the CPU can do

2026-10-18. Research audit requested by Greg. No new target search. No new cipher family proposed as a finding.

## Verdict

Transposition remains the best working hypothesis. The IDP attack is a published, relevant method, and our
controls show that its tested regions are practical on this CPU. Continuing to widen an unaided search into
longer keys has a weak case. The remaining uncertainty includes the system, the text preparation, and the
search's ability to recover atypical plaintext. It is not just the number of CPU cores.

The most useful next effort is evidence acquisition, with a small historical-text calibration before another
long target campaign. This audit did not start a new search campaign.

## Question and method

Read the puzzle's canon, hypotheses, handoff, prior-work survey, experiment 12's classifier and generators,
experiment 21's C search and controls, and experiment 22's checked-in logs. Re-read Lasry's thesis chapter 9
from the locally cached source PDF text. Check the public prior work and CrypTool's implementation online.

`audit.py` reads only checked-in JSONL from 21/22. It checks that each target body contains all 28 intended width
pairs and the full evaluation budget, then totals process CPU time and reports the recorded controls. It also
computes factorial key counts and exact all-success binomial bounds. No probabilities of the real system are
computed. No new plaintext is generated.

Run from the repository root:

```
python3 -I puzzles/blume-salamanca-1937/analysis/23-method-audit/audit.py > puzzles/blume-salamanca-1937/analysis/23-method-audit/result.txt
```

The existing engine check was rerun from `01-solver`: `python3 -I test_engine.py`. C decryption matched the
independent Python encryption reference on 300/300 random cases, including incomplete rectangles and CC/CR.
This checks the original engine's transformation mechanics, not all of 21's search logic or historical fit.

## CPU feasibility

Numbers below are recomputed in `result.txt`, rather than inferred from elapsed run times.

| existing target sweep | pairs, 50 M IDP evaluations each | process CPU hours |
|---|---|---|
| Full T1 | 28 | 4.865 |
| T1[0:595] | 28 | 7.196 |
| T1[5:615] | 28 | 6.798 |
| T1[10:615] | 28 | 7.419 |
| Total, experiments 21 and 22 only | 112 | 26.278 |

At w1 12–15 and w2 16–17 a 50 M run took 9.85–43.67 CPU minutes (median 29.40). Parallel workers can shorten
elapsed time subject to core availability. These are historical run costs, not a benchmark for another width.

For the second key alone, 20! = 2,432,902,008,176,640,000 permutations. Even an illustrative 1,000,000 complete
key evaluations per second takes 77,094 years to enumerate them, before varying the first width, body length,
or system. That rate is deliberately illustrative, not measured. IDP evaluations in a local search are not
coverage of all permutations. Cryptanalysis must exploit structure rather than enumerate the whole space.

Experiment 21 already measured the relevant difficulty: its climbs usually recover the second key only from
within 2–4 swaps. Additional cores buy more attempts. They do not widen that measured region of useful guidance.
The swap-ball counts in 21 explain why longer keys hurt, but are not a runtime law: the actual search uses segment
moves and biased initial selection, not independent uniform sampling from a swap ball. Neither those counts nor
the sparse longer-key pilots establish a reliable completion budget. The previous 70–200 M estimate is a pilot
extrapolation that still needs controls.

## What the method gets right

- Independent plant and solver seeds in the current controls; matched lengths, budgets, and explicit recovery rules.
- Actual recovery on plants rather than confidence based on a high language score alone. 21 recovered 20/20;
  22 recovered 29/30. Targets produced no candidates above the registered threshold.
- Measurement of the score near and far from the true key, plus comparisons with the published implementation.
- Correction of the seed leak in 05 and of the offset-selection artifact in 18. The current handoff records both.

Those results are useful negative evidence for ordinary plaintext encrypted exactly as the tested models specify.
The failures do not show that the cipher is impossible or that the CPU is incapable of classical cryptanalysis.

## Where the conclusions exceed the tests

1. **"Excluded" is conditional empirical shorthand.** A probabilistic solver with an 80% pass rule is not an
   exhaustive proof. The corner controls sample a few keys and texts, not every pair and key. Even an iid 10/10
   sample has an exact two-sided 95% lower success bound of 0.6915 on that plant distribution. That is not a
   probability that the target was missed. The full-length 20/20 pools a broad draw with a harder-corner draw;
   it does not establish uniform sensitivity throughout the band. Keep the negative results and their limits.

2. **The plaintext controls are proxies.** `01-solver/plaintext.py` alters held-out novels: it drops articles and
   QUE, inserts PUNTO, and adds spelled quantities. Book separation prevents direct training-text leakage, but
   this remains literary material tested against a literary language model. It is not an independent corpus of
   1930s trade telegrams. The sourced 1937 example in `sources/conventions-survey.md` uses STOP. The controls
   do not establish sensitivity to the target's combination of names, abbreviations, commercial vocabulary,
   multilingual fragments, code words, or nulls inserted before transposition. Trimming the ciphertext's ends
   does not test nulls inserted into the plaintext before encryption.

3. **Experiment 12 ranks simulated generators, not every historical cipher.** Its diagonal Gaussian uses related
   statistics, so its log-score gaps are not calibrated odds for historical hypotheses. Its homophonic model
   uses just 26 outputs with random borrowing; its nomenclator is a random substitution with random short word
   groups; its codebooks have uniform or alternating C/V artificial groups. Other codebooks, restricted keys,
   and substitution-plus-transposition were not covered. The evidence still strongly favors a natural-letter
   transposition over the ordinary alternatives tested. "Every other cipher type refuted" exceeds that evidence.
   Literal ADFGX/ADFGVX is directly incompatible with the observed alphabet; that narrow exclusion is stronger.

4. **Same letter source does not establish same system or key.** Experiment 11's p = 0.21 is a failure to detect
   different letter distributions. Distinct transpositions of the same language can have the same distribution.
   A shared system is a useful simplifying hypothesis, with the sender/date/destination as context. It is not
   established by this p-value. Joint attacks must keep the two messages' separate rectangle boundaries; simply
   concatenating the ciphertexts would change the assumed encryption.

5. **The historical prior remains unproved.** No source connects double columnar encryption to these senders.
   The long-key German instruction previously cited has already been withdrawn. The system is plausible and
   historically available; it is not identified. Werner's wool story is testimony, not a known plaintext. A
   convincing decryption could disprove that story. Context must validate a recovered reading rather than force it.

## What to investigate next, in order

1. **Acquire outside evidence.** Pursue Bochsler's note 44 and the reported 2020 attempt, using the existing
   unsent outreach draft. Inspect the actual note/report before treating its contents as known. Identify BLUME
   through registered telegraphic-address lists, Salamanca business directories, and receiving-office records.
   Search for replies, drafts, further Oswald traffic and a key instruction. These could identify the system,
   provide a key phrase, or supply a genuine plaintext passage. Sending outreach remains Greg's action.

2. **Calibrate on the kind of message we need to recover.** Freeze a small independently sourced set of period
   Spanish commercial/military telegrams and a clean baseline. Test the suspected cipher at both lengths, then
   vary one preparation rule at a time: STOP/X, abbreviations and names, nulls before transposition, and a few
   substitutions or an insertion/deletion in the transmitted copy. Measure both known-key language-score
   recognition and blind key recovery. That separates a poor scoring model from a poor search. The archive
   transcription is checked; errors made before these PTT copies are not ruled out. Do not invent edits to the
   target or random null locations until a control shows a way to test them.

3. **Make the next computational test depend on that result or new evidence.** A dossier-derived key list can
   be practical, but only as a bounded test with a planted list key and declared phrase/ranking conventions.
   Bourdeau already tried 6.6 M dictionary words/phrases: generic list enlargement is not new evidence. Phrase
   priors and a crib-driven attack are credible alternatives to random starts. A short likely word is a weak
   crib; a long externally supported passage is much stronger. Any new score, key prior, or budget must improve
   blind controls in the currently failing region before another target sweep. Preserve promising partial
   readings for independent checks, with shuffled controls for word spotting; do not count fragments as solutions.

If these leads produce nothing, pause at the stated wall: unidentified system/preparation and inadequate
demonstrated recovery for long keys. Do not default to ever-longer keys merely because shorter searches failed.

## Sources and limits

- **Repository evidence:** `01-solver/plaintext.py`, `12-type-diagnostics/{README.md,diagnose.py,result.txt}`,
  `21-dc-method/{README.md,dcm.c,results/}`, `22-dc-trimmed/results/`, and the existing `sources/` surveys.
  Audit arithmetic is `audit.py` → `result.txt`. The recommendations above are our interpretation.
- **SCHOLARLY:** Lasry, *A Methodology for the Cryptanalysis of Classical Ciphers with Search Metaheuristics*,
  2018, chapter 9, especially 9.4.6.1–2,
  https://kobra.uni-kassel.de/handle/123456789/15274 . Read from the PDF/text already cached by experiment 21 in
  `21-dc-method/out/thesis/`; the handle and alternate PDF hosts did not reopen through web fetch today.
  The challenge's first solution combined partial-output word spotting, source-book identification, and a
  known-plaintext attack. It was not a demonstration of guaranteed blind convergence on any 600-letter text.
- **PRIMARY for implementation:** Lasry and Krauß, CrypTool 2 IDP analyser,
  https://github.com/CrypToolProject/CrypTool-2/blob/main/CrypPlugins/IDPAttack/IDPAnalyser.cs (fetched today).
  **PRIMARY project report:** https://www.cryptool.org/en/posts/solving-double-column-challenge/ (fetched today).
- **CLAIMANT:** Bourdeau's own logs/notes,
  https://github.com/dbourdeau/cyphersolver/blob/main/targets/blume/NOTES.md (fetched today). The web raw view
  returned an older state; use our dated captured survey for the later scope, not that view as a current ledger.

A targeted web search found no replacement method demonstrated on this exact problem and no newly accessible
2020 report. This is a search limit, not evidence that neither exists.
