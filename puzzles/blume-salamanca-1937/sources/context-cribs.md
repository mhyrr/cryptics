# Context and cribs for the BLUME SALAMANCA telegrams

Compiled 2026-10-16 for the deep dive. The brief was AGENTS.md, rubric/RUBRIC.md and this dive's README. It is
read-only research: about 24 web searches and fetches, plus a reading of the dossier images.

Tiers: `PRIMARY`, `SCHOLARLY`, `SECONDARY`, `CLAIMANT`, `POPULAR`, as in AGENTS.md rule 1. "Read by us" means
this session looked at the page image or text itself. Letter counts come from Bourdeau's `ct1.txt` and `ct2.txt`.
They match the hashes in the README (`e266615d…`, `8fd5cfb8…`):

| | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 (615) | 58 | 12 | 30 | 24 | 73 | 5 | 9 | 8 | 43 | 2 | 2 | 20 | 24 | 53 | 69 | 35 | 2 | 40 | 39 | 36 | 16 | **3** | **0** | 6 | **2** | 4 |
| T2 (160) | 23 | 2 | 5 | 5 | 19 | 7 | 4 | 1 | 11 | 1 | 0 | 5 | 4 | 14 | 11 | 4 | 0 | 15 | 10 | 9 | 7 | 2 | 0 | 0 | 0 | 1 |

The rare letters are budgets: telegram 1 has room for at most **3 V, 2 Y, 2 Q, 2 K, 2 J, 4 Z, 5 F and 8 H** in all
615 letters. A crib list that spends four V's is wrong somewhere.

---

## 0. New primary observations (dossier images, read by us)

- **T1 carries a typed routing indication that was struck out: `(VIA VIGOEMDENKABEL)`.** In its place the pencil
  note reads "Angleterre Eastern". It went to "London Mcl." at 11 42. The Vigo–Emden cable was the German cable
  route, and the sender's first choice was apparently to route through Germany. Next to the text a pencil note
  reads "als Chiffriert aufgegeben" ("handed in as cipher"). Source: BAR image 527,
  https://image.recherche.bar.admin.ch/iiif/2/0000%2F0357%2F8609%2FSubdossier_0000066%2FUnterlagen_0000072%2F00000527.jpg/full/full/0/default.jpg
  `PRIMARY`. Bourdeau's notes record "via Angleterre Eastern" but not the struck Vigo–Emden line.
- **T2 is stamped `Cde`**, carries "Via angleterre Eastern" and "3HW" in pencil, and gives the sender in pencil as
  "Dr ing. W. L. Oswald" (Werner Leodegar), not "W. E.". Source: BAR image 531,
  https://image.recherche.bar.admin.ch/iiif/2/0000%2F0357%2F8609%2FSubdossier_0000066%2FUnterlagen_0000072%2F00000531.jpg/full/full/0/default.jpg
  `PRIMARY`.
- **Werner Oswald's interrogation of 28 April 1937** (Abhörungsprotokoll, BAR Dokument_0000069, images 501, 503
  and 505, read in full). The points that bear on cribs:
  - Werner and Viktor M. Oswald founded a trading company **in Madrid** after 1932. It dealt "hauptsächlich mit
    Wollexporten" and "Kompensationsgeschäfte" (mainly wool exports, plus compensation deals). **Patvag A.-G.**
    was founded in Zurich in 1933 to support that Spanish business. The Madrid office closed at the outbreak of
    war. Viktor "befindet sich heute … in **San Sebastian**" (in April 1937), "to continue the ongoing wool
    business".
  - The telegrams were sent by Viktor, who was passing through Zurich, and bear his personal signature. The trip
    concerned "Wiedereröffnung eines Bureaus im nationalen Spanien" (reopening an office in Nationalist Spain) and
    a "Wollgeschäft aus dem nationalen Spanien nach der Schweiz" (a wool deal from Nationalist Spain to
    Switzerland). The aim was to bring "schweizerische Exportguthaben die dort eingefroren sind" (Swiss export
    balances frozen there) back into Switzerland.
  - Werner's guess: "dürfte es sich … um **Rücksprachen mit seinen spanischen Wolleinkäufern** handeln" (they
    were probably consultations with his Spanish wool buyers). Viktor wanted to keep the plan from "**Hisma** mit
    Sitz in **Sevilla**" until it had been discussed "mit den spanischen Behörden in **Burgos**".
  - "Den Schlüssel besitze ich ebenfalls nicht, da ich selbst mit meinem Bruder nicht chiffriert verkehre" (I do
    not have the key either, since I do not correspond with my brother in cipher).

  Manifest:
  https://www.recherche.bar.admin.ch/recherche/files/manifests/0000/0357/8609/Subdossier_0000066/Dokument_0000069/_kEy9uWu1p9MZwH671Unxj3.json
  `PRIMARY` (testimony, not plaintext). This agrees with Bourdeau's summary
  (https://github.com/dbourdeau/cyphersolver/blob/main/targets/blume/NOTES.md, `CLAIMANT`) and adds the Madrid
  company, the "Spanish wool buyers" and San Sebastián.

## 1. Transposition systems documented in use, 1936–37

**Summary: we found no document that ties any transposition system to any party in Spain in 1936–37.** The
systems actually documented for the Spanish war are substitution systems and machines. A double transposition is
documented for the German army only before 1927 and from 1940.

### Spanish Nationalists
- **Enigma** (commercial and Heeres models), bought from Germany from November 1936. The Italian, German and
  Nationalist forces used it from then to the end of the war. Source: Soler Fuensanta, López-Brea Espiau and
  Weierud, "Spanish Enigma: A History of the Enigma in Spain", *Cryptologia* 34(4), 2010; author copy at
  https://cryptocellar.org/pubs/enigma-in-spain.pdf. `SCHOLARLY`. The text was searched: the paper says nothing
  about hand transposition systems.
- **The Spanish strip cipher**, a homophonic substitution. Reported as "widely adopted by both sides". Campos,
  Gascón, Latorre and Soler, *Cryptologia* 2013. Seen only as a search abstract:
  https://iit.comillas.edu/publicacion/revista/en/673/Genetic%20algorithms%20and%20mathematical%20programming%20to%20crack%20the%20spanish%20strip%20cipher
  `SCHOLARLY` (abstract only).
- **"LUCI" (1937)**, a Francoist numerical homophonic substitution with syllabic and lexical units, broken by
  the Republican cipher bureau. Seen only as a dataset record:
  https://observatorio-cientifico.ua.es/documentos/696fbb07765d35494aa2c675 `SCHOLARLY` (record only).
- **Transposition: nothing found.** A Spanish-language search for Nationalist "doble transposición" and
  "transposición" in 1936–37 returned nothing relevant.

### Spanish Republicans (for contrast)
- The strip cipher (as above), and codes. Niebel found Civil War telegrams in the strip cipher whose keys had
  been lost, and Paar's team in Bochum decrypted them. Source: Lasry, PhD thesis, Kassel 2018, ch. 6, p. 84,
  https://www.uni-kassel.de/upress/online/OpenAccess/978-3-7376-0458-1.OpenAccess.pdf `SCHOLARLY`. **No
  Republican transposition system was found.**

### German side
- **Doppelwürfel (double columnar transposition).** Lasry's thesis (§9.1, p. 174) says the German army used it
  in WWI with K1 = K2 ("Übchi", solved by the French). During WWII it was used by several countries, including
  "German Abwehr operatives in Latin America". `SCHOLARLY`. Ostwald and Weierud call it
  "Doppelwürfelverfahren (DWV)" in official German documents, list the Wehrmacht-Handschlüsselverfahren (WHSV)
  as "another double transposition cipher", and say Weierud is preparing a history of Wehrmacht manual ciphers
  for **1936–1945**. Source: "Modern cryptanalysis of the Truppenschlüssel", *Cryptologia* 47(3), 2022, p. 1 and
  n. 1, https://cryptocellar.org/pubs/mcts.pdf `SCHOLARLY`. That companion paper was not found online. It is the
  source that would settle what the German army had in hand in 1936–37.
- Wikipedia (citing Hüttenhain) lists the Heftschlüssel as "replaced by the double transposition" in **1940**. It
  also lists the Doppelwürfel 4-S-40 and says "used until 1926 or 1927", which looks garbled. The Kammwürfel
  (comb transposition) is undated. Source:
  https://en.wikipedia.org/wiki/German_Army_cryptographic_systems_of_World_War_II `SECONDARY`.
- **Doppelkastenschlüssel** (double Playfair, a substitution, not a transposition). Its key instructions are
  dated 2 Dec 1940 and Dec 1941 (https://cryptocellar.org/wmc/index.html, `PRIMARY` documents listed).
  **Rasterschlüssel 44** (grille transposition) dates from 1944. Neither existed in January 1937.
- **Condor Legion:** Enigma machines prepared for it between 2 Oct 1936 and 2 Mar 1937 (Weierud et al. 2010,
  as above). No hand system for the Legion was found.
- **Hisma/Rowak:** no source on their cipher practice was found. A 1944 CIA file has a Bernhardt cable to
  "HISROWAK" Berlin, en clair in the copy (search result only,
  https://cia.gov/readingroom/docs/BERNHARDT%2C%20JOHANNES_0001.pdf, not opened).
- **Parameters:** no source found gives a 1930s key length, null or padding rule for any German hand
  transposition. Wikipedia de "Doppelwürfel" advises only that the two keys should differ in length and ideally
  be coprime, with no number (https://de.wikipedia.org/wiki/Doppelw%C3%BCrfel, `SECONDARY`).

### Bourdeau's "15 to 25 letter key phrases": no source, probably a conflation
Bourdeau's NOTES.md says "German-trained users of the Doppelwürfel were told to take two key phrases of 15 to
25 letters each". He cites no source, and none was found. The nearest documented numbers are modern:
- **Otto Leiberich's 1999 recommendations for the double transposition challenge:** "Both transposition keys
  should be long enough: 20 to 25 elements", coprime lengths, about 500 letters. Schmeh's 2007 challenge used
  key phrases longer than 20 (Lasry thesis §9.3, pp. 175–176, `SCHOLARLY`). These come from a Cold War
  cryptanalyst designing a puzzle, not from a 1930s German instruction.
- Lasry's own result headline is "Double Transposition cipher using keys longer than 15 elements" (thesis ch. 1).

The "15 to 25" figure looks like these two numbers merged and projected back onto 1937. **Verdict: Bean is right
that the claim is unsupported** (Bean's comment, https://github.com/dbourdeau/cyphersolver/issues/37,
15 Oct 2026, `POPULAR`; Bourdeau agreed in the same thread). It is weaker than a hallucination only in that
real numbers lie behind it. The claim must not set the search's prior on key length.

### Bean's second point: repeated strings between T1 and T2
Bean argues there are "far too many overlaps (repeated strings) between the two telegrams for this to be likely
double transposition". We ran a **scratch check (not checked in; it needs an `analysis/` script under rule 6)**:
shared n-grams between T1 and T2 against 2,000 independent shuffles of each.

| n | shared | shuffled mean | 99th pct | max |
|---|---|---|---|---|
| 4 | 9 | 2.2 | 7 | 9 |
| 5 | 2 | 0.2 | 2 | 4 |
| 6 | 1 (`APMOEP`) | 0.0 | 1 | 2 |

T2 opens `NOCU` + `APMOEP` (positions 0 and 5). T1 has `NOCU` at 17 and `APMOEP` at 263. The excess at n = 4 is
real at about the 1-in-1000 level and supports Bean's observation. What it implies (for example, a single
columnar or another system with the same key, where shared plaintext openings stay contiguous) is a hypothesis
for hypotheses.md, not a conclusion here.

### Swiss firms and commercial practice
- **Nothing found** on Swiss commercial transposition practice in the 1930s. Commercial telegraphy ran on code
  books (CDE), not ciphers (see §2). Werner said he and his brother did not correspond in cipher, so this key
  was probably Viktor's arrangement with his Spanish correspondent, not a Patvag house system.

### Italian military (CTV)
- **Nothing found for 1936–37.** A search summary says Italian army instructions in WWI used double transposition
  with a 9-letter key changed daily (musei.difesa.it, *The Secret War on the Italian Front*). The page we fetched
  (p. 126) does not contain that claim, so it is listed under Unverified.

### Route, Nihilist, disrupted columnar, grilles, nulls
- Lasry (thesis ch. 5, opening paragraph) lists route, rail fence and grille transpositions historically, and says columnar
  was "the most popular", with the IRA using it as its main cipher in the 1920s. `SCHOLARLY`. **Nothing ties a
  disrupted columnar, Nihilist transposition, grille or null convention to Spain in 1937.**

## 2. Telegram-writing conventions (1930s, international and Spanish)

From the **Madrid Telegraph Regulations, 1932** (in force from 1 Jan 1934), League of Nations Treaty Series
vol. 151, https://treaties.un.org/doc/Publication/UNTS/LON/Volume%20151/v151.pdf `PRIMARY`, read by us:
- **Art. 10, code language (CDE):** artificial or real words "must not contain more than five letters; they may
  be formed in any way. They must not contain the accented letter é." The accepting officer writes "CDE" on the
  form. CDE is charged at 7/10 of the full rate (European system) or 6/10 (extra-European).
- **Art. 11, cipher language:** "combinations of letters, with the exception of the letter é, not fulfilling the
  conditions of plain language or code language", or figures. Letters and figures may not be mixed in one group.
- **Art. 12, permitted characters:** A–Z plus IJ, and the figures. **There is no Ñ and no accented vowel except
  é** (which is barred in code and cipher). So **Ñ must have been written N** (or by some digraph convention), and
  accents were dropped.
- **Art. 19 §3:** cipher passages are counted at five characters to the word.
- **What this means for the solver:** a five-letter transposition group is formally indistinguishable from a CDE
  "artificial word" of five letters. That explains why the text is in five-letter groups, and why T2 could be
  stamped Cde. **Padding the last group to five letters is therefore likely.** Both lengths (615, 160) are exact
  multiples of 5 by construction, so up to 4 trailing (or embedded) filler letters per telegram are plausible.
  No source states which filler letters were customary.

From a **1937 Spanish telegram, Valencia to Buenos Aires, 5 June 1937** (Republican, plain language,
transcribed with original spelling): **STOP** is the separator ("RUEGOLE MAXIMA DIFUSION ADJUNTO TELEGRAMA STOP
ANTE…", "…GARCIA GRABADOR STOP SALUDOS DOMENCHINA"). Ñ is written N ("ESPANA", "MANANA", "PINUELA"), accents
are dropped, and enclitic verb forms are used ("RUEGOLE"). Source: M. T. Pochat, "Un telegrama de hombres de
ciencia…", *Olivar* 9(11), 2008, pp. 145–149,
https://olivar.fahce.unlp.edu.ar/article/download/OLIv09n11d01/pdf/4691 `SCHOLARLY` (with a `PRIMARY`
transcription). This is a single example from the other side and in plain language, but it is direct evidence
that a Spanish 1937 international telegram used **STOP**, not PUNTO.

**Not found:** a 1930s source for spelled-out numbers in Spanish cipher telegrams, for X as a word separator in
Spanish or Swiss practice, or for a standard Spanish commercial abbreviation list. The letter budget gives a hint
rather than a source: T1 has 6 X with no W. X is either a separator or filler (German military practice used X
for a full stop, but that is training-data memory and unverified, see below), or it is in
EXPORTACION/TEXTIL/EXTRANJERA. T2 has no X at all, which argues against X as a mandatory separator in this
correspondence.

## 3. Probable words (cribs)

Each entry gives the reason and source, and whether the word fits the letter budgets of T1 and T2. "Rare" marks
K, W, X, Q, Y, J and Z.

| crib | why | source | fits T1? | fits T2? | rare |
|---|---|---|---|---|---|
| **LANA / LANAS** | the stated subject, a wool deal | interrogation, BAR Dok. 69 (`PRIMARY`) | yes | yes | – |
| **BURGOS** | the authorities to be consulted; the red note says Viktor was "in Burgos" | Dok. 69; BAR img 527 (`PRIMARY`) | yes | yes | – |
| **HISMA** | the firm to be kept uninformed | Dok. 69 (`PRIMARY`) | yes (H only 8) | yes (H only 1) | – |
| **SEVILLA** | Hisma's seat | Dok. 69 (`PRIMARY`) | yes (spends 1 of 3 V) | yes | – |
| **SANSEBASTIAN** | Viktor's base by April 1937 | Dok. 69 (`PRIMARY`) | yes | yes | – |
| **SALAMANCA** | the destination (may recur in the text) | the form | yes | yes | – |
| **OFICINA** (and REABRIR, ABRIR OFICINA) | the trip's purpose: reopening an office in Nationalist Spain | Dok. 69 (`PRIMARY`) | yes | yes | – |
| **COMPENSACION** | the Madrid company did "Kompensationsgeschäfte"; Hisma/Rowak ran compensation trade | Dok. 69; Iberoamericana article (search only) | yes | yes | – |
| **CREDITOS, SALDOS, DIVISAS** | Swiss "Exportguthaben … eingefroren" (frozen export balances) | Dok. 69 (`PRIMARY`) | yes | yes | – |
| **FRANCOS (SUIZOS)** | Swiss currency of the balances | inferred from Dok. 69 | yes (F only 5) | yes | Z |
| **PESETAS** | the Spanish side of any price | inferred | yes | yes | – |
| **EXPORTACION** | export balances, wool export | Dok. 69 | yes | **no** | X |
| **SUIZA, ZURICH** | the destination of the wool; the place of sending | Dok. 69 | yes | yes | Z |
| **PATVAG** | the Zurich firm (Werner a partner), founded 1933 for the Spanish business | Dok. 69, image 501 (`PRIMARY`) | yes (V) | yes | – |
| **HOVAG** | Werner's 1936 firm (Holzverzuckerungs-AG) | HLS, https://hls-dhs-dss.ch/de/articles/030150/2019-10-16/ (`SECONDARY`) | yes (V) | yes | – |
| **VICTOR** (Spanish spelling) | sender and signatory per Werner | Dok. 69 | yes (V) | yes | – |
| **VIKTOR** | same, German spelling | Dok. 69; red note "Oswald Viktor" | yes (uses both K) | **no** | K |
| **OSWALD** | the surname | Dok. 69 | **no: W = 0** | **no** | W |
| **STOP** | 1937 Spanish telegraph separator | Pochat 2008 (above) | yes | yes | – |
| **MONEDA EXTRANJERA** | the Comité de Moneda Extranjera (Burgos, Decree 81, Nov 1936) controlled foreign exchange | BOE 1936-39 (search snippet only, see Unverified) | yes | **no** | J X |
| **JUNTA TECNICA** | the Burgos government in Jan 1937 | as above (search only) | yes | yes | J |
| **KILOS** | wool is sold by weight | trade inference; Bourdeau suggests it from the letter counts (`CLAIMANT`) | yes (both K) | **no** | K |

**Hard constraints:**
- **OSWALD, WERNER and ROWAK cannot occur.** Telegram 1 has no W, so the text does not spell the surname
  (unless W was rendered as V or UU, a convention for which no source was found).
- **The three V's in T1** must cover everything among VICTOR, SEVILLA, PATVAG, HOVAG, DIVISAS, VAGON and the
  like. At most three of these can appear.
- **Q = 2 and Y = 2 in T1** mean QUE and Y ("and") almost never occur. That fits telegraphic style, which drops
  them (Bourdeau, `CLAIMANT`).
- **T2 has no K, X, Q, Y or W:** KILOS, VIKTOR, EXPORTACION and EXTRANJERA cannot be in T2.
- The two K's in T1 can be **KILOS, VIKTOR, HUNZIKER** (the Hunziker business dates from April 1937, after the
  telegrams, so it is unlikely), or a name.

### Guesses (not for solver use)
Items with a plausible reason but no source tying them to this correspondence. They should not become cribs
without new evidence.
- BLUME as a word inside the text. TONELADAS, PRECIO, MIL, CIEN, spelled-out figures (no 1930s Spanish source
  found for spelled-out numbers in cipher telegrams).
- BERNHARDT (Hisma's head), ALEMANIA, CLEARING, TEXTIL, MERINO, LAVADA/SUCIA (washed/greasy wool).
- Names of Spanish wool firms or of "Wolleinkäufer" (wool buyers). None are known.
- GENERALISIMO, CUARTEL GENERAL (Franco's HQ was in Salamanca). Not linked to the Oswalds.
- PUNTO as a separator (the one 1937 Spanish example uses STOP).

## 4. Who "Blume" may be
- **Nothing found.** Fuentes's project searched the BOE Gazeta for 1936–38: "BLUME returned no documents" (OCR
  sensitivity not measured). The 1936 Anuario General de España volumes exist at the BNE (ZR/332) but have not
  been read for Salamanca. Source:
  https://github.com/jfuentesibanez/sentinel-blume-salamanca/blob/main/docs/SOURCES.md `CLAIMANT`. One search by
  us ("Blume" Salamanca 1937 with Hisma/Rowak/Cuartel General) found nothing.
- The form gives an address of two words, BLUME SALAMANCA, with no street. That is the shape of a **registered
  telegraphic address** (a short code name registered with the destination office) or a well-known recipient. This
  is an inference from the form (`PRIMARY` for the form, the inference ours).
- Werner thought the telegrams were consultations with Viktor's **Spanish wool buyers**, which points to a Spanish
  firm or agent. Recipients in Salamanca in January 1937 were largely Franco's HQ and the services around it.
- "Blume" is German for "flower". It could be a German surname, a cover word (Flor?), or a registered code word.
  None of these is supported by a source.
- **What would breach this wall:** the 1936–37 Spanish list of registered telegraphic addresses for Salamanca, the
  Anuario General de España 1936 Salamanca pages, or the receiving copies at Salamanca's telegraph office.

## 5. Language
- **The address is Spanish** (SALAMANCA) and the destination is Nationalist Spain.
- **The correspondents:** Viktor ran a **Madrid** trading company from 1932 to 1936, and Werner thought the
  telegrams were addressed to **Spanish wool buyers** (Dok. 69, `PRIMARY`). That points to Spanish.
- **Against German:** W = 0 in 775 letters. German prose has W at about 1.9%, so about 15 would be expected.
  Bourdeau's chi-squared also puts German last of seven corpora (NOTES.md, `CLAIMANT`). The routing first chosen
  (Vigo–Emden, a German cable) shows German links, not German text.
- **Against Italian:** no evidence of Italian correspondents.
- **Portuguese:** not tested by Bourdeau (his corpora: Spanish, Latin, French, Italian, English, German, plus
  Portuguese only in the key-phrase lists). Portuguese has ç and ã, which were dropped. It shares Spanish's O
  frequency, and NH or LH would show up as excess H and L, but H is low (8). There is no context pointing to
  Portugal except that Lisbon was a supply route.
- **Hisma's working language:** no source found. It was a German–Spanish company based in Seville, so it was
  probably bilingual. In any case, Hisma was the party being kept out of this exchange.
- **Verdict:** the context points to Spanish (with Ñ written N and accents dropped). There is no direct evidence
  such as a plaintext copy or a reply.

## Unverified claims
- German military practice of writing X for a full stop: training-data memory, not checked here.
- The Comité de Moneda Extranjera (Decree 81, Nov 1936) and the "Comisión de Industria y Comercio" of the Junta
  Técnica: from search snippets of BOE 1936-39 (https://boe.es/gazeta/dias/1936/11/24/pdfs/BOE-1936-39.pdf),
  not opened.
- WWI Italian double transposition with a 9-letter key changed daily: from a search summary of musei.difesa.it.
  Not found on the page fetched (p. 126).
- Hisma/Rowak's "systematic compensation system" covering most private trade: from a search summary of
  https://journals.iai.spk-berlin.de/index.php/iberoamericana/article/viewFile/876/559, not opened. Germany
  "obtaining wheat, wool, hides … in large quantities from the Iberian Peninsula" is verified in FRUS 1937 vol. I,
  doc. 359 (Consul Sholes, Milan, 9 Nov 1937), https://history.state.gov/historicaldocuments/frus1937v01/d359
  `PRIMARY`.
- Fees: T1 49.90 fr for 125 words (0.399 fr per word); T2 14.00 fr for 34 words (0.412 fr per word). The two
  rates are nearly equal, although T2 is stamped Cde and T1 is marked "chiffriert". If CDE meant 7/10 of the
  full rate, the rates would differ by 30%. The tariff for Zurich to Salamanca via England has not been checked,
  so no conclusion is drawn.
- Bochsler's *Nylon und Napalm* (2022), note 44: a failed 2020 decipherment attempt by Heinzmann, Matteotti,
  Liniger and Viveksanth (per Bourdeau). The report was not found.
