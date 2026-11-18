# Next session — missing keys, 1500–1620

**Last session:** 2026-11-18. No. 1336: the table was widened to 26 values and the bare line was tested. The
test failed on reader disagreement. The 2911 bench passed the day before; the builder is `line/align.py
build --abridged`.

## First action

**No. 1336, Speciano and Borromeo**, stands at a named wall. Read `items/1336/README.md` from "Third stage" down.
- `items/1336/key-v1.tsv`: 26 sign values. Two tables built apart (c. 44r pair; c. 269r pair, blind) agree
  on 13 of 14 shared signs. The cipher is one sign per letter, with several signs for each vowel.
- Bare line on F 131 inf. c. 14r: readers E and F agree at 0.806 (bar 0.85). The registered word-coverage
  test passes on E (above 194 of 200 shuffles) and fails on F (167). **No reading is claimed.**
- **Later, a post-hoc test combining the four readers passed** (`items/1336/lattice.py`; above 199 of 200
  shuffles). Proposed reading: `?con?participa???u?ne??de?rum?ntoe`. **Next: value the signs `u`, `utail`,
  `pi`, `boxbar`, `9`, `phi` from c. 269r with the same four-reader columns against the c. 270r text
  (register first), then rerun `lattice.py read`.**
- Observation, untested: the four decodes share `con`, `icipa`, `rum?nto`; the clear line before it ends
  "il tutto e". About ten signs under a brown stain are the wall. The table is no longer the limit.

What would breach it, all Greg's call:
1. A better image of F 131 inf. c. 14r and F 47 inf. c. 269r from the Ambrosiana (an outside message).
2. More letters in this cipher in the Borromeo correspondence (F 47, F 49, F 131 inf. and neighbours): each
   bare passage with a clean image is a new reading with the 26 values. This needs no outside message, only
   the Ambrosiana's public viewer, and is the best next step inside the repo.
3. Rivolta's catalogue for the attribution of F 47 no. 131.

Not yet done: `/session-close` was not run on 2026-11-17 or 2026-11-18; the handoffs were written by hand.
Readers' crops live in `items/1336/readers/<X>/crops/` (not checked in); no reader reported opening another's.

## Other candidates

- **No. 2351, Acciaiuoli:** strongest reported complete pair, three documents
  from the same date. The Florence image endpoints timed out, including
  outside the sandbox. Ready to revisit when scans are available.
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
