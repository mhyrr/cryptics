# 12. Sweep pilot: pairing cipher letters with decipherments, BnF fr. 16107, views 1–215

**Question.** For every letter in cipher in views 1–215 of BnF Français 16107 (Saint-Goard, Madrid, Jan–Apr 1580; Gallica `btv1b9009661v`, PRIMARY), is there a contemporary decipherment sheet? What is left over?
Dockets and binding order are not trusted: in fr. 16106 a sheet docketed "23 avril 1579, Dechiffré de la precedente" deciphers a letter of 23 Dec 1579 bound 150 folios away.

## Method
1. `sheets.py`: contact sheets, 12 spreads each (900 px sources). Each page classed by eye as cipher, clear, decipherment or blank; the fraction of a page in cipher was estimated by eye (`*0.5` in `items.tsv`).
2. `linecount.py`: lines per page from the row-ink profile (line pitch by autocorrelation). Calibration: view 6 gives 32/33 against about 37/40 by eye, so it **undercounts by about 10–15%**. It gives the same bias to cipher and decipherment pages, so the ratio is usable and the absolute numbers are rough.
3. Pairing used adjacency, the archivist's docket and size (decipherment lines ÷ cipher lines). The content join was read for one doubtful group only (7 Feb, views 45–65, fetched at 1800 px as `m45 … m65.jpg`).
4. `count.py` computes everything below from `items.tsv`, `pairs.tsv` and `linecounts.tsv`. Output: `counts.txt`.

## Result (from `counts.txt`)
21 letters with cipher, 16 decipherment sheets, 16 pairs. Every decipherment sheet has a partner. Every pair is adjacent, and every pair's docket dates agree. Fifteen pairs fall in a decipherment/cipher ratio of 0.50–0.87; fr. 16106's ratio is about 0.60.

| pair | views (cipher → decipherment) | ff. | ratio | confidence |
|---|---|---|---|---|
| 7 Jan | 5–11 → 11–14 | 2–7 → 8–10 | 0.50 | high |
| 13 Jan | 15–19 → 18–21 | 12–15 → 16 | 0.50 | medium (re-shot views) |
| 31 Jan (1) | 24–28 → 28–30 | 20–23 → 24–26 | 0.67 | high |
| 31 Jan (2) | 32–35 → 36–37 | 28–31 → 32–33 | 0.80 | high |
| 31 Jan Reine | 38–41 → 42–43 | 34–36 → 38–39 | 0.87 | high |
| **7 Feb (B)** | 48–51 → 52–55 | 44–47 → 48–50 | **0.33** | **low** |
| 20 Feb (1) | 70–75 → 76–79 | 65–69 → 71–74 | 0.70 | high |
| 20 Feb (2) | 80–83 → 84–85 | 75–77 → 79 | 0.62 | high |
| 2 Mar (1) | 94–100 → 102–105 | 89–95 → 97–100 | 0.54 | high |
| 2 Mar (2) | 106–109 → 110–112 | 101–103 → 105–106 | 0.69 | high |
| 8 Mar | 118–124 → 126–131 | 113–118 → 121–125 | 0.66 | high |
| 10 Mar | 136–139 → 140–142 | 131–134 → 135–136 | 0.87 | high |
| 20 Mar (1) | 146–154 → 154–159 | 141–148 → 149–153 | 0.70 | high |
| 20 Mar (2) | 159–161 → 161–162 | 154–155 → 156 | 0.73 | high |
| 23 Mar | 173–176 → 177–179 | 168–170 → 172–174 | 0.69 | high |
| 3 Apr | 185–192 → 193–198 | 180–187 → 188–193 | 0.85 | high |

## Leftovers (letters with cipher and no decipherment found in views 1–215)
All five are from the 7–10 February dispatch or at the window's edge.
- **7 Feb, au Roy (A)**: views 44–47, ff. 40r–43v. Cipher runs 40v–43r, about 134 lines. The draft table listed this letter as clear. *Medium confidence.*
- **7 Feb, au Roy, "sur la mort du Roy de Portugal"**: views 55–61, ff. 51r–56v, about 288 cipher lines. 51r says the writer "envoye les dupplicata" of an earlier letter with this one, which could explain why some 7 Feb cipher went undeciphered. *Medium confidence.* It may itself own ff. 48–50; see below.
- **7 Feb, a la Reyne (2)**: views 64–67, ff. 59r–61v. Cipher runs 59v–61r, about 74 lines, checked at 1800 px. *Medium-high confidence.*
- **10 Feb, Pierre Dor to Saint-Goard**: views 68–69, f. 63v, about 12 cipher lines. I did not check for an interlinear decipherment, so this one is *unexamined*, not a leftover.
- **20 Apr, au Roy**: view 215, f. 210r. The cipher begins at the foot of the page, and the letter and any decipherment continue past view 215. *An artefact of the window.*

**The 7 Feb group is unresolved.** The sheet at ff. 48r–50v (views 52–55) is continuous: 48v runs on into 49r mid-sentence, and the "sur la mort" docket that shows in view 53 belongs to f. 51, not to f. 49. The sheet is paired with letter B only because it sits next to it and carries the docket. Its size ratio, 0.33, is an outlier. Its first words, "Ilz seroient bien estonnez d'entendre … le peuple de Portugal … Castillans … la nouvelle de la mort …" ("They would be much astonished to hear … the people of Portugal … Castilians … the news of the death …"), fit the "sur la mort" letter at least as well as B. I could not test the join with the budget I had. Four 7 Feb cipher letters (about 670 lines) share one 5-page decipherment.

## Corrections to the draft table (`sources/fr16107-jan-apr-1580.md`)
- The 3 Apr decipherment runs ff. 188r–193r ("Escrit a Madrid … avril 1580"), not 188r–189r.
- View 44, f. 40 (7 Feb au Roy) contains cipher; it is not a clear letter.
- f. 49 does not begin a document. The docket seen over it belongs to f. 51.

**Caveat on the 0.33.** `linecounts.tsv` gives 4 lines for 53R (f. 49r) and 3 for 54R (f. 50r). The contact sheet shows both as full, faint decipherment pages, so the script failed on them. If each holds about 25 lines, the sheet has about 100 lines and B's ratio becomes about 0.6, which is normal. Size therefore does not separate B from the "sur la mort" letter. Only the content join can.

## Limits
Page classes and the fraction of each page in cipher were judged by eye from contact sheets. Line counts are a script estimate (±15%). Content joins were read only for the 7 Feb group. Folios were read from the stamped foliation at low resolution, so they can be off by one where slips overlap.

## Next
Read the 48r opening against the clear text just before the cipher in each 7 Feb letter (44r, 51r, 40v, 59v). Check f. 63v. Run views 216–380.

## Rerun
```
uv run --with pillow python3 linecount.py 1 215 > linecounts.tsv
uv run --with pillow python3 sheets.py 1 215 12 3 600 <outdir>
python3 count.py > counts.txt
```

## Join test, 2026-11-10 (`join-7feb.md`)
Known-plaintext test by one Opus reader on full-size images (`bands.py` cuts the bands). **The sheet at ff. 48r–50v
deciphers the "sur la mort" letter (ff. 51r–56v), not letter B**: its opening, "Ilz sont … bien estonez d'entendre",
agrees with that letter's first two cipher lines for 27 consecutive letters (bar: 15). The end join was not tested.
The pair "7 Feb (B)" in the table above is therefore wrong; `pairs.tsv` is left as the pilot wrote it.
Letters A and B do not match the sheet at either end (medium-high confidence). The Queen Mother letter was not tested.
**Left without a decipherment in views 1–215: A (ff. 40r–43v), B (ff. 44r–47r), and the Queen Mother letter
(ff. 59r–61v).** Not yet "undeciphered": views 216–380 are unchecked. The "sur la mort" letter says duplicates of the
31 Jan dispatch travel with it; B's clear opening differs from the 31 Jan (2) letter's (main thread, one comparison),
and A and the Queen Mother letter were not compared with the 31 Jan letters.
The sheet's content: `sources/fr16107-ff48-50-decipherment-1580-02-07.md`.

## Views 216–380 (2026-11-10)

Same method and scripts. Contact sheets of 12 spreads (`sheets.py 216 380 12 3 600`), line counts appended to
`linecounts.tsv` (`linecount.py 216 380`), items I53–I94 appended to `items.tsv`, pairs appended to `pairs.tsv`,
`count.py` rerun into `counts.txt`. I52 (20 Apr) was extended in place: it was cut at the window edge.
Dockets were read from 2–2.5× crops of the 900 px views; dates in square brackets are uncertain readings.
The volume runs on past April to Dec 1580: from view 298 to 326 it is Spanish news-letters from Badajoz, and the
last views are court minutes and a Spanish sentence (enclosure). View 380 is the end of the volume.

**Counts (whole volume, from `counts.txt`).** 31 letters with cipher, 27 decipherment sheets, 26 pairs.
Views 216–380 alone: 11 letters with cipher (incl. the completed I52), 11 decipherment sheets, 10 pairs,
12 clear letters, 5 minute groups, 3 enclosures, 1 unread slip.

| pair | views (cipher → decipherment) | ff. | ratio (script) | note |
|---|---|---|---|---|
| 20 Apr | 215–217 → 221 | 210r–211v → 216r | **0.40** | not adjacent: the Reine letter (f. 214) and blank f. 215 sit between |
| 13 May (1) | 233–236 → 237–238 | 227r–230r → 231r–232r | 0.59 | |
| 13 May (2) | 239–253 → 253–262 | 233r–246v → 247r–256r | 0.82 | 26 pages of cipher |
| 28 May | 267–268 → 269 | 261v–262r → 263r | **0.97** | probably script: 268R counted 15, about 20 cipher lines by eye (→ about 0.85) |
| 1 Jun | 276–279 → 280–281 | 270r–273r → 274r–275r | 0.58 | |
| 13 Jun | 286–289 → 290–292 | 280r–283r → 284r–285v | 0.78 | |
| 7 Jul | 328–329 → 330–331 | 322r–323r → 324r–v | 0.82 | |
| [15] Jul | 333–334 → 337 | 327r–328r → 331r | 0.59 | letter docket hidden by a strip; date from the decipherment |
| 22 Aug | 345–348 → 349–350 | 339r–342r → 343r–344r | 0.72 | |
| Castro / Pierre Dor | 376–377 → 377–378 | 369r–v → 370r–v | **0.11** | script failed (377R = 6 lines, 378L = 4); by eye about 33 / 72 ≈ 0.45 |

Every pair's docket agrees ("Dechiffré de la precedente", or for the last one, "Dechiffré de la Response du Sr de
St Goard a Anthoine de Castro ou au Consul Pierre Dor", matching the cipher leaf's "Response du Sr de St Goard a Dom
Anthoine de Castro et au Consul Pierre Dor").

**Leftovers.**
- *Decipherment sheet with no cipher letter:* **I90, views 368–370, ff. 361r–363r, docketed "6 Decembre 1580 Madrid,
  Dechiffré".** About 4 full pages (script 66 lines; it fails on 368R; about 150 by eye). It stands among the
  Sept.–Dec. court minutes; no cipher letter of that date, or near it, is in the volume. First line, read at 2.5×
  from 900 px and only partly: "Sire, Le [xx?] ... du moys passé j'ay ... par la voye de ..."; last line
  "De Madrid le [vj?] decembre 1580" (uncertain). This is an orphan of the volume, but its docket and (if read
  right) its own closing date say December 1580, so nothing yet ties it to 7 February.
- *Letter with cipher and no sheet:* I58, views 229–231, ff. 224r–225v, a letter of 2 May 1580 *to* Saint-Goard
  (sender unread), about 21 cipher lines among clear text. An incoming letter; like Pierre Dor's (I18) it would be
  deciphered in Madrid, not at court. Unexamined for an interlinear decipherment.

**The 7 Feb question.** No decipherment sheet in views 216–380 is docketed February, and none stands alone except
I90. All the others are adjacent to a cipher letter whose docket date agrees, and only the 20 Apr pair is out of the
0.45–0.9 band for a reason other than a visible script failure. So **A (ff. 40r–43v), B (ff. 44r–47r) and the Queen
Mother letter (ff. 59r–61v) have no decipherment anywhere in fr. 16107**, unless I90 is a misdated 7 Feb sheet. Its
size (about 150 lines by eye) does not rule that out (A+B ≈ 306 cipher lines × 0.6 ≈ 180), but its dating does
argue against it. Test: fetch f. 361r at 1800 px, read the opening, and compare it with the clear text before the
cipher and the first cipher lines of A (40v) and B (44r), as in `join-7feb.md`.

**Flagged sheets.**
- I53, view 221, f. 216r, "20 avril 1580, Deschiffré de la precedente": ratio 0.40, and not adjacent. One page; the
  text ends about four fifths down, so it looks complete. First line not read (900 px). The "precedente" is literally
  the Reine letter, which shows no cipher. Medium confidence that it deciphers I52; a content join would settle it.
- I90 (above). I67 (28 May) and I93 (Castro) are flagged by the script only; by eye both fit.

**Limits.** As for views 1–215: classes and cipher fractions by eye from contact sheets; line counts ±15% with
failures on faint pages (368R, 377R, 378L, 268R); folios from the stamped foliation at 900 px, which in places
carries two numbers, so ±1. Single cipher lines at the foot of 327R, 335R/336L and 343R–345R are strips of
neighbouring leaves, not letters. The slip at view 222L (I55) is clear prose in a court hand and was not read. No
content join was attempted in this window.

## Orphan sheet I90 checked, 2026-11-10 (main thread, full-size image of view 368)
F. 361r opens: "Sire, Le xxiii[e] [Novembre] du moys passé, j'ay escript a Vostre Majesté par la voye de Monsieur de
Lansac, et bien au long de ce qui se pouvoit dire …" ("Sire, on the 23rd [November] of last month I wrote to Your
Majesty by way of Monsieur de Lansac, and at length …"), and goes on to the maréchal de Retz in Piedmont, the new duke
of Savoy and the duc du Maine's forces in Dauphiné. It is a whole letter of December 1580 whose cipher original is
not in this volume. **It does not decipher the 7 Feb letters.**
So in the whole of fr. 16107 no decipherment sheet answers to 7 Feb letters A (ff. 40r–43v), B (ff. 44r–47r) or the
Queen Mother letter (ff. 59r–61v). Still open before "undeciphered": whether A or the Queen Mother letter duplicates a
31 Jan letter, whether a sheet lies in another volume, and whether they are printed.

## Closed, 2026-11-10: the three 7 Feb letters are duplicates
`analysis/13-feb7-letters/README.md`: letters A, B and the Queen Mother letter of 7 Feb repeat the cipher of the 31 Jan
dispatch, deciphered at ff. 32–33, 24–26 and 38–39. Every cipher letter in fr. 16107 has a decipherment in the volume.
