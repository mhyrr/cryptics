# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` /
`disputed`), and a source pointer.

## The object
- BnF Espagnol 132 is on Gallica, `ark:/12148/btv1b10032556x`. It has 288 canvases, each an
  open spread, unlabelled. Canvas c shows f. (c + 3) on the right page, at least for canvases
  195–250. `established`: images checked 2026-10-03 (`sources/PROVENANCE.md`).
- F. 198r is canvas 195 right, f. 198v is canvas 196 left, and f. 199r is canvas 196 right.
  The letter ends "de Madrid a 15 de Abril 1579" and is signed "Ant. Perez". `established`:
  image.
- F. 198–199 mixes clear Spanish and cipher within lines. A clear header reads "Ill.e señor".
  `established`: image.

## The text
- Tomokiyo's Cipher 4 key, plus the signs 2H = que and H = ne, reads f. 198–199 (Pérez, 15 April 1579),
  f. 87r–v (Pérez, 13 Sept 1578) and f. 123r (Philip II, 20 Oct 1578) as continuous Spanish that
  joins the clear text. `established` for the key; `likely` for the reading (Sonnet transcriptions,
  no reconciled human transcription). `analysis/01-decode-f198/`, `analysis/02-key-extensions/`.
- Independent check: the cipher on f. 87r l. 12 decodes "don alonso de sotomayor", and f. 88r names
  Don Alonso de Sotomayor in clear. `established`.
- Pérez's letter of 15 April 1579, in cipher, says the King refused him leave to retire, and that
  the Archbishop of Toledo had the Princess of Éboli urge him to stay. `likely`: reading v1,
  `analysis/02-key-extensions/reading-f198-v1.md`.

- f. 105 (13 Oct 1578, Cipher 3) is Antonio Pérez's letter to Vargas, not the King's: it speaks of "la carta de
  [Su Magestad]" and "la discreción de [V.m.]" and is signed Antº Pérez. `likely` (two blind readers).
- ff. 103 and 113 are independent encipherments of one royal letter of 13 Oct 1578 about Mos de la Mota, governor of
  Gravelines: 300 escudos a month, an encomienda, a Spanish letter sent through Alonso de Curiel with the French one.
  `likely`; it agrees with the companion letters to Mota (ff. 107, 111) and Curiel (f. 109) listed in the volume.
- f. 154 (King, 4 Dec 1578) orders Vargas to find out, secretly, about Guise's cipher "con mi hermano", the
  Guise–Lorraine "unión" and "los 800 mill ducados", and whether Don John received part of them. `likely` (one reader,
  held-out decode).

## Context (external)
- Pérez sought the secretaryship left vacant by Diego de Vargas (Mediterranean/Italian affairs), with the
  support of the Marqués de los Vélez and Archbishop Quiroga; the office was split, Zayas taking a share.
  `likely`: es.wikipedia "Antonio Pérez del Hierro" (SECONDARY, fetch summary 2026-10-04; it dates the vacancy
  "1568", which conflicts with Quiroga's appointment in 1577 and a RAH snippet giving Diego de Vargas's death
  as 26 Sept 1576). Our f. 198 cipher independently names "el Marqués de los Vélez [y] Quiroga" in this
  matter and says the King would "desmembrar y repartir" "el oficio de Vargas" (reading v1). See H5.
- In April 1579 Pérez complained that the King avoided giving him audience and begged him to stop the
  Escobedo family's prosecution; the King cited Easter devotions. `likely`: Mignet 1846 footnote (SCHOLARLY,
  archive.org `antonioperezetph00mign`, text read 2026-10-04). Pérez asked leave to retire and the King refused:
  Pérez, *Relaciones* (CLAIMANT) via Mignet and Lafuente. `sources/history-2026-10-04.md` §2.5, §12.
- No source read so far describes Quiroga urging Pérez to stay through Éboli in 1579. Our f. 198 reading is
  the only witness. `established` as a negative search result, not as a fact about 1579.

## Keys
- The volume uses four ciphers. Cipher 4 ("Vargas Mexia's Cipher 4", September 1578 – April
  1579) covers f. 123 and f. 198. Its letters are the numbers 1–23. Marks attached to a number
  add a vowel: dot after = -a, + = -e, dot below = -i, "6" after = -o, dot above = -u, caret =
  null?. Capitals stand for consonant clusters, and a few short codes for words. Devos (1950),
  p. 422, reconstructed it from Vargas Mexía's letter of 16 May 1579; Tomokiyo added "a" = u,
  "v" = o, and conjectured some clusters. `likely`: Tomokiyo, Cryptiana spanish3D.htm (SECONDARY,
  last modified 16 Jan 2026), key image in `sources/cache/cryptiana/`.

- Cipher 4 extensions that passed held-out tests (2026-10-04, ff. 87, 154, 157, 179): 2H = que (83/84), Σ = o
  (37/38), H = ne (14/16), and Devos's rule that a cross above doubles the letter (36/36). `established` for the
  values; `analysis/05-cipher4-v2/tally-judged.md`. 21. = que holds only on f. 198 (`disputed`).
- Cipher 3 reads as Spanish under Tomokiyo's Cp.30 table once the vowel marks are tokenized as in
  `sources/transcription/CIPHER3-GUIDE.md` (the -i curl is a joined 6, the -o hook a "p", the -u T-bar a "u"), with
  "u." = que. `likely`: ff. 103, 105, 113, 165, 167 decode; calibration 68% syllable-exact against Tomokiyo on f. 83.

## Prior scholarship: settled points
- Ochoa (1844), *Catálogo razonado de los manuscritos españoles … Biblioteca Real de Paris*,
  pp. 220–224, no. 9999 (= es. 132): 290 folios; many letters "en cifra … imposible descifrar
  no teniendo la clave"; the cipher appears "precisamente cuando se va á hablar de materias
  delicadas". He summarizes clear letters only and has no entry for the letter of 15 April 1579.
  `established`: archive.org `CatalogoRazonadoDeLosManuscritos`, djvu text (SECONDARY), fetched 2026-10-03.
- Rubino (2012), "The Secrets of Antonio Pérez Decoded", OSU honors thesis supervised by Geoffrey
  Parker (kb.osu.edu/handle/1811/51582, SCHOLARLY-student; PDF supplied by Greg 2026-10-04):
  transcribes the clear text of eight Pérez letters (ff. 66, 87, 105, 136, 148, 157, 179, 198) and
  marks every cipher passage "[CIFRA]". Her only decoding is one word, "adelante", in f. 257 (1580),
  found by comparison with a plaintext. Her f. 198 summary: Pérez cleared up the rumours "mostly in
  code". `established`.
- Rubino's clear-text transcription of f. 198 agrees with ours at every clear/cipher join. Her gaps
  are where our decoded runs fall. `established` (comparison by reading).
- No full decipherment of es. 132 is published. Tomokiyo reads only words of f. 198 ("le Marques
  de los Velez", "Escovedo", "mi inocencia", "falso testimonio") and a preliminary f. 3. `likely`:
  Tomokiyo (as above). Not checked: Parker, *Imprudent King* (2014), which may use these letters.
- Bourdeau's repository (324 target folders, checked 2026-10-03) has no es. 132 target. `established`:
  GitHub API listing of `dbourdeau/cyphersolver/targets`.
