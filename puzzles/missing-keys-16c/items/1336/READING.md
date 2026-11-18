# No. 1336 — the reading so far (2026-11-18)

Speciano and Borromeo, Milan, Biblioteca Ambrosiana, 1574–75. No published key was found at the gate
(`gate.md`). How each figure here was got is in `README.md`; the method is in `../../line/METHOD.md`.

Rules of this file. Decoded lines are script output (`results/reading.txt`, `results/lattice-read.txt`,
`results/omitted.txt`). `?` is a sign with no value, or a place the readers did not settle. Word division, the
letters in square brackets and every English gloss are interpretation and are mine.

## The key: 28 values (`key-v2.tsv`)
One sign per letter, several signs for the common vowels, one sign for a doubled letter. Sign names are the
shape names of `SIGN-GUIDE.md`.

| Letter | Signs | Letter | Signs |
|---|---|---|---|
| a | `3` `7` `4` | m | `K` |
| b | `plus` | n | `qx` |
| c | `odot` | o | `6` `pis` |
| d | `tri` `trid` | p | `hash` |
| e | `8` `a` `2` | r | `x` |
| f | `dcross` | s | `H` |
| g | `q` | t | `M` |
| h | `zhe` | tt | `omega` |
| i | `l` `lam` | u | `A` `E` `sha` |
| l | `v` | | |

What it rests on: three tables built blind from two pairs. The c. 44r table and the c. 269r table agree on 13
of 14 shared signs; the four-reader c. 269r table agrees with their union on 23 of 24. With the first 17
values held, 263 of 373 places on c. 269r spell its translation; shuffled tables give 110 to 141.

Seen but under the bar (not used above): `utail` i (5 places of 5), `pi` o (5 of 7), `box` e (6 of 8), `N` s
(3 of 3), `u` i (9 of 16; probably two shapes under one name). No value yet: `phi`, `boxbar`, `9`, `theta`.

## 1. The small slip, F 49 inf. c. 44r (101 signs, 87 valued)

    ??linomidisueidueprinc?pali??nominat
    ge?alett?raacarnigli?onoilca?te?ano
    dimilanoetilpr?mid?nted?l?enato

Italian: ?? li nomi di [q]uei due princ[i]pali ?? nominat? ge? a lett[e]ra a Carnigli[a] [s]ono il ca[s]te[ll]ano
di Milano et il pr[e]mid[e]nte d[e]l [S]enato.

English: "…the names of those two principals … named in the letter to Carniglia are the castellan of Milan
and the president of the Senate."

- The clear note under the slip says the same. Its two readers could not read two words; the cipher gives
  both: `princ?pali` and `pr?mid?nte`.
- Unexplained: `m` where "presidente" has `s`; `s` where "quei" has `q` (the sign `H` is `s` at 8 places on the
  other slip and `q` at one place here).

## 2. The main slip, F 47 inf. c. 269r (784 signs after the four-reader merge, 571 valued)
The period translation on c. 270r, as reader PA has it, with my English:

> Sua Santità essendo risoluta di avocare lei propria la causa della giurisdittione, ha eletto monsignor
> Frumento et Gratti che andò in Spagna l'anno passato, liquali s'habbino da studiare secretamente … perché
> havendola detta a monsignor Carniglia gli ordinò che non dicessi cosa alcuna … ma io l'ho saputo da uno di
> questi tre deputati … li dui ultimi deputati a me paiono buoni ma il primo mi dà gran fastidio, perché non
> vedo come Sua Santità se ne possa fidare … a suo tempo sarà bene farne avvisato il Papa … et questo si potrà
> fare alla venuta di lei.

"His Holiness, having resolved to take the jurisdiction case to himself, has chosen Monsignor Frumento and
Gratti, who went to Spain last year, to study it in secret … having told Monsignor Carniglia, he ordered him
to say nothing … but I learned it from one of these three deputies … the last two deputies seem good to me,
but the first troubles me greatly, because I do not see how His Holiness can trust him … in due time it will
be well to warn the Pope … and this can be done when you come."

The cipher by our key, lines 1, 3, 9–11 of 15 (all 15 are in `results/reading.txt`):

     1  ???uadsantita?epen?dos?ris?uua??diu?derel?eipr?pr
     3  gnur?t?o?i??fruumenti??t?rapictt?ean??igpnnau?u?la?o?
     9  ?secretip??mament?g?n?mihaper?sroi?to??e??n??n??
    10  ???riuaale?g??u?uiduoiu?t?im?deputut?am?paionobuonimailp
    11  rimomitt???dag?ran?astidiop?uero????no?g?ue?o?asante?

- The decode follows the translation throughout: `santita` (1), `fruumenti` (3), `secreti…mament` (9),
  `paiono buoni ma il p|rimo mi` (10–11), `gran ?astidio` (11).
- **The cipher is fuller than the translation at one place** (`results/omitted.txt`): between "monsignor" and
  "Frumento" stand about 11 signs with no counterpart, decoding `ur?t?` … `i??`. The translation speaks of
  three deputies and names two. Whether those signs hold a third name or a forename is not read.
- The second name is `?rapictt?` in the cipher; the readers of the translation give "Gratti" with doubt.
- Seven signs after the last word of the translation (`?utt????`) are not read.

## 3. The bare line, F 131 inf. c. 14r, 4 July 1574 (38 columns from four readers)
The clear line before it ends "il tutto è" ("the whole of it is"). No decipherment is on the page.

    ?con?participa???u?ne??de?rum?ntoe

Italian: ? con ? participa… ? ? ? u ? n e ? ? de[l] [F]rum[e]nto e

English: "… with … participat… … of Frumento and …"

- Test: the best path under the true table scores above 200 of 200 shuffled tables (`results/lattice-test.tsv`,
  28 values; 199 of 200 with 26). This was a post-hoc test after a registered one failed; see `README.md`.
- 21 of the 26 letters shown have all four readers' votes. `f` before `rum` has three readers of four and was
  dropped by the path.
- Open because the key has no value (readers agree): columns 1, 16, 17, 18, 20, 23. More paired text cures
  these.
- Open because the readers disagree: columns 5, 9, 24, 25, 27–29, 33, under a stain and a hole. A better
  image cures these.

## What is new here
- A 28-value key for a cipher with no published key.
- Two words of the c. 44r note that its own clear text does not yield to the readers.
- A partial reading of a line that has no decipherment: it concerns something done "with … participat…" and
  "of Frumento".
- A place where the cipher slip holds more than its period translation.

None of this has been checked against the Ambrosiana's manuscript catalogue or the literature on Borromeo's
correspondence beyond the gate search.
