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
- BNCF Teca serves 300 dpi masters of the Carte Machiavelli without login
  (`ImageViewer?idr=<image id>&azione=showImg&usage=2`, about 2,700 × 3,700 px). `established` · `items/2911/fetch.py`
  ran; `items/2911/PROVENANCE.md`.
- The cipher of the Dieci di Balìa with Machiavelli in August 1510 (Carte Machiavelli V/134, V/125, V/135, V/136,
  V/140) has a surviving period key online: Carte Machiavelli VI/82, units 1–4, four sheets of one cipher.
  `likely` · PRIMARY (the sheets), compared by one isolated Fable agent on sign inventory (13 of 13 distinctive
  signs) and six glossed signs; no letter was decoded with it. `items/2911/keysheet-check.md`.
- V/139 cc. 1v–2r is Machiavelli's autograph decipherment of V/140. `likely` · BNCF record as quoted by the scout,
  `items/2911/gate.md`; not re-read by the main thread.

## The key line's tools (2026-11-16)
- `line/align.py` rebuilds Cp.30 from a pair without anchors: on five synthetic pairs of 3,000 letters with 12%
  reader noise it marks 41–44 values and none is wrong; on a real pair of 885 units (es. 132 f. 255 against the
  Simancas minute) 26 of 29 frequent signs are right and no `certain` value is wrong. `established` for this one
  key design · `analysis/02-calibration-synthetic/result.tsv`, `analysis/03-calibration-real/result.tsv`.
- The held-out scorer gives a shuffled table 0.25. `established` · same files.
- `line/align.py` fails when the plain side of a pair is an abridgement. On no. 2911 it valued 97% of sign places
  as null and no letter, on four runs. Its model assumes both sides hold the same text end to end. `established` ·
  `items/2911/results/heldout.tsv`, `items/2911/outside/diagnosis.tsv`.
- `align.py build --abridged` rebuilds the 2911 key blind from V/140 and the 1877 print: on the full pair 33 of
  36 marked rows right, place precision 0.935, recall 0.617, no null; on the first page 36 of 36. On two letters
  that took no part in the build, 94% (V/134) and 79% (V/125, another hand) of the signs it values agree with
  the period key. `established` for this pair; the builder's costs were fitted to it and the full pair was
  scored twice · `items/2911/bench/README.md`, `items/2911/bench/runs/results.tsv`.

- `tied.py blind` (items/2351) rebuilds the no. 2351 key from letter A and reader PE's loose plain text
  without the answer: 74 signs marked, 55 shared with the answer, 53 the same (0.964); place precision 0.984,
  recall 0.847. It ties a marked sign to consonant(base) + vowel(mark) and treats an unmarked base as a sign
  of its own. Two scored runs, both registered first, both pass. `established` for this one pair; the model's
  shape used one lesson disclosed from the answer, and 19 marked signs have no answer value to judge them ·
  `items/2351/bench/README.md`, `items/2351/bench/runs/results.tsv`.

## Item 2911: the Dieci's cipher with Machiavelli, August 1510 (known-answer pilot)
- Under the period key (VI/82, as read by one isolated agent) the cipher side of V/140 is 53% syllable signs,
  41% letter signs, 0.2% nulls, 1.67 letters per valued sign, 4,619 letters in all. `likely` (one agent's
  matching of sheet shapes to guide names) · `items/2911/outside/diagnosis.tsv`.
- Machiavelli's copy on V/139 (printed in Opere VI, 1877, pp. 54–55 n. 1) is an abridgement of the letter in
  V/140: 41.7% of the cipher tokens have no counterpart in it, in 20 interior stretches. `likely` · same file,
  `items/2911/outside/uncovered-print.tsv`; "covered" is a script's alignment, not a reader's judgement.
- The copy is loose as well as short. On the first page 1,265 of the print's 1,893 letters stand in blocks
  equal to the true decode; 714 decode letters have no print, in 68 blocks; with the true key held, a sign
  spells the print at its place 55% of the time. `established` · `items/2911/bench/spelling.py`,
  `items/2911/bench/runs/vx_beam_oracle-p1-miss1.0.log`.
- Two Opus readers agree on 90% of the sign tokens of V/140 at 300 dpi, and the true key values 99.5% of the
  tokens they read. `established` · `items/2911/results/agreement.tsv`, `outside/diagnosis.tsv`.
- Two Opus readers cannot transcribe Machiavelli's fast autograph: their consensus keeps 57% of the words.
  `established` · `items/2911/results/prep.tsv`.
- Passerini–Milanesi, Opere VI (1877) does not print the Dieci's letter of 17 August 1510 (V/134): the volume
  goes from 13 August to 18 August. Whether Bertelli 1964 or the Edizione Nazionale prints it was not checked.
  `established` for the 1877 volume · SCHOLARLY · archive.org `leoperediniccol03milagoog`, `items/2911/print/README.md`.

## Item 2911 bench (2026-11-17)

- Repeat seeding recovered correct *provisional* values: two starts in the
  shortlist agreed at every proposed value with the period table. The lock
  rule extended neither and the trial marked no values. `established` for
  this run and the period-table transcription ·
  `items/2911/bench/runs/v3_seed-p1-seed-audit.tsv`, `results.tsv`.
- The strongest blind run before the bench reopened (`v2_boot`) got 86 places right, all single
  letters, and 66 wrong. It recovered no syllables. `established` for the
  bench score · `items/2911/bench/runs/v2_boot-p1-errors.tsv`.
- The true-table start reached 0.960 precision and 0.601 recall on p1.
  `established` for that oracle diagnostic ·
  `items/2911/bench/runs/results.tsv`.

- Merging compatible repeat seeds recovered 105 syllable places and 101
  letter places on p1. It also got 152 places wrong. The best blind table
  scores 0.575 precision and 0.155 recall. Multi-sign extension added no
  values to its 15-value provisional start. `established` for this run ·
  `items/2911/bench/runs/results.tsv`, `v6_merge-p1-errors.tsv`, `v6_merge-p1.log`.

## Next candidates (2026-11-17)

- The Castaldo key is already published. Bourdeau's catalogue still listed
  1332 open during the refresh. `established` for the public records ·
  [PR 224](https://github.com/dbourdeau/cyphersolver/pull/224) and
  [issue 746](https://github.com/dbourdeau/cyphersolver/issues/746).
- Ambrosiana F 47 inf. no. 131 c. 269r has a cipher slip and an instruction
  to see the following folio. C. 270r is indexed as the decipherment.
  The related F 131 inf. c. 14r and F 49 inf. c. 44r have cipher passages.
  `established` for layout · PRIMARY ·
  `items/1336/gate.md`, `items/1336/PROVENANCE.md`.
  Their use of the same key is open.
- The memorandum F 46 inf. n. 275 c. 652r (1573, catalogued "N.D. a N.D.", no decipherment) is in the same
  cipher table as c. 269r and c. 44r. `likely` · a test registered before the decode: `key-v2.tsv` scores above
  200 of 200 shuffled tables on four readers' transcriptions · `items/1336/results/c652-test.tsv`,
  `items/1336/READING.md` section 4. One page, one test, 28 values.

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
