# Conventions survey: stops, fillers, indicators, charging and digits (1918–1937)

Compiled 2026-10-16. Read-only research: about 15 searches and fetches. Three of the fetches were full texts,
searched locally: Givierge, *Cours de cryptographie* (1925, English translation), Langie, *Cryptography* (1922
English edition, with an appendix by the translator J. C. H. Macbeth), and the Madrid Telegraph Regulations
(1932) in League of Nations Treaty Series vol. 151. This file builds on `key-type-survey.md` and
`context-cribs.md` and does not repeat them. Tiers follow AGENTS.md rule 1.

Terms used here. A **stop** is a letter that carries a meaning (full stop, word break). A **filler** is a letter
added to complete a table or the last group. A **null** is a meaningless letter placed anywhere else in the text.

**Summary.** (1) **X as a stop: found for the German army by 1930.** The 1930 Enigma test message separates its
sentences with X. English Playfair practice in 1922 used X (or Z) as a divider and a filler. French (1925) and
Spanish (1937) telegrams used the word STOP. Nothing Swiss was found. (2) **Fillers: found in Givierge and in
Macbeth's appendix.** Columnar tables were normally left incomplete, with no filler. Grilles and code groups were
padded. Macbeth names X or Z, then a prearranged word such as STOP. Lange & Soudart is not online, and no German
handbook was found. (3) **Indicators: partly found.** Check words in bank telegrams went first, and strip-cipher
indicators went at the head of the message. **No final reference group and no "REF" convention was found.**
(4) **Charging: the rules were found; the Swiss tariff was not.** Under the 1932 rules, any letter group of five
letters or fewer meets the definition of code language. So five-letter cipher groups could be charged as CDE. The
two fees per word are within 3% of each other, which does not fit "T1 at full rate, T2 at CDE rate". (5)
**Digits: partly found.** The rules forbade mixing letters and figures in a secret group. Period examples spell
numbers out. No source for the QWERTYUIOP top row or for a figure-shift letter was found.

---

## 1. X as a full stop or separator

| Finding | Source | Tier |
|---|---|---|
| **German army, 1930.** The test message of the *Schlüsselanleitung zur Chiffriermaschine Enigma I* ("key instructions for the Enigma I cipher machine", seemingly 1930) reads "FEINDLIQE INFANTERIEKOLONNE BEOBAQTET **X** ANFANG SUEDAUSGANG BAERWALDE **X** ENDE DREI KM OSTWAERTS NEUSTADT" ("Enemy infantry column observed. Head at the south exit of Bärwalde. Tail three km east of Neustadt."). X stands where the full stops go. CH is written Q. The page states no rule; the usage is shown, not prescribed. The English translation is at TNA HW 25/9. | Weierud, https://cryptocellar.org/enigma/e-message-1930.html (fetched) | `SCHOLARLY` (Weierud's page; the message text is from a 1930 instruction) |
| **German Wehrmacht, undated rule.** "Dabei werden Satzzeichen durch „X“ ersetzt" ("punctuation marks are replaced by X"). Also "Eigennamen verdoppelt und in „X“ eingeschlossen" ("proper names doubled and enclosed in X"). The fetch did not capture the footnote, so the rule is undated here. | https://de.wikipedia.org/wiki/Enigma_(Maschine), note 26 (fetched; first half of the page only) | `SECONDARY` |
| **German Navy, 1940.** The translated 1940 general procedure (M.Dv. 32/1) is online, but the page we opened (paras 98–107) holds no plaintext rules. We did not find the paragraph that states the X rule. | https://www.codesandciphers.org.uk/documents/egenproc/page20.htm (fetched) | `PRIMARY` (translation) |
| **English Playfair practice, 1922.** "The decipherer should never neglect to write down the X or Z, as the case may be, when used as a divisory letter." X or Z splits doubled letters and fills up a group (see §2). This is a divider inside letter pairs, not a full stop. | Macbeth, "The Playfair Cipher System, etc.", appendix to Langie, *Cryptography* (1922), pp. 168–169, https://archive.org/details/cryptographylang00lang | `SCHOLARLY` (handbook) |
| **French military, 1925: STOP, not X.** Givierge's worked plaintexts are French army orders that use the word STOP: "LE SEPTIEME CORPS SE PORTERA DEMAIN SEPT DECEMBRE DE BLESMES SUR ROBERT-ESPAGNE STOP" ("The Seventh Corps will move tomorrow, 7 December, from Blesmes to Robert-Espagne. Stop."), p. ~61. Also pp. ~66–67 and ~79. | Givierge 1925, https://archive.org/details/french-colonel-marcel-givierges-1925-book-cours-de-cryptographie-cryptography-course | `SCHOLARLY` (handbook) |
| **Commercial code telegrams.** "Many correspondents end their messages with 'period' (line 31) …", and "Telegrams often end with a punctuation mark." In code, the stop is a codeword. | Givierge, pp. ~130 and ~143 | `SCHOLARLY` |
| **Telegraph rule: X as the multiplication sign.** "The multiplication sign (x) is admitted … It is replaced in transmission by the letter X, which is counted as a separate word." This is a plain-language rule, not a stop. | Madrid Telegraph Regulations 1932, Art. 12 §5, LoN TS 151, p. 59, https://treaties.un.org/doc/Publication/UNTS/LON/Volume%20151/v151.pdf | `PRIMARY` |
| **Spanish counterpart:** nothing new. The one 1937 Spanish example remains STOP in plain language (Pochat 2008, `context-cribs.md` §2). One Spanish search found no cipher manual. | search, 2026-10-16 | — |
| **Swiss counterpart:** none found. The Réglette page gives no stop rule. | https://cryptomuseum.com/crypto/swiss/reglette (fetched) | `SECONDARY` |

**Answer.** X as a sentence separator is documented in German army practice by 1930, by example rather than by a
written rule we could read. No Swiss, Spanish or French source uses X this way. The French and Spanish
counterpart was the word STOP.

## 2. Nulls and fillers (1918–1937 handbooks)

| Finding | Source | Tier |
|---|---|---|
| **Columnar tables are normally incomplete, with no filler.** "The letters are inscribed in them in rows of equal length (save sometimes the last) … When the last line is equal in length to the others, the table is said to be 'completely filled.' When it is not, the table is called 'incompletely filled.'" The worked example (LA SIXIEME DIVISION PARTIRA CE SOIR, key MARSEILLE) has 30 letters in 9 columns, a last row of 3 letters, and no filler. "We will usually meet with it in sets of five letters." | Givierge, pp. 94–95 | `SCHOLARLY` |
| **Block transposition: leave the remainder short.** "We shall skip the sets or letters missing at the end of the message when we get to the last set, if it is incomplete." | Givierge, p. 94 | `SCHOLARLY` |
| **Grilles: pad the last block with nulls.** "We have to divide up the text into sets equal to this number of cells, filling in the last part with nulls. The property of messages always having a length equal to the same number — a perfect square — indicates the use of a revolving grille." | Givierge, p. ~109 | `SCHOLARLY` |
| **Nulls in substitution: rare letters, or at the start.** Nulls "placed at the beginning … do not cause any serious trouble". Letters absent from the cipher table can serve as nulls: "J, K, and W are replaced by I, C, and V in the clear. Hence, the decipherer scratches out all the J's, K's, and W's." | Givierge, pp. ~50–51 | `SCHOLARLY` |
| **Playfair: nulls also separate words.** "We introduce nulls into the plain text to prevent the formation of a digraph by a repeated letter, as well as to separate words if deemed necessary (punctuation, ease of reading, etc.)." No letter is named. | Givierge, p. ~85 | `SCHOLARLY` |
| **Code in fives: the short last group.** "When the final group does not contain five digits, some correspondents leave it as it is or complete it with zeros, which attracts attention. But some take the precaution to complete it with null digits other than zeros." | Givierge, p. ~131 | `SCHOLARLY` |
| **Playfair fillers named: X or Z, then a prearranged word.** "The letter agreed upon for the purpose of dividing repeated letters may be used to fill up a group. Should more than one letter be required to complete a group, as many letters as are required may be taken from a prearranged word, such as STOP, FINISH, etc." The worked example uses Z as divider and "STOP to complete an unfinished group". | Macbeth, appendix to Langie (1922), p. 168 | `SCHOLARLY` |
| **Swiss army Réglette: random digits.** "If the last group is partly unused, it should be padded with random digits." Messages of "more than 15 to 20 words" were split into parts, each under a new key number. The page credits Hütter (personal correspondence, 2017), so the rule may not be the 1918–39 wording. | https://cryptomuseum.com/crypto/swiss/reglette | `SECONDARY` |
| **Lange & Soudart, *Traité de cryptographie*:** not read. It is not on archive.org, and no digitized copy turned up. Catalogue records give Paris, Alcan, 1925 (Georgetown) or 1926 (Bibliothèque numérique de la Défense). A bookseller lists a "nouvelle édition" (new edition) of 1935. | https://findingaids.library.georgetown.edu/repositories/14/archival_objects/1424681 ; https://www.maremagnum.com/en/libri-moderni/traite-de-cryptographie/162588022 (search results, not opened) | `SECONDARY` |
| **German handbook or military instruction, 1918–37:** none found. | — | — |

**Answer.** The handbooks a 1937 reader could buy leave an incomplete columnar table as it is, with no filler.
They pad grilles and code groups. Only the English Playfair appendix names filler letters: X or Z, then a
prearranged word. None of these sources prescribes X as a transposition filler.

## 3. Indicator, reference and check groups

| Finding | Source | Tier |
|---|---|---|
| **Bank check words go first.** Plain language keeps its status despite "a check word or check number placed at the beginning of the text in bank and similar telegrams" (Art. 9 §2). It is "the first word of a plain language text" and may not "exceed five letters or five figures" (Art. 20 §1(3)). | Madrid 1932, LoN TS 151, pp. 57 and 69 | `PRIMARY` |
| **Office serials and preamble data are not charged; the sender's own references are.** "The nature of the telegram, the name of the office of origin, the number of the telegram, the date and time of handing-in, the service instructions … route indications … are not charged." If the sender puts them in the text, "they are then comprised in the number of chargeable words." | Madrid 1932, Art. 18 §2, p. 67 | `PRIMARY` |
| **Strip-cipher indicators at the head.** "The position was shown by placing, at the head of the message, an indicator." | Givierge, pp. 23–24 | `SCHOLARLY` |
| **Typical endings in commercial code:** "period", "best regards", "letter follows". Typical openings: "I have received", "answer". "Signatures are found at the ends often preceded by a punctuation" mark. | Givierge, pp. ~130 and ~143 | `SCHOLARLY` |
| **A final group used as a reference or serial number:** not found. | — | — |
| **"REF" plus two letters as a telegram convention:** not found. The 1932 Regulations' list of paid service indications has no REF (we read Art. 14 only in passing; see Unverified). | — | — |

**Answer.** The period sources put check words and indicators first, at the head of the text. We found no source
for a final reference group, and none for REF.

## 4. Charging

**The rules (Madrid 1932, LoN TS 151, `PRIMARY`, read in full for these articles):**
- **Art. 10 §2(2), p. 57.** "The code words, whether real or artificial, must not contain more than five letters;
  they may be formed in any way."
- **Art. 10 §3–4, p. 57.** "The officer who accepts a telegram in code language enters on the form the service
  instruction = CDE =." CDE is charged at "7/10ths of the full rate in the case of the European system" and 6/10
  for the extra-European system.
- **Art. 11 §1(2), p. 59.** Cipher language is "words, names, expressions or combinations of letters … not
  fulfilling the conditions of plain language (Art. 9) or code language (Art. 10)."
- **Our reading:** a group of five letters or fewer, "formed in any way", meets the conditions of code language.
  By Art. 11, letter cipher in the Regulations' sense means groups longer than five letters. **So five-letter
  cipher groups could be accepted and charged as CDE.** The text does not say this in so many words; it follows
  from the two definitions.
- **Art. 26 §3, p. 81.** CDE telegrams pay at least five words. In the European system, "each Administration has
  the right to impose a minimum charge which must not exceed one franc fifty (1 fr. 50) per telegram, or to collect
  the charge in any way convenient to it".
- **Art. 25 §4, p. 79.** "A telegram is subject to the rules of the European system when it passes exclusively over
  the communications of countries belonging to that system."
- **Art. 27 §1, p. 81.** European ceilings, in gold francs per word: 0.12 terminal and 0.07 transit for Germany,
  Spain, France, Great Britain and Italy; 0.09 and 0.07 for the other countries of Europe, Switzerland among them.
  Cable rates come from Table A, which is not in vol. 151. **Art. 27 §6:** a sender who prescribes the route "must
  pay the charge proper to that route".
- **Art. 18 §1, p. 65.** Route indications are not counted. This fits T1's 125 = 123 groups + 2 address words;
  the struck "VIA VIGOEMDENKABEL" was not charged.
- **Art. 18 §4, p. 67.** "The counter officer marks with a cross the last word of each section of fifty actual
  words …, the paid service indications and the words in the address being included in the first section." **This
  is the rule behind T1's pencilled (50) after group 48 and 100 after group 98** (`headers.md`).
- **Article numbers.** `context-cribs.md` §2 cites "Art. 19 §3" for counting cipher at five characters to the word.
  In our reading the rules are Art. 18 §7 (groups of letters at five characters to the word) and Art. 20 §3(3)–(4)
  (p. 71). Art. 19 counts the address.

**The Swiss tariff:** not found. One search in German found no Swiss PTT word rate for Spain in 1936–37, direct or
via London.

**Arithmetic, only from rates we can cite** (the 7/10 factor above; the 0.47 per word on T2's reverse,
`headers.md`, `PRIMARY`):

| Test | Expected | Observed | Fits? |
|---|---|---|---|
| Fee per word | — | T1 49.90 / 125 = 0.3992; T2 14.00 / 34 = 0.4118 | within 3% of each other |
| T1 at full rate, T2 at CDE (7/10) | T2 = 0.7 × 0.3992 × 34 = 9.50 | 14.00 | **no** |
| 0.47 is the full rate; both at CDE (7/10) | 0.329 per word: T1 41.13, T2 11.19 | 49.90, 14.00 | **no** |
| 0.47 is the rate for both | T1 125 × 0.47 = 58.75 | 49.90 stamped; T1's reverse has "59.05 (?)" below a rule | a lead, see below |
| Ratio stamped / (0.47 × words) | 0.70 (CDE) or 1.00 (full) | T1 0.849; T2 0.876 | neither |

What the arithmetic shows:
- **The two telegrams were charged at nearly the same rate per word.** That fits one charging class for both,
  whatever the class was. It does not fit T1 at full rate and T2 at CDE rate. "Als Chiffriert aufgegeben" did not
  buy T1 a higher rate.
- A common rate per word plus a fixed fee per telegram fits both fees exactly at 0.3945 per word plus 0.59. A
  fixed fee up to 1.50 is allowed by Art. 26 §3(b). The values are not round, so this is a fit, not a tariff. T2's
  reverse also has 16.60 under 15.98, a difference of 0.62.
- **Lead for the dive:** 0.47 × 125 = 58.75, close to the uncertain "59.05" on T1's reverse. The clerk may have
  priced both telegrams at 0.47 first and then reduced both. Reread T1's reverse (c11, c12) with this in mind.

## 5. Digits in letter ciphers

| Finding | Source | Tier |
|---|---|---|
| **No mixing in one secret group.** "The combination, in one group, of figures and letters with a secret meaning is not allowed." A code telegram may carry figure groups up to half its chargeable words; above that it is charged as cipher. A letter cipher therefore had to carry numbers as letters, or as separate all-figure groups. T1 and T2 contain no figures. | Madrid 1932, Art. 11 §2 (p. 59), Art. 10 §5 (p. 57) | `PRIMARY` |
| **German army, 1930: spelled out.** "DREI KM" ("three km") in the 1930 test message. | Weierud, as in §1 | `SCHOLARLY` |
| **German Wehrmacht, undated: digit by digit.** "Zahlen ziffernweise ausgeschrieben" ("numbers written out digit by digit"). | de.wikipedia, as in §1 | `SECONDARY` |
| **French military, 1925: mostly spelled out.** "SEPT DECEMBRE", "UNE HEURE", "SEPT HEURES", "SIX MAI". But the printed plaintexts also show figures: "DEPART A 7 HEURES", "COTE 230". | Givierge, pp. ~61, ~66, ~79 | `SCHOLARLY` |
| **Commercial letter tables, 1922.** Firms marked prices with "some easily remembered word of ten different letters which are used to denote figures. For instance, the word 'bankruptcy' might be employed, B to represent 1, A 2, and so on. An extra letter is generally used in the case of a figure which is repeated." | Macbeth, appendix to Langie, p. ~161 | `SCHOLARLY` |
| **Swiss army Réglette:** the slider carried "the numbers 0-9 and some punctuation characters", enciphered directly to two-digit numbers. | cryptomuseum, as above | `SECONDARY` |
| **Typewriter top row (QWERTYUIOP), figure-shift letter, Spanish or Swiss letter-cipher rule:** not found. | — | — |

**Answer.** Period practice spelled numbers out, and the 1932 Regulations pushed a letter cipher that way. A
ten-letter word table was a known commercial device. The top-row and figure-shift conventions were not found.

---

## What bears on the dive (our reading, not a source)

- **X in T1.** The sources give X three roles: a German sentence separator (1930), an English Playfair divider and
  filler (1922), and the telegraph multiplication sign (1932, plain language). A stop reading needs about five
  sentence breaks in 615 letters, which telegram style allows. A filler reading needs fillers that the transposition
  handbooks do not ask for: they leave columnar tables incomplete. Fillers for the last five-letter group number at
  most four. **Test for `analysis/`:** under a columnar table, fillers that complete the last row land at the ends
  of columns. T1's X's sit at letters 363, 425, 441, 597, 610 and 615, so a script can check whether any width
  puts several of them at column ends.
- **F in T2.** No source uses F as a stop, filler or null. Macbeth's sample filler words (STOP, FINISH) do not fit
  T2 either: T2 has one H.
- **REF in both final groups.** No convention was found. The period sources put check groups and indicators first.
  A transposition rarely sends the last plaintext letters to the last cipher group. So REF.. is either outside the
  transposition (added after encipherment, like Art. 18 §2's sender reference) or a coincidence. Untested.
- **One system or two.** The charging evidence does not separate the telegrams. Five-letter groups qualified as CDE
  under Art. 10. T2 bears the CDE stamp that Art. 10 §3 prescribes. T1, marked "chiffriert", paid nearly the same
  fee per word. The different labels look like clerks' notes on one kind of telegram, not two systems.

## Unverified claims

- **That a written German rule "X = Punkt" (X = full stop) existed before 1937.** The 1930 example shows the usage.
  The rule text we could read (de.wikipedia) is undated. The 1940 M.Dv. 32/1 paragraph was not located.
- **"UD" for the question mark, "Y" for the comma, "XX" for the colon in German Enigma practice:** training-data
  memory only. The de.wikipedia fetch did not mention them. UD matters here because T2 ends REFUD. Do not use it
  as a crib without a source.
- **German top-row digit convention (Q = 1 … P = 0) in navy or air force practice:** memory only, not found.
- **Enigma indicators in the message header (1940 procedure):** search summary only, not opened. Tiltman's 1921
  Russian "DELEGAT" discriminant in the preamble: search summary of
  https://nsarchive.gwu.edu/sites/default/files/documents/4895707/Brigadier-John-H-Tiltman-Experiences-1920-1939.pdf,
  not opened. VIC cipher indicator inserted into the message: 1950s, Scribd summary, not opened.
- **Swiss franc devaluation of 26 September 1936 and how PTT converted gold-franc rates afterwards:** memory, not
  checked. It may explain the odd fee arithmetic.
- **What Lange & Soudart (1925, 1935) say about fillers, nulls and indicators:** not read; no digitized copy found.
- **That Givierge's STOP is in the French original, not added by the translator:** the plaintexts are printed in
  French, so this is likely, but the 1925 French edition was not opened.
- **The Réglette padding and message-splitting rules:** from a 2017 private communication cited by cryptomuseum,
  not from a period instruction.
- **The full list of paid service indications (Madrid 1932, Art. 14):** not read item by item for REF. The service
  instruction list on p. ~113 (CDE, SCDE, FCDE …) was seen only through the search for "CDE".
- **Whether the Eastern route from London to Spain kept the telegram in the European system** (Art. 25 §4) and
  which cable it used: not checked.
- **The meaning of "I A\*" and "II A\*" on the fee stamps, and of "3HW" on T2:** not checked.
- **Page numbers** for Givierge and Macbeth come from the archive.org OCR running heads and are approximate (±1).
