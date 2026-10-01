# Joyeuse to Villars, 15 February 1594 (BnF Cinq Cents de Colbert 33, f. 539)

**Catalog entry:** `catalog/entries/viete-undeciphered-ciphertexts.md` · **Ticket:** TK-006
(the folder is named `viete-f539` because the dive covers only f. 539, the
unsolved item of that entry; f. 555 is its solved control)
**Status:** opened 2026-10-01 · short-text wall. Gate passes on length, but the matched annealing control fails (0.093 vs 0.986 positive). Target not run. Breach needs more same-key text or seeded values.

## Brief
F. 539 is an original letter from Cardinal François de Joyeuse in Rome to André
de Brancas, seigneur de Villars, League governor of Rouen. It is dated 15 February
1594. A clear French frame surrounds an 11-line block in a graphic-sign cipher.
The volume has no decipherment of it. This dive asks one question: is f. 539
breakable the way the Marmont letter was? Marmont's recipe has three steps: a good
transcription from the image, homophonic annealing, and a check against an
outside document.

## What a solution would have to do
1. Give one sign-to-value table that reads the whole cipher block as continuous
   French. The table must reproduce from a transcription that someone else can
   check against the Gallica image (canvas 544).
2. Show the solver recovering a known key on a synthetic text of the same length,
   the same sign count and the same layer structure (letters, marked signs,
   numbers) before its output on f. 539 counts. A solver that fails this control
   proves nothing on f. 539, in either direction.
3. Agree with the clear frame. The cipher sits after "Ce que je vous puis dire
   d'icy en substance n'est autre chose sinon que", so the plaintext must
   continue that sentence and be news from Rome.
4. Fit the Rome mission of February 1594 and Villars's position (the truce, and
   his negotiation with Henri IV that ended in the treaty of 27 March 1594). It
   must not contradict the letters of the same week in the volume (ff. 535–555).
5. Account for every layer: the code numbers either get readings consistent
   across their repeats (152 occurs three times) or are left as named code groups,
   not forced into letters.
6. Ideally, agree with an independent witness: a second letter in the same key,
   a key sheet, or an interlinear gloss.

## Scope of this dive
In scope: the race check, the images, a blind second transcription, the length
gate, and, only if the text passes the gate, a pre-registered annealing run with
a matched control. Out of scope this session: archival search outside Gallica,
and a full re-solve of f. 555 (it is the control, used only for its length and
sign count).
