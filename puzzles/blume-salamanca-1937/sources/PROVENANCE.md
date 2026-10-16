# Provenance

One line per file in this folder: filename, origin URL or citation, date
fetched, and what (if anything) was changed from the original.

Primary object: Swiss Federal Archives (BAR), **E4320B#1974/47#277***, *Spanische Revolution (Passvisas etc.)*,
1936–1938, Aktenzeichen C.08-01.03; subdossier 0000066, unit **Unterlagen_0000072** (14 canvases).
Collection manifest: `https://www.recherche.bar.admin.ch/recherche/files/manifests/0000/0357/8609/3578609.json`
(the host `recherche.bar.admin.ch` without `www.` refused connections on 2026-10-16, so the URL in the brief
fails as written; the `www.` host serves the same paths).
Unit manifest: `https://www.recherche.bar.admin.ch/recherche/files/manifests/0000/0357/8609/Subdossier_0000066/Unterlagen_0000072/_0SdRie66XgUmMsGvKtNEaQ.json`
(SHA-256 of the manifest as fetched: `ab125a91dfa32113bf4fc35fda53198a95b79348c1b43812ed3ade4222770a19`).
Image URLs follow the pattern
`https://image.recherche.bar.admin.ch/iiif/2/0000%2F0357%2F8609%2FSubdossier_0000066%2FUnterlagen_0000072%2F000005NN.jpg/full/full/0/default.jpg`,
with NN = 18 + canvas number (canvas 9 → 00000527, canvas 13 → 00000531). Bourdeau's "canvases 9 and 13 of
Unterlagen 0000072" is correct.

| File | Origin | Fetched | Changes |
|---|---|---|---|
| `telegram-1.txt` | Read by us from BAR canvas 9 (`images/…_c09.jpg`), PRIMARY | 2026-10-16 | Transcription. 123 groups, 8 per line as on the form (16 lines), uppercase, address words BLUME SALAMANCA and the struck "(VIA VIGOEMDENKABEL)" omitted, pencilled (50) and (100) omitted |
| `telegram-2.txt` | Read by us from BAR canvas 13 (`images/…_c13.jpg`), PRIMARY | 2026-10-16 | Transcription. 32 groups, 5 per line as on the form (7 lines), uppercase, address words omitted |
| `headers.md` | Our reading of BAR canvases 1, 9–14, and the BAR OCR of Dokument_0000069 | 2026-10-16 | Written by us |
| `images/bar-E4320B-1974-47-277_sub66_unterlagen72_c01.jpg` | BAR canvas 1 (00000519), full size 1807 × 2533. PTT covering letter, 15 Jan 1937 | 2026-10-16 | None (byte copy) |
| `images/bar-E4320B-1974-47-277_sub66_unterlagen72_c09.jpg` | BAR canvas 9 (00000527), full size 2562 × 2346. Telegram 1, front | 2026-10-16 | None |
| `images/bar-E4320B-1974-47-277_sub66_unterlagen72_c11.jpg` | BAR canvas 11 (00000529), 2617 × 1807. Telegram 1 with the attached tissue folded back, showing the pencilled fee sums | 2026-10-16 | None |
| `images/bar-E4320B-1974-47-277_sub66_unterlagen72_c13.jpg` | BAR canvas 13 (00000531), 2540 × 1808. Telegram 2, front | 2026-10-16 | None |
| `images/bar-E4320B-1974-47-277_sub66_unterlagen72_c14.jpg` | BAR canvas 14 (00000532), 2544 × 1811. Telegram 2, reverse (pencilled fee sum) | 2026-10-16 | None |

## Hashes

SHA-256 of the files as committed, and of the bare letters (all groups joined, uppercase, no spaces or newlines):

| File | SHA-256 of file | groups / letters | SHA-256 of bare letters | matches the published hash? |
|---|---|---|---|---|
| `telegram-1.txt` | `335f069847b0a5e40d4943cfb1db2397815e3e819146770f8f2d54293f6d5776` | 123 / 615 | `e266615d92019276513c1b7656f10c4f1a3d1e8eb739d28fd481ae337a434c55` | **Yes**: Bean (issue 14) and Bourdeau (`ct1.txt` upper-cased) |
| `telegram-2.txt` | `a0e09d752f6a5f477da167ab1c8cbf0f8c12e427cfbbdbfab17aa88c660a0ca1` | 32 / 160 | `8fd5cfb82fc3c39fe0ee007b19ada7e74b4ae7747cd9b794d36dce101e17a644` | **Yes**: Bean (issue 14) and Bourdeau (`ct2.txt` upper-cased) |

| Image | SHA-256 |
|---|---|
| `…_c01.jpg` | `01b1d429f63285735b736daa7b0ee7889bd731001cacdb57016f9c656fac971b` |
| `…_c09.jpg` | `410d37a5644106efead1eb636229cb74d781e202dd82838a8fce5b196266be73` |
| `…_c11.jpg` | `327d83f906b84985c65eac13defdb72043ae73091bd3e0df483f1db5c7121453` |
| `…_c13.jpg` | `84002a17f2d703512fa277e94fc94dccc8ce0a0791044a2a71b39dd4d1cb9d85` |
| `…_c14.jpg` | `24f80f01cfb980a215389ffa5a7d876e31607dce8bc7a755ff6e13e0ec7994d3` |

Canvases of Unterlagen_0000072 not copied here (URL pattern above; SHA-256 of the full-size IIIF JPEG fetched
2026-10-16):

| Canvas | Content | SHA-256 |
|---|---|---|
| c02 | blank back of c01 | `d0a0e97e72965f61739700679b9d48babbba0f4483be92cbe97a617b02c88775` |
| c03 | Hunziker "Superbeton-Schleuder-Rohr" bomb drawing (photo card) | `502107a96362034201c79b9ba50a5e878df85836c2c062d3061a06cff3c38441` |
| c04 | back of photo card | `18588d02b4816f84c7df9aba66ab3c0af002321bb57f8decaf068f9add446950` |
| c05 | photo, test target "32 / 59 Durchschläge, 400 Gramm Sprengstoff" | `6c0aba7a3749ae0c78d28fcd8fd3488d089ff4a2c62f465db11828bb106ef322` |
| c06 | back of photo card | `1b0b2b7a379dbfbbe70c9ae0cc5ae970be8ad461914cd4890ee6d80a47a6f64e` |
| c07 | photo, Hunziker works | `d62827c0f2c7f0225b1f4634e28ea7e8dc9b6c1817b42b5423f27fc85dbfc2ed` |
| c08 | back of photo card | `2bdecb096a795e5187e765838fba24941359a632f6b7466871f99422ae62c736` |
| c10 | telegram 1, attached tissue half folded back | `53d26061e084c9118df722271ac3c72ed2dc4f1347ec9d487882ddd9c75e053f` |
| c12 | telegram 1, reverse | `7ae2fee101760deca0fd37761548021e881b22a3f4c9e626cb03c8c2873ddfe2` |

## Secondary copies (not stored here)

| Copy | Origin | Fetched | Tier | Note |
|---|---|---|---|---|
| `telegram1.jpg` (1134 × 1012, SHA-256 `fe25852aa1c7998d88d78646bad5e8997365f20af8d1084b2140e12ead519ba1`) | `https://github.com/dbourdeau/cyphersolver/tree/main/targets/blume`, from Klaus Schmeh's Facebook post | 2026-10-16 | SECONDARY (photograph of the same form) | Same object as BAR c09, lower resolution |
| `telegram2.jpg` (2048 × 1376, SHA-256 `a2fc356b404cf9670e60239ba8380e1ac975295e59b5cc0a854074b58299bde1`) | same repo; from the Facebook image server via Bean, issue 14 | 2026-10-16 | SECONDARY | Same object as BAR c13 |
| `ct1.txt` (SHA-256 of file `d442e136d63bfc066c20374e2b454ca5581b164e940b307d5600d0d463df943e`), `ct2.txt` (`d2cdadbefb0bef2fbcdcf83bf6de1b104583e166f14f0a3d2b545024b3188df0`) | same repo | 2026-10-16 | CLAIMANT (his transcription) | Lowercase, no spaces; upper-cased they give the two hashes above |
| Schmeh's full image | `https://scontent.fsyd3-2.fna.fbcdn.net/v/t39.30808-6/495053957_23955786440685923_6316138309898944488_n.jpg?…&oe=6AC34D95` (full URL in issue 14) | tried once 2026-10-16 | POPULAR | **Dead**: HTTP 403 "URL signature expired" |
| Issue 14 | `https://github.com/dbourdeau/cyphersolver/issues/14` (Richard Bean) | 2026-10-16 | CLAIMANT | Source of the two published hashes |
| Dossier OCR | `https://www.recherche.bar.admin.ch/recherche/files/ocr/0000/0357/8609/OCR-Text-komplett.zip` | 2026-10-16 | PRIMARY (machine OCR of the archive images) | Used only to search the dossier, see `headers.md` |
