# Direct-neighbour results

## Assisted development diagnostic

| old stratum/trial | base-key rank at true width | assisted exact recovery |
|---|---|---|
| 1/9 | 1717 | False |
| 2/0 | 2916 | False |
| 2/3 | 4876 | False |
| 2/5 | 3336 | False |
| 2/7 | 394 | False |

Both the true first width and base phrase were supplied. These are not blind controls.

## Development benchmark

| supplied first width | score | CPU seconds | role |
|---|---|---|---|
| 22 | -4.0437 | 44.868 | exact old-plant recovery |
| 19 | -5.7969 | 83.309 | cost check |

These development rows are excluded from the fresh gate.

## Fresh per-width controls

The first width is supplied. Keys/plaintext are not supplied. Minimum distances are from the original list.

| stratum | trials | recovered (>=95%, shift<=40) | exact | false candidates | scan CPU seconds | total CPU seconds |
|---|---|---|---|---|---|---|
| exact | 10 | 10 | 10 | 0 | 587.658 | 596.058 |
| one | 10 | 10 | 10 | 0 | 680.765 | 689.065 |
| two | 10 | 9 | 9 | 1 | 971.411 | 987.411 |
| random | 10 | 0 | 0 | 0 | 917.970 | 969.970 |

Control gate: FAIL (>=8/10 exact and one, zero false candidates across all 40).

These controls use literary-proxy plaintext. Near-list success does not establish arbitrary-key coverage.

## Post-search acceptance diagnostic

| control | score | true-text score | shifted agreement | exact K2 | exact K1 |
|---|---|---|---|---|---|
| two/8 | -4.5505 | -4.0688 | 0.4683 | True | False |

This explains a failed control. It is not a fresh test or a target result. No settings changed.

## Exploratory T1 grid and matched shuffle

| body | widths complete | best quadgram score | candidates | scan CPU seconds | total CPU seconds |
|---|---|---|---|---|---|

NOT RUN: the complete control gate failed. No target protocol was frozen.

Recorded fresh-control CPU seconds: 3242.504; target/shuffle CPU seconds: 0.000.

One shuffle is not a p-value. All target widths must complete. A candidate still needs independent T2 validation.
