You are a research scout for item 2351 of the dive `puzzles/missing-keys-16c` in `/Users/mhyrr/work/cryptics`.
Do not spawn agents. Read `CLAUDE.md` (rules 1, 2, 3, 8), then
`puzzles/missing-keys-16c/items/2351/gate.md` and `puzzles/missing-keys-16c/items/2351/SIGN-GUIDE.md`.

**Goal.** Find any published cipher key (a table of signs and their values) that could belong to the cipher
Roberto Acciaiuoli, Florentine ambassador in France, used in his letters from Amiens of 23 October 1513
(Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 190–192), or to a cipher of
the same family. Save what you find in a form a script can test. You do not test it and you do not try to
read the letters.

**What the cipher looks like** (from our own count; shapes are in SIGN-GUIDE.md): base signs that are small
letters, figures and capitals; five small marks written above a base (tiny figures 1, 3, 4, 5 and a tilde);
sixteen bases take those marks (7 3 8 y t x r s q z 6 2 4 S 5 and one more), the other signs never do.
About 124 distinct signs in 1,100.

**Leads, in order.**
1. Our gate file says: "The neighboring Pandolfini correspondence has a published table with a similar sign
   style." Find where that table is published and get it. Start with D. Bourdeau's `cyphersolver` repository
   on GitHub (PR 531 and its `research/` folders, the catalogue entry for no. 2351 at
   `https://dbourdeau.github.io/cyphersolver/solve/2351.html`), then S. Tomokiyo's Cryptiana pages on
   Florentine and Italian ciphers of 1490–1530 (cryptiana.web.fc2.com), then the DECODE database's public
   pages.
2. Florentine chancery ciphers of 1500–1515 for ambassadors in France: Francesco Pandolfini, Niccolò
   Machiavelli's legations, Roberto Acciaiuoli, Francesco Vettori. Printed keys or reconstructions in
   Desjardins and Canestrini, *Négociations diplomatiques de la France avec la Toscane* (vol. 2 OCR is at
   `puzzles/missing-keys-16c/items/2351/cache/print/negociations-v2_djvu.txt`), Meister's *Die
   Geheimschrift im Dienste der päpstlichen Kurie* and *Die Anfänge der modernen diplomatischen
   Geheimschrift*, and any article on Florentine "cifre" with superscript figures.
3. Any description of how this family works: what a figure written above a sign means.

**Write** in `puzzles/missing-keys-16c/items/2351/sources/`:
- `tables.md`: for each table found, the source with URL and tier (PRIMARY, SCHOLARLY, SECONDARY, CLAIMANT,
  POPULAR), who it belonged to and when, how it is said to work, and how close its signs look to ours.
  What you looked for and did not find goes under `## Not found`. What you could not verify goes under
  `## Unverified claims`.
- For each table you can transcribe, `table-<short-name>.tsv` with columns `sign<TAB>value<TAB>note`, the
  sign described in the vocabulary of SIGN-GUIDE.md where it fits (base, `^mark`), in plain words where it
  does not. If the table is only an image, save the image beside it and say so.

**Limits.** Web search and fetch only; no login, no purchase, no message to anyone. Direct `curl` downloads
are blocked here: use Python `urllib` or the fetch tool. Touch no file outside `items/2351/sources/`. Stop
when the three leads are exhausted or after about 25 fetches, whichever is first, and say which.

**Final message:** what you found in five lines or fewer, the files written, and the one lead most worth
following next.
