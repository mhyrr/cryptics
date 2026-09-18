# E1 input audit — no historical score

A testable exploratory recipe and independent dictionary block are frozen.
The historical run is blocked on source-backed German captions and target alignment.
Controls were specified but not run; scores and predictions are null.

Sample: scans [326, 327], 10 entries; 5 have no Hebrew transliteration; 1 entry has an unresolved reading and abstains.

| Entry | Eligible domains for odd n=3..25 (not caption matches) |
|---|---|
| 326-1 | none |
| 326-2 | none |
| 326-3 | none |
| 326-4 | none |
| 326-5 | {"7": ["PERESCH"]} |
| 327-1 | none |
| 327-2 | {"7": ["NEKUDAH"]} |
| 327-3 | none |
| 327-4 | none |
| 327-5 | none |

## Discovery diagnostic, kept out of evaluation

Literal caption-to-reported-headword matching only. This does not test word
placement, dictionary completeness, or square-letter recovery.

| Example | Caption | Reported headword | Literal match |
|---|---|---|---|
| teacher | Vergangene Sachen Zuwissen | Lehrer | False |
| diviner | Zuekünftige Sachen | Warsager | False |
| instructor | Bericht auf allerley Zweyffelhafftige fragen Zuehaben; item 2 | Vnterweiser | False |
| sky | WunderZeichen vnd witterungen vorZuwissen | Himmel | False |
| water | Inn wasser | Wasser | True |
| wax | Inn Wax vnd durch allerley schrifften | Wachs | False |
| beast | Inn Thier gestallt | Thier | True |
| bird | In Vogels gestallt | Vogel | False |
| earth_overlap | In hülen, gewölben vnd grotten vnder der Erden | Erdt | False |

Literal matches: 2/9 discovery associations.
This is a limit of literal selection as a general explanation, not an independent success rate.

No sampled entry has been declared absent from historical captions: the caption join
has not occurred. Lexical exclusions, caption misses and alignment failures are distinct.

The exact missing artifact is a caption-only table with German source text, locator,
verified Mathers target ID, alignment evidence independent of letters, and exposure flags.
English translation or square seeds cannot silently substitute for that input.
