# Research log — append-only, newest first

## Dead ends
Refuted hypotheses and closed approaches, each with the date and the entry
that killed it. Nothing here is deleted.

-

---

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
