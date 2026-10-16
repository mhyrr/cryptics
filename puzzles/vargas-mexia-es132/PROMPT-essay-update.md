# Session prompt: fold the 2026-10-16 first readings into the essay

Paste everything below the line into a fresh session, from the repo root `/Users/mhyrr/work/cryptics`.

---

/focus vargas-mexia-es132

**Goal.** Revise `essay/DRAFT.md` to use the new first readings of 14 royal cipher letters (exp 09, 2026-10-16). The angle
is unchanged: a file catalogued in 1844 as "imposible descifrar" holds the King's side of the Pérez scandal. History
leads; method follows. The new material must serve that angle. It must not turn the essay into a survey of 1578–79
diplomacy.

**Rule change (Greg, 2026-10-16).** `PROMPT-essay.md` says "The essay adds no new findings." That rule is lifted for the
findings in `canon.md` § "First readings of unread royal letters (exp 09)". Nothing else is lifted: no claim enters the
essay unless it is in `canon.md` with a confidence label, and Rule 2 (training data is not a source) applies to every
background fact.

## Read first (in this order; do not re-derive)
1. `essay/DRAFT.md`, all of it, including the editorial section at the end, "Proposed modifications from the 2026-10-16
   readings". That section is an approved starting outline (A1–A6, B1–B5, C). Follow its confidence labels, its
   corrections (B5) and its warnings: do not imply Pérez leaked anything; "teatino" stays unidentified in the narrative;
   do not repeat the claim that "teatino" meant Jesuit in the 1570s.
2. `canon.md` (new section at the end), `hypotheses.md` H6, H17, H18, H19.
3. `analysis/09-unread-letters/README.md` (Result) and the readings: `reading_f41.md` first, then `reading_f185.md`,
   `reading_f62.md`, `reading_f54.md`, `reading_f89.md`, `reading_f37.md`, `reading_f132.md`, `reading_f85.md`.
4. `analysis/08-borja-crib/README.md` (Result): the calibration figure every new quotation is qualified by.
5. `essay/CLAIMS.md`, `essay/QUOTES.md`, `essay/EDITOR-NOTES.md`, `PROMPT-essay.md` (form, register, reader, length).
6. Greg's tools: `~/work/writing/.claude/commands/editor.md` and `slopwriting.md`; `~/.hive/SOUL.md` (Voice).

## What to add (beyond the existing outline)
**N1. f. 41: Pérez as the King's secret channel, four weeks after the murder.** This is the most important new item. The
outline was written before it was read. In late April 1578 the French resident ambassador proposed that Philip and Henri
III join to punish their rebels and check Elizabeth. He asked to deal through **Antonio Pérez**. Pérez reported every
step to the King and carried the answer back ("Antonio Pérez me dio parte de todo"). Vargas was told to feign ignorance
in Paris. Evidence: two blind readers, 92% / 94% agreement, "Antonio Pérez" decoded at the same five places; Paz K 1546
independently lists the league negotiation. Place it where the draft moves from the murder (March 1578) toward the
months of trust. It shows that the King still used Pérez for his most secret French business after Escobedo's death.
State it as what the letter shows. Do not argue a theory of the murder from it. The ambassador is not named in the
cipher: write "the French ambassador in Madrid", and give Saint-Goard only as "by date" in a note.
**N2. Optional texture, one or two sentences at most:** Saint-Goard's audience of June 1578 (f. 62: Philip will judge "por
las obras", by deeds), or Maintenon's of September (f. 89). Use one only if it helps the reader see Pérez's world. If
neither does, leave both out.
**N3. A1–A3 from the outline:** the Lansac leak (now also H18, with Longlée as a candidate) and the calibration figure.
A4 (pilgrim) and A5 (f. 37) stay optional, as the outline says.

## Method section
In "For historians and cryptographers", add exp 09 to the record. List the letters read for the first time; give the
agreement range (80–97%, two witnesses each); the external checks (Paz for ff. 37, 41, 185, 202; f. 171's clear sentence
matching f. 174's cipher); the calibration (exp 08: 86% precision, ~63% recall); and the wall (f. 213, show-through).
The `marknorm.py` normaliser and its controls get one sentence.

## Process
1. **Plan first.** Before writing prose, show Greg a short plan: which items go in, where (section and paragraph), and
   roughly how many words each. Wait for his OK.
2. Then write. Keep the length within `PROMPT-essay.md`'s range. If a new item pushes the essay over, cut elsewhere and
   say what you cut.
3. Every new quotation: Spanish, then English at once; add a `QUOTES.md` row (Q42 onward), a `CLAIMS.md` group (AG
   onward; add AL for f. 41) and a note. Renumber the notes.
4. Delete the editorial "Proposed modifications" section from `DRAFT.md` once its items are handled. Record each
   decision (used / not used / why) in `EDITOR-NOTES.md`.
5. Run Greg's editor pass and the slop check on the changed paragraphs only.
6. Commit by file with a plain message. Do not publish. Publication waits for Greg's full-draft review.
