# Full-neighbourhood K1 results

Assisted old-failure development: exact=True, score=-4.0688, recorded CPU seconds=0.6. True K2/width supplied; excluded from fresh gates.

## Isolated K1

| stratum | records | recovered | exact | candidates | false candidates | recorded CPU seconds |
|---|---|---|---|---|---|---|
| low | 10/10 | 10 | 10 | 10 | 0 | 0.900 |
| middle | 10/10 | 10 | 10 | 10 | 0 | 2.600 |
| high | 10/10 | 10 | 9 | 10 | 0 | 4.400 |
| wrong-width | 10/10 | 0 | 0 | 0 | 0 | 2.400 |
| shuffle | 10/10 | 0 | 0 | 0 | 0 | 3.700 |

Gate: **PASS**.

## Fresh end-to-end

| stratum | records | recovered | exact | candidates | false candidates | recorded CPU seconds |
|---|---|---|---|---|---|---|
| exact | 10/10 | 10 | 10 | 10 | 0 | 737.782 |
| one | 10/10 | 10 | 10 | 10 | 0 | 699.440 |
| two | 10/10 | 9 | 9 | 9 | 0 | 676.671 |
| random | 10/10 | 0 | 0 | 0 | 0 | 802.141 |

Gate: **PASS**.

Isolated positives receive true K2 and first width; negatives are wrong-width/shuffled. End-to-end controls receive first width only, with K1/K2/plaintext withheld. Recovery permits a cyclic shift <=40 and requires >=95% agreement.

## Target and matched shuffle

No target records yet; both complete gates and a frozen protocol are required.


Recorded CPU seconds: isolated=14.000; end-to-end=2916.034; target/shuffle=0.000.

Literary-proxy controls do not establish historical preparation. Per-width calibration is conditional. One shuffle is not a p-value. A score-qualified candidate still needs independent historical/T2 validation.
