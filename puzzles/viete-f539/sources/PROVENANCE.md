# Provenance

One line per file in this folder: filename, origin URL or citation, date
fetched, and what (if anything) was changed from the original.

Images are git-ignored (`cache/`). Regenerate them from the URLs below; the
SHA-256 values in `IMAGES.sha256` identify the bitstreams used on 2026-10-01.

| File | Origin | Fetched | Changes |
|---|---|---|---|
| `cache/c544_full.jpg` | PRIMARY: BnF Cinq Cents de Colbert 33, Gallica `ark:/12148/btv1b10033958p`, canvas 544 (f. 539 right page, 539v/540 left), `https://gallica.bnf.fr/iiif/ark:/12148/btv1b10033958p/f544/full/full/0/native.jpg`, 7580 × 5347 | 2026-10-01 | None |
| `cache/c545_full.jpg` | PRIMARY: same, canvas 545 (verso; f. 540 blank) | 2026-10-01 | None |
| `cache/c561_full.jpg` | PRIMARY: same, canvas 561 | 2026-10-01 | None |
| `cache/c562_full.jpg` | PRIMARY: same, canvas 562 (f. 555r, the control), 7564 × 5347 | 2026-10-01 | None |
| `cache/c563_full.jpg` | PRIMARY: same, canvas 563 (f. 555v cipher lines; f. 556) | 2026-10-01 | None |
| `cache/f539_block_view.jpg` | Derived: IIIF region `3850,2150,2950,1350` of canvas 544 at width 1400 | 2026-10-01 | Crop and downscale by the IIIF server |
| `cache/bands/*.jpg` | Derived: IIIF regions of canvas 544 at native resolution; URLs in `cache/bands/REGIONS.tsv` | 2026-10-01 | Crop only |
| `cache/bourdeau/` | CLAIMANT/working notes: D. Bourdeau, `targets/joyeuse/` at commit `9226922ffb0663b1d9b95f4ef898d093efd74ef2`, `https://raw.githubusercontent.com/dbourdeau/cyphersolver/<commit>/targets/joyeuse/<file>` | 2026-10-01 | None. Kept out of git; used only for comparison after the blind readings were frozen. |
| `transcription/reader-A/`, `transcription/reader-B/` | Blind readings of `cache/bands/` and `cache/f539_block_view.jpg` by two isolated Sonnet 5.5 readers | 2026-10-01 | Raw readings; no merges applied |
| `breach-research-2026-10-01.md` | Research notes by a Sonnet 5.5 subagent: Lasry 2022, candidate archive material, published League keys, historical context. Each claim is tiered and URL'd in the file | 2026-10-01 | None; claims marked UNVERIFIED there stay unverified |
| `cache/lasry-histocrypt2022.pdf` | SCHOLARLY: Lasry, HistoCrypt 2022, https://ecp.ep.liu.se/index.php/histocrypt/article/download/402/360 | 2026-10-01 | None (git-ignored) |
| `tomokiyo.md` | SECONDARY: S. Tomokiyo, Cryptiana, "Ciphers Broken by François Viète", https://cryptiana.web.fc2.com/code/viete.htm (last modified 15 June 2022); text copied from the page by Greg | 2026-10-03 | Page text only; images and links dropped |
| `f394-summary-scan.md` | PRIMARY facsimile, read by a Sonnet 5.5 subagent: Colbert 33 ff. 394r–399v, "Sommaire du contenu en divers pacquets surpris sur ceux de la Ligue en Avril 1594" (canvases 399–405) | 2026-10-03 | Single-pass draft reading; not checked by a second reader |
| `joyeuse-siblings.md` | PRIMARY facsimile, read by a Sonnet 5.5 subagent: Joyeuse's clear letters ff. 544 (canvas 549R), 551 (557R, 559L), 553 (560R, 561L) | 2026-10-03 | Single-pass draft diplomatic transcription with [?] marks; not checked by a second reader |
