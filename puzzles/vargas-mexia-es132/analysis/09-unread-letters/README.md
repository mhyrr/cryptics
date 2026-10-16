# 09 — First readings of es. 132 letters nobody has read

**Opened 2026-10-16.** Goal: new decipherments, not verification.

## Which letters are unread
Tomokiyo's table of contents (cryptiana `spanish3D.htm`, cached) lists the Cipher 3 royal letters. Subtracting every
letter read by cabinet-noir (30 letters; repository unchanged since 2026-10-02, tree listed 2026-10-16), pangoleen
(ff. 26r, 87, 157, 179, 273–274; its later work is on other volumes) and this dive leaves these **unread** letters:

| Folios | Date (Tomokiyo) | Images on disk |
|---|---|---|
| 37, 39 | Madrid, 15–16 Apr 1578 (two weeks after Escobedo's murder), countersigned Çayas | no (thumbs only) |
| 41 | Madrid, 29 Apr 1578 | no |
| 50, 54, 62 | Bosque de Segovia, 7 and 14 Jun 1578 | no |
| 79, 85 | El Pardo 4 Aug; 10 Sep 1578 | no |
| 89 / 93 (dup) | Madrid, 19 Sep 1578 | no |
| 119 | Madrid, 15 Oct 1578 | no |
| 129 / 132 (dup) | Madrid, 1 Nov 1578 | no |
| 150 | Madrid, 30 Nov 1578 | no |
| 171 / 174 (dup) | El Pardo, 23 Jan 1579 (f. 169 is a clear decipherment of a letter of 22 Jan) | no |
| 181, 185 | El Pardo 7 Feb; Madrid 18 Mar 1579 | no |
| **202** | **Aranjuez, 17 May 1579, countersigned Çayas** | **yes** (`pages/exp07/`) |
| **213** | **San Lorenzo, 7 Jul 1579, countersigned Ant. Pz** | **yes** |
Also read by one reader only (ours): ff. 206, 208, 211.

"Unread" means: no published or repository decipherment found by us. Paz's summaries of Vargas's own letters
and Teulet's prints of Simancas minutes may cover some of the same matters; each reading is checked against them after
decoding, and any overlap is reported.

## Run 1: ff. 202 and 213 (pre-registered)
- Guide `CIPHER3-GUIDE.md` **v2.3** (adds the letter-form h, letter-group codes, marks on code signs; from exp 08),
  decoder `../04-cipher3/decode_c3_v2.py --v22`, extensions `../04-cipher3/c3_extensions.tsv`, all frozen in the commit
  that adds this README. Exp 08 code candidates are **not** in the decoder (21⁺ failed, 6⁺ ambiguous); they are applied
  only as a labelled reading aid after decoding.
- Two blind Sonnet readers per letter (A forward, B reverse), prompt `reader-prompt.md` via `mkprompt.py`.
- Decode both; `../07-after-arrest/compare_decoded.py` for agreement; reading assembled where A and B agree, unknowns
  left as unknowns. Expected accuracy from exp 08: ~86% of decoded letters right, ~1/3 of text unread.
- What would count as new: the content of either letter, especially anything on Pérez, Éboli, Escobedo, the office
  "de Vargas", or why Çayas countersigns on 17 May.

## Run 2: ff. 37–38 (King to Vargas, Madrid, 15 Apr 1578; pre-registered 2026-10-16)
Images: Greg's browser screenshots (`../../sources/cache/gallica-manual/es132_f37*`, `es132_f38r_zoom.png`), staged
as passages P1–P5 in `../../sources/cache/f37-blind/`. Known lacuna: the right ends of the three cipher lines at the foot
of f. 37v (gutter). Same frozen guide v2.3, decoder and extensions as run 1. Two blind Sonnet readers (A forward,
B reverse), prompt `reader-prompt-f37.md` (image budget ~60 views, after the request-limit failure of f. 213 reader A).
Clear text read by me on the images: reply to Vargas's letters; Alençon; the Scots ambassador and Mary Stuart (Mendoza
told to help); visits to Lorraine and Madame Marguerite; Don Pedro de Toledo's passage; couriers and passports; the
birth of a son to the Queen on the night of Sunday 13 April (the future Philip III, b. 14 Apr 1578); a packet for Don
John "que importa mucho que llegue con brevedad y seguridad"; date "De Madrid a xv de Abril 1578", Yo el Rey, Çayas.

## Runs 3–4: f. 174 (King, El Pardo, 23 Jan 1579; duplicate of f. 171) and f. 181 (King, El Pardo, 7 Feb 1579)
Pre-registered 2026-10-16. Greg's screenshots in page (time) order, staged in `../../sources/cache/f174-blind/`,
`f181-blind/`. Same frozen guide v2.3, decoder and extensions. Two blind Sonnet readers each, prompt
`reader-prompt-shots.md` (overlap rule, image budget). f. 181 readers start after the f. 213 re-read, to stay under the
image request limit.

## f. 213 (7 Jul 1579): parked at a named wall (2026-10-16)
Four readers so far: A (images failed), B (no reverse pass), A2 (running at the time of writing), B2 (pass 2 partial;
budget ran out). B and B2 transcribe alike, but the decode reads only in stretches ("e lo que toca a la …", "he visto lo
que me escrivís", "la Reyna madre", "tratar con franceses"), even after normalising B2's hook mark written `e` to `p`
(`f213_B2_hooknorm.txt`, exploratory). **Wall:** heavy show-through from the opposite pages on ff. 213v–214r, which the
readers report line by line. **Breach:** a contrast-enhanced or show-through-subtracted image (subtract the mirrored
facing page), or a human reader of the original.

## Runs 5–6: f. 171 (original of the 23 Jan 1579 letter; f. 174 is its duplicate) and f. 185 (Madrid, 18 Mar 1579)
Pre-registered 2026-10-16. Greg's screenshots in time order. f. 171: 5 shots (shot 2 is a low-resolution spread), one
blind reader (a third independent witness of the 23 Jan letter after f. 174 A/B). f. 185: ff. 185–190, 21 overlapping
shots, bold ink with bleed-through; split into three sections of 7 shots (`f185a/b/c-blind`), two blind readers per
section; sections overlap at their edges and are joined by matching decoded text. Same frozen guide, decoder,
extensions, prompt `reader-prompt-shots.md`. At most four readers at once.

## Method addition: per-reader vowel-mark normalisation (`marknorm.py`, 2026-10-16)
Written after f. 174 A showed a consistent mark swap; frozen before f. 174 B and any f. 185 output. Tries the 120
permutations of the five mark vowels, scores each decode with a letter-trigram model built from the dive's clear
Spanish (excluding the file scored). **Controls passed** (`marknorm_controls.txt`): identity ranks 1/120 for f. 202 A,
f. 202 B, f. 37 A, f. 37 B. f. 174 A: best is o↔i (identity ranks 20/120), the swap seen by eye; normalised decode
`f174_A_norm.txt`. Limit: it does not fix base-sign misreadings (f. 174 A also writes 9 as "q"/"g"); it is not extended
to bases, to avoid fitting noise. A reader whose decode needs more than a mark permutation is a weak witness.
**Amendment (after f. 185a B, before f. 185a A reported):** a number followed by `e` is read as the hook `p` before
decoding (guide §2 lists "an e with a tail" under the hook). Controls re-run: identity still ranks 1 for the four
trusted readers (`marknorm_controls.txt`).

## Runs 7–13 (pre-registered 2026-10-16): ff. 119, 41, 89, 132, 54, 62, 85
Greg's screenshots, staged in `../../sources/cache/<folio>-blind/`; already-read letters in the same batch (ff. 44, 46,
58, 60, 81, 83; cabinet-noir) set aside as `gallica-manual/es132_f*_read_*`. Two blind readers per letter, prompt
`reader-prompt-shots.md`, same frozen guide/decoder/normaliser. Priority order as listed; at most four readers at once.

## Result
(pending)
