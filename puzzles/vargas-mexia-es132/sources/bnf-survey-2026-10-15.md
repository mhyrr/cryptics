# BnF survey for the es. 132 dive (2026-10-15)

This is a source survey. It contains no decipherment and no readings. It asks what other BnF holdings (Gallica, fonds
espagnol, français, Dupuy, Colbert, Clairambault, NAF) bear on the dive's named walls. Those walls are Vargas's own
dispatches, the 13 Sep 1579 Saint-Goard leak, the 29 Nov 1579 Portugal paper, and the key gaps in Ciphers 2–4.

**Access note.** Gallica returned HTTP 403 to every request on 2026-10-15: the SRU API, the IIIF manifest of es. 132,
and the ark pages, from both urllib and WebFetch. **No Gallica image or Gallica record was viewed in this survey.** The
Gallica arks below come from BnF Archives et manuscrits (BAM) records or from Tomokiyo's pages. Nobody has opened them.
BAM itself works over urllib: a session cookie, then a POST to `resultatRechercheSimple.html`, then
`ajaxGetCompDisplay.html?eadCompId=…` for sub-volumes. The helper scripts were kept in the session scratchpad. Raw
pages are in `sources/cache/bnf-survey/`.

## Summary: best leads

1. **BnF Français 16106: Saint-Goard's own 1578–1579 dispatches from Madrid**, which are originals and partly in
   cipher. Gallica `btv1b90096628`, 380 ff. The volume "includes almost none from 1575–1578" (Tomokiyo). From f. 207
   onward the cipher is the one later passed to Longlée. Mousset (1912) printed a reconstruction of that key, and Tomokiyo
   gives another, so the cipher passages can be read with a published key. **What it would breach:** the 13 Sep 1579
   question, "where Saint-Goard gets las cosas de acá". It would show what Saint-Goard actually reported from Madrid in
   Jul–Aug 1579, and possibly whom he credits.
   - Ribera (2018, pp. 197–198, via en.wikipedia; not seen) says Saint-Goard set his secretary (Longlée) to uncover the
     **Lanssac negotiation of 1579** over Larache. The same account says "the Spanish ambassador in France was surprised
     to see how well apprised Saint-Goard was of the affair", and urged Philip to find out who his contact was.
   - es. 132 already contains f. 217, a copy of Philip's letter of 22 Aug 1579 to Lansac. Our 13 Sep reading has "lo que
     Lan[gro]e dezía".
   - *Hypothesis only, not tested:* "Lan[gro]e" may be Longlée, and the leak may be the Lanssac/Larache affair.
   - A detailed item list of fr. 16104–16111 exists in **fr. 17019, ff. 176–197** (BAM record).
2. **BnF Français 16107 (1580) and 16108 (1581–82): Saint-Goard's later dispatches.** Gallica `btv1b9009661v` and
   `btv1b9009660f`. Both cover Portugal and his Portuguese contacts. Ribera (p. 302, via en.wikipedia) also reports a
   **1581 French interception of the Spanish ambassador's mail in Paris, with the cipher broken for Henri III.** That
   ambassador is Tassis, Vargas's successor. **What it would breach:** context for the 29 Nov 1579 Portugal paper, through
   the French–Portuguese channels. It is also a possible French-side witness to Spanish embassy ciphers just after
   Vargas, if the 1581 decipherments survive (where they are is unknown).
3. **BnF Français 15561, f. 42: Juan de Borja (Prague) to Philip II, 12 Jul 1579, in Cp.30 (= our Cipher 3).**
   Gallica `btv1b9064570k`. BAM catalogues the volume only as "XXII Règne de HENRI III (1579)", inside a general recueil
   (fr. 15540–15584). The record does not say "chiffre" or "espagnol", and the letter is not in DECODE (full DECODE list
   checked, below), so this is a mis-catalogued Spanish cipher page of exactly our period. Tomokiyo reconstructed Cp.30
   from it, and reports a code "108 with a plus sign" for "sa Magd". **What it would breach:** H12 (108⁺ = Su Magestad,
   "no held-out possible in es. 132") gets an outside Cipher 3 witness. It also gives extra Cp.30 text for the key gaps
   (35 = pr/pl; code values). Second question: how did a Spanish royal dispatch reach the French court's papers in 1579?
   That bears on French interception of Spanish mail in Vargas's time.
4. **es. 132 itself: f. 169 is a decipherment**, not a cipher letter. Morel-Fatio art. 78: "Du même au même.
   Déchiffrement. El Pardo, 22 janvier 1579". Gachard's "sauf une seule" refers to it. f. 177 is a decipherment of
   Parma's letter to Vargas of 25 Jan 1579 (art. 81). Tomokiyo's table of contents agrees on both. Neither folio
   appears in our canon, research log or analysis files. **What it would breach:** if f. 169 deciphers a letter whose
   ciphertext is in the volume, it is a full crib for Cipher 3. Candidates are ff. 171/174 (23 Jan 1579, Cipher 3) or a
   letter that went missing. In any case it shows how Vargas's office expanded codes. Cheap: look at canvases 166 and 174
   once Gallica answers.
5. **The Mary Stuart letters (fr. 20506, fr. 2988, Colbert 470): negative for our questions.** Lasry, Biermann and
   Tomokiyo (2023) summarise all the letters. The 1578–1580 ones (F227, F249, F241, F233, F179, F231, F181, F38) never
   name Vargas, Pérez or Escobedo, and contain no leak from the Spanish court. The only Spanish-adjacent detail is an
   enclosure (12 Jun 1578) for "Francisco Berthy", "probably a secretary to Don John of Austria". No full transcription
   set is public: the paper gives one full decryption (F38) plus summaries, and a full edition is announced for 2027
   (POPULAR report).

## Leads table

| Shelfmark | Folios | Date | Content | Cipher? | Catalogued as | URL | Tier | Relevance |
|---|---|---|---|---|---|---|---|---|
| BnF fr. 16106 (Harlay 228 (4)) | 380 ff.; Saint-Goard cipher from f. 207 | 1574, 1578, 1579 | Saint-Goard (French amb. in Spain) dispatches to the court; minutes of court letters | yes, about half of his letters to the King (Gellard 2014 via WP); key published by Mousset 1912 pp. lviii–lix and Tomokiyo | "Ambassades et missions en Espagne de Jean de Vivonne, sr de Saint-Gouard … III Années 1574, 1578 et 1579" | BAM https://archivesetmanuscrits.bnf.fr/ark:/12148/cc462349 ; Gallica https://gallica.bnf.fr/ark:/12148/btv1b90096628 | SECONDARY (catalogue); PRIMARY once read | 13 Sep 1579 leak (Saint-Goard's source); Lanssac/Larache; es. 132 f. 217; "Lan[gro]e" |
| BnF fr. 17019 | ff. 176–197 | n/d | Detailed item list of fr. 16104–16111 | n/a | per BAM record of fr. 16104–16111 | (not checked) | SECONDARY | finding aid for lead 1 |
| BnF fr. 16107 (Harlay 228 (5)) | 372 ff.; f. 63 (Pierre Dor, Lisbon, 10 Feb 1580), f. 225 (d'Abadie, 2 May 1580) | 1580 | Saint-Goard dispatches; Portugal succession | yes | "IV Année 1580" | https://gallica.bnf.fr/ark:/12148/btv1b9009661v | SECONDARY | 29 Nov 1579 Portugal paper (French Portuguese channels); Saint-Goard's man taken at Irún (f. 267) |
| BnF fr. 16108 (Harlay 228 (6)) | 471 ff. | 1581–1582 | Saint-Goard dispatches; possible 1581 interception of the Spanish ambassador's mail | yes | "V Années 1581 et 1582" | https://gallica.bnf.fr/ark:/12148/btv1b9009660f | SECONDARY | French intercepts of Spanish embassy cipher just after Vargas (Ribera p. 302, unverified) |
| BnF fr. 15561 | f. 42 | 12 Jul 1579 | Juan de Borja, Prague, to Philip II: Parma's taking of Maastricht | yes, Cp.30 = Cipher 3 (Tomokiyo) | "XXII Règne de HENRI III (1579)" in "Recueil de lettres … Charles IX, Henri III …" (fr. 15540–15584); not in DECODE | https://gallica.bnf.fr/ark:/12148/btv1b9064570k ; Tomokiyo http://cryptiana.web.fc2.com/code/henryiii.htm , spanish3.htm | SECONDARY (Tomokiyo); PRIMARY once read | H12 (108⁺ = Su Magestad) outside es. 132; Cp.30 values (H11 35 = pr); French possession of a Spanish dispatch in 1579 |
| BnF fr. 15560, 15562–15563 (same recueil) | whole volumes | c. 1579–1580 | Letters to Henri III's court (often to Villeroy). fr. 15562 ff. 65–70 are French cipher letters from Antwerp, 16 Jan 1580 (not Spanish) | Tomokiyo: 15560 "apparently no cipher"; 15563 "apparently no cipher" | "Règne de Henri III" | Tomokiyo henryiii.htm; fr. 15562 Gallica https://gallica.bnf.fr/ark:/12148/btv1b9064029p | SECONDARY | other Spanish intercepts of 1579–80 might sit unflagged in the same recueil (not swept) |
| BnF es. 132 | f. 169 | 22 Jan 1579 | Philip II to Vargas: "Déchiffrement" | decipherment (clear) | Morel-Fatio art. 78; Tomokiyo TOC no. 78 | Gallica canvas ~166 | SECONDARY (catalogue) | Cipher 3 key gaps if its ciphertext is in the volume (ff. 171/174?); not in our files |
| BnF es. 132 | f. 177 | 25 Jan 1579 | Parma to Vargas: "Déchiffrement" | decipherment (clear) | Morel-Fatio art. 81 | Gallica canvas ~174 | SECONDARY | Parma–Vargas cipher; context |
| BnF es. 336 (Morel-Fatio 183; Saint-Germain Harlay 262) | ff. 72, 74, 78 | 25 Nov 1579 | Antonio de Castro, Cascais, to Saint-Goard (Portuguese), French translation, and copy to the King of France | no | "Lettre d'Antonio de Castro à M. de S-Goard …" | Morel-Fatio 1892 pp. 67–68 (archive.org `cataloguedesmanu00bibl_0`) | SECONDARY | Portugal channel to the French court in exactly the week the Portugal paper is in Paris (29 Nov 1579) |
| BnF es. 336 | f. 79 | undated | "Note remise par l'ambassadeur d'Espagne au roi de France pour obtenir qu'aucun secours ne soit accordé aux rebelles de Flandre". Copy | no | as quoted | same | SECONDARY | could be Vargas (1578) or Álava (1560s); unplaced |
| BnF es. 336 | f. 69 | 5 Nov 1571 | Zúñiga (Rome) to Álava (Paris), Cg.6 | yes, undeciphered | in Morel-Fatio | Tomokiyo spanish3.htm | SECONDARY | calibration only (a Paris embassy cipher before Vargas) |
| BnF fr. 20506, fr. 2988, Colbert 470 | listed in Lasry et al. §3.2 | 1578–1584 | Mary Stuart's cipher letters to Castelnau | yes, solved | fr. 20506: "dépêches chiffrées … relatives surtout à l'Italie"; fr. 2988: "Pièce en chiffre" | Lasry, Biermann, Tomokiyo, Cryptologia 47(2), 2023, doi:10.1080/01611194.2022.2160677 (PDF cached) | SCHOLARLY | negative: no Vargas, Pérez, Escobedo or Spanish-court leak in the 1578–80 summaries |
| BnF Colbert 472 | p. 347 | c. 1580s | A Castelnau cipher table | key | n/a | Lasry et al. 2023 fig. 16 | SCHOLARLY | French side only; not relevant |
| DECODE records 1960–2025 | es. 132 by folio | 1577–1580 | 60 records, "Decrypted", owner 83, created Dec 2020 – Jan 2021, with key documents "Cp30 [key]", "Vargas Mexia's Cipher 2/3/4 [key]" | yes | DECODE | https://de-crypt.org/decrypt-web/RecordsView/1977 (and 1960–2025) | SECONDARY | the Cipher 2/3/4 key documents are behind login (we got a placeholder image); a free account might expose Tomokiyo's key sheets |

## Checked and empty

- **Morel-Fatio 1892, *Catalogue des manuscrits espagnols et portugais*** (archive.org `cataloguedesmanu00bibl_0`, OCR
  cached):
  - The index entry "Vargas Mexia (Juan de)" points only to no. 184 (= es. 132). No other espagnol volume holds Vargas
    material.
  - "Perez (Antonio)" points to 178 (later Pérez pieces, 1590s), 183 arts. 12, 47, 48 (Pérez 1590s letters), 186 and 531.
    None is from 1577–1580.
  - "Saint-Goard" points only to es. 336 art. 37.
  - Every 1577–1580 date outside no. 184 was grepped. Nos. 185–186 (= es. 421–422, 17th-century copybooks) hold copies of
    Portugal-succession papers of 1579–1580 and the King's letter to the Duke of the Infantado on Éboli's arrest
    (29 Jul 1579, printed in Pérez's *Obras*). There is no Council of War paper on taking Portugal, and nothing in
    cipher.
  - No Spanish key (cifra general or particular) of 1577–1581 appears in the catalogue. Es. 455 holds a 1586 notebook of
    "Cifras con diversos señores" with decipherments, but Morel-Fatio dates the ciphers late 15th / early 16th century.
- **BAM keyword search "Vargas Mexia":** 64 hits, 63 of them es. 132 items. The other is es. 66, a false hit on
  "Mexia". "Saint-Gouard", "Saint-Goard" and "Lansac Larache" returned 0 hits as keywords. "Vivonne Espagne" found the
  fr. 16104–16111 record.
- **Ochoa 1844** (cached in the dive): no. 9999 says the volume ends with "diez hojas" in French and Italian, some
  "aclaraciones de lo que está en cifra". Morel-Fatio describes those leaves (arts. 126–129) as an Italian copy, a
  French memoir and the Blois articles. No decipherment is listed among them except ff. 169 and 177. The neighbouring
  Ochoa entry (10255) is unrelated.
- **Viète for Henri III, 1577–1581:** no published decipherment by Viète of a Spanish dispatch earlier than 1589 was
  found. His documented Spanish work (Moreo, Mendoza, Tassis 1593) sits in fr. 3641, 3977, 3982–3984 and Colbert
  500/33, all 1589 or later. The `viete-f539` dive's volume (Colbert 33) is 1594. None of this touches Vargas's years.
- **Mary Stuart letters:** see Summary 5. Spanish content in 1578–80 is limited to Mary's comments on Anjou, Spain and
  England. Mendoza (London) appears only as the Spanish ambassador in England from 1583.
- **DECODE (full list of 10,106 records fetched once with `recperpage=ALL`):**
  - Paris/BnF records dated 1570–1585 or "16th century" (167): Spanish-language ones are only the 60 es. 132 records.
  - None for fr. 15561, fr. 16106–16108, or any other Spanish cipher in the fonds français of 1577–1581.
  - Other BnF 16th-century cipher holdings in DECODE (fr. 3995, 3616, 3022, 20506, an "italien 1583" group) are French
    or Italian.

## Walls met

- **Gallica 403** (all endpoints, both fetchers). Nothing above was viewed. Re-run when Gallica answers. The breach is a
  browser session, or a later retry from this laptop.
- **DECODE key documents** need an account (placeholder image returned). Downloaded placeholders were left in
  `cache/bnf-survey/decode-keys/` (deleting them was not permitted). They contain no data.
- **Ribera 2018** (*Diplomatie et espionnage*, Classiques Garnier) is not online. The Lanssac and 1581 claims come from
  en.wikipedia's summary with page cites.
- **Cryptologia full text:** tandfonline returned 403. The paper was read from a republished PDF
  (friendsofsheffieldcastle.org), cached as `lasry-biermann-tomokiyo-2023.pdf` / `lasry2023.txt`.

## Unverified claims

- That "Lan[gro]e" in the 13 Sep 1579 letter (ff. 222/226) is Longlée, and that the leak concerns the Lanssac/Larache
  affair. This is the surveyor's inference from Ribera-via-Wikipedia, the f. 217 Lansac letter, and Castries's
  Moroccan-series printing of Vargas letters of Jul–Sep 1579. Not tested.
- Ribera 2018 pp. 197–198 (Vargas surprised by Saint-Goard's knowledge of Lanssac's negotiation; asks Philip to trace
  his contact) and p. 302 (1581: Henri III held the Spanish ambassador's mail and had its cipher broken). Known only
  through en.wikipedia "Jean de Vivonne" (SECONDARY, wikitext cached `wp-jean-de-vivonne.wikitext`).
- Tomokiyo: fr. 15561 f. 42 is Borja's letter in Cp.30, with 108⁺ = "sa Magd". Tomokiyo's pages are fetched and
  cached, but the image is not seen.
- Tomokiyo: Saint-Goard's cipher changes at fr. 16106 f. 207, and fr. 16106 has "almost none from 1575–1578". BAM's
  title says "1574, 1578 et 1579", which is consistent.
- Allaire (1997), "Le décodage de la correspondance chiffrée des diplomates espagnols au XVIe siècle" (*Correspondre
  jadis et naguère*, pp. 207–218). Per Tomokiyo, its annexe reconstructs Cp.30 from **Vargas's own letter to the King of
  9 Apr 1579**. That is a Vargas dispatch in Cipher 3; its archive is unknown and Allaire was not seen. This bears
  directly on wall 1 and the Cipher 3 key.
- Mendoza to Zayas, London, 5 May 1578 (CSP Spain ii, quoted by Tomokiyo): Vargas gave Mendoza "a very small cipher"
  and "did not use the general cipher". It is a possible description of one of es. 132's small ciphers. Not checked
  against CSP.
- Ochoa's description of the final leaves as containing "aclaraciones" of the cipher. It conflicts with Morel-Fatio's
  item list (above).
- Whether ff. 169/177 are contemporary decipherments made in Vargas's office or later ones, and whether f. 169's
  ciphertext survives in the volume.
- The full 2027 edition of Mary Stuart's letters (Routledge, Paranque et al.) rests on a search-result summary of
  Northeastern University news. Not read.

## Sources

- Morel-Fatio, *Catalogue des manuscrits espagnols et des manuscrits portugais* (1892), archive.org
  `cataloguedesmanu00bibl_0`, nos. 183–186, 454–455 and index (SECONDARY). Cached `morel-fatio-1892_djvu.txt`.
- Gachard, *La Bibliothèque nationale à Paris* I (1875), pp. 415–424, archive.org `labibliothque01gach` (SCHOLARLY).
  Cached `gachard-1875-v1_djvu.txt`.
- BnF Archives et manuscrits: fr. 16104–16111 https://archivesetmanuscrits.bnf.fr/ark:/12148/cc462349 ; fr. 15540–15584
  search hit "Français 15561" (SECONDARY). Cached `bam-*.html`.
- Tomokiyo, Cryptiana: "French ciphers during the Reigns of Charles IX and Henry III"
  http://cryptiana.web.fc2.com/code/henryiii.htm ; "Spanish Ciphers during the Reign of Philip II"
  http://cryptiana.web.fc2.com/code/spanish3.htm ; "Reading an Undeciphered French Letter from Antwerp (1580)"
  http://cryptiana.web.fc2.com/code/antwerp.htm (SECONDARY). Cached `cryptiana-*.htm`.
- Lasry, Biermann, Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578–1584", *Cryptologia* 47(2) 2023,
  doi:10.1080/01611194.2022.2160677 (SCHOLARLY). PDF via
  https://friendsofsheffieldcastle.org/wp-content/uploads/Deciphering-Mary-Stuart-s-lost-letters-from-1578-1584.pdf ;
  OpenAlex metadata cached.
- en.wikipedia "Jean de Vivonne" (SECONDARY, citing Ribera 2018, Gellard 2014, Amalric 2018).
- DECODE/DECRYPT database https://de-crypt.org/decrypt-web (SECONDARY). Full list cached `decode-all.html`; filtered
  subset `decode-bnf-1570-1585.txt`.
