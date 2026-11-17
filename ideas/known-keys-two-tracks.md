# Known keys, two tracks — plan (2026-11-17)

**Status:** started 2026-11-16 as `puzzles/missing-keys-16c/`, with two changes: the census is dropped as a product
(Bourdeau's project already publishes one), and the goal is one recovered key. The network block applied to the
cloud session only; the hosts answer from Greg's machine.
**Prompted by:** Tomokiyo's Cryptiana page "French ciphers during the Reigns of Charles IX and Henry III"
(https://cryptiana.web.fc2.com/code/henryiii.htm, SECONDARY), the source of "Longlée's cipher" used in the
es. 132 Saint-Goard work. Greg asked whether it holds more to do. Answer: not as a solved/unsolved list (that is
`unsolved.htm`, already in the catalog as `french-royal-ciphers-1567-1610`), but as a census of working keys.

Two tracks, decided by Greg on 2026-11-17:

1. **New decipherments.** Only text nobody can already read. Outside solvers are clearing Cryptiana's unsolved list
   (`NEXT-SESSION.md`, field note 2026-11-10), so a reading counts only if it is new.
2. **What the keys tell us.** What the reconstructed keys show about how Spain, France and others enciphered,
   1560–1610, and where a key is still genuinely missing. Take a stab at recovering one.

Track 2 goes first: its gap list feeds Track 1's targets.

---

## What we already know (do not redo)

- **Saint-Goard's own dispatches are not new content.** Every cipher letter in fr. 16107 has a contemporary
  decipherment in the volume; the three 7 Feb 1580 "leftovers" are duplicates of 31 Jan
  (`puzzles/vargas-mexia-es132/analysis/13-feb7-letters/`). The 23 Dec 1579 letter's decipherment is at fr. 16106
  ff. 208–209. An ambassador's dispatches home were deciphered on arrival, and the sheet is usually bound beside them.
- **Why es. 132 was new:** it is Vargas's *captured* correspondence, held by France without a key. New content lives in
  intercepted or captured letters, private ciphers, and letters whose decipherment sheet is lost.
- **The novelty test** (Greg, 2026-10-18, `PLANS.md`): (a) no published reading; (b) no plaintext can exist by
  construction (no clear minute kept by the sender, no decipherment by the recipient); (c) we can reach the images.
- **A ranked list of known-key targets already exists:** `sources/screenshot-opportunities-2026-10-18.md`
  (15 rows: Mendoza in fr. 3641, Sancy, Baugy, Dodieu, Péricard, Sabran, Sega, Velada, Ungnad, Gondomar, …).
  Track 1 starts from it, not from scratch.
- **Key recovery from ciphertext alone is hard on nomenclators.** `puzzles/viete-f539/`: on ~344 tokens over ~145
  signs, the matched annealing control failed (0.093 vs 0.986 positive), and 50 seeded values or an 80-letter crib
  still left ~50% wrong. Any Track 2 recovery attempt must clear a control first.

---

## Track 2 — key census (first)

Home when started: `/focus nomenclator-census-16c` (proposed slug; a cross-puzzle study, so its README says it has
no single catalog entry).

### What a result would have to do (written before any analysis)
- Cover every published reconstructed key in scope, not a convenient subset, and say which were left out and why.
- Record each key's features from the key itself (image or table), not from a page's prose summary.
- Make every comparative claim ("Spain used more homophones than France after 1580") come from `census.py` over
  `census.tsv`, with counts and the number of keys behind each figure (rule 6).
- Separate *what a power used* from *what survives and was reconstructed*: the census measures the second. Say so.
- For the gap list: name the correspondent, the dates, the shelfmark, the amount of ciphertext, and why no key is
  known (none published, or none recoverable), each with a source.

### Scope
Keys reconstructed or printed for diplomatic and political correspondence, c. 1555–1615: France, Spain, the Papacy,
Venice, the Empire, England, Savoy, the League. Extend the dates only if a power has fewer than ~5 keys in range.

### Sources to sweep
- Cryptiana pages (filenames known from repo references; fetch the site index for the full list): `henryiii.htm`,
  `spanish3.htm`, `spanish3D.htm`, `antwerp.htm`, `vatican.htm`, `unsolved.htm`, `louisxiii.htm`, `mayenne.htm`,
  `GL.htm`, the League page, the Francis I-era page; Cryptiana blog posts of 2026 (Danzay key; French numerical
  ciphers of the 1570s).
- Devos 1950 (Spanish keys, Cp.nn numbering); keys already transcribed in
  `puzzles/vargas-mexia-es132/sources/keys/` (Ciphers 1–4, Cp.30 Borja variant) and the Papal 1628 key.
- DECODE key records (de-crypt.org) for the same powers and dates.
- Lasry et al. papers (Mary Stuart 2023; Henri IV–Brèves 2021) and Mousset 1912 (Longlée).
- Bourdeau's catalogue/notes where they transcribe keys (cited in `screenshot-opportunities`).

### Data model: `analysis/01-census/census.tsv`, one row per key
`key_id, power, user_from, user_to, date_first, date_last, source_url, tier, reconstructed_or_original,
alphabet_size, homophones_per_vowel, homophones_per_consonant, nulls, syllabary (none/partial/full), syllable_form
(digits/letters/symbols), code_words_count, code_form, diacritic_vowel_marks (y/n), doubling_sign, symbol_type
(digits/letters/glyphs/mixed), shared_with (other key_ids), letters_known_using_it, notes`

### Analyses (`census.py`)
- **Q1, practice by power and decade:** feature distributions per power per decade; which features co-occur (e.g.
  the Spanish vowel-diacritic style of Cp.30 vs French homophonic nomenclators).
- **Q2, lineage and reuse:** keys shared across embassies or reissued (Cp.30 was used by Vargas, Mendoza and Borja);
  how long a key stayed in service; whether compromise (a known interception) was followed by a change.
- **Q3, gaps — "keys still needed":** for each correspondent pair with surviving cipher letters, is there a known key?
  Output `gaps.tsv`: `pair, dates, shelfmarks, est_cipher_tokens, same_key_letters, has_decipherments_nearby,
  novelty_test (a/b/c), source`. Rank by same-key ciphertext volume and by whether glossed letters exist (glossed
  siblings make a key recoverable without cryptanalysis, as with Sancy and Velada).

### "Take a stab": one key recovery
1. Pick the top gap where same-key ciphertext is largest and no glossed sibling exists.
2. **Calibrate first (rule 7):** run the same method on a known key of the same type and similar token count
   (candidates: Cp.30 from es. 132; Longlée from fr. 16106–16107, where we have decipherments as ground truth).
   Set the pass bar before running: e.g. ≥80% of tokens correct on the held-out control.
3. Only if the control passes, run the target. If not, record the wall (minimum tokens needed) in `NEXT.md`.

---

## Track 1 — new decipherments

Home when started: `/focus intercepted-ciphers-1560-1620` (proposed slug).

### What a reading would have to do (written before any reading)
- Pass the novelty test (a)(b)(c) **before** reading, with the checks written down per candidate.
- Use a key that is established for that correspondent and date (from the census), or one recovered in Track 2 that
  passed its control.
- Two independent readers per letter, as in es. 132 exp 10/13; agreement reported by script; disagreements listed.
- Coherent across the whole letter, not one passage: names, dates and events check against outside sources.
- A duplicate test on the *cipher content*, not the clear opening or the date (lesson of exp 13).

### Where to look (in order)
1. Rows of `sources/screenshot-opportunities-2026-10-18.md` that pass (b) as captured or intercepted material:
   Mendoza in fr. 3641 (check Simancas K for clear minutes first), Velada (Morgan), Gondomar (RB), the 1716–18
   intercepts.
2. Census Q2/Q3 output: any key whose users' letters sit in an *enemy's* archive (French intercepts of Spanish,
   Spanish of French, League letters seized by the Crown).
3. Orphans: cipher letters whose decipherment sheet is lost (the fr. 16107 orphan sheet of 6 Dec 1580 is the reverse
   case and shows they exist).

### Gate per candidate (`candidates.tsv`)
`shelfmark, folios, sender, recipient, date, key_id, captured_or_intercepted (y/n, source), recipient_decipherment
searched (where), sender_clear_minute searched (where), DECODE checked, Cryptiana checked, other solvers checked
(Bourdeau, Lasry, Ryabov), images reachable (viewer), est_tokens, verdict`. Read only rows with verdict `pass`.

---

## Order of work (first session with network)

1. Fetch the Cryptiana index and `henryiii.htm`; cache under `sources/cache/` (gitignored). Record each fetch in
   PROVENANCE. Two or three verification fetches per key, aimed at the features the census records.
2. Open Track 2 with `/focus`; fill `census.tsv` from the keys already in the repo plus `henryiii.htm` and
   `spanish3*.htm`; write `census.py` and a first `gaps.tsv`.
3. Fan out if needed: one Opus agent per power (France, Spain, Papacy/Italy, Empire/England/other), each writing rows
   only, no sub-agents (AGENTS.md "Subagents"). Synthesis stays on the main thread.
4. From `gaps.tsv` plus `screenshot-opportunities`, fill `candidates.tsv`; open Track 1 when one candidate passes.
5. Close with `/session-close`.

## Environment

The Default environment allows no outside hosts; on 2026-11-17 the session could not add any (the environments
service rejected both a new environment and an edit). Greg to add, under Allowed domains:
`cryptiana.web.fc2.com`, `cryptiana.blogspot.com`, `gallica.bnf.fr`, `archivesetmanuscrits.bnf.fr`, `archive.org`,
`web.archive.org`, `de-crypt.org`. Gallica serves the Playwright browser, not scripts (es. 132 exp 10); full-size
pages may still need Greg's screenshots.

## Open decisions (Greg)
- Slugs and the Track-2-first order.
- Priority against the es. 132 essay review (parked research since 2026-11-11).
- Whether the census should go past 1610 (Baugy, Sabran, Velada are 1616–1641).

## Unverified claims
- The full set of Cryptiana key pages: only the filenames cited in this repo are known; the site index was not
  fetched on 2026-11-17 (host blocked). The 2026 blog posts (Danzay; French numerical ciphers) are known from a search
  snippet only.
- That the henryiii page quotes no deciphered passages: recorded by the 2026-11-10 session
  (`puzzles/vargas-mexia-es132/sources/saint-goard-prior-publication-2026-11-10.md` §5), not re-checked.
