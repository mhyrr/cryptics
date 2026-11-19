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

## 4. The memorandum, F 46 inf. n. 275, c. 652r, 1573 (190 columns from four readers; no decipherment exists)
Registered test passed before the decode was seen: true table above 200 of 200 shuffled tables
(`results/c652-test.tsv`). Lower case: letters a reader's sign supports under `key-v2.tsv`. `?`: no value or
no agreement. Clear words are reader PJ's, with PK's variant after a slash. `results/c652-read.txt` shows
which letters all four readers support.

| line | text |
|---|---|
| 1–3 | Le cause di sospicione da poter dir publicamente se sara necessario sono La propalatione del suo uoto che uoi scriuete hora, et hauete scritto altre uolte. Le seconde/secrete da dire a N. S.re sono l'esser lui nella medesima |
| 4 | Nun(ti)o? / Nauo? con Mass..o? / Mastro? nella cosa **??del??giuol??littaa** |
| 5 | **m?fu?att??apere** a S. S.ta celo / uelo **inordinatu?im?** |
| 6 | **ietaghim?t????u?deimbarlamentoi?uesiuero** (six readers; see "Reading update" below) |
| 7–8 | **delpo?tifich??lme?gli?lopersei?redeualae te** (line 7 from six readers) per il quale si puo pensare quanto potrebbe sauedere / strauedere facilmente |
| 9 | nel giudicar cause doue sia interessato Principe con potent… |
| 10 | si aggiunge **tt?laopigi?c?esuasantita** da alcuni / Se alcuno |
| 11 | uolte mostrato meco hauer **eedi?inonbu?ga** per la quale |
| 12–13 | **??gdeue** haa / Sua confidar tal giudicio nelle me mani, ne io fidarme ne in tanto interesse della mia chiesa. |

English of the clear frame: "The grounds of suspicion that can be stated publicly, if it is necessary, are
the disclosure of his vote, which you write now and have written before. The second (or: secret) ones, to be
told to Our Lord [the Pope], are his being in the same … in the matter … by which one can judge how easily
he might go wrong in judging cases where a Prince is concerned … there is added … for which … entrust such
a judgment to my hands, nor I trust myself … in so great an interest of my church."

**What the cipher gives, by script:** `del`, `giuol`, `litta`, `fu?att??apere`, `inordinat`, `barlamento`,
`delpontific?t`, `opi`, `esuasantita`, `non`, `deue`.

**My interpretation, not a result:** "fu fatto sapere" (it was made known); "inordinat…" (inordinate);
"parlamento" (parliament, or talk); "del pontificat[o]" (of the pontificate); "l'opi[n]i[one] che Sua
Santità" (the opinion that His Holiness); "[non] deve … confidar tal giudicio" (must [not] entrust such a
judgment); "giuol … Litta" may be "[fi]gliuol[o] … Litta" (the son of Litta; Litta is a Milanese family).
The sense fits the clear frame: reasons to hold a judge suspect in a case touching the writer's church.
No name, date or event has been checked outside.

**Leads for unvalued signs (from this decode, so not yet evidence):** `pi` between `pontific` and `t`
(a?) and in `u?ga`; `boxbar` in `fu?att`; `u`/`theta` in line 6. A registered stage should hold these out.

**Seventh stage, 2026-11-19: no new supported letter.** A registered test of values proposed by script
from lines 4–5 and 10–12 failed its bar (true table above 178 of 200 control tables; bar 190;
`results/stage7-test.tsv`, `README.md` "Seventh stage"). The key stays at 28 values and every line above
stands as printed, with `?` where it was. Lines 6 and 7, supported letters only:

    6  ietaghim?t???u?deimbarlamentoinuesiuero
    7  delpontific?t?lme?gli?loperseineedeualae

What the failed stage leaves as leads, not letters:
- `pi` = o: the script's choice from this leaf, and the c. 269r pair gives o at 5 of 7 places. If it held,
  line 7 would have `pontifico t` and line 11 `buoga`; neither is read here. My note: the eye's guess
  `pontificat[o]` (of the pontificate) needs a where the script and the pair give o, so that gloss in the
  interpretation above is weaker than it looked.
- `rc` = e and `N` = m were proposed and are not supported by the pair (a, s there).
- `boxbar`, `u`, `theta` have under one place of votes in lines 4–5 and 10–12, so no value was proposed.
- `litta` (line 4) depends on two columns the readers dispute; a path that runs line 4 on into line 5
  reads `lieua` there. The interpretation "Litta" above should be read with that doubt.

**Open (as of the seventh stage):** line 6 and the second half of line 7 do not yet read as words; the
readers are weakest there (12 and 8 doubtful tokens for reader M).

### Reading update, lines 6–7, six readers (2026-11-19)
**This is a reading update and nothing more.** Lines 6–7 were held-out text in the failed seventh stage and
their decode had been seen. What follows is post hoc for the key: it adds no evidence for any value, tests
nothing, and `key-v2.tsv` stays at 28 values. No shuffled-table control was run, because no bar could be
registered.

Two fresh readers, N and O, transcribed the two lines under guide revision 2 (they agree at 0.842 by unit).
`lattice652_67.py` lines them up with J, K, L, M and runs the c. 652r lattice on these two lines
(`results/c652-67-six.txt`: every column, its votes and shares). J–M's names were brought to revision-2
names by shape rulings only (`rename-r2.tsv`). Revision 2 splits the long-barred q off as `qxl`; a
revision-1 `q` therefore counts half `q`, half `qxl`, and a revision-1 `qx` half `qx`, half `qxl`, never
settled by value. The six-reader merge keeps a sign at 73 of 80 places (0.912); all six agree outright at 36.

    6  path      ietaghim?t????u?deimbarlamentoi?uesiuero
       under ½    ^       ^         ^   ^   ^    ^ ^
       by vote   i?taghim??????u??ei?baroame?toi?de?iuero

    7  path      delpo?tifich??lme?gli?lopersei?redeualae
       under ½            ^ ^   ^            ^  ^ ^
       by vote   delpo?tif?c?t?l?e?gli?loperstti??eaeualae

`path`: the lattice's supported letters, as in the table above; `?` where no vote has a value the path can
use. `^`: a letter on the path whose signs hold under half the six votes. `by vote`: no letter model, the
letter whose signs hold half the votes or more (the two-letter value `tt` makes line 7 one longer).
Of 80 places, 67 have a supported letter (54 with half the votes or more, 13 under) and 13 are open.

**Open places, by cause (13).**
- The key has no value and the readers agree (10): line 6 `o` (place 11), `pibox` (12), `phi` (13), `pi`
  (16), `qxl` (32); line 7 `qxl` (6), `pi` (14), `box` (18), `N` (22), `qxl` (31). More readers will not
  close these; more paired text might.
- The readers disagree (3): line 6 place 9 (a q-sign under the watermark: `qxl`, `q` or `qx`), place 14
  (`N` 0.42, `H` 0.33, `M` 0.17); line 7 place 13 (`M` 0.50 against `u` 0.37). A better image might close
  these.

**Letters on the path with under half the votes (13).**
- The majority sign has no value (4): line 6 `e` (place 2, `qxl` 0.52), `t` (10, `u` 0.70), `n` (28, `qxl`
  0.67); line 7 `m` (16, `lammast` 0.50).
- The vote alone gives another letter (4): line 6 `l` where five of six read `6` = o (place 24), `u` where
  `tri` = d has 0.58 (33); line 7 `e` where `omega` = tt has 0.78 (29), `d` where `4` = a has 0.62 (34).
  Here the letter model, not the readers, chose.
- The readers are split (5): line 6 `m` 0.42 against r 0.40 (place 20), `s` 0.42 (35); line 7 `i` 0.45
  against m 0.40 (10), `h` 0.08 (12), `r` 0.37 (32).

**What changed against the four-reader rows.**
- The `n` of `pontific` (line 7 place 6), of `inuesiuero` (line 6 place 32) and of `seine` (line 7 place
  31) is gone. Both revision-2 readers, and the guide's own examples, give `qxl` there, and the key has no
  value for `qxl`: its `n`
  belongs to the short-barred `qx` of c. 44r. Whether `qxl` is `qx` written long is not known. That is a
  lead from a decode, the same kind the seventh stage could not confirm, and it is not a value.
- `barlamento` stays on the path but two of its letters do not stand on the votes: the `l` has one reader
  of six (the other five read `6`, o) and the `n` is a `qxl` place with 0.08. By vote the stretch is
  `baroame?to`.
- `pontific`: N and O both read `lam` (i) where three of the first four read `K`, so the second `i` of
  `tific` now has 0.45 against 0.40 for m. The `t` two places after the `c` in the old row is now open on
  the path (`M` 0.50 against an unvalued `u` 0.37).
- Line 6 has 40 places, not 39: N and O each count 40 signs, and with six rows the columns under the
  watermark (places 9 to 11) line up one to one.
- N and O write dots (guide 6.3) after signs 28 and 34 of line 6 and after signs 26, 31 and 35 of line 7
  (N also after 6). J–M's brief had no dot token, so dots are listed in the result file and are in no
  column. Whether they divide words is not known and no word division is read from them here.

**My interpretation, not a result.** Standing on majority votes: `del` (of the) at the start of line 7
and the letters `loper` in line 7; the `d` of `dei` (of the) in line 6 is a tie, `tri` 0.50 against `A` 0.50. `parlamento` (parliament, or talk) and `del
pontific…` (of the pontiff, or of the pontificate) remain possible readings and are weaker than section 4
printed them: each needs `qxl` to be n, and `parlamento` also needs an `l` that five readers of six do not
see. Line 6 before `dei` and line 7 after `loper` still do not read as words. No name, date or event has
been checked outside.

## What is new here
- A partial reading of an undeciphered memorandum of 1573 (section 4), on a test registered before the decode.
- A 28-value key for a cipher with no published key.
- Two words of the c. 44r note that its own clear text does not yield to the readers.
- A partial reading of a line that has no decipherment: it concerns something done "with … participat…" and
  "of Frumento".
- A place where the cipher slip holds more than its period translation.

None of this has been checked against the Ambrosiana's manuscript catalogue or the literature on Borromeo's
correspondence beyond the gate search.
