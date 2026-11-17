# Hypotheses

Numbered, never renumbered. Status: `open` / `supported` / `weakened` /
`refuted` / `superseded by Hn`. Every hypothesis names the test that would
move it. Results are recorded in `research.md` and in `analysis/`.

| # | Hypothesis | Status | Test that would move it | Evidence so far |
|---|---|---|---|---|
| H1 | The Terranova letters are in the general cipher Cg.12 (1582). Then no key is missing and the result is a known-key reading. | open | Get the Cg.12 table (Devos 1950). Decode a two-reader transcription of item 6 by script. Pass: continuous Spanish against a shuffled-table control. | For: date and office fit a general cipher; underlined figures and CVC codes match Tomokiyo's description of Cg.12. Against: nothing yet. One page seen, by eye. |
| H2 | They are in a particular cipher of the Cg.12 / Cp.30 family (same design, other values). Then the key is missing and the family prior should recover it. | open | If H1 fails: measure which design features hold (letter shift, vowel marks, code series). Then run the recovery under README criteria 3–4. | Depends on H1. |
| H3 | DECODE R9318 ("Duca di Terranova") is the key. | open | Greg's DECODE login: view R9318 and compare its design and values with the transcription. | Bourdeau's catalogue names it as a key to test; nobody reports having tested it. |
| H4 | In Spanish keys of 1575–1587 the code lists are alphabetical in both plain word and code, so a few known codes bound the rest. | open | Script over the keys we hold (Ciphers 1–4, Cp.30) and Devos's tables: rank correlation of plain order and code order. | Not measured. It is the family prior that H2 needs. |
| H5 | Jean Bazin's two cipher letters of 15 Sept 1573 (Colbert 338 pp. 189, 191) use Monluc's Cipher 1 or 2. | open | Compare the signs and clear "jargon" words with Tomokiyo's Monluc tables. Parked: outside this dive's first target. | Bourdeau's vetting saw clear words (janvier, may, Valence) inside the cipher. Tomokiyo says Monluc's Cipher 1 uses month names as code words. Bazin wrote from Monluc's Polish mission. |
| H6 | An aligner that lets stretches of cipher go unmatched (gaps opened and extended at a cost, as in local sequence alignment) rebuilds the 2911 key from V/140 and the printed text. | open | Use the 2911 pair as a calibration case: `items/2911/work/cipher-doubles.txt` against `work/plain-print.txt`, scored by script on `items/2911/outside/truth.tsv`. Bar to be written before the run. Also a synthetic pair with 40% of the plain text removed in stretches. | For: the outside check shows the complete-pair assumption is what failed, and the transcription is sound. Against: untried; 53% syllable signs over about 100 sign types is harder than Cp.30. |
| H7 | A stage 4 bar set against something measurable without the answer (for example the gap between accuracy and the shuffled control, with a recall floor) separates a right key from a wrong one on pairs whose plain side is inexact. The fixed 0.85 does not. | open | On 2911, score the true key (`outside/truth.tsv`) and shuffled tables by fold; on es. 132 f. 255 the same. Propose the bar from those two; test on the next item. | The true key scores 0.735 on 2911's covered stretches and 0.79 on f. 255: both under 0.85. |

## Notes
- H1 and H2 split Greg's goal. Only H2 gives a new key. H1 must be tested first because it is cheap and because
  criterion 1 requires it.
