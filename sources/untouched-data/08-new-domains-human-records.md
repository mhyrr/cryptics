# 08 — New domains: human-made records and institutions

*2026-10-15. Survey only (Rule 9): no discovery was attempted. Brief: `BRIEF.md`.
Fetch note: WebFetch could not resolve several hosts this session (rism.info,
arxiv.org, locomat.loria.fr, lmu.de), so many claims below rest on search-result
summaries of those pages rather than a direct read. Those are flagged where the
score depends on them, and the shakiest are repeated under Unverified claims.*

**Summary of best bets**

1. **RISM music incipits (new).** Over 1.7M machine-readable incipits under CC-BY, about 200k anonymous sources, and a record of attributions found by incipit search (Vivaldi in Durham and Dresden). An all-pairs sweep of anonymous against attributed incipits is a laptop job, and a match is easy to check. **Best pilot.**
2. **Shared errors in printed mathematical tables (new).** Recomputing a table is a perfect verifier, and the errors that tables share show who copied whom. Babbage (1827) found that 13 sets of tables shared six errors. Most scanned tables have never been diffed against recomputed values.
3. **Unflagged hallucinated citations in court filings (seed, reframed).** Charlotin's database lists about 1,600 cases, but only where a court made a finding. RECAP holds millions of filings no court checked, and CourtListener's citation-lookup API gives a near-mechanical first pass. The ethics need care.
4. **Damaged type and printers' ornaments (new).** The CMU *Areopagitica* attribution and the Compositor ornament database are precedents. The verifier is strong (physical type damage), but most page images are behind licenses.
5. **Cuneiform joins (seed).** The eBL Fragmentarium found Gilgamesh pieces by algorithm. CDLI and eBL release open ATF. Crowded by the experts themselves, so the open lane is narrow.

---

### 1. RISM incipits: attributing anonymous music by melodic matching

- **Data.** RISM (Répertoire International des Sources Musicales) catalogs music manuscripts and prints, mostly 1600–1850. Its records are released as open and linked open data in MARC XML and RDF under CC-BY (version stated as 3.0 in one RISM post; check it). RISM reports over 1 million records and over 1.7 million music incipits, encoded in Plaine & Easie code (PAE) or MEI. The data was collected to catalog sources library by library, not to cross-match works.
- **Question / a find.** An incipit on an anonymous or misattributed source that matches, interval for interval, a work securely attributed elsewhere. Also: one work circulating under two composers' names, and borrowed movements inside pasticcios.
- **Gap evidence.** RISM says it holds over 200,000 anonymous sources, about 20% of the database. Today, identification relies on single users searching one incipit at a time and reporting back ("people like you regularly let us know when they have spotted an error or identified an anonymous piece"). I found no published exhaustive all-pairs sweep. **Note:** many records carry only a text incipit or a key or clef, with no notes, so the searchable pool is smaller than 200k.
- **Verifier.** Strong and cheap. (a) Mechanical: transposition-invariant interval and rhythm match over 10 or more notes, then the next incipits (movements 2 and 3) of the same work must match too. (b) Expert: a musicologist compares the full sources (often digitized). RISM's editorial team accepts corrections.
- **Precedent.** RISM blog, "Vivaldi and a Search Engine" (2013): a database search turned up an anonymous, incomplete set of parts for RV 241 at Durham Cathedral, a second source for a concerto whose Dresden score was thought unique. 2014: a transposed-incipit search showed that a "Brescianello" violin concerto embeds a Vivaldi movement (pasticcio). 2017: another misattributed Vivaldi work found in Dresden. All were found one query at a time.
- **Recipe.** Code: parse the MARC XML (field 031 holds incipits), normalize PAE to an interval sequence with a coarse rhythm profile, and index n-grams (n=6–8). For each anonymous incipit, retrieve candidates, then score with local alignment; require two or more movements of the same source to match. LLM: read the hit list, write the case note, check that the composer's dates fit the source date, and flag famous tunes (chorales, folk melodies) and other common-property cases.
- **Cost.** Under 1 GB of data. A CPU-hours job. About $0–20 of LLM tokens to triage a few hundred hits.
- **Traps.** Generic openings (arpeggiated tonic triads, scale runs), chorale and hymn tunes, dance formulae, and Alberti-bass beginnings all match by accident. Incipit encoding errors. A copyist's name read as the composer. 18th-century misattribution was common and sometimes deliberate (publishers sold "Haydn" freely), so a match to a *named* source does not settle authorship. It moves the question from "anonymous" to "attributed in source X". Calibrate on known cases (the Vivaldi finds above) before trusting any score.
- **Crowding.** `PARTLY`. RISM staff and users do this ad hoc, and music-IR research (incipit similarity) exists. I found no record of a published full sweep.
- **Ethics.** Clear. Historical works, CC-BY data, no living subjects.
- **Scores.** data_ready 4 · gap 4 · verifier 4 · cheapness 5 · payoff 3 · ethics_clear 5
- **Sources.**
  - https://rism.info/community/data-services.html (PRIMARY: data services; via search summary)
  - https://rism.info/rism_online_catalog/2015/04/16/rism-data-as-open-data-and-linked-open-data.html (PRIMARY: CC-BY, MARC XML/RDF)
  - https://rism.online/docs/api/incipit-search/ (PRIMARY: incipit API, PAE)
  - https://rism.info/rediscovered/2013/08/23/vivaldi-and-a-search-engine.html (PRIMARY: RV 241 Durham)
  - https://rism.info/rediscovered/2014/08/11/vivaldi-embedded-violin-concerto-by-brescianello.html (PRIMARY)
  - https://rism.info/rediscovered/2017/04/25/yet-another-misattributed-and-rediscovered-vivaldi.html (PRIMARY)
  - https://rism.info/rediscovered/2015/12/17/setting-the-rism-records-straight.html (PRIMARY: 200k anonymous, user reports)
  - https://releve.erudit.org/en/journals/renref/2024-v47-n1-renref09375/1111828ar.pdf (SCHOLARLY: review of RISM Online, MEI incipits)

### 2. Printed mathematical tables: errors, and the genealogy of copying

- **Data.** Thousands of 17th–20th-century tables (logarithms, trigonometric functions, factor tables, astronomical and navigation tables) scanned in Internet Archive, HathiTrust, Google Books and Gallica. Most are public domain. Denis Roegel's LOCOMAT project at LORIA publishes recomputed reconstructions of dozens of tables (Bürgi, Pitiscus, Vega, Babbage, Andoyer, Peters, Sang and others), with notes on the errors in each.
- **Question / a find.** (a) Uncatalogued errors in specific printed tables. (b) The real finding: **shared errors as fingerprints**. When two tables carry the same wrong digit, one copied the other (or a common source), even when it claims independent computation. This is stemmatics with a perfect oracle, because the true value is computable.
- **Gap evidence.** Fletcher, Miller, Rosenhead and Comrie's *Index of Mathematical Tables* (2nd ed. 1962) and *MTAC*/*Mathematics of Computation* errata cover the major tables, by hand and then by early machine. Roegel's reconstructions cover a curated set. The long tail of ordinary 18th–19th-century editions (school logarithms, national navigation tables, reprints) has, as far as I found, never been OCR'd and diffed systematically. I found no corpus-wide error-genealogy study.
- **Verifier.** Total and mechanical: recompute the function to the printed precision with correct rounding. A disagreement is a fact. Whether it is a typo, a rounding convention, or a copy-inherited error is then a judgment, but a constrained one.
- **Precedent.** Babbage, *On Errors common to many Tables of Logarithms* (1827): six errors common to 13 sets of tables printed in London 1633–1822, from which he inferred copying. Roegel reconstructs Babbage's own 1827 table and notes many last-digit errors beyond 100000 in a section Babbage copied from Callet. Roegel on Bürgi's sine table: very accurate, but sin 4° is printed with one wrong digit, judged a copying slip because the neighbouring difference is correct (difference checking as a verifier). Sang (1871) found errors in Vlacq. Lefort had found most of them earlier (a priority dispute).
- **Recipe.** Code: choose one table family (for example 7-place common logarithms, 1620–1900; dozens of editions). Run Tesseract or a digit-specific OCR on page images; tables are clean, regular grids of digits. Run difference checks to separate OCR errors from print errors: a print error leaves a consistent jump in the second differences, while an OCR slip fails both the recomputation and a re-read. Recompute exactly with Python `decimal`. Build an error × edition matrix, then cluster or do phylogenetic inference on shared errors. LLM: read prefaces and title pages for each edition's claimed sources and compare them with the error genealogy; write up.
- **Cost.** CPU only. About 1 day per table family for OCR and diffing. Tokens are negligible.
- **Traps.** OCR digit confusion (3/8, 1/7, 5/6) creates false "errors", so require each error to be confirmed on the page image (human or second OCR). Rounding conventions (some tables mark rounded-up last digits). Stereotype plates reused across "editions" make identical errors trivially. Errata slips bound in some copies only. Do not mistake a correction for an error: a later edition fixing an error is also signal.
- **Crowding.** `PARTLY`. Roegel (LOCOMAT) for flagship tables, and historical errata literature. The long tail and the genealogy question look open.
- **Ethics.** Clear.
- **Scores.** data_ready 3 · gap 4 · verifier 5 · cheapness 4 · payoff 2 · ethics_clear 5
- **Sources.**
  - https://locomat.loria.fr/locomat/reconstructed.html (SCHOLARLY: LOCOMAT list; not fetchable this session, seen via search)
  - https://locomat.loria.fr/buergi-sines/roegel2016buergi-sine-table1.pdf (SCHOLARLY: Bürgi sin 4° error)
  - https://treasures.scss.tcd.ie/literature/TCD-SCSS-V.20161219.001/DenisRoegel-Babbage1827doc.pdf (SCHOLARLY: Babbage/Callet last-digit errors)
  - https://historyofinformation.com/detail.php?id=4617 (SECONDARY: Babbage 1827 checking)
  - https://thocp.callapple.org/biographies/papers/computer_error.htm (POPULAR: Babbage's "Errors common to many tables", 13 tables / 6 errors)
  - https://www.ams.org/mcom/1950-04-029/S0025-5718-50-99482-8/S0025-5718-50-99482-8.pdf (SCHOLARLY: MTAC errata series)
  - https://www.nature.com/articles/158252b0.pdf (SCHOLARLY: Sang/Lefort priority)

### 3. Court filings: hallucinated citations nobody caught (plus model-bill copying)

- **Data.** CourtListener (Free Law Project) offers about 9–10M opinions, and its RECAP archive holds tens of millions of PACER dockets and hundreds of millions of documents gathered by browser extension. It provides an API, bulk files, and a Citation Lookup API backed by about 18M citations, built on the Eyecite parser. Legislative text: the Sunlight-era corpus of over 500k state bills, and LegiScan (license to check).
- **Question / a find.** (a) Briefs and motions citing cases that do not exist, or misquoting real ones, **in filings no court has flagged**. (b) Secondary: bills that are near-verbatim copies of model legislation (well trodden), or judicial opinions copied from party briefs or proposed orders.
- **Gap evidence.** Damien Charlotin's AI Hallucination Cases database had 1,598 worldwide entries by 9 June 2026 (1,058 US by early June per UNC), but it includes only decisions where a court explicitly found or clearly implied reliance on hallucinated material. The undetected rate in filings is unmeasured. That is the gap. On legislation, *Copy, Paste, Legislate* (USA Today/Arizona Republic/CPI, 2019) scanned nearly 1M bills and found about 10,000 copied ones, and DSSG's Legislative Influence Detector found 14,137 model-to-bill reuses. That part is `CROWDED`.
- **Verifier.** Near-mechanical: citation lookup returns 404 ("valid format, not in corpus"), then a person checks the reporter volume and page (CourtListener, Caselaw Access Project, Google Scholar). A "case does not exist" finding is binary once checked. Misquotations need a text diff against the opinion.
- **Precedent.** Charlotin's database itself. FLP built the lookup API explicitly "to combat hallucinations". Corley (2008, *PRQ*) used plagiarism software to measure Supreme Court opinions' borrowing from briefs (about 10% overlap on average). Feldman extended this to 1946–2014 (NYT 2015).
- **Recipe.** Code: sample RECAP filings by date (pre-2022 as a control, since no LLMs, versus 2023–26), extract citations with Eyecite, and batch-resolve them through the API (rate limits: about 60 valid citations per minute according to a third-party guide). Keep the 404s, then filter reporter typos and unpublished or slip-opinion citations. LLM: for each survivor, search alternative databases and judge "really nonexistent vs. obscure". Code computes the rates. **Report rates by court, year and filer type (pro se vs. counsel), not names.**
- **Cost.** Free API but rate-limited. PACER fees do not apply, because the data is already in RECAP. Days of wall-clock time, low dollars.
- **Traps.** Citations to unpublished or state-reporter cases missing from CourtListener (false 404s), parallel citations, OCR'd older filings, and pro se litigants' garbled but real citations. The pre-LLM control period is essential (Rule 7): it measures the base rate of honest bad citations.
- **Crowding.** Hallucinations: `PARTLY` (Charlotin catalogs court-found cases, and vendors sell checkers). Legislation copying: `CROWDED`.
- **Ethics.** Filings are public, but naming individual lawyers or pro se litigants for unflagged errors harms living people who were never adjudicated. Publish aggregate rates. Any individual case goes to the court or bar, not to a blog. Pro se filers should be excluded from any named reporting.
- **Scores.** data_ready 4 · gap 4 · verifier 4 · cheapness 4 · payoff 3 · ethics_clear 3
- **Sources.**
  - https://free.law/tag/case-law (PRIMARY: "Combat Hallucinations and Look Up Citations with our New API")
  - https://wiki.free.law/c/courtlistener/help/api/rest/v4/citation-lookup (PRIMARY: API docs)
  - https://www.vaquill.ai/blog/courtlistener-citation-lookup-api-guide (POPULAR: rate limits, status codes)
  - https://library.law.unc.edu/2026/06/handling-hallucinations-a-reflection/ (SECONDARY: 1,058 US cases, inclusion criteria)
  - https://haqq.ai/blog/ai-legal-hallucination-audit.html (POPULAR: 1,598 worldwide, 9 June 2026)
  - https://publicintegrity.org/state-politics/copy-paste-legislate/how-we-uncovered-10000-times-lawmakers-introduced-copycat-model-bills-and-why-it-matters/ (POPULAR: method)
  - https://dssgfellowship.org/lid/ (SECONDARY: LID)
  - https://volokh.com/?p=13637 (POPULAR: Corley 2008 summary)

### 4. Damaged type and printers' ornaments: who printed the anonymous books

- **Data.** Early modern books printed anonymously or with false imprints (censorship era). Images: EEBO (ProQuest) and ECCO (Gale) are **licensed**. Open subsets: Folger, Internet Archive, Google Books, BnF Gallica, and national library digitizations. The Fleuron database, now **Compositor** (University of Birmingham), extracted over 1M (some sources say 1.5M) ornament images from ECCO by computer vision and is publicly searchable.
- **Question / a find.** Link an unsigned or false-imprint book to a printer by recurring damaged sorts (individual broken letters) or cracked woodblock ornaments, with the damage progressing over time, which also dates undated editions.
- **Gap evidence.** CMU's team (Warren et al.) attributed Milton's *Areopagitica* (1644) to Matthew Simmons and Thomas Paine using damaged type across about 100 pamphlets of the 1640s. The method is new and the corpus coverage is small. Vogler et al. (arXiv 2306.07998, 2023) built a learned matcher for damaged character imprints. Compositor is used by bibliographers ad hoc. I found no systematic sweep of all anonymous ESTC items.
- **Verifier.** Strong: a distinctive break must recur across several sheets and books, and progress monotonically in time. A bibliographer confirms on originals. ESTC records printers for signed comparanda.
- **Precedent.** *Areopagitica* attribution (*Milton Studies*, 2020). The Compositor/Fleuron user community. Traditional ornament-based attribution (Maslen's Bowyer ornament stock) is the hand-made precedent.
- **Recipe.** Code: pick one decade and city with an open image base. Detect ornaments and initials (Compositor already did this for ECCO-era books), embed them, cluster, and build ornament-to-signed-printer links. For a given anonymous title, look up its ornaments. LLM: cross-reference ESTC imprints and dates, and draft the bibliographic argument. The character-level damaged-type pipeline needs a GPU and high-resolution images.
- **Cost.** The ornament route is CPU-feasible on Compositor outputs. The damaged-type route needs a GPU and image rights. Licensing is the real cost.
- **Traps.** Ornament blocks were lent, sold and copied (recut copies look alike). Type was shared between printing houses. Facsimile reprints. Image-resolution artefacts that look like damage.
- **Crowding.** `PARTLY`. CMU (Warren, Vogler, Berg-Kirkpatrick) and the Compositor team.
- **Ethics.** Clear. Licensing terms on EEBO/ECCO images apply.
- **Scores.** data_ready 2 · gap 4 · verifier 4 · cheapness 2 · payoff 3 · ethics_clear 5
- **Sources.**
  - https://www.cmu.edu/news/stories/archives/2019/november/john-milton-mystery.html (SECONDARY: CMU news)
  - https://muse.jhu.edu/article/748968 (SCHOLARLY: *Milton Studies* article)
  - https://arxiv.org/pdf/2306.07998 (SCHOLARLY: Contrastive Attention Networks for Attribution of Early Modern Print)
  - https://www.digitalhumanities.org/dhq/vol/15/1/000537/000537.html (SCHOLARLY: Fleuron, DHQ 2021)
  - https://blog.bham.ac.uk/compositor/?p=13 (PRIMARY: Compositor contents)

### 5. Unrecognized sources and borrowings in early English print (EEBO-TCP text reuse)

- **Data.** EEBO-TCP Phase I: 25,363 hand-keyed (not OCR) TEI texts from 1473–1700, CC0 since 1 Jan 2015, on GitHub, Box and the Oxford Text Archive. A clean, complete, legally free corpus.
- **Question / a find.** Passages in canonical authors (Shakespeare, Marlowe, Jonson, Milton, Donne) that align with earlier texts nobody has named as sources. Also antedatings of words and phrases against dictionary first-use dates.
- **Gap evidence.** The McCarthy–Schlueter case suggests source-hunting by software is far from exhausted. Their source was an unpublished manuscript, but the method (WCopyfind n-gram alignment) applies to the whole of print. On antedating, Fred Shapiro's ADS-L posts show individual hunters still regularly antedating OED entries from digitized newspapers.
- **Verifier.** Mechanical for the alignment (shared rare n-grams with a computable chance probability against the corpus). The scholarly judgment of "source" vs "common stock" is human. Antedating: the dated page image is the verifier (OED accepts only precisely dated citations verified from originals).
- **Precedent.** McCarthy & Schlueter (2018): WCopyfind matched George North's *A Brief Discourse of Rebellion* (1576, British Library MS) to over 20 passages across 11 Shakespeare plays. Reviewers were positive (Bevington), but the claim is still debated, so record it as `CLAIMANT`-adjacent. Shapiro antedated "journalism" to 1827 against the OED's 1833.
- **Recipe.** Code: lemmatize and normalize spelling (VARD-style), take rare 4–6-gram shingles weighted by corpus rarity, and run pairwise alignment for each target author against all texts printed earlier. Rank by the probability of the shared rare-gram cluster under a null model. LLM: filter proverbs, Bible and liturgy (common stock), check against known source studies (Bullough's *Narrative and Dramatic Sources*), and draft the note.
- **Cost.** About 1–2 GB of XML. CPU only. Hours.
- **Traps.** Proverbial and biblical language. Common sources (both texts borrowing from a third). The "parallel-passage" crank tradition in authorship questions (Oxfordian and Baconian cases ran exactly this method with weak null models). Rule 7: calibrate on known sources (Holinshed→history plays, North's *Plutarch*→*Antony and Cleopatra*) and demand that the method recovers them at a stated false-positive rate. OCR-date errors for antedating (Shapiro's "pro-life" 1989→1969 mis-OCR).
- **Crowding.** `PARTLY`. Text-reuse DH work exists (e.g. TCP-based reuse studies), and Shakespeare source study is a crowded field. Systematic sweeps for lesser authors look open.
- **Ethics.** Clear.
- **Scores.** data_ready 5 · gap 3 · verifier 3 · cheapness 5 · payoff 3 · ethics_clear 5
- **Sources.**
  - https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/5 (PRIMARY: 25,363 texts, public domain)
  - https://news.umich.edu/?p=22652 (SECONDARY: release announcement)
  - https://www.folger.edu/podcasts/shakespeare-unlimited/george-north-manuscript/ (SECONDARY: McCarthy & Schlueter)
  - https://www.bangordailynews.com/2018/02/09/news/using-plagiarism-software-nh-scholar-finds-similarities-between-shakespeare-plays-earlier-manuscript/ (POPULAR)
  - https://listserv.linguistlist.org/pipermail/ads-l/2006-June/060195.html (CLAIMANT-ish: Shapiro "journalism" antedating)
  - https://listserv.linguistlist.org/pipermail/ads-l/2022-June/161578.html (POPULAR: OCR-date trap)

### 6. Cuneiform: joins between fragments, and the untranslated tail

- **Data.** CDLI catalogue and ATF transliterations (GitHub `cdli-gh/data`, last dump Aug 2022, about 5.8 GB with LFS; newer export via cdli.earth). Licence unconfirmed. eBL Fragmentarium transliterations: a public endpoint plus a Python ATF parser, about 25,000 tablets and over 350,000 lines as of the 2024 data paper. ORACC projects (per-project licences).
- **Question / a find.** Two fragments in different museum numbers that belong to the same tablet (a "join"), or a fragment that belongs to a known composition (Gilgamesh, Enuma Elish), found by sequence alignment of transliterations.
- **Gap evidence.** The Fragmentarium (Jiménez, LMU) matched a new Gilgamesh fragment by algorithm in Nov 2022 and has reportedly matched over 1,500 pieces since 2018, including 20 Gilgamesh fragments (2024 press). The method works and the backlog is large, but the people best placed to run it are already running it on their own corpus.
- **Verifier.** Strong. An alignment of overlapping lines with an existing manuscript is checkable by any Assyriologist. A physical join needs museum photos or access.
- **Precedent.** Above (Fragmentarium/cuneiBLAST). Gutherz et al., *PNAS Nexus* 2023: Akkadian→English neural MT at BLEU4 36.5 (cuneiform) and 37.5 (transliteration), with fluent-but-wrong outputs noted.
- **Recipe.** Code: take the eBL and CDLI ATF, normalize signs, and run a local alignment (BLAST-like) of every fragment against every composite text, including *cross-corpus* hits (CDLI fragments against eBL composites), which may be the gap. LLM: a draft gloss of the aligned lines for the expert. Do not publish LLM translations as readings.
- **Cost.** CPU. Hours to a day.
- **Traps.** Formulaic and lexical texts (omen series, lexical lists, standard phrases) align everywhere. Transliteration conventions differ between projects. MT fluency is not accuracy (Gutherz et al. say so).
- **Crowding.** `CROWDED` for literary joins (eBL). `PARTLY` for cross-corpus and non-literary (archival) texts.
- **Ethics.** Mostly clear. Unprovenanced tablets on the market (looting, e.g. post-2003 Iraq) mean a "new join" can launder a looted object. Flag unprovenanced items and do not help market valuation.
- **Scores.** data_ready 4 · gap 2 · verifier 4 · cheapness 5 · payoff 3 · ethics_clear 4
- **Sources.**
  - https://github.com/cdli-gh/data (PRIMARY)
  - https://cdli.earth/postings/201 (PRIMARY: bulk data)
  - https://doaj.org/article/11c2067e19d44b0da3dd228b8faf80a6 (SCHOLARLY: eBL dataset, *JOHD* 2024, doi 10.5334/johd.148)
  - https://theconversation.com/ai-is-helping-us-read-ancient-mesopotamian-literature-205091 (POPULAR: Nov 2022 Gilgamesh fragment, written by project members)
  - https://westhawaiitoday.com/2024/08/14/hawaii-news/piecing-together-an-ancient-epic-was-slow-work-until-ai-got-involved/ (POPULAR: 1,500 matches, 20 Gilgamesh; AP syndication)
  - https://academic.oup.com/pnasnexus/article/2/5/pgad096/7147349 (SCHOLARLY: Gutherz et al. 2023)

### 7. Numismatics: automated die studies across open coin images

- **Data.** ANS MANTIS (open data ODbL, images CC BY-NC per 2017 reports, over 160k high-resolution images), with images syndicated through Nomisma/IIIF into CRRO, OCRE and PELLA type corpora. Auction archives (CoinArchives, ACSearch) are not open; their terms of service forbid scraping.
- **Question / a find.** Die links (two coins struck from the same die), which give die counts and therefore mint output estimates, and die chains that date issues. Also forgeries: modern fakes made from transfer dies share an identical "die" across museum specimens.
- **Gap evidence.** Die studies are done by hand per issue. Cornet et al. (ECCV-W 2024) and arXiv 2502.01186 (2025) build automatic die studies and a first labelled die-link dataset (329 images). The L'Isle-Jourdain hoard example has about 972k pairings for 1,395 coins, the scale that makes manual work infeasible. ANR "STUDIES" (2023) is funded for this. Thousands of open museum images have never been die-studied as one pool.
- **Verifier.** Good: a die link is confirmable by a numismatist on two images (shared flaws, letter positions). Mint-output claims need statistical die-count estimators (Esty), which are a known minefield.
- **Precedent.** The ANS CADS program (Taylor 2020 thesis, with van Alfen) on Athenian owls. The methods papers above. I found no sourced case of a new discovery from an *open-image cross-museum* sweep.
- **Recipe.** Code: pull IIIF images for one type (e.g. a CRRO RRC number with 50+ specimens), segment the coin, do local-feature matching (SIFT/SuperPoint plus RANSAC) or SSIM, and cluster. LLM: look up type metadata and write the human-review queue.
- **Cost.** CPU feasible for hundreds of coins per type. GPU helps.
- **Traps.** Same-type, different-die coins look very alike. Wear and lighting differences. Duplicate photos of the *same coin* in two collections (provenance duplicates, not die links; though finding those is itself useful for provenance). Esty-style die-count extrapolations are fragile.
- **Crowding.** `PARTLY`. CEA/Paris-Saclay (Cornet), ANS (CADS), ANR STUDIES.
- **Ethics.** Mostly clear on museum data. Avoid auction data (terms of service), and avoid producing authentication verdicts on market coins (commercial and legal exposure, laundering).
- **Scores.** data_ready 3 · gap 3 · verifier 4 · cheapness 3 · payoff 3 · ethics_clear 4
- **Sources.**
  - https://mlanthology.org/eccvw/2024/cornet2024eccvw-automatic (SCHOLARLY)
  - https://arxiv.org/abs/2502.01186v1 (SCHOLARLY: SSIM die-link dataset)
  - https://arxiv.org/html/2407.20876v1 (SCHOLARLY)
  - https://anr.fr/Project-ANR-23-CE38-0014 (PRIMARY: ANR STUDIES)
  - https://numismatics.org/pocketchange/cads/ (PRIMARY: ANS CADS)
  - https://coinweek.com/ans-introduces-160000-high-resolution-downloadable-images (POPULAR)
  - https://coinbooks.org/v20/esylum_v20n34a16.html (POPULAR: CC BY-NC, ODbL)

### 8. War dead missing from the commemorative registers

- **Data.** CWGC Find War Dead (web export to CSV via "Download Results"; one user reports a limit of about 20k rows). Comparator: Library and Archives Canada's CEF personnel files, **all 622,290 digitized** (about 30M pages, free to view; service file PDF plus attestation JPEG). Australian (NAA B2455) and NZ files are similar.
- **Question / a find.** Service members who died in service within the CWGC qualifying window (to 31 Aug 1921 for WWI) but are not commemorated. Typically deaths after discharge from war-attributable causes, or deaths in Canada. The CWGC accepts such cases with evidence.
- **Gap evidence.** The In From The Cold Project has existed for over 20 years and reports over 8,000 cases processed. That proves the gap exists and is not closed. I found no figure for how many were accepted (the IWM community pages list accepted cases).
- **Verifier.** Excellent and institutional: CWGC/MoD adjudication against published criteria, plus the service file's own death documentation.
- **Precedent.** IFCP accepted cases (Lives of the First World War communities).
- **Recipe.** Code: the hard part is that the CEF files are images. Use the LAC database's indexed fields (name, regimental number, birth date). Death and discharge dates are in the PDFs and need OCR or HTR of typed and handwritten forms. Candidate set: soldiers whose file contains a death date in the window, minus CWGC matches by name and service number. LLM: read the handwritten death or discharge pages (HTR plus LLM reading) and prepare the IFCP-style evidence pack. A human submits.
- **Cost.** Bulk download of about 600 TB of PDFs is impossible. Work on targeted subsets (e.g. files flagged "deceased" in the index). Days of work, modest dollars.
- **Traps.** Name and number mismatches (re-enlistments under new numbers; LAC linked multiple files). Deaths outside the window. Already-submitted IFCP cases, so coordinate with IFCP first to avoid duplicate submissions. This is a crowded volunteer niche with good practice.
- **Crowding.** `CROWDED`/`PARTLY`: In From The Cold Project (UK-led, all Commonwealth). Its methods are largely manual, so a compute assist is a contribution *to* them, not around them.
- **Ethics.** Positive purpose. Next-of-kin may be living descendants. Medical details in service files (VD, psychiatric) are sensitive: do not publish them, only submit evidence.
- **Scores.** data_ready 3 · gap 3 · verifier 5 · cheapness 3 · payoff 3 · ethics_clear 4
- **Sources.**
  - https://infromthecold.org/ (PRIMARY: project, 8,000+ cases)
  - https://livesofthefirstworldwar.iwm.org.uk/community/7533/ (PRIMARY: accepted cases)
  - https://www.infodocket.com/2018/08/15/library-and-archives-canada-announces-completion-of-canadian-expeditionary-force-digitization-project-approximately-30-million-pages-digitized/ (SECONDARY: 622,290 soldiers)
  - https://www.bac-lac.gc.ca/eng/discover/military-heritage/first-world-war/personnel-records (PRIMARY)
  - https://www.greatwarforum.org/topic/309385-cwgc-excel-spreadsheet-version-cemetery-lists/ (POPULAR: CSV export)

### 9. Baseball's official record vs. the reconstructed record

- **Data.** Retrosheet: box scores for 221,443 games, event files for 205,886 (including 5,186 "deduced"), and discrepancy files against official totals back to 1915. Free use with a credit line. Plus Negro Leagues data (deduced play-by-play), now part of MLB's official record since 2024 (Unverified, see below). Newspaper box scores in Chronicling America.
- **Question / a find.** Official season totals (hits, RBI, runs) that are wrong because of a ledger error, so that a record, batting title or milestone changes.
- **Gap evidence.** Retrosheet "always ends up with a few dozen differences" per season that it cannot reconcile. They are published and unresolved. Retrosheet's working assumption is that it, not the official record, is wrong, but Ruane notes that "in many cases the official view is pretty obviously wrong." Pre-1915 discrepancy work is incomplete.
- **Verifier.** Good: multiple independent newspaper box scores and game stories for the disputed game, plus the official day-by-day ledger. Acceptance by MLB is political and slow.
- **Precedent.** Hack Wilson's 1930 RBI total raised from 190 to 191 by MLB in June 1999, after James Braswell found in 1977 that a 28 July 1930 RBI had been credited to Charlie Grimm. Verified from four newspapers and the AP box score. SABR's study of corrections to Tigers runs scored, 1945–2007.
- **Recipe.** Code: take the discrepancy files, rank by "would change a leaderboard or milestone", then pull Chronicling America OCR (to 1963) for the specific game dates and parse box-score lines. LLM: read the game story and decide which player drove in or scored. Code tallies.
- **Cost.** Trivial.
- **Traps.** Scoring-rule differences by era (the 1931 RBI rule change), newspaper box-score errors that propagate (wire copies are not independent sources), and the Ty Cobb 1910 batting-title controversy as a cautionary tale of decades of re-litigation.
- **Crowding.** `CROWDED`. Retrosheet and SABR volunteers are expert and active. A compute assist on newspaper parsing is the only lane.
- **Ethics.** Clear (historical public figures).
- **Scores.** data_ready 5 · gap 2 · verifier 4 · cheapness 5 · payoff 2 · ethics_clear 5
- **Sources.**
  - https://sabr.org/journal/article/hack-wilsons-191st-rbi-a-persistent-itch-finally-scratched/ (SECONDARY)
  - https://archive.seattletimes.com/archive/19990623/2968014/hack-wilsons-rbi-total-raised-to-191 (POPULAR)
  - https://retrosheet.org/Research/RuaneT/rev1930_art.htm (SECONDARY)
  - https://www.retrosheet.org/faq.htm (PRIMARY: discrepancy policy)
  - https://www.retrosheet.org/downloads/csvdownloads.html (PRIMARY: counts, terms)
  - https://sabr.org/journal/article/the-authorized-correction-of-errors-in-runs-scored-in-the-official-records-1945-2007-for-detroit-tigers-players/ (SECONDARY)

### 10. The scientific literature as a dataset of errors (seed; mostly crowded)

- **Data.** PubMed Central OA subset (full text and supplementary files, bulk FTP), Crossref metadata, and the Retraction Watch database (now open via Crossref).
- **Question / a find.** Mechanical inconsistencies: gene names corrupted into dates in supplementary Excel files, impossible means (GRIM), p-value and statistic mismatches (statcheck), tortured phrases (paper mills), duplicated images.
- **Gap evidence.** Ziemann et al. 2016: 987 supplementary files from 704 articles out of 35,175 files had gene-name errors. The 2021 follow-up found 30.9% (3,436/11,117) of articles with Excel gene lists affected, "accumulating unabated". The Problematic Paper Screener sweeps about 130M papers weekly and has helped drive more than 1,000 retractions. **The open lane:** the same spreadsheet-autocorrect damage in *other* identifier systems (e.g. chemical CAS numbers, plant or species codes, SNP/locus IDs, sample IDs like "1-2" becoming dates) in other fields' supplements. I found no study of these, but did not search exhaustively. See Unverified.
- **Verifier.** Mechanical (the corrupted string is a deterministic Excel transform of a valid identifier).
- **Precedent.** As above. Also HGNC renamed SEPT1→SEPTIN1 and MARCH1→MARCHF1 in response.
- **Recipe.** Code: download PMC OA supplementary .xlsx files for one non-genomics field. For each column, test whether values look like Excel date serials or date strings *and* the column's other values are valid IDs of a known scheme. LLM: classify column semantics and write the report.
- **Cost.** CPU. Tens of GB of downloads.
- **Traps.** Legitimate dates. Already-flagged papers. Naming authors (see ethics).
- **Crowding.** `CROWDED` (Bik, Cabanac/PPS, statcheck, Ziemann, ImageTwin, Retraction Watch). Non-genomic spreadsheet corruption is possibly `OPEN`.
- **Ethics.** Errors are not misconduct. Report to journals and authors, aggregate publicly. Paper-mill accusations against named individuals need care.
- **Scores.** data_ready 5 · gap 2 · verifier 5 · cheapness 5 · payoff 2 · ethics_clear 4
- **Sources.**
  - https://pmc.ncbi.nlm.nih.gov/articles/5359807 (SCHOLARLY: Ziemann et al. 2016)
  - https://doaj.org/article/8b429b7b5d454a8c9aeef110207e3418 (SCHOLARLY: "Gene name errors: lessons not learned", *PLoS Comp Biol* 2021)
  - https://retractionwatch.com/2023/09/20/guest-post-genomics-has-a-spreadsheet-problem (POPULAR)
  - https://arxiv.org/pdf/2210.04895 (SCHOLARLY: Problematic Paper Screener)
  - https://univ-grenoble-alpes.fr/news/the-conversation/the-conversation-problematic-paper-screener-trawling-for-fraud-in-the-scientific-literature--1547580.kjsp (POPULAR: 130M papers weekly)

---

## Pilot in a day

**RISM anonymous-incipit sweep (candidate 1).** It is CPU-only and uses CC-BY data. The verifier comes in two stages: first a mechanical multi-movement match, then expert review. Known positives (the Vivaldi RV 241 Durham parts; the Brescianello/Vivaldi pasticcio) give a calibration check before any new claim (Rule 7).

1. **Get the data.** Start at https://rism.info/community/data-services.html and the linked-open-data page described in https://rism.info/rism_online_catalog/2015/04/16/rism-data-as-open-data-and-linked-open-data.html (the full MARC XML dump historically lived under opac.rism.info). If the bulk dump has moved, use the RISM Online API (https://rism.online/docs/api/incipit-search/) and page through sources. *I could not resolve rism.info from this container, so confirm the current dump URL first.* Put the downloads in their own directory under `puzzles/` or the scratchpad, and run Python with `-I`.
2. **Parse.** Use stdlib `xml.etree.iterparse` over MARC field `031` (subfields: `p` PAE notes, `g` clef, `n` key, `o` time signature, and `a`/`b`/`c` work, movement and incipit numbers) and field `100` (composer, or "Anonymus").
3. **Normalize.** Convert PAE to an absolute pitch sequence, then to an interval sequence, dropping rests, grace notes and ornaments. Keep a coarse duration ratio sequence.
4. **Index.** Build an inverted index of interval 7-grams (transposition-invariant). Down-weight n-grams that occur in more than *k* works (generic openings).
5. **Match.** For each anonymous source, score attributed candidates with a local alignment of the full incipit. **Require two or more movements of the same source to match movements of the same attributed work.** That is the false-positive filter.
6. **Calibrate.** Confirm that the pipeline recovers RV 241 (Durham) and the Brescianello/Vivaldi movement. Record the recall, and the hit rate on a shuffled-composer null.
7. **Output.** A CSV of ranked candidate attributions, checked into `analysis/` with the script (Rule 6). The LLM writes a one-paragraph case note for the top 20. Nothing is published as an attribution until a musicologist or RISM confirms it.

## Unverified claims

- RISM licence version (CC-BY 3.0 vs 4.0) and the current bulk-dump URL. rism.info did not resolve from this container. Figures (1.7M incipits, 200k anonymous) come from search summaries of RISM pages.
- Whether anyone has already published a full all-pairs RISM anonymous-incipit sweep. Absence was not demonstrated, only not found.
- LOCOMAT pages (locomat.loria.fr) were not directly fetchable. The Bürgi sin 4° detail and the Babbage/Callet note come from search-result summaries of Roegel's PDFs.
- The "13 tables / 6 shared errors" figure for Babbage 1827 comes from a POPULAR page quoting Babbage. The primary text was not checked.
- The Fragmentarium figures (1,500+ matches, 20 Gilgamesh fragments) are press figures (AP 2024). The "cuneiBLAST" name is from a search summary.
- CDLI data licence: not found.
- ANS image licence (CC BY-NC 4.0) is from 2017 reports. Current terms are not checked.
- That forgeries have been detected by die-matching museum and auction coins against known fake dies. I recall this from collector practice (forgery reference sites) but found no source.
- CWGC export row limit (about 20k), from one forum user.
- The In From The Cold Project's count of *accepted* cases was not found (only "8,000+ processed").
- That Negro Leagues statistics (1920–48) entered MLB's official record in 2024. From memory; not verified this session.
- EEBO-TCP Phase II public release (I recall 2020). Not verified; the Oxford page found says Phase II access is restricted.
- The non-genomic spreadsheet-corruption gap in candidate 10 is a conjecture. No search was done for prior studies in chemistry or ecology.
- Hallucination-database counts (1,598 worldwide) come from a POPULAR vendor blog citing Charlotin. The database itself was not opened.
- Citation Lookup rate limits come from a third-party guide.

## Raw ideas considered

| # | Idea | Kept / dropped, why |
|---|---|---|
| 1 | RISM anonymous music incipits | **Kept (#1)**: open data, mechanical first pass, precedent |
| 2 | Shared errors in printed math tables | **Kept (#2)**: perfect verifier, Babbage precedent |
| 3 | Hallucinated citations in RECAP filings | **Kept (#3)**: unflagged-filing gap; ethics managed by aggregate reporting |
| 4 | Model-bill copying in state legislation | Folded into #3: `CROWDED` (USA Today, LID) |
| 5 | Judges copying briefs or proposed orders | Folded into #3: Corley and Feldman did it |
| 6 | Damaged type and ornaments → printers | **Kept (#4)**: CMU precedent; image licensing is the wall |
| 7 | EEBO-TCP source and borrowing detection | **Kept (#5)**: CC0 clean text |
| 8 | OED/Wiktionary antedating from Chronicling America | Folded into #5: verifier fine, payoff small, ADS-L crowd |
| 9 | Cuneiform joins (CDLI/eBL) | **Kept (#6)**: crowded by eBL itself |
| 10 | Akkadian MT of untranslated tablets | Folded into #6: no verifier for translation quality without experts |
| 11 | Coin die studies on open images | **Kept (#7)** |
| 12 | Coin and medal forgery detection via shared transfer dies | Folded into #7: no sourced precedent found |
| 13 | CWGC vs CEF/AIF service files | **Kept (#8)**: institutional verifier |
| 14 | Retrosheet discrepancies vs newspapers | **Kept (#9)**: crowded but clean verifier |
| 15 | Science literature errors (GRIM, statcheck, PPS, images) | **Kept (#10)** as `CROWDED`, with a narrower open lane |
| 16 | Clinical-trial registry vs publication (unreported results, outcome switching) | Dropped: `CROWDED` (TrialsTracker, COMPare); verifier good but the space is swept |
| 17 | Museum open-access images: same object in two museums / forgeries | Dropped: verifier weak (needs physical exam); provenance-duplicate detection noted under #7 |
| 18 | Nazi-era provenance gaps (Lost Art, museum provenance pages) | Dropped: legal exposure, claims involve living heirs; verifier is archival and slow |
| 19 | Chronolocation of undated archive photos (LoC) | Dropped: verifier is soft (shadow-dating error bars), and the payoff is per-photo; also borders on file 04 OSINT |
| 20 | Unidentified WWII aircraft wrecks or soldiers' remains | Dropped: next-of-kin ethics; overlaps file 01 remote sensing; verification needs DNA |
| 21 | IPUMS full-count census: enumerator fabrication (curbstoning) | Dropped: IPUMS terms forbid redistribution; the payoff tends toward naming individuals (enumerators) |
| 22 | Age-heaping and demographic anomalies in historical censuses | Dropped: well studied (demography literature), little "discovery" |
| 23 | Lottery winner data (repeat-winner fraud) | Dropped: payoff is identifying private individuals (brief rule) |
| 24 | Benford tests on election returns | Dropped: crank-dominated field; Benford is not a valid fraud test for elections |
| 25 | SEC XBRL filings: internal arithmetic inconsistencies | Dropped for this file: plausible and mechanical, but closer to financial OSINT; harm to living people; academic and regulator crowd |
| 26 | Historical map stemmatics via shared phantom features (copy traps, phantom islands) | Dropped: map georeferenced corpora too small and noisy; verifier is judgment |
| 27 | Philately: plate reconstruction (plating) by plate flaws | Dropped: open images scarce; a niche already served by specialist software and societies |
| 28 | Typewriter or typeface forensics in archival typescripts | Dropped: no open corpus; drifts toward identifying individuals |
| 29 | Watermark databases (Bernstein, WZIS) for paper dating | Dropped: data partly open, but matching needs beta-radiographs not in public scans |
| 30 | Epigraphy: joining Greek or Latin inscription fragments (PHI, EDH) | Dropped: PHI texts not openly licensed for bulk use; Ithaca (DeepMind) covers restoration and attribution; joins need stone measurements |
| 31 | Ship-loss registers (Lloyd's List) vs wreck databases | Dropped: Lloyd's digitization is licensed; overlaps file 01 bathymetry wrecks |
| 32 | Patent full text: inventions anticipated in old patents ("prior art discovery") | Dropped: no clean verifier of novelty; commercial crowd |
| 33 | Historical recipe and cookbook text reuse | Dropped: low payoff; the same method as #5 |
| 34 | Hymn-tune and folk-tune families (Bronson, Roud index) | Dropped: overlaps #1 method; Roud index licensing unclear |
| 35 | Place-name databases (GNIS/GeoNames) with impossible or ghost features | Dropped: payoff is data cleaning, not discovery |
| 36 | Old phone directories → historical business geography | Dropped: privacy and no clear question |
| 37 | Architectural drawings (HABS/HAER) ↔ standing buildings | Dropped: no defined find; verifier is a site visit |
| 38 | Sports: cricket and football historical scorecards (CricketArchive) | Dropped: data licensed; Retrosheet is the cleaner analogue |
| 39 | Sheet-music OCR (IMSLP) for unattributed arrangements | Dropped in favour of #1: RISM already has encoded incipits; OMR noise is a trap |
| 40 | Medieval charters: forged-charter detection by formulae | Dropped: belongs to file 05 (documents/archives) |
