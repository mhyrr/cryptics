# No. 2351 — the reading so far (2026-11-19)

Roberto Acciaiuoli, Florentine ambassador in France, two letters in cipher from Amiens, 23 October 1513
(ASF, Mediceo avanti il Principato, filza LXXII, docs. 190–192). How each figure was got: `README.md`.

Rules of this file. Letters in `code type` are script output (`results/b-lattice-read.txt`): a letter stands
only where a reader's sign has a value in the key; `?` is a place where no reader's sign has one. The spaces
between words, anything in square brackets and all English are interpretation and are mine. Names of people
and the historical setting are from memory and are not verified. No word here has been checked against an
outside source.

## The key
`key-v1.tsv`: the 36 entries of `key-v0.tsv` unchanged, plus two added at stage 7.
- Thirty entries come from B. Dudout's reconstruction of Francesco Pandolfini's cipher of 1514–15 (CLAIMANT;
  Bourdeau's `cyphersolver`), mapped onto our sign names; 22 of them are confirmed on letter A's pair. Six
  were added from that pair. A figure above a consonant sign gives the vowel after it: 3 = i, 4 = e, 5 = a,
  tilde = o.
- **Added 2026-11-19, both `probable`:** `bbar` = i (39 places in letter B) and `zm` = non (19 places). They
  come from a table built blind from letter A and passed a test on letter B written before the run. Neither
  reached `certain`.
- Seven more values from that blind table are listed in `key-v1.tsv` as `unknown` and are not used: mark
  `1` = u, base `2` = b, `flong` = et, `Q` = per, unmarked `4` = maesta, `L4` = ell, `ttt` = tt. The test did
  not show them. It did not refute them either: it misses about one true value in six.
- The blind table's "q" for base `S` is an error; "qu" stands.
- Still without a value: about a quarter of the columns, among them the commonest unmarked sign (`delta`),
  `flong`, and the word signs.

## Letter A (to "the Magnificent Giuliano")
Its chancery copy in clear is c. 233. English from reader PE's transcription: see `readers/PE/NOTES.md`. In
short: the Pope's dealings with France sit badly in many hands; keep them to Monsignor de Marseille alone;
Acciaiuoli has worked on Robertet about the embassy of obedience; the French will do what the Pope wants.

## Letter B (to the government, "Magnifici Domini"): no decipherment in the file

**How much reads.** Three readers (H, G, I) lined up in 1,922 columns over 41 lines.
- 1,396 columns (0.73) have a supported value: 2,530 letters. In 1,184 of them all three readers support it.
- 526 columns are open. In 525 the readers agree well enough and the key has no value for the sign; in 1
  the readers did not read it. More readers would not help. More key would.
- Before today: one merged text, 1,291 of 1,885 signs valued (0.68). The gain is 105 columns: 47 from
  reading the three readers together, 58 from the two added values.

**The test behind it** (registered before the run; `results/b-lattice-test.tsv`): with `key-v0.tsv`, which
never saw letter B, the path through the readers' votes scores above 200 of 200 tables with the same values
shuffled. On planted passages the method passes 19 of 20 Italian texts and 0 of 20 random ones, and 85% of
the letters it prints as supported are right. So a letter below can be wrong, most of all where only one or
two readers support it.

**Phrases, with what each rests on.** The counts are `lattice.py words` (`results/b-words.tsv`): letters
that all three readers support / letters that one or two support / open places. "New" counts letters that
rest on the two values added at stage 7.

| Line | Supported letters, my word division | 3 / 1–2 / open | New | English (mine) |
|---|---|---|---|---|
| 1 | `ultima mia` | 8 / 1 / 0 |  | my last [letter] |
| 1 | `si?nificai alle si?nori` | 19 / 0 / 2 | 1 | I reported to [your] lordships |
| 2 | `senza aueua o?dinato di mandare in ??go?sa` | 25 / 7 / 4 | 1 | "senza" [word sign `T`; see the note under the table] had ordered to send into … [Burgundy?] |
| 2 | `cento lance` | 10 / 0 / 0 |  | hundred lances |
| 3 | `non si moue` | 9 / 0 / 0 | 3 | does not move |
| 3 | `in?epe?tatamente` | 13 / 1 / 2 | 1 | unexpectedly |
| 4 | `la spesa` | 7 / 0 / 0 |  | the expense |
| 4 | `in peri?losi` | 6 / 4 / 1 | 1 | in dangerous … |
| 5 | `felicemente` | 11 / 0 / 0 |  | happily |
| 5 | `ancora maraui?lia` | 11 / 4 / 1 |  | still a wonder |
| 5 | `poteuono ?pa?a pi? auanti che l ampeto de` | 23 / 8 / 3 |  | they could [pass] further than the onset of … |
| 7 | `con la copia de??le??ra` | 11 / 5 / 4 |  | with the copy of the letter[s] |
| 8 | `so?ra questo dise?no ? pensi?ro` | 22 / 1 / 4 |  | on this plan [and] thought |
| 9 | `le parole del ? col quale` | 16 / 3 / 1 |  | the words of the [..] with whom |
| 10 | `pa?lai si uede li ?a dato questa cosa molestia ? ro?to qualche dise?no` | 50 / 3 / 5 | 1 | I spoke: one sees this matter has given him trouble [and] broken some plan |
| 11 | `da un canto lo ?reme la paura de` | 24 / 0 / 1 |  | on one side the fear of … presses him |
| 12 | `lo sde?no con?ro a` | 13 / 0 / 2 |  | the anger against |
| 12 | `de quali mi pa?lo ? molto iratamente dicendomi` | 32 / 5 / 2 | 1 | of whom he spoke to me very angrily, telling me |
| 13 | `per la paura de?o ?e?cito ?n?lese` | 18 / 5 / 5 |  | for fear of the English army |
| 13 | `sendo io loro so?rano si?nore non ?a??o ?auto` | 30 / 2 / 6 | 4 | I being their sovereign lord, they have not had |
| 14 | `ri?ua?do di me` | 8 / 2 / 2 |  | regard for me |
| 14 | `me in pericolo` | 12 / 0 / 0 | 1 | me in danger |
| 14 | `te?to di fa?melo perdere` | 16 / 3 / 2 |  | tried to make me lose it |
| 15 | `qualcosa de? animo del re` | 19 / 1 / 1 |  | something of the King's mind |
| 16 | `monsi?nore li a aueua resposto che ne?? poteua ma?lio sapere l animo di` | 48 / 7 / 4 |  | my lord had answered him that no one could better know the mind of |
| 16 | `che lo? medesimi ? quali ?rono` | 20 / 2 / 3 |  | than they themselves, who were |
| 17 | `conscii se li ?aueuono fa?to ingiuria ? no` | 27 / 5 / 3 | 2 | aware whether they had done him wrong or not |
| 17 | `le consci?nti? loro` | 15 / 0 / 2 |  | their consciences |
| 18 | `?rouando ?aue?li fa?to ingiuria` | 24 / 0 / 4 | 1 | finding they had done him wrong |
| 18 | `e pe?ta?ino la ?nitione` | 15 / 2 / 3 |  | let them expect the punishment |
| 19 | `la stagione del ue?no po?ria ramo?uare lo sde?no` | 34 / 3 / 4 |  | the winter season could soften the anger |
| 20 | `uol?re li animi a riposa?si` | 19 / 2 / 2 |  | turn minds to rest |
| 20 | `romore ? demonseratione ancora` | 26 / 0 / 1 |  | noise [and] show still |
| 22 | `gente dise?nate ? andare in` | 21 / 0 / 2 | 1 | the troops assigned to go into |
| 22 | `non sono ancora ?ndate ne son per moue?si` | 27 / 5 / 2 | 3 | have not yet gone, nor are about to move |
| 29 | `si ne licentia` | 12 / 0 / 0 |  | is being dismissed |
| 30 | `l resto de?? gente` | 11 / 2 / 2 |  | the rest of the troops |
| 31 | `s?riuete ???li?ramente` | 16 / 0 / 5 |  | write … freely |
| 33 | `lo s?ri?ale` | 8 / 0 / 2 |  | the spiritual [matter] |
| 33 | `si fa l o?dinatanne del mandare` | 17 / 8 / 1 |  | the order for the sending is being made |
| 34 | `?redo pa?ino molti gi??ni` | 18 / 0 / 4 | 1 | I believe many days will pass |
| 35 | `questi del consi?lio` | 17 / 0 / 1 |  | those of the council |
| 36 | `da non li segare cosa ne` | 17 / 2 / 0 | 3 | not to [deny] him anything |
| 37 | `sendo se?uita la tempesta` | 18 / 3 / 1 |  | the storm having followed |
| 38 | `le cose in te?mane che per questo` | 17 / 9 / 1 |  | things in such a state that for this |
| 39 | `ue?no non sono per altera? ci pare che din monseri la uia` | 38 / 6 / 2 | 3 | [this] winter are not about to change; it seems to us that God shows us the way |
| 39 | `da ?uenire al?a fine desiderato di` | 18 / 9 / 2 |  | to come to the desired end of |
| 40 | `qui?tare ??rista?nita di che di? li conceda ?ratia` | 35 / 2 / 6 |  | quieting Christendom, for which God grant him grace |
| 40 | `che di qua ?redo sia ??rouare que?a facilita che desi` | 38 / 2 / 4 |  | for here I believe he will find the ease he desires |

Across these 49 phrases: 1,202 places, 969 with all three readers, 124 with one or two, 109 open.

**Notes on the table.**
- Line 2, "senza": the word sign `T` has the value "senza" (without) from Dudout's table, never tested on
  our pair, and one of the three readers has another sign there. "Without had ordered" is not Italian. His
  table gives the same sign with a mark above as "Sua Maestà" (His Majesty), which would give "His Majesty
  had ordered to send into …". That is a guess of mine and is not in the key.
- Line 12, "iratamente" (angrily): yesterday's reading had "ingratamente" (ungraciously), with the gap
  filled by me. The letter i is now supported, by the added value `bbar` = i.
- Line 36, "segare": two of the three readers have the sign for "ne" there and one has the sign for "se";
  the letter model took the one. "negare" (deny) is the majority reading and the word the sentence wants.
  This is the method's known fault (the 85% above), and the table shows it: those letters are counted
  under "1–2".
- Line 16, "ma?lio": the same. Two readers have "me", giving "me?lio" (better).
- "ancora" (still, yet) in lines 5, 20 and 22 is one word sign (`B`), read by all three readers each time.
  Its value is from Dudout's table and was never tested on our pair; it fits all three places.

**What the letter says, as far as it goes (my summary; the phrases above are the evidence).**
- Lines 1–4. He refers to his last letter. Someone had ordered a force sent, with "cento lance" (a hundred
  lances) and thousands of something; a thing happened "unexpectedly"; "the expense"; dangers.
- Lines 5–8. "Happily"; they could go no further than the onset of [a people whose name does not read];
  a copy of letters is enclosed; "on this plan and thought".
- Lines 9–13. He spoke with someone whose title does not read [the King, I think]: the matter has troubled
  him and broken some plan. On one side fear presses him; on the other his anger against [name not read],
  of whom he spoke "very angrily"; fear of the English army.
- Lines 13–18. Quoted speech: "I being their sovereign lord", they had no regard for me; me in danger;
  tried to make me lose it. They had sent to learn "something of the King's mind", and "my lord" answered
  that none could know it better than they themselves, who knew whether they had wronged him or not: let
  them look to their consciences; finding they had wronged him, let them expect the punishment.
- Lines 19–21. The winter season could soften the anger and turn minds to rest; noise and show still.
- Lines 22–32. The troops assigned to go to [place not read] have not gone and are not about to move;
  counts of thousands and hundreds of lances; an army "is being dismissed"; the rest of the troops; "write
  freely".
- Lines 33–41. On the spiritual matter: the order for the sending is being made; he thinks many days will
  pass; those of the council; not to deny him anything; the storm having passed and things so placed that
  they will not change this winter, "it seems to us that God shows us the way" to the desired end of
  quieting Christendom, "for which God grant him grace; for here I believe he will find the ease he desires".

The Swiss, Burgundy and the King named in yesterday's version of this file are my reading of gaps
(`??go?sa`, `de??si`, `del?`), not supported letters. They are likely and they are not shown.

## What is not done
- A quarter of letter B's columns have no value. Four leads have two independent supports each (Dudout's
  key and our blind table) and no pass on letter B: unmarked `2` = t, `2` with a mark = b, `flong` = et,
  `L4` = ll (`results/dudout-shapes.md`). `flong` alone stands at 68 places in letter B. They need a
  registered test that does not lean on the letter model, which cannot judge "et".
- No phrase has been checked against an outside source: who "Monsignore" is, the campaign of autumn 1513,
  the embassy "for the spiritual matter".
- Whether letter B is printed anywhere is checked only against Desjardins and Canestrini vol. 2 (absent).
- The four values of the Pandolfini table that this hand seemed to contradict have had their second look:
  three were our mismatch of shapes, and mark `1` = u is open (`results/dudout-shapes.md`). No image of
  Pandolfini's letters was seen.
