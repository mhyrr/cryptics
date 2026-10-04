# 02 — key extensions found on f. 198, frozen for a held-out test

## Question
Five signs in f. 198–199 are missing from Tomokiyo's Cipher 4 table or read differently from
it. Do the values proposed from f. 198 hold at every occurrence there (criterion 4), and do
they hold in a *different* Cipher 4 letter transcribed afterwards?

## Method
`kwic.py` lists every occurrence in both readers with decoded context (`kwic.txt`). Values
were judged by reading every occurrence, not only the ones that first suggested them.
Extensions are frozen in `extensions.tsv` and applied by `decode_v1.py` (upper case in the
output marks an extension value).

## Result on f. 198 (in-sample)
| Sign | Value | Fit |
|---|---|---|
| 21. (q + dot) | que | 19/19 |
| 21_ (q + dot below) | qui | ~6/7 |
| 2H (reader B) | que | 6/7; A merges 2H and 2+ ("me") as "24+" |
| H | ne | 4/4 |
| Σ / ε | o | 9/9 |

## Held-out test 1: f. 87–88 (Pérez, 13 Sept 1578), 2026-10-03, `heldout_f87_v1.txt`
The letter is mostly clear (about 84 cipher tokens, on f. 87r–v only), not "casi toda en
cifra" as Ochoa's note was taken to mean. One blind reader (frozen at commit before decoding).
- **Base key: confirmed independently.** The cipher on f. 87r l. 12 decodes "don alonso de
  sotomayor"; f. 88r names "Don Alonso de Sotomayor" in clear.
- **Extensions: inconclusive (underpowered).** Each occurrence was judged by reading:
  - 21. = que: 2/2 ("lo que", "aquellas partes").
  - 21_ = qui: 1/2 ("no quiere" fits; "QUIsto" reads better as "visto", so possibly a misread 17_).
  - H = ne: 0/3 clear (l. 19 run unread; l. 44 unclear).
  - Σ = o: 1 unclear.
  - 2H: no occurrence.
  Too few occurrences to apply the ≥ 80% rule.

## Held-out test 2: f. 123r (Philip II to Vargas Mexía, 20 Oct 1578), 2026-10-03, `heldout_f123_v1.txt`
Same rule: blind transcription (frozen before decoding), `decode_v1.py` unchanged, each
extension consistent at ≥ 80% of its occurrences. An extension with fewer than 3 occurrences
(in both held-out letters together) is reported as untested. About 300 cipher tokens. The letter
decodes as continuous royal Spanish ("y yo os agradezco la buena inteligencia…", "será bien que
vos procuréys de entender diestramente lo que en el negocio huviere passado… y las personas que
intervenían… y aun si pudiéssedes aver algunos papeles o cartas…").

## Verdict across both held-out letters
| Extension | Held-out fit | Verdict |
|---|---|---|
| 2H = que | 13/13 (f. 123) | **PASS** |
| H = ne | 3/3 (f. 123) | **PASS** |
| Σ = o | 6/8 (one misfit, "de [Σ]visarme" needs a; one unclear) | **FAIL (strict)**: 75%; 6/7 excluding the unclear case. Mostly holds |
| 21. = que | 2/2 (f. 87); the royal letter writes que as 2H | untested |
| 21_ = qui | 1/2 (f. 87) | untested |

The base key is confirmed independently by f. 87 ("don alonso de sotomayor" in cipher; the name in
clear on f. 88r). The f. 198 reading stands on: base key (confirmed); 2H and H (held-out pass);
Σ (mostly); 21. and 21_ (in-sample only, 19/19 and ~6/7).
