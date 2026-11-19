# Scout C: 2854, 1270, 2395 (2026-11-19)

Gating only, no readings. The rows are in `scout-C.tsv`. Images are in `sources/cache/cross/<id>/`, which is gitignored.

Tool note: `line/sign_height.py` crashes on JPEGs whose PGM conversion carries a comment line (`#unknown`), as the
DARA JPEGs do. I converted each page with `magick <jpg> -strip <png>` first and measured the PNG. The script itself
was not changed.

## 2854: Ferdinand to John II, Seville, 9 June 1478 (pass, conditional)

- **Page.** The DARA PDF comes from `https://opacaraimagenes.aragon.es/7a/9e/AHPZ_C_CRAR_000024.pdf`. The
  `dara.aragon.es/opac/app/attachment` link returns only an HTML viewer to a script. The PDF holds three images at
  160 ppi:
  - p.1 is 1671 x 2319, with "Senor muy excellente" and then about 30 lines of cipher.
  - p.2 is a 3440 x 2385 spread: about 32 more cipher lines on the left, and on the right 4 cipher lines, then the
    clear close, the Seville dateline of June 1478 (read by eye), and Ferdinand's autograph "Yo el Rey" with a
    secretary's signature.
  - Total by eye: about 66 lines x about 35 signs, roughly 2200 signs.
  - Sign height: `h_median` 30 px, box 1400,1800,150,230 on p.1. This is well above the 15 px floor.
- **Design, from crops.** One- and two-digit numerals (14, 28, 34, 49 ...) are mixed with letter-like signs (b, g, h,
  q, f, and a frequent "du") and signs carrying a superscript a or dots. This looks like a homophonic letter cipher
  with digit homophones or a nomenclator. Counts are still needed.
- **Pair.** None. A small hand has written about six letters over one word of p.1 line ~20. That is a gloss or a
  correction, not a decipherment.
- **What would change the verdict.**
  - Gate 4 rests on Tomokiyo 2018, "Ferdinand-John II of Aragon Cipher (1476-1479)"
    (https://www.academia.edu/37751652). Its text could not be read (403), so whether the key is printed in full, and
    whether it is this system, is not checked. If it is not, the item has no pair and fails.
  - The `ferdinand1473` keys (1473 and 1474) are earlier systems of a different design (by profile) and are a
    weaker hold.
- **Lead for the "what it adds" sentence.** De Francisco Olmos, *En la España Medieval* 18 (1995)
  (https://revistas.ucm.es/index.php/ELEM/article/download/ELEM9595110241A/23372), prints John II's two cipher
  letters to Ferdinand of 10 July and 11 August 1478 from clear copies in RAH Salazar A-7. The article says
  "las cartas estaban cifradas" ("the letters were ciphered"). It cites Zurita, *Anales*, book XX, ch. 22, for a
  summary.
  - Zurita collected the CRAR letters, so his *Anales* may also summarise this 9 June letter. That would be a loose
    paraphrase pair, not a true one. Not checked.
  - The RAH letters are the reply direction and may share the key. Whether their cipher originals survive is not
    checked.

## 1270: Juan Manuel, BNE MSS/20212/61/1-7 (fail at readable: access)

- **Page.** I could not get any page.
  - `bdh-rd.bne.es` (viewer and `pdf.raw`) and `bnedigital.bne.es` both answer 403 to the script.
  - The Chrome extension was not connected this session.
  - The Europeana IIIF manifest has only metadata and a thumbnail that points back to BNE.
- **What is known.** The 9 Nov 2026 vetting saw letter 1 only (Genoa, 10 Nov 1496): about 40 lines of a symbol
  cipher on one spread, with no decipherment. The dates of letters 2-7, and which of them are ciphered, remain
  unknown.
- **Prior art.** Tomokiyo's AlonsoSanchez.htm covers only the BRAH 9/23-24 letters of March-June 1522
  (R9499-R9529). It never mentions MSS/20212/61 or any Juan Manuel letter of 1496-1519, so the BNE letters are not
  taken as far as checked.
- **Neighbours, if images are got.**
  - For letters of about 1500-1510: the Cifra general de los Reyes Católicos (Galende Díaz 1994 app. 1, transcribed
    in the outside target `esp318`).
  - For 1520-22: Tomokiyo's 1522 Juan Manuel table.
- **Gate 1 is thin.** I found no source on a 1496 Genoa mission. The writer's Wikipedia page starts him as
  ambassador to England in 1499.
- **What would breach the wall.** A browser session on BNE Digital that saves the "high" PDF of each letter.

## 2395: Card. Giulio de' Medici to Galeotto de' Medici (fail at buildable)

- **Pages.** IIIF `full/max` gives 1272 x 1778 on both rectos (server maximum).
  - 734 (c. 742r) has 13 lines of large letter-like signs. `h_median` is 35 px.
  - 733 (c. 741r) has about 28 lines of small geometric signs with dots and bars above. `h_median` is 13.5 px at
    default settings, because the dots count as components. It is 21 px with `--minarea 30`. By the gate's default
    rule it is below the floor.
- **No gloss.** The faint cursive among 733's lower lines is mirrored show-through or offset (the left margin reads
  backwards), not a gloss.
- **Dateline.** 734 reads "xv Maij MDXXj", i.e. 15 May 1521. The DBI entry for Clemente VII has Giulio leaving for
  Florence on 28 Jan 1521 and returning on 30 April. A Florence letter of 15 May 1521 to Rome therefore needs
  checking against his itinerary; the year may be 1520.
- **Buildable fails.**
  - There is no pair.
  - The two letters use different ciphers, so neither has a second passage.
  - The Medici keys of the decade in outside targets (`corsi1513`, `pandolfini1514`) put a superscript vowel digit
    on consonant signs. That is not either design here.
  - Meister 1906 is on HathiTrust (US only) and was not seen. ASF Cifrari was not searched.
- **Side note.** 734, about 260 signs in a plain alphabet of about 20-25 signs, looks like a cheap ciphertext-only
  solve. That lies outside METHOD and is not a cross-section item.
