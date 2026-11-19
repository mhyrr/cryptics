# Scout brief: four gates for cross-section candidates (2026-11-19)

You are a scout for stage 1 of `line/PROMPT-cross-section.md`. Read `CLAUDE.md` (repo root), then
`puzzles/missing-keys-16c/line/PROMPT-cross-section.md` (the gate table) and the section "What you need" of
`line/METHOD.md`. Do not read further. **Do not spawn agents. Do not attempt any reading or decipherment.**
Rule 9 of CLAUDE.md applies: this is gating, not solving.

Work from `puzzles/missing-keys-16c/`. Your candidates and output file names are in your dispatch prompt.

## Inputs you may use
- The catalogue entry: `python3 -I -c "import json;d={e['id']:e for e in json.load(open('sources/cache/bourdeau-catalogue-2026-11-18.json'))['entries']};print(json.dumps(d[ID],indent=1,ensure_ascii=False))"`
- Outside targets: `line/taken-2026-11-19.tsv` (ids named by 887 profiles fetched today) and the profiles
  themselves, `sources/cache/bourdeau-profiles-2026-11-19.json` (map path -> text). Grep the profiles for the
  shelfmark, writer and recipient too: a target can cover an item without naming its id.
- Web search and fetch. Use Python (`urllib`) for downloads, never curl. No personal details in any request;
  User-Agent `cryptics-research-script`.

## Per candidate, four gates
1. **Matters.** Who wrote to whom, when, and what the unread text could add, in one sentence a historian
   would accept. Cite one SCHOLARLY or PRIMARY source by URL (the archive record counts as PRIMARY for who and
   when; the "what it adds" needs a SCHOLARLY or SECONDARY source on the episode).
2. **Not taken.** The taken file and a profile grep (above), then two or three web searches for a printed or
   online decipherment, key or reading. Say what you searched and what you did not check.
3. **Readable.** Fetch one cipher page at the largest size the server gives (IIIF: try `full/max` or
   `full/full`; note the pixel width). Save it to `sources/cache/cross/<id>/` (gitignored). Measure with
   `python3 -I line/sign_height.py <image> --box W,H,X,Y`, box round the cipher block only (look at the image
   first, by reading it, to place the box). Record `h_median` and the box. Pass: 15 px or more.
   Calibration: no. 1336 c. 269r measures 11 px (readers agreed at 0.80); no. 2351 measures 20 px (0.91).
4. **Buildable.** Is there a pair: the same text in cipher and in clear (a decipherment of the time between
   the lines or on another leaf, a clear minute, a printed edition)? Estimate its length in signs (lines x
   signs per line, by eye from the image, say so). Is there a published key of the same chancery and decade
   to hold (name it and where it is)? Is there a second passage in the same cipher for a test? Describe the
   design from what the page shows: letters only, base sign plus marks, many digit groups (a code list).
   Pass: a pair of 100 signs or more, or a neighbour key to hold, plus a second passage.

Spend two or three fetches per gate at most. When a gate fails, record it and move on; the remaining gates may
then be `not checked`.

## Output
Append one tab-separated row per candidate to your file `line/cross-section/scout-<X>.tsv`, with this header
(write the header first):

    id	short_title	writer	recipient	date	matters	matters_src	not_taken	searches	image_url	image_w	box	h_median	pair	pair_signs	neighbour_keys	second_passage	design	verdict	failed_gate	notes

`verdict` is `pass` or `fail`; `failed_gate` names the first gate failed. Every cell cites its source (URL)
or the script that made it. Write each row as soon as that candidate is done; a usage limit can stop you.
Then write `line/cross-section/scout-<X>.md` with a short note per candidate: what you saw on the page,
anything that would change the verdict, and URLs. Report back in under 300 words.
