# Tier 2, step A: thresholds, fixed before any tier-2 target run

Generated 2026-10-17 10:10 EDT by `python3 -I step_t2.py thresholds-a` from `controls-T2A.jsonl` and `noise-T2A.jsonl`. Rule (README step A4): halfway between the highest noise score at that length (shuffles of one body of that length, widths 5, 8, 12, 20, 30, 45, three shuffles each) and the lowest true-text score among recovered plants of the passing bands at that length. A band passes at ≥ 8/10 plants with ≥ 90% of letters in place. Every body uses the controls of its own length. `step_t2.py target-a` refuses to run unless every check line below is in this file.

| length | w 5–8 | w 9–30 | w 31–45 | noise body | noise ceiling | noise, passing widths only | lowest true text (passing) | threshold |
|---|---|---|---|---|---|---|---|---|
| 610 | 10/10 pass | 10/10 pass | 7/10 **fail** | T1[5:615] | −5.5603 | −5.8726 | −4.3275 | **−4.9439** |
| 605 | 10/10 pass | 10/10 pass | 8/10 pass | T1[10:615] | −5.5980 | −5.5980 | −4.3133 | **−4.9557** |
| 600 | 10/10 pass | 10/10 pass | 7/10 **fail** | T1[15:615] | −5.6394 | −5.8249 | −4.1906 | **−4.9150** |
| 595 | 10/10 pass | 10/10 pass | 10/10 pass | T1[20:615] | −5.5443 | −5.5443 | −4.2452 | **−4.8948** |
| 590 | 10/10 pass | 10/10 pass | 6/10 **fail** | T1[5:595] | −5.4626 | −5.7182 | −4.2398 | **−4.8512** |
| 585 | 10/10 pass | 10/10 pass | 8/10 pass | T1[10:595] | −5.4286 | −5.4286 | −4.2006 | **−4.8146** |
| 580 | 10/10 pass | 10/10 pass | 7/10 **fail** | T1[15:595] | −5.4363 | −5.7923 | −4.2055 | **−4.8209** |
| 575 | 10/10 pass | 10/10 pass | 8/10 pass | T1[20:595] | −5.4676 | −5.4676 | −4.4177 | **−4.9427** |
| 155 | 10/10 pass | 7/10 **fail** | 0/10 **fail** | T2[5:160] | −4.4540 | −5.8781 | −4.3170 | **−4.3855** |
| 150 | 10/10 pass | 8/10 pass | 0/10 **fail** | T2[10:160] | −4.4591 | −4.6826 | −4.4625 | **−4.4608** |
| 145 | 10/10 pass | 6/10 **fail** | 0/10 **fail** | T2[15:160] | −4.2888 | −5.6971 | −4.2028 | **−4.2458** |
| 140 | 10/10 pass | 6/10 **fail** | 0/10 **fail** | T2[20:160] | −4.1718 | −5.7808 | −4.3791 | **−4.2755** |
| 135 | 10/10 pass | 8/10 pass | 0/10 **fail** | T2[5:140] | −4.2158 | −4.6564 | −4.3810 | **−4.2984** |
| 130 | 10/10 pass | 7/10 **fail** | 0/10 **fail** | T2[10:140] | −4.2176 | −5.7263 | −4.4380 | **−4.3278** |
| 125 | 10/10 pass | 9/10 pass | 0/10 **fail** | T2[15:140] | −4.1047 | −4.3483 | −4.3855 | **−4.2451** |
| 120 | 10/10 pass | 8/10 pass | 0/10 **fail** | T2[20:140] | −4.0479 | −4.4635 | −4.2779 | **−4.1629** |

At L = 150, 140, 135, 130, 125, 120 the noise ceiling lies at or above the lowest passing true text, so the threshold as the rule draws it lies above some true texts. It is applied as written; the main thread judges.

Check lines:
```
BAND-A L=610 w 5-8: 10/10 pass
BAND-A L=610 w 9-30: 10/10 pass
BAND-A L=610 w 31-45: 7/10 FAIL
THRESHOLD-A L=610: -4.9439
BAND-A L=605 w 5-8: 10/10 pass
BAND-A L=605 w 9-30: 10/10 pass
BAND-A L=605 w 31-45: 8/10 pass
THRESHOLD-A L=605: -4.9557
BAND-A L=600 w 5-8: 10/10 pass
BAND-A L=600 w 9-30: 10/10 pass
BAND-A L=600 w 31-45: 7/10 FAIL
THRESHOLD-A L=600: -4.9150
BAND-A L=595 w 5-8: 10/10 pass
BAND-A L=595 w 9-30: 10/10 pass
BAND-A L=595 w 31-45: 10/10 pass
THRESHOLD-A L=595: -4.8948
BAND-A L=590 w 5-8: 10/10 pass
BAND-A L=590 w 9-30: 10/10 pass
BAND-A L=590 w 31-45: 6/10 FAIL
THRESHOLD-A L=590: -4.8512
BAND-A L=585 w 5-8: 10/10 pass
BAND-A L=585 w 9-30: 10/10 pass
BAND-A L=585 w 31-45: 8/10 pass
THRESHOLD-A L=585: -4.8146
BAND-A L=580 w 5-8: 10/10 pass
BAND-A L=580 w 9-30: 10/10 pass
BAND-A L=580 w 31-45: 7/10 FAIL
THRESHOLD-A L=580: -4.8209
BAND-A L=575 w 5-8: 10/10 pass
BAND-A L=575 w 9-30: 10/10 pass
BAND-A L=575 w 31-45: 8/10 pass
THRESHOLD-A L=575: -4.9427
BAND-A L=155 w 5-8: 10/10 pass
BAND-A L=155 w 9-30: 7/10 FAIL
BAND-A L=155 w 31-45: 0/10 FAIL
THRESHOLD-A L=155: -4.3855
BAND-A L=150 w 5-8: 10/10 pass
BAND-A L=150 w 9-30: 8/10 pass
BAND-A L=150 w 31-45: 0/10 FAIL
THRESHOLD-A L=150: -4.4608
BAND-A L=145 w 5-8: 10/10 pass
BAND-A L=145 w 9-30: 6/10 FAIL
BAND-A L=145 w 31-45: 0/10 FAIL
THRESHOLD-A L=145: -4.2458
BAND-A L=140 w 5-8: 10/10 pass
BAND-A L=140 w 9-30: 6/10 FAIL
BAND-A L=140 w 31-45: 0/10 FAIL
THRESHOLD-A L=140: -4.2755
BAND-A L=135 w 5-8: 10/10 pass
BAND-A L=135 w 9-30: 8/10 pass
BAND-A L=135 w 31-45: 0/10 FAIL
THRESHOLD-A L=135: -4.2984
BAND-A L=130 w 5-8: 10/10 pass
BAND-A L=130 w 9-30: 7/10 FAIL
BAND-A L=130 w 31-45: 0/10 FAIL
THRESHOLD-A L=130: -4.3278
BAND-A L=125 w 5-8: 10/10 pass
BAND-A L=125 w 9-30: 9/10 pass
BAND-A L=125 w 31-45: 0/10 FAIL
THRESHOLD-A L=125: -4.2451
BAND-A L=120 w 5-8: 10/10 pass
BAND-A L=120 w 9-30: 8/10 pass
BAND-A L=120 w 31-45: 0/10 FAIL
THRESHOLD-A L=120: -4.1629
```
