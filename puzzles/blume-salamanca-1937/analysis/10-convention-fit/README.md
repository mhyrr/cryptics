# 10-convention-fit — does a period writing convention explain 08's misfits?

## Question
Does any period writing convention explain the misfits that `08` found? In T1: X 6 vs 1 expected, U 16 vs 30,
M and P high. In T2: F 7 vs 1 expected, and no X. This experiment computes letter-count fits only. It attempts no
decipherment.

## Pre-registered readings
Copied verbatim from the dispatch brief before anything was run. Not edited afterwards.

- A convention "explains" a misfit if, at its pre-set parameters, the telegram's p ≥ 0.2 AND |z| < 2 for that misfit letter (X for T1, F for T2). A convention that only reaches it inside the rate sweep is "possible at a tuned rate", which is weaker, and the README says so.
- If g2 (X for stop) explains T1 and leaves T2 at p ≥ 0.1 (T2 has no X, which needs ~0 stops in 160 letters; report P(0 X) in T2-length plants), "X is the stop sign" becomes the leading account of T1's X.
- If only g6 or g7 explains T1's X, the X's are nulls or content; positions (experiment 09) and the type diagnostics must then separate them.
- If no generator explains T2's F, the F excess stays unexplained and is carried to stage 2 as a constraint, not dropped.
- If the plants' IC median exceeds 0.073 for every convention, the telegrams are flatter than Spanish telegraph text, and nulls or embedded code words become live.

## Method
`fit.py` extends `08-letter-fit/fit.py` unchanged in its statistics. For each generator:
- Reference: 40 chunks of 10,000 letters from that generator, each from a random point of the held-out corpus.
- Statistic: chi-square of the telegram's 26 letter counts against the reference, `(c − n·f)² / (n·f + 0.5)`.
- Null: 500 plants from the same generator at the telegram's length. p = (plants ≥ observed + 1) / 501.
- Per-letter z = `(c − n·f) / √(n·f + 0.5)`, as in `08`.
- Also from the same plants: the index of coincidence (median, 5th and 95th percentile); P(X ≥ 6) in 615-letter
  plants; P(F ≥ 7) and P(no X) in 160-letter plants.

Every generator starts from a fresh `random.Random(20261016)`, the seed `08` used. So g0 must reproduce `08`'s
Spanish telegraph line exactly, not only within noise. The whole Spanish table is rerun at seeds 20261017 and
20261018 to show the seed noise.

**Generators.** `conventions.py` holds a copy of `01-solver/plaintext.telegram` with hooks added. It reads the word
stream from `plaintext.heldout_words`. With no hooks it consumes the random stream exactly as `plaintext.telegram`
does, and `fit.py` checks that their output is identical before it runs anything else. The baseline: articles and QUE
dropped with probability 0.7; a stop word at each sentence end (the corpus marks `.`, `!`, `?` and `;`); a spelled
quantity such as QUINIENTOSKILOS ("five hundred kilos") inserted before a word with probability 0.03. Parameters
were fixed before the first run:

| id | convention | parameters | period source |
|---|---|---|---|
| g0 | baseline: PUNTO ("full stop") | as `08` | none; context-cribs §3 lists PUNTO as a guess |
| g1 | STOP for the stop word | | one 1937 Spanish telegram (Pochat 2008, context-cribs §2) |
| g2 | X for the stop word | every sentence end | none found; "German X for a full stop" is unverified memory |
| g3 | no stop word | | none |
| g4a, g4b | spelled quantities at 2× and 3× `08`'s rate | 0.06, 0.09 per word | none found (context-cribs §2) |
| g5a, g5b | numbers as letters, replacing the spelled quantities | 0.03 per word; 2–6 digits (length uniform, first digit 1–9, the rest 0–9, all uniform); (a) A–J = 1–0, (b) QWERTYUIOP = 1–0 | **none.** The 1932 Madrid Regulations, art. 11, bar mixing letters and figures in one group, so a letter cipher had to turn figures into letters somehow. No source gives either table. |
| g6a | X nulls before transposition | an X before each letter with probability 5/615 | none. The rate was set from T1's excess, so g6a matching T1's X count is built in, not evidence. |
| g6b | random nulls before transposition | a uniform random letter before each letter with probability 0.03 | none |
| g7a | business vocabulary | before a word, with probability 0.15, a word drawn uniformly from the 31 words of the context-cribs §3 crib table | the subjects come from the 1937 interrogation (PRIMARY); the insertion rate has none |
| g7b | as g7a, with the X- and F-bearing words removed | 27 words (drops EXPORTACION, EXTRANJERA, OFICINA, FRANCOS) | as g7a |
| g8 | F for the stop word, T2 only | every sentence end | none; a symmetry check for g2 |
| g9a | g1 + g7a | | |
| g9b | g2 + g7a | | |
| g9c, g9d | g2 + g4a, g2 + g4b | | |

The crib table was written in an earlier session, before `08` found the X and F misfits, so it was not fitted to
them. g7b shows how much g7a depends on its four X- and F-bearing words. The 31 words are every upper-case word in
the table's first column: LANA, LANAS, BURGOS, HISMA, SEVILLA, SANSEBASTIAN, SALAMANCA, OFICINA, REABRIR, ABRIR,
COMPENSACION, CREDITOS, SALDOS, DIVISAS, FRANCOS, SUIZOS, PESETAS, EXPORTACION, SUIZA, ZURICH, PATVAG, HOVAG,
VICTOR, VIKTOR, OSWALD, STOP, MONEDA, EXTRANJERA, JUNTA, TECNICA, KILOS. In English: wool, wools, Burgos, Hisma,
Seville, San Sebastián, Salamanca, office, reopen, open, compensation, credits, balances, foreign currencies, francs,
Swiss, pesetas, export, Switzerland, Zurich, Patvag, Hovag, Victor, Viktor, Oswald, stop, currency, foreign, board,
technical, kilos. The list includes OSWALD (a W) and VIKTOR and
KILOS (K), although the table itself rules those out for T1 or T2. The brief says every word, so they stay in.
`fit.py` parses the table and checks it against this list.

**Italian and Portuguese check.** The two best Spanish conventions, ranked by min(T1 p, T2 p) over g1–g9 (g8
excluded because it is T2 only; ties broken by T1 p), are rerun in Italian and Portuguese. The language's own stop
word, article list and quantity words are used. X and F stops stay single letters. The crib words stay in Spanish,
because most are names.

**Rate sweep** (a separate table, labelled as tuned). A pass found only here is "possible at a tuned rate".
- g2: an X at a fraction q of sentence ends, nothing at the rest; q = 0.25, 0.5, 0.75.
- g6a: X-null rate 1, 2, 3, 8, 12 per 615 letters.
- g6b: null rate 0.01, 0.05, 0.10.
- g7a: crib rate 0.05, 0.10, 0.20, 0.30.
- g4: quantity rate 0.12, 0.15.
- g8 (T2 only): an F at a fraction q of sentence ends, q = 0.25, 0.5, 0.75.

## Run
From this folder: `python3 -I fit.py > result.txt`. It takes about 6 s of CPU. It first checks that g0 matches
`plaintext.telegram` and that the crib list matches the context-cribs table. Raw numbers go to `out/results.json`
(gitignored). The column "share of plants with IC ≤ the telegram's" was added after the first run. It draws no
random numbers, and a diff confirmed that no other number changed.

## Result
Full tables are in `result.txt`. g0 reproduces `08` exactly: T1 chi² 58 (plants median 26), p = 0.080; T2 35 (19),
p = 0.110.

**Pass rule at pre-set parameters, Spanish** (seed 20261016; the last two columns give all three seeds)

| gen | T1 p | T1 z X (6 vs E) | T2 p | T2 z F (7 vs E) | P(no X in 160) | explains T1 X | explains T2 F |
|---|---|---|---|---|---|---|---|
| g0 PUNTO | 0.080 | +5.3 (0.6) | 0.110 | +4.6 (1.1) | 0.85 | no ×3 | no ×3 |
| g1 STOP | 0.096 | +5.1 (0.6) | 0.072 | +4.4 (1.2) | 0.89 | no ×3 | no ×3 |
| g2 X stop | 0.094 | −1.8 (12.5) | 0.130 | +4.2 (1.3) | 0.06 | no ×3 | no ×3 |
| g3 no stop | 0.062 | +5.0 (0.6) | 0.126 | +4.1 (1.4) | 0.85 | no ×3 | no ×3 |
| g4a qty 0.06 | 0.074 | +5.3 (0.6) | 0.094 | +4.3 (1.3) | 0.88 | no ×3 | no ×3 |
| g4b qty 0.09 | 0.066 | +5.7 (0.5) | 0.104 | +4.2 (1.3) | 0.87 | no ×3 | no ×3 |
| g5a A–J | 0.080 | +5.0 (0.6) | 0.180 | +4.1 (1.4) | 0.82 | no ×3 | no ×3 |
| g5b QWERTY | 0.078 | +5.0 (0.6) | 0.110 | +4.8 (1.1) | 0.82 | no ×3 | no ×3 |
| **g6a X nulls 5/615** | **0.523** | **+0.2 (5.6)** | 0.130 | +4.1 (1.4) | 0.22 | **yes ×3** | no ×3 |
| g6b random nulls 3% | 0.144 | +3.5 (1.3) | 0.132 | +4.0 (1.4) | 0.72 | no ×3 | no ×3 |
| g7a cribs 15% | 0.134 | +3.0 (1.6) | 0.114 | +4.3 (1.3) | 0.68 | no ×3 | no ×3 |
| g7b cribs, no X/F | 0.062 | +5.3 (0.5) | 0.072 | +4.9 (1.0) | 0.88 | no ×3 | no ×3 |
| **g8 F stop** | – | – | **0.818** | **+1.4 (4.0)** | 0.81 | – | **yes ×3** |
| g9a STOP + cribs | 0.084 | +3.2 (1.5) | 0.102 | +4.4 (1.2) | 0.70 | no ×3 | no ×3 |
| g9b X stop + cribs | 0.074 | −1.1 (9.7) | 0.126 | +4.5 (1.2) | 0.08 | no ×3 | no ×3 |
| g9c X stop + qty 0.06 | 0.090 | −1.2 (9.7) | 0.144 | +4.0 (1.4) | 0.08 | no ×3 | no ×3 |
| g9d X stop + qty 0.09 | 0.074 | −1.3 (10.2) | 0.112 | +3.9 (1.5) | 0.10 | no ×3 | no ×3 |

Seed spread: T1 p for g6a is 0.52 / 0.48 / 0.40; T2 p for g8 is 0.82 / 0.77 / 0.87. No other generator passes at
any seed. The highest other p is g5a's T2 p of 0.206 at seed 20261017, and F there is still at z +3.8.

**The other T1 letters** (z, T1 observed vs expected)

| gen | P (35) | U (16) | S (39) | M (24) | K (2) | W (0) |
|---|---|---|---|---|---|---|
| g0 PUNTO | +2.0 (25.0) | −2.5 (30.0) | (44.7) | +2.0 | +0.8 | −0.2 |
| g1 STOP | +2.1 (24.6) | −0.8 (19.5) | −2.2 (55.3) | +2.0 | +0.8 | −0.2 |
| g2 X stop | **+4.8 (15.7)** | −1.0 (20.8) | (46.6) | +1.7 | +0.6 | −0.6 |
| g3 no stop | **+4.7 (16.0)** | −1.1 (21.0) | (48.9) | +1.7 | +0.7 | −0.4 |
| g5a / g5b | +2.0 / +1.7 | −2.6 / −2.8 | | +2.0 | **+2.1 / +2.1** | −0.4 / −1.2 |
| g6a X nulls | +1.8 (26.0) | −2.6 (30.1) | (43.3) | +1.9 | +0.7 | −0.7 |

g5b also predicts 7.8 Y in T1 (observed 2, z −2.0) and 1.8 W (observed 0).

**Index of coincidence of the plants**, Spanish, T1 length (T1 = 0.0695)

| | median range | T1's place among plants (share with IC ≤ 0.0695) |
|---|---|---|
| stop-word only: g0, g1, g3, g4a, g4b | 0.0732–0.0753 | 0.026–0.052 |
| X stops: g2, g9b–d | 0.0720–0.0736 | 0.09–0.19 |
| nulls, letter-coded numbers, cribs: g5–g7, g9a | 0.0714–0.0731 | 0.08–0.20 |

T2 (0.0710) sits at the 26th to 57th percentile under every generator. Eight of the sixteen Spanish T1-length
medians are below 0.073.

**Italian and Portuguese check.** The two best Spanish conventions by min(T1 p, T2 p) were g6b (0.132) and g6a
(0.130).

| | g0 T1 p | g6a T1 p (z X) | g6b T1 p | T2 p, all three | T2 z F |
|---|---|---|---|---|---|
| Italian | 0.004 | 0.006 (+0.4) | 0.014 | 0.09–0.15 | +3.2 to +3.3 |
| Portuguese | 0.040 | 0.076 (−0.2) | 0.106 | 0.08–0.16 | +3.3 to +3.5 |

With X nulls, Italian T1 still fails on K, V (3 vs 13), J, Y and B, and Portuguese T1 fails on K, B and P (each
z ≈ ±2.5).

**Rate sweep (tuned rates; a pass here is "possible at a tuned rate" only)**

| gen | T1 p | T1 z X | T2 p | T2 z F | P(no X in 160) | verdict |
|---|---|---|---|---|---|---|
| g2, X at q = 0.25 / 0.5 / 0.75 of sentence ends | 0.086 / 0.092 / 0.106 | +1.3 / −0.4 / −0.8 | 0.08–0.13 | +4.1 to +4.6 | 0.41 / 0.21 / 0.12 | fails at every q, on P |
| g6a, X nulls 1 / 2 / 3 / 8 / 12 per 615 | 0.194 / 0.250 / 0.425 / 0.291 / 0.242 | +2.9 / +1.7 / +1.1 / −0.8 / −1.8 | 0.08–0.13 | +4.2 to +4.6 | 0.62 / 0.53 / 0.39 / 0.11 / 0.04 | T1 X passes from 2 to 12 per 615 |
| g6b, random nulls 0.01 / 0.05 / 0.10 | 0.072 / 0.160 / 0.198 | +4.4 / +2.8 / +1.8 | 0.11–0.18 | +3.7 to +4.5 | | fails (0.10 just misses on p) |
| g7a, cribs 0.05 / 0.10 / 0.20 / 0.30 | 0.09–0.13 | +4.5 / +3.7 / +3.1 / +2.5 | 0.09–0.12 | +4.3 to +4.5 | | fails |
| g4, quantities 0.12 / 0.15 | 0.068 / 0.070 | +5.4 / +5.6 | 0.100 / 0.070 | +3.9 / +3.7 | | fails |
| g8, F at q = 0.25 / 0.5 / 0.75 (T2) | – | – | 0.269 / 0.529 / 0.798 | +3.3 / +2.4 / +1.6 | | T2 F passes at q = 0.75 only |

## Reading
*Script author's reading. The main thread judges.*

1. **T1's X: only X nulls explain it.** g6a passes at all three seeds, but its rate came from T1's own count, so the
   X match is built in. What g6a adds is this: with X accounted for, the rest of T1 fits Spanish telegraph text at
   p 0.40–0.52. The X term alone is 28 of T1's chi² of 58. X nulls at T1's rate leave P(no X in 160) = 0.22, so T2's
   lack of X does not rule out one null rule for both. Pre-registered reading 3 applies: only g6 explains T1's X, so
   the X's are nulls, or content not in the crib list. Experiment 09 (positions) and the type diagnostics must
   separate them. g7 does not explain the X: at 15% of words the crib list raises expected X only from 0.6 to 1.6.
2. **X is not the stop sign at these settings.** Pre-registered reading 2 does not fire. An X at every sentence end
   gives 12.5 X per 615, twice T1's count, and P(no X in 160) = 0.06. At half the sentence ends the X count fits
   (z −0.4), but p stays at 0.09. The reason is P.
3. **The PUNTO generator hid a third misfit, P.** T1 has 35 P. A stop word with a P in it (PUNTO, STOP) brings the
   expected count to about 25. Without one (X stop, no stop) P is at z +4.7 to +4.9 (35 vs 16). U and S point the
   other way: PUNTO predicts 30 U (T1 has 16), and STOP predicts 55 S (T1 has 39). No stop word fits P, U and S
   together. The U deficit in `08` is a by-product of the PUNTO generator, not a property of T1 alone. M runs
   +1.7 to +2.4 under every Spanish generator, and no convention moves it.
4. **T2's F: only F as a stop sign passes, and no tradition is known for it.** g8 passes at all three seeds (p
   0.77–0.87; F expected 4.0 vs 7). Its tuned variant passes only at q = 0.75. Nothing with a period source moves
   F: crib words with FRANCOS and OFICINA, spelled quantities with FRANCOS as a unit, and letter-coded numbers all
   leave z between +3.7 and +4.9. Pre-registered reading 4 does not fire on its letter, since g8 passes. But the
   only pass is the symmetry check with no source. My reading: carry the F excess to stage 2 as a constraint, and
   record "F as a separator" as the one convention that fits the counts.
5. **Each telegram's misfit is one letter.** T1 without its X's fits (g6a, p ≈ 0.5). T2 without its F's fits (g8,
   p ≈ 0.8). One over-represented letter per message, a different one in each, fits a per-message null or
   separator letter. It does not show one.
6. **IC: pre-registered reading 5 does not fire.** Plant medians run 0.0714–0.0753, and eight of sixteen are below
   0.073. T1 (0.0695) sits in the bottom 3–5% for conventions that only change the stop word. It sits in the
   bottom 8–20% for conventions that add rare letters (nulls, letter-coded numbers, crib words, X stops). T2 is
   unremarkable everywhere. T1 is a little flat for PUNTO-style text. Additive conventions remove that, but the
   IC does not separate them.
7. **Language.** Spanish stays best. X nulls do not rescue Italian (T1 p 0.006) or Portuguese (0.076). T2's F
   excess is there in all three languages.
8. **Letter-coded numbers.** No source exists for either table. Both move K the wrong way: the baseline's K comes
   almost entirely from the unit word KILOS ("kilos"), so removing spelled quantities leaves T1's 2 K at z +2.1.
   The QWERTY table also predicts W and Y that T1 lacks.

## Caveats
- The reference and the null come from the same generator, as in `08`. The corpus is held-out literary prose with
  a telegraphese transform, not real 1937 telegrams. Its sentence ends (`.`, `!`, `?`, `;`) set the stop count: about one per
  49 letters of output (g2 expects 12.5 X in 615). Real telegrams may stop less often. The g2 sweep covers that.
- g6a's rate (5/615) was fitted to T1. Its T1 pass shows that X nulls are consistent with the counts, not that they
  occurred. Letter counts carry no position, so g6a cannot tell nulls from content X. That is experiment 09's job.
- Letter counts do not change under transposition, so every result here holds for any transposition. None of it
  applies if the cipher substitutes letters.
- The crib list's 15% insertion rate and uniform choice have no source. The list includes OSWALD, VIKTOR and KILOS,
  which put W and K into the plants even though the crib table rules them out for T1 or T2. The brief said every
  word.
- g5's numbers use uniform digits. Real figures have more zeros. Zero is J in table (a) and P in table (b), so a
  zero-rich stream would add J or P. This was not tested.
- The pass rule's p is driven mostly by the misfit letter itself. The X term is 28 of T1's 58, and the F term is 21
  of T2's 35. "Explains the letter" and "the telegram fits" are not independent tests.
- With 500 plants, p moves by about ±0.05 between seeds (g6a T1: 0.40–0.52). The "best two" ranking for the
  Italian and Portuguese check separated g6b from g6a by 0.002, which is within noise. Both were run.

## Sensitivity: book 27738 excluded (added after the first result)
Experiment 09 found that held-out book 27738 (Palacio Valdés, *José*) ends in an English–Spanish glossary, and the
generator draws from it. `sensitivity_27738.py` removes the whole book from the Spanish word stream: 12.5% of
held-out letters, more than the glossary alone. It patches `plaintext.EXCLUDE` inside its own process, so
01-solver is unchanged. It reruns g0, g1, g2, g3, g6a and g8 at the same three seeds. Run:
`python3 -I sensitivity_27738.py > sensitivity_27738.txt` (about 3 s). `fit.py` now also records the plants' 90th
percentile. That draws no random numbers, and `result.txt` is unchanged.

Seed 20261016, with the book → without. "3 seeds" is the range without the book.

| gen | T1 p | T1 p, 3 seeds | T1 z X | T1 z P | T1 z U | T2 p | T2 p, 3 seeds | T2 z F |
|---|---|---|---|---|---|---|---|---|
| g0 | 0.080 → 0.014 | 0.014–0.026 | +5.3 → +5.0 | +2.0 → +2.5 | −2.5 → −2.2 | 0.110 → 0.024 | 0.024–0.034 | +4.6 → +4.7 |
| g1 | 0.096 → 0.014 | 0.012–0.016 | +5.1 → +5.3 | +2.1 → +2.3 | −0.8 → −1.0 | 0.072 → 0.012 | 0.012–0.022 | +4.4 → +4.9 |
| g2 | 0.094 → 0.034 | 0.032–0.034 | −1.8 → −1.2 | +4.8 → +4.8 | −1.0 → −1.1 | 0.130 → 0.038 | 0.032–0.056 | +4.2 → +4.6 |
| g3 | 0.062 → 0.006 | 0.002–0.008 | +5.0 → +4.6 | +4.7 → +4.7 | −1.1 → −1.2 | 0.126 → 0.046 | 0.044–0.046 | +4.1 → +4.4 |
| g6a | 0.523 → **0.210** | **0.188–0.220** | +0.2 → +0.1 | +1.8 → +2.4 | −2.6 → −2.2 | 0.130 → 0.022 | 0.022–0.030 | +4.1 → +4.8 |
| g8 | – | – | – | – | – | 0.818 → 0.659 | 0.643–0.663 | +1.4 → +1.7 |

T2's X, P and U z-scores move by 0.3 or less. Across all three seeds no z-score moves by more than 0.8.

The z-scores hardly move. The p values fall, by a factor of 1.2 (g8, T2) to 34 (g3, T1), because the glossary had
fattened the null's tail. For g0, the plants' 90th-percentile chi² falls from 45 to 39 (T1) and from 36 to 27 (T2), while the
telegrams' own chi² stays at 59 and 34. Consequences:
- Without the book, Spanish telegraph text fits neither telegram. T1 p is 0.014–0.026 and T2 p is 0.024–0.034
  under g0. `08`'s p values, and those in the Result tables above, were inflated by the glossary.
- **g6a now only just passes for T1's X**: p 0.21 / 0.19 / 0.22, so it passes at two seeds of three. With X nulls,
  T1 now fits at p ≈ 0.2, not 0.5. P rises to z +2.4.
- **g8 still passes for T2's F** at all three seeds (p 0.64–0.66). F's z is +1.7 to +1.9, close to the |z| < 2
  limit.
- Nothing new passes. Which letters misfit (X and P in T1, F in T2) does not change.
- T2 now fails at p < 0.06 under every rerun convention except g8. Its F excess carries even more of its misfit than the
  main table showed.
