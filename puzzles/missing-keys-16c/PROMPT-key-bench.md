# Prompt: get the key right on the no. 2911 bench

Run this in a fresh session in `/Users/mhyrr/work/cryptics`. It follows `PROMPT-key-line.md` (the pilot) and
replaces its Phase 2 for now.

## Goal

Rebuild the key of no. 2911 from its pair, blind, with a script that passes the bar already written in
`items/2911/bench/README.md` (the H6 bar). Then read the two bare letters with that key. No. 2911 has a known
answer, so this is a test of our method, not a new key. The method is the product: a key builder that works on a
syllable cipher whose plain side is an abridgement.

Out of scope, by Greg's decision (2026-11-17): finding key sheets. No DECODE, no archive search, no login. We
rebuild keys from pairs. Do not start another item.

## Read first, in this order

1. `AGENTS.md` (repository rules).
2. `puzzles/missing-keys-16c/items/2911/bench/README.md`: what is frozen, the commands, the score, the bar, the
   sealing rules, results so far.
3. `puzzles/missing-keys-16c/items/2911/README.md`, section "After the failure".
4. `puzzles/missing-keys-16c/research.md`: the 2026-11-17 entry only. `hypotheses.md`: H6 and H7.
5. `line/align.py` and `bench/variants/v1_gap.py`, `v2_boot.py`, `vx_oracle.py`. These are the code you extend.

Do not read `NEXT.md` for the bench; it predates it. Rewrite it at the end.

## State

- All reading is done. No reader agent runs in this session. Inputs are frozen in `bench/inputs/`.
- One trial is one command: `python3 run.py <variant> [p1|full]`, 15–60 seconds on `p1`. It writes a table to
  `bench/runs/` and one row to `bench/runs/results.tsv`.
- Five variants have run. None passes. The pilot aligner and the gap variants collapse to "every sign is null".
- The diagnostic `vx_oracle` starts the passes from the true table and holds it: precision 0.96, recall 0.60,
  31 of 32 marked rows right. So the model and the pair are sound. The open problem is the start.
- Two causes are known. Signs occur 10–30 times each, too few to stand out in a wide search window. And the
  likelihood barely prefers the true table: gaps are cheap, and a right value that meets a different spelling
  costs as much as a wrong one.
- The cipher is about half syllable signs (consonant plus vowel) and nulls are 0.2% of places. The plain side
  leaves out 42% of the cipher, in 20 stretches.

## Sealing

`items/2911/outside/` and `cache/keysheets/` hold the answer. `score.py` and `vx_oracle.py` may read them. You
may not open them, print them, or let a builder variant import them. A builder sees only its cipher file and its
plain file. `results.tsv` holds no values. If you need to know why a variant fails, write a script that reports
counts, never values. Do not paste sign values into chat.

`p1` is the development set. `full` and the two bare letters are the test. Do not tune on `full`.

## The work, in this order

Each trial is one new file in `bench/variants/`. Before you run it, add a short entry to the bench README: what
the variant changes, what you expect, and what result would count against it. After the run, add the result row
and one sentence on what it showed. Commit the variant and its README entry together.

The order comes from how people rebuild keys from a deciphered letter (Charles V 1547: Pierrot, Desenclos,
Gaudry, Zimmermann, HistoCrypt 2023) and from Lasry's solvers.

1. **Homophone groups from near-repeats.** Find runs of cipher signs that occur twice and differ at one place.
   The two signs at that place probably share a value. Build groups from the cipher text alone and report how
   many signs join a group and how often each group occurs. Then let the builder count evidence per group as
   well as per sign. Check the groups with `score.py`-style counts (share of grouped pairs that truly share a
   value), written to a file without values. A group rule that is wrong more than 1 time in 10 is dropped.
2. **Seed and extend.** Replace the global fit as the start. Take seeds that are certain from the two files
   alone: words written in clear inside the cipher (`[[...]]` units), and repeated cipher runs matched to
   repeated plain words by relative position. From the seeds, fix a few places. Decode with the partial table,
   match half-read words to the plain text near the expected position, lock those places, and repeat. Every lock
   needs a stated rule (for example: at least four letters fixed by signs already valued, one candidate word
   within the window). A sign gets a value only from locked places. Run the existing passes (`v1_gap` model)
   only after the table has a value for most frequent signs, as `vx_oracle` shows they hold a good start.
3. **Nulls near-absent.** A sign may be null only on direct evidence: a repeated run that occurs with and
   without it. Otherwise the empty emission is off.
4. **Layout test.** Check whether a syllable sign is a consonant shape plus a vowel mark in the transcription
   (`SIGN-GUIDE.md` describes shapes only). If yes, learn consonant and vowel separately. If the signs are
   unrelated shapes, record that and skip this step.
5. **Language score on unmatched text.** Decode the stretches the plain side leaves out and score them with
   `line/fluency.py` against `work/wordlist.txt`. Use the score to choose between candidate values for signs
   that the pair leaves `unknown`. Never use it to override a value the pair supports.
6. **Spelling tolerance.** A value that is right but meets a one-letter spelling difference should cost less
   than a wrong value. Add only if steps 1–3 leave precision under the bar.

Steps 1–3 are the main attempt. Do them even if an early one looks weak alone; they are meant to work together.

## Pass, and what follows

The bar is the H6 bar in the bench README. Do not change it. On `p1` and on `full` against the printed text:
precision ≥ 0.90, recall ≥ 0.60, marked rows wrong ≤ 10% with at most 2 `certain` wrong, null share ≤ 0.10.

When a variant passes on `p1`:
1. Run it on `full` once. Report the row whatever it says.
2. Decode `bench/inputs/bare-V134-1r.txt` and `bare-V125-5r.txt` with the built table. Score against the period
   decode in `outside/` by script. Report the share of signs valued and the share that agree. Give English
   beside any Italian you quote.
3. Port what worked into `line/align.py` (log-space pass, gap state, the seed step, a stop when the built null
   share exceeds 0.5). Rerun `analysis/02-calibration-synthetic` and `analysis/03-calibration-real`. Both must
   still pass their bars. Run `line/test_line.py`.
4. Update H6 and H7 in `hypotheses.md`, `canon.md`, and the ledger row for 2911.

## Stop rules

- Stop and write the wall if steps 1–3 are all built and `p1` precision is still under 0.5, or after eight
  variants without a pass. Say what the best variant gets right, what it gets wrong (counts by sign type and
  frequency band, no values), and what would breach it. A named wall is a finished result.
- One honest attempt per idea. Do not tune a constant more than three times on `p1`.
- Stop and ask Greg before: any message to Tomokiyo, Bourdeau, DECODE or an archive; reserving an item; anything
  that needs a login or costs money; starting another item.

## Discipline

- Key work runs on Fable on the main thread. No reader agents. An Opus agent may write a mechanical helper
  script; it may not open `outside/` and may not spawn agents.
- Every number you report comes from a checked-in script and a checked-in result file.
- Findings land as they happen: result → `research.md` (dated, newest first); what is now believed →
  `canon.md`; status → `hypotheses.md`.
- Python standard library only. Run tests from `line/`.
- Commit small, stage by file name, never amend after a failed hook. Do not push. Leave `AGENTS.md` alone; its
  modification predates this work.
- End of session: `/session-close`. Rewrite `NEXT.md` and `NEXT-SESSION.md` so they describe the bench.

## Report at the end

For Greg, in this order: did a variant pass; the row for `p1` and `full`; the bare-letter figures; which of the
six steps carried the result and which did nothing; what changed in `line/align.py` and whether both calibrations
still pass; what you would do on the next item.
