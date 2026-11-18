# Next session — missing keys, 1500–1620

**Last session:** 2026-11-18 (long). No. 1336: a 28-value key built by us and a partial reading of a bare line.
No. 2351: opened, four failed stages, then read with a mostly borrowed key (Dudout's Pandolfini table); letter
B, which has no decipherment in the file, passes its registered test. Method: `line/METHOD.md`. Results:
`items/1336/READING.md`, `items/2351/READING.md`. `/session-close` was not run; handoffs written by hand.

## Stopped mid-flight on 2026-11-18 (usage limit, about 16:30 ET). Do these first.
Five background agents were cut off. A new session cannot resume them; start them again.

1. **No. 1336, new leaf F 46 inf. n. 275, c. 652r** (`items/1336/README.md`, "Sixth stage"; registered, not
   run). Strips are cut (`python3 items/1336/strips652.py` remakes them; the image is
   `items/1336/cache/more/11447.jpg`, refetch by id 11447 with `fetch.py`'s URL form if the cache is gone).
   Clear-word readers PJ and PK are done (`readers/PJ|PK/p652.txt`). **Cipher readers J, K, L, M wrote
   nothing: dispatch four Opus readers again with `items/1336/reader-prompt-c652.md`.** Both plain readers
   found cipher on eight lines, not seven: line 8 begins with two signs that may end line 7's run. Tell the
   cipher readers so (a note beside the prompt, not a change to the guide), and cut a strip for line 8, or
   rows will not line up across readers. Then `python3 lattice652.py test`, and only after it
   `python3 lattice652.py read`. Do not look at any decode before the test.
2. **No. 2351, blind bench** (`items/2351/bench/README.md`). The Fable agent was cut off after writing
   `bench/variants/v1_free.py` and `v2_soft.py` and one unscored table in `bench/runs/`; no scored run
   (`runs/results.tsv` does not exist), nothing committed, no notes in the bench README. Start one fresh
   Fable agent with the same brief (the dispatch text is in the session transcript: point it at
   `bench/README.md`, tell it the two variant files exist and are unreviewed). The main session has seen the
   key's values and must not write builder code for this bench itself.

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
Read `items/2351/READING.md`, then `items/2351/README.md` from "Stage 5" down. State: the cipher is, in most
values, the one B. Dudout rebuilt for Pandolfini (1514–15, same filza). `key-v0.tsv` has 36 entries (30 from
his table, 22 of them confirmed on letter A's pair; 6 added). Letter B, never used in the build, passes its
registered test (trigram mean −2.055 against a shuffle maximum of −2.278) and decodes to Italian in long
runs: the King's anger at the Swiss, fear for Burgundy and of the English, troops not yet moved, the winter,
the council ready to deny the Pope nothing. Four earlier stages failed and are recorded.
Next: (1) widen the key from letter A's pair with the 36 values held and reader PE's text (the unvalued
signs `delta`, `beta`, `Q`, `gamma`, `bbar`, `zm`, `L4`, the word signs and the numbers between points);
(2) a lattice reading of letter B with per-word support, as on no. 1336; (3) check Dudout's shapes for the
four contradicted values; (4) Greg's call: tell Bourdeau or Dudout (outside message); check other editions
for letter B.

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
