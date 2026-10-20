# Encryption procedure evidence for a 1937 Zurich-to-Salamanca cipher telegram

Compiled 2026-10-20 by the procedure research agent. Read-only research, about 40 searches and fetches. Builds on
`sources/conventions-survey.md`, `sources/key-type-survey.md` and `sources/context-cribs.md` sections 1-2 and does not
repeat them. Calibration texts are in the separate file `calibration-telegrams.md`. Tiers follow AGENTS.md rule 1.
English is given beside every non-English quotation.

**Connected-to-Oswalds** means a document ties the item to Viktor or Werner Oswald, Patvag, or the BLUME/Salamanca
correspondence. **Available-only** means it existed in Europe before January 1937 and a person in their position could
have met it. **Nothing in this file is of the first kind.** No document found names a cipher method, a key, or a
handbook used by either brother.

## Summary

1. **Key numbering from a keyword: confirmed in a source the Oswalds could have bought (Givierge 1925).** The worked
   example is key MARSEILLE, numbered 7 1 8 9 2 4 5 6 3. The two E's, two L's are numbered left to right (E=2 then
   E=3, L=5 then L=6). We re-ran it by script: the rule reproduces Givierge's printed cryptogram
   `AIRIX SREPS IIAEO CMNEL DAOSV TRIII` exactly. The same page shows the table left incomplete (30 letters, 9
   columns, last row of 3), with **no filler**. Parker Hitt (1916) gives the same alphabetical numbering for MEXICO
   (4 2 6 3 1 5), no repeated letters. Langie (1922) gives only a numeric key (2, 6, 4, 1, 5, 3), no word rule.
   The left-to-right rule for repeats is also the modern textbook rule (Pommerening, FARAD = 4 1 5 2 3). Computational
   consequence: a keyword key should be tried with the stable left-to-right tie-break first.
2. **Spanish-specific preparation rules, from 1916: no accents, no N-tilde, no K or W.** Hitt says Spanish cipher texts
   use the 24-letter alphabet A B C D E F G H I J L M N O P Q R S T U V X Y Z, the receiver supplying accents and tilde.
   This matches the "no W" in both telegrams. It is a US army handbook describing Mexican traffic, not Spanish or Swiss
   practice. Available-only, and 21 years early.
3. **X as filler or stop in Spanish cipher examples, 1916: two instances.** Hitt's Spanish transposition example
   ends `...ORDENES FINISX` and a Spanish substitution example ends `NOCHE X.` Hitt's third has "(X) Fin". Available-only.
   Together with the 1930 German Enigma example already in `conventions-survey.md`, this strengthens "X is a plausible
   stop or filler" but gives no rule for a transposition.
4. **Nationalist censorship may have banned code outright in autumn 1936.** US Ambassador Bowers telegraphed on
   12 Sep 1936 that the rebel authorities at Burgos had told the military authorities at Vigo that "no messages in
   code shall be permitted". We have one secondary report of an instruction to one port, not the order itself, and
   no evidence on whether it covered a Zurich-to-Salamanca telegram in January 1937 (these two telegrams did pass).
   If code and cipher were barred on this route, the senders had a reason to use something that looked like plain
   five-letter code words. This is a lead, not a finding.
5. **Double transposition in non-military literature before 1937: found only as a named variant, not as commercial
   practice.** Givierge (1925) says "works on cryptography" use "double transposition" for a table written by a keyed
   column order with rows also keyed, and that the name is "sometimes" used for what should be called
   "retransposition". Hitt (1916), Case 2-c, says rows-and-columns rearranged "by means of a key word or key words" is
   "not infrequently met with because it seems to offer safety by use of two key words". Both are available-only.
   No commercial or banking user was found.
6. **Not reachable:** Sacco (1936), Lange and Soudart (1925), any Spanish manual 1900-1936, any Swiss or German
   commercial handbook. See Gaps.

## Findings table

| # | Finding | Exact text | Date | Source and locator | Tier | Original read? | Link to Oswalds | Computational consequence |
|---|---|---|---|---|---|---|---|---|
| 1 | Keyword to numeric key; repeated letters numbered left to right; incomplete table, no filler | "we choose a key, usually literal, and transform it into a numerical key" (on key MARSEILLE; numbers printed `7 1 8 9 2 4 5 6 3` in the OCR as "71892456 3"). Example text "LA SIXIEME DIVISION PARTIRA CE SOIR", 30 letters, "three complete rows and 3 letters left over". French source, English translation. | 1925 | Givierge, *Cours de cryptographie*, pp. 94-95, https://archive.org/details/french-colonel-marcel-givierges-1925-book-cours-de-cryptographie-cryptography-course (djvu text downloaded and searched) | SCHOLARLY | y (text of English translation) | Available-only | Key numbering: sort key letters, ties by position, left to right. Verified by script against the printed cryptogram. Table not padded: ciphertext length need not be a multiple of the key length. |
| 2 | "Double transposition" defined; "retransposition" is a separate thing | "Under the title of double transposition, the said works allude to cases where the columns are inscribed in the table in an order determined by a key, and where the letters in each column are inscribed not from top to bottom ... but in an order likewise determined by a key, the same or different. (Sometimes the name 'double transposition' is used for another system which should be called 'retransposition.')" | 1925 | Givierge, p. ~94 (ch. on tabular transpositions, text at line 15145 of the djvu file) | SCHOLARLY | y | Available-only | In 1925 "double transposition" can mean a column permutation plus a within-column permutation (one table, two keys), not two successive columnar passes. Worth a hypothesis: the BLUME cipher could be one table with row and column keys. |
| 3 | Retransposition (several successive simple transpositions) described | "A simple transposition system may be applied several times, for example, the tabular system, and 2, 3, etc., transpositions may be made ... in the majority of cases, we must resort to anagramming as the only method of solution." | 1925 | Givierge, "Retranspositions", p. ~116 (djvu line 17576) | SCHOLARLY | y | Available-only | Two successive columnar passes are a recognised idea, with no key rule given. |
| 4 | Keyword to numbers, no repeated letters | "It was probably MEXICO 4 2 6 3 1 5, meaning that the 4th column of the plain text was transferred in enciphering so it became our 1st" | 1916 | Hitt, *Manual for the Solution of Military Ciphers*, Case 2-a, https://www.gutenberg.org/files/48871/48871-0.txt (downloaded, searched) | SCHOLARLY | y (plain text) | Available-only | Alphabetical numbering of a keyword; Hitt's solver speculates about the key word but does not need it. |
| 5 | Rows and columns both rearranged, by key words, "not infrequently met with" | "Case 2-c. In this case, both lines and columns are rearranged by means of a key word or key words ... This cipher is not infrequently met with because it seems to offer safety by use of two key words and by the great but only apparent complexity of the method." | 1916 | Hitt, Case 2-c | SCHOLARLY | y | Available-only | Supports a row-and-column variant as a historically common amateur choice. Hitt solves such ciphers by arranging columns, then rows. |
| 6 | Padding rule for rectangles | "the necessity of filling up a rectangle with nulls if the number of letters of the message is just a little greater than a multiple of the rectangle" | 1916 | Hitt, Case 1 (geometric transposition) | SCHOLARLY | y | Available-only | Rectangles with nulls are for complete-rectangle (route) methods. Hitt's own columnar examples (Case 2-b: 105 letters, 3 x 7 x 5) show no nulls. Conflicts with Givierge's unpadded columnar table only in method, not in advice. |
| 7 | Spanish cipher alphabet: no accents, no N-tilde, no K or W | "Accented vowels and Ñ are also not found and we may, in general, say that a cipher whose text is Spanish will be prepared with the following alphabet: A B C D E F G H I J L M N O P Q R S T U V X Y Z, and the receiver must supply the accents and the tilde" | 1916 | Hitt, "Data for the Solution of Ciphers in Spanish" | SCHOLARLY | y | Available-only. Describes Mexican army and secret-service traffic. | The letter set of a Spanish transposition cryptogram: no K, no W, no N-tilde. Both BLUME telegrams have no W. Check whether either contains a K. Hitt also notes the rare letters H, X, Z are raised by Mexican place names. |
| 8 | X as stop or end filler in Spanish cipher examples | H1: `...ALLI ESRERO ORDENES FINISX` (as printed; ESRERO is Hitt's text, probably a slip for ESPERO, "I await"). H4: `PARA EL ATAQUE CONTRA TORREON ORDENO QUE SUS TROPAS MARCHEN ESTE NOCHE X.` ("For the attack on Torreon I order your troops to march this night.") H3: `... un ciclista (X) Fin.` | 1916 | Hitt, Cases 1-f, 4-b special solution, and the TOLEDO example; see `calibration-telegrams.md` H1, H3, H4 | SCHOLARLY | y | Available-only; probably constructed | X as a trailing letter, in plain Spanish telegraphic style. Does not show an X inside the text. |
| 9 | Code messages banned by Nationalist authorities, Sep 1936 | Bowers, St. Jean de Luz, 12 Sep 1936: the rebel authorities at Burgos had told the military authorities at Vigo that "no messages in code shall be permitted" (the US Vice Consul's protest "unavailing"). | 12 Sep 1936 | FRUS 1936 vol. II, doc. 719 (file 852.721/5), https://history.state.gov/historicaldocuments/frus1936v02/d719 (fetched; paraphrased by the fetch tool, not read as a facsimile) | PRIMARY (published diplomatic telegram, a report of an order, not the order) | y (printed edition) | Context for the Burgos end of the route; not tied to the Oswalds | If cipher was barred in Nationalist Spain, a five-letter-group transposition passes only if the censor saw it as CDE "artificial words" (Art. 10, see `context-cribs.md`). Ask: did the telegrams carry the Cde stamp? (T2 did, per `headers.md`.) |
| 10 | Spanish army rules for cipher telegrams, July 1935 | "Los telegramas se cifrarán siempre por completo" (telegrams are always to be ciphered in full, never mixing plain and cipher); courtesy formulas barred; "Se cuidará de enmascarar la gran frecuencia de las letras E y A" (care is to be taken to mask the high frequency of the letters E and A); no re-encryption under a second cipher; no phone calls to clear up cipher doubts | Jul 1935 | Instructions of Subsecretario Fanjul, War Ministry, original in the Archivo Militar de Avila, as summarised in Boletin ENIGMA 11, https://www.ugr.es/~aquiran/cripto/enigma/boletin_enigma_11.htm (HTML downloaded; summary only, original not seen) | SECONDARY | n | Available-only, and concerns a number-group substitution key, not transposition | Shows Spanish army practice of 1935 was substitution with number groups, plain text and cipher not mixed. Nothing about transposition. |
| 11 | Keys from literature in a double-transposition programme | "The 'Schlüssel-Losungen' (key phrases) for K1 and K2 were based on parts of German literature." (Leiberich's letter to Lasry, Stasi agent traffic.) | c.1950s-65 | Lasry, PhD thesis, Kassel 2018, section 9.3, https://www.uni-kassel.de/upress/online/OpenAccess/978-3-7376-0458-1.OpenAccess.pdf (downloaded, text searched) | SCHOLARLY | y | Available-only, 20 years late and a different user | Not 1937 evidence. Only shows that keys drawn from running text were the intelligence-service practice later. |
| 12 | Kullback's dictionary attack on double transposition assumes keys derived from words | "his book includes a dictionary attack, where keys are derived from words" | 1930s-40s original; 1980 reprint | Lasry thesis, section 9.2 (describing Kullback) | SCHOLARLY | n (Kullback not read) | Available-only | Supports trying keyword-derived keys first. Kullback's date was not checked. |
| 13 | Left-to-right tie-break as the modern textbook rule | "bei gleichen Buchstaben der erste die niedrigere Nummer bekommt" (for equal letters the first gets the lower number); FARAD gives 4 1 5 2 3 | modern | Pommerening teaching pages, search summary, https://www.staff.uni-mainz.de/pommeren/Kryptologie02/Klassisch/6_Transpos/Beispiele.pdf (not opened) | SECONDARY | n | n/a | Same rule as Givierge. Not independent evidence for 1937. |

## What was asked and not found

- **Lange and Soudart, *Traité de cryptographie*** (Paris, Alcan, 1925; "nouvelle edition" listed 1935): catalogue
  records only (Georgetown, French defence digital library, a bookseller). Not read. Nothing can be said about its
  transposition or key rules.
- **Sacco, *Manuale di crittografia*** (1925, 2nd ed. 1936; English translation 1977/1996): the archive.org copy
  `manualofcryptogr0000sacc` is a lending-library item (restricted); the full-text search endpoint returned 403 and
  we did not circumvent it. One search result says instructions "probably attributed to Sacco" recommended a double
  transposition with a 9-letter key changed daily in Italian WWI practice (Venice historian's paper, search summary
  only, not opened). Not read.
- **Spanish manuals.** The only title found is Garcia Carmona, *Tratado de criptografia con aplicacion especial al
  Ejercito* (Madrid, 1894; Ministry of Defence facsimile 2011), described by the publisher as covering "the methods
  known at the time" and criticising the official military cipher. The sellers' page does not say whether it covers
  transposition. No 1900-1936 Spanish handbook, no Spanish army "Reglamento" on cipher (apart from the 1935 Fanjul
  instructions), and no Spanish translation of Givierge, Sacco or Lange was found.
- **Swiss or German commercial handbooks ("Geheimschrift fuer Kaufleute"), bank test keys, bank cipher practice:**
  nothing. Searches returned only Swiss army material from after 1938 and modern teaching pages.
- **Nationalist Burgos practice on numbers, N-tilde, STOP/PUNTO, nulls, indicators in cipher telegrams 1936-37:**
  nothing beyond finding 9 above and the plain-language STOP example already in `context-cribs.md`.
- **Anything tying a method to Viktor or Werner Oswald:** nothing.

## Search and fetch log

Numbers are in order. "Result" says what was usable.

| # | Query or URL | Site | Result |
|---|---|---|---|
| 1 | Sacco Manuale di crittografia 1936 trasposizione doppia chiave | web | Bibliographic only; Venice notebook note on Italian WWI double transposition (not opened) |
| 2 | Sacco Manual of Cryptography double transposition key numbering | web | Nothing from Sacco |
| 3 | manual de criptografia Espana 1920s 1930s transposicion Ejercito reglamento | web | Nothing on a manual; pointers to Boletin ENIGMA and the Fanjul 1935 rules |
| 4 | Lange Soudart Traite de cryptographie 1925 | web | Catalogue records only |
| 5 | archive.org advanced search: Sacco; Spanish and French titles 1900-1940; German Geheimschrift | archive.org API | Sacco lending copy only; Givierge and Langie confirmed; no Spanish or German handbook |
| 6 | Biblioteca Virtual de Defensa criptografia manual | web | Nothing |
| 7 | scienceblogs.de, Spanish cipher mid-20th century | WebFetch | 1945 prison-service strip cipher, not relevant |
| 8 | working.mde.es article on criptografia | WebFetch | DNS failure |
| 9 | ugr.es/~aquiran/cripto/museo.htm | WebFetch | No 1890-1939 Spanish handbook listed |
| 10 | Quirantes, Spanish books on cryptography | web | Garcia Carmona 1894 only |
| 11 | Malaga archive "Criptografia" PDF; polifemo.com Carmona; revistas.ucm.es Galende | WebFetch x3 | Generic text; Carmona book blurb; Galende on Latin America, not relevant |
| 12 | Google Books API (4 queries) | googleapis.com | HTTP 429, no results |
| 13 | Sacco full-text search endpoint on archive.org | archive.org | HTTP 403; stopped |
| 14 | Burgos 1937 telegramas cifrados prohibidos particulares | web | FRUS 719 (Burgos code ban); Boletin ENIGMA 11 |
| 15 | Spanish Civil War private cipher telegrams banned | web | Same, plus Ziffren acrostic anecdote (not used) |
| 16 | FRUS 1936 doc 719 | WebFetch | 12 Sep 1936 Bowers telegram |
| 17 | Boletin ENIGMA 11 | WebFetch | July 1935 Fanjul instructions; 26 Jul 1936 Las Palmas telegram |
| 18 | Nationalist 1937 commercial telegrams code plain language | web | Nothing |
| 19 | suspension lenguaje secreto telegramas Espana 1936 | web | 1977 BOE only (post-dates; not used) |
| 20 | ugr.es gce01.htm | WebFetch | Images and captions only |
| 21 | FRUS 1937 doc 550 | WebFetch | Not relevant |
| 22 | telegrama 1936 texto Franco Mola | web | Palma newspaper telegrams on prensahistorica (OCR, fetch refused) |
| 23 | telegramas comerciales lana 1934-36 | web | Nothing |
| 24 | PARES telegrama digitalizado 1936 | web | USF scans; Aguirre-Irujo 1938 in Vasconia |
| 25 | Vasconia 467/459 (WebFetch, urllib, Playwright) | eusko-ikaskuntza | HTTP 400 every time |
| 26 | USF span_civil_war/74 and its PDF | WebFetch, urllib, Playwright | Metadata only; PDF refused |
| 27 | Playwright navigation to the Vasconia article (see 25) and USF | Playwright | Closed |
| 28 | Pochat 2008 PDF | olivar.fahce.unlp.edu.ar | Downloaded; full telegram text |
| 29 | wikisource telegrama 1936 | web | Nothing |
| 30 | telegrama comercial 1933-35 transcripcion | web | Nothing |
| 31 | Hisma/Rowak/Bernhardt telegram Burgos | web | Nothing |
| 32 | prensahistorica path=65336; memoriademadrid attachment | WebFetch x2 | HTTP 429 and 403 |
| 33 | Quirantes: Boletin 11 page for Las Palmas telegram | WebFetch | Ciphertext digits; five words of plaintext |
| 34 | Clave X Mar Cantabrico telegramas descifrados | web | marcantabrico.htm, Boletin 14 |
| 35 | marcantabrico.htm, boletin_enigma_14.htm, boletin_enigma_11.htm | WebFetch then urllib | Full text of M1-M8 and the Gordon Ordas instructions |
| 36 | Lasry thesis PDF | uni-kassel.de | Downloaded; sections 9.1-9.3 on double transposition |
| 37 | Givierge and Langie djvu text | archive.org | Key numbering example MARSEILLE; "double transposition" and "retransposition" passages |
| 38 | Chiffrierung Geheimschrift fuer Kaufleute Spaltentransposition | web | Pommerening rule; no period handbook |
| 39 | Swiss bank 1930s cipher telegram test key | web | Nothing relevant (post-1938 Swiss army only) |
| 40 | Hitt 1916 and Friedman transposition | web, gutenberg.org | Hitt full text downloaded; Spanish examples, Case 2-c; Friedman not opened |

## Gaps (what would close them)

1. **Sacco 1936 and Lange-Soudart 1925/1935, full text.** A library with the physical books or a legitimate
   lending copy. Sacco is the likeliest handbook to name double transposition and a keyword rule for a Spanish or
   Swiss reader of the 1930s (Italian army practice).
2. **Anything on the Oswalds' own habits.** Burgos or Zurich business archives, or the Federal Archives dossier's
   covering letters (the dossier images were not searched for a key reference; `headers.md` and `PROVENANCE.md`
   describe what was read). The Bochsler outreach (`outreach-bochsler.md`) is the person most likely to know.
3. **The Nationalist telegraph rule for code and cipher, autumn 1936 to early 1937.** The Spanish Telegraph
   Service's circulars or the Nationalist official bulletin for 1936-37. Without it finding 9 cannot be applied to
   the Zurich route.
4. **A Spanish handbook 1900-1936.** Garcia Carmona 1894 could be checked in the 2011 facsimile; the BNE Biblioteca
   Digital Hispanica was not reachable by our tools.
5. **Commercial calibration telegrams.** See `calibration-telegrams.md`; none found.

## Unverified claims

- Finding 9 rests on a published US diplomatic telegram as read through a fetch tool's paraphrase; the exact
  wording "no messages in code shall be permitted" is the tool's quotation of the telegram.
- Finding 10 (Fanjul 1935 rules) is from Quirantes' summary; the Avila original was not seen. The remark that the
  rule set covers number-group substitution is our reading of the summary.
- The OCR of Givierge's key line reads "71892456 3"; we read it as `7 1 8 9 2 4 5 6 3` because that reproduces the
  printed cryptogram when run, which is a check on our reading, not a view of the page image.
- The Sacco WWI double-transposition remark (9-letter key changed daily) is a search-engine summary of a paper we
  did not open.
- Hitt's examples may be constructed. His statement that most of the "hundreds of actual cipher messages" he saw
  were Mexican army and secret-service traffic is the only provenance claim.
- A "Caruncho Method" Spanish police cipher was mentioned by a blog commenter (scienceblogs.de); not checked, and
  probably unrelated.
