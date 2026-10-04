# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

-

---

## 2026-10-04 (session 3, after close) — the letters and the Escobedo murder

- Greg asked what the letters add to the Wikipedia (= 1911 Britannica) account of Escobedo. Read Mignet's full text
  (archive.org `antonioperezetph00mign`, djvu text). Two findings, written into `OVERVIEW.md` §7 and canon:
  1. Mignet p. 120 n. 2 quotes the King's April 1579 note (Hague ms. f. 101): he will not stop the prosecution, since that
     would admit his part in the murder; "os aquieteis y sosegueis". The f. 198 cipher reports the same wish
     ("me sossiegue y esté quedo"). Our fact sheet had summarized this footnote without the admission or the wording.
  2. Mignet pp. 68–73: Pérez alleged a Don John–Guise confederation denounced by Vargas as a motive; Mignet, from Vargas's
     correspondence, says the information postdates the murder. f. 154 shows the King still inquiring in Dec 1578, through
     Pérez.
- Nothing in the letters bears on the poison attempts, the killers, or the Éboli affair.

## 2026-10-04 (session 3) — Cipher 3 tokenization, Cipher 4 second readers, reconciliation

- **Cipher 3 tokenization solved from Tomokiyo's aligned duplicates (ff. 81/83).** Native crops of f. 81
  (canvas 78) show the -i curl written like a joined 6 ("256" = vi, "316" = cri), the -o hook like "p",
  the -u T-bar like "u", and "u·" alone = que ("y lo que vos" = `28 15p u. 25p<bar>`). Only signs with a cross
  above are marked code words. Guide (`sources/transcription/CIPHER3-GUIDE.md`), decoder v2 and "u." = que
  frozen in `2b0fdfb` before any v2 reader started. H9, H10, H11 added.
- **Calibration (f. 83, one blind reader with the guide):** 38/56 = 68% of Tomokiyo's labelled syllables exact
  (`analysis/04-cipher3/calibration_f83.txt`). Misses are systematic: a z-shaped 2 read as "u" (5×) and
  dropped marks above. Guide addendum v2.1 sent to the four running readers (f. 105 A2/B2, ff. 103, 113).
- **Cipher 4, cross above doubles** (Devos's rule): v1 split "<cross above>" into junk tokens. Read as a
  mark, it gives aquella, intelligencia, allí, dello, succeso, aquellas, llegó on f. 123 B (7/7 in-sample).
  Decoder v2 frozen (`8fafd88`) before the v2 texts and before f. 154 (an untouched Cipher 4 letter of the
  King, 4 Dec 1578) was transcribed. H8.
- **f. 123: two blind readers agree closely** (`analysis/05-cipher4-v2/diffs_f123.txt`: 260 aligned, 40 blocks).
- **Rubino joins (v1, f. 157/179)** in `analysis/03-perez-corpus/rubino-joins.md`. Her text has 19 and 16
  [CIFRA] marks (not 13 and 8). f. 157: 9 gaps join both sides cleanly, 9 partly, 1 none; f. 179: 11–12 yes.
  External check: the f. 157 cipher reads "Mos de la Mota"; the volume holds royal letters of 13 Oct 1578 to
  M. de la Mota, governor of Gravelines (ff. 107, 111, Tomokiyo's TOC).
- **Cipher 3 readable (guide v2.1, decoder v2 unchanged).** f. 103 (Philip II, 13 Oct 1578; not used to build
  the guide) decodes as continuous Spanish: Mos de la Mota, the plaça de Gravelinas, "los dichos 300 escudos …
  al mes", "hasta que se le haga merced de una encomienda equivalente", a letter to Mota "en español" sent
  "por medio de Alonso de Curiel" with the French one. The volume itself holds the companion letters of that day
  (to M. de la Mota, ff. 107/111; to Alonso de Curiel, f. 109; Tomokiyo's TOC): criterion 6 met against the
  volume. f. 113 (its duplicate, enciphered independently) decodes to the same text.
- **f. 105 is Pérez's letter, not the King's.** Both v2 readers: "[149⁺] verá por la carta de [108⁺] lo que le
  escrive", "[108⁺] me ha mandado", "se remite a la discreción de [149⁺]"; signed Antº Pérez (A2, B2). Rubino's
  attribution stands; our 2026-10-04 "scope correction" (following Tomokiyo's TOC) was wrong. Codes 108⁺ = Su
  Magestad and 149⁺ = V.m. frozen (`739c8c1`) on A2 and then replicated by B2 (6× and 2×, same places). No
  held-out test is possible inside es. 132: Rubino marks no cipher in Pérez's other letters (ff. 66, 136).
- **A2/B2 agreement on f. 105:** 72% of decoded syllables (`analysis/04-cipher3/agree_f105.txt`).
- **"u." = que:** 40 occurrences on f. 103 and many on f. 105, all fitting (in-sample for those letters, but the
  value was frozen from Tomokiyo's f. 81 before either was read: a held-out pass).
- **Duplicate alignment values a code:** f. 103 "T.⁺" stands where f. 113 spells "particulares" (3×); f. 105 has
  the same T-shaped code 2× in fitting contexts. Frozen (`f97ea08`) before the held-out pair ff. 165/167.
- **35:** "plaça" (pl) on ff. 103/113, "pretensiones"/"primero" (pr) on ff. 103/105. Both values occur; H11 open.
- **Held-out Cipher 3 (ff. 165/167, duplicates of 10 Jan 1579, one reader each).** Both decode as Spanish in stretches
  (Don Alonso de Sotomayor, Mos de la Mota, "correo propio"). f. 165 spells "personas particulares" and "particular";
  f. 167 has cross-marked codes in both places ("[7⁺] [1⁺]", "en [1⁺]"): T⁺/1⁺ = particular(es) 2/2 consistent, n < 3.
  7⁺ = personas, one occurrence. 21⁺ (5× over ff. 113, 165) unvalued.
- **Cipher 4 v2 (exp 05).** Reconciled two-reader texts for ff. 87, 123, 157, 179, 198; held-out f. 154 (King, 4 Dec 1578)
  read whole. Held-out tally: 2H 83/84, Σ 37/38, cross-doubling 36/36, H 14/16 pass; 21. = que fails outside f. 198.
  f. 154: Lalaing and the Malcontents, Arras, Mota's envoy Andrés de Ayala, and a secret inquiry into Guise's cipher
  "con mi hermano" and "los 800 mill ducados" (H6 supported). f. 157: "Arcauti" (cf. royal letter to Pedro de Arcauti,
  f. 193). f. 179: "García de Arze" (v1 "Garnica"); the private-letter passage reads continuously (H7). f. 198: "ra" is a
  cipher sign, = "oficio" in 4 contexts (candidate). `analysis/05-cipher4-v2/`.
- **History** (`sources/history-2026-10-04.md`): Mignet (1846) dates to April 1579 Pérez's plea that the King
  stop the Escobedo family's suit, and the King's evasion; Lafuente has Pérez asking to retire and the King
  refusing. No source found for Quiroga's mediation through Éboli: our f. 198 reading is the only witness so far.

## 2026-10-04 — Pérez's letters and Cipher 3 (experiments 03, 04)

- Pre-registered experiment 03 (`f1e54bb`). Six Sonnet agents: readers for ff. 105 (A, B), 148, 157,
  179, and a Simancas search.
- f. 148: no cipher (Rubino agrees). f. 105: Philip II's letter in Cipher 3 (Tomokiyo), not Pérez's.
  Rubino's list misled the plan. Corrected in 03.
- Cipher 4 held-out test 3 (ff. 157, 179): 2H = que 11/14 (79%, just below the frozen bar; 24/27 over all
  held-out letters); the others are consistent but under 3 occurrences. Details in `analysis/03-perez-corpus/`.
- Decoder bug (Cipher 4 has no 13) fixed; earlier outputs unchanged.
- f. 157 links to f. 123: the King repeats the order to get papers "con el mayor recato". Parma is
  written to; "el manejo del dinero en los de ay" and a "correspondencia" are to cease. That is H6.
- f. 179: the private-letter passage behind Rubino's "damaging admission" is in cipher. That is H7.
- Cipher 3 (f. 105): the key is confirmed by Spanish fragments, but the text is not readable yet. Digit
  grouping differs between readers, and the codes are unvalued. `analysis/04-cipher3/`.
- Simancas (`sources/simancas-search-2026-10-04.md`): Paz, *Catálogo IV* (archive.org `catlogo4secret01spai`)
  puts Vargas Mexía's cipher originals "y algunas minutas de respuestas de Felipe II" in **K 1550–51**;
  the Apr–Jul 1579 correspondence with the King and Pérez in K 1554–55; Vargas's letters of Jul–Dec 1578
  in K 1545/1546/1549/1552–53 (K 1546 mentions Nazareth and Alençon). PARES item level and images are not
  checked (JavaScript site).

## 2026-10-04 — Rubino (2012) read

Greg supplied the PDF (`sources/cache/Senior_Honors_Thesis.pdf`, git-ignored; text via pdftotext).
- Rubino, supervised by Geoffrey Parker, transcribed the clear text of eight Pérez letters. Every
  cipher passage is "[CIFRA]" (f. 87 l. 12, where we decode "don alonso de sotomayor", is "[CIFRA]").
  She decoded one word ("adelante", f. 257). So the cipher of f. 198 was unread in her thesis.
- Her clear text matches ours at every join, and our decoded runs fill her gaps. That is a human
  paleographic check on our clear text and on the cipher boundaries.
- Corrections to v1: "al cabo se vio [mi inocencia]" (not "servio"); "vida sosegada y christiana".
  The postscript is Hernando de Escobar's.
- Her open question was whether this "tell-all" letter caused Vargas Mexía to cut Pérez from his
  will (1580). The cipher reads as a defence, not a confession.
- Not checked: Parker, *Imprudent King* (2014), for any later reading of these letters.

## 2026-10-03 — opening

**Why this target.** The viete-f539 dive showed that what decides a cipher is uses per sign, not
length (f. 539: 2.4; Marmont: about 8; f. 555: about 10). Filters for the next target: a lot of
same-key text, images we can fetch (Gallica, not DECODE), and outside Bourdeau's sweep. I first
recommended Clairambault 322, but the catalog entry itself calls that letter "short and
code-heavy", so it fails the first filter. Es. 132 passes all three, and its keys are published.

**Race check.** Bourdeau: no es. 132 folder among 324 targets (2026-10-03, GitHub API); his
CATALOGUE.md mentions only Francisco de Vargas 1552, which is a different man. Cryptiana spanish3D.htm,
last modified 16 Jan 2026: keys for all four ciphers, no full reading, f. 198 words only.

**Images.** Canvas c = f. (c + 3) recto. F. 198–199 = canvases 195 (R) and 196 (L, R).

**Dispatched (Sonnet 5.5).** A key agent (Tomokiyo's tables → `sources/keys/`); blind readers A and B
(f. 198–199 → `sources/transcription/`); a context agent (Rubino 2012, the 1844/1847 catalogues,
the Escobedo timeline, Devos 1950).

**Keys, decoder, readings.** The key agent's Cipher 4 file matches Tomokiyo's image. Decoder frozen
(`1f17a34`) before the transcriptions were opened. Readers A (748 tokens) and B (~755 tokens) frozen
(`1bd1c16`). Ochoa 1844 (archive.org) describes es. 132 as no. 9999: the cipher was "imposible
descifrar no teniendo la clave". No entry for 15 April 1579.

**Decode.** Tomokiyo's table reads both transcriptions as Spanish joining the clear text. Residues
traced to five signs. Every occurrence was listed (`analysis/02-key-extensions/kwic.txt`) and judged:
21. = que (19/19), 21_ = qui (~6/7), 2H = que (6/7, B), H = ne (4/4), Σ = o (9/9). A merges B's "2H"
(que) and "2+" (me) as "24+"; B's distinction resolves them. Extensions frozen (`11985aa`) for a
held-out test on Pérez's letter of 13 Sept 1578.

**Reading v1** (`analysis/02-key-extensions/reading-f198-v1.md`, provisional). The King had intended an
office "de Vargas" for Pérez, then changed his mind and split it. Pérez blames Escovedo's lawsuit,
which ended in his favour ("servió mi inocencia", "los flacos fundamentos"), and the "falso
testimonio". He asked leave to retire away from those who "me han procurado quitar la honra y la
vida". The King refused. The Archbishop of Toledo had the Princess of Éboli urge him to stay, under
oath that the King would regret his going.
