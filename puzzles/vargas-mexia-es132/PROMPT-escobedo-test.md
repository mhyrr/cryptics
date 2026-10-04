# Session prompt: test Pérez's "Guise confederation" claim with the pre-murder cipher letters

Paste everything below the line into a fresh session (`/focus vargas-mexia-es132` first, or as the session goal).

---

/focus vargas-mexia-es132

Goal: test, with ciphered letters nobody has read, one plank of the Escobedo mystery: whether Philip II had reports
of a Don John–Guise understanding **before** Juan de Escobedo was murdered (31 March 1578), as Antonio Pérez later
claimed, or only after, as Mignet (1846) argued.

## Read first, in order
1. `puzzles/vargas-mexia-es132/NEXT.md`, `README.md`, `canon.md`, `hypotheses.md`. Search `research.md`, don't read it whole.
2. `OVERVIEW.md` §7 "The letters and the Escobedo murder" (the argument this session tests).
3. `sources/escobedo-letters-survey-2026-10-04.md` (the source survey: which letters exist, where, in what cipher,
   whether images are online or decipherments are printed). **Start from its "Readable now" list.**
4. `sources/transcription/CIPHER3-GUIDE.md` (the Cipher 3 transcription guide; shapes only) and
   `sources/keys/README.md` (all four keys and their uncertainties).
5. Mignet's full text is cached at `sources/cache/mignet1846.txt` (pp. 68–73 the claim and rebuttal; p. 120 n. 2
   the King's April 1579 note; appendix E).

## The question, stated so it can fail
Pérez (via Mignet pp. 68–69) named, among the facts that decided the King on Escobedo's death, a secret
confederation of Don John and the Guises "sous le titre de défense des deux couronnes", denounced by Vargas Mexía.
Mignet (pp. 71–73): Vargas was named in Oct 1577 and reached Paris on **10 Dec 1577**; his reports on Don John and
Guise are "presque toutes postérieures au meurtre". Our f. 154 (4 Dec 1578, Cipher 4) shows the King still asking
Vargas for "el fundamento" of Guise's cipher with Don John and the 800,000 ducats.

**Window:** 10 Dec 1577 – 31 Mar 1578. Write this in `hypotheses.md` as H16 before reading anything:
- H16a (Pérez): a letter in the window (Vargas → King, or King → Vargas) reports or asks about a Don John–Guise
  league, pact, "unión", or joint designs on England/Scotland. 
- H16b (Mignet): the window's letters do not; such reports begin after 31 March 1578.
State the test: every letter in the window that we can image is transcribed and decoded in full; H16a is supported by
one clear passage (quoted with token positions, criterion 5), weakened if all window letters are read and none has it.
A partial read supports nothing. Name the letters that could not be read (the wall).

## Letters already in hand (BnF Espagnol 132, Gallica `ark:/12148/btv1b10032556x`; canvas c = f. (c+3) recto on the right page; verify folio numbers)
All are Philip II → Vargas, i.e. what the King asked Vargas in the window:
| Folio | Date | Cipher | Key status |
|---|---|---|---|
| f. 3 | 16 Dec 1577 | Cipher 1 | Devos p. 418 + Tomokiyo; partial table (`keys/cipher1.tsv`); Tomokiyo published a preliminary decipherment on Academia.edu |
| f. 11 | 24 Jan 1578 | Cipher 2 | Tomokiyo cracked it fully (`keys/cipher2.tsv`: 2 = a … 23 = z, vowel marks) |
| ff. 17 / 22 | 8 Mar 1578 | Cipher 2 | duplicates: each checks the other |
| f. 26 (+ dup) | Mar 1578 | Cipher 2 | |
| f. 34 | 16 Mar 1578 | Cipher 2 | |
| f. 32 | 17 Mar 1578 | Cipher 3 | readable with the guide; codes in `analysis/04-cipher3/c3_extensions.tsv` |
Also check the survey for Vargas → King letters in the window (Simancas Estado K; Teulet vol. 5; Devos used Vargas's
letter of 12 Dec 1577 for Cipher 1) and whether any are imaged or printed with contemporary decipherments.

## Method (as in sessions 1–3; do not cut corners)
1. **New experiment folder** `analysis/06-premurder/` with a README pre-registering H16, the letters, the readers and
   the pass/fail rule. Commit before any transcription.
2. **Decoders first, frozen by commit before any transcription exists:**
   - Cipher 2: write `decode_c2.py` from `keys/cipher2.tsv` and Tomokiyo's stated conventions (his page, cached at
     `sources/cache/cryptiana/spanish3D.htm`: marks + = e, e/ρ-like = a, underdot = i, overdot = o, dot to the right =
     u, overbar = null?; numbers 2–23; letter-forms f/n/p for clusters cr/pr/tr; open problem "6 with diacritics").
     Calibrate it on Tomokiyo's own partial transcription of f. 11v (printed on his page) before reading anything new.
   - Cipher 1: write `decode_c1.py` from `keys/cipher1.tsv` (syllable numbers 6–100, glyph letters, marks). Flag every
     gap; Devos's conflicting values (12 a, 21 e, 31 u) are reported, never chosen silently.
   - Cipher 3: reuse `analysis/04-cipher3/decode_c3_v2.py` unchanged.
3. **Transcription guides for Ciphers 1 and 2**, shapes only, written from Tomokiyo's images and examples (as
   `CIPHER3-GUIDE.md` was for Cipher 3). Calibrate each with one blind reader on a passage Tomokiyo has read and score it
   by script (as `analysis/04-cipher3/calibrate.py` did: 68% for Cipher 3).
4. **Two blind readers per letter** (Sonnet 5.5 subagents; Opus if Greg prefers; tell them not to spawn agents). Readers see
   only the guide and the images: never keys, decodes, other readers, or this prompt's hypotheses. Crops via Gallica IIIF
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b10032556x/f{canvas}/{x},{y},{w},{h}/full/0/native.jpg`, python urllib with a
   User-Agent (shell curl is blocked), no upscaling past 100%. Commit each transcription before decoding.
5. **Reconcile** with `analysis/05-cipher4-v2/align.py` and a blind reconciler per letter (sees both transcriptions, the
   diff list and the images; never a decode). Watch for notation collapse (in session 3 a reconciler merged the digit 1 with
   the virgula). Commit v2 before decoding.
6. **Decode, then read.** Syllables from code; word division and translation are interpretation and are labelled so. Every
   claim about Guise/Don John is quoted with token positions and both readers' readings (criterion 5).
7. **Duplicates** (ff. 17/22, f. 26 and its duplicate) are independent encipherments: align them to check readings and to
   value codes, as ff. 103/113 did for "particulares".
8. **Synthesis stays on the main thread**: what the letters say about Don John, Guise, England, Scotland, "las dos coronas",
   Escobedo. Then judge H16 against the pre-registered rule. File as you go: canon / research / hypotheses.

## What would solve or move the mystery, honestly
- This tests one plank (the Guise confederation as a pre-murder fact), not who ordered the murder or why.
- If H16a is supported, Pérez's reasons-of-state account gains a documented basis that Mignet denied.
- If H16b holds across every window letter, the "confederation" was assembled after the fact, strengthening the view
  that the state-reason justification came later.
- Either way, write it into `OVERVIEW.md` §7 and republish the Artifact
  (`python3 overview-build/build.py OVERVIEW.md overview-build/template.html <out>.html`, then publish to
  https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2 by passing its URL).

## Walls to expect and name
Simancas originals not imaged on PARES (needs Greg or a visit); Cipher 1's incomplete table; single-reader limits;
a contemporary decipherment in print would override ours (use it and say so).

## Rules
AGENTS.md throughout: source and tier everything; training data is not a source; say "contested"; freeze before testing;
commit transcriptions before decoding; statistics from scripts in `analysis/`; stop at a clean wall and name it;
`/session-close` at the end.
