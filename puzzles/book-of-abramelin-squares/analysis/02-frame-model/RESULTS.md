# 02 — Frame rules and error tolerance

Fixed 5% error channel; ties abstain. Accuracy is against withheld digital cells. The symmetric-original and orbit-shuffled controls use the identical subset. Corruption results are in results.json; no source reading was changed.

| Control / mask / method | Correct / predicted | Coverage | Baseline correct on same cells | Exact tasks |
|---|---:|---:|---:|---:|
| orbit_shuffled / cells / frame_mdl | 382/388 | 82.4% | 76 | 19/55 |
| orbit_shuffled / cells / global_exact | 419/419 | 89.0% | 84 | 30/55 |
| orbit_shuffled / gnomon / frame_mdl | 25/28 | 2.1% | 8 | 0/55 |
| orbit_shuffled / gnomon / global_exact | 473/473 | 35.3% | 91 | 0/55 |
| orbit_shuffled / orbits / frame_mdl | 0/0 | 0.0% | 0 | 0/55 |
| orbit_shuffled / orbits / global_exact | 0/0 | 0.0% | 0 | 0/55 |
| original / cells / frame_mdl | 555/591 | 79.6% | 101 | 18/81 |
| original / cells / global_exact | 456/463 | 62.4% | 85 | 30/81 |
| original / gnomon / frame_mdl | 99/106 | 5.0% | 24 | 0/81 |
| original / gnomon / global_exact | 615/696 | 32.6% | 138 | 0/81 |
| original / orbits / frame_mdl | 0/0 | 0.0% | 0 | 0/81 |
| original / orbits / global_exact | 0/0 | 0.0% | 0 | 0/81 |
| planted_frames / cells / frame_mdl | 413/415 | 76.9% | 7 | 9/60 |
| planted_frames / cells / global_exact | 0/0 | 0.0% | 0 | 0/60 |
| shuffled / cells / frame_mdl | 19/139 | 18.7% | 26 | 0/81 |
| shuffled / cells / global_exact | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / gnomon / frame_mdl | 31/197 | 9.2% | 29 | 0/81 |
| shuffled / gnomon / global_exact | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / orbits / frame_mdl | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / orbits / global_exact | 0/0 | 0.0% | 0 | 0/81 |
| symmetric_original / cells / frame_mdl | 388/390 | 82.8% | 70 | 17/55 |
| symmetric_original / cells / global_exact | 419/419 | 89.0% | 79 | 30/55 |
| symmetric_original / gnomon / frame_mdl | 86/92 | 6.9% | 20 | 0/55 |
| symmetric_original / gnomon / global_exact | 473/473 | 35.3% | 91 | 0/55 |
| symmetric_original / orbits / frame_mdl | 0/0 | 0.0% | 0 | 0/55 |
| symmetric_original / orbits / global_exact | 0/0 | 0.0% | 0 | 0/55 |
