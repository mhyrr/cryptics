# Screenshot opportunities: a known key plus pages behind a viewer (2026-10-18)

*Agent survey, 2026-10-18. Inputs: `CLAUDE.md`, `sources/untouched-data/09-review-2026-10-16.md`,
`10-decryptable-resweep-2026-10-18.md`, `puzzles/vargas-mexia-es132/NEXT.md`, the repo's BnF and Italy surveys, and a fresh
`git clone` of Bourdeau's `dbourdeau/cyphersolver` (last commit 14 Oct 2026), including its cached copies of Tomokiyo's
cryptiana pages (`research/gallica_sweep/src/*.txt`, `research/gallica_siblings/src/*.htm`). About 25 web searches.
**WebFetch failed with DNS `ENOTFOUND` on every host tried** (themorgan.org, revistas.um.es, ecp.ep.liu.se,
publikationen.badw.de), so web facts below rest on search-result text, and most "where the key is" facts rest on
Bourdeau's repository and the cached Tomokiyo pages (both SECONDARY). No readings were attempted (rule 9).*

## Summary

1. The best use of Greg's browser is still **es. 132's four unread royal letters (ff. 39, 50, 79, 150)**, plus f. 129 as a
   held-out duplicate of the already-read f. 132. The key, the pipeline and a verifier are all in this repo. About 12 images.
2. The best new find is **BnF fr. 3641 nos. 27, 48, 50 and 58**: Spanish cipher letters of 1589–92 that Bourdeau's
   catalogue says read with **Cp.30, our own Cipher 3**, and Tomokiyo's 1592 syllabic cipher. Bourdeau set them aside on
   22 Sept as "key lookups", not new solves. About 10 images.
3. **Saint-Goard's 1579 dispatches (fr. 16106)** with Mousset's printed key remain the best outside check on es. 132.
   The volume is large, so Greg should first capture its item list (fr. 17019 ff. 176–197), then about 20 pages of
   Jul–Sep 1579.
4. Five more Gallica letters have a key that Tomokiyo or Lasry has published but nobody has applied, by Bourdeau's
   22 Sept list. Each takes 2–25 images: Sancy, Baugy, Dodieu, Péricard, Sabran. Rows 6–9 (Morgan, HHStA, DECODE, PARES)
   are complete-list rows. Each needs a login, a scan order or a reading-room request, not screenshots.
5. Shortcut for every Gallica row: in a normal browser, the IIIF URL
   `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<view>/full/full/0/native.jpg` returns the full-resolution page
   (Bourdeau's notes report 3000–5000 px). Saving that file beats a screenshot. Use it unless Gallica refuses it in the browser too.

## Ranked table

"View" means Gallica's image number (`/f<view>.item`), not the folio number. Ranking: verifier first, then
novelty (crowding), then Greg's time.

| # | Document | Key source (tier) | Viewer + shelfmark + folios | ~Images | Verifier | Crowding | Login? |
|---|---|---|---|---|---|---|---|
| 1 | **Philip II → Vargas Mexía, 1578**: four unread royal letters (Madrid 16 Apr; Bosque de Segovia Jun; El Pardo 4 Aug; Madrid 30 Nov 1578). These are the King's instructions to his Paris ambassador in the months after Escobedo's murder | Cp.30 / Cipher 3 (Devos 1950 via Tomokiyo), `puzzles/vargas-mexia-es132/sources/keys/cipher3.tsv` (SECONDARY; repo-verified on 13 letters) | Gallica, BnF **Espagnol 132**, `btv1b10032556x`: **ff. 39, 50, 79, 150**, plus **f. 129** (duplicate of the already-read f. 132). Spreads: f. N recto ≈ view N−3 (right page), verso ≈ view N−2 (left) (from `fetch_pages.py`, f. 32r = view 29) | 10–12 spreads | Two blind readers (frozen exp-09 protocol); f. 129 vs f. 132 is a **held-out duplicate**; Paz summaries of Vargas's replies (K 1546–1551) | Uncrowded: no es. 132 entry in Bourdeau; cabinet-noir and Tomokiyo stopped | No |
| 2 | **Spanish cipher letters in BnF fr. 3641, nos. 27, 48, 50, 58**: Bernardino de Mendoza's Paris embassy papers, 1589–92, which came into French hands | Cp.30 (our Cipher 3, in repo) and Nevers collection key **no. 54** = Tomokiyo's "Syllabic Numerical Cipher (1592)" (Philip II–Parma/Sessa/Ibarra) (SECONDARY: Tomokiyo nevers.htm, cached in Bourdeau `research/gallica_sweep/src/nevers.txt` l. 573) | Gallica, BnF **fr. 3641**, `btv1b52508089f`. Pieces nos. 27, 48, 50, 58; folios not mapped. Anchors: no. 6 = f. 14 = views 35–36; no. 36 = f. 76 = view 169. Find each piece by its "N°" mark | 8–12 | Key from an independent source must yield continuous Spanish; Mendoza's own minutes and the AGS K-series as cribs; sibling decipherments in the same volume (nos. 4, 29, 44 decipher nos. 3, 28, 43) | **Parked by Bourdeau** (catalogue 319, 22 Sept 2026: "Nevers key no. 54 and Cp.30") as key-lookup, not a solve target. No reading found | No |
| 3 | **Saint-Goard (French ambassador, Madrid) → Henri III and Catherine, 1578–79**: the cipher passages, including whatever he reported in Jul–Sep 1579 about the Lansac/Larache affair and "las cosas de acá" | Mousset (1912), pp. lviii–lix, key reconstruction (via Tomokiyo; page refs from repo survey, not seen); Tomokiyo's own reconstruction (SECONDARY) | Gallica, BnF **fr. 16106**, `btv1b90096628`, cipher from **f. 207** to the end (380 ff.); item list in **fr. 17019 ff. 176–197**; continuation fr. 16107 `btv1b9009661v` (1580), fr. 16108 `btv1b9009660f` (1581–82) | 22 (fr. 17019 list) + ~20 (Jul–Sep 1579) | The key comes from another source, so readable French is a mechanical check. Es. 132 (Spanish side, same events) as cross-check | Not in Bourdeau (0 grep hits for Saint-Goard/Saint-Gouard); Tomokiyo worked the key; no edition of the passages found | No |
| 4 | **Sancy (French ambassador, Constantinople) → Henri IV and Puisieux**, two unread letters | "Sancy Cipher-2", recoverable from glossed (deciphered) letters in the same volume (Bourdeau catalogue 311, SECONDARY) | Gallica, BnF **fr. 16148, ff. 200, 206** + the glossed siblings in the same volume (Gallica ark not confirmed here) | 6–10 | Key rebuilt from glossed pairs predicts held-out glossed passages before it touches ff. 200/206 | Parked by Bourdeau (catalogue 311) | No |
| 5 | **Nicolas de Baugy → Mangot, c. 1616–17**, two letters | Tomokiyo's Baugy key (louisxiii.htm; key image `louisxiii_Baugy.png` cached in Bourdeau repo) (SECONDARY) | Gallica, BnF **Clairambault 369**, `btv1b9000782k`, **ff. 2, 59** (key specimen f. 109) | 4–6 | Published key → continuous French; f. 109 specimen | Parked by Bourdeau (catalogue 309); Baugy key used by Bourdeau only for an elimination (cocquet target) | No |
| 6 | **Dodieu de Vély → Montmorency (1530s, Charles V's court)**, two letters | Tomokiyo "Dodieu Cipher 1" (francis-era page, not fetched) (SECONDARY) | Gallica, BnF **fr. 20506, ff. 49, 52** (ark: `btv1b525047581` per Bourdeau link; confirm) | 4 | Published key → continuous French; Dodieu edition (rom.uga.edu) for context | Parked by Bourdeau (catalogue 308) | No |
| 7 | **Péricard → unknown, Paris, 21 Jul 1593** (League) | Tomokiyo's reconstruction from no. 69 (f. 146, Péricard → Mercœur, 11 Jul 1593) incl. figure codes 10–59 (SECONDARY; league.txt l. 284–288) | Gallica, BnF **fr. 3984 no. 73, f. 152**, `btv1b9060633d`, plus f. 146 for the key | 2–3 | Short; key from a sibling. Weak (few figures) | Parked by Bourdeau (catalogue 313) | No |
| 8 | **Sabran → Bouthillier, 1633 and 1635** (about 18 cipher passages): the French resident's reports from Genoa/Italy | Lasry's 1631 Louis XIII–Sabran key, image on Tomokiyo GL.htm (SECONDARY) | Gallica, BnF **fr. 4134 ff. 46–73; fr. 4135 ff. 132–251** (arks not confirmed) | ~25 | Published key → continuous French; held-out passages | **Risk:** Tomokiyo reports that Lasry "found the same cipher" in these letters, so he may have read them. Check GL.htm first. Parked by Bourdeau (310) | No |
| 9 | **Sega / Baudouin-Desportes / Mauclerc, 1593** (papal-side League letters) | Tomokiyo League polyphonic key (mayenne.htm) | Gallica, BnF **fr. 3984 ff. 186, 189** (`btv1b9060633d`); fr. 3985 no. 7 (`btv1b90606498`) | 6, at maximum resolution | Total, once the glyphs read; 1,100 aligned glyphs on f. 188v (Bourdeau) as calibration | **Bourdeau attempted 17 Sept, stopped at glyph accuracy (75–79%)**. Our two-reader protocol is the untested lever | No |
| 10 | **Philip IV → Marquis de Velada, London, 1636–41**: 23 cipher letters marked "not deciphered" | Recoverable from the 12 deciphered letters in the same lot. No printed key found | Morgan Library, record **130074** (35 letters), related 130090 and 130097. **"MA Unassigned"**, so almost certainly no Corsair images | n/a: reading-room request or scan order | Pairs from the deciphered 12 predict held-out text; AGS Estado minutes of the same letters (if they survive) are a full crib | Open (no published reading; not in Bourdeau) | Morgan reading-room registration |
| 11 | **Ungnad → Maximilian II, 12 Mar 1576; Sinzendorff → Rudolf II, 1578** | DECODE R392 (Ungnad's key; transcribed in Bourdeau repo) and R1384 (SECONDARY) | ÖStA/HHStA **Türkei I 32-3 ff. 199–203; 37-2 ff. 1–8**. Not digitized | n/a: ~26 scans ordered | Key lookup with no homophones; Gerlach's *Tage-Buch* | Bourdeau blocked on the same scans; coordinate | ÖStA order |
| 12 | **Charles V's Rome ambassadors 1555: Manrique & Toledo → Charles V (9 Feb 1555); Juan de Vega → Prince Philip** | Tomokiyo identified the Imperial Cipher of 1544–54; *Estudios Románicos* 34 (2025) papers reconstruct related imperial ciphers (SCHOLARLY, abstracts only) | PARES, **AGS Estado leg. 882 ff. 15–18** and **leg. 873 f. 4** (DECODE R9965, R9964). Whether PARES has these images is not verified; PARES serves only about 1000×1400 px (Bourdeau, estrada1503/toledo1565) | 4–8 | Published or reconstructed key; DECODE attachments to compare | Bourdeau set both aside (289, 323) as "probably unread"; DECODE labels them "Decrypted" with no text | DECODE login for the attachments; PARES none |
| 13 | **Cosimo I → Agnolo Niccolini** (Medici envoy), 21 letters | Cifrario **R4033** filed in the same ASF file (PRIMARY via DECODE) | DECODE R4034–R4054 (ASF images) | ~25 | The key is filed with the letters | Parked by Bourdeau (330) | **DECODE login with image rights** |
| 14 | **Intercepted French diplomatic letters, 1716–18 (Châteauneuf, La Marck, d'Iberville)**: the 12 of 38 with no decipherment written over the cipher | Plaintext written over the cipher in 26 sibling records, so the key comes from those pairs | BL **Add MS 61574** (Blenheim Papers, intercepted correspondence 1716–18, "partly in cipher with some decipherments", per BL record via search); DECODE R8052–R8088 | ~40 | Key from 26 pairs; held-out pairs | Parked by Bourdeau (294) | DECODE login; BL images not known to be online |
| 15 | **Gondomar's correspondence, Real Biblioteca (II/2106–2239)**: cipher letters to the London ambassador, 1613–22 | Nomenclators of 1614 (RB II/2183 doc. 25) and 1625 (II/1850 doc. 17) in the same collection; *Avisos* 100–101 (2023) used them (SCHOLARLY) | Real Biblioteca. **Digitization not confirmed** | unknown | Collection keys; *Avisos* readings (Gaytán, II/2170; II/2213) as calibration | Partly crowded: Real Biblioteca/*Avisos* authors are working through it | Unknown |

## Greg's shopping list (top 3)

General settings for all three. Use a desktop browser at full-screen. In the Gallica viewer, the **f-number in the URL is the
image (view) number**, and the stamped folio number is written at the top right of each recto. Check it on the image.
**Preferred capture:** open `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<view>/full/full/0/native.jpg` in a new tab
and Save As `<shelfmark>_v<view>.jpg`. **Fallback:** the viewer's download button (Télécharger), which offers a full-size
JPEG. **Last resort:** screenshots. Zoom until one line of cipher fills the screen width, then take overlapping
screenshots top to bottom (about 4–6 per page), with the stamped folio number visible in the first one. Do one request
at a time, with no parallel tabs hammering the server.

### 1. es. 132, ff. 39, 50, 79, 150 (+ f. 129)

Ark `btv1b10032556x`. Each view is an opening (verso left, recto right), and f. N recto is on view ≈ N−3.

1. Open `https://gallica.bnf.fr/ark:/12148/btv1b10032556x/f36.item` and confirm that the right-hand page is stamped **39**.
   If it is not, step ±1 until it is, and note the offset.
2. Save views **36, 37** (f. 39r–v), **47, 48** (f. 50r–v), **76, 77** (f. 79r–v), **147, 148** (f. 150r–v),
   **126, 127** (f. 129r–v), adjusted by the offset from step 1. If a letter runs onto the next leaf, also save the
   following view.
3. Native IIIF size for each view (expect roughly 6000 px wide for an opening). If you screenshot instead, zoom so
   that the numeral marks above the figures are clearly separate (about 2–3× the "fit page" view).
4. Drop the files in `puzzles/vargas-mexia-es132/sources/cache/gallica-manual/`, named `es132_v036.jpg` and so on.

### 2. fr. 3641, nos. 27, 48, 50, 58

Ark `btv1b52508089f`.

1. Open `https://gallica.bnf.fr/ark:/12148/btv1b52508089f/f1.item`. The volume's pieces carry ink numbers "N° 27"
   and so on. As a guide, no. 6 = f. 14 = views 35–36, and no. 36 = f. 76 = view 169. So **no. 27** should lie roughly between
   views 120 and 165: step through until you find it, then save every view of that piece (cipher pages and the
   address leaf).
2. Do the same for **48, 50, 58**, which lie after view 169 (probably views 190–260).
3. Also save the views of **nos. 3/4, 28/29 and 43/44** (cipher + period decipherment pairs) if they are within a few
   views of your path. They are calibration cribs: they let us test Cp.30 on a known answer before reading the four targets.
4. Native IIIF size. Name the files `fr3641_v<view>.jpg`.

### 3. Saint-Goard: fr. 17019 (item list), then fr. 16106 Jul–Sep 1579

1. **Item list first:** BnF fr. 17019, ff. 176–197 (detailed list of fr. 16104–16111). Find its ark by searching
   "Français 17019" on gallica.bnf.fr, then save the ~22 views of ff. 176–197. With these, we can tell you exact
   folios for every 1579 dispatch, instead of you paging through 380 leaves.
2. Then open fr. 16106, `https://gallica.bnf.fr/ark:/12148/btv1b90096628/f1.item`. Once we send the folio list from
   step 1, save the dispatches dated **July to September 1579** (expect 15–25 views). Before the list arrives, it is safe
   to save the first few cipher pages after **f. 207**, so that the key can be tested on them.
3. Native IIIF size. Name the files `fr16106_v<view>.jpg`.

## Set aside (checked, and why)

- **Henri IV ↔ Landgrave Moritz of Hesse, 1603–05:** the ciphertext is printed in Rommel 1840 (Google Books) and the key
  in Rommel 1846 / BnF Clair 360 (Tomokiyo henryiv page). However, Moriz Ritter (1871, Bavarian Academy) wrote
  "Die chiffrirten Stellen in Rommel's Correspondance inédite…". That makes this a **calibration case** (rule 7), not a
  new reading. It is cheap (one print book) if we want to score a reader against a known answer.
- **Henri IV → Maisse, fr. 16093:** solved by Bourdeau (Brienne clear copies).
- **Philip II → Mendoza, fr. 3641 nos. 5/6:** resolved by Bourdeau (period decipherments in the volume). Only nos. 27, 48,
  50 and 58 remain (row 2).
- **Granvelle/Renard (Besançon) and Simancas Estado Flandes 507–516, Roma 899–903:** the 2025 *Estudios Románicos* papers
  (Pich-Ponce; Luo; Leone) publish keys, but the letters carry decipherments in the margin or facing the text (CCFr
  records), so the text is not new.
- **Gualterio / Botti, BL Add MS 20443:** the BL record says "many in cipher, with decipherings". The tables are Add MS 20582
  (not 20244, as Bourdeau's note has it). Little new text.
- **Siena Concistoro 2308:** this is key search, not a key in hand, and Lasry is active (14 Oct). See resweep #4.
- **Madison → Randolph 1782:** Burnett (1917) called these "never deciphered", but modern editions very probably decode them.
  Not checked, so not listed.

## Unverified claims

- That the Gallica IIIF `native.jpg` URL works from Greg's browser. Bourdeau's notes report that it works with a browser
  User-Agent. This container got CONNECT 403.
- **Row 2:** that nos. 27, 48, 50 and 58 of fr. 3641 are cipher letters still unread, and that Cp.30 / Nevers no. 54 is
  the right key. This rests only on Bourdeau's CATALOGUE.md line for item 319 (SECONDARY). Their folios and dates were
  not seen. The view guesses are extrapolations.
- **Row 3:** that Mousset (1912) prints the key at pp. lviii–lix. This comes from the repo's 2026-10-15 BnF survey, citing
  Tomokiyo. A web search on 18 Oct found Mousset's 1908 Longlée thesis but did not confirm the 1912 edition or its key.
- **Rows 4–8:** the keys and the "parked" status come from Bourdeau's CATALOGUE.md (22 Sept 2026 list), and Tomokiyo's
  pages as cached there. The cryptiana pages themselves could not be reached. Lasry may since have read the Sabran
  letters (row 8). The arks for fr. 16148, 4134 and 4135 were not found, and the fr. 20506 ark is inferred.
- **Row 10:** whether the Morgan has images, and whether "deciphered" means interlinear decipherment or a separate
  summary. The "MA Unassigned" accession is from search text only.
- **Row 12:** that AGS Estado 873 and 882 are digitized on PARES, and that the DECODE attachments do not match these leaves.
- **Row 14:** that Add MS 61574 is the volume holding the Châteauneuf/La Marck/d'Iberville records. The BL group record
  (Add MS 61569–61574, 1716–18) was seen in search text only.
- **Row 15:** whether any Gondomar II/ volume is digitized, and how many cipher letters are unread.
- Image counts are estimates, not counts of the volumes.
- DECODE image access: Bourdeau used a logged-in session. Whether a fresh free account gets image rights was not checked.
