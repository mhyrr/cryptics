# "BLUME SALAMANCA": two cipher telegrams, Zurich to Salamanca, 8 January 1937

**Catalog entry:** `catalog/entries/early-20th-century-coded-telegrams.md` (member 3) · **Ticket:** TK-008
(the folder is named for the one member this dive attacks, as `viete-f539` is)
**Status:** opened 2026-10-16 · no solution. Diagnosis (session 5, 2026-10-17): a transposition of a
natural-letter text, one system for both telegrams; every other cipher type refuted. Excluded with passing controls:
double columnar w ≤ 15 (full length, and with the end cut off), single columnar (with the end cut off), routes,
sets of n and Nihilist read by rows (T1 n ≤ 50, any preamble; session 6, `18`), the 4 × 4 grille. Open: double
columnar with long keys (the named wall). See `NEXT.md` and `sources/key-type-ranking.md`.

## Brief
Dr. ing. W. E. Oswald's Zurich office (Bahnhofstrasse 12) sent two telegrams to "BLUME SALAMANCA" on
8 January 1937. Telegram 1 has 123 five-letter groups (615 letters), and telegram 2 has 32 groups (160 letters).
Werner Oswald told the Swiss Federal Police that his brother Viktor sent them, about wool and Swiss export credits.
The letters have the frequencies of a natural language, so the text is probably a transposition. We try to recover
the keys, or to exclude a stated family of transpositions with planted controls that show the search could have
found the keys.

## What a solution would have to do
From the catalog entry: "give one pair of keys per telegram, or a shared key, that turns all 615 and 160 letters
into continuous Spanish (or the language actually used), without residual unexplained letters. The content must
be checkable against Oswald's documented business and the Nationalist side's 1937 procurement. A key that reads
only a fragment is not a solution." Sharpened:

1. **Whole text.** One stated system and key turns all 615 letters of telegram 1 into continuous text in one
   language. Every letter is accounted for: as plaintext, or as a null or padding letter that follows a stated rule.
2. **Telegram 2.** The same system reads all 160 letters of telegram 2, with the same keys or with keys whose
   relation to telegram 1's keys is stated (for example, a daily key change).
3. **Independent re-decrypt.** A script that shares no code with the solver reproduces both plaintexts from the
   keys and from our transcription (`sources/telegram-1.txt`, `sources/telegram-2.txt`, SHA-256 in
   `sources/PROVENANCE.md`).
4. **Score above the control threshold.** The plaintext scores above the threshold that the matched controls set
   in `analysis/01-solver/README.md` before any target run. A fluent fragment is not a hit: annealers make fluent
   fragments from noise.
5. **The system existed.** The system was in documented use in 1936–37, or it is a simple variant of one that was.
6. **Content check.** The text fits the documented context: Viktor and Werner Oswald, the wool and export-credit
   deal, Hisma, Burgos and Salamanca in January 1937, and Nationalist procurement. It must not contradict the
   dossier (Swiss Federal Archives E4320B#1974/47#277).
7. **Lengths agree.** The plaintext length and any padding agree with the form's word counts (125 and 34 words
   including the address).

## Scope of this dive
**In scope this session:** Step 0 (prior work), the transcription check against the images, context and cribs,
a solver for double columnar transposition after Lasry, Kopal and Wacker (2014) with matched controls, and target
runs only in bands whose control passes.

**Out of scope:** contacting Bourdeau, Bean, Fuentes or anyone else (an external action, so ask Greg first);
regions Bourdeau already excluded (used only as solver controls); any family with no documented use in 1937.

## The excluded region (Step 0, from Bourdeau's notes, 11 Oct 2026)
Source: `https://github.com/dbourdeau/cyphersolver/blob/main/targets/blume/NOTES.md` (CLAIMANT tier: his own
runs, with planted controls and checked-in logs). Conventions: *forward* = write rows, read columns (twice).
*Reversed* = write columns, read rows. *Mixed* = one of each.

| region | method | his control |
|---|---|---|
| every single transposition: rail fence, decimation, routes, single columnar ≤ 20 | exhaustive or annealing | plants recovered |
| forward single columnar, widths 21–45 | annealing on the whole decryption | plants 25–45 read (partly) |
| all reversed-direction systems, single and double (w1·w2 below ~560) | lag scan | z 9–26 on plants vs 3.9 on target |
| forward double columnar, w2 ≤ 10, w1 ≤ 41 | exhaustive K2 + IDP, K1 annealed | true K2 rank 1 of w2! |
| forward double columnar, w2 = 11, w1 ≤ 41 | exhaustive K2 (7.6 h) | rank 1 of 39,916,800 |
| both mixed conventions, w2 ≤ 10 (w1 ≤ 61 or 41) | exhaustive K2 | plant 19 × 8 read |
| K2 a dictionary word or a 1–5-word phrase (2.65 M + 3.98 M entries), w1 8–40 | IDP dictionary attack | z 11–21 on plants |
| full-key annealing, forward, two keys to 16 × 16 | annealing | power only to ~11 × 14 |

**Open:** forward double columnar (and the mixed conventions) with both keys of 12 letters or more, where K2 is
not a dictionary phrase. Bourdeau's swap-based IDP local search failed on plants at 19 × 23 ("a needle").
Lasry reports success of over 60% at 19 × 20 and 90% at 18–19 on 599 letters, with segment moves and a
left-to-right pre-pass (thesis, ch. 9.4.6). Our search starts there.
