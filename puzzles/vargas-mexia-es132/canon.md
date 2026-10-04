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

## Keys
- The volume uses four ciphers. Cipher 4 ("Vargas Mexia's Cipher 4", September 1578 – April
  1579) covers f. 123 and f. 198. Its letters are the numbers 1–23. Marks attached to a number
  add a vowel: dot after = -a, + = -e, dot below = -i, "6" after = -o, dot above = -u, caret =
  null?. Capitals stand for consonant clusters, and a few short codes for words. Devos (1950),
  p. 422, reconstructed it from Vargas Mexía's letter of 16 May 1579; Tomokiyo added "a" = u,
  "v" = o, and conjectured some clusters. `likely`: Tomokiyo, Cryptiana spanish3D.htm (SECONDARY,
  last modified 16 Jan 2026), key image in `sources/cache/cryptiana/`.

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
