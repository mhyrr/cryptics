# 14 — Protocol: does the caption select the seed word, or interior rows?

Frozen 2026-09-20, before any German headword was nominated. This is the E3
asked for in the experiment 11 handoff, changed in three ways. The reasons are
experiments 12 and 13, run earlier the same day.

1. Lookup is code over a local OCR index of the whole dictionary (experiment
   12), not hand searches. E2 lost six of eleven lookups to search failures.
2. The cohort is every Mathers purpose label (231 labels, 30 chapters), not
   eight captions.
3. The target is every full row, top rows and interior rows scored separately.
   Experiment 12 found interior rows match the dictionary at the shuffled
   control rate. E1 and E2 tested a dictionary word on the central row only.
   This experiment still scores interior rows, so the caption question for
   interiors gets a direct answer at full scale.

E1 (experiment 10) and E2 (experiment 11) stay unchanged.

## Exposure

The Mathers corpus is exposed at project level. Experiment 12 printed the list
of top rows that match the OCR vocabulary, without their German headwords.
Experiment 13 showed the main thread Dehn readings for chapters 1-14. The main
thread has also seen E2's five dictionary entries. For these reasons the main
thread does not nominate. Nominations come from subagents that receive only
`labels.json` and the nomination rules below. This is not a blind-witness test.

## German nomination rules (given to the nominating agents verbatim)

For each English label nominate at most THREE German dictionary headwords, in
this order of priority:

1. the concrete entity, material or state the operation concerns, as a noun
   (or adjective for a quality) in nominative singular;
2. one direct German synonym of the same scope, if a common one exists;
3. the action as an infinitive, only when the label names an action and no
   entity, or when the action is the point of the label.

Use plain modern German spelling; the lookup code handles historical spelling.
No mythological identifications, no Hebrew, no Latin, no guesses about what a
magic square might contain. "In the form of X" means nominate X. If a label
only repeats its chapter heading, nominate from the heading. A label with no
nameable referent gets an empty list. Each nomination carries the English
phrase it renders.

## German lookup operations (lookup.py), each with its reason

Applied identically to the nomination and to the OCR headword. Development
data: the eleven E2 nominations and their retrieved headwords.

| Operation | Reason |
|---|---|
| case fold, long s to s, ß to ss, strip diacritics | typography; Fraktur OCR renders umlauts inconsistently |
| v/u, w/u, j/i, y/i, th/t | 16th-century orthographic variants of one headword (E2 rule, kept) |
| ck/k, tz/z, dt/t, c/k outside ch and sch | same class; the dictionary prints Camel and Kamel forms alike |
| collapse doubled letters | Kriegsman / Kriegsmann, Alter man / alter Mann, Reitter / Reiter |
| eu, ai to ei; ue, ae, oe to u, a, o | Reuter / Reiter; Bluemen / Blume |
| drop a final e on words longer than three letters | Schlang / Schlange, Blum / Blume |
| headword lines split on "/" | the dictionary prints synonym headwords on one line |
| strip the frame head -gestalt and one linking s, en or n | the caption frame "in X-gestalt" names X; closed list of one head |
| edit distance one on keys of five or more letters, only when no exact key exists | Fraktur OCR error (Waffer for Wasser); flagged `ocr_tolerant` |

Not permitted: semantic substitution after a miss, open-ended fuzzy matching,
splitting other compounds, any change to a Hebrew transliteration. Every
nomination's tier and every miss is kept in `lookups.json`.

## Candidate words

For each retrieved entry: the OCR tokens printed next to Hebrew type
(`hebrew_adjacent` in experiment 12). These are OCR, so long s often appears
as f. Matching treats f and s as one letter on the dictionary side only.
No reading of a page image enters this experiment; a result that matters gets
image verification afterwards and that is reported separately.

## Matching tiers, applied identically to real and control pairings

- `exact`: equal after upper case, J to I, V and W to U, long s to S.
- `skeleton`: equal after also SCH to S, deleting H, collapsing doubled letters.
- `near`: edit distance at most one on the exact form, length five or more.

## Test

Unit: the chapter. Captions and squares are not reliably aligned by number
inside a chapter (Peterson's note to chapter 5 shows three different orders),
so a row counts as a hit when it matches any candidate word of any label in
its own chapter.

- Seed test: targets are Mathers top rows (one per analyzable square).
- Interior test: targets are all full interior rows of Mathers squares, each
  also tried reversed.
- Same two tests on the Dehn readings from experiment 13, reported separately.

Control: 2,000 random permutations of candidate sets across chapters
(`random.Random(2026092014)`), keeping each set intact. Report observed hits,
control mean, control maximum and the share of permutations with at least the
observed count. Also report hits when ocr_tolerant lookups are excluded.

## Gate

If fewer than 100 labels receive at least one candidate word, report an input
failure and do not interpret the counts.

## What would count

A seed-test hit count well above every permutation supports caption selection
of the seed (H7, H15 for top rows). An interior count inside the permutation
range says captions do not select full interior rows through this dictionary.
Neither result is a generator. Exact alignment of label to square inside a
chapter is not tested.
