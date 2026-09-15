# Rubric — scoring an unsolved text

Every catalog entry carries six scores, each 1–5. Four are the axes Greg named
(mystery, material, solvable, compute). Two more are recorded because they
change what you would actually do with an entry (verifiable, crowding). The
ranking script combines them; the weights live in `scripts/rank.py` and are
the only place to change them.

Score the text as it stands today, from sources you can cite. When two
readings of an axis are defensible, pick one, say why in the entry's "Why the
scores" section, and set the entry's `confidence` field to `low` or `medium`.

## Admission test

An entry belongs in the catalog when all three hold:

1. **Intent.** A human author or workshop appears to have constructed the text
   to carry a determinate meaning, structure, or message. Deliberately open
   art (a Mallarmé poem that means to shimmer) can enter, but scores low on
   `solvable`.
2. **Material.** Enough survives that the meaning is in principle recoverable
   from the evidence, not only from a lucky future find.
3. **Unresolved.** No reconstruction of the intended meaning has convinced the
   relevant scholarly field. "Contested" counts. "Solved but popularly believed
   unsolved" does not; it goes in `catalog/EXCLUDED.md` with the citation.

Undeciphered scripts that wait on a bilingual or on more inscriptions (Linear A,
Indus, Rongorongo, Proto-Elamite) fail test 2 and go in `EXCLUDED.md`. Known
hoaxes and forgeries go there too, with the debunking cited. Resolved cases we
keep on purpose as calibration (Copiale, Zodiac 340, Trithemius Book III, the
Soyga table algorithm) get `status = "solved"` and stay in `entries/` so the
rubric can be checked against known outcomes.

## The axes

### `mystery` — how unresolved, and how much a solution would matter

| | |
|---|---|
| 5 | Central question wide open; a convincing solution would be a notable event in its field and beyond |
| 4 | Wide open; would matter to the field |
| 3 | Partly resolved, or resolved in outline with a real residue of dispute |
| 2 | A working consensus exists with minority dissent |
| 1 | Effectively resolved; residual "mystery" is popular, not scholarly |

### `material` — quantity and quality of surviving primary evidence

| | |
|---|---|
| 5 | Complete or near-complete text, good witnesses, fully digitized, published transcription |
| 4 | Substantial text, digitized, transcription exists but with gaps or disputes |
| 3 | Substantial text but access is partial (undigitized, no critical edition, poor images) |
| 2 | Fragmentary; the surviving portion limits what any method can recover |
| 1 | A few lines, a single damaged witness, or reported only at second hand |

### `solvable` — probability that a determinate intended meaning exists

This is the axis that separates a cipher from a hoax, and an allegory from
noise. Score the probability that there is a "there" there.

| | |
|---|---|
| 5 | Near-certain: the author says so, or the structure is demonstrably non-random and purposeful |
| 4 | Likely: strong internal evidence of design (statistics, keys, paratext, contemporary testimony) |
| 3 | Open: serious scholars hold both "meaningful" and "meaningless/open/hoax" positions |
| 2 | Doubtful: the best evidence favors a hoax, glossolalia, deliberate openness, or lost referent |
| 1 | Very doubtful: strong evidence of fabrication, or the "meaning" is unrecoverable by construction |

### `compute` — plausibility that AI or computation contributes something new

Score what a well-run 2026 effort could do, not what a chatbot would say.
Ask: is the text digitized and transcribed? Is there a statistical, structural,
or combinatorial question inside the mystery? Are there large corpora of
parallels an embedding search or a language model could sweep? Is there a
concrete check (a key that decrypts, a source that matches) that would tell
you when you are done?

| | |
|---|---|
| 5 | The core question is computational (cipher, table structure, statistical fingerprint) and the data is ready; or a mass source-parallel sweep is the obvious next move nobody has done |
| 4 | Computation can settle a sub-question or eliminate hypothesis families; data mostly ready |
| 3 | Computation can assist (parallel search, quantification of prior claims) but cannot decide |
| 2 | Mostly a humanistic judgment problem; computation is a minor aid |
| 1 | Nothing to compute: the residue is taste, faith, or lost context |

### `verifiable` — could a proposed solution be recognized as correct?

| | |
|---|---|
| 5 | Yes, mechanically: a key decrypts the whole text, a formula regenerates the tables, a source matches word for word |
| 4 | Yes, by strong criteria: predicts unread portions, explains multiple independent anomalies |
| 3 | By scholarly consensus, which could form within years |
| 2 | Only by plausibility; competing readings would remain |
| 1 | Not really; any reading is as good as another |

### `crowding` — how saturated prior effort is

Higher is emptier. A fresh field is worth more than a picked-over one.

| | |
|---|---|
| 5 | Almost nobody has worked it; no dedicated monograph |
| 4 | A handful of serious treatments |
| 3 | A modest literature; the obvious approaches have been tried |
| 2 | A large literature; famous attempts by capable people have failed |
| 1 | Thousands of attempts, an active crank ecosystem, every naive approach exhausted |

## Composite rankings

`scripts/rank.py` produces two orderings and prints the weights it used:

- **classic** = mystery + material + solvable. "Greatest unsolved text" as a
  reader would mean it.
- **attackable** = classic + 2·compute + verifiable + ½·crowding. "Where could
  we plausibly make progress." This is the ranking Greg said would change the
  list, so `compute` is double-weighted.

Both are shown in `catalog/INDEX.md`. Change the weights in the script, never
by hand-editing the index.

## Confidence in the scores

`confidence = "high" | "medium" | "low"` on each entry says how well the scorer
knew the material. Low-confidence entries are flagged in the index. A second
pass on the top 50 should raise every one of them to medium or better before
the list is called done.

## Calibration

The `status = "solved"` entries are the test set. A good rubric should have
scored Copiale and Zodiac 340 as `compute = 5, verifiable = 5` before they
fell, and should score a known hoax as `solvable ≤ 2`. If the weights rank a
solved case below a hoax on `attackable`, the weights are wrong. Record any
such check in `rubric/CALIBRATION.md` when there are enough entries to run it.
