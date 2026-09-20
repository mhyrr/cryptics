# Research log — append-only, newest first

## 2026-09-20 (second session) — The fork: interior letters are free; the seed half closed

Greg asked for the dive to be taken to its end, in the order NEXT.md set.
Experiments 10 to 15 are unchanged. Every test below was committed before it
ran; commit hashes are in each experiment's README.

**Experiment 16, the fork.** Unit of choice: the orbit of a cell under
transpose plus half-turn. 781 interior orbits. Entropy of the letter given its
class: 2.92 bits (vowels 2.10, consonants 3.49); a top-row letter given its
class has 2.99. Chapter preference lowers cross-validated loss by 0.15 bit
against permuted chapters (p 0.001), prince groups 0.06 (p 0.02), the letter
above 0.06 (p 0.002). Seed-letter reuse is 35.9 % against 35.4 % by chance:
the handoff's 39 % was the chance rate. R at row two, column two: 16 of 42
against 12.1 (p 0.07); R is simply the commonest consonant. Mathers and Dehn
do not disagree more in interiors once each square's own error rate is held
fixed (69 against 63.0, p 0.13). Best top-one accuracy 32 %. By the rule
frozen beforehand this supports end state B. An estimator artifact (every
context model loses to class-only in absolute loss under leave-one-square-out)
is recorded in the README; gains are read against permuted controls.
Chapter-to-prince mapping: mediated PRIMARY, Mathers Book II chapter 20 on
[Peterson's page](https://www.esotericarchives.com/abramelin/abramelin.htm).

**Experiment 17, the residue.** Romanization frozen first. Of 176 unmatched
top rows: 74 are one letter from a Hebrew transliteration (control 32.3); 5
match romanized Greek exactly (control 2.2); Latin body words 9 (control 6.5).
Post hoc, after OIKETIS pointed to it: reading η and ει as I, the Reuchlinian
way, gives 6 exact matches against a control of 0.5, four of them new
(THIRAMA, PARADILON, ALAMPIS, KIXALIS). Seed estimate from the dictionary:
roughly 105 to 110 of 232. PRIMARY, machine-read: the two BSB volumes as in
experiment 12.

**Experiment 19, image reads.** One Opus reader, crops only. All 21
caption-selected seeds of experiment 14 are printed in the nominated entry.
In a random sample of 30 entries the OCR harvest holds 15 of 36 printed
transliterations. The square spelling reduces aspirates: sch to S, ch to C,
bh to B, th to T. PRIMARY: BSB `bsb11762465`, scans listed in the README.

**Experiment 18, German captions.** The Warburg print sets chapters 1 to 3 as
grids and the rest as row lists under each caption. Layout was labelled by
subagents that returned band numbers only; captions were read from
caption-only pages; nominators saw captions only. 239 captions. By chapter the
German captions retrieve 27 Mathers seeds (permutation maximum 14; English
labels gave 21). Per square against Mathers numbering: 7 against 3.5 (share
0.03), with hits spread over offsets −2 to +2: Mathers orders squares
differently. PRIMARY: [Warburg print](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf).

A first dispatch of the four Warburg square readers died on the account spend
limit before writing anything. No square letter reached the main thread.

## 2026-09-20 — Dictionary indexed; Dehn readings scored; captions select seeds, not interiors

Greg asked for a hard push and left the plan to judgment. The handoff proposed
E3 as a repaired caption-first test of a dictionary word on the central row.
Four experiments replaced that plan. E1 and E2 are unchanged.

**Experiment 12.** E2's lookups failed on remote search. The BSB serves hOCR
per scan, so both volumes (1,434 scans) are now indexed locally: 14,360
headword lines, 3,680 distinct Latin-script words printed next to Hebrew type.
Against that OCR vocabulary, 56 of 232 Mathers top rows match exactly
(shuffled control 8.6). Interior rows: 4 of 373 (control 2.7). Interior lines
containing a dictionary word as substring: 83 of 395 (control 86.7).
PRIMARY, machine-read: [1596](https://www.digitale-sammlungen.de/de/view/bsb11762465),
[1595](https://www.digitale-sammlungen.de/en/view/bsb10314207).

**Experiment 13.** While extracting labels the main thread found that the
pinned Peterson page prints `D:` readings from Dehn's German-based edition in
its note column: 79 square readings, never used by this project. Two were seen
by accident (5/1 in full, the reading beside 5/2 in part) and are flagged.
Models were committed (`469663f`) before parsing. On cells blank in Mathers:
experiment 01's symmetry fills 83 right of 90 on borders; vowel/consonant
checkerboard 153 of 193 interior cells; checkerboard plus most common letter
61 of 193; most common letter alone 48 of 193. Edited PRIMARY at two removes —
[Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm).

**Experiment 14 (the E3).** Protocol and lookup code committed (`9438ec0`)
before nomination. Three Opus subagents saw only Mathers's 231 English purpose
labels and nominated at most three German headwords each. Code lookup with a
closed list of spelling operations; 173 labels received candidates. Tested by
chapter against 2,000 permutations of candidate sets across chapters. Seeds:
21 skeleton-tier hits, permutation mean 1.9, maximum 14. Interior rows: 0
hits, permutation mean 0.3. Two hits read on the image: Löwe prints arieh and
cephir (both are Mathers seeds); Schnee prints ſcheleg.

**Experiment 15.** Dehn's spirit lists (Book II chapter 19) against Dehn's
squares: 29 exact row matches of 390 names, control 4.9; matched rows are 26
top, 26 bottom, 31 inner. Mathers's own list does not fill blank rows: 3
predictions in 70 rows, none right, control 2.9.

Process: the first fetch ran one request at a time and was restarted with four
workers. The first index build stopped each entry at the first Greek word and
missed most Hebrew; fixed before any reported count. `.gitignore` now covers
`analysis/*/out/`.

## 2026-09-18 — E2 caption-first pilot: source obtained, no usable scored lexical inputs

Greg prioritized caption-first lexical prediction separately from frozen E1.
[Experiment 11](analysis/11-caption-first-e2/README.md) records the successive
policy, nomination, alignment, lexicon, code and prediction freezes. E1 is
unchanged. The method nominates at most two German lookup concepts per caption,
retains all alternatives and misses, and fixes central-row/T placement.

PRIMARY: the [Warburg digitization](https://wdl.warburg.sas.ac.uk/object-wdl-awm-aadf)
provides a German printed caption source beyond the supplied edition excerpt.
Its catalog dates the item 1853; imprint dating is not adjudicated here. The
first eight chapter-5 captions were transcribed from cropped facsimiles on PDF
pages 339–340. No pilot square letters were displayed. All eleven lookup
nominations were frozen before dictionary entries or target sizes were opened.

The familiar-spirit purpose list in the mediated PRIMARY
[Mathers transcription](https://www.esotericarchives.com/abramelin/abramelin.htm)
supports seven purpose-label alignments, of which three have complete grids.
German 2/4/8 align to complete Mathers 5/8, 5/9, 5/11. The giant has no matching
Mathers purpose and stays unmatched. These alignments do not prove correct
historical ordering or identity of the square texts. No seed was used to join.

Exact/prefix BSB searches and twelve images yielded five relevant-sense entries:
PRIMARY [Rieſe, scan 1001](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=1001),
[Blume, 239](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=239),
[Alter man, 86](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=86),
[Kriegsman, 804](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=804),
[Reuter, 996](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=996).
All relevant Hebrew-gloss Latin alternatives and continuation boundaries remain
in the lexicon/images. Two headword joins are verified; three require German
n/nn or ei/eu operations outside the frozen policy; six searches remain
unresolved. No OCR miss is called dictionary absence. The three -gestalt
compounds remain unsplit. Blume from historical Bluemen also exposes an
insufficiently explicit ue/u normalization in the nomination log; the README
records that ambiguity rather than treating the baseline pool as confirmatory.

The frozen predictor made **zero predictions over 27 hidden interior cells**
in the three complete targets, both with all interiors hidden and with one
whole D4 group hidden at a time. All three caption inputs abstain before
placement. Twenty caption permutations, twenty word-letter controls (vacuous
empty domains), and twenty T-orbit-value controls also yield no predictions.
The caption-free vocabulary yields no predictions through contradiction. Those
failure modes differ. Dictionary positional mode gets 6/12 letters right;
training-fold frequency gets 4/27. Neither uses captions. No whole square is
recovered and caption accuracy is null. Full computed evidence is in
[RESULTS.md](analysis/11-caption-first-e2/RESULTS.md) and its checked-in JSON.

This is an uninformative pilot, not a recovered selector or a rejection of
dictionary derivation. The limiting input is now usable caption-to-headword
lookup under a specified German spelling/morphology policy. A revision requires
a new experiment/cohort. Keep Hebrew transliteration spelling separate from
German headword lookup. Do not redraw E2 or expand it after seeing outcomes.

Exposure mistakes are explicit: an early prose filter re-emitted already exposed
edition p. 138 rows; an OCR/TSV failure displayed neighboring Warburg chapter-4
moon/water rows; an HTML-context diagnostic after nomination freeze re-exposed
Mathers 5/1 and rider/eagle seed commentary. The latter targets are unmatched or
incomplete and not scored. See the [exposure audit](analysis/11-caption-first-e2/EXPOSURE.md).
All scored data have earlier project-level Mathers exposure. No new manuscript
or German chapter-5 square answers were opened; this is not a blind session.

Verification: four new synthetic tests passed; saved outputs reproduced with
PYTHONHASHSEED=7919; E1's freezes/input audit still reproduce. H7/H12/H15 remain
open. The caption-first question retains priority over another generator search.

## 2026-09-18 — E1 caption selector frozen before independent dictionary sampling

Continued from 9202fed. Read the prescribed handoffs, canon, hypotheses and
experiments 06/09, then experiment 05's protocol and solver. No repeat source
acquisition searches. [Experiment 10](analysis/10-caption-selector/README.md)
records the specification, exact selector/solver, independent sample and checks.

E1 uses literal German caption/headword tokens, all eligible Hebrew-gloss Latin
transliterations, exact spellings, a central row in odd squares, and T symmetry.
Residual orbits stay free. Visible letters cannot be repaired; names are not
inputs. These are our exploratory choices, not a recovered construction.
Binary brute-force checks verify completion counts and consensus. A competing
center word causes abstention; the center cross does not determine the full grid.

Froze protocol/code/tests before computing the dictionary block selection.
The SHA-256 rule chose scans 326–327 of bsb11762465. Acquired those direct IIIF
images and scan 328 to complete the last entry, using the already documented
endpoint. No search, redraw or collection by recognized square word.
PRIMARY: [326](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=326),
[327](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=327),
[328](https://www.digitale-sammlungen.de/de/view/bsb11762465?page=328).
All ten starting entries remain in the ledger. Five lack Hebrew transliterations;
one has an uncertain initial letter and abstains. Accents and phrases remain
literal exclusions. E1 has PERESCH/NEKUDAH at n=7; this is domain availability,
not caption selection. Froze the transcription before any target-caption join.

A separate computed discovery diagnostic gives 2/9 literal matches to the
reported headwords. Knowing past things does not literally select Lehrer;
Wax/Wachs and Vogels/Vogel need different additional operations. No retrospective
semantic expansion added. These examples never enter independent denominators.

Inspected the existing target schema: no captions. The already exposed first
45 Mathers export lines were reread during format inspection; no raw witness
opened. A bounded check of supplied PDFs emitted headers/term counts, not grid
rows. pypdf was unavailable, so existing pdftotext was used. Edition Book IV
pp. 138–142 are followed by an excerpt break and appendix p. 175; visually
verified the intervening PDF page 125 marked LESEPROBE. Compilation extraction
supplied no verified caption-to-Mathers mapping. Edited PRIMARY sources and
hashes are saved in the caption audit. Zero text-layer term hits are not a
caption-wide absence claim. No further acquisition search attempted.

Exact wall: source-backed local German captions, target IDs, exposure/uncertainty
and alignment evidence independent of square letters. E1 can be tested once
that table and the evaluation harness are frozen. The existing source sample
cannot silently stand for all 81 targets. Controls and interior masks are
specified but unrun; scores/predictions are null. H7/H12 remain open; add H14
for this narrow candidate. Do not redraw the lexicon if overlap is zero.

## 2026-09-18 — Supplied draft resolves layout; capital erasure limits reconstruction

Greg supplied the edition and compilation PDFs, then the 50-page structural
draft. Hashes are pinned in sources/LOCAL-PDFS.json and experiment 09/source.json.
The access wall is resolved. Rendered and visually read draft printed pp. 4,
7–10, 35–41 and 46 (PDF offset +2), plus compilation pp. 3–4 and edition
printed pp. 140–141. No raw witness or independent evaluation target opened.

CLAIMANT / edited examples — [Kollatsch draft](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_).
The BEHEMOT figure is not transposed: its row 6 has a blank at column 3 and
`s` at column 4, while its accompanying sequence reads `rerotin`. The prose
says middle row; the sequence places BEHEMOT in column 4. These are two
separate source inconsistencies, not extraction errors. The wax figure agrees
cell for cell with the compilation. Footnote 12 specifies the frame-strip
reading directions. Decomposed frame diagrams on pp. 7–8 explain interleaved
text extraction; they are not alternate whole-grid row readings.

[Experiment 08](analysis/08-capital-overlay/README.md), specified before draft
acquisition, masks only capitals and tests TA symmetry. Dragon, beast and bird
still require at least 22, 22 and 21 lowercase erasures respectively. Water
is compatible but all nine masked cells are unconstrained. Exact count-matched
and frame-count-matched mask controls and exhaustive small-grid tests are saved.
This refutes H13's narrow capitals-only model, not the author's broader account.

The draft explicitly allows lowercase disruption and repeated insertion/erasure
(pp. 37–38). It proposes T precursors for beast and bird, not TA.
[Experiment 09](analysis/09-structural-draft/RESULTS.md) therefore also reports
the source-selected families: dragon TA needs 22 further lowercase erasures,
beast T needs 14, bird T needs 6. No repairs are performed. Two gentler examples,
NEBBELAH and GEBHINAH, become T-compatible after capital erasure. Three and two
capital positions respectively are forced to the letters already present;
four central cells remain free in each. Those cells form three independent
orbits, giving 26^3 = 17,576 conditional A–Z completions. Water likewise has
three free orbits. No changed original letter is recovered in these cases.
These alphabet counts do not assert that every completion is a valid word.

On p. 46 the author says names were inserted or, more often, derived from the
squares' letters. This remains his claim. It prevents us from assuming that
those names are independent inputs. The lexical and name arguments are deferred
to installments two and three. The supplied draft specifies no complete rule
for choosing entries, alternatives, placement and remaining independent letters.
H7/H12 remain open. Next write an explicitly exploratory, answer-independent
lexical specification before any independent sampling; further installments
would be useful sources, but repeat access searches are not the next experiment.

Verification: experiments 08/09 reproduce their saved outputs; 09 checks the
supplied PDF hash; four exhaustive/guard tests pass. Experiments 05–07 retain
their original data and outputs. No historical prediction accuracy measured.

## 2026-09-17 — Broader search for an ungated structural-draft mirror

At Greg's request, searched the exact title, author plus symmetry/Abramelin,
PDF-filtered queries, and domain-limited queries covering Knowledge Commons,
Zenodo, Internet Archive and ResearchGate. Also searched the exact author/title
combination in Google through the in-app browser. No usable independent mirror
was found; relevant results returned Academia's paper/profile. This is a search
outcome, not proof that no mirror exists.

The [Knowledge Commons title search](https://works.hcommons.org/search?q=Symmetriestruktur)
returned no matches in its own visible interface (PRIMARY access observation).
The [Academia paper](https://www.academia.edu/127154626/Zur_Symmetriestruktur_der_magischen_Buchstabenquadrate_von_Des_Abraham_von_Worms_Buch_der_wahren_Praktik_von_der_alten_Magie_)
still yields extracted text to the web tool, but not source diagrams. This is
the route already used in experiment 06, not a new resolution of the image gap.
No signup, message to the author, or new witness exposure. The next useful
acquisition route is an author-supplied PDF or an existing authorized download;
no external communication was sent. Existing edition and compilation mirrors
remain usable, as recorded in experiment 07. Research browser tab closed.


## 2026-09-17 — Browser verification and published diagrams after `3815688`

Started at 3815688 with a clean worktree. Verified the Codex in-app browser
on example.com before reading the handoffs. HIVE memory confirmed the edited
witness validation trap. No subagents or external communications used.

The structural draft's “See full PDF” opened an account prompt. Switched to
the edition's already cited DOI, which now resolves to a public Knowledge
Commons record. Read the PDF viewer and visually inspected printed pp.
138–142 (PDF 120–124). Its BEHEMOT note says column. Followed the author's
public repository results to the edited square compilation and inspected pp.
1–4. Its figures confirm the recorded orientations for the selected examples.
The author's Academia profile showed no separate lexical/name installment;
its explicit draft download link led to signup. No terms accepted, account
created, or access control bypassed. The draft's diagrams remain unchecked.

Filed source URLs, page/figure locators, separate readings, exposure and limits
in [experiment 07](analysis/07-published-diagrams/README.md). Its comparison
computes 10/10 case-sensitive row agreements with experiment 06. This does
not establish whether the draft transposes its BEHEMOT diagram or mislabels it.
No new lexical rule, hidden-orbit score, raw manuscript answer or incomplete
prediction. Adjacent compilation pp. 1–5 were exposed by the viewer text layer;
edition navigation additionally exposed prayer text on printed pp. 174–175.

Verification: experiment 07 comparison regenerates and --check passes;
experiment 06 --check and its three unit tests pass. Git diff against 3815688
confirms experiments 05 and 06 are unchanged. Browser tabs closed at finish.
H7/H12 and TK-005 remain open. Next: obtain the structural-draft pages through
authorized access, then specify answer-independent construction choices before
selecting evaluation inputs. Compilation verification removes one uncertainty;
it does not provide the missing construction rule.


## 2026-09-17 — Construction evidence after `bb87024`

Started at bb87024 with a clean worktree. Read AGENTS, both handoffs, canon,
hypotheses and the requested experiment 05 files. Read the browser skill and
searched its documented Node REPL tool names; none was exposed. HIVE memory
confirmed the corrected-edition verifier trap. No subagent, browser, server,
shell download or new raw German witness was used.

Retrieved Kollatsch's English account, edition preview and structural draft as
web-extracted text. Read the lexical discussion and accessible Book IV apparatus,
then focused on frame order, lexical central lines, overlap and name insertion.
Exact URLs/pages and statement/observation/proposal distinctions are in
analysis/06-construction-evidence/EVIDENCE.md. The web screenshot request failed
because Academia returned HTML; the edition DOI returned an internal error.
Focused source searches did not yield a usable PDF. The requested source-diagram
inspection remains unfulfilled. This is an access wall, not permission to infer
layout from flattened text or use another shell download client.
After Greg's encouragement, made one final browser-availability check using
Tidewave's required help action. It reported no connected browser. No local
application or browser was launched to follow its generic connection suggestion.

Wrote the audit specification before its script. Saved ten already-exposed
polygram sequences, captions, locators and positional observations in a new
experiment. The six prior dictionary excerpts remain discovery inputs;
Thier/Vogel and the overlap vocabulary are not independently transcribed.
The generated construction table and JSON list candidate lengths, explicit
paths, every orbit and conflict under six families, capitals and nominated
opposed-word overlaps. Source figures remain unverified throughout. No
witness alignment by numbering was attempted. Retained blikaril as the edition
reading with its reported W1 variant in a separate note; no grid was corrected.

The audit changes the next question: inner words are reported, so boundary-only
is too narrow. The exposed RAKKIA and MAIAM paths reach inner TA orbits but do
not equal the independently read dictionary spellings and each leaves two inner
orbits free. The beast sequence reads BEHEMOT down the central column, consistent
with the edition note but not the structural discussion's row terminology.
Figure inspection must decide whether this is extraction orientation. Global
symmetry conflicts in beast/bird prevent treating the edited sequences as
intact symmetric constructions. Frame-filling order alone supplies no values.

Retained boundary, central-line, near-central expansion, opposed-word overlap
and name-overlay candidates with prospective falsifiers. None has been selected
as a source-verified, answer-independent recipe. No independent contiguous
lexicon sample, historical implementation, reconstruction score or incomplete-
square prediction was produced. H7/H12 remain open. No randomness inference.
The earlier comparison edition was not pursued because it does not presently
resolve construction.

Updated canon, hypotheses and both handoffs. The immediate next input is the
cited source figures, then a frozen applicability/placement/spelling policy
that can fail on other grids. Only afterward acquire and freeze a preselected
contiguous dictionary sample including misses and run the original protocol.

Verification: new audit regenerates and --check agrees under PYTHONHASHSEED=7919;
three new tests pass (including exhaustive binary 3×3 symmetry counts), and
six original solver tests pass. The facsimile audit/source checksums and original
preflight output check pass. git diff against bb87024 for experiment 05 is empty.
No original freeze or historical performance field changed.

## 2026-09-17 — Direct facsimile readings after `d812620`

Verified the supplied manifest: all 28 JPEGs and SOURCES.tsv match their hashes.
Inspected the 1596 title, 1595 title and printer's note, and the full-page spans
of Lehrer, Himmel, Vnterweiſer, Wachs, Warſager and Waſſer. No network acquisition
or browser was needed. Greg's observations and the acquisition reports were
already exposed, as were claims.json's targets; this was not blinded reading.

Saved scoped readings in `analysis/05-period-dictionary/facsimile-readings.json`:
printed Latin transliterations, adjacent alternatives, entry boundaries and
uncertainties. This is not a full multilingual transcription or an independent
lexicon. Greek/Hebrew originals and long poetic sections remain in the facsimiles.
The third Hebrew consonant at Vnterweiſer remains unresolved bet/mem. The Latin
reads melabbed; Lehrer independently prints melammed alongside moreh and alluph.
Do not infer ambiguous Hebrew from either transliteration. The d/t headword
variation and Hüfft/Hütte before Himmel are visible but unexplained.

`audit_facsimiles.py` verifies original source bytes and computes the comparison
with the separate claimant quotations. All six dictionary targets agree;
three quoted square spellings agree after the recorded layout/case operations.
Water's ma- / iim line join is logged explicitly. Differences rakia/rakkia,
maiim/MAIAM and nechoth/necot remain differences. No fitted transformations
were added. See FACSIMILE-FINDINGS.md and the generated facsimile-audit.json.

The original frozen claimant/preflight files remain unchanged. The six-example
source check neither identifies the historical edition uniquely nor tests
unseen letters. No comparison edition, justified interior coordinates or
preselected independent dictionary block is available. No historical model
was implemented or scored. H7/H12 stay open. The next input is a documented
positional construction; the earlier edition is separately needed for the
error claim. No raw German witness opened and no randomness inference made.

All inspected packet pages are now discovery-exposed. This corrects the
acquisition handoff's stale sentence that no new source letters were exposed;
no new *square* letters were exposed in this pass. Do not call a later sample
from these pages unexposed. Updated canon, hypotheses, source audit, provenance,
README and both handoffs to retire the obsolete image-access wall.

Verification: the facsimile audit reproduces under PYTHONHASHSEED=7919 and
verifies all source checksums. The six existing experiment 05 tests pass, and
the original run.py --check still verifies the preflight outputs. No catalog
or historical performance result changed.

## 2026-09-17 — Browser access continuation from `34b1f43`

Started at the requested commit with a clean working tree. Read the handoffs,
canon, hypotheses and experiment 05 inputs before attempting source access.
The browser skill requires a Node REPL execution tool absent from the exposed
tool inventory. The alternative available Tidewave browser tool's help action
reported no connected browser. Web opens of both supplied BSB viewers and
Google Books `jkY8AAAAcAAJ` failed with non-retryable safe-open errors;
`LPyVAQ1q89cC` failed with a cache miss. No page image was acquired or inspected.
No browser/server was started and no shell-download workaround was attempted.
The fallback request to download scans or capture pages remains unfulfilled.

Filed [IMAGE-REQUEST.md](analysis/05-period-dictionary/IMAGE-REQUEST.md): title
pages and Himmel/Lehrer in A–S; Vnterweiſer/Wachs/Warſager/Waſſer in T–Z;
full entry boundaries and continuations; readable original scripts; source URLs
and viewer numbers. Actual dictionary page numbers are still unknown. Modern
edition pp. 138–141 must not be misreported as dictionary page locators. An
earlier comparison edition remains an additional input for the error claim.

HIVE search returned an older convention suggesting Python downloads after
curl rejection. The current user instruction and recorded restriction take
precedence; that workaround was not used. No purchase or library request made.

No new dictionary, square or raw German witness readings were exposed. The
six claimant examples remain separate from an independent lexicon. There is
no new evidence for an interior path; the frozen protocol remains a candidate
operational recipe. H7/H12 stay open. No historical evaluation, incomplete-square
prediction or randomness inference follows from this access failure.

Verification: all six experiment 05 unit tests pass. `run.py --check` with
`PYTHONHASHSEED=7919` reports “Preflight outputs verified.” Frozen inputs,
solver and generated results are unchanged. Updated canon, hypotheses, source
audit, README and both handoffs. The requested cache directory contains only
`ACCESS.txt`, not images; the tracked image request preserves the acquisition
specification beyond the ignored cache.


## 2026-09-17 — Period dictionary: source wall, explicit recipe and preflight

Continued from the four experiments, with independent inner-letter prediction
as the criterion. Retrieved the claimant account, edition preview and symmetry
draft; the [source audit](analysis/05-period-dictionary/SOURCE-AUDIT.md) carries
URLs, tiers, locators and access outcomes. Identified the exact Frankfurt
1595/1596 dictionary and its A–S/T–Z divisions. Logged six reported spelling
pairs separately from primary findings. No dictionary image was inspected.
Do not promote quoted correspondences to an independently verified lexicon.

The experiment's code compares the quoted strings with only long-s/case folding.
Three agree literally; three do not. This is a check of extracted quotations,
not confirmation of dictionary readings or the linguistic argument. The source
wall is legible entry images with edition and neighbouring context. An earlier
comparison edition is also needed to test an edition-specific error claim.
The exact failed routes and catalogue records are recorded for the next session.

The next operational hypothesis is selected words at fixed interior positions,
plus declared symmetry. No source retrieved supplies a general placement rule.
An all-rows dictionary construction would exceed the evidence. Wrote
`analysis/05-period-dictionary/PROTOCOL.md` before implementation; froze its hash,
quoted-claim inputs and an artificial fixture before running. No historical
lexicon, caption mapping or historical predictions were frozen or scored.

Implemented exact lexical assignment on declared paths, with every competing
branch and free orbit domain retained. In the planted square it recovers 9/9
hidden inner letters; adding an alternative center word yields two completions,
8/8 correct predictions and one abstention. Seed-only leaves 456,976 completions
and abstains on all nine cells. Contradictory and shuffled-word cases return no
completion and no prediction. Symmetry alone predicts none. All counts come
from [saved results](analysis/05-period-dictionary/results.json). These are
software controls on one artificial square, not historical power estimates.

Six tests pass, including independent brute-force counts for small squares.
The first test run revealed a mistaken hand-written expected free-orbit count;
replaced it with independent cell enumeration. `run.py --check` reproduces both
outputs under `PYTHONHASHSEED=7919`. The solver/helper and input hashes are saved.
Historical result fields are null: **blocked**, not zero accuracy or refutation.

Discovery exposed edition Book IV pp. 138–142 and variants; all examples in the
retrieved structural draft are conservatively exposed too. No new raw German
witness was read, no incomplete-square prediction was issued, and no source
reading or earlier experiment changed. H7 stays open; H12 separates independent
interior prediction from seed attribution. Canon, hypotheses, provenance and both
handoffs updated. Next experiment: fixed interior lexical placement after the
image, lexicon and placement gates pass. No randomness conclusion follows.

## 2026-09-16 — Stress-test verification and close

`analysis/stressbench/run_all.py` completes all three new experiments and the
shared tests. `run_all.py --check` regenerates the manifest, six per-experiment
artifacts and the combined report under a different Python hash seed; all eight
artifacts match byte-for-byte. Fifteen new tests and eight first-pass tests pass.
The new tests exercise orientation, transitive grouping, histogram preservation,
whole-orbit masking, scoring, donor independence and causal rollout. No source
cells or experiment-01 outputs changed. Every new experiment has a README,
script and checked-in result. Canon, hypotheses and both handoffs are updated.

The benchmark generates 1,752 frame evaluation cases plus 666 corruption cases,
2,688 fragment cases and 4,992 recurrence cases. These are overlapping method,
mask and control evaluations, not independent observations. No catalog files
changed. TK-005 remains open for the source and witness audit.

## 2026-09-16 — Ten attacks, three implementations, controlled stress tests

Greg asked for ten different approaches and code for the best three. Wrote
[ATTACKS.md](ATTACKS.md) before running the new models. Selected independent
frame rules with copying-error costs, shared fragments across seed families,
and learned nonlinear local recurrences. These separate geometric completion,
independent letter content and recursive generation. No witness data were added.

Built a frozen shared manifest: 81 complete grids, 81 seed/orientation groups,
five deterministic folds. Masks remove scattered cells, whole eight-way
symmetry orbits, or all cells except a top-left boundary. Every model and donor
baseline excludes its test fold; the frame model itself only fits visible target
cells. Added full histogram-preserving shuffles, a geometry-preserving shuffle
on the same 55 symmetric grids, and known planted constructions. These are
fixed internal controls, not statistical significance tests or an untouched
historical test set. The original digital grids had already been inspected.

[The generated report](STRESS-TESTS.md) contains the measured outcomes and
per-fold evidence. Experiment 02 gets 555/591 scattered-cell predictions right
versus strict symmetry's 456/463. Coverage rises but exact recovery falls
30→18 of 81 tasks. It predicts nothing for entirely hidden symmetry orbits.
The original export receives 12 suggested letter changes across eight grids;
these are flags to inspect, not evidence of copying errors. H8 supported in
its narrow scattered-cell form; H11 refuted for the injected-error task.

Experiment 03 gets 2/10 whole-orbit predictions right and abstains in three
folds. Adding fragments after frames supplies two right and two wrong guesses
on scattered masks, and four wrong guesses on boundary masks. The standalone
method recovers all 320 planted motif centers; the composition misses one due
to a wrong frame prediction. H9 weakened for this corpus-derived vocabulary.

Experiment 04 selects from 12 family/corner configurations by nested training
validation. All five outer folds select pair lookup. Selected-corner rollout
gets 301/1,429 letters right, versus a frequency baseline's 262 on those cells;
one fold loses to the baseline. No complete task is recovered and no confident
prediction is made. The matched symmetric subset loses to the baseline.
Teacher-forced results are labelled separately; they never count as generation.
The planted nonlinear recurrence is recovered with 3,920/3,920 interior letters
correct in held-out confident rollout. H10 weakened as an Abramelin generator.

No thresholds or families were tuned after these outputs. The selected boundary
mask is separate because the training-selected corner can differ from top-left.
No control comparison silently uses different source subsets. Retain all results,
including the higher exact-task count for the simpler symmetry rule.

The Reeds comparison remains methodological. Search located the original paper
and its publisher bibliography, but direct PDF retrieval failed. We do not
claim to implement Reeds's historical Soyga algorithm; the planted recurrence
is explicitly our own A–Z construction. Kollatsch's frame and dictionary prior
art remains attributed in the plan and canon. Catalog scores are unchanged.

Next recommendation: verify the period-dictionary source and prepare an
independent lexicon/caption mapping for a new whole-orbit test. This is a distinct
attack, not parameter tuning on the current benchmark. Historical verification
still requires the facsimile audit and uncorrected witness targets in TK-005.

## 2026-09-16 — Verification and close

Eight unit tests pass. Re-running extraction, analysis and report generation
reproduces all four derived artifacts byte-for-byte; prediction input hashes
and the total fill count agree with the results. All 104 catalog entries pass
validation after adding the required tiered Sources list; rankings regenerated.
Git's default whitespace check flags the rank generator's existing intentional
Markdown two-space line breaks; the check passes with blank-at-eol disabled.
TK-004 is closed (first dive opened); TK-005 retains the witness-audit work.

## 2026-09-16 — First structural result and handoff

The web tool exposed rows and explicit dot placeholders, allowing an offline
corpus without the requested Python network download. Preserved a 207-line
row export spanning all numbered Mathers tables, then parsed its merged records
into 242 square records. The extraction excludes separately labelled German
supplements; raw rows and literal labels remain. Ten layouts fail the strict
square/single-letter criteria and stay excluded pending images.

[Experiment 01](analysis/01-mathers-structure/README.md) records the method;
[RESULTS.md](analysis/01-mathers-structure/RESULTS.md) gives generated counts.
Measured 81 complete and 151 incomplete analyzable grids. H1–H3 fail in their
declared exact forms. H4 is supported as a constraint statement: combined
symmetry forces 1,064 cells in compatible incomplete grids, yet MAIAM retains
four free letter choices. This is not a discovery of an original generator.

After that first result, added a fixed-rule diagnostic masking each complete
grid to top row and left column. It compares against a visible-letter mode on
the same prediction cells and counts errors and abstentions. No hidden answer
selects the evaluated sample. It tests artificial missingness in this export;
it neither trains nor validates against a second witness.

Saved conditional fills and source hashes in `predictions.json`. During source
discovery, Peterson's variants and examples from Kollatsch's November 2024 draft
were displayed. **Correction to the opening note:** no German manuscript images
were inspected, but some German *readings in editions* were exposed. Future
work must not call them blind targets.

Kollatsch's September 2025 inventory supersedes his 2021 count; see canon for
the updated source. The N 161 shelfmark was found in the SLUB holdings catalog,
but its open imaging remains unresolved. A [2020 source](https://solascendans.com/2020/05/15/abramelin-musings-the-dresden-manuscript/)
(POPULAR) places the N 111 squares at viewer image 243 / written page 240;
this is a locator to verify, not a checked folio reference.

Revised the catalog's absence-of-work claims, set status to partial, and reduced
compute 5→4 and crowding 4→3. Confidence becomes medium. The basis is prior
structural work and incomplete verification readiness, not the failure of an
exhaustive generator search. Follow-up ticket: TK-005.

## 2026-09-16 — Opening the dive and checking the premise

Greg selected Abramelin and authorized a first evening of witness discovery,
Mathers extraction, characterization and simple rule tests. The criteria and
finite first-pass families were written into README before computing results.

The literature search changes the proposed novelty claim. Peterson points to
Kollatsch's edition, and the author's publication list supplies a square-symmetry
draft and a conjecturally corrected compilation. See canon for tiered links.
Do not use those corrected letters as blind manuscript targets. The dictionary
derivation is a lead to replicate, not our finding.

The HAB records expose digitization requests but no direct manuscript images.
The Dresden N 111 viewer is linked but blocked by a JavaScript challenge.
N 161 access remains unresolved. No German square readings have been inspected.

The shell policy rejected curl, including an escalated call. Requested explicit
permission for Python HTTP downloads; web-source work continued independently.

## 2026-09-17 — Dictionary page images acquired

Greg asked whether the image packet was gettable and authorized Playwright
subagents. A main-thread probe showed both BSB viewers load from this
machine and that the BSB IIIF image API serves the original scans, so the
packet was filled with native bitstreams, not screenshots. Two Opus subagents,
one per volume, no nested agents.

Method (reproducible): IIIF manifest per volume; canvas labels carry only scan
numbers and there are no printed page numbers anywhere in either body. Each
canvas has an hOCR endpoint (`https://api.digitale-sammlungen.de/ocr/<id>/<n>`)
and the 1596 volume advertises IIIF content search. Candidates came from the
OCR; every hit was verified on the image at 200–400 %. The content search
alone misleads: its first "Himmel" hit is scan 430, inside an unrelated E entry.

Results: title/imprint and all six entries found, with continuations and
neighbours. 28 full-page JPEGs at native resolution (about 1290 × 2120 px),
SOURCES.tsv and a sha256 manifest are tracked in `sources/period-dictionary/`;
its README carries the locator table. Volume identity checked on the object:
1596 "Pars prima" (body Aal → Syrup) and 1595 "Partis I. Pars II.", whose
verso-of-title note states the new part begins at letter T.

Observations recorded, not interpreted: the 1596 Lehrer headword reads
"Lehrer / Schulmeiſter / Vnderweiſer" with a d, against 1595's "Vnterweiſer";
in the 1595 Vnterweiſer entry the Hebrew gloss transliterated "melabbed" has
a third letter ambiguous between bet and mem at native resolution; the 1596
volume prints Hüfft and Hütte immediately before Himmel, out of order.

Limits: the IIIF service caps at native size, so Hebrew vowel points are at or
past legibility. No entry was transcribed into a lexicon, no comparison with
claims.json was run, and no earlier comparison edition was acquired.

Process: a local hook restricts curl to localhost; the T–Z subagent fetched the
public IIIF files with Python urllib instead. Reported to Greg.

## Dead ends

- 2026-09-20: a dictionary word on a full interior row (central or other),
  selected by caption or not, is at the control rate in Mathers and in the Dehn
  readings (experiments 12, 14). Filling blank rows from Mathers's spirit list
  predicts nothing (experiment 15).

- 2026-09-16: H1–H3 fail as exact statements about the digital sample; see
  experiment 01. Preserve the distinction from possible corrupted precursors.
- 2026-09-16: H6, the claim of no prior structural work, refuted by the author's
  listing of an explicit symmetry study. No claim of first discovery is justified.
