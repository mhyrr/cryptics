# Gate: catalogue no. 2192 (AGI Indiferente 737 N.171, Tierra Firme 1554)

Scout: Opus stage 0, 2026-11-16. Proposed verdict at the end; the main thread decides.

**Proposed verdict: `skip: race lost`.** The item is already being worked in Bourdeau's repository by another
contributor (WAINUT), with letter 1's key rebuilt from the Panama 29 clear copy, a held-out test run, and letter 2
attempted. The site page for 2192 shows it as "in progress".

## 1. Race: FAILS

- Bourdeau's repo has a target directory `targets/sosa1554/`, added in commit `cbd93dbe` (2026-11-12T06:33Z,
  "WAINUT sosa1554 (new): Álvaro de Sosa to the officials at Seville, Nombre de Dios, 4 July 1554 (catalogue 2192,
  letter 1 of AGI ...") and merged in `a0e37b77` (2026-11-12T12:24Z, "Integrate WAINUT PRs #461, #473, #469, #468").
  Evidence: https://github.com/dbourdeau/cyphersolver/tree/HEAD/targets/sosa1554 and
  https://raw.githubusercontent.com/dbourdeau/cyphersolver/HEAD/targets/sosa1554/NOTES.md (POPULAR/CLAIMANT tier:
  a contributor's working notes).
- Contents (file names only, from the git tree): `key.tsv`, `key_draft.tsv`, `key_frozen.tsv`,
  `clear_panama29_R6_N23.txt`, `transcription_ind737_letter1*.txt`, `decryption_ind737_letter1.txt`,
  `reading_ind737_letter1.md`, `translation_ind737_letter1.md`, `scripts/em.py` (alignment), and
  `work/letter2_attempt/`.
- State per its NOTES.md: letter 1 "decoded, not read"; held out 447/587 = 76.1% letters against the copy; letter 2
  "attempt on the heading only"; letters 3-5 "not started". Status "in progress (not written up)".
- Site: https://cyphersolver.com/solve/2192.html (repo `docs/solve/2192.html`, rebuilt 2026-11-17) labels it
  "class A · priority 6.5 · in progress". (https://dbourdeau.github.io/cyphersolver/ now 301-redirects to
  https://cyphersolver.com/.)
- Open PRs (30 listed via GitHub API, `pulls?state=open`), last 50 closed PRs and last 100 issues: no mention of
  2192 / Sosa / Tierra Firme / Indiferente / Panama. The work came in through the merged PRs named above.
- Our cached catalogue `sources/cache/bourdeau-catalogue-2026-11-16b.json` does **not** show this: entry 2192 has
  no `reserved`, `writeup` or progress field and its vetting (4 Nov) says "open"; the string `sosa1554` does not occur
  in the file. The "in progress" state lives in `targets/` and the generated site, not in `catalogue.json`.
- Tomokiyo: fetched and grepped `unsolved.htm`, `spanish.htm`, `spanish2.htm`, `spanish2A/2B/2C.htm`, `spanish3.htm`,
  `spanish3D.htm`, `GL.htm` at https://cryptiana.web.fc2.com/code/ for Sosa, Tierra Firme, Panam-, Indiferente,
  Indias: no hit. Only a bibliography line for Lohmann Villena 1954 (spanish2.htm, spanish3.htm).
- DECODE: not checked by me (JS app). The 4 Nov vetting and WAINUT's 12 Nov notes both say not on DECODE; unverified
  by this scout.

## 2. The pair is real: yes, by others' evidence (not re-checked by me)

- PARES description of Indiferente 737 N.171 (quoted in the catalogue entry): "El texto descifrado de la primera
  carta se halla en el legajo Panama,29,R.6,N.23" ("the deciphered text of the first letter is in bundle Panama 29
  R.6 N.23"). The Panama record carries the reverse note "el texto cifrado de esta carta se encuentra en Ind. Gen.
  737 n 171" ("the cipher text of this letter is in Ind. Gen. 737 no. 171"), per the vetting.
- WAINUT's notes: Panama 29 images 1-2 carry the title "Copia de la carta que el gou[ernad]or de tierra firme
  escrivio a los officiales de Sevilla" ("Copy of the letter that the governor of Tierra Firme wrote to the officials
  of Seville"), the same four paragraphs as cipher letter 1, signed Alvaro de Sosa, "del nombre de dios a iiij de
  jullio de 1554" ("from Nombre de Dios, 4 July 1554"). Their key built on paragraphs 1-2 scores 76% on held-out
  paragraphs 3-4, which is strong evidence the pair is the same text.
- Form: **A1** (separate sheet, separate legajo). The vetting found no interlinear gloss on any of the 28 leaves.
- I did not view the images (see 3), so the layout comparison is not mine.

## 3. Images: not verified by me (PARES returned HTTP 429)

- Every request to `pares.cultura.gob.es` from this environment (description/300401, show/300401,
  description/381859; five requests in total, 2026-11-17 03:44-03:46 GMT) returned `429 Too Many Requests` with no
  `Retry-After`. I stopped rather than hammer it. Possibly other scouts are hitting PARES from the same address.
- Recipe as recorded by WAINUT (unverified here; NOTES.md "Documents"): open `catalogo/show/<id>` with a cookie
  jar, read the `(txt_id_imagen, dbCode)` pairs from it, then fetch
  `ViewImage.do?accion=42&txt_descarga=1&dbCode=<d>&txt_id_imagen=<n>&txt_zoom=10&...`, which returns an 864 px
  JPEG, "the largest size served"; dbCode alone returns image 1. The vetting saw 864x1240 px.
- Legibility at 864 px, per WAINUT: "dots above and below are often hard to see"; a blind reviewer agreed on about
  85% of base shapes. Since the system marks vowels with dots, that is a real limit.
- Nothing saved under `items/2192/cache/`.

## 4. Size (from others' counts; not measured by me)

- Letter 1 cipher (Indiferente 737 images 1-2): 41 lines, 1651 sign tokens (WAINUT `profile.json`, "measured").
  Well above the 150 bar.
- Clear copy: four paragraphs, about 1995 letters scored (1408 + 587 in their test).
- Bare letters 2-5: vetting estimate about 25 cipher pages, 12-25 lines each, 350-400 lines in all, not measured.
- Second cipher copy of letter 1 at Panama 29 images 8-9: not measured.

## 5. Period key

- None known online. Not on DECODE (vetting, WAINUT; unverified by me).
- Lohmann Villena, "Cifras y claves indianas", *Anuario de Estudios Americanos* XI (1954) p. 285 (citation from
  Tomokiyo's spanish2.htm): one web search found no text or table of contents; whether it prints a Tierra Firme /
  Sosa key is **unverified**. WAINUT's notes also list it as unchecked.

## Observations (from others' notes; I viewed no image)

- Sign system: Latin-looking letter signs, word gaps kept, marks above and below signs, clear words occasionally
  inside the cipher ("ausencia", image 19, per vetting); numbered slash-marked lines on images 17-25.
- Letter-to-image map (WAINUT + vetting): letter 1 = images 1-2 (docket 4); letter 2 = images 5-6, another hand,
  docket on 8 beginning "Relación de los navíos de la flota" ("Account of the ships of the fleet"); remaining
  letters on 9-11, 13-15 and 17-26; blanks 3, 7, 27; dockets 4, 8, 12, 16, 28.
- Letter 2 being a fleet list rather than a Sosa letter suggests Panama 29 R.6 N.22 / N.24 / N.25 are not
  necessarily its plaintext; not checked.

## Page inventory (from the vetting and WAINUT; not checked against images)

| image | letter | kind | lines |
|---|---|---|---|
| 1-2 | 1 | cipher | 41 total |
| 3 | - | blank | 0 |
| 4 | 1 | docket | short |
| 5-6 | 2 | cipher (second hand) | ? |
| 7 | - | blank | 0 |
| 8 | 2 | docket | short |
| 9-11 | 3? | cipher | ? |
| 12 | - | docket | short |
| 13-15 | 4? | cipher | ? |
| 16 | - | docket | short |
| 17-26 | 5? | cipher, numbered lines | ? |
| 27 | - | blank | 0 |
| 28 | - | docket | short |
| Panama 29 R.6 N.23: 1-2 | 1 | clear copy | 4 paragraphs |
| Panama 29 R.6 N.23: 5 | 1 | second clear copy | ? |
| Panama 29 R.6 N.23: 8-9 | 1 | second cipher copy | ? |

## Note for the line

`line/queue.py` keys on `reserved` and `writeup` in `catalogue.json` (line 52). Work in progress shows only as a
`targets/<slug>/` directory whose `profile.json` names the catalogue number, and as "in progress" on
`docs/solve/<id>.html`. The queue should also check those, or every item will need this manual check.

Contamination note: reading WAINUT's NOTES.md exposed this scout to a summary of their sign values for letter 1. I did
not open their key or transcription files.
