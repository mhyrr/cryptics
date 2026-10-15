# 05: Documents, archives, and text corpora

*Survey agent, 2026-10-15. Brief: `sources/untouched-data/BRIEF.md`. Survey only (Rule 9):
no discovery was attempted. **Search budget ran out** before every claim could be checked, and
**direct fetches of gallica.bnf.fr, cl.lingfil.uu.se (DECODE), pares.mcu.es, loc.gov,
tandfonline.com and revistas.um.es all failed** from this session (DNS failures in WebFetch,
proxy 403 from the container). Most facts below rest on search-result summaries of the cited
pages. Treat the scores as provisional. Each unchecked fact is listed under Unverified claims.*

## Summary: best bets

1. **Mis-catalogued cipher pages in digitized national-library manuscripts** (Gallica first). Mary Stuart's 57 letters sat in the BnF catalogue as "Italian matters". A page classifier, then a cross-check against DECODE, is cheap and feeds this repo's cipher dives directly. The verifier is mechanical: a key either yields readable French or Spanish or it does not.
2. **Triage of DECODE's "unsolved" records with automated solvers.** About 10,000 records are public. Crowding is rising (Stockholm's DescryptTool, Matthew Green's Decipher), but the long tail of single-letter nomenclators is still open, and this repo already holds several such records (R8623, R8624, R8447, R4886, R1579).
3. **Pre-instrumental earthquakes (and aurorae) in OCR'd newspapers.** A 2013 Adelaide thesis recovered 110 unrecognised South Australian earthquakes from Trove. Chronicling America (about 23.7M pages) has no equivalent sweep that this survey found. The verifier is clean: independent reports from several towns plus the existing catalogue.
4. **Anonymous plays and works in national-library manuscript fonds, found by HTR plus stylometry.** ETSO's *La francesa Laura* (BNE, 2023) is the template. Other languages' anonymous holdings look unswept.
5. **Cairo Genizah after MiDRASH.** About 400,000 fragments now have machine transcriptions, against fewer than 10% before. Text matching against known works can find identifications and joins. The field is crowded at the top, but a hobbyist now has the text to work with.

---

### 1. Mis-catalogued cipher documents in digitized manuscript collections (Gallica sweep)

- **Data:** BnF Gallica, which holds digitized manuscripts including the Cinq Cents de Colbert, fonds français and Dupuy. Images are served over IIIF (`https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<n>/full/<w>,/0/native.jpg`) with a manifest per volume, and an SRU search API exists. This repo's `viete-f539` dive already downloaded Colbert 33 over IIIF on 2026-10-01. Reuse is under the BnF's non-commercial conditions (Gallica *conditions d'utilisation*, not re-verified here). Other targets with IIIF: Vatican DigiVatLib, e-codices, BL Digitised Manuscripts, and Simancas via PARES (see #3).
- **Question / what a find looks like:** a page, or a block within a page, in cipher (symbol alphabets, digit groups, nomenclator code) whose catalogue record does not say "chiffre". The record either misdescribes it or does not describe it at all, and it is not in DECODE. A real find is such a page, deciphered with a solved or recovered key, and placed (author, date, recipient).
- **Gap evidence:** Lasry, Biermann and Tomokiyo found 57 letters of Mary Stuart (1578–84) in BnF holdings. The catalogue listed them as first-half-16th-century Italian material, and the letters were in fact in French ([ScienceDaily](https://sciencedaily.com/releases/2023/02/230207191551.htm), [Medievalists.net](https://www.medievalists.net/2024/02/codebreakers-crack-secrets-of-mary-queen-of-scots-lost-letters/)). That is a catalogue-level miss at the national library most studied by cipher historians. DECODE records are entered by researchers, so they cover what someone already noticed. One commenter estimates that about 1% of archival material is encrypted (POPULAR, uncheckable; see Unverified). No published page-level sweep of Gallica for cipher was found.
- **Verifier:** (a) a human glance confirms the page is cipher (cheap and fast); (b) the real test is decipherment into a known language, which is mechanical and self-checking; (c) plaintext copies or drafts elsewhere, such as the Walsingham papers for the Mary Stuart letters; (d) cipher historians (the DECODE/DECRYPT team, Lasry, Tomokiyo).
- **Precedent:** the Mary Stuart letters, above (Cryptologia 2023, SCHOLARLY, via POPULAR reports). Lasry's Bauffremont letter in Colbert 500/33 f. 555 is another BnF cipher solved by computer ([HistoCrypt paper](https://ecp.ep.liu.se/index.php/histocrypt/article/download/402/360), SCHOLARLY).
- **Recipe:** *Code* pages through SRU result sets for a fonds (for example, all Colbert volumes), pulls each folio at 400 px width, and caches it. A *vision model* labels each thumbnail cipher / mixed / clear on a fixed prompt. Before any sweep, *code* measures that labeller's precision and recall on a held-out labelled set: known DECODE/BnF cipher pages against random clear pages (Rule 6). *Code* then joins hits to the catalogue record and to DECODE shelfmarks and outputs "cipher page, not described as cipher, not in DECODE". The LLM then reads the clear context on each hit (salutation, date, signature) to propose a placement, which a human checks. Decipherment is a separate deep dive (`/focus`).
- **Cost:** about 100k thumbnails per large fonds. Vision labelling with a cheap model costs tens of dollars; downloading at a polite rate takes a day or two. No GPU.
- **Traps:** decorative or tabular pages (accounts, astrological tables, music, shorthand, Greek, Hebrew) read as "symbols". Pages already described in older printed catalogues (Omont) but not online. Ciphers whose keys are lost and whose text is too short (the `viete-f539` wall: 344 tokens did not break a homophonic cipher). Crank history: "codes" seen in ordinary secretary hand.
- **Crowding:** `PARTLY`. Lasry, Biermann and Tomokiyo have worked the BnF by hand, and DECRYPT catalogues it. No machine page sweep was found.
- **Ethics:** clear. Sixteenth- to eighteenth-century diplomatic correspondence; no living persons; nothing is looted by publishing a shelfmark. Respect Gallica's rate limits.
- **Scores:** `data_ready 4`, `gap 4`, `verifier 5`, `cheapness 4`, `payoff 4`, `ethics_clear 5`
- **Sources:** ScienceDaily 2023 (POPULAR) https://sciencedaily.com/releases/2023/02/230207191551.htm; Scientific American (POPULAR) https://www.scientificamerican.com/article/scientists-decipher-50-letters-from-mary-queen-of-scotts-before-her-beheading1/; Medievalists.net 2024 (POPULAR) https://www.medievalists.net/2024/02/codebreakers-crack-secrets-of-mary-queen-of-scots-lost-letters/; Lasry, Bauffremont letter, HistoCrypt (SCHOLARLY) https://ecp.ep.liu.se/index.php/histocrypt/article/download/402/360; repo `puzzles/viete-f539/` (Gallica IIIF already used).

### 2. DECODE "unsolved" records: automated triage

- **Data:** the DECODE database of historical ciphers and keys (Héder & Megyesi). Secondary literature puts it at about 10,000 early modern ciphertexts and keys, spanning the 14th century to 1965. The DECRYPT site says all records are open to the public, with images and, for many, transcriptions ([DECRYPT](https://de-crypt.org/); Version 2 paper, HistoCrypt 2022, [SZTAKI](https://eprints.sztaki.hu/10338/)). An earlier paper counts more than 1,000 keys, about 41% of them transcribed. This repo notes that some records need a login (Greg's, DECODE R2281 in `viete-f539`).
- **Question / what a find looks like:** take a record marked as a ciphertext with no plaintext and no key. Either (a) a key already in DECODE solves it (key–cipher matching across records), or (b) a homophonic or nomenclator solver with a language model breaks it. A find is a readable plaintext of a record that was not readable before.
- **Gap evidence:** the repo's own catalogue lists unsolved DECODE records that "were not opened" or "not yet tried" (`catalog/entries/royalist-civil-war-ciphers.md`: BL Add MS 72438 ff. 9–10 beside "about 49 captured Digby keys" in the same volume; `ferdinand-iii-habsburg-ciphers.md`: R1579). Same-volume keys left untried are a concrete gap.
- **Verifier:** mechanical. A key either produces fluent text in the expected language or it does not. The matched-control discipline already used in `viete-f539` (anneal on a known positive of the same length first) guards against overclaiming.
- **Precedent:** the Mary Stuart solution used Lasry's CrypTool-based homophonic solver; key–ciphertext matching is a standard DECRYPT task ([DECRYPT project, Cryptologia 2020](https://www.tandfonline.com/doi/full/10.1080/01611194.2020.1716410), SCHOLARLY). Kopal and Megyesi's 2026 DescryptTool (an agentic LLM workbench, Cryptologia) reportedly solved 10 of 10 Vigenère-family test cases (POPULAR report; not checked).
- **Recipe:** *code* exports DECODE metadata, filters records whose type is ciphertext and whose status is unsolved, and groups them by archive, volume and date. For each group it ranks candidate keys by catalogue proximity (same volume, same correspondent, ±10 years). *Code* applies each key and scores the output with a language model, then runs a homophonic solver where no key fits. The *LLM* only reads the top outputs and proposes word boundaries and named entities, which a human checks against the archive context.
- **Cost:** a CPU laptop. Annealing solvers take minutes per record, and transcription is the bottleneck: many records have images but no transcription, so a human or a vision reader must transcribe them. The repo's experience is that Sonnet readers are a known quality wall.
- **Traps:** a short text produces "solutions" that are noise. The `viete-f539` controls showed that even 50 known signs leave about half the text wrong. Nomenclator codes (hundreds of code words) cannot be broken without the key. The crank history is LLMs "translating" cipher, which is why Rule 6 applies.
- **Crowding:** `PARTLY`, rising. The Stockholm DECRYPT/DESCRYPT group (DescryptTool, 2026), Matthew Green's open-source "Decipher" (2026, POPULAR report), and Tomokiyo's site. The long tail of single records still looks unworked.
- **Ethics:** clear (historical; the youngest material, near 1965, could name living people: skip post-1945 records).
- **Scores:** `data_ready 3` (images yes, transcriptions partial, some login), `gap 3`, `verifier 5`, `cheapness 4`, `payoff 3`, `ethics_clear 5`
- **Sources:** Héder & Megyesi 2022, DECODE v2 (SCHOLARLY) https://eprints.sztaki.hu/10338/; DECRYPT site (PRIMARY, not fetched) https://de-crypt.org/; Megyesi et al., "Decryption of historical manuscripts: the DECRYPT project", Cryptologia 2020 (SCHOLARLY) https://www.tandfonline.com/doi/full/10.1080/01611194.2020.1716410; Kopal & Megyesi, DescryptTool, Cryptologia 2026 (SCHOLARLY, citation only) https://doi.org/10.1080/01611194.2026.2693460; Schneier blog, June 2026 (POPULAR) https://www.schneier.com/blog/archives/2026/06/ai-used-to-decrypt-medieval-ciphers.html; aiweekly on Green's Decipher (POPULAR) https://aiweekly.co/alerts/matthew-green-releases-decipher-an-ai-assisted-cipher-cracker.

### 3. Simancas (PARES): cipher letters with interlinear decipherments, for key recovery

- **Data:** Archivo General de Simancas, Estado series (Flanders, Rome, Naples, France K), digitized in part on PARES (`pares.mcu.es`, a Spanish Ministry of Culture portal, free image viewing). How much of Estado is online was **not verified** (see Unverified).
- **Question / what a find looks like:** Simancas holds the *received* letters, often deciphered between the lines by the secretariat. Each such letter is a plaintext–ciphertext pair. Harvesting the pairs mechanically reconstructs keys (alphabets, syllables, code words). Those keys then read (a) the letters with no interlinear text and (b) the same correspondence's cipher held elsewhere: BnF Espagnol 132 for this repo, Vargas Mexía's side in K 1550–1555.
- **Gap evidence:** a 2025 cluster of papers in *Estudios Románicos* reconstructs individual Simancas ciphers by hand, one correspondence at a time: Joanna of Austria (Estado 507–516), Rome 1543 (leg. 871), the 1565–66 conclave (leg. 899–902), Naples 1547. That shows interlinear pairs exist and are being worked, and that the coverage so far is per legajo, not systematic.
- **Verifier:** mechanical (a held-out letter decrypted with the recovered key must be readable), plus printed calendars (CODOIN; the Calendar of State Papers Spain on British History Online) that print some plaintexts.
- **Precedent:** this repo's `vargas-mexia-es132` dive. Tomokiyo's Cipher 4 key reads BnF letters, and held-out letters confirm it (repo, PRIMARY work product). The *Estudios Románicos* papers above (SCHOLARLY).
- **Recipe:** *code* pulls PARES images for the target legajos. A *vision reader* (two independent readers, per the repo's es132 practice) transcribes cipher groups and interlinear plaintext. *Code* aligns the two and tallies sign→value with counts. *Code* builds a key with confidence per sign and tests it on held-out letters. A human paleographer reviews.
- **Cost:** reader passes cost tens of dollars per legajo; human review is the bottleneck. No GPU.
- **Traps:** interlinear decipherments are sometimes partial or paraphrased. Keys changed often, so letters must be grouped by key before pooling. Simancas K material has been partly calendared, so check print before claiming novelty.
- **Crowding:** `PARTLY` (the *Estudios Románicos* group; Tomokiyo).
- **Ethics:** clear.
- **Scores:** `data_ready 3`, `gap 3`, `verifier 5`, `cheapness 3`, `payoff 4` (for this repo specifically; 3 generally), `ethics_clear 5`
- **Sources:** *Estudios Románicos* 2025 articles (SCHOLARLY; abstracts via search, not fetched): https://revistas.um.es/estudiosromanicos/article/view/615151, https://revistas.um.es/estudiosromanicos/article/view/615731, https://revistas.um.es/estudiosromanicos/article/download/613911/376591/2488931; repo `puzzles/vargas-mexia-es132/NEXT.md`; British History Online, Calendar of State Papers Spain (SECONDARY) https://www.british-history.ac.uk/node/79554.

### 4. Anonymous and misattributed works in digitized manuscript fonds (HTR + stylometry)

- **Data:** national-library theatre and literary manuscripts catalogued "anónimo" or "anonyme", with images online: BNE (Biblioteca Digital Hispánica), BnF Gallica, BSB, ÖNB. Reference corpora: the ETSO corpus (over 1,000 prints and 400 manuscripts, about 350 dramatists, for Spanish Golden Age drama), EEBO-TCP for English (#5), and comparable corpora for French and Italian.
- **Question / what a find looks like:** an anonymous or misattributed text that stylometry assigns to a known author with a held-out-validated confidence, and which a philologist confirms from content, dating and versification. The precedent is a "new" Lope play.
- **Gap evidence:** ETSO says it aims to restore works across about 350 dramatists, and that many anonymous manuscripts remain untested. The equivalent sweep in other literatures (French *comédies*, Italian *commedia* scenarios, German *Haupt- und Staatsaktionen*) was not found. The Mozart KV 648 copy (Leipzig, 2024) surfaced during catalogue work on a collection that had been held since the 19th century.
- **Verifier:** stylometric control experiments (ETSO reports 99% correct identification of Lope in controls), then philologists (*Anuario Lope de Vega* peer review), then external evidence (titles in period lists of an author's plays).
- **Precedent:** *La francesa Laura*. A Transkribus transcription of a BNE manuscript catalogued anonymous in 1882 was attributed to Lope by Cuéllar and Vega García-Luengos, announced January 2023 and published in *Anuario Lope de Vega* (SCHOLARLY via POPULAR and Transkribus blog reports). Mozart, *Ganz kleine Nachtmusik* KV 648: a c. 1780 copy found in the Leipzig Municipal Libraries during work on the Köchel catalogue, 2024 (POPULAR; the attribution is not certain, per the reports).
- **Recipe:** *code* lists anonymous manuscripts per fonds from the catalogue APIs. *HTR* (Transkribus or an open model) transcribes them. *Code* runs delta-family stylometry against an author corpus, with leave-one-out controls per author and an "inconclusive" class. The *LLM* reads only the top candidates to extract datable content (allusions, versification), for a human to judge.
- **Cost:** HTR is the main cost: Transkribus credits or a self-hosted model, hundreds of dollars for a fonds. Stylometry runs on a CPU.
- **Traps:** stylometry on noisy HTR output (ETSO says results were close to those on edited text, but that is a self-report). Collaborative and revised plays. Copyist interference. The Shakespeare-attribution cottage industry is the crank history: most "new Shakespeare" claims fail. Many ETSO reports end "inconclusive", which is the correct output.
- **Crowding:** `CROWDED` for Spanish Golden Age drama (ETSO). `OPEN` elsewhere, as far as this survey found.
- **Ethics:** clear.
- **Scores:** `data_ready 3`, `gap 3`, `verifier 4`, `cheapness 3`, `payoff 4`, `ethics_clear 5`
- **Sources:** Transkribus blog on Cuéllar (POPULAR, vendor) https://www.transkribus.org/blog/lost-play-by-lope-de-vega-álvaro-cuéllar; ETSO reports (SCHOLARLY, project) https://etso.es/en/informes/analisis-estilometrico-el-rey-angel; Cuéllar & Vega, *Talía* / UCM (SCHOLARLY) https://revistas.ucm.es/index.php/TRET/article/view/74625; Reuters via China Daily HK, 3 Feb 2023 (POPULAR) https://chinadailyhk.com/article/313346; ZME Science on KV 648 (POPULAR) https://zmescience.com/science/news-science/lost-mozart-manuscript-discovered-in-leipzig-dating-back-to-his-childhood.

### 5. EEBO-TCP and newspapers: unattributed text reuse and lost sources

- **Data:** EEBO-TCP, 53,831 transcribed English books to 1700, CC0 since August 2020 (Oxford Text Archive, TCP, UChicago PhiloLogic). Chronicling America OCR for the 19th century (#6).
- **Question / what a find looks like:** long verbatim or near-verbatim passages shared between an EEBO text and a later work that cites no source. Sharper: shared passages that point to a *lost* common source, such as an unprinted manuscript or a lost play.
- **Gap evidence:** pairwise reuse detection across all 54k texts is cheap now, but no published complete EEBO-wide reuse table was found (UChicago's Textual Optics Lab runs PhiloLogic and sequence-alignment tools over EEBO; whether a full all-pairs table exists is unverified).
- **Verifier:** the passages themselves. Alignment is mechanical, and a reuse claim is checkable by reading both. Book historians and early-modern editors judge direction and significance.
- **Precedent:** McCarthy & Schlueter (2018) used WCopyfind to connect George North's manuscript *A Brief Discourse of Rebellion and Rebels* to 11 Shakespeare plays (Boydell & Brewer; the Folger calls it "investigated and debated", so `contested`). Viral Texts (Cordell & Smith) found thousands of unrecognised reprinted texts in Chronicling America.
- **Recipe:** *code* builds n-gram shingles over regularized spelling (VARD-style or MorphAdorn), uses minhash to find candidate pairs, and runs Smith–Waterman alignment. It filters out the Bible, proverbs, legal formulae and catechisms. The *LLM* summarizes each surviving cluster and guesses direction for a human to check.
- **Cost:** EEBO-TCP is about 1.5B words; all-pairs minhash fits in a day on a 64 GB VM. Under $50.
- **Traps:** common-source effects (the Bible, Erasmus's *Adagia*, homilies) flood the output. Spelling variation. "Source" claims inflate into authorship claims: the McCarthy work sits close to the authorship question, a field with a long crank history (Oxfordians).
- **Crowding:** `PARTLY` (Textual Optics Lab; Viral Texts for newspapers; many single-author source studies).
- **Ethics:** clear.
- **Scores:** `data_ready 5`, `gap 2`, `verifier 4`, `cheapness 5`, `payoff 3`, `ethics_clear 5`
- **Sources:** TCP EEBO page (PRIMARY) https://textcreationpartnership.org/tcp-texts/eebo-tcp-early-english-books-online/; Oxford Text Archive Phase 2 (PRIMARY) https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/6; UChicago Textual Optics Lab (SCHOLARLY, project) https://textual-optics-lab.uchicago.edu/node/29; Folger podcast with McCarthy & Schlueter (SECONDARY) https://www.folger.edu/podcasts/shakespeare-unlimited/george-north-manuscript/; Bangor Daily News 2018 (POPULAR) https://www.bangordailynews.com/2018/02/09/news/using-plagiarism-software-nh-scholar-finds-similarities-between-shakespeare-plays-earlier-manuscript/; Viral Texts / *Going the Rounds* (SCHOLARLY) https://manifold.umn.edu/projects/going-the-rounds.

### 6. OCR'd newspapers: pre-instrumental earthquakes, aurorae and other transient events

- **Data:** Chronicling America (Library of Congress): about 23.7M pages and more than 4,500 titles, 1736–1963 (April 2026 LoC deck). Since 2025 it is available only through the loc.gov API, and bulk OCR status after the August 2025 relaunch is unclear. Trove (National Library of Australia), with an API key. Many national equivalents (Delpher, Papers Past, BnF RetroNews in part).
- **Question / what a find looks like:** an earthquake absent from the national historical catalogue, reported independently from several towns on the same date, with intensities that can be mapped. The same applies to aurora sightings at low latitude (storm-size estimates) and to fireballs.
- **Gap evidence:** the Trove precedent recovered **110 previously unrecognised events** for South Australia alone (Adelaide thesis, 2013). Rubenach et al. (2021) used Trove to re-examine 12 Queensland earthquakes, and Trove challenged some existing interpretations. This survey found **no comparable sweep of Chronicling America** for earthquakes or aurorae (absence of evidence; the budget ran out before a targeted check).
- **Verifier:** the existing catalogue (USGS / Stover & Coffman for the US; national catalogues elsewhere), consistency across independent towns (the clock times must agree), and for aurorae, magnetometer records where they exist (Colaba, Greenwich) and Hayakawa-style catalogues.
- **Precedent:** Adelaide thesis (SCHOLARLY); Rubenach et al., *Aust. J. Earth Sci.* 2021 (SCHOLARLY); Hayakawa et al. reconstruct historical storms from more than 700 auroral records in archives (SCHOLARLY, arXiv 1807.05186).
- **Recipe:** *code* runs keyword queries ("earthquake", "shock", "tremor", "aurora", "northern lights") per date through the loc.gov API and pulls OCR text. The *LLM* extracts structured fields (place, date, local time, felt effects, rough intensity) as JSON, with the quote attached. *Code* clusters reports by date and geography and matches them against the catalogue. Unmatched clusters with three or more independent towns go to a seismologist or historical-seismicity specialist.
- **Cost:** API pulls take hours to days at a polite rate, and LLM extraction over about 50k hits costs $20–100. No GPU.
- **Traps:** reprinted wire stories make one report look like many (Viral Texts shows how pervasive reprinting was), so de-duplicate by text. Explosions, gunpowder mills and blasting. Figurative "earthquake" (political). OCR errors in dates. Aurora reports with no time stamp. The crank history is "earthquake swarm" claims built on one sensational paper.
- **Crowding:** `PARTLY` for Australia (Trove studies). `OPEN` for the US and Chronicling America, as far as found.
- **Ethics:** clear (historic public events).
- **Scores:** `data_ready 4`, `gap 4`, `verifier 4`, `cheapness 5`, `payoff 3`, `ethics_clear 5`
- **Sources:** LoC Chronicling America technical information (PRIMARY) https://www.loc.gov/collections/chronicling-america/about-this-collection/technical-information/; LoC NDNP deck, April 2026 (PRIMARY) https://loc.gov/ndnp/guidelines/docs/GASiteVisitDataAPI20260401.pdf; LoC migration notice (PRIMARY) https://loc.gov/ndnp/migration; Adelaide thesis 2013 (SCHOLARLY) https://digital.library.adelaide.edu.au/dspace/handle/2440/84130; Rubenach et al., JCU (SCHOLARLY) https://researchonline.jcu.edu.au/67279/; Hayakawa et al., 1872 storm (SCHOLARLY) https://arxiv.org/pdf/1807.05186.

### 7. Cairo Genizah after MiDRASH: identifications and joins by text match

- **Data:** MiDRASH (ERC Synergy, €10M, launched with the National Library of Israel's KTIV) reports machine transcriptions of about 400,000 Genizah fragments, about 160 million words. Before this, fewer than 10% had readable transcriptions. Images come from the Friedberg Genizah Project and holding libraries. Coverage reports differ on whether the full search is live yet. Download and licence terms were not verified.
- **Question / what a find looks like:** (a) an "unidentified" fragment that matches a known work: a lost or rare text, a variant of a known one, or a quotation of a lost work; (b) a join, meaning two fragments in different libraries that are one leaf or one manuscript.
- **Gap evidence:** a 90% untranscribed corpus has just become text, and earlier computational joining used images only (Wolf & Dershowitz: about 1,000 confirmed joins in months, against roughly a century of manual work).
- **Verifier:** Genizah specialists (FGP's join registry, the Taylor-Schechter Unit), and the text match itself (shared lines are checkable).
- **Precedent:** the Tel Aviv/Friedberg image-based join finder (SCHOLARLY: IJCV 2011; ICCV workshop 2009).
- **Recipe:** *code* pulls transcriptions, n-gram-indexes them against the Sefaria corpus and known works, and lists high-scoring matches of fragments catalogued as "unidentified". It also finds text-continuity joins (one fragment's last line continues in another fragment). The *LLM* triages Judeo-Arabic content. Human Genizah scholars confirm.
- **Cost:** low once the data is downloadable. Access is the uncertainty.
- **Traps:** HTR error rates are not reported. Liturgy repeats everywhere. Many "identifications" may already sit in FGP's internal catalogue.
- **Crowding:** `CROWDED` (MiDRASH itself, FGP, the Princeton Geniza Project). The hobbyist angle is checking specific genres the projects deprioritize.
- **Ethics:** clear.
- **Scores:** `data_ready 2` (access unverified), `gap 3`, `verifier 4`, `cheapness 4`, `payoff 3`, `ethics_clear 5`
- **Sources:** JNS, "AI unlocks Cairo Genizah's hidden world" (POPULAR) https://www.jns.org/ai-unlocks-cairo-genizahs-hidden-world/; NLI ERC announcement (PRIMARY) https://www.nli.org.il/en/at-your-service/announcements/european-research-council-awards; Wolf et al., join candidates (SCHOLARLY) https://mlanthology.org/iccvw/2009/wolf2009iccvw-automatically; NBC/LiveScience on 1,000 joins (POPULAR) https://www.livescience.com/16620-digitized-cairo-genizah-texts.html.

### 8. Printed mathematical tables: errata detection by recomputation

- **Data:** digitized historical tables (logarithms, trigonometric functions, astronomical ephemerides) on Internet Archive, HathiTrust and Gallica. LOCOMAT (Denis Roegel, LORIA) has already reconstructed dozens.
- **Question / what a find looks like:** the list of wrong entries in a given table, and propagation: which later tables copied the same error, which dates the lineage of copying (who copied whom). It works as a calibration case for Rule 7: a perfect verifier with a modest payoff.
- **Gap evidence:** Roegel reconstructs "ideal" tables and notes that the originals' errors "have not been reproduced". Systematic per-table error listings and copy-lineage analyses across many tables were not found.
- **Verifier:** total and mechanical (recompute each value).
- **Precedent:** LOCOMAT reconstructions record specific errors (Bürgi's sine table: a copying error at 4°, recoverable from its difference column). The classic 19th-century errata literature (Babbage) exists, but citation was not verified.
- **Recipe:** *OCR* of the digit columns (a vision model or Tesseract with a digit whitelist). *Code* recomputes the values and diffs them, then fingerprints shared errors across tables. The LLM is barely needed.
- **Cost:** trivial.
- **Traps:** OCR digit errors look like table errors, so every flagged entry needs a crop and a human glance. Deliberate rounding conventions.
- **Crowding:** `PARTLY` (LOCOMAT).
- **Ethics:** clear.
- **Scores:** `data_ready 4`, `gap 3`, `verifier 5`, `cheapness 5`, `payoff 1`, `ethics_clear 5`
- **Sources:** LOCOMAT index (SCHOLARLY, project) https://locomat.loria.fr/locomat/reconstructed.html; Gunter 1620 reconstruction (SCHOLARLY) https://locomat.loria.fr/gunter1620/gunter1620doc.pdf; Bürgi sines (SCHOLARLY) https://locomat.loria.fr/buergi-sines/roegel2016buergi-sine-table1.pdf.

---

### Considered and set aside (status recorded so nobody re-proposes them blind)

| Candidate | Why set aside | Crowding | Sources |
|---|---|---|---|
| **Herculaneum scrolls (Vesuvius Challenge)** | Real and live: June 2026 announcements of PHerc. 139 title *On Gods* Bk 8 and PHerc. 1667 read in full; data and code reportedly open and a new $1M prize. A funded field with its own verifiers. | `CROWDED` | UKy (PRIMARY) https://engr.uky.edu/herculaneum; Diamond 2026 (PRIMARY) https://www.diamond.ac.uk/Home/News/LatestNews/2026/New-secrets-revealed-from-the-Herculaneum-scrolls.html; ADN/AP (POPULAR) https://www.adn.com/nation-world/2026/06/25/scientists-have-just-unlocked-the-secrets-of-an-ancient-scroll-torched-by-mount-vesuvius/ |
| **Palimpsest multispectral data (Sinai, Codex Climaci Rescriptus)** | Strong precedent: Hipparchus star-catalogue fragments (Gysembergh, Williams & Zingg, *JHA* 53(4), 2022). The Sinai project imaged 74 palimpsests, about 6,800 pages, and an open-access publication was funded. The UCLA site could not be fetched, so data access is unverified and `data_ready` unknown. Worth a recheck: if the processed images are open, this moves up. | `PARTLY` | Taylor, ORA (SCHOLARLY) https://ora.ox.ac.uk/objects/uuid:a381b5f0-1437-495e-a050-15d4418f9066/files/sw6634633k; Culture in Crisis (SECONDARY) https://cultureincrisis.org/projects/sinai-palimpsest-project-open-access-online-publication; CNRS PR (PRIMARY) https://d-sciences.dsi.sorbonne-universite.fr/sites/default/files/media/2022-11/CPCNRS-cataloguehipparque-EN_0.pdf |
| **Oxyrhynchus unpublished papyri** | About 400–500k pieces, about one EES volume a year (vol. LXXXVIII, 2025), "at least 40 more volumes". The images are not public. Ancient Lives (Zooniverse) is concluded. Fails `data_ready`. | `CROWDED` (Oxford/EES) | Nongbri 2019 (SECONDARY) https://brentnongbri.com/2019/10/20/how-much-material-from-oxyrhynchus-remains-unpublished/; Oxford publications (PRIMARY) https://oxyrhynchus.web.ox.ac.uk/publications |
| **Ship logbooks (climate, wrecks)** | oldWeather: 16,400 volunteers, 1.09M pages from 302 ships, about 1.6M observations feeding ICOADS. Wreck-location mining is a looting risk (coordinates). | `CROWDED` | Wikipedia (SECONDARY) https://en.wikipedia.org/wiki/Old_Weather |
| **Declassified-document redaction diffs (JFK 2025, CREST, FRUS)** | Diffs between official releases already exist (jfkdiffs.com, the Mary Ferrell Foundation, The Black Vault). Reconstructing text that is *still* redacted from duplicates edges toward defeating security and can expose living sources. Dropped under the brief's ethics rule; only diffs of officially released versions are acceptable, and that ground is crowded. History Lab (Connelly) does pattern analysis of redaction. | `CROWDED` | MFF (SECONDARY) https://www.maryferrell.org/pages/Featured_2025_JFK_Records_Releases.html; Black Vault (POPULAR) https://www.theblackvault.com/documentarchive/the-black-vaults-2025-jfk-files-search-tool/; Columbia Magazine on History Lab (POPULAR) https://magazine.columbia.edu/article/what-declassified-government-documents-reveal-about-americas-dark-secrets |
| **Lost films and media** | Identification happens in curated workshops (LoC "Mostly Lost", from 2012) on archive prints that are not public data. Nothing is machine-readable to sweep, and verification is connoisseurship. | `PARTLY` | LoC 2017 (PRIMARY) https://www.loc.gov/item/prn-17-062/library-investigates-mostly-lost-films/2017-05-01/ |
| **Binding fragments (Bristol Merlin type)** | The 2019 Bristol Merlin (Suite Vulgate, 1250–75) was found physically in bindings, not in digitized data. Fragmentarium hosts fragment images, but no machine-matching precedent was verified. A possible follow-up: cross-match Fragmentarium against IIIF codices. | `PARTLY` | Bristol 2019 (PRIMARY) https://www.bristol.ac.uk/news/2019/january/bristol-merlin-.html; Fragmentarium (PRIMARY) https://fragmentarium.ms/pages/about/digital-laboratory |

---

## Pilot in a day

**Candidate #1, scoped to one fonds: a cipher-page sweep of BnF Cinq Cents de Colbert.** It feeds `viete-f539` (Colbert 33) and the Spanish-cipher work directly.

*Precondition:* `gallica.bnf.fr` was **not reachable** from this survey session (WebFetch DNS failure, container proxy 403). The repo downloaded from it on 2026-10-01, so check `curl -sS "$HTTPS_PROXY/__agentproxy/status"` and the allowlist first. If it is blocked, run the identical pipeline on e-codices or BL IIIF, or ask Greg to allow the host.

1. **List the volumes.** Gallica SRU:
   `https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=dc.title%20all%20%22Cinq%20cents%20de%20Colbert%22%20and%20dc.type%20all%20%22manuscrit%22&maximumRecords=50&startRecord=1`
   Page through `startRecord`, collect the ark IDs, and keep the SRU XML under `analysis/` (Rule 6).
2. **Pull manifests and thumbnails.** `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/manifest.json`, then each canvas at `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<n>/full/400,/0/native.jpg`. Throttle to about 1 request per second, which gives roughly 30k images in about 9 hours, so run overnight or start with 50 volumes.
3. **Build the labelled control before sweeping.** Positives are the known cipher folios: Colbert 33 f. 539 (`ark:/12148/btv1b10033958p`, canvas 544, already in the repo), Lasry's Colbert 33 f. 555, and other BnF records in DECODE. Negatives are 200 random folios. Label them by eye.
4. **Classify.** Run a vision model on each thumbnail with one frozen prompt that returns `{cipher|mixed|clear|table|other}` plus a one-line reason. Report precision and recall on the control set; stop if recall is below 0.8.
5. **Join.** For each hit, compare against the BnF Archives et Manuscrits description (does it say "chiffre" or "en chiffre"?) and against DECODE shelfmarks (manually, if the DECODE host is still blocked). Output `hits.tsv`: ark, folio, label, catalogue text, in-DECODE y/n.
6. **Stop there.** The deliverable is the list of undescribed cipher pages. Decipherment of any of them is a `/focus` dive with its own controls.

Cost: about $10–40 of vision calls for 30k thumbnails at a cheap tier, and one day.

## Unverified claims

- The DECODE record count ("about 10,000") comes from secondary reviews (a 2026 DescryptTool summary). The DECODE and DECRYPT sites could not be fetched, the "all records open to the public" statement is from a search snippet, and the repo notes that some records need a login.
- The exact Cryptologia citation and date for Lasry, Biermann & Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578–1584" (reports range from Feb 2023 to "last year" in 2024). The BnF shelfmarks of the 57 letters were not recovered here.
- The "about 1% of archival material is encrypted" estimate comes from a blog comment on Schneier's site and has no source.
- DescryptTool's "10/10 Vigenère cases" is a POPULAR summary of a paper not read. The "Borg cipher deciphered in 28 minutes" claim (via AzerNEWS) is unconfirmed.
- How much of the Simancas Estado series is digitized on PARES, and which authors and project are behind the 2025 *Estudios Románicos* cipher articles, were not checked (the search budget was exhausted).
- Whether Chronicling America bulk OCR downloads are currently available after the August 2025 relaunch is unclear from LoC's own pages.
- That no Chronicling America sweep for historical earthquakes or aurorae exists is absence of evidence from one search.
- Whether a complete EEBO-TCP all-pairs text-reuse table already exists (possibly at the UChicago Textual Optics Lab) was not checked.
- MiDRASH: whether the 400k transcriptions are downloadable, under what licence, and their error rates.
- Whether the Sinai Palimpsests processed images are openly downloadable today.
- Lost-work "finds" proposed in the dispatch prompt (an unknown Plautus, a new Ovid, Cervantes, a "lost Chrétien", a lost Euripides fragment in a digitized collection) were **not found** by this survey and are not asserted. The Bristol Merlin (2019) is real but was a physical find in bindings, not a digitized-data find.
- Babbage-era errata literature on printed tables: cited from memory only, not verified.
