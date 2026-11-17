# Provenance

One line per file in this folder: filename, origin URL or citation, date
fetched, and what (if anything) was changed from the original.

| File | Origin | Fetched | Changes |
|---|---|---|---|
| `cache/bourdeau-catalogue.json` (gitignored; sha256 3f093d3291076c45…) | https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/catalogue.json | 2026-11-16 | none |
| `cache/SCMisc_50207.jpg` (gitignored) | https://cdm15999.contentdm.oclc.org/digital/iiif/SCMisc/50207/full/full/0/default.jpg — BYU Vault MSS 771 item 6 p. 1 | 2026-11-16 | none |
| `cache/SCMisc_53902.jpg` (gitignored) | same host, page 53902 — BYU Vault MSS 518 f. 3 item 2 p. 1 | 2026-11-16 | none |
| `cache/bourdeau-catalogue-2026-11-16b.json` (gitignored; sha256 3f093d3291076c45…, identical to the first pull) | same URL, second pull before the pilot gate | 2026-11-16 | none |
| `cache/lazarillo-wikisource.txt` (gitignored; sha256 637c95272664020c…) | es.wikisource API, `action=parse`, page "El Lazarillo de Tormes/Tratado primero" (1921 edition) | 2026-11-16 | HTML tags stripped, whitespace collapsed; plaintext for `analysis/02-calibration-synthetic` |

Cryptiana pages read this session are cached at the repo level, `sources/cache/cryptiana/` (gitignored):
`unsolved.htm` (sha256 d339ab9a…), `henryiii.htm` (2d90a1d1…), `spanish3.htm` (a56ad0de…), fetched 2026-11-16.
Bourdeau's site pages are in `sources/cache/solvers/`.
