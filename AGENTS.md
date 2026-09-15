# AGENTS.md — operating rules for this repository

Read `README.md` for what the project is. This file is how to work in it.
`STRUCTURE.md` says where files go.

---

## Vision

Most writing about famous unsolved texts is a genre: a claimant announces a
decipherment, the press amplifies, the field shrugs, nobody updates. This
repository exists to be the thing that survives that cycle: a catalog careful
enough that someone can check it, and, for the puzzles we actually attack, a
research record disciplined enough that a wrong hypothesis dies on the page
instead of living on in a blog post.

Two products, each complete on its own:

1. **The catalog.** A scored, sourced list of the greatest unsolved texts,
   ranked two ways: as a reader would rank them, and by where a modern effort
   could plausibly make progress. A rigorous "this one is a hoax" or "this one
   is open by design" is a full success for an entry.
2. **The deep dives.** For a small number of puzzles, a multi-session attack
   that leaves behind a canon of what is known, an append-only record of what
   was tried, and a list of live hypotheses each with a stated test.

## Rules

### 1. Source everything, tier everything

Every load-bearing factual claim carries a URL and a tier: `PRIMARY` (the
object, a facsimile, a critical edition), `SCHOLARLY` (peer-reviewed or
academic press), `SECONDARY` (encyclopedic), `CLAIMANT` (a proposed solution
written by its proposer), `POPULAR` (journalism, blogs). A claim you could not
verify goes under `## Unverified claims`, never dropped, never quietly asserted.

### 2. Your training data is not a source

You will remember things about the Voynich manuscript. Some of them are wrong,
and the literature has moved since your cutoff. Web search or fetch every
claim that a score depends on. If you recall a decipherment claim and cannot
find it, say so under Unverified claims.

### 3. Say "contested," don't pick a winner by vibe

Where the field is split, record the split and who holds each position.
"Reported, not established" is a legitimate and frequently correct thing to
write. The catalog's `status` vocabulary exists for this: `unsolved`,
`partial`, `contested`, `solved`, `likely-hoax`, `likely-noise`.

### 4. State what a solution would have to do, before proposing one

Every catalog entry and every deep dive carries a "What a solution would have
to do" section. It is written before any hypothesis, and a hypothesis is
judged against it. This is the crank filter. A reading that explains one folio
and hand-waves the other two hundred is not a reading.

### 5. Hypotheses die on the page

In a deep dive, `hypotheses.md` lists every hypothesis with a status
(`open`, `supported`, `weakened`, `refuted`, `superseded`) and the test that
would move it. When a test is run, the result goes to `research.md` (dated,
append-only) and the status changes. Refuted hypotheses stay listed. Nothing
gets deleted to look tidy.

### 6. LLMs interpret, code computes

Any claim of the form "the distribution of X is anomalous," "these two
passages match," "this key decrypts N% of the text" comes from a script in
`puzzles/<slug>/analysis/` that someone else can rerun, with its output
checked in. A language model's impression of a statistic is not a statistic.

### 7. Calibrate against the solved cases

The catalog keeps solved cases (`status = "solved"`) on purpose. Before
trusting a score or a method, ask what it would have said about Copiale,
Zodiac 340, Trithemius Book III, or the Soyga tables before they fell.

### 8. Stop at a clean wall, and name it

Every deep dive ends somewhere: an undigitized witness, an untranscribed
folio, a question of taste, a text that is probably noise. When you hit that,
record what the wall is and what would breach it in `NEXT.md`, then stop. A
precisely named wall is a finished result. A partial answer with its wall named
beats a confident wrong one.

### 9. Don't solve during cataloging

While building or scoring the catalog, do not attempt readings. If you find
yourself testing a substitution on Voynich folio 1r, you have left the
catalog and entered a deep dive. Open one with `/focus` and do it there, where
the record will be kept.

## Session discipline

- **Start of session:** read `NEXT-SESSION.md`. If a puzzle is in focus, read
  its `NEXT.md`, then `canon.md`, then `hypotheses.md`. Do not read
  `research.md` end to end; search it.
- **During:** findings land in the right file as they happen, not at the end.
  Is this true → `canon.md`. How I learned it → `research.md`. What I now
  suspect → `hypotheses.md`.
- **End of session:** run `/session-close`. It rewrites the puzzle's `NEXT.md`
  and the top-level `NEXT-SESSION.md`. A session without a handoff loses its
  value to the next one.
- **Commits:** small and by file. Stage by name. Never amend after a failed
  hook. `catalog/INDEX.md` is regenerated, not edited; commit it with the
  entries that changed it.

## Subagents

Catalog research fans out well: one agent per category, each writing entries
from the template, each told what is and is not theirs. Deep-dive analysis
also fans out: one agent per hypothesis test, writing to `analysis/`. Reading
and synthesizing results stays on the main thread, because the judgment
about what a result means is the work.

Every dispatch prompt points at this file, `rubric/RUBRIC.md`, and the
relevant template. It does not re-brief.

Dispatch research and drafting agents on **Opus**, not the main-thread model,
and tell them not to spawn agents of their own. The first sweep on this repo
burned the monthly spend limit in minutes when six Fable agents each fanned
out again. Verification fetches per entry: two or three, aimed at the facts
that drive the scores.

## Tooling

Python 3.11+ standard library for the catalog scripts. A deep dive that needs
more gets its own `uv`-managed environment under `puzzles/<slug>/analysis/`
with a `pyproject.toml`, and its README says how to run it. Keep dependencies
minimal; if the standard library can do it, use it.
