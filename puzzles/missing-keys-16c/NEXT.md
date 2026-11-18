# Next session — missing keys, 1500–1620

**Last session:** 2026-11-18. No. 1336 went from 17 values to a 28-value key and a partial reading of the bare
line. The method is written down in `line/METHOD.md`; the result in `items/1336/READING.md`.

## First action

**No. 1336, Speciano and Borromeo.** Read `items/1336/READING.md`, then `items/1336/README.md` from "Fifth
stage" down. State: `key-v2.tsv` (28 values; three blind tables agree on 23 of 24 shared signs); bare line on
F 131 inf. c. 14r reads `?con?participa???u?ne??de?rum?ntoe` (post-hoc test, above 200 of 200 shuffles).

In order:
1. **More text in this cipher.** Search the Ambrosiana viewer for other Speciano–Borromeo letters of 1574–75
   with cipher (F 47, F 49, F 131 inf. and neighbours). Each paired passage values more signs (`u`, `utail`,
   `pi`, `boxbar`, `9`, `phi` are agreed by readers and unvalued); each bare passage is a new reading.
2. **The 11 signs between "monsignor" and "Frumento"** on c. 269r line 2–3 that the translation lacks
   (`results/omitted.txt`): two more readers on bands 1–2 only, then the lattice method there.
3. **The split sign `u`**: readers put two shapes under one name (values i, t, l at different places). A
   guide revision 2 for that one shape, then re-read.
4. Greg's call: better images of c. 14r and c. 269r from the Ambrosiana; Rivolta for the attribution; the
   literature on the 1574 jurisdiction dispute for Frumento, Gratti and Carniglia.

Not done: `/session-close` (handoffs written by hand). Commits since `feab65c` are local, not pushed.
Readers' crops are in `items/1336/readers/<X>/crops/` (not checked in).

## Second item in flight: no. 2351, Acciaiuoli (opened 2026-11-18)
Read `items/2351/README.md` ("Where this stands"). Cipher letter A is transcribed well (three readers, 0.91);
the clear copy on c. 233 is not (four readers, under half the words). Four registered stages failed: two
paired builds, a builder tied to consonant-and-vowel structure, and a cipher-only solve in twelve forms. No
table is kept. The mark structure is real (`results/marks.tsv`); its meaning is not known.
Next, in order: (1) find the published Pandolfini table the gate mentions and screen it against letter A by
script; (2) Greg's call: a real scan of c. 233 from the ASF, or a stronger reader on the image we hold;
(3) transcribe letter B and widen the cipher-only search to forms where a base holds several values.
Tools made here that are general: `items/2351/tied.py` and `solve.py` (planted checks in `results/`).

## Other candidates

- **No. 2345, Baldovino:** the prescribed archive probe timed out again.
- **No. 1332, Castaldo:** the taken list and merged recovery settle the race.
  Its glosses and published key could serve as a separate control.
- **No. 2911:** bench passed in a second session on Fable. `align.py build --abridged` rebuilds the key
  blind: p1 0.964 precision, 0.629 recall, 36 of 36 rows; full 0.935, 0.617, 33 of 36 (full scored twice).
  Bare letters: V/134 66% of signs valued, 94% agree with the period key; V/125 63%, 79%. Record:
  `items/2911/bench/README.md`. Open on this item:
  1. **Is any of it unread in print?** Machiavelli's copy leaves out 42% of V/140, and Opere VI (1877) does not
     print V/134. Check Bertelli 1964 and the Edizione Nazionale (Legazioni, 1510) for V/134, V/125 and the
     full text of V/140. If they are absent, the period-key decodes in `items/2911/outside/` are a first
     reading, and need a second reader before any claim. Not checked yet.
  2. H7: an answer-free stage 4 bar. Candidate: the row evidence score of `mark_by_evidence`.
  3. The beam is sensitive on short pairs (finds all or half of the table; no wrong rows either way). A
     planted pair as loose as 2911 (55% of places spell the plain side) has not been run through `synth.py`.

Terranova remains a separate class C target.
