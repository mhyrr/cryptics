# Next session — missing keys, 1500–1620

**Last session:** 2026-11-17 (third of the day; it went on to open no. 1336). The 2911 bench was reopened on Fable and passed; the builder
is in `line/align.py` as `build --abridged`. Before that, Greg opened the scope for another target.

## First action

**No. 1336, Speciano and Borromeo**, is open and half done. Read `items/1336/README.md` from "Plan B" down.
State: a 17-value table (`items/1336/key-c44-v0.tsv`, provisional rows = share ≥ 0.6) built from the clean
slip on F 49 inf. c. 44r and its note, confirmed on the F 47 slip against its translation (263 of 373 exact
matches; shuffles 110–141). The cipher is one sign per letter. No reading of the bare line on c. 14r is
claimed.

In order:
1. Widen the table: `align.py build --abridged` on c. 269r against c. 270r. Use a majority of the four
   readers (A, B with `n-a`→`a`, `n-slong`→`slong`; C, D). Check it against the 17 values: count signs valued
   differently. Register the check before running.
2. Two more Opus readers on c. 14r with guide revision 1 (first pair agreed on 0.750).
3. Then the c. 14r decode, tested by exact matches against shuffles before any Italian is quoted.
4. Greg's call: ask the Ambrosiana for a better image of F 47 inf. c. 269r; check Rivolta for the
   attribution of F 47 no. 131; look for more letters in this cipher in the Borromeo correspondence.

Readers' crops live in `items/1336/readers/<X>/crops/` and in the session scratchpad; no reader reported
opening another's.

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
