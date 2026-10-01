# NEXT — handoff for the next session

**Last session:** 2026-10-01
**Where it stopped:** at a named wall (short text). Steps 0–4 of the session plan are done.
Step 5 (the target run) was not run, by the frozen decision rule in
`analysis/01-annealing/README.md`.

## Do first
1. Read `analysis/01-annealing/README.md` (Result). The matched control fails, so a
   ciphertext-only run on f. 539 means nothing. Do not run one.
2. If any outside material arrives, ask whether it gives **same-key text**
   (breach 1) or **known values** (breach 2) before anything else.
3. Next cheap experiment, if there is no new material: pre-register H6. Add seeded-value
   cells (k = 10, 20, 33 known signs) to the 344/145 control. This says how many values
   a crib or key fragment must supply before annealing works. It is the Marmont question
   proper, since Marmont started from 33 values.

## Open questions
- What does DECODE R2281 (ff. 539–540) actually hold? It needs a login; Greg offered to pull it.
- Does Aubery, *Histoire du cardinal duc de Joyeuse* (1654, Gallica bpt6k856018v), print a
  Joyeuse–Villars letter of early 1594, or the plaintext gist of this one?
- Where are Joyeuse's incoming papers for 1594? The clear frame says Villars wrote to him
  "en chiffre" (H7).
- The reader labels are not reconciled (A 145, B 165, Bourdeau 127). This matters only once a
  breach exists. Then reconcile three ways against the image before any solve.
- 152 occurs three times and 89 and 30 twice. Name codes? (H4)

## Named wall
**Short-text wall.** F. 539 has 344 sign tokens over about 145 signs, so each sign is seen
about 2.4 times. A solver that recovers a Marmont-shaped key at 98.6% recovers 6–17% here,
even when every sign is assumed to be a letter. The passing point at this sign count lies
between 700 and 1,400 same-key tokens. Merging variants would have to bring the inventory
to about 40 signs, and the unmarked inventories alone are 79–128.

What would breach it:
1. **More same-key text, about 400 to 1,100 tokens more.** Candidates: Villars's cipher
   letter to Joyeuse (mentioned in the frame); Joyeuse's other Rome despatches of
   Jan–Mar 1594 (BnF fr. 3623–3625 per Bourdeau, unverified; Aubery 1654); DECODE records.
2. **Known values.** A key sheet; a decipherment in another hand; a sign shared with a solved
   sibling (f. 530, f. 555 and Caulet–Joyeuse were all tested and ruled out); or a strong crib.
   Run H6 first to learn how many values are needed.
3. **Viète's own work**, if a decipherment of f. 539 survives anywhere (none found in the volume).
