# Next session — missing keys, 1500–1620

**Last session:** 2026-11-18 (evening; restart after the usage limit). Both cut-off items finished.
- **No. 1336:** the memorandum F 46 inf. n. 275 c. 652r (1573, no decipherment) is in our table. Test
  registered before the decode: above 200 of 200 shuffles. Partial reading: `items/1336/READING.md` section 4.
- **No. 2351:** the blind bench met its bar in two scored runs (55 shared signs, 53 the same). Builder ported
  as `items/2351/tied.py blind`. Record: `items/2351/bench/README.md`.
- **No. 2911:** the print check hit a library wall (below).
`/session-close` was run. Commits are local, not pushed.

## First action: no. 1336, widen the key with c. 652r held out properly
Read `items/1336/READING.md` section 4 and `items/1336/README.md` from "Sixth stage" down.
State: `key-v2.tsv` has 28 values and now reads three leaves. On c. 652r 144 of 190 columns have a supported
letter; lines 6 and 7 are half open.

1. **Register a seventh stage before touching the key.** The c. 652r decode suggests values for unvalued
   signs (`pi`, `boxbar`, `u`, `theta`; `READING.md` lists them as leads). They come from that decode, so
   they are not evidence there. Design: propose values from c. 652r lines 4–5 and 10–12 plus the clear
   frame, then test on lines 6–7, on c. 14r's open columns and on the 11 untranslated signs of c. 269r
   (`results/omitted.txt`). Write the bar first.
2. **The guide.** Four readers asked for the same rulings: `q` against `qx` when a long stroke runs under
   two signs; the small `H` against `N`; dots inside runs; strike-through lines (line 5). Readers also made
   up names for one sign four ways (`n-dollar`, `n-phi8`, `n-sbar`; `n-tribar`, `n-eqtri`). A guide revision
   2, then two fresh readers on lines 6–7 only.
3. **Outside check of the reading** (catalog rule 1): who the judge is, the "Litta" case, the 1573
   jurisdiction dispute at Milan. Nothing in section 4 has been checked against the literature.
4. **More text:** the scout's list `items/1336/more-letters.md` has smaller cipher groups not yet read.
5. Greg's call: better images of c. 14r, c. 269r and c. 652r from the Ambrosiana; Rivolta for the
   attribution; whether to tell anyone.

## Second: no. 2351, Acciaiuoli
Read `items/2351/READING.md`, then `items/2351/bench/README.md` ("Result" down).
1. **Compare the blind table with `key-v0.tsv`** (the main thread may now do this; the bench is closed).
   Run 2 marks 19 signs the answer does not value and differs on 2 shared signs: each is either a new value
   or an error. Decide by letter B, with a registered test, not by eye.
2. Lattice reading of letter B with per-word support, as on no. 1336.
3. Dudout's shapes for the four contradicted values.
4. Greg's call: tell Bourdeau or Dudout (outside message); check other editions for letter B.

## Walls named this session
- **No. 2911, is V/134 or V/125 unread in print?** Bertelli, *Legazioni e commissarie* (1964) and the
  Edizione Nazionale vol. VI are not online as far as three searches went. Breach: a library copy; look for
  the Dieci's letter of 17 Aug 1510 (incipit "Dopo l'ultima de' x") and the "Summario" of 22 Aug 1510.
  Until then the decodes in `items/2911/outside/` make no claim to be a first reading.

## Open on method
- H6: the clean test is still owed. Both builders (`align.py build --abridged`, `tied.py blind`) passed on
  the pair they were shaped on. A third pair, or a planted pair as loose as the real ones (55% of places
  spell the plain side; 1.64 letters a sign), would test them.
- H7: an answer-free stage 4 bar; candidate is the row evidence score.
- `tied.py blind` needs a foothold: 3 of 6 short planted pairs (450–600 signs) fail, visibly.

## Housekeeping
- Stale crops from the cut-off readers sit in `items/1336/readers/{J,K,L,M}/crops/` (untracked; a delete
  was denied this session). New crops are in `crops2/`. Safe to remove by hand.
- `items/2351/bench/runs/*.key.tsv` and logs hold values and are untracked on purpose.

## Other candidates
- **No. 2345, Baldovino:** the archive probe timed out twice; awaits Florence scans.
- **No. 1332, Castaldo:** key already published (PR 224); usable as a separate control.
- Terranova remains a separate class C target (README criteria; H1–H4 untested).
