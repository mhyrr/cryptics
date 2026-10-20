# Historical evidence for the BLUME SALAMANCA telegrams

Work in `puzzles/blume-salamanca-1937`. Read the repository's `AGENTS.md` and
`STRUCTURE.md` first. This is a research task. Do not start another target
decryption campaign.

## Objective

Find historical evidence that changes what we should give the solver: a
supported key or key source, an identified cipher procedure, an independently
supported plaintext passage, or additional related traffic. Return a small,
ranked set of testable options. A precise account of inaccessible evidence is
a valid result. Do not manufacture candidates to fill a quota.

The central question is: **what did these correspondents actually have in
common that could supply their keys and encryption instructions?**

## Read before searching

Read `NEXT.md`, `canon.md` and `hypotheses.md`. Then read:

- `sources/PROVENANCE.md`, `headers.md` and `context-cribs.md`;
- `sources/key-type-survey.md`, `conventions-survey.md`,
  `heinzmann-search-2026-10-20.md` and `outreach-bochsler.md`;
- `analysis/23-method-audit/README.md` and the READMEs/results of 26 and 27;
- `analysis/24-phrase-seeded/phrases.py` and its candidate manifest, to see
  which contextual phrases and construction rules were already used.

Search `research.md` for relevant subjects; do not read it end to end.
Consult project memory if available. Older status summaries and exclusion
claims may be stale: the current handoff and method audit govern their scope.

## Starting evidence and limits

Two cipher telegrams were sent from Zurich to `BLUME SALAMANCA` on 8 January
1937. The retained bodies contain 615 and 160 letters. The Swiss Federal
Archives reference is `E4320B#1974/47#277`, *Spanische Revolution (Passvisas
etc.)*, subdossier `0000066`, unit `Unterlagen_0000072`, canvases 9 and 13.
Exact manifests and image URLs are in `sources/PROVENANCE.md`.

The sender's office is associated with the Oswalds at Bahnhofstrasse 12,
Zurich. Preserve differences between names/initials in individual records.
Werner's police testimony attributes the messages to his brother Viktor and
describes wool trading, frozen Swiss export balances and reopening a Spanish
office. He mentions keeping the plan from Hisma until discussions with the
authorities in Burgos. This establishes what Werner said, not what the
messages contain. Do not force discoveries to support that account.

BLUME's identity remains unresolved. It could be a registered telegraphic
address, a person, an organization or another designation. Establish its
function before treating it as a surname or translating it.

Transposition is a working hypothesis. Double columnar encryption has not
been historically tied to these senders. A shared system or shared keys
between the two messages is also unproved.

Our repaired solver recovers many planted messages when the second key is on
or near a contextual phrase list. Its completed phrase searches produced no
candidate on T1; unrelated random-key controls did not recover. This makes
better external constraints useful. It does not make any surviving cipher
family or untried phrase likely by elimination. Current plaintext controls
are modified novels, not period commercial telegrams.

## Investigation order

**1. Identify BLUME.** Start with registered telegraphic-address lists,
Salamanca commercial/telephone directories, chambers of commerce, trade
registers and contemporary newspapers, concentrating on 1935–1938 and using
adjacent years when necessary. Trace a proposed match to an address, business,
person or office, and then seek a separate connection to Oswald or the
relevant correspondence. A matching word alone is insufficient. Look for
independent corroboration; copied directory entries are not independent.

**2. Follow the correspondence.** Use the identification, or the documented
Oswald businesses if BLUME remains unidentified, to locate letters, replies,
telegrams, account books, codebooks and instructions. Begin with the Swiss
dossier and its related records; follow specific leads into Spanish archival
catalogues, including PARES, Salamanca and Burgos collections, and company
or personal papers. Search in Spanish, German and French as appropriate.
OCR-negative files are not image-verified negatives. Inspect promising pages
and neighbouring correspondence, recording what was actually viewed.

Prioritize exact keys, code sheets, dated instructions, plaintext drafts,
matched incoming/outgoing messages, and repeated traffic with indicators or
other evidence of shared keys. Preserve each message's boundaries. Do not
concatenate traffic simply because the sender or date matches.

**3. Recover the earlier research.** Inspect Regula Bochsler's *Nylon und
Napalm* (2022), note 44, if accessible. Establish what it actually says about
the reported 2020 attempt by Peter Heinzmann, Carlo Matteotti, Patrick Liniger
and Kandiah Viveksanth. Follow the citation to any report or research papers.
Prior web searches are logged; extend them with a new source or route rather
than repeating them. The possible HSR/cnlab identification is unconfirmed.
Do not attach unrelated namesakes to this work. If access requires contact,
record the precise request and intended recipient; send nothing.

**4. Establish the encryption and message preparation.** Seek contemporary
instructions connected to the people, firms or institutions actually found.
A manual available in Europe is evidence of availability, not of their use.
Distinguish pre-January-1937 practice from later practice. Investigate how
keys were selected, ranked and changed; whether the two stages used related
keys; and how numbers, accents, repeated keyword letters, abbreviations,
separators, indicators and padding were handled. Routing, nationality and
tariff stamps alone do not identify an encryption method.

If available, collect a small, independently sourced sample of comparable
period Spanish business telegrams, preferably with images and transcriptions.
These would let us test whether our scoring model recognizes the kind of
plaintext we need. Keep this calibration material separate from evidence
about the particular messages.

## Turn findings into solver options

Separate four evidence types: cipher procedure, possible key material,
possible plaintext, and calibration text. For each proposed option record:

- Exact original text/spelling; date; people or institution; source URL,
  archive reference and page/image; source tier; whether you read the original.
- The chain connecting it to these messages, including contradictory evidence
  and uncertain links. Distinguish a documented key from a contextual guess.
- The specific computational consequence: supplied numeric key, bounded set
  of phrases, supported key-length range, key relationship, preparation rule,
  externally supported plaintext passage, or additional traffic.
- Any normalization or extraction alternatives. Say which are documented and
  which are modern test choices. Bound those alternatives before target use;
  do not generate arbitrary combinations of every name and place.
- A falsifiable test, required fresh controls, and what a negative result
  would and would not establish. Note overlap with earlier phrase lists.

A company name appearing in a business record is not proof that it was a
key. A likely subject word is not known plaintext. A phrase suggested by a
partial solver output is not independent evidence. Prefer evidence that
selects among competing systems or keys over background that fits everything.

For a proposed plaintext passage, necessary letter-count constraints may be
checked under an explicitly stated pure-transposition model. Passing them
does not validate the passage. **Do not apply ciphertext letter budgets to
key phrases:** their letters need not occur in the message.

Do not silently turn a German description of the business into an exact
Spanish crib. Do not alter the ciphertext or invent padding rules to rescue
a candidate. Use scripts for normalization, counts, ranking permutations,
deduplication or other numerical claims. Keep raw source forms and provenance
when different phrases collapse to one numeric key.

## Deliverables and stopping rule

Save a sourced report and search log under `sources/historical-evidence/`.
Record searches, catalogues/date ranges covered, documents/pages inspected,
access failures and remaining gaps. Do not report a failed search as proof
that a document or person does not exist.

Produce `sources/historical-evidence/solver-options.jsonl`, one record per
candidate family, with stable IDs and fields for evidence type, raw text,
source locator, source tier, date, connection to the messages, confidence,
proposed derivation/preparation, bounded variants, prior-search overlap and
the proposed control/target test. Use null where something is unknown. Keep
weak contextual guesses explicitly labelled; they are not solver-ready keys.
If computation is needed, use the next unused numbered `analysis/` folder
with a README, reproducible script and checked-in result.

Conclude with the strongest supported finding, a ranked shortlist (possibly
empty), the single best next solver experiment if justified, and the exact
document/access barrier that would most improve our position. Explain which
claims remain uncertain. Do not assign invented probabilities of decryption.

Complete one documented research pass and stop at a named evidence wall.
Do not start solver runs, send outreach, spend money or bypass access
restrictions. Do not change historical hypotheses to fit target outputs.
Update the research record and handoff with findings and source limitations.
The return to computation requires a separately frozen plan and fresh controls.
