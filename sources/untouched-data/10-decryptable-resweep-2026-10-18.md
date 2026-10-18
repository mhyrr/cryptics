# 10: Re-sweep for targets a small team could actually decrypt (2026-10-18)

*Agent re-sweep, 2026-10-18. Inputs: `catalog/entries/*.md`, `catalog/EXCLUDED.md`, files 01–09 here,
`NEXT-SESSION.md` "Pick up next" item 3, and each `puzzles/*/NEXT.md`. Also Bourdeau's public `cyphersolver` repository
(cloned 18 Oct, last commit 14 Oct 2026). It turned out to be the decisive crowding check. About 12 web searches or fetches.
Ranked by verifier, then by the size of the generator space, then by reachability, then by crowding. Fame does not count.
No readings were attempted (rule 9).*

## Summary

1. **Ungnad 1576 (with Sinzendorff 1578)** is the most certain decryption on the list. The key is in hand (a single
   substitution alphabet with no homophones and about 50 code words). The wall is one order of scans from the Vienna
   archive (HHStA), about €100–160.
2. **The es. 132 unread letters** remain the cheapest new readings. The key is known, the method has already worked in
   this repo, and nobody else is working them. The cost is Greg's screenshot time.
3. **Velada/Morgan** and **Siena nos. 20+23** are the best uncrowded and crowded cases where the key can be found by
   checking a short list of candidates. In each, 12 deciphered sibling letters (Velada) or 42 keys filed with the
   letters (Siena) reduce key recovery to checking a short list.
4. **Armstrong 20 Feb 1808** is the one target with a stated generator. Madison wrote that its key was "concerted with
   another correspondent", which leaves about five candidate legation codes. Its first test can run from this
   container today.
5. **The Barb.lat.6960 papal dive should close as a calibration case.** Bourdeau confirmed on 20–21 Sept 2026 that
   Kiewning (1897) prints the letters and that the Biermann–Bosbach 1628 key reads all 28 apart from about 1,750 code
   groups. **Access:** only `raw.githubusercontent.com`, `git clone github.com`, `pypi.org` and
   `books.googleapis.com` (429) answered from here. Every archive host was refused.

## Access note

Every probe used `curl -m 15` on 2026-10-18. Where the table says "CONNECT 403", the agent proxy refused the tunnel and
curl printed `000`; `/__agentproxy/status` logged each refusal as `connect_rejected`. Hosts refused this way: gallica.bnf.fr (page and IIIF),
digi.vatlib.it, cryptiana.web.fc2.com, founders.archives.gov, catalog.archives.gov, archives.gov, loc.gov,
tile.loc.gov, themorgan.org, corsair.themorgan.org, bdh-rd.bne.es, jacar.archives.go.jp, de-crypt.org,
cryptoole.satoru.net, pares.mcu.es, searcharchives.bl.uk, luna.folger.edu, masshist.org, realbiblioteca, archive.org,
web.archive.org, hathitrust, gutenberg.org, en.wikipedia.org, oesta.gv.at, archivinformationssystem.at,
real-d.mtak.hu, sammlungen.ulb.uni-muenster.de, bibliotheques-numeriques.defense.gouv.fr, arcsi.fr, ecp.ep.liu.se,
dbourdeau.github.io, scienceblogs.de, findingaids.lib.umich.edu, zenodo, huggingface. WebFetch also failed (DNS
ENOTFOUND) for themorgan.org, cryptiana, hungaricana and the SHD library, so those facts rest on search snippets.
**Reachable:** `git clone https://github.com/dbourdeau/cyphersolver` (200), `raw.githubusercontent.com` (200),
`pypi.org` (200), `books.googleapis.com` (429, rate-limited but reachable), `s3.amazonaws.com` (403 from the bucket,
not the proxy). github.com web pages answered 403/400; git and raw work. Earlier sessions reached DigiVatLib and
Gallica screenshots, so the allowlist differs between sessions. Plan on Greg's browser for every image.

## Candidates

| # | Target | Verifier | Generator hypothesis + space | Data reachable (HTTP) | Crowding | First concrete step | CPU / human hours |
|---|---|---|---|---|---|---|---|
| 1 | **Ungnad → Maximilian II, 12 Mar 1576** (HHStA Türkei I 32-3 ff. 199–203); add **Sinzendorff → Rudolf II, 1578** (Türkei I 37-2 ff. 1–8) to the same order | Total: a key lookup yields continuous German | The key is Ungnad's own (DECODE R392, transcribed: a single substitution alphabet, 11 digraph signs, about 50 code words, no homophones). Space 1. Sinzendorff: 2 candidate keys (R392 and Breuner 1575, R1384) | Ciphertext: not digitized (ÖStA AIS has no scans); oesta.gv.at CONNECT 403. Key transcription in Bourdeau's repo via git: 200 | Bourdeau's team, blocked on the same wall since 23–24 Sept. Listed undeciphered by Láng 2015 | Email an ÖStA reproduction order for both ranges (about 26 scans at €6); offer Bourdeau shared images | CPU ≈ 0; human 2–4 h, plus 2–6 weeks waiting for the archive |
| 2 | **es. 132 unread royal letters** (ff. 39, 50, 79, 150, 177; f. 129 duplicates f. 132; f. 213 blocked by show-through) | Strong but not total: two blind readers plus duplicates, Paz summaries, Teulet minutes | Known keys (Cipher 3, Cp.30). Space 1 | Gallica CONNECT 403. Greg's screenshots work | Uncrowded: no es. 132 entry in Bourdeau's catalogue; cabinet-noir and Tomokiyo have stopped | Greg screenshots ff. 39–50; run the frozen exp-09 protocol | CPU ≈ 0; 0.5–1 M tokens per letter; about 1 h of Greg per letter |
| 3 | **Philip IV → Velada, 1636–41** (Morgan; 35 letters, 23 "not deciphered") | Strong to total: pairs from the 12 deciphered letters predict the held-out 23 | Key recovered by aligning the deciphered letters. Philip IV's numeric ciphers are nomenclators of a few hundred to a thousand groups. Space: one key per period, if the chancery kept it | themorgan.org and Corsair CONNECT 403. Whether images exist is unknown | Open: not in Bourdeau, nothing published found | Greg asks Morgan reading-room services for images of both records (130074, 130090) and whether the "deciphered" 12 carry interlinear text | CPU < 1 h; human 5–15 h once images arrive |
| 4 | **Siena, Concistoro 2308 nos. 20+23** (about 4,900 tokens; also nos. 7, 11, 17, 19, 21) | Total: 4,900 tokens is far above unicity | 42 keys filed in the same busta (DECODE R4746–R4789); about 10 transcribed in Bourdeau's repo. Space 42, plus a nomenclator or syllabic layer | Transcriptions: git 200. Key images: de-crypt.org CONNECT 403 (needs a DECODE login with image rights) | **Crowded and active:** Lasry read nos. 6 and 24 with key R4755 on 14 Oct 2026; Bourdeau found no key for nos. 20+23 | Ask Bourdeau which of the 42 keys were checked against nos. 20+23; transcribe the rest; score each mechanically | CPU minutes; human 10–20 h of key transcription |
| 5 | **Armstrong → Madison, 20 Feb 1808** (369 groups, values 1–1900, 35 symbol passages) | Total: continuous English across 369 groups, opening from the clear "The" | Madison, 15 May 1808: "No such Cypher is in the office, and must be one concerted with another correspondent." Candidates: Pinkney/Monroe (London), Erving (Pinckney's legation code, partly rebuilt by Bourdeau), Livingston, Bowdoin. About 5 codes × the 19.6 M-setting transform family already coded | Ciphertext and both rebuilt code tables in Bourdeau's repo: git 200. Founders CONNECT 403 | Moderate: Bourdeau and a Codex search excluded only the THE=972 and WE028 codes. AFIO 2025 claim rejected by Tomokiyo and Bourdeau | Run `feb20_known_code_search` with the Pinckney code table from `targets/erving1807`, **from this container** | 1–4 CPU-h on 4 cores; human 2–4 h |
| 6 | **Sega / Baudouin-Desportes / Mauclerc, 1593** (BnF fr. 3984 ff. 186, 189; fr. 3985 no. 7) | Total once glyphs are read: Tomokiyo's League polyphonic key | Key known. Space 1. The wall is glyph accuracy: 75–79% now, more than 90% needed | Gallica CONNECT 403; screenshots. 1,100 aligned training glyphs (f. 188v) in Bourdeau's repo: git 200 | Bourdeau attempted (17 Sept), not read | Apply the es. 132 two-blind-reader protocol to f. 189 (33 lines); score against Bourdeau's held-out glyphs first | CPU ≈ 0; about 1–2 M tokens; 2 h Greg |
| 7 | **Ferdinand the Catholic nos. 93, 94** (BnF Espagnol 318) | Total if the key fits | The *Gran cifra* of 1501–04 (Bergenroth's reconstruction, BNE MSS 20.211/52), suggested by the range of code initials. Space 1 | BNE CONNECT 403. Not served online. Letters on Gallica (403; screenshots) | Bourdeau in progress | Order a BNE reproduction of MSS 20.211/52 | CPU ≈ 0; human 5 h plus the order |
| 8 | **Berthier → Napoleon, 22 Dec 1812** | Strong: a two-part code aligned with a candidate clear text (Chuquet 1912, letter XXIII, from the same carton AF/IV/1643) | The plaintext probably exists in print. Space: about 2 candidate letters of 22 Dec | Only 7 lines (Cryptiana) to 22 lines (Bourdeau) of ciphertext. Full text only in Vilcoq, *RHA* 1969/4 pp. 22–27. SHD library CONNECT 403 | Bourdeau stopped at the same wall | Greg searches bibliotheques-numeriques.defense.gouv.fr for *RHA* 1969 no. 4 (other volumes are there) | CPU < 1 h; human 3–6 h |
| 9 | **Barb.lat.6960** (papal dive) | Total: Kiewning 1897 prints the decipherments | 1628 key (Biermann–Bosbach, DECODE R215) reads all 28 letters | DigiVatLib CONNECT 403 today (reached on 16 Oct) | **Done by others** (Bourdeau, 20–21 Sept 2026) | Record H2 as answered by Bourdeau's catalogue 237. Optional H3: the code-group residue as a calibration corpus | CPU ≈ 0; 1 h to close the dive |
| 10 | **Marie de Médicis → Brèves, 1610** (fr. 3789) | Total, if the key photo is legible | Henri IV–Brèves key, BnF fr. 3642 (Desenclos; DECODE R2077). Space 1 | fr. 3642 is not on Gallica; the DECODE photo is 833 px and partial | Bourdeau attempted, closed | Ask Lasry for the R2077 plaintext, or order fr. 3642 images | Short (about 100 signs); 2–4 h |
| 11 | **Lüderitz consul's telegram, 9 Oct 1911** (43 five-figure groups) | Strong: a codebook plus additive yields English | A British FO or consular code or a printed commercial code with an additive. Space: dozens of codebooks × additive | archive.org CONNECT 403 | Low (Cipherbrain 2016, Cryptoole open) | Find which 1911 British consular code was issued; check whether TNA holds it | Unknown |
| 12 | *Reference:* **Blume telegrams, 1937** | Total (bigram fitness of the plaintext) | It becomes enumerable only if K2 comes from a stated source (a dossier phrase or the 2020 report). The dossier list is about 10⁴–10⁵ phrases × 2-swap neighbourhoods; Bourdeau already ran 6.6 M dictionary phrases | Data in repo | Bourdeau plus this repo | `puzzles/blume-salamanca-1937/NEXT.md` item 3 | Hours per list |

**Set aside, with the reason.** Each of these was checked against Bourdeau's notes or the entry.
- Kryptos K4: the plaintext is sealed until 2075.
- Beale: a book-cipher scan over Gutenberg came back negative, and a fabrication argument is published.
- Oberrhein Enigma: only the middle-ring gap is left, it costs 26 times more, and Bourdeau has it open.
- Sun Yat-sen 文密: Bourdeau searched about 200k condenser tables, and the condenser is probably a table.
- SP 53/16 nos. 78 and 79: images are paywalled, and the neighbouring keys fail.
- D'Estaing 1779: needs the AAE copy.
- Viète f. 539: the short-text wall.
- Florence 1414: the letters are not located.
- Esterházy 1744 and Durán 1718: the filed keys do not reach the high code values.
- Dresden Serpent Series (item 3): arithmetic, but not a decryption, and not checked in this pass.

## Top five

### 1. Ungnad 1576 and Sinzendorff 1578: a key in hand, text not yet photographed
**What a solution must do.** Read all five folios of German with one key, so that every code word resolves. It should
also agree with Gerlach's *Tage-Buch* for March 1576.
- The key (R392) has no homophones and no nulls, so if it fits, reading is a lookup. If it does not fit, five folios
  of a single-substitution cipher are long enough to break from ciphertext alone.
- Of the targets here, this has the best chance of ending in a complete decryption.
- The risk is that the 1576 letter uses a different key. The earlier Ungnad–Rym letters are in Latin. For
  Sinzendorff, R1384 is the second candidate.
- On crowding, coordinate rather than race. Bourdeau's team has the key transcribed and is blocked on the same scans.

Sources:
- Bourdeau, `targets/ungnad1576/NOTES.md` and CATALOGUE entries 342–343 (SECONDARY, repo work by others): https://github.com/dbourdeau/cyphersolver
- Láng 2015 repertory, C.Ung.03 and C.Sin.03, "megfejtetlen" (SCHOLARLY, as quoted by Bourdeau): https://real-d.mtak.hu/922/7/dc_758_13_doktori_mu.pdf
- ÖStA reproduction prices and order form (PRIMARY institutional; snippet only): https://www.statearchives.gv.at/dam/jcr:8df8339c-ece3-44cd-a62a-eda3d72228c8/Repro_english_version_update20.12.2023.pdf
- Interception of the April 1576 letters and Ungnad's use of simple substitution (POPULAR, academic author): https://blog.oup.com/?p=133141

### 2. es. 132 unread letters: proven pipeline, nobody else working
**What a solution must do.** Two blind readers must agree, the reading must match Paz's summaries where they exist, and
any duplicate copy must read the same.
- Exp 09 read six folios in one day.
- What remains is ff. 39, 50, 79, 150 and 177. F. 169 has a clear-text decipherment, and f. 213 is parked behind the
  show-through wall.
- Bourdeau's catalogue does not mention es. 132 or Vargas Mexía, so the readings would be new as far as the
  recorded search goes.
- The limit is the verifier. Calibrated on Borja, recall was 63%, so a reading is new but not exact.

Sources:
- `puzzles/vargas-mexia-es132/NEXT.md` and `analysis/09-unread-letters/` (PRIMARY, repo work)
- `09-review-2026-10-16.md` §09#1 (repo)
- Bourdeau CATALOGUE.md and SOLVED_CATALOGUE.md, no es. 132 match on grep, 18 Oct (SECONDARY): https://github.com/dbourdeau/cyphersolver

### 3. Philip IV to Velada (Morgan): key recoverable from the 12 deciphered siblings
**What a solution must do.**
- Rebuild the key from pairs in the deciphered letters only.
- Predict held-out deciphered passages before touching the 23.
- Read the 23 as continuous Spanish that fits 1636–41 events (the Downs, 1639).

The catalogue's own wording ("23 of the letters are not deciphered") was reconfirmed by search on 18 Oct. Nothing
newer was found, and Bourdeau's catalogue has no Velada entry. Two things are unknown: whether images exist, and
whether the "deciphered" letters carry the decipherment beside the cipher (which a crib requires) or only a separate
summary.

Sources:
- Morgan catalogue records (PRIMARY; snippet only, fetch failed): https://www.themorgan.org/literary-historical/130074 and https://www.themorgan.org/literary-historical/130090
- Related Morgan record, Malvezzi 1640 (PRIMARY, snippet): https://www.themorgan.org/literary-historical/130097

### 4. Siena nos. 20+23: 4,900 tokens against 42 keys filed in the same busta
**What a solution must do.** One filed key, or a variant, reads nos. 20+23 as continuous Italian or Latin. No. 20
opens "Sacra Regia Maiestas", so the reading must also fit a letter addressed to a king.
- Ciphertext-only fitness stays at −2.9 per token under every variant Bourdeau tried. That points to a syllabic or
  code layer, which a filed key would supply.
- Generator space: 42 keys. Only about 10 are transcribed in Bourdeau's `keys/` (R4750, R4753, R4754, R4756, R4757,
  R4762, R4764, plus three rebuilt).
- Crowding: Lasry (with Claude and ChatGPT Astra) matched nos. 6 and 24 to R4755 on 14 Oct. Ask before working.

Sources:
- Bourdeau, `targets/siena1421/NOTES.md` and `targets/siena1431/NOTES.md` (SECONDARY): https://github.com/dbourdeau/cyphersolver
- ASSi Concistoro inventory 1952 (PRIMARY finding aid): https://dgagaeta.cultura.gov.it/public/uploads/documents/PAS/5b27904b5c1ff.pdf
- Yale Ilardi reel of the Siena *Lettere cifrate* (PRIMARY, catalogue): https://doi.org/10.60600/YU/QDOHXM

### 5. Armstrong 20 Feb 1808: a generator stated by the recipient
**What a solution must do.**
- Render all 369 groups, including the frequent groups 17, 18, 38, 1 and 14.
- Account for the 35 symbol passages.
- Continue the clear "The".
- Agree with a second letter in the same code, or with the key.

The hypothesis follows from Madison's sentence: the code was concerted with another correspondent, so it is one of the
other legations' codes.
- Bourdeau's repo holds the Pinckney legation code, partly rebuilt from Erving 1807 (1651 the, 133 of, 1343 and).
- It also holds a C++ search over 19.6 M transforms that was run only against THE=972 and WE028.
- The first step needs nothing from an archive.
- The digit bias Bourdeau found (groups of 100 or more end in 0 in 39% of cases and in 1 in 20%) is a second clue to
  how the code was generated. A table that hands out numbers in steps of 10 would leave that trace.
- The AFIO 2025 solution is a CLAIMANT reading. Under Bourdeau's adjudication script it uses 30% of its own mapped
  occurrences, against 41% for a shuffled control.

Sources:
- Bourdeau, `targets/armstrong/NOTES.md`, the `feb20_known_code_search/` files and `targets/erving1807/NOTES.md` (SECONDARY): https://github.com/dbourdeau/cyphersolver
- Founders Online transcription (PRIMARY, via search; direct fetch 403): https://founders.archives.gov/documents/Madison/99-01-02-2728
- AFIO announcement (CLAIMANT): https://www.afio.com/member-news/2025/05/27/we-have-a-winner-in-the-armstrong-madison-encrypted-letter-contest/
- Madison to Jefferson, 15 May 1808, "concerted with another correspondent" (PRIMARY, as quoted by Bourdeau from Founders 99-01-02-3082; not opened here)

## Unverified claims

- That HHStA Türkei I 32-3 ff. 199–203 and 37-2 ff. 1–8 are still undigitized. This rests on Bourdeau's 23–24 Sept
  check; ÖStA could not be reached from here. Current ÖStA scan prices were seen only in search snippets.
- That the Velada letters have no published reading, and whether images exist. Only search snippets of the Morgan
  records were seen.
- That *Revue historique de l'armée* 1969 no. 4 is in the SHD digital library. Other volumes (1970) are there; this
  issue was not found.
- That the Pinckney/Erving code has never been tested against 20 Feb 1808. This is inferred from the absence of such a
  test in Bourdeau's notes.
- Which of the 42 Siena keys have been checked against nos. 20+23.
- Bourdeau's and Lasry's results are repo notes by others (SECONDARY). None was independently re-run here.
- The es. 132 unread list follows `puzzles/vargas-mexia-es132/NEXT.md` (2026-10-16), which differs from 09-review's
  eleven-letter list. NEXT.md is the later source.
- The hour estimates are judgements, not measurements.
