# Missing keys, c. 1555–1615: find one and recover it

**Catalog entry:** none of its own. It draws on `catalog/entries/french-royal-ciphers-1567-1610.md` and
`charles-v-unsolved-cipher-letters.md`. This is a cross-puzzle study (plan: `ideas/known-keys-two-tracks.md`).
**Status:** opened 2026-11-16 · target chosen (Terranova → Sfondrati, 1583); no transcription or test yet.

## Brief
Greg's goal (2026-11-16): recover a cipher key that nobody has, easiest first. Applying a published key to unread
letters does not count as the result here. The method is to use the keys already reconstructed (Tomokiyo, Devos,
this repo) as a prior on what a missing key of the same chancery looks like.
The planned key census is no longer a product of its own: Bourdeau's project already publishes one over 783 systems
(`canon.md`). We keep only the gap list and one recovery.

## What a solution would have to do
1. **The key is missing.** Before any recovery, every published key of the same power and decade is tested on the
   target by script and fails by a stated margin. If one fits, the result is a known-key reading and is reported as that.
2. **Two blind transcriptions** of the target from the images, agreement measured by script.
3. **Control first.** The recovery method is run on a known key of the same family and similar token count, with the
   pass bar written before the run. No control pass, no target run (the `viete-f539` lesson).
4. **Held-out test.** The key is built on part of the letters and must decode the rest. Report the share of tokens
   decoded and the share of words a reader accepts, both by script, against shuffled-key controls.
5. **Continuous sense.** Decoded cipher must join the clear text on both sides and agree with outside facts
   (names, dates, events of Aug–Oct 1583).
6. **A key table** in `sources/keys/`, each value marked `certain` / `probable` / `unknown` with the positions that
   support it. Unknown codes stay unknown.

## Scope of this dive
In: the gap list (`analysis/01-gaps/`); the Terranova–Sfondrati letters of 1583 (BYU Vault MSS 771 and 518).
Out for now: the eight-power feature census; French targets (Bazin 1573, Danzay 1557–67) until the first target closes.
