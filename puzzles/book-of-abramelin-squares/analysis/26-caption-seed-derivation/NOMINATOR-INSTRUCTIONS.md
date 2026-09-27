# Instructions for nominators (experiment 26)

You receive one file, `nominator-input.json`: the German captions of Book IV
of a manuscript, grouped by chapter, each chapter with its heading as
written. Open no other file, do not search the web, and do not consult any
dictionary. Do not start other agents.

## Task

For each caption, nominate at most THREE German headwords, written as a
German dictionary of about 1600 would list them: the lemma (nominative
singular for a noun, infinitive for a verb, base form for an adjective).
Period spelling is allowed; modern spelling is also fine.

Order of priority:

1. the concrete entity, material, person, animal, place or state the caption
   concerns, as a noun (or an adjective for a quality), taken from the
   caption's own words where the caption names it;
2. one direct German synonym of the same scope, if a common one exists;
3. the action as an infinitive, only when the caption names an action and no
   entity, or when the action is the point of the caption.

Rules:

- No mythological identifications, no Hebrew, no Latin, no Greek, no guesses
  about what a magic square might contain.
- "In gestalt eines X", "In X gestalt" and "Wie ein X" mean nominate X.
- A compound counts as one headword. If you judge that a dictionary would
  list only its parts, you may nominate the head noun instead.
- A caption that only refers back ("Aliud", "ad idem", "Dasselbe") takes the
  subject of the nearest preceding caption in its chapter that names one.
- A caption that is only a number takes the chapter heading as its caption.
  If the chapter heading has no title, the chapter's first captioned item
  gives the title.
- Ignore the copyist's Latin notes such as "mea Correctio".
- A caption with no nameable referent gets an empty list.
- "„" and "-" inside a word mark a line break. [a/b] marks two possible
  readings; you may use either.

## Output

Write one JSON file, `nominations-<your letter>.json`, in the folder you are
given, and nothing anywhere else:

```json
{"nominator": "<your letter>",
 "items": [
  {"key": "p246-c1-g1",
   "nominations": [
     {"german": "<headword>", "renders": "<caption words>", "reason": "<one line>"}
   ]}
 ]}
```

One item per caption key in the input, in input order, including items
with an empty list. Keep each reason to one line.
