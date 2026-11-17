# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` /
`disputed`), and a source pointer.

## The field (as of 2026-11-16)
- Bourdeau's `cyphersolver` is now a multi-contributor project: 972 write-ups, daily pull requests, and an open
  catalogue of 1,388 unsolved items with class, access and scores. `established` · POPULAR/CLAIMANT ·
  https://dbourdeau.github.io/cyphersolver/catalogue.html, `catalogue.json` (sha256 3f093d32…, fetched 2026-11-16).
- It already publishes a key census: "How keys changed", 783 systems, 1400–1950, by kind, sign type, power and
  device (homophones, nulls, syllable signs, marks). `established` · same site, `key-evolution.html`.
  Consequence: our planned census Q1 (practice by power and decade) would repeat it.
- Its contributors are reading the fr. 15567–15568 letters from Tomokiyo's `henryiii.htm` now (Hautefort,
  Matignon-1 pull requests dated 16 Nov 2026). `established` · catalogue page, PR list.
- Tomokiyo's unsolved list names this repo's es. 132 work (entry dated 11 Nov 2026). `established` · SECONDARY ·
  https://cryptiana.web.fc2.com/code/unsolved.htm (last modified 17 Nov 2026).
- Of that catalogue, 56 items of 1550–1620 can be worked from online images: 17 class A, 22 B, 17 C.
  `established` as a count of his data · `analysis/01-gaps/gaps.tsv`.
- `catalogue.json` does not record work in progress. A target folder in the repository does: no. 2192 was open in
  the catalogue while `targets/sosa1554/` (merged 12 Nov 2026) held a rebuilt key for it. Of 132 class A
  desk-workable items, 43 are named in some target profile (upper bound on taken). `established` ·
  `items/2192/gate.md`, `line/taken.tsv` (879 profiles fetched 2026-11-16).

## The key line's tools (2026-11-16)
- `line/align.py` rebuilds Cp.30 from a pair without anchors: on five synthetic pairs of 3,000 letters with 12%
  reader noise it marks 41–44 values and none is wrong; on a real pair of 885 units (es. 132 f. 255 against the
  Simancas minute) 26 of 29 frequent signs are right and no `certain` value is wrong. `established` for this one
  key design · `analysis/02-calibration-synthetic/result.tsv`, `analysis/03-calibration-real/result.tsv`.
- The held-out scorer gives a shuffled table 0.25. `established` · same files.

## The target: Terranova → Sfondrati, 1583
- Carlo d'Aragona Tagliavia, duke of Terranova, governor of Milan, to Paolo Sfondrati, Spanish ambassador in
  Savoy. BYU Vault MSS 771: 13 of 27 items carry cipher, 14 Aug – 26 Sep 1583, about 30 cipher pages. One more
  letter of 5 Oct 1583 in Vault MSS 518 folder 3, which also holds 38 clear Terranova letters of 1583.
  `likely` · Bourdeau catalogue nos. 2077 and 2518 (vetting notes; not re-counted here).
- Images are open without login (CONTENTdm IIIF). `established` · fetched SCMisc pages 50207 and 53902 at full
  size, 2026-11-16 (`sources/cache/`).
- Bourdeau lists the set as class C (no key), not attempted, prior art "open as far as checked".
  `established` as his statement · catalogue no. 2077.
- Page 50207 (item 6, 14 Aug 1583) is cipher from the first line: figures, letters with marks above,
  three-letter groups (hom, sim, cem, vil, hol, ful, roe) and underlined two-digit figures (58, 98).
  `likely` · my reading of one image; no transcription yet.

## The key family
- Philip II's general ciphers went to governors and ambassadors. Cg.12 was issued early in 1582 (a copy was received
  in Venice 19 May 1582). The next general cipher is Cg.13 (1587). `established` · SECONDARY · Tomokiyo,
  https://cryptiana.web.fc2.com/code/spanish3.htm, citing Devos 1950.
- Cg.12: letters shown by the next letter of the alphabet (a → b), figures, vowel indicators for syllables;
  nomenclature of figures 36–99, a second series 0–99 underlined, two-letter codes (ba, be…) and three-letter
  codes (bal, bel…). `established` as Tomokiyo's description · same page. The table itself is in Devos 1950;
  no image of it is on Tomokiyo's page.
- Cp.30 (1581), which this repo holds as `vargas-mexia-es132/sources/keys/cipher3.tsv`, is "similar to Cg.12 in
  many respects". `established` as Tomokiyo's statement · same page.
- DECODE R9318 is a key record "Duca di Terranova" (BayHStA KÄA 4591 f. 95, numerical, homophonic with
  nomenclature, undated). Images need a login. `established` · https://de-crypt.org/decrypt-web/RecordsView/9318.
