# Editorial record

2026-10-05. Outline approved; Greg requested a distinct deslopify and compression pass, preserving useful quotations.

## Independent editor

One Opus review, via the installed Claude CLI because Opus is not available in the native subagent selector. The prompt included `~/work/writing/.claude/commands/editor.md` verbatim, the complete first draft, and the compression brief. Tools were disabled; no subordinate readers or writers were used. The editor was asked for criticism, not rewritten prose. First draft preserved in commit `1cf1591`.

# Editor's report: "Into My Hands," first draft

## Register and effect

The register you're reaching for is narrative, warm and exact. The draft mostly hits **exact**. It reaches **narrative** in three places and **warm** in about four sentences. In my Fiona read, I leaned in at the opening, the cipher table, all of "Stay where you are," and the last line. I leaned back through most of "Without the key" after the table, the second half of "Madrid, March 1578," and nearly all of "A paper in Paris."

The main problem is not flourish. It's the narrator repeatedly stepping in front of the story to disclaim. Most sections end on a negative:

- "cannot establish… do establish"
- "Nothing in them warrants"
- "without claiming to know"
- "Nor does… establish"
- "as far as we can read it"
- "do not establish," then "remains unknown"

Each caveat is honest. Together they turn the body into a defence brief. The reader starts bracing for the retraction instead of the scene. The caveats that change what the reader believes should stay in the body. The ones that only protect the writer belong in the notes or the specialist section, which already repeats most of them.

The story's spine is the friendship: executor, the sons' trust, "our children kiss your hands," the will revised, the papers sealed. It's on the page but never pointed at, so a general reader may not see it as the spine. That matters for compression: those beats must survive any cut.

## Weak spots and leaks

**The missing signature**
- **¶2** restates ¶1. "Pérez's signature stood beneath the King's. He received dispatches…" repeats "had countersigned the King's letters and received the ambassador's private confidences."
- **¶2**, "what had happened to his friend": the nearest "his" is Philip. The friendship is also asserted here before anything shows it.

**Without the key**
- **¶3**, "where a folio is a manuscript leaf" and "The signs below are a typographic transcription of the handwriting": throat-clearing before the best demonstration in the piece.
- **¶5–6** are methods prose in the narrative. "Duplicate letters and printed drafts supplied checks…" duplicates *From ink to text*. The disclosure itself must stay, but these paragraphs are where the story first stalls.

**Madrid, March 1578**
- **¶1**, "Philip's own words about his involvement will appear in the April letter below." **Query:** the essay's "April letter" is Pérez's 15 April cipher. Philip's words come from the separate note Mignet quotes, so this signpost points the reader at the wrong document.
- **¶1**, "Suspicion fell at once." **Query:** is "at once" supported by the record?
- **¶2**, "the Guises, the family of the French Duke of Guise": the gloss explains the word with itself.
- **¶4**: the second half (the Simancas conference, the Mignet May dating) is specialist material.
- **¶6–7** are two conclusions to one argument, and they restate each other. "Reading the available letters before the murder found no…" is lab-notebook syntax. ¶7 is a full hedge sandwich. This is the largest stall in the piece.

**The dead man's papers**
- **¶4**: the date sentence is orphaned after the quotations. "Philip's questions leave both… to be established" and "Nothing in them warrants…" say the same thing twice.
- **¶5**, "The secretary was involved in closing down and investigating the business whose earlier history would later enter his defence." This should be the section's payoff. You shrank on "was involved in," and the relative clause buries the irony.
- **¶5**, **Query:** Pérez *reported* that the dealings would cease. Does the record support "closing down" as his act?

**Only in the private letter**
- **¶1**, "Rubino found these provisions in printed clauses of the will": attribution that could live in the note.
- **¶3**, "It could matter greatly whether Pérez meant Philip or another official." This is the most dramatic open question in the essay, delivered in its flattest voice. The sentence after it restates it.
- **¶4**, last sentence: the backward step in past perfect stalls the transition into April.

**Stay where you are**
- **¶2**, the office "of Vargas": a general reader will stall here. Does it mean Vargas's own post? You flag the uncertainty but never say what the reader is meant to picture.
- **¶2**, "the reference is understood here as the family's action": passive, note voice.
- **¶3**, "His defence is concerned with what people have been saying about him and what the King is seen to do." The quotations show a man obsessed with honour. This sentence names that obsession in a committee's words. You shrank.
- **¶4**: the Éboli-lovers sentence is a digression that raises and drops a question. Does it earn its place?
- **¶6**: the independence method sits right at the climax, between the two "be calm" passages.
- **¶7**, "There is also a discrepancy that should remain on the page." The sentence announces its own honesty.
- **¶7**, **Query:** "the suit has ended with his innocence established." ¶2's summary never says Pérez claims the suit *ended*. As written, the discrepancy arrives without setup. Does the reading support "ended"?
- **¶8**, **Query:** "without knowing how the business would turn out" is mild inference. It's probably fine, but check it.

**Another hand**
- **¶1**, the "Instead…" sentence: the Idiáquez reversal is a genuinely good irony. Here it's tangled in a long clause.
- **¶3**: the first two sentences are methods prose.

**A paper in Paris**
- **¶1**, "One noun in this passage remains uncertain." The general reader doesn't learn which noun or why it matters. That's a caveat with no payoff.
- **¶3**: catalogue apparatus.
- **¶4**: the will revision is placed right after the leak inquiries and then disclaimed. **Query:** does this placement invite the causal inference the sentence denies?
- **¶5**, "Paz's catalogue records Vargas's illness and codicil… then his burial." The ambassador's death is delivered as a finding-aid entry.

**Specialist section**
- "Mignet's undated… report… remains undated in our record" is a tautology.
- **Folio 273:** the commit log (c6dd439, 87907d3) says f. 273 has its second witness and is closed. The draft still says "its second reading remains pending." Check this against the record.

## Passages to protect

- The opening sentence. "less than a month before" does real work.
- "a mis manos": "into my hands," and its October echo with Zayas. The title earns itself there.
- "For a long time, readers could follow him only as far as the numbers began." This is the best line in the front half.
- The f. 81 table and the *todas* walkthrough, plus "The difficulty is often deciding what the scribe actually drew." It turns paleography into stakes.
- "Philip was taking the report seriously two months before Escobedo died." It's plain and load-bearing.
- The Mary, Queen of Scots episode with "grandes quimeras." It's the only colour in the Madrid section.
- The executor and the sons' trust. This is the friendship's foundation.
- "Who that person is remains unread." It's dry and exact.
- "Between receipt and presentation there was room for the secretary's judgment."
- "grita y mentiras" and "Much of that promised truth follows in cipher." The deadpan works.
- The *sossiegue* / *sosegueis* echo, and the bare juxtaposition "Pérez tells his friend… Philip explains…" This is the emotional centre of the piece. Don't let the methods prose around it grow.
- The Doña Juana close.
- "Pérez and Éboli were arrested on the night of 28 July 1579." It barks because the long April section precedes it.
- "The silence belongs to this side of the correspondence, as far as we can read it." This is the one hedge that is also a good sentence.
- "del consejo no lo es."
- "sin comunicarlos a nadie" as the final line. It lands.

## Shortening opportunities

These need no evidence-bearing quotation to be cut:

- **Missing signature ¶2**: the duplicated countersignature sentences.
- **Without the key ¶5–6**: could compress to a single disclosure. Duplicate-check detail and project chronology go to the specialist section.
- **Madrid ¶4**: second half to a note.
- **Madrid ¶6–7**: merge into one conclusion. This is the largest saving.
- **Dead man's papers ¶4**: one of the two "not proven" sentences.
- **Private letter ¶3**: the restatement after "remains unread."
- **Stay ¶4**: the provenance sentences duplicate note 13.
- **Stay ¶6**: the method sentences go to a note.
- **Another hand ¶3**: the method sentences go to *From ink to text*.
- **A paper in Paris ¶3**: Simancas apparatus to note 16.

My rough estimate is 500–700 narrative words, with no quotation lost. The draft does not need to be shorter than 3140 words to work. It needs fewer moments where the narrator explains how careful it is being.

## Writer decisions

### Register and narrative

Accepted the editor's main diagnosis: repeated qualifications were interrupting the narrative. Kept the qualifications
that change the reading of a passage: missing March leaves; the unproved money; the unnamed person in the private-channel
letter; the uncorroborated archbishop–Éboli intervention; imperfect legibility after the arrest. Moved repeated method
and transmission detail into the specialist section. The executor appointment, sons' trust, family close, and revised
will remain. The last line still concerns custody of the papers.

Protected the opening, the numbers-began sentence, the cipher table and its explanation, the paired requests to be calm,
and the domestic close. Retained the reserved tone of the ending. No weather, rooms, gestures, private thoughts, or
new motive for the murder was supplied.

### Compression and deslopify

Applied `~/work/writing/.claude/commands/slopwriting.md` and the explicitly requested essay-detector use of
`~/.claude/skills/deslopify/SKILL.md`. Classification: long document, primarily linear narrative, changing to reference
prose in the specialist section and notes. The writer made every change; the editor supplied no replacement draft.

- **Restatement:** removed repeated accounts of Pérez receiving/showing letters; kept the June/July facts together near
  the opening. Combined the pre-murder conclusions. Cut the second warning that the ducats are not a proven payment.
- **Announced significance:** removed “There is also a discrepancy that should remain on the page” and “It could matter
  greatly…”. The discrepancy and the missing name remain stated directly.
- **Apparatus interrupting the story:** moved the Simancas conference description to note 8; moved the possible Portugal
  paper identification to note 16; moved the April transmission/independent-decoding detail to the specialist section.
  Parker's supervision is now in note 3. Illness/codicil chronology is in note 17; the body states the burial.
- **Digression:** cut the aside on whether Pérez and Éboli were lovers. It established no claim used by the essay. The
  source register records the cut. Rubino's speculation about why the will changed remains in note 11, not as a proposed
  explanation in the narrative.
- **Agency and attribution:** replaced the implication that Pérez personally closed down the business with his documented
  act of relaying the inquiry. “He believed he deserved” became what he writes the King should have done. His uncertainty
  at the letter's close is explicitly something he says.

The head-and-tail check preserved both: the opening introduces the dated change of correspondent, and the ending adds
the executors' instruction rather than summarizing the essay. A full rhythm read followed the cuts. The narrative still
has room for the longer quoted passages and their translations.

Scanner findings were judged in context. “Survived” in the trust provision is literal, not inflated prose. The three
examples of corroboration in the specialist section are actual checks, not a rhetorical triad; retained. The vocabulary
list is calibrated on engineering prose, so ordinary historical language was not replaced with synonyms.

`scan.sh` initially hit an awk multibyte error in its vocabulary output. Running with `LC_ALL=C` completed that output;
the Unicode text itself was not changed. `audit.sh` initially flagged an extra occurrence of 1579 added while relocating
the April check. That redundant year was removed. The final audit exits 0 with no introduced tic or unsourced-number
flag. Its conservation output still lists fewer repetitions of names and two numeric tokens: an extra 800,000 from the
deleted repeated caveat (the translated quotation retains it), and a repeated 1580 in the rearranged final note (the
year remains in both body and note). No number's value changed; code spans and URLs were preserved.

### Fact pass

- Checked Spanish quotations against the joined readings/canon, preserving bracketed supplies and omissions. The only
  quote change after the compression snapshot is lowercasing the initial “y” in the f. 81 specimen to match the source,
  with the same change in its translation. All 52 narrative quoted passages remain, comparing case-insensitively.
- Corrected the misleading first-draft signpost that called Philip's separate April note “the April letter below.”
- Confirmed immediate suspicion against Pérez in the already-read Lafuente record; retained it.
- Put Pérez's claim that the suit ended into the first account of his defence, before juxtaposing the King's note.
- Kept the unknown office and its Vargas unidentified; kept the archbishop intervention as Pérez's provisional account.
- Confirmed the source's October/December dates, arrest date, countersignatures, and the two leak passages. No culprit is
  suggested. The candidate “Consejo” is labelled only in the specialist section.
- Checked the newly committed f. 273 update (`c6dd439`, `87907d3`). It now has two witnesses, so removed the stale pending
  task from the draft and outline. Did not adopt the third-party inferred 1573 date or the misassigned marginal date.
- Kept the failed/weaker duplicate checks, sample qualifications, and character-match definitions. No experiment rerun or
  new historical statistic was needed; the essay reports checked-in results.
- Generated and reviewed `CLAIMS.md`: every non-structural content line, including translations, table rows and endnotes,
  has source keys. Locations, text and draft hash were checked in code. All 17 numbered notes are cited and defined.

### Length and conservation

Whitespace word counts include headings, quotations and translations; notes are counted separately. The skill scanner
strips Markdown/code differently, so its document-wide count is lower.

| Part | First draft (`1cf1591`) | Revised draft |
|---|---:|---:|
| Narrative | 3,140 | 2,562 |
| Specialist section | 1,013 | 1,063 |
| Notes | 365 | 422 |

The narrative lost 578 words. All 52 quoted passages survived. The increase in specialist text and notes is mainly
relocated provenance plus the f. 273 correction. This is not a claim that the original proposed 4,800-word version was
written and then cut; the first actual draft was already shorter.

### Delivery state

Full draft ready for Greg's review. No publication yet: `PROMPT-essay.md` requires the full-draft review before the page
or document choice. The substantive limitations remain visible in the draft; no human paleographer review is claimed.

## Greg's fuller draft: order and quotation provenance · 2026-10-05

Greg restored narrative material in `DRAFT-fable.md` (`59f5c92`) after finding the earlier compression too severe.
That file supplied the base for this revision of `DRAFT.md` and remains unchanged as a comparison. This pass applies
his request to begin with the murder's context, preserve an engaging narrative, and distinguish deciphered passages
from clear text and earlier publications. No further drafting/editor agents were used.

### Order and narrative

- Open with Escobedo's murder, the relationship between the two secretaries and Philip, and Vargas's place in the
  correspondence. Introduce the volume through Pérez's April explanation. The reader knows the stakes before meeting
  Ochoa, Devos and the cipher specimen.
- Keep the reading history next, followed by “Reports from Paris” and the letters in sequence. Move the July/August
  missing-signature contrast into “Another hand,” immediately after the arrest.
- Keep the restored Guise/two-crowns quotations, household detail, longer April excerpts and Pérez's later fate.
  Remove the repeated account of the murder and one repeated statement of the January result. No general compression
  target was imposed. Narrative: 3,325 whitespace words, including headings and quotations/translations; specialist
  text: 1,094; notes: 568. The fuller base was already shorter than the original outline's 4,800-word estimate.
- Renumber the 21 notes by first appearance and update the internal cross-reference.

### Quotation audit

`QUOTES.md` records 34 entries: all narrative Spanish quotations/specimens plus the specialist candidate “Consejo.”
Bold marks spans written in cipher; matching English spans are bold. Plain Spanish manuscript text was already in
ordinary handwriting. Printed quotations are attributed in the prose, since a printed text can itself descend from
an official decipherment. English translations are editorial throughout.

The mixed boundaries matter: f. 12v's serious-consideration clause is clear; f. 179's instruction mixes cipher with
clear text, including its reassurance that there will be no danger; f. 198v's philosopher phrase is clear, while the
devil/ministers phrase crosses a boundary. The raw reconciled decode leaves a sign inside *diablo* unresolved, so the
essay now marks `[diablo]` and `[devil]` as supplied. The refused-leave quotation is on f. 199r, not f. 198r.

Tomokiyo's f. 81 specimen and isolated f. 198 readings are credited. The opening and family farewell were already
transcribed by Rubino. Cabinet-noir's earlier readings and pangoleen's overlapping readings prevent any blanket
claim that the bold passages are first decipherments by this project. Teulet's official decipherments, Mignet's
printed draft/note, Ochoa's commentary and Paz's catalogue summary each retain their separate source identity.

The expanded Mignet passage was checked on the **printed page image**, p. 120 n. 2, scan leaf 74:
`https://archive.org/download/antonioperezetph00mign/page/n74.jpg`. Restored *escussar*, *no asido*, *escusse*, *sosegaeis*
and the accent in *será*. The Hague original remains uninspected. Apart from that corrected excerpt, all quotation
wording in the fuller narrative survives after accounting for bold, punctuation and the explicit `[diablo]` supply.
The Spanish *de Vargas* was added beside the already-present English *of Vargas*.

### Factual and stylistic review

- Replaced the assertion that neither April writer had seen the other's letter with the documented limit: their
  order within April is unknown. Separate transmission does not establish what the historical writers had seen.
- Kept the office and its Vargas unidentified; the fuller draft's proposed secretary/vacancy is not secure.
- Replaced “Pérez countersigned … so he knew” with the signature fact. Replaced the ambiguous “something true … under
  the wrong name” with the precise January result: dealings before the murder, no established confederation.
- Removed the absolute claim that the transcription method prevented a reader from anticipating a word; the
  procedure separates transcription from decoding, while the specialist section still admits shared model errors.
- Confirmed the restored poison detail in Lafuente. Confirmed the year/place of Pérez's death in the indexed PARES
  authority record; its direct page returned 429. The disputed day remains outside the essay.
- Ran one deslopify scan and one before/after audit, using the skill as a detector. Kept literal *survived* in the will
  clause and the specialist list of three independent catalogue checks; neither is a rhetorical tic. The audit's
  exit 1 flags intentional source/date/folio additions, not unresolved prose faults: 1567 replaces the opening's
  relative “twelve years”; publication dates identify prior readings; 199 corrects the quotation's leaf; 206 adds
  the dispatch source; the remaining numeric tokens belong to notes and source URLs. Removed occurrences of 1579,
  198 and `OVERVIEW.md` §7.2 reflect rearrangement, the folio correction and replacement with a direct page citation.
  No historical number was silently changed. All original URLs remain.
- `CLAIMS.md` now maps 275 content lines. A script checked the exact mapped text/line numbers, draft hash, coverage
  and all 21 note definitions/references. The quotation comparison reported only the Mignet correction and added
  *de Vargas* after ignoring typography, brackets and terminal punctuation. `git diff --check` passed.

The revised reading copy is `DRAFT.md`; publication remains pending Greg's review and page/document choice.

## More of the cipher text · 2026-10-06

Greg asked for more consequential cipher quotations. Expanded four places using the existing joined readings:

- **20 October 1578, f. 123:** the inquiry now continues to the request for papers or letters from the Theatine or
  other people. The ellipsis omits the uncertain *prendas* clause. The unidentified Theatine is qualified in the prose;
  the reading is not a new identification.
- **4 December 1578, ff. 154v–155r:** restored the report of Guise's cipher with Don John, the union involving Lorraine,
  and the 800,000 ducats. The King's ensuing questions test that report. Both the single-local-reader qualification
  and the distinction between reported money and an established payment remain.
- **15 April 1579, f. 198v:** Pérez's claim that his enemies tried to take his honour and his life is now quoted from
  the cipher instead of paraphrased.
- **29 November 1579, ff. 245/247:** restored the King's question about the route and means by which the paper reached
  Paris, from the longer joined reading already in `OVERVIEW.md`.

The “two crowns” passage was already present. It remains attributed to Teulet's printed official decipherment and
is not bolded as one of our Espagnol 132 readings. Its crowns are Spain and France; the December report concerns a
different union. No new cipher work or first-reading claim was added.

The deslopify detector found no new pattern requiring a change: the literal will-clause *survived* and specialist
catalogue examples remain for the reasons recorded above. Source spellings *mil* and *mill* both survive in the
December quotations. Updated `QUOTES.md` (new Q35 plus extended Q11/Q12/Q32); corrected its October letter date from
3 to 13 October against experiment 07. The essay itself already said only “By October.” Refreshed `CLAIMS.md`, including
the stale will-note reference left by the previous renumbering. No earlier substantive quotation was cut.

Verification: 283 exact claim mappings and draft hash; 21 ordered notes; 35 quotation entries. All earlier narrative
quotations survive intact or inside longer excerpts. New Spanish passages match the existing joined readings.
Narrative: 3,473 whitespace words (+148); specialist: 1,094; notes: 568.
