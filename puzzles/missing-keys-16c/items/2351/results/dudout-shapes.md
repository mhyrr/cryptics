# Dudout's shapes for the four contradicted Pandolfini values (2026-11-19)

Stage 6 held B. Dudout's key for Francesco Pandolfini's letters of 1514–15, mapped onto our sign names, and
letter A's pair contradicted four of its values: mark `1` = u, base `2` = t, `flong` = f, `hash` = ll. The
question here: is each a mismatch of shapes in our mapping (`sources/map-pandolfini.tsv`), or a real
difference between the two men's ciphers?

## Sources
- CLAIMANT · `https://github.com/dbourdeau/cyphersolver/tree/main/targets/pandolfini1514` and
  `.../targets/pandolfini1515`, fetched 2026-11-19 from `main` into `sources/raw-bourdeau-2026-11-19/`
  (13 files: both `NOTES.md`, `SIGN_CONVENTIONS.md`, `PROTOCOLE.md`, both `profile.json`, seven
  transcriptions). Fetched 2026-11-18: `sources/raw-bourdeau/` (`LEGENDE.md`, `key_v6.json`, `ARBITRAGE-v6.md`).
- **His files hold no image of any sign.** `pandolfini1514/NOTES.md`: "No image or derivative is included."
  A shape can be compared only through his written legend (in French) and through how a sign behaves: how
  often it stands, whether it takes a figure above, what stands beside it. Counts: `dudout_shapes.py`,
  `results/dudout-counts.tsv` (his seven transcriptions, 7,363 tokens; our letters A and B, 3,061).
- Our shapes: `SIGN-GUIDE.md`. Our readers and his agents never saw each other's pages.

## Verdicts

| Value held at stage 6 | Verdict | In short |
|---|---|---|
| mark `1` = u | **same shape; no real difference shown** | the same tick, the same share of the vowel marks (0.052 and 0.051); the stage 6 count is not confirmed by the blind build |
| base `2` = t | **shape mismatch (ours)** | we gave one name to two of his signs: his `Z` (t, never marked, before `7`) and his `2` with a figure (b or c) |
| `flong` = f | **shape mismatch (ours)** | our `flong` behaves as his `F` (barred F = et), not as his rare `J` (f) |
| `hash` = ll | **shape mismatch (ours)** | his `H` and `4#` (ll) behave as our `L4`; our `hash` stands in other places |

So three of the four contradictions come from our mapping, and none is shown to be a difference between
Acciaiuoli's cipher of 1513 and Pandolfini's of 1514–15.

## Mark `1` = u
- His legend: the superscript is "chiffre(s) écrits au-dessus (voyelle)" (figure or figures written above:
  the vowel); 1 = u. Our guide: `^1` is "one short upright or slanted tick". The same thing.
- Share of all vowel marks: his `^1` 191 of 3,701 (0.052); ours 79 of 1,560 (0.051). His other four run
  0.216 to 0.269; ours 0.215 to 0.269. The five marks are the same five in the same proportions, with our
  tilde where his 2 stands.
- Evidence on the value in our letters: stage 6 counted 10 places that spell u against 19 that do not; the
  blind build counted 12 against 8 and marks it u; stage 7 on letter B does not show it (u is above 15 of
  19 other letters; a scores higher). Our readers put a `^1` on signs that take no vowel (`D`, `G`, `B`,
  `alpha`: 10 of 79), and our addendum notes that `^1` and `^5` are confused. A mark read wrongly one time
  in three would give counts like these.
- **Verdict: not a shape mismatch, and not a shown difference. Open.** The value u is reported by Dudout and
  by our blind build; it is not established on letter B.

## Base `2` = t
- His legend has two signs here: `2` ("a 2 or a curled ʒ; not told apart") and `Z` ("trait suivi d'un 2
  couché", a stroke followed by a lying 2, "-2"). His key: `Z` = t; `2` with a figure = c by default, b by
  sense ("signe 2 polyphone b/c"); `2` alone = o.
- How they behave: his `Z` stands 95 times bare and 3 times with a figure, and the next sign is `7` in 86 of
  the 95 (t before r: "tra", "tro"). His `2` stands 14 times bare and 249 times with a figure.
- Ours: `2` ("a low wavy 2 … often with a long flat entry stroke on its left like -2") stands 45 times bare,
  24 of them before `7`, and 28 times with a vowel mark. Our `z` (angular, flat top, bar through the
  middle) stands 12 times bare and 72 with a mark.
- So our unmarked `2` is his `Z`, and our `2` with a mark is part of his `2` with a figure. Our mapping gave
  `Z`'s value t to our `2` under a mark, where it does not belong. Per 1,000 signs: his `2` with a figure 34;
  our `z` with a mark 23.5 plus our `2` with a mark 9.1, together 32.6. His "b or c by sense" is what one
  name for our two shapes would produce: `z` = c (key-v0, confirmed on the pair) and `2` = b.
- The blind build, which knew none of this, gives unmarked `2` = t (3 hits, 7 misses; not marked) and
  `2` with a mark = b (marked `probable`). Stage 7 does not show b on letter B (above 12 of 19 letters).
- **Verdict: shape mismatch in our mapping. No difference between the ciphers is shown.** Leads, reported
  and not established: unmarked `2` = t; `2` with a mark = b.

## `flong` = f
- His legend: `J` = "ʄ (long s/f à boucle)", long s or f with a loop, value f (s in two words of the 1515
  letter); `F` = "F barré = et", a barred F, the word *et* (and).
- Ours: `flong` = "tall stem with a crossbar near the top and a loop or hook at the foot … Very common".
  The crossbar is his `F`'s bar; the loop is his `J`'s. The description fits both.
- How they behave: his `J` stands 18 times (2.4 per 1,000). His `F` stands 117 times (15.9 per 1,000); the
  signs after it are `3` 17, `D` 16, `W` 9. Our `flong` stands 98 times (32.0 per 1,000); the signs after it
  are `3` 14, `omega` 9 (his `W`), `D` 6, `bbar` 6. A sign this common that stands before *a*, *che* and *i*
  is the word "et", not the letter f.
- Ours is twice as common as his `F`. Either Acciaiuoli writes *et* more, or `flong` also holds his `J` or
  another tall sign. Not settled.
- The blind build gives `flong` = et (11 hits, 19 misses). Stage 7 cannot judge it: the model's corpus
  spells the word "e".
- **Verdict: shape mismatch in our mapping (we matched `flong` to `J`; it is mostly his `F`).** Lead,
  reported and not established: `flong` = et.

## `hash` = ll
- His legend: `H` = "# (double barre croisée)", in the 1515 conventions "two looped strokes crossed by a
  bar, ℓℓ"; and `4#` = a 4 crossed by the double bar. Both = ll. The 1515 notes treat them as one sign
  ("our H = his 4#").
- How they behave: his `4#` stands 55 times and his `H` 22 (together 10.5 per 1,000). Before them:
  `3^4` (de), `3` (a), `S^4` (que). After them: `3` (a), `Q` (e), `W` (i), `O` (o). That is "della",
  "alla", "quello".
- Ours: `L4` ("a large 4 whose flat stroke runs out to the left") stands 24 times (7.8 per 1,000); before
  it `S+4` 8 and `3+4` 8. The same places. Our `hash` ("two slanted stems crossed by two bars") stands 19
  times; before it unmarked `z` 8 and `n` 7; never after `3+4` or `S+4`.
- So his ll sign is our `L4`, and our `hash` is some other sign, with no value yet. The blind build gives
  `L4` = "ell" (3 hits, 6 misses), which is ll with a letter taken from its neighbour; stage 7 does not
  show "ell" (above 107 of 199 strings; "lli" scores highest).
- **Verdict: shape mismatch in our mapping.** Lead, reported and not established: `L4` = ll.

## What follows
- The four rows dropped at stage 6 were right to drop: three were on the wrong sign.
- Four leads now have two independent supports (Dudout's key from his pairs; our blind build from ours) and
  no pass on letter B: unmarked `2` = t, `2` with a mark = b, `flong` = et, `L4` = ll. Three of the four are
  not the values stage 7 tested (`L4` was tested as "ell"; unmarked `2` was not a candidate). A new stage
  could test them, registered first, on letter A's pair by hits and misses (it needs no letter model, so
  "et" can be judged) with letter B's lines held out as stage 7 did.
- Nothing here was checked on an image of Pandolfini's letters. That would settle the shapes outright.
