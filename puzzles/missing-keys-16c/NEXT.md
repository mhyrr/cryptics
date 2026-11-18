# Next session — missing keys, 1500–1620

**Last session:** 2026-11-17 (third of the day). The 2911 bench was reopened on Fable and passed; the builder
is in `line/align.py` as `build --abridged`. Before that, Greg opened the scope for another target.

## First action

Start with **no. 1336, Speciano and Borromeo**. Read
`items/1336/gate.md`. The Ambrosiana scans are in its local cache.
Run `python3 -I fetch.py` from the item folder to recreate it.

The build pair is F 47 inf. no. 131 c. 269r, cipher, and c. 270r, clear.
The other letters, F 131 inf. no. 7 and F 49 inf. no. 18, are reserved
for transfer. F 49 c. 44r has a separate clear note of uncertain
relation to its cipher slip. Keep that note outside derivation.

Start with a small independent reading sample on c. 269r. Its ink is
blotched and the public image is 750 px wide. Freeze the sign guide, measure
agreement and continue only if legible. Then check pair completeness,
record the anchors and reserve holdout text before fitting. OPAC indexes
F 47 under Speciano but does not name the sender in the title. Check
Rivolta and test whether related known tables already fit before claiming
a missing key. H8 is open.

In a Claude Code session Opus readers and Fable key work are available, as AGENTS.md prescribes. Build the
key with `python3 line/align.py build <cipher> <plain> --out key-v0.tsv --abridged` if the translation is
loose, plain `build` if it is complete. This will be the builder's first clean test (H6).

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
