# The key line — design (2026-11-16, draft for Greg's review)

How to turn one "class A" catalogue item into a key, and how to walk the rest.
Class A is Bourdeau's label: a cipher letter survives with its period decipherment (the **pair**), and
sibling letters in the same cipher are bare. Aligning the pair gives a key table nobody has written down.

Terms, used one way throughout:
- **pair**: a cipher text and the period decipherment of that same text.
- **bare letter**: a cipher letter in the same system with no decipherment.
- **token**: one cipher sign as transcribed (a figure, a letter with its mark, a code group).
- **key table**: token → value, with a type (letter, syllable, word, null) and a status.
- **item**: one catalogue number.

## Part 1 — one item, end to end

Each stage has an output file and a stop rule. A stop is a result: it goes in the ledger with its reason.

### Stage 0 — Gate (one Opus scout, about 30 minutes, no reading)
Checks, each answered with a URL or a file:
1. **Race.** Fresh pull of Bourdeau's `catalogue.json`, his write-ups index and open pull requests; Tomokiyo's
   pages; DECODE. Is the item still open, unreserved and unwritten?
2. **The pair is real.** The decipherment is of *this* cipher text, not only "of the same system". Note its form:
   **A1** separate sheet, **A2** interlinear or marginal. (A2 aligns by position but the cipher reading is not blind.)
3. **Images.** Every page of the pair and of the bare letters is reachable, and a cipher line is legible at the
   size served. Record the URL pattern.
4. **Size.** Rough token counts: pair, bare letters. Fewer than about 150 pair tokens → skip (too little to hold out).
5. **A period key.** Does one survive (archive, DECODE)? If online, the item is a key lookup, not a key build: skip
   and note it. If offline, it becomes the outside check at stage 7.

Output: `items/<id>/gate.md` with verdict `go` / `skip: <reason>`. The main thread decides, not the scout.

### Stage 1 — Fetch
Script, not hand. Pages to `items/<id>/cache/` (gitignored); one line each in `items/<id>/PROVENANCE.md`.

### Stage 2 — Transcribe (Opus readers, isolated)
- The main thread writes a **sign guide** from one sample page: shapes and names only, no values. Frozen by commit.
- **Cipher side:** two readers per page, A top-down and B bottom-up (the es. 132 exp 09 protocol). They see the
  guide and the cipher pages. They do not see the decipherment, the other reader, or any key.
- **Plain side:** two readers transcribe the decipherment. Different agents from the cipher readers.
- `compare.py` reports token agreement per page. Disagreements stay marked; nothing is settled by vote of one.
- Stop rule: cipher agreement under 85% after one guide revision → wall "sign legibility", with the page named.

Form A2 exception: the gloss sits on the cipher line, so one image shows both. Readers transcribe cipher and gloss
as paired lines. The key's test then rests on stage 5 alone, and the write-up says so.

### Stage 3 — Align and build (Fable; code computes)
`align.py`: monotone alignment of the cipher token sequence to the plaintext letter sequence. Each token takes a
span of 0 letters (null), 1 (letter), 2–3 (syllable) or a whole word (code). Iterate: align, tabulate
token → span, re-align with the table as prior, until stable. Clear-text words inside the cipher letter are fixed
anchors. Fable's job is to supply anchors and judge conflicts; it does not assign values by hand.
Output: `key-v0.tsv` with, per token: value, type, support count, conflict count, positions.

### Stage 4 — Held-out test on the pair (the gate for everything after)
- Before the run, write the pass bar in `items/<id>/README.md` and commit.
- Build the table on part of the pair, decode the rest, compare with the period decipherment by edit distance.
  Five folds by line when there is only one pair.
- Control: the same table with values permuted within type.
- Default bar: held-out letter accuracy ≥ 85% on tokens the table covers, coverage ≥ 70%, permuted control ≤ 25%.
- Fail → no reading. Record the numbers and stop.
- Pass → freeze `key-v1.tsv` (commit hash in the ledger).

### Stage 5 — Read the bare letters
- Two-reader transcription as in stage 2. Decode by script with `key-v1`. Unknown tokens print as unknown.
- `fluency.py`: share of decoded words found in a period word list, against the permuted-key control.
- The reading is assembled only where both readers' decodes agree. English translation beside the original.
- Extending the key from bare letters: a new value needs three occurrences and no conflict, and is marked
  `probable`. A value from one context stays `unknown`.

### Stage 6 — Sense check
The decoded text must join the clear text on both sides, and its names, dates and events must fit outside
sources. Search for an edition or calendar that already prints the content; if one exists, say so.

### Stage 7 — Outside check and close
- If a period key survives offline, name the shelfmark: it is the test anyone can run.
- Files: `sources/keys/<id>.tsv`, `items/<id>/reading.md`, `items/<id>/README.md` (question, method, numbers,
  wall if any), one ledger row.
- Nothing is sent to Tomokiyo, Bourdeau or DECODE without Greg.

### Calibration before the first item (rule 7)
The aligner is tested on answers we know, with the bar set first:
1. **Synthetic:** encipher period Spanish with `vargas-mexia-es132/sources/keys/cipher3.tsv`, add reader noise at
   the rate measured in es. 132, rebuild the key from the pair, score against the true table.
2. **Real:** Saint-Goard's letter of 23 Dec 1579 and its decipherment (BnF fr. 16106 ff. 208–209, already in
   `vargas-mexia-es132/sources/`). Rebuild Longlée's cipher from that pair and score against Tomokiyo's table.
If either fails, fix the aligner before touching an item.

## Part 2 — walking the catalogue

### The ledger
`line/ledger.tsv`, one row per item, append-only in effect (rows change status, never vanish):
`id, title, cls, form (A1/A2), language, repository, status, reason, pair_tokens, bare_tokens, heldout_acc,
coverage, control_acc, key_commit, agents_used, opened, closed`.
Status: `queued` → `gated-out` | `go` → `walled` | `key-built` → `read`.

### The queue
`line/queue.py` rebuilds the queue from a fresh catalogue pull at the start of every batch:
1. Keep class A, desk-workable, not reserved, no write-up, not already in the ledger as closed.
2. Drop items whose status text shows work by others since the last pull (the diff is printed, not hidden).
3. Order by: language we can read (Spanish, French, Italian, Latin) first; then solvability high, difficulty low;
   ties broken toward items that share an archive or a cipher family with one already done.
Today's pull gives 76 candidates; the gate will cut that number, by how much is unknown.

### Batches
- **Pilot:** one item, alone, through all stages. Then stop and report cost (agents, hours, where it stuck).
- **Batches of five** after that. Gate all five first (five Opus scouts in parallel), then work the `go` items.
- **Clusters:** 21 candidates sit in the Florence Medici papers. One fetch script and often one chancery's sign
  habits serve many items, and keys from one chancery check each other. Take a cluster as a run of batches.
- After each batch: ledger, a short batch note in `research.md`, and a list for Greg of keys ready to announce.

### Who does what
| Work | Model | Rule |
|---|---|---|
| Gate scout, one per item | Opus | No reading. No sub-agents. Two or three fetches per check. |
| Readers, two per side per page | Opus | Isolated. See only the guide and their pages. No sub-agents. |
| Align, key table, held-out verdict, reading, sense check | Fable | Main thread, or one Fable agent per item that may not spawn. At most two at once. |
| Queue, ledger, scoring, comparison | scripts | Checked in, rerunnable. |

### What stops the line
- Pilot cost is out of proportion to one key. Greg decides.
- Two items in a row fail stage 4 for the same reason: fix the method before the next.
- The queue pull shows the remaining items taken.
- Any step that needs a login, a paid scan or a message to a person: it waits for Greg.

## Open decisions (Greg)
1. **Pilot item.** No. 2192 (Tierra Firme, 1554, Spanish, five letters, one deciphered in another Seville file) if
   its images pass the gate; else no. 2345 (Baldovino del Monte, Rome, 1555, Italian).
2. **Scope of the walk.** All 76, or only Spanish, French and Italian of 1500–1650 where our key families help?
3. **Announcing.** Per key, per batch, or only at the end? Earlier protects priority; later hides the method.
4. **Terranova.** Run it as a class C side track with the same tools once the aligner is calibrated, or park it.

## Changes proposed after the pilot (2026-11-17; not yet adopted, Greg decides)

From phase 0 and the pilot on no. 2911 (`research.md`, entries of 16–17 Nov 2026). Stages keep their numbers.

**Stage 0 — gate.**
1. Race: the catalogue file does not show work in progress. Run `line/taken.py` on a fresh pull of the
   `targets/*/profile.json` files and drop named ids (`queue.py --taken`) before any scout is sent.
2. Before a scout: the main thread checks by script that the image host answers and that the entry needs no login.
   Four scouts cost 606k tokens and passed no item.
3. Check 5 is run by an isolated agent when a candidate key is online, so the builder stays blind.
4. New check 6: search for a printed edition of the decipherment. If one exists it is the plain side, and no
   plain readers are sent.
5. New check 7: is the decipherment complete? Compare its length with the cipher's (signs × a letters-per-sign
   guess, lines against lines). An extract or abridgement is flagged; it needs the gap-tolerant aligner (H6).

**Stage 2 — transcribe.**
6. The sign guide carries picture sheets cut from the page, not prose alone. It is written from every hand in the
   item, not one page.
7. Before stage 3, by script: readers' made-up names for one shape are merged; doubled shapes are tested by count
   and joined where the pair is far commoner than chance; the unit decision for marks is written down.
8. The 0.85 stop rule is applied to the item's total. A short page under it is reported, not a stop.
9. Plain side: tags (`<del>`, `<ins>`, `[?]`, `[…]`) and the consensus rule are part of the pipeline. If the
   consensus keeps under 80% of the words, the plain side is unfit and the item waits for a print or a better reader.

**Stage 3 — align.**
10. The aligner must allow cipher stretches with no plain text (H6). Until it does, only complete pairs go through.
11. A degeneracy stop before stage 4: if more than 30% of valued places are null, or a fold decodes under 20% of
    its letters, report "aligner degenerate" and do not run the held-out test.
12. Log-space arithmetic moves from `items/2911/align_log.py` into `line/align.py`.
13. Calibrate at the item's own scale and shape (units, sign types, unread share, no anchors) on a synthetic pair
    before the item's first alignment.

**Stage 4 — held-out test.**
14. Control bar: ≤ 0.30 and at least 25 points under the accuracy (the scorer's chance level is 0.25).
15. A recall floor. The accuracy bar itself is open (H7): the true key scores 0.735 on 2911 and 0.79 on es. 132
    f. 255, so a fixed 0.85 fails right keys on inexact plain sides.
16. `probable` needs four supporting places.

**Queue.** 132 class A desk-workable items, 89 after `--taken`. For 1450–1700, most of what is left sits behind
the ASF host (13 items) or a DECODE login (34 items). Class A in the catalogue does not mean a pair exists: the
33 Sforza items have no decipherment on the leaf.
