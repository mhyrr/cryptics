# Coverage check during the frozen controls

2026-10-20. Independent verification review, confirmed on the main thread. No additional search run.

| region or list | what the repository actually records | pointer |
|---|---|---|
| Arbitrary K2 <=11, first width <=41 | Bourdeau's recorded exhaustive-K2 attack, CLAIMANT tier; not a new test here | puzzle `README.md:55`, especially 65–66 |
| First width <=15, K2 lengths 12–15 | experiment 03's validated/target region; it explicitly leaves first width>=16 with these K2 lengths open | `../03-target-h1/README.md:19` |
| First width <=15, K2 lengths 16–17 | experiment 21's validated/target region | `../21-dc-method/README.md:12` |
| Bourdeau's phrase attack | his own recorded 6.6M entries, first widths 8–40; no demonstrated membership of every dossier-derived phrase | puzzle `README.md:68`, CLAIMANT tier |
| Experiment24's actual target | 5,284 active numeric keys, K2 lengths 18–28, first widths 12–22 | `../24-phrase-seeded/README.md:52` |
| Larger phrase metadata | 8,534 guesses, lengths 8–32; the wider 2–30 first-width run was development on three plants, not wider target coverage | `../24-phrase-seeded/README.md:50` |
| Experiment26's proposed target | original active keys plus one-swap neighbours; K2 lengths 18–28, first widths 12–22, full 615-letter T1 | `README.md`, frozen `control-plan.json` |

Thus **first widths>=16 with K2 lengths 12–17 remain outside our validated target region**. The supplied-K2
isolated controls improve evidence for the K1 stage, but do not fill this blind-target gap. Inactive phrase
lengths 8–17/29–32 and first widths outside12–22 are not covered by experiment 26. Earlier evidence must be
cited per region, with its own conventions, plaintext preparation and recovery limits.

Do not say that the entire phrase list is spent. A negative experiment 26 result would cover its finite active band and
pipeline, not all contextual phrases, all widths, or all historical systems. This audit does not expand the
frozen target grid; another band requires its own declared plan and passing controls.
