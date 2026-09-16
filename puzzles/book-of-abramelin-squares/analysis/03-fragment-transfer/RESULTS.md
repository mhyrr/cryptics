# 03 — Transfer of fragments between seed families

Five fixed folds. Each donor group has one total vote, divided among its compatible letters. At least three donor groups, two observed context letters and 90% agreement required. Added-after-frames rows isolate the incremental predictions; the combined row includes frame predictions too.

| Control / mask / method | Correct / predicted | Coverage | Baseline correct on same cells | Exact tasks |
|---|---:|---:|---:|---:|
| orbit_shuffled / cells / fragments | 1/6 | 1.3% | 2 | 0/55 |
| orbit_shuffled / cells / fragments_added_after_frames | 0/2 | 0.4% | 0 | 0/55 |
| orbit_shuffled / cells / frame_then_fragments | 382/390 | 82.8% | 76 | 19/55 |
| orbit_shuffled / gnomon / fragments | 0/0 | 0.0% | 0 | 0/55 |
| orbit_shuffled / gnomon / fragments_added_after_frames | 0/0 | 0.0% | 0 | 0/55 |
| orbit_shuffled / gnomon / frame_then_fragments | 25/28 | 2.1% | 8 | 0/55 |
| orbit_shuffled / orbits / fragments | 4/4 | 0.7% | 4 | 0/55 |
| orbit_shuffled / orbits / fragments_added_after_frames | 4/4 | 0.7% | 4 | 0/55 |
| orbit_shuffled / orbits / frame_then_fragments | 4/4 | 0.7% | 4 | 0/55 |
| original / cells / fragments | 4/16 | 2.2% | 4 | 0/81 |
| original / cells / fragments_added_after_frames | 2/4 | 0.5% | 2 | 0/81 |
| original / cells / frame_then_fragments | 557/595 | 80.2% | 103 | 18/81 |
| original / gnomon / fragments | 0/0 | 0.0% | 0 | 0/81 |
| original / gnomon / fragments_added_after_frames | 0/4 | 0.2% | 0 | 0/81 |
| original / gnomon / frame_then_fragments | 99/110 | 5.1% | 24 | 0/81 |
| original / orbits / fragments | 2/10 | 1.2% | 0 | 0/81 |
| original / orbits / fragments_added_after_frames | 2/10 | 1.2% | 0 | 0/81 |
| original / orbits / frame_then_fragments | 2/10 | 1.2% | 0 | 0/81 |
| planted_fragments / motif_centers / fragments | 320/320 | 100.0% | 41 | 80/80 |
| planted_fragments / motif_centers / fragments_added_after_frames | 319/319 | 99.7% | 41 | 79/80 |
| planted_fragments / motif_centers / frame_then_fragments | 319/320 | 100.0% | 41 | 79/80 |
| shuffled / cells / fragments | 1/1 | 0.1% | 1 | 0/81 |
| shuffled / cells / fragments_added_after_frames | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / cells / frame_then_fragments | 19/139 | 18.7% | 26 | 0/81 |
| shuffled / gnomon / fragments | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / gnomon / fragments_added_after_frames | 0/0 | 0.0% | 0 | 0/81 |
| shuffled / gnomon / frame_then_fragments | 31/197 | 9.2% | 29 | 0/81 |
| shuffled / orbits / fragments | 1/4 | 0.5% | 2 | 0/81 |
| shuffled / orbits / fragments_added_after_frames | 1/4 | 0.5% | 2 | 0/81 |
| shuffled / orbits / frame_then_fragments | 1/4 | 0.5% | 2 | 0/81 |
| symmetric_original / cells / fragments | 2/10 | 2.1% | 1 | 0/55 |
| symmetric_original / cells / fragments_added_after_frames | 0/2 | 0.4% | 0 | 0/55 |
| symmetric_original / cells / frame_then_fragments | 388/392 | 83.2% | 70 | 17/55 |
| symmetric_original / gnomon / fragments | 0/0 | 0.0% | 0 | 0/55 |
| symmetric_original / gnomon / fragments_added_after_frames | 0/4 | 0.3% | 0 | 0/55 |
| symmetric_original / gnomon / frame_then_fragments | 86/96 | 7.2% | 20 | 0/55 |
| symmetric_original / orbits / fragments | 0/8 | 1.5% | 0 | 0/55 |
| symmetric_original / orbits / fragments_added_after_frames | 0/8 | 1.5% | 0 | 0/55 |
| symmetric_original / orbits / frame_then_fragments | 0/8 | 1.5% | 0 | 0/55 |
