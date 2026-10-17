# Key-type survey: hand transpositions available to a Swiss engineer in January 1937

Compiled 2026-10-16 for NEXT.md "Do first" item 1 (H4, H5). Read-only research: about 25 web searches and
fetches, plus full-text reads of Langie (1922 English edition) and Givierge (1925, English translation) from
archive.org. It does not repeat `context-cribs.md` §1. Tiers follow AGENTS.md rule 1.

**Summary.** No source ties any named transposition system to the Oswalds, to Swiss commerce, or to Spain in
1936–37. The Swiss army's own hand cipher of the period was a substitution. The Spanish hand systems were
substitutions. The German army's documented transpositions are from before 1927 or after 1940. So the candidate
list below comes from the two French-language handbooks a Swiss reader of 1937 could most easily have had:
Langie (a Lausanne cryptologist, 1918) and Givierge (1925). Both describe the same small set of hand
transpositions. Only two of them keep plaintext runs together by design: **word transposition** and **route
(geometric table) transposition read along rows**. Block transposition and the turning grille keep runs only in
part. Columnar systems keep none, except that a shared opening under the same single columnar key leaves shared
column tops (Givierge, below). That last mechanism matters for H5 even though single columnar itself is excluded.

## Candidate systems

Ranked by "keeps short plaintext runs" first, then by how well documented the system is for the period.

| system | how it works (one line) | documented user / date | source + tier | keeps short plaintext runs? |
|---|---|---|---|---|
| Word transposition | The words of the plaintext, not the letters, are reordered by a key or a rule. | Described as a known practice by Givierge, *Cours de cryptographie*, 1925, ch. XII (end), p. ~114. No named user. | https://archive.org/details/french-colonel-marcel-givierges-1925-book-cours-de-cryptographie-cryptography-course `SCHOLARLY` (a cryptographer's textbook; treat as handbook) | **Yes.** Every word stays intact. A common phrase in both messages would give shared strings of whole-word length. But the cipher text would then contain readable Spanish words, and Bourdeau found none; letters inside words would have to be transposed too. |
| Route / geometric table transposition | Write the text into a table by one path (rows, spiral, serpentine, knight's move) and read it out by another. | Givierge 1925, p. 94: "a knight's move in chess, geometric figures, spirals from the center to the circumference or vice versa". No named user. | Givierge, as above `SCHOLARLY` | **Partly.** Routes that read along the rows of the writing table (forward or reversed, as in a serpentine or a row-reordering) keep row-length runs. Spiral and diagonal routes break most of them. Reversed runs would show as reversed shared strings; `02` looked only at forward matches. |
| Block (periodic) transposition | Cut the text into sets of n letters; move the sets, or the letters within each set, by an n-digit key. | Givierge 1925, p. 94, worked with key 4-2-6-3-7-1-5 on sets of seven. No named user. Givierge: with one message of this kind "we have very little chance of ever succeeding". | Givierge, as above `SCHOLARLY` | **Partly.** If whole sets are moved, runs up to n letters survive. If letters within a set are permuted, only pairs that the key keeps adjacent survive. A common phrase gives identical cipher only when it sits at the same offset modulo n in both messages. |
| Turning (revolving) grille | A square card with holes is laid on a grid, the text written through the holes, the card turned 90° three times; read the grid by rows. | Langie 1918 (English 1922), pp. 40–42 and a solved example; Givierge 1925, pp. ~104–110. Langie notes a "high Austrian officer" added null letters to it. | Langie: https://archive.org/details/cryptographylang00lang `SCHOLARLY` (handbook); Givierge, as above | **Partly.** Plaintext order is kept within each quarter turn, but letters are spaced by the hole pattern; adjacency survives only where holes are adjacent. Givierge: a length that is a multiple of a perfect square points to a grille. **160 = 10 × 16 fits a 4×4 grille; 615 (= 3 × 5 × 41) fits no square** without nulls or a short last block. |
| Single columnar ("dividers"), incomplete table, nulls | Write in rows under a key; read columns in key order; last row may be short; Langie's example adds a first row of nulls. | Langie 1918/1922, pp. 42–44 ("dividers", key 2-6-4-1-5-3, incomplete last row; a null first line KVLPZU). Givierge 1925, pp. 94–95 ("tabular transpositions", the "standard" kind). Lasry: IRA main cipher in the 1920s (context-cribs §1). | Langie and Givierge, as above `SCHOLARLY` | **Partly, and only across messages.** Within one message, cipher neighbours are plaintext letters a row apart. But Givierge (p. 112): with two messages in the same key, "the letters at the same distances from the beginnings of the two plain-text messages will be at the same distances from the beginnings of the cipher". A shared opening of L letters gives shared column tops of about L/w letters each, at positions that depend on each message's column lengths. **This is the observed pattern** (shared 4–6-grams, no constant offset). Excluded for T1 alone by Bourdeau's single-columnar tests; not excluded as a joint mechanism. |
| Double columnar (Doppelwürfel, Übchi, "retransposition") | Single columnar applied twice, with the same or different keys. | Givierge 1925, ch. XIII "Retranspositions" (any table system "may be applied several times"); Übchi WWI German army (context-cribs §1); Abwehr agent ciphers; the 1944 **Rasterersatzverfahren** uses "double columnar transposition with a numerical key of 20 to 25 numbers". | Givierge as above `SCHOLARLY`; https://cryptocellar.org/wmc/index.html `PRIMARY` (document list; the 20–25 figure is from the page's description of the 7 Dec 1944 instruction, not opened); https://cryptocellar.org/pubs/mcts.pdf `SCHOLARLY` | **No.** A shared opening gives shared column tops after the first pass of about L/w1 letters; the second pass spreads those by w2. Shared 4-grams would need a very long common phrase. This is why `02` weakens H1/H2. |
| Cadenus | A 25-row grid transposed by columns with row shifts keyed to letters; text length a multiple of 25. | Credited to Lange & Soudart, *Traité de cryptographie*, 1925, by one search result. Not checked in the book. | Search result: https://www.sites.google.com/site/cryptocrackprogram/user-guide/cipher-types/other/cadenus `POPULAR` | **No.** And **ruled out by length**: neither 615 nor 160 is a multiple of 25. |
| Transposition plus digraph substitution | Write in a table, take column digraphs, encipher them by a digraph table. | Givierge 1925, ch. XIII. | Givierge, as above `SCHOLARLY` | **No**, and ruled out: substitution would disturb the Spanish letter frequencies, which the telegrams keep. |

### Systems surveyed and excluded (not transpositions, or wrong date)
- **Swiss army Réglette**, a keyed slide rule, "based on the Vigenere Cipher", output as two-digit numbers.
  "Developed around 1918 by the Nachrichtensektion (Intelligence Section) of the Swiss Army", used "up to Brigade
  level", "in use until 1939". https://cryptomuseum.com/crypto/swiss/reglette `SECONDARY` (citing Ritter, *Das
  Fernmeldematerial der Schweizerischen Armee seit 1875*, 10. Folge, 2002). A substitution with digit output, so
  not this cipher. **It is the only Swiss army hand system before 1938 that we found.** The Swiss army bought
  Enigma D and K from 1938 (https://www.hamfu.ch/de/geraete/geraet.php?id=155, `SECONDARY`, search summary).
- **Spanish Civil War hand systems.** Soler Fuensanta's survey ("Secretos en el aire"): the Republicans used
  "sistemas, un poco modificados, como el playfair, utilizado por los guerrilleros, y sistemas de cinta múltiple"
  (systems, slightly modified, such as Playfair, used by guerrillas, and multiple-strip systems); among
  Nationalists "a niveles inferiores se siguieron utilizando métodos menos sofisticados como tablas de homófonos
  y sistemas de cinta" (at lower levels less sophisticated methods such as homophone tables and strip systems
  continued to be used); and on the Republican side "los preponderantes fueron los sistemas de cinta, los libros
  de códigos y los códigos de trinchera" (the predominant ones were strip systems, code books and trench codes).
  No transposition is named. https://www.slideshare.net/slideshow/46-secretos-en-el-aire-la-criptografa-en-la-guerra-civil-espaola/27656244
  `SCHOLARLY` (author's own presentation). All substitutions, so excluded.
- **German Wehrmacht manual ciphers.** The cryptocellar document list has nothing dated before January 1940.
  Doppelkastenschlüssel (1940–41) is a substitution; Rasterschlüssel 44 and the Rasterersatzverfahren are 1944.
  https://cryptocellar.org/wmc/index.html `PRIMARY` (list of documents).

## (a) The 2020 attempt (Heinzmann, Matteotti, Liniger, Viveksanth)

**Not found.** Six searches (the four surnames together and in pairs, "Kandiah Viveksanth", "Peter Heinzmann"
with Telegramm/Kryptologie/HSR, "Carlo Matteotti" with Kryptologie/cnlab, the book title with Oswald and
Salamanca) returned nothing on the attempt. Cryptiana's 2023 post does not mention it
(https://cryptiana.blogspot.com/2023/09/a-telegram-from-switzerland-1937.html, `SECONDARY`, fetched).

What is confirmed: Bourdeau's notes give the full names as **"Peter Heinzmann, Carlo Matteotti, Patrick Liniger
and Kandiah Viveksanth"**, say Bochsler's note 44 records it as a **failed** 2020 attempt, and say "their report
was not found online" (https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/targets/blume/NOTES.md,
`CLAIMANT`, fetched). Nothing is known of what they tried.

What would breach this: note 44 itself (Bochsler, *Nylon und Napalm*, 2022, a print book; not online to us), or a
direct question to Bochsler or to the four. The name Peter Heinzmann matches a Rapperswil (HSR/OST) networking
professor and founder of cnlab, but no source links that person to this attempt; that is a guess, not a finding.

## (c) Weierud on German hand ciphers, and other Oswald traffic

- **Weierud's 1936–45 history:** not found online. His public pages (cryptocellar `wmc/index.html`, fetched) list
  no German manual-cipher document before 13 January 1940 (the "Allgemeine Vorschrift für alle
  Schlüsselverfahren"). The forthcoming history is mentioned only in Ostwald & Weierud, *Cryptologia* 2022, n. 1
  (already in context-cribs §1). So **we still have no document of what German hand transposition, if any, was in
  use in 1936–37.**
- **New, relevant to the "15 to 25" question:** the cryptocellar list describes the 1944 Rasterersatzverfahren as
  double columnar with a numerical key of 20 to 25 numbers. That is a real German figure, but from December
  1944, not 1937. It does not support Bourdeau's claim for 1937.
- **Other Oswald cipher traffic:** none found. One search (Werner/Viktor Oswald, Bundespolizei, telegrams, Spain,
  Emser Werke) returned nothing. The only known traffic is the two telegrams in BAR Dossier 66.

## What this means for H4 and H5 (our reading, not a source)
- The literature a 1937 Swiss amateur could buy offers no system that is both documented and keeps 4–6-letter runs
  inside one message, except word transposition and row-reading routes.
- The cheapest mechanism for the shared strings is Givierge's p. 112 effect: **the same table key on both messages
  with a common opening (or closing)**. Under a single table this gives shared column tops; under a route read by
  rows it gives shared row runs. The H5 test in NEXT.md item 2 should check both, and also reversed matches.
- The turning grille is worth one length check: T2 fits a 4×4 grille exactly (10 blocks); T1 needs nulls.

## Unverified claims
- That Lange & Soudart (1925) describe the Cadenus cipher: one software help page says so. The book was not
  read. Cadenus is usually associated with American Cryptogram Association practice; treat the attribution as
  doubtful.
- What Lange & Soudart (1925) say about transpositions in general: not read. Bibliographic details (Alcan, Paris,
  1925 or 1926) and "Soudart was the Chief of the French Army's Cipher Section" come from a search summary of
  bibliotheques-numeriques.defense.gouv.fr, not opened.
- "Before the Second World War Switzerland had no expertise in cryptography": a search summary (watson.ch /
  swissinfo, citing Rudolf J. Ritter), not opened.
- Swiss Enigma D/K purchases from 1938 (HAMFU): from a search summary, not opened.
- Nihilist transposition (rows and columns permuted by one key) as a period system: not found in Langie or
  Givierge by our text search; not otherwise checked.
- German commercial or private cipher handbooks of the 1920s–30s describing transpositions: none found in the
  budget. Not searched in German book catalogues.
- That the Peter Heinzmann of note 44 is the HSR/cnlab professor: a guess from the name.
- Page numbers for Givierge are from the archive.org OCR running heads (93, 94, 112) and are approximate for the
  word-transposition and grille passages.
