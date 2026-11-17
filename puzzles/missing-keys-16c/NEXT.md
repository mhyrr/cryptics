# NEXT — handoff for the next session

**Last session:** 2026-11-16 to 2026-11-17 (ran `PROMPT-key-line.md`: phase 0 and a pilot)
**Where it stopped:** Tools built and calibrated. Four pilot candidates gated; none clean. Greg approved no. 2911
(Dieci to Machiavelli, 1510) as a known-answer test. Its held-out test failed: the aligner valued every common
sign as null. The outside check shows why: Machiavelli's decipherment is an abridgement (42% of the cipher has no
plain text) and the cipher is half syllable signs. The transcription is sound. No key was built; no bare letter read.

## Do first
1. **Greg reads the report** (`research.md`, 17 Nov entry) and the proposed changes at the end of `PIPELINE.md`.
   Phase 2 (batches) waits for his go.
2. **Make the aligner tolerate unmatched cipher (H6).** Write the bar first. Calibration cases: the 2911 pair
   (`items/2911/work/cipher-doubles.txt`, `work/plain-print.txt`, truth `items/2911/outside/truth.tsv`, by script
   only) and a synthetic pair with 40% of the plain text cut out in stretches. Port the log-space E-step from
   `items/2911/align_log.py` and add the degeneracy stop. The 2911 pair is spent as a held-out test; it is now a
   development case.
3. **If H6 passes on 2911:** send the four bare-letter readers (V/134, V/125; prompts and guide are frozen in
   `items/2911/`), read with the rebuilt key, and score the reading against the true key. V/134 (17 Aug 1510) is
   not in Opere VI (1877); check Bertelli 1964 and the Edizione Nazionale before calling it unread.
4. **No. 2345** (Baldovino del Monte): rerun `items/2345/fetch.py --probe` when the ASF host answers, then finish
   its gate. It is still the best candidate for a true missing key.
5. **Stage 4 bar (H7):** propose a bar that the true keys of 2911 and f. 255 pass and shuffled tables fail.
6. Terranova (H1–H5) is unchanged and waits on the Cg.12 table or DECODE R9318.

## Open questions
- Greg: DECODE login (it refused him on 17 Nov). Wanted: R9318 (Terranova key), R6087–6097 (Cosimo I keys of
  1554–55, decides no. 2345), R2281 (Viète), R5625–5630 (no. 880). Save to `sources/cache/decode/R<n>/`; key
  sheets go to an isolated agent, not the main thread.
- Greg: scope of the walk (open decision 2 in `PIPELINE.md`). The reachable queue for 1450–1700 is thin.
- Greg: reserve items with Bourdeau, or work unannounced? Target folders, not the catalogue, show who is working.
- `AGENTS.md` shows as modified in the working tree; the change predates this session and was not touched.

## Named wall (if any)
The aligner cannot build a key from a pair whose plain side is an abridgement. Breach: H6.
