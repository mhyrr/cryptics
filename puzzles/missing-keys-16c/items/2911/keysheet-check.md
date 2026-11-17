# Key-sheet check: is a period key for the V/134 cipher online?

Bounded check for `gate.md` check 5 (`PIPELINE.md` stage 0 check 5, stage 7), 2026-11-16. One agent, no
sub-agents. **This file holds no sign-to-value pair and no deciphered text.** The key sheets themselves do:
`cache/keysheets/` is key material, and the main thread and the transcription readers should not open it.

**Overall: yes. A period key for the cipher of V/134 is online: BNCF Carte Machiavelli VI/82, units 1° to 4°,
which are four sheets of one and the same cipher. Unit 5 is a different system.** The identification is direct
for V/139 (a period gloss agrees with the key) and by inventory for V/134, V/125, V/135, V/136 and V/140. No
sign of V/134 or V/125 was read with the key. See "How sure" and "Not verified".

## Sources

| what | URL | tier |
|---|---|---|
| VI/82 images, 19 pages, 300 dpi | `https://teca.bncf.firenze.sbn.it/ImageViewer/servlet/ImageViewer?idr=BNCF0003858589` … `8607` `&azione=showImg&usage=2`; one line per file in `PROVENANCE.md` | PRIMARY |
| BNCF description of VI/82 (five "Cifrario" records, names cited, life dates, old index) | `https://teca.bncf.firenze.sbn.it/OAI/servlet/OAIHandler?verb=GetRecord&metadataPrefix=mag&identifier=oai:bncf.firenze.sbn.it:21:FI0098:AutografiPalatini:Machiavelli_VI_82` (cached `cache/mag/VI_82.mag.xml`) | SECONDARY (library catalogue, "descrizione di prima mano", first-hand description, dated 18/06/2009) |
| Cipher pages V/134, V/139, V/140, V/136 c. 7 | as in `PROVENANCE.md` | PRIMARY |

Fetch: `python3 -I fetch.py --keysheets` (new flag; urllib, generic User-Agent). All 19 pages came back at
the first try; no host refused.

**Carta numbers.** File names use the MAG's carte, which count a modern ruled bifolium wrapped round the
unit as cc. 1 and 9. The BNCF description counts without it, so its "c. 1v" (the endorsement) is the MAG's
2v, its "c. 2r" is the MAG's 3r, and so on. Below, "MAG c." is the file name's carta.

## What is in VI/82

| MAG c. (file) | pencil no. on the leaf | what it is |
|---|---|---|
| Copertina | - | modern cover |
| 1r (`_02_1r`) | "82" | **modern** ruled sheet (19th-century hand): a partial working key, entries written as pairs with "=". Every pair compared (about ten) agrees with unit 1. 1v blank. |
| 2r (`_04_2r`) | "82.1°" | **unit 1, writing side** |
| 2v (`_05_2v`) | - | unit 1, endorsement on a pasted slip |
| 3r (`_06_3r`) | "4" | unit 1, list of names |
| 3v (`_07_3v`) | - | unit 1, reading side, headed "Da deciferare" (for deciphering) |
| 4r (`_08_4r`) | "82.2°", "5" | **unit 2**; 4v blank |
| 5r (`_10_5r`) | "82.3°", "1", "N. XLII" | **unit 3**; 5v, 6r blank; 6v one word, not read |
| 7r (`_14_7r`) | "82.4°", "3" | **unit 4**; 7v blank |
| 8r (`_16_8r`) | "6" | **unit 5**; 8v endorsement on a pasted slip |
| 9r, 9v | - | the modern wrapper, blank |

## The V/134 cipher, by shape (from V/134 c. 1r and V/140 c. 1r, looked at before any key sheet)

Lower-case letter forms used as signs; the figures 2, 3, 4, 8, 9; letters and figures carrying a small
superscript o; letters carrying a dot; doubled and tripled letters written as one sign; a few capitals;
invented marks (a square with a dot in it, a circle with a dot, a circle with a bar, a circle on a stem,
a dotted cross, a C with a dot, an omega-like sign, crossed and tailed forms). No word spaces. One
five-sign run recurs twice on V/134 c. 1r (end of line 2, line 7) and at least three times on V/140 c. 1r
(lines 1, 4, 6): the two letters share sign groups as well as signs.

## Per unit

### Unit 1 (82.1°), MAG cc. 2r-3v — verdict: `same cipher`

**Endorsement and date evidence.**
- Head of c. 2r: "p(er) Roma et Francia", "da scrivere" (for Rome and France; for writing). Top right, an
  archival note "Busta 6ª 3[6]" (envelope 6, 3[6]; last figure altered).
- Slip on c. 2v: "Cyfra co(n) li Or(ator)i di Francia / it(em) p(er) Roma cum m(esser) F. Pepi / con
  m(esser) Franc(esc)o Gualterotti et / [one line struck through, not read] / Luigi della Stufa or(ator)i /
  al Re (Christianissi)mo" (cipher with the orators of France; also for Rome with Messer F. Pepi; with
  Messer Francesco Gualterotti and Luigi della Stufa, orators to the Most Christian King).
- c. 3v head: "Da deciferare" (for deciphering).
- c. 3r, list of about 55 names and terms, among them "Ascanio", "Adorni", "Car(dina)le S. P. ad vincula"
  (the Cardinal of San Pietro in Vincoli), "C. di Roano" (Cardinal of Rouen), "Duca di Valentinese" (Duke of
  Valentinois), "Re Federigo" (King Federico), "Mons(igno)r di Ligni", "Mons(igno)r di Ubigni",
  "Mess(er) G. Jacopo", "Piero de Medici", "S(igno)re di Faenza", "S(igno)re di Piombino", "Papa",
  "Pisani", "Viniziani" (Venetians). "Ciamonte" (Chaumont) is squeezed in between two lines, with its
  number altered: a later addition.
- BNCF life dates for persons named: Ascanio Sforza d. 1505, Piero de' Medici d. 1503, Federico of Naples
  d. 1504, Francesco Gualterotti d. 1509. So the sheet and its endorsement are earlier than 1510; the
  names point to about 1500-1503 (my dating, see Unverified claims). The cipher was not retired then:
  see units 3 and 4.

**Design.** A homophonic alphabet (22 plain letters, one to four signs each, the signs being letters,
figures and a few marks, some dotted); a row of about ten nulls headed "Nulle"; a table of syllables,
one row per consonant (b, c, d, f, g, l, m, n, p, qu, r, s, t, u), five vowels across, with a few longer
syllables added at the end of some rows, about 75 signs, which is where the doubled letters, the
superscript-o signs and most invented marks live; a row "Duple" (doubles) of twelve signs for doubled
consonants; a list "Dictioni" (words) of about 28 common words, one sign each; and on c. 3r a list of
names and terms, each given a two-digit number. c. 3v gives the same table turned round for the reader,
sorted by the shape of the sign.

**Evidence against V/134.** All of the distinctive signs checked are on this sheet (table below), and so is
the whole class structure the letters show: plain letters and figures, doubled letters, superscript-o
forms, a handful of marks. I met no sign on V/134 c. 1r or V/140 c. 1r that I could not find on the sheet,
but this was a look at some twenty sign types, not a census (a census needs the transcription and a
script). Value-level confirmation: on V/139 c. 1r (the Dieci to Machiavelli, 7 Aug 1510, the covering
letter of V/140) line 3 carries a period gloss in pale ink. Two runs of three consecutive signs there
agree with unit 1 against the gloss words written above them or keyed to them from the margin (six signs
of six; nothing recorded). I did not work through the rest of that line.

### Unit 2 (82.2°), MAG c. 4r — verdict: `same cipher`

**Endorsement and date evidence.** None: no heading, no endorsement, no names. Old pencil number "5".

**Design.** A reading-side table only: one row per sign shape (a, b, c, d, e, f, g, h, i, l, m, n, o, p,
q, r, s, t, u, x, y, z), each sign with its meaning written above; then three boxed panels, "Caratteri"
(characters: the invented marks), "numeri" (numbers: the figure signs) and one more of word signs; and a
row "nulle". It is the same arrangement as unit 1 c. 3v, in a quicker hand, with a struck-out line.

**Evidence.** About ten cells compared with unit 1 (the square with a dot, the dotted cross, three doubled
letters, three superscript-o signs, two marks): each carries the same meaning as on unit 1. The null row
shows the same shapes in the same order as unit 1's. It is the same cipher laid out for deciphering.

### Unit 3 (82.3°, "N. XLII"), MAG c. 5r — verdict: `same cipher`

**Endorsement and date evidence.** "N. XLII" (no. 42) in large letters at top right, presumably a chancery
or archive number of the cipher (not verified). c. 6v has one word in a looped flourish, not read. Names
on c. 5r: "Re di Francia", "Papa", "Re di Spagna", "Viniziani", "Imperatore", "Fiorentini", "Sanesi",
"Lucchesi", "Genovesi", "Ciamonte" (Chaumont), "Pandolpho", "Duca d'Urbino", "La Trimolle" (La
Trémoille), "Consalvo" (Gonzalo de Córdoba), "Pavia" (reading uncertain), then four entries half lost to
a tear, ending "… d'Inghilterra", "… di Savoia", "… di Angolem" (of Angoulême; reading uncertain). BNCF
dates: Chaumont d. 1511. The list has dropped unit 1's dead (Ascanio, Re Federigo, Piero de' Medici,
Valentino) and has Chaumont and La Trémoille in the body of the list: later than unit 1, and before 1511
if lists were kept current.

**Design.** As unit 1's writing side: alphabet with homophones, syllable table, "Nulle", "Duple",
"Dictioni" (one row), names with two-digit numbers. Lower half of the leaf torn away at the centre.

**Evidence.** Alphabet row and the first six syllable rows compared cell by cell with unit 1: same sign in
the same cell throughout. The alphabet has fewer second and third homophones than unit 1. **The name list
is renumbered:** several names that are on both lists carry a different number here than on unit 1, while
others keep theirs. So for names the 1510 letters should follow unit 3 or 4, not unit 1.

### Unit 4 (82.4°), MAG c. 7r — verdict: `same cipher`

**Endorsement and date evidence.** No endorsement. Names: "Re di Francia", "Papa", "Viniziani", "Sanesi",
"Genovesi", "Lucchesi", "Pisani", "Roano" (Rouen), "Re di Spagna", "Fiorentini", "Ciamonte", "Imperatore",
"Orsini", "Vitelli", "Colonnesi", "Pandolpho", "Giampaulo", "Duca d'Urbino", "M(esser) Giovanni",
"Consalvo", "Pavia" (uncertain). BNCF dates: Georges d'Amboise (Rouen) d. 1510, Chaumont d. 1511.

**Design.** As unit 3, complete except for a torn top left corner (alphabet letters a to d and the left
ends of the first three syllable rows are lost). Has "Nulle", "Duple", "Dictioni".

**Evidence.** Alphabet row from e onward, six syllable rows, the null row and the doubles row compared
with unit 1: same sign in the same cell. Its name numbers agree with unit 3's where both have the name.

### Unit 5, MAG c. 8r — verdict: `different system`

**Endorsement and date evidence.** Slip on c. 8v: "Cifera di m(esser) Goro" (cipher of Messer Goro).
Names: "Piero de' Medici", "Vitellozo", "Pandolfo Petrucci", "Pisani", "Pistoia", "Cancellieri",
"Panciatichi", "Tarlatino", "Montagna di Pistoia" (the Pistoia hills), "M(esser) Giovanni Bentivogli",
"Duca Valentino", "Pescia", "Piano di Pistoia" (the Pistoia plain), "Fanti" (foot), "Cavalli leggieri"
(light horse), "Homini d'arme" (men-at-arms), "M(esser) Goro", "Pacciono". BNCF: Vitellozzo Vitelli d.
1502. A Pistoia cipher of about 1501-1502.

**Design.** An alphabet only (a to z and "&"), two or three signs per letter, all invented geometric marks
(squares, crosses, triangles, strokes with dots, small circles on stems), no letter forms, no figures, no
superscripts, no syllable table, no doubles. Names are given compound drawn marks, not numbers.

**Evidence.** None of the V/134 repertoire (letters, figures, superscript o, doubled letters) is here.

## Signs of V/134 and V/140 against unit 1 c. 2r

Shapes and places only. "Top rows" is the alphabet block, "table" the block of bracketed rows left and
right, "lists" the two blocks at the lower right.

| sign (shape) | seen on | on unit 1? | also on |
|---|---|---|---|
| A: square with a dot inside | V/134 ll. 3, 9; V/140 ll. 2, 3, 5 | yes, lists | units 2, 3, 4 |
| B: three o's in a row, one sign | V/134 l. 2 | yes, lists | unit 4 |
| C: circle with a dot inside | V/134 ll. 4, 9; V/140 ll. 2, 4 | yes, table (left) | units 3, 4 |
| D: dotted cross (a cross with dots in its angles) | V/134 ll. 4, 5, 6; V/140 ll. 1, 5 | yes, lists | units 2, 3, 4 |
| E: omega-like sign | V/134 ll. 3, 7; V/140 ll. 2, 6 | yes, table (left) | units 3, 4 |
| F: C with a dot inside | V/134 ll. 3, 5; V/140 ll. 5, 6 | yes, table (right) | units 2, 4 |
| G: circle on a descending stem | V/134 ll. 3, 5, 6, 7; V/140 l. 1 | yes, table (left) | units 2, 3, 4 |
| H: doubled letters as one sign (tt, bb, ss, aa, rr, pp) | both, every line | yes, table (six places) | units 2, 3, 4 |
| I: letter or figure with superscript o (r, p, 3, a, q, c, m, b) | both, every line | yes, table (each of the eight) | units 2, 3, 4 |
| J: y with a curved stroke above | V/134 ll. 2, 7; V/140 l. 7 | yes, table (left) | units 2, 3, 4 |
| K: capital A with a bar; capital B | V/140 ll. 3, 6 | yes, table (first row) | units 2, 3 |
| L: L with a small cross | V/140 l. 4; V/139 c. 1r ll. 6, 8 | yes, lists | units 2, 3, 4 |
| M: 7 with a cross stroke | V/134 ll. 3, 4; V/140 l. 2 | yes, table (left) | units 2, 3, 4 |

13 of 13 present. On unit 5: none. Line numbers are from reduced crops of the first eight or nine lines
of each page and may be off by one; the "also on" column lists only units where I saw the sign, so a unit
missing there is not a unit lacking it.

## How sure

- **VI/82 units 1-4 are one cipher: high.** Cell-by-cell agreement across three writing-side sheets and
  one reading-side sheet.
- **That cipher is the cipher of V/139 c. 1r (7 Aug 1510): high.** Six glossed signs of six agree; the
  inventory agrees; units 3 and 4 name Chaumont and La Trémoille, the French commanders of 1510.
- **V/134 (17 Aug 1510), V/125, V/135, V/136, V/140 are in that same cipher: high, but indirect.** Same
  office, same correspondent, ten days later; same inventory (13 of 13 above); the recurring five-sign run
  shared by V/134 and V/140; V/140 is V/139's own enclosure. Nothing on V/134 or V/125 was read with the
  key, by the rule of this check.
- A further pointer, value-free: the modern clear text of V/136 (c. 7) leaves a two-digit number
  unresolved and has two names struck out and corrected, which is what deciphering with a numbered name
  list looks like; and VI/82 is wrapped in a modern working key. Someone has probably read these letters
  with VI/82 before. I did not show that the two modern sheets are one hand or one paper.

## Not verified

- No value-level test on V/134, V/125, V/135, V/136 or V/140. The quickest one that keeps the main thread
  blind: an isolated agent reads two lines of V/140 c. 1r with unit 3 or 4 and compares with V/139 cc.
  1v-2r.
- No census of signs. A sign of the 1510 letters that is on none of the four sheets (a later addition to
  the cipher) would not have been caught.
- Which name list was in force in August 1510 (unit 3 or unit 4; they agree where they overlap, but
  neither is dated).
- The struck line of the unit 1 endorsement, the word on c. 6v, and the meaning of "N. XLII".
- Whether VI/82 has been published or transcribed (DECODE, Tomokiyo, the Edizione Nazionale): not searched
  in this run.
- The gloss check on V/139 c. 1r went to the edge of the "do not decode" rule: the plain words were already
  on the page in a period hand, and I compared six signs with them. I name it so the main thread can
  weigh it.

## Unverified claims

- The dating of unit 1's name list to about 1500-1503 and of unit 5 to 1501-1502 rests on what I recall of
  the persons named (Federico of Naples deposed 1501; the Cardinal of San Pietro in Vincoli elected pope in
  1503; the Pistoia factions of 1501-1502), beyond the life dates the BNCF record gives. Not fetched.
- That Pepi was orator at Rome and Gualterotti and della Stufa orators in France in 1501-1503. Not fetched.
- That "Ubigni" is Bérault Stuart d'Aubigny and "G. Jacopo" Gian Giacomo Trivulzio (the BNCF record gives
  the second).
