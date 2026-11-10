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
