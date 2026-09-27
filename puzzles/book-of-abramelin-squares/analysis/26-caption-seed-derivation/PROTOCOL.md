# 26 — Derive each seed from its caption. Pre-registration

Frozen 2026-09-27. Greg approved the design. This file, `cohort.py`, its
outputs and the three instruction files are committed before any nomination.
Each later step (nominations, entries manifest, raw readings, scorer, the
scoring run) is committed before the step that depends on it. Nothing here
is edited after a step runs; corrections go in the README under a dated
heading and are labelled post hoc.

## The claim under test

Each square is its caption translated through the Frankfurt *Sylvae
quinquelinguis* (1596 A–S, `bsb11762465`; 1595 T–Z, `bsb10314207`;
PRIMARY). The caption's subject, looked up as a German headword, yields one
of the entry's printed forms: a Hebrew transliteration mostly, sometimes
Greek or Latin. That form, respelled by a fixed rule, is the top row (the
seed). Experiment 25 established symmetry and checkerboard filler blind. If
most seeds follow from their own captions, the construction is described
at the level Reeds described Soyga: a stated procedure reproduces the text,
and the remainder is measured authorial choice.

New since experiments 14, 18 and 20: per-grid German captions located beside
each grid (experiment 25's inventory), and dictionary entries read on the
page image by two readers instead of OCR (about 40 % recall, experiment 19).

## Exposure

- The main thread has read canon, hypotheses and experiments 14, 17, 19 and
  25's README. These show about 30 Mathers seeds with their headwords
  (experiment 19's table: NESER, CEPHIR, PETHEN, SELEG and others) and three
  Dresden readings: the 12.4 exemplar seed MILCHAMAH, its correction
  MILEHAMAH and the rebuilt row EHACARIDA (all in grid `p252-c1-g1` or its
  excluded exemplar), and APPARET for 4.3 (secondary A). Dresden seeds are
  mostly the same words as Mathers seeds: the two differ on 7.3 % of top-row
  cells.
- In this session the main thread has not opened experiment 25's
  `COLLATION.md`, `consensus.json`, `cells.json` or `readings/`, and no
  script prints a top row before the scoring run. The main thread saw the
  pages 243–245 readings (experiment 22) and the Warburg readings
  (experiment 20) in earlier sessions; secondary cohorts A and B are exposed.
- The main thread does not nominate, locate or read. Nominators, locators
  and readers are fresh Opus agents, each isolated, each writing to its own
  scratchpad folder. Their training may include printed Abramelin editions.
  Nominators are forbidden Hebrew, Latin and guesses about squares; each
  nomination carries its caption words and a reason, and the verifier checks
  for nominations the caption does not motivate.
- Design choices below that the main thread made with this exposure: the
  Latin scope, the crop rule, the agreement normalization, the candidate
  token rule and the S4 digraph list. None depends on a Dresden seed.

## Cohorts (`cohort.py` → `cohort.json`)

| Cohort | Grids | Captions from | Seeds from |
|---|---:|---|---|
| **P, primary** | 198 | experiment 25 inventory, pages 246–272, numbered, text caption | experiment 25 readers A and B |
| P-bare | 20 | chapter heading (items with a bare number: 14.2–12, 24.1–6, 25.1–2, the first 26.2) | same |
| A, secondary | 19 (+3 bare) | experiment 22 locator audit, pages 243–245 | experiment 22 posthoc collation (Sol readers) |
| B, secondary | 239 captions | experiment 18 `captions-de.json`, unchanged | experiment 20 readers A and B (Warburg print) |

The five unnumbered copyist grids (`p251-c2-g2`, `p252-c1-g3`, `p257-c3-g3`,
`p259-c2-g2`, `p265-c3-g3`) are excluded. In chapter 11 the unnumbered grid
follows a Latin note ("Sed puto fortasse sic sese habere debere") and is
probably the copyist's correction, not the exemplar; it is excluded all the
same, by the numbering rule. Numbered correction grids (11.3, 12.4, 18.3,
19.6) stay in P. Captions "Aliud", "ad idem" and similar stay in P; the
nominators resolve them to the preceding subject by rule.

## Seeds

- **P and P-bare.** The top row of the grid as read by experiment 25's
  readers A and B (`readings/A`, `readings/B`): a position is known where
  both give the same letter A–Z (after J→I). A seed with any unknown, blank
  or conflicting position is **ineligible** and listed by grid key. The rule
  applies to every numbered grid, square or not.
- **A.** Row 1 of experiment 22's `posthoc-collation.json`, the same rule
  on its `consensus` field.
- **B.** Experiment 20's rule unchanged: readers A and B give the identical
  top row with no `?` or `.` (after its J→I and letter filter).

## Nomination

Three fresh Opus nominators, isolated from each other and from every other
file. Each receives `nominator-input.json` (captions and chapter headings of
cohorts P, P-bare, A, A-bare; nothing else) and `NOMINATOR-INSTRUCTIONS.md`.
Each gives at most three German headwords per caption, with the caption
words rendered and a one-line reason. The union of the three is kept, each
nomination tagged with its nominator. `nominations.json` is committed before
any lookup. Cohort B reuses experiment 18's frozen `nominations-de.json`.

**Gate:** if fewer than half of the 198 P captions receive a nomination,
stop and report to Greg (the nomination step is the bottleneck).

## Locating entries, code first (`locate.py`)

1. Every distinct nominated headword (P, P-bare, A and B) goes through
   experiment 14's `lookup.Index.find`, unchanged: closed spelling
   operations, `-gestalt` frame stripping, one-edit OCR tolerance on keys of
   five or more letters.
2. **Running heads.** A matched headword line with y below 200 px and three
   or fewer letters is a running head ("Se", "Wa") and is dropped.
3. A headword with no remaining entry goes to a **locator agent**. Code gives
   the locator the three scans bracketing the headword's alphabetical
   position (by the sorted keys of experiment 12's headword lines). The
   locator returns scan, column and the headword line's vertical position,
   or "not in range". It reads nothing else.
4. **Crop rule.** From experiment 12's `parse_page` lines for the scan: the
   headword's column (gutter as in experiment 19), from 40 px above the
   headword line to 15 px above the first headword line more than 150 px
   below it; height bounded to 600–1,400 px and the page. If no headword
   line follows in that column, a second part is added: the next column in
   reading order (column 2, or column 1 of the next scan) from its first
   body line to its first headword line, at most 900 px. Native resolution,
   BSB IIIF image API.
5. `entries-manifest.json` (headword → volume, scan, column, box, part URLs,
   crop hashes, lookup tier or locator) is committed with the crops' hashes
   before any reader runs. Crops live in the ignored `out/` and are
   restored by `locate.py --fetch`.

**Gate:** if more than half of the P captions have no located entry for any
nomination, stop and report to Greg before reading.

## Reading entries

Two fresh, isolated Opus readers (A and B) per batch of about 60 crops read
the same crops under `READER-INSTRUCTIONS.md`. They see the crops and the
OCR's headword text only: no caption, no square, no seed, no nomination.
Per crop they record the headword as printed and, for that entry only:

- every Latin-letter transliteration printed beside Hebrew type (long s as s);
- every Greek form, in Greek letters, accents and breathings as printed;
- every Latin form given as an equivalent of the headword, excluding the
  POETICE epithet lists, the French (Gallic.) forms and example phrases.

`?` marks any doubtful letter. No normalization by the readers. Raw readings
are committed before the scorer opens them.

**Agreement.** A form counts only where both readers give it. Latin-script
forms are compared after NFKD, removal of combining marks, lower case, ſ→s,
and removal of everything but letters, `?` and single spaces. Greek forms
after NFD, lower case, ς→σ, removal of combining marks except the rough
breathing (U+0314). A form containing `?` never counts. Agreement is the
multiset intersection of A's and B's forms for the crop and column.

**Candidates.** A caption's candidates are the agreed forms of every entry
located for any of its nominations. A multi-word form gives each word and
the words joined. Latin-script candidates are the Hebrew transliterations
and the Latin forms; Greek candidates are the Greek forms.

## Derivation tiers, fixed before scoring

`norm(s)`: NFKD, drop combining marks, upper case, ſ→S, J→I, V→U, W→U,
keep A–Z (experiment 14's `exact` with diacritics stripped first).

| Tier | A seed matches a candidate when | Candidates |
|---|---|---|
| `exact` | `norm(seed) == norm(form)` | Latin-script |
| `aspirate` | `norm(seed)` equals `norm(form)` after any subset of the types SCH→S, CH→C, BH→B, TH→T, each chosen type applied to every occurrence (form tokenized left to right, SCH before CH) | Latin-script |
| **`skeleton`** (primary) | experiment 14's `skeleton` equal on both sides (SCH→S, delete H, collapse doubled letters) | Latin-script |
| `near` (secondary) | the two skeletons differ by one edit, seed skeleton of five letters or more | Latin-script |
| `greek` | `norm(seed)` is one of experiment 17's frozen `romanize.variants` of the form | Greek |
| `greek_itacist` | as `greek`, also with η and ει read as I (experiment 17's post hoc code, now declared in advance: H22's repeat) | Greek |

Tiers are reported cumulatively: exact ⊆ aspirate ⊆ skeleton ⊆ near;
greek ⊆ greek_itacist. The primary count is `skeleton` on Latin-script
candidates. Greek derivations are reported in S2, and in a declared
"all tiers" line (skeleton ∪ greek_itacist); they do not enter the decision.

## Scoring (`score.py`, run once)

- **Statistic.** The number of eligible grids whose seed matches a candidate
  of its own caption, at each tier.
- **Primary control.** Candidate sets permuted among the eligible grids of
  each chapter, 2,000 draws, `random.Random(20260927)`. This holds the
  chapter's topic fixed and tests per-square specificity. One permutation per
  draw serves every tier.
- **Secondary control.** Candidate sets permuted across the whole cohort,
  2,000 draws.
- p = (1 + draws ≥ observed) / 2,001, one-sided. Report observed, control
  mean, control maximum, p.
- **Derivations.** Every derivation with its chain: caption → nominated
  headword (nominator) → volume, scan, box → printed form → tier → seed.
- **Failures.** Every eligible seed not derived at `skeleton`, with its
  stage: F1 no nomination; F2 no entry located; F3 entry located, no agreed
  form; F4 agreed forms, no match. F4 carries flags: `near`, `greek_itacist`,
  `other_caption` (matches a candidate of another caption in the same
  chapter), `elsewhere` (matches an agreed form anywhere in the read set).
- **D3, headword identity.** Derivations whose entry's agreed printed
  headword has the same experiment 14 key as the nomination, against those
  reached through OCR-tolerant or neighbouring lines.

## Decision rule: cohort P, `skeleton`, within-chapter control

- **Seed layer derived:** at least 60 % of eligible seeds, and p < 0.001.
- **Partial:** p < 0.01 and under 60 %.
- **Not supported:** p ≥ 0.05.
- Otherwise **open**.

Minimum: 100 eligible seeds, else **too few seeds**.

**Forecasts, stated so they can miss.**
- Greg's: 35 % (20–50 %).
- Mine: **25 % (15–35 %)**, verdict partial. Reasons: the caption-free
  ceiling is about 45 % of seeds (experiment 17: 56 exact OCR matches of 232
  at about half recall, plus near matches); nominators reach the printed
  headword for perhaps 55–65 % of those; and Dresden's top rows carry copying
  noise that the skeleton tier does not absorb. Experiment 20's per-square
  rate was 17 of 205 with OCR candidates and one nominator; image reading
  and three nominators should roughly double to triple it.

## Secondary tests, declared now

- **S1, centre half-word.** Cohort P, n × n grids with odd n ≥ 5: the first
  (n+1)/2 letters of the central row, read left to right and right to left,
  all positions known by the seed rule. Same candidates, tiers and controls;
  a grid counts once. Also the full central row, forward and reversed,
  where it is not a palindrome. Motivation: Kollatsch's inner words MAIAM,
  TSIPPOR, BEHEMOT (CLAIMANT, experiments 06–07) and APPARET/AERE under the
  caption "In der lufft" (Dresden 4.3).
- **S2, language columns.** Derivations by the column of the matching form:
  Hebrew transliteration, Greek, Latin; overlaps shown.
- **S3, Warburg replication** (cohort B): caption c/k against Warburg square
  c/k, experiment 18's nominations unchanged, candidates from this
  experiment's readings, the same tiers, controls and decision rule; also
  without chapter 5 (experiment 11 development data).
- **S4, spelling rule.** For each Latin-script derivation up to `skeleton`,
  every digraph of the printed form (sch, ch, ph, th, bh, dh, gh, kh), every
  other h and every doubled letter is marked kept or reduced by the
  assignments that reproduce the seed; a choice that differs between
  assignments is ambiguous. Counts per type test whether the reduction is a
  rule or a tendency (PETHEN and CEPHIR keep their h).
- **Cohorts A and P-bare** are scored the same way and reported as
  descriptions. P-bare's within-chapter control is degenerate where a
  chapter's captions are identical; only the across-cohort control is read.

## Verification

After the run a fresh-context Opus verifier recomputes every count from the
raw files with its own script, and looks for leakage (did a nominator or
reader see a seed?), tier bugs and double counting. Its findings go to
`VERIFICATION.md`; any correction is labelled post hoc.

## Dispatch plan

3 nominators; up to 4 locators; 2 readers per batch of about 60 crops; 1
verifier. Expected about 28 dispatches, cap 40. The reader count is fixed
when the manifest is frozen and reported before the first reader batch.

## Stop conditions

- A clean wall is named, not worked around: an entry absent from both
  volumes, captions whose subject has no headword, readers unable to agree
  on Greek.
- The two gates above stop the run for Greg.
- No threshold, tier or control changes after any seed is seen. New ideas
  go to a new pre-registered experiment.

## What would not follow

"Derived": the seed layer is described by a stated procedure; the
nominators' choices remain a human-level step, and the procedure is not
shown to be the compiler's. "Partial": captions select seeds for a measured
share; the rest is mapped by failure stage. Neither result bears on the
interior letters.
