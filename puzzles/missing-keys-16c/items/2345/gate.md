# Gate: catalogue no. 2345 (Baldovino del Monte to Cosimo I, Rome, 14 March 1555)

Scout: Opus stage 0, 2026-11-16. The main thread decides. The verdict is at the end.

**Proposed verdict: `go`, but only once the images come in.** Today checks 2, 3 and 4 could not be run,
because the ASF image server could not be reached at all from this environment (see 3). Check 1 (race)
passes. Check 5 turned up something the catalogue does not say: DECODE catalogues the ASF chancery key
volume for Cosimo I, with records dated 1554 and 1555. If `fetch.py` fails again on a second try, the
proposal becomes `skip: images unreachable` until ASF PAD is back.

Entry under test: `sources/cache/bourdeau-catalogue-2026-11-16b.json`, `id == 2345` (cls A, importance 3,
solvability 5, difficulty 2, vetted 2026-11-06 by "claude leads review batch n13").

## 1. Race: PASSES (still open, unreserved, unwritten)

- **Site page.** https://cyphersolver.com/solve/2345.html was fetched 2026-11-16. Its header reads
  "Unsolved Catalogue · no. 2345 · class A · priority 7.4 · open". It does not say "in progress". The repo
  copy, https://raw.githubusercontent.com/dbourdeau/cyphersolver/HEAD/docs/solve/2345.html, is identical
  (24,767 bytes both).
- **GitHub (API, via urllib).** I grepped titles and bodies for `baldovin|del ?monte|\b2345\b|mediceo
  (del principato )?436|443`:
  - all 30 open PRs: no hit;
  - the 100 most recently updated closed PRs (back to 2026-11-14T14:59Z): no hit;
  - the 100 most recently updated issues of either state (back to 2026-11-15T11:43Z): no hit.

  Search API, `repo:dbourdeau/cyphersolver`:
  - `Baldovino`: 0 results;
  - `2345`: one hit, #293 (deboli1787, catalogue 416), unrelated, matching on the number only;
  - `"del Monte"`: one hit, #405 (row 1564, Muzio to Ferrante Gonzaga, 1550), unrelated.

  The 100 most recent commits (2026-11-16T19:00Z to 2026-11-17T03:36Z by the repo's clock) mention none of
  the patterns.
- **Tomokiyo** (https://cryptiana.web.fc2.com/code/). I grepped `unsolved.htm`, `italian.htm` and
  `vatican.htm` for Baldovino, del Monte, Julius III / Giulio III. No hit. In `unsolved.htm`, "Medici"
  hits only Catherine de Médicis and Marie de Médicis.
- **DECODE** (https://de-crypt.org/decrypt-web/RecordsList?cmd=search&search=<q>):
  - `Baldovino`: no records;
  - `Mediceo del Principato`: no records;
  - `Giulio III`: no records;
  - `Monte`: 11 records, none relevant. The nearest is the Santa Croce France nunciature, 1552-54
    (records 6-10), which the vetting already set aside.

  On key records, see 5.
- **Edition or study.** Two web searches: `"Baldovino del Monte" cifra Cosimo 1555 lettere decifrazione`,
  and `"Baldovino" "del Monte" 1555 Cosimo Medici lettere Giulio III conclave Marcello II carteggio
  edizione`. Neither found an edition or study that prints these letters or their key. The hits were
  inventories of other volumes, the Bellaso 1555 challenges, and the CSUN Sede Vacante 1555 pages.

  The vetting reports that Desjardins III prints only a Baldovino letter of 30 June 1554. I did not check
  that again.

## 2. The pair is real: NOT VERIFIED (no images)

I could not view any page, so I cannot say anything about layout, length, clear words, dockets or the
join between the decipherment and the clear text. What other sources say, all unverified by me:

- **(a) 436 cc. 849-850 → c. 851.** The catalogue cites the inventory (vol. VII, note 117) as recording a
  decipherment at c. 851 for Baldovino's 21 Dec 1554 letter. A note in an inventory saying "decipherment"
  points to the same text, not only the same system, but I have not seen it. The inventory PDF (vol. VII,
  Morviducci 2004, filze 431-446) is not on regione.toscana.it, which holds vols. III, XI, XII and XVI.
  The ASF "Inventari on-line" copy is on the same unreachable host.
- **(b) 443 c. 78 → c. 79.** Only the catalogue's inference supports this pair. c. 79 is "a clear unsigned
  'Informazione sull'atteggiamento del Papa'" ("Information on the attitude of the Pope"), filed between
  Baldovino's cipher carte 78 and 85, and the catalogue calls it "very likely" the decipherment.

  The inventory also notes that the Baldovino key in Cifrari II serie F. III "does not correspond" to
  443 c. 78. Whichever way that is read, 443 c. 78 may not be in the same system as 436 c. 849 and 443
  c. 679. The vetting compared hand and figure style only between 436 c. 849r and 443 c. 679r; it does not
  say whether c. 78 matches them.
- **Form (A1 or A2).** By the catalogue's description, both look like **A1** (decipherment on a separate
  carta). The vetting says nothing is written "over or beside the figures" on 443 c. 679. Unverified for
  436 c. 849-850 and 443 c. 78.

## 3. Images: NOT REACHED today. Recipe written, not tested

- From this sandbox, every TCP connection to `archiviodistatofirenze.cultura.gov.it:443` (2.42.229.114)
  timed out, on about 10 attempts over roughly 30 minutes on 2026-11-16. `cultura.gov.it` and
  `www.archivi.beniculturali.it` timed out as well. WebFetch, from a different network, got `connect
  ECONNREFUSED 2.42.229.114:443`. Other hosts were fine (GitHub, cyphersolver.com, de-crypt.org,
  fc2.com), so this is the ASF/MiC side: an outage or a block. A blanket local block is ruled out. I did
  not try to get around it.
- `fetch.py` (in this folder) encodes the recipe from the catalogue's `access_note`:
  1. Fetch riproduzione page `/archividigitali/riproduzione/?id=<rid>&ua=<filza>` and read the `.ptif`
     path it names.
  2. Check the carta against the ptif name `<seq>_C_<carta>_<R|V>.ptif`.
  3. Read `iipsrv.fcgi?IIIF=<ptif>/info.json` for the native size.
  4. Fetch `full/max/0/default.jpg`, falling back to `full/<w>,/0/default.jpg`.
  5. Fetch one region crop, `0,0,1200,400/full/0/default.jpg` of 443 c. 679r, to show that region
     requests work.

  The rids for 436 cc. 849r-851v, 443 cc. 78r-v and 678r-679v come from the catalogue links. Those for
  443 cc. 79r-v (601432-3) and 85r-v (601444-5) are guesses from the sequence; the script checks each guess
  against the ptif and tries neighbouring ids if it is wrong.

  The script stops at once with "ASF PAD unreachable" if the unit page does not answer. `--probe` resolves
  ptifs and prints native sizes without downloading.
- **Unverified.** I could not confirm whether more than 2000 px is served, whether region crops work, or
  whether a cipher line is legible. The vetting worked at 1400 px and 2000 px and read figure groups such
  as 02, 39, 56 at 2000 px, so legibility at 2000 px is likely. That is the vetting's statement, not mine.
- `PROVENANCE.md` records that nothing was fetched.

## 4. Size: NOT MEASURED. The catalogue's figures only

| file | carta | what it is | cipher/clear/mixed | lines | rough signs |
|---|---|---|---|---|---|
| 443_c678r.jpg | 443 c. 678r | Baldovino 14 Mar 1555, first part | clear (per vetting) | ? | 0 |
| 443_c678v.jpg | 443 c. 678v | same letter | clear (per vetting) | ? | 0 |
| 443_c679r.jpg | 443 c. 679r | same letter, end and postscript | **mixed**: 6 cipher lines, clear close, 10-line cipher P.S. (per vetting) | 6 + 10 cipher | ~330 + ~550 digits (per vetting) |
| 443_c679v.jpg | 443 c. 679v | ? | ? | ? | ? |
| 436_c849r.jpg | 436 c. 849r | Baldovino 21 Dec 1554 | cipher, or mixed? | ? | ? |
| 436_c849v/850r/850v.jpg | 436 cc. 849v-850v | same letter | ? | ? | ? |
| 436_c851r.jpg / 851v | 436 c. 851 | decipherment (per inventory note 117) | clear | ? | ? |
| 443_c78r.jpg / 78v | 443 c. 78 | Baldovino 6 Jan 1555 | "full page" cipher (per catalogue) | ? | ? |
| 443_c79r.jpg / 79v | 443 c. 79 | "Informazione sull'atteggiamento del Papa" | clear | ? | ? |
| 443_c85r.jpg / 85v | 443 c. 85 | another Baldovino cipher carta (per catalogue) | ? | ? | ? |

- **Bare letter:** about 880 digits, per the vetting. Its note "frequent 02, 39, 56, 59, 64" implies groups
  of two digits, so roughly 440 signs if the groups are pairs. That is my inference from the vetting's
  wording, not something I measured. The vetting calls it a "continuous figure cipher", so the figures
  probably run on without separators, but this is unverified.
- **Pairs:** unknown. A "full page" (443 c. 78) at the bare letter's density of about 55 digits per line
  would easily clear 150 pair signs. Pair (a) spans two carte, 849-850. The 150-sign bar is probably met,
  but not shown.

## 5. A period key: the catalogue says "not online"; DECODE lists the volume (images behind login)

- The catalogue, quoting inventory vol. VII, says ASF "Cifrari II serie F. III" holds a key attributed to
  Baldovino that "does not correspond" to 443 c. 78, and that it is not online. I could not check the
  inventory wording (host down).
- **New, and contradicting the entry's `prior_art`.** The entry says DECODE's ASFi records are 17th-18th
  century. They are not all: DECODE has a series `ASFi_SIVol3_*` of **Key** records whose Additional
  Information reads "Chiavi delle cifre del carteggio di Cosimo I dal 1536 al 1573 – volume di 250 cc non
  numerate" ("Keys of the ciphers of Cosimo I's correspondence, 1536 to 1573: a volume of 250 unnumbered
  carte"). The records run at least to `ASFi_SIVol3_130` (1573). Those dated near the item:

  | DECODE record | signature | date |
  |---|---|---|
  | 6087 | SIVol3_92 | 1554 |
  | 6088 | SIVol3_93 | 1554 |
  | 6089 | SIVol3_94 | 1554 |
  | 6090 | SIVol3_95 | 1554-1555 |
  | 6091 | SIVol3_96 | 1554 |
  | 6093 | SIVol3_98 | 1554 |
  | 6094 | SIVol3_99 | 1555-1556 |
  | 6095 | SIVol3_100 | 1555, 2 pp. |
  | 6096 | SIVol3_101 | 1555 |
  | 6097 | SIVol3_102 | 1555 |

  The URL for each is `https://de-crypt.org/decrypt-web/RecordsView/<n>?showdetail=`. Sender and Receiver
  are blank on every one checked (6088, 6090, 6094-6097). "Access Mode: Authentication required", so the
  images are not public. I did not log in and did not look at any key.
- **Unverified:** whether DECODE's "SI Vol3" is the inventory's "Cifrari II serie F. III", and whether any of
  these records is Baldovino's key. SIVol14 records also carry a "Chiavi delle cifre" label, so the mapping
  from DECODE volume to ASF filza is not obvious.
- **Consequence for the pipeline.** The key is not public, so this is not a "key lookup, skip" case. But a
  period key that someone with a DECODE account can open probably exists. At stage 7 it is the outside
  check, and Greg might prefer to ask for access rather than build the key. That is the main thread's call.

## Looking only: notes I could not make

I could not make any notes on clear words inside the cipher, marks above or below figures, or other
Baldovino carte in the filze 436/443 unit indexes, because those indexes are on the unreachable host.

## Proposed verdict

`go`, if `python3 -I fetch.py` succeeds and a quick look confirms three things:
1. 436 c. 851 is a decipherment of the text on cc. 849-850 (the opening joins the clear text).
2. The pair holds at least about 150 signs.
3. 436 c. 849 and 443 c. 679 use the same figure style.

Pair (b) (443 cc. 78-79) should count as unconfirmed, and possibly a different key, until c. 79 has been
compared with c. 78 by length and by a docket. Otherwise: `skip: images unreachable (ASF PAD down
2026-11-16)`, to be reopened when it is back.
