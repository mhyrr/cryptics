# NEXT — handoff for the next session

**Last session:** 2026-10-03
**Where it stopped:** at a named wall (short text). Steps 0–4 of the session plan are done.
Step 5 (the target run) was not run, by the frozen decision rule in
`analysis/01-annealing/README.md`.

## Do first
1. Nothing automatic is left to try on f. 539 as it stands. Experiments 01 and 02 close both
   ciphertext-only and crib-seeded annealing: `analysis/01-annealing/`, `analysis/02-seeded/`.
2. Work only on breaches: a key sheet, or more same-key text (see Named wall). The best
   archival lead is Villars's own cipher letter to Joyeuse, mentioned in the frame (H7).
3. If a partial key turns up with ≥ 33–50 values, the next step is a human-assisted finish
   from the solver's output, not more annealing.

## Open questions
- DECODE R2281: Greg's account gets no images (not needed); the record text is still unchecked.
- Aubery, *Histoire du cardinal duc de Joyeuse* (1654, Gallica bpt6k856018v) has no OCR (0%).
  Searching it means reading page images; its second part (432 pp. of pieces) is the target.
- The April 1594 packet digest (f. 394) and Joyeuse's same-day letters are read: there is no gist
  of f. 539 and no Villars. The content is likely the Pope's refusal of Navarre (H8).
- 209 occurs in f. 539 and as ij^c ix in f. 553: is there a shared Rome numeric nomenclator (H4)?
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
2. **Known values: nearly the whole key.** A key sheet or a decipherment in another hand. Siblings
   f. 530, f. 555 and Caulet–Joyeuse are ruled out. Experiment 02 shows cribs and fragments are not
   enough: 50 known signs leave ~45% of the rest wrong.
3. **Viète's own work**, if a decipherment of f. 539 survives anywhere (none found in the volume).
