# 06 — Wild cards: culture, consumer/open-government data, software, mathematics

*Survey, 2026-10-15. Brief: `sources/untouched-data/BRIEF.md`. No discoveries attempted (Rule 9).
Container note: from this session's network proxy, oeis.org, api.fda.gov, download.open.fda.gov,
static.nhtsa.gov, database.lichess.org, dumps.wikimedia.org, huggingface.co and icpsr.umich.edu all
returned 403. GitHub raw/git was reachable. That shaped the pilot choice.*

## Summary (best bets)

1. **Mathematics is where this domain has a verifier, and it is the only place here that does.** OEIS holds
   ~13.6k sequence entries with a "Conjecture" in a comment line. Many were checked only as far as the author's b-file.
   A173419 is the template: a conjecture "true for n < 1800" fails at p = 3359 (found Aug 2026).
2. **Erdős problems: real, but `CROWDED`, and the trap there is the literature, not the math.** 40 of 1,221 problems
   are tagged as settleable by finite computation. Since Oct 2025 the main discovery mode has been "this was
   already solved in a paper nobody linked." Do the literature search before you compute.
3. **Consumer and government complaint data (NHTSA, reviews, FAERS/MAUDE) has strong precedent but a weak hobbyist verifier.** The verifier is a
   recall or a health-department inspection, which only an agency can trigger. FAERS is `CROWDED` by paper mills.
   NHTSA complaints are the least bad of these. Don't name a company in public until the agency has acted (defamation risk).
4. **Fan fiction is honestly a weak lead.** The legal dataset is AO3's 2021 metadata dump. There is no ground truth for trope
   diffusion, and the community is actively hostile to scraping. The only fact you could check is training-data contamination, which
   is a fact about LLMs, not about culture. Authorship deanonymization is excluded.
5. **Low payoff or saturated:** chess novelties, EDGAR Benford sweeps, Open Payments, game datamining (TCRF), folk-tune families. Endangered-language
   audio is high value, but the verifier is the community, and the work is transcription, not discovery.

---

### 1. OEIS conjectures checked only to the edge of their own b-file

- **Data.** OEIS Foundation; reference database of integer sequences; ~400,313 entries in the Git export
  dated 2026-10-15T03:00 (`github.com/oeis/oeisdata`, `seq/AXXX/AXXXXXX.seq`, internal format; b-files under
  `files/`). Sparse shallow clone of `seq/` is ~2.0 GB. License CC BY-SA 4.0 (repo README).
- **Question / what a find looks like.** A `%C`/`%F` line saying "Conjecture: … (verified for n <= N)". The find is
  either a counterexample beyond N or an extension of the verified range with the bound stated. A secondary find is
  a b-file term that disagrees with the program in `%p`/`%o` (an erratum).
- **Gap evidence.** Grep over the 2026-10-15 export (method in Pilot): 26,687 `%C`/`%F` lines mention "conjecture",
  spread over 13,632 entries. 1,264 of those lines carry a "verified/checked/true for/holds for/tested" qualifier, i.e. a
  stated finite range. 412 lines already mention a disproof, counterexample or "false". Those must be excluded.
  The formal benchmark covers only 492 of them (OEIS Open). A173419: Kamenetsky's 2019 conjecture
  was "true for n < 1800", exactly the b-file length, and failed at p = 3359 (Patanè, Aug 2026, HAL preprint, now in the entry).
- **Verifier.** Mechanical: an independent program reproduces the counterexample. For the ~492 formalized ones, a
  Lean proof of the negation. Final arbiter is the OEIS editors, who accept the comment.
- **Precedent.** A173419 counterexamples (2026, computations scripted with help from Claude, per search
  summary). A242463 "no primes" conjecture disproved when a(39) was prime. OEIS Open benchmark: LMs settled 147/492
  formalized conjectures at $50/attempt, and 160 cumulatively. Adding 476k arXiv papers as context did not help.
- **Recipe.** Code: parse `.seq` files and extract conjecture lines with a stated range. An LLM classifies each line as
  finite-checkable / asymptotic / vague and drafts a checker from the `%o` program. Code then runs the checker from N to
  10·N or 100·N. An LLM only triages and drafts; correctness comes from cross-checking two independent implementations.
  Hits are submitted as OEIS comments.
- **Cost.** Laptop. Clone ~2 GB, triage a few thousand lines with an LLM at a few dollars, CPU hours per candidate.
- **Traps.** Off-by-one/offset conventions (`%O`). Conjectures already refuted in a later comment, or in a linked sequence.
  Floating-point checkers. "Verified to N" claims that were never true (bug in the original). Counterexamples
  that are trivial because the conjecture was misread. Significance: most of these are curiosities. The
  OEIS Open author says so too.
- **Crowding.** `PARTLY`. The 492 formalized conjectures are a public benchmark that labs and Epoch AI run. The
  unformalized ~13k are not swept systematically, as far as the search found.
- **Ethics.** Clear. Etiquette: OEIS editors are volunteers, so batch-submitting LLM-written comments would be a harm. Submit
  only verified items, with code.
- **Scores.** data_ready 5 · gap 4 · verifier 5 · cheapness 5 · payoff 2 · ethics_clear 5
- **Sources.**
  - https://raw.githubusercontent.com/oeis/oeisdata/main/README.md — PRIMARY (license, layout)
  - https://raw.githubusercontent.com/oeis/oeisdata/main/seq/A173/A173419.seq — PRIMARY (conjecture to 1800; counterexample 3359)
  - https://hal.science/hal-05756029/ — CLAIMANT (Patanè counterexamples; cited in entry, not fetched)
  - https://arxiv.org/pdf/2608.11941 — SCHOLARLY preprint (OEIS Open: 147/492; via search summary, arXiv fetch failed)
  - https://groups.google.com/g/seqfan/c/gbb7MKvandc — CLAIMANT (author's 160/492 cumulative)
  - https://oeis.org/A242463 — PRIMARY (via search summary)

### 2. Erdős problems: finite-computation cases plus literature reconciliation

- **Data.** `teorth/erdosproblems`, `data/problems.yaml` (416 KB, fetched), a community mirror of erdosproblems.com
  (T. Bloom). Formal statements: `google-deepmind/formal-conjectures`. 1,221 problems.
- **Question.** (a) The 25 "falsifiable", 8 "decidable" and 7 "verifiable" problems (40 total, computed from the YAML;
  STATISTICS.md agrees) can be settled by finite computation. (b) A problem marked "open" may already be solved in
  the literature.
- **Gap evidence.** 589 problems carry status `open` in the YAML. 248 problems are "potentially related to an OEIS sequence"
  but unlinked. On 2026-10-06 erdosproblems.com stopped displaying statuses and solve counts, and the AI-contributions
  wiki has been frozen since 2026-06-30. So the gap is real, and so is the community's fatigue with AI scoreboarding.
- **Verifier.** Lean (864 statements formalized). Bloom and the forum for literature claims.
- **Precedent.** Oct 2025: OpenAI staff claimed GPT-5 "found solutions to 10 previously unsolved Erdős problems".
  Bloom: it found references "I personally was unaware of." The post was deleted. This is the trap, and it is also a real
  service: literature search has its own section in Tao's wiki (~84 entries). Google's Aletheia study ran ~700 "open"
  problems and resolved 13; 8 of the 13 were already in the literature. #728 (Jan 2026, GPT-5.2 Pro + Aristotle Lean) is called
  the first autonomous AI solution with no prior literature found. #281 is disputed.
- **Recipe.** Code: filter the YAML for falsifiable/decidable/verifiable. An LLM does a literature sweep first (MathSciNet/zbMATH/arXiv
  citations of the source paper). Code runs a bounded search and cross-checks it. If a proof is involved, an LLM drafts
  Lean, which mathlib checks. Post to the problem's forum thread.
- **Cost.** $0–$200 per problem in tokens. CPU for the computations, which can be heavy: these problems are tagged finite
  because they are hard finite.
- **Traps.** Claiming novelty for something already published (this has happened repeatedly to OpenAI, Google and hobbyists). Ambiguous
  statements (11 tagged). Lean formalizations that do not match the intended statement. Subconscious reproduction from
  training data.
- **Crowding.** `CROWDED`. Every frontier lab, Epoch, and an "Erdosproblems-llm-hunter" site linked from each row.
- **Ethics.** Clear. The cost falls on community attention, which is why the site de-emphasized scores.
- **Scores.** data_ready 5 · gap 2 · verifier 5 · cheapness 4 · payoff 3 · ethics_clear 5
- **Sources.**
  - https://raw.githubusercontent.com/teorth/erdosproblems/main/README.md — PRIMARY (policy change 2026-10-06; wiki frozen)
  - https://raw.githubusercontent.com/teorth/erdosproblems/main/STATISTICS.md — PRIMARY (counts)
  - https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems — PRIMARY (categories, caveats)
  - https://www.eweek.com/news/openai-math-hype/ — POPULAR (Oct 2025 episode, Bloom quote)
  - https://arxiv.org/pdf/2601.22401v2 — SCHOLARLY preprint (Aletheia: 13 resolved, 8 already in literature)
  - https://arxiv.org/pdf/2601.07421 — SCHOLARLY preprint (#728 writeup)

### 3. Historical mathematical tables: errata by recomputation

- **Data.** Printed tables of logs, trig functions, primes and factors (1600s–1950s), digitized by Google Books, the Internet Archive
  and HathiTrust. Reconstructions by D. Roegel's LOCOMAT project (locomat.loria.fr, PDFs).
- **Question.** Recompute every entry and list the errors. Trace which tables copied which errors. That is a
  provenance and stemmatics question about who copied whom, which matters to this repo.
- **Gap evidence.** Error propagation is documented: a 1973 erratum to the Fletcher–Miller–Rosenhead *Index* traced an
  error back to Airey 1935. Abramowitz & Stegun Table 27.5 had 11 terminal-digit errors found by recomputation. LOCOMAT
  covers many tables, but not all of them. Gap size: unverified.
- **Verifier.** Perfect: recompute in arbitrary precision. The OCR is the weak link; check against the page image.
- **Precedent.** LOCOMAT error analyses (Bürgi's sine table: a copying error at sin 4°, a rounding error at 6°10′). The
  *Math. Comp.* "Table Errata" section ran for decades.
- **Recipe.** OCR digits with code and check them against recomputation. An LLM only reads the headers and layout. Code diffs every cell.
  Errors cluster by printer and edition, and the clustering is the stemma.
- **Cost.** Laptop. OCR of dense numeric tables is the time sink.
- **Traps.** OCR errors masquerading as table errors. Deliberate "trap" errors inserted to detect copying (rumored, so check).
  Different rounding conventions.
- **Crowding.** `PARTLY` (Roegel, essentially one person, highly productive).
- **Ethics.** Clear.
- **Scores.** data_ready 3 · gap 3 · verifier 5 · cheapness 4 · payoff 2 · ethics_clear 5
- **Sources.**
  - https://www.ams.org/mcom/1973-27-124/S0025-5718-73-99697-X/S0025-5718-73-99697-X.pdf — SCHOLARLY (via search summary)
  - https://www.ams.org/mcom/1965-19-089/S0025-5718-65-99955-2/ — SCHOLARLY (table errata)
  - https://locomat.loria.fr/buergi-sines/roegel2016buergi-sine-table1.pdf — SCHOLARLY (Roegel)

### 4. NHTSA complaints: prospective early-defect detection

- **Data.** NHTSA Office of Defects Investigation consumer complaints. Free-text narrative plus make/model/year/component, flat file
  `FLAT_CMPL.zip` (field spec at static.nhtsa.gov/odi/ffdd/cmpl/CMPL.txt; older host www-odi.nhtsa.dot.gov). Public
  domain (US government). Multi-GB unzipped (2015 import guide: ≥2 GB).
- **Question.** Which make/model/component pairs are now running above baseline, with narratives describing a
  common failure mechanism, and have no open investigation or recall?
- **Gap evidence.** GM ignition switch: complaints about shutdowns arrived about twice a month from Feb 2003. A House report said NHTSA
  had enough to act by 2007. In 2015 NHTSA admitted its staff had framed the problem as an airbag problem. The 2015 IG also found
  no formal statistical analysis of early-warning data.
- **Verifier.** Weak for an outsider. Only a later ODI investigation or recall confirms a signal, on a horizon of months to years. A
  retrospective backtest against `FLAT_RCL` (recalls) is a usable proxy.
- **Precedent.** An ESV-conference paper (Jones et al.) detected pre-recall excess for 19/24 recalled vehicles with a "mean
  7.43-year lead" time. That is retrospective, and hindsight-tuned (CLAIMANT). Abrahams et al. 2012 on forum mining.
- **Recipe.** Code: rolling complaint rates per (model, component) normalized by sales/fleet. An LLM clusters the narratives
  into failure mechanisms and spots one mechanism hidden under several component codes. That miscoding is exactly what
  hid the GM case. Output: a petition to ODI (a defect petition under 49 CFR 552 is the public channel; unverified detail).
- **Cost.** Laptop. Token cost for narrative clustering of one model-year cohort: tens of dollars.
- **Traps.** Media-stimulated complaint spikes. Fleet-size confounding. Lawyer-driven complaint campaigns. Backtests tuned
  on known recalls (the 7.43-year lead is the canonical overfit).
- **Crowding.** `PARTLY`: NHTSA's own contractors (KBR SmarTxT), automakers' warranty analytics, plaintiffs' firms.
- **Ethics.** Defamation and market risk: don't publish "Model X kills people" from complaint counts. Send it to ODI, not to a blog.
  Complaint narratives can contain PII (it is redacted, but not perfectly). Do not try to contact complainants.
- **Scores.** data_ready 4 · gap 3 · verifier 2 · cheapness 4 · payoff 4 · ethics_clear 3
- **Sources.**
  - https://catalog.data.gov/dataset/nhtsas-office-of-defects-investigation-odi-complaints-complaints-flat-file — PRIMARY
  - https://static.nhtsa.gov/odi/ffdd/cmpl/CMPL.txt — PRIMARY (format; via search summary)
  - https://www.industryweek.com/safety/us-auto-regulator-admits-failures-gm-ignition-switch-case — POPULAR
  - https://www.cbsnews.com/news/gm-recall-scathing-report-says-regulators-missed-chance-to-correct-faulty-switch-issue — POPULAR
  - https://static.nhtsa.gov/esv/pdf/ESV/Proceedings/28/ESV26-289.pdf — CLAIMANT (retrospective detection)

### 5. Consumer reviews as a food-safety signal

- **Data.** Yelp Open Dataset (academic license; restaurant reviews, a subset of cities). Amazon review corpora (research
  releases, e.g. McAuley lab). Live Google/Yelp reviews are off-limits by ToS.
- **Question.** Clusters of "got sick after eating X" reviews for one restaurant or product lot that were never reported.
- **Gap evidence.** NYC pilot: only ~3% of the illnesses described in reviews had been reported to the health department. Amazon
  study: the model flagged >20,000 reviews, mostly on non-recalled products. The authors suggest some of those should have been investigated.
- **Verifier.** A health department. It interviews reviewers and inspects (NYC: 3 outbreaks, 16 illnesses, violations confirmed). A
  hobbyist cannot do this. For packaged food, an FDA/USDA recall later is the proxy.
- **Precedent.** MMWR 2014 (NYC DOHMH + Columbia + Yelp): 294k reviews → 893 flagged → 3 unreported outbreaks. JAMIA
  Open 2019 (Amazon, BERT F1 0.74). A 2025 arXiv preprint: LLMs reach >90% micro-F1 classifying Yelp GI reviews.
- **Recipe.** An LLM classifies the reviews (this is now solved). Code does space-time clustering per business. The output goes to a
  health department, never to the public.
- **Cost.** Cheap.
- **Traps.** Norovirus from other sources blamed on the last meal eaten. Fake or competitor reviews. Base rates (a big restaurant
  gets more "sick" reviews). Historical open datasets mean the outbreak is long over, so there is nothing to act on.
- **Crowding.** `CROWDED` as a method (health departments in NYC and Chicago, among others, run it operationally). Open as a hobbyist
  discovery only in the sense of a retrospective paper.
- **Ethics.** Naming a small business publicly is defamation and harm. Reviewers are private individuals. Payoff is
  public health, but only through an agency.
- **Scores.** data_ready 3 · gap 2 · verifier 2 · cheapness 5 · payoff 2 · ethics_clear 2
- **Sources.**
  - https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6320a1.htm — SCHOLARLY (MMWR)
  - https://stacks.cdc.gov/view/cdc/29244/cdc_29244_DS1.pdf — SCHOLARLY
  - https://www.bu.edu/sph/news/articles/2019/ai-can-predict-product-recalls-from-customer-reviews — POPULAR (JAMIA Open study)
  - https://arxiv.org/abs/2503.09743v1 — SCHOLARLY preprint (LLM classification)

### 6. FAERS / MAUDE disproportionality: listed as a warning

- **Data.** openFDA (drug/event ~20M+ reports, device/event ~24M+ per third-party counts, unverified). Bulk JSON
  partitions listed in a manifest (`api.fda.gov/download.json`, per openFDA docs). MAUDE quarterly pipe-delimited files.
  FDA notes MAUDE moving to AEMS in 2026 (status unverified).
- **Question.** Drug–event or device–failure pairs reported disproportionately often (PRR/ROR/EBGM) and not on the label.
- **Gap evidence.** Weak. The gap is in quality, not coverage.
- **Verifier.** Only pharmacoepidemiology (cohort studies) or an FDA label change, which takes years. Disproportionality is hypothesis-generating.
  openFDA itself says "assume all results are unvalidated."
- **Precedent (negative).** Retraction Watch, Sept 2025: *Expert Opinion on Drug Safety* published 174 FAERS
  disproportionality papers in 2024 (~60% of its output) and then banned them. Frontiers in Pharmacology went from ~30 to >120 such papers and now requires
  external validation. A preprint describes these papers as hard to distinguish from paper-mill output.
- **Recipe.** Don't. If anyone does: code computes the statistics; an LLM reads narratives (MAUDE free text) for mechanism. Pre-register.
- **Cost.** Cheap, which is the problem.
- **Traps.** Stimulated reporting after news or FDA alerts. Notoriety bias. Duplicates. Masking. Indication confounding. Sham-alert
  studies show reporting trends that look the same as after real alerts.
- **Crowding.** `CROWDED` (FDA, EMA, industry, paper mills).
- **Ethics.** False safety scares cause real harm (people stop taking needed drugs). Company defamation.
- **Scores.** data_ready 5 · gap 1 · verifier 1 · cheapness 5 · payoff 2 · ethics_clear 2
- **Sources.**
  - https://retractionwatch.com/2025/09/16/exclusive-journal-bans-drug-safety-database-papers-as-they-flood-the-literature — POPULAR
  - https://zenodo.org/records/17116885 — SCHOLARLY preprint
  - https://link.springer.com/article/10.1007/s40264-014-0225-0 — SCHOLARLY (sham alerts)
  - https://open.fda.gov/about/updates/2015_12_23_direct_downloads — PRIMARY (downloads; via search summary)
  - https://www.fda.gov/medical-devices/medical-device-reporting-mdr-how-report-medical-device-problems/mdr-data-files — PRIMARY

### 7. Wikidata / Wikipedia internal contradictions

- **Data.** Wikidata JSON dumps (CC0) and Wikipedia dumps (CC BY-SA), from dumps.wikimedia.org.
- **Question.** Statements that contradict each other (disjoint-class violations, birth after death, an infobox that disagrees with the body
  text or with another language edition). A "find" is a corrected fact with a source.
- **Gap evidence.** Doğan & Patel-Schneider (2024): "many incorrect statements and internal contradictions," found by SPARQL. A
  Phabricator task asks what fraction of constraint violations are false alarms, so this is unquantified.
- **Verifier.** A cited primary source settles each case. This is per-item human work, not mechanical.
- **Precedent.** Disjointness-violation and class-order studies. CorHist repair-rule learning (WWW 2019), deployed to editors.
  WikiContradict (NeurIPS 2024, 253 instances): LLMs are poor at noticing implicit conflicts, a caution for LLM-only sweeps.
- **Recipe.** Code with SPARQL/dump parsing finds structural contradictions. An LLM compares cross-language infoboxes and proposes
  which side is right, with a source. A human checks the source and edits.
- **Cost.** Dumps are large (100+ GB uncompressed for Wikidata, unverified); a cloud VM is helpful.
- **Traps.** Contradictions that are real disagreements in the sources (dates, Julian/Gregorian calendars). Vandalism already reverted.
  Bot-edit etiquette: mass LLM edits will be reverted, and the editor banned.
- **Crowding.** `PARTLY` (Wikidata constraint reports exist; research groups).
- **Ethics.** Living-person (BLP) policy. Do not "correct" private individuals' data.
- **Scores.** data_ready 4 · gap 3 · verifier 3 · cheapness 3 · payoff 2 · ethics_clear 4
- **Sources.**
  - https://arxiv.org/pdf/2410.13707 — SCHOLARLY
  - https://arxiv.org/pdf/2406.13805 — SCHOLARLY (WikiContradict)
  - https://phabricator.wikimedia.org/T241543 — PRIMARY (open question on false-alarm rate)

### 8. Endangered-language archives: untranscribed audio

- **Data.** PARADISEC: 18,500 h of audio and 4,000 h of video across ~1,400 languages. ELAR (SOAS, now Berlin). Access conditions vary
  per item, and many need registration and agreement.
- **Question.** Not "discovery" in the lidar sense. It is the first transcription or summary of recordings nobody has listened to since
  they were made. Finds: a lost song cycle, a speaker of an unrecorded dialect, mislabelled language metadata.
- **Gap evidence.** PARADISEC (Oct 2025): one ASR model trained on 38 h transcribed 22 h of previously untranscribed audio. The
  2026 post says ASR is "still early" for most of the collection's languages.
- **Verifier.** Speakers and community members, and the original depositor or linguist. Slow, human, but real.
- **Precedent.** The PARADISEC/Melbourne ASR work above. Language-ID mislabel discovery is plausible but unsourced.
- **Recipe.** Code runs a multilingual language-ID/ASR model to flag mislabelled items and draft segmentations. An LLM drafts summaries
  from glossed transcripts only. Everything goes back through the archive.
- **Cost.** GPU helpful for ASR. Access requests take weeks.
- **Traps.** Hallucinated transcripts of low-resource languages. LLM "translations" with no training data.
- **Crowding.** `PARTLY` (the archives' own funded projects; LDaCA 2022–27).
- **Ethics.** Serious: Indigenous data sovereignty, CARE principles, restricted and sacred material. Never redistribute. Work only
  with the archive.
- **Scores.** data_ready 2 · gap 4 · verifier 2 · cheapness 2 · payoff 4 · ethics_clear 2
- **Sources.**
  - https://www.paradisec.org.au/blog/2025/10/large-language-models-for-small-languages/ — PRIMARY
  - https://www.paradisec.org.au/blog/2026/06/online-media-annotation/ — PRIMARY

### 9. Fan fiction (AO3): taken seriously, and where it leads

- **Data.** Legitimate: AO3's official March 2021 metadata dump (works + tags CSVs: dates, language, word count, tags; a
  selective sample). Illegitimate: nyuuzyou's April 2025 scrape of ~12.6M works to Hugging Face, removed by DMCA (OTW
  filed). AO3 states it asked Common Crawl to stop (Dec 2022), rate-limits, makes "no exceptions for researchers or
  those wishing to create datasets", and added Cloudflare AI-bot blocking after the 2025 scrape (the last point is from Reddit; unverified).
- **Question, honestly.** Three candidate "facts":
  (a) *Cultural evolution*: when and where a trope or neologism first appears in a tag, and how it spreads across fandoms.
  The metadata dump supports this. (b) *LLM contamination*: whether a model has seen fandom-only vocabulary. The 2023
  Omegaverse "Sudowrite test" is the folk precedent. (c) *Authorship deanonymization*: **excluded.** AO3 is
  pseudonymous by design. Many writers are minors, queer, or writing sexual content under pseudonyms for safety. The payoff of
  linking a pseudonym to a real person is identifying a private individual, which the brief rules out.
- **Gap evidence.** For (a), thin: Pianzola, Acerbi & Rebora (2020) already measured tag accumulation in the HP fandom. The
  search found no other trope-diffusion study, so the gap exists, but is it a *discovery*?
- **Verifier.** For (a), none mechanical. "First appearance" depends on what was scraped and when; works get deleted,
  orphaned, back-dated. Fanlore (a human-written fandom history) is the only cross-check. For (b), a membership-inference test,
  which is shaky science.
- **Precedent.** Pianzola et al. 2020 (SCHOLARLY). Sudowrite/Omegaverse (POPULAR; the company denied scraping, and the test is
  circumstantial).
- **Recipe.** Code computes tag first-use dates and diffusion curves across fandoms from the 2021 dump. An LLM clusters synonym tags
  (AO3's tag wranglers have done this by hand: ~5M tags wrangled in 2021).
- **Cost.** Trivial.
- **Traps.** The dump is a sample. Tag wrangling rewrites history (canonical tags are merged later). Deleted works. Treating
  AO3 as all of fandom (LiveJournal, FF.net and Tumblr predate it).
- **Crowding.** `OPEN` because it is low value, not because it is overlooked.
- **Ethics.** Hostile community. Full-text use violates the clear wishes of the platform and the authors. Restrict yourself to the official
  metadata. No deanonymization. Payoff is a humanities paper, not a discovery.
- **Scores.** data_ready 3 · gap 2 · verifier 1 · cheapness 5 · payoff 1 · ethics_clear 2
- **Sources.**
  - https://fanlore.org/wiki/AO3,_AI_and_scraping — SECONDARY (fan wiki)
  - https://www.transformativeworks.org/ai-and-data-scraping-on-the-archive/ — PRIMARY (OTW; via search summary, fetch failed)
  - https://next.fanlore.org/wiki/2025_Unauthorised_AO3_Scraping_for_AI_Model_Training_via_Huggingface — SECONDARY
  - https://acerbialberto.com/publication/cp_2020_chr/ — SCHOLARLY
  - https://techcrunch.com/2023/06/13/fan-fiction-writers-are-trolling-ais-with-omegaverse-stories — POPULAR
  - https://joellene.substack.com/p/data-science-x-ao3-1-spikes-in-published — POPULAR (2021 dump contents)

### 10. Software and game archaeology (Software Heritage, TCRF, prototypes)

- **Data.** Software Heritage (>19B files, >290M origins; research graph datasets). The Internet Archive software
  collections. Game ROMs/binaries (copyrighted).
- **Question.** Unused content in shipped games. Lost source recovered from an archive (e.g. Parmap, after Gitorious closed).
- **Gap evidence.** TCRF has >30,000 articles. The famous titles are thoroughly mined; the obscure ones are not.
- **Verifier.** Good: the content is in the binary, or the commit is in the archive. Significance is the weak part.
- **Precedent.** TCRF and Hidden Palace (prototype releases). The Software Heritage recovery of Parmap. The MySpace "Dragon Hoard" (490k
  songs recovered from a 2008–10 academic crawl).
- **Recipe.** Code disassembles and diffs assets against what is referenced. An LLM reads strings and debug text and translates
  Japanese dev comments.
- **Cost.** Laptop, but a lot of skilled human time.
- **Traps.** Fan-made hoaxes ("found" prototypes). ROM hacks presented as originals.
- **Crowding.** `CROWDED` for games (a large, skilled hobbyist community). `PARTLY` for SWH research.
- **Ethics.** Copyright and DMCA on redistributing binaries. Firmware digging slides toward vulnerability research, which is out of scope
  ("defeating security"). Secrets in archived code: don't harvest them.
- **Scores.** data_ready 3 · gap 2 · verifier 4 · cheapness 3 · payoff 1 · ethics_clear 3
- **Sources.**
  - https://arxiv.org/pdf/2004.00514 — SCHOLARLY (Software Heritage; Parmap)
  - https://tcrf.net/Main_Page — SECONDARY
  - https://www.sophos.com/en-gb/blog/myspace-songs-come-back-from-the-dead — POPULAR

### Dropped (one line each, with reason)

- **Chess novelties (Lichess open database, CC0 per mirrors).** A "novelty" is by definition just absent from databases, and engines
  already search better than any sweep. No discovery left that an engine doesn't trivially produce.
- **SEC EDGAR Benford sweeps.** Amiram et al. (2015) has been challenged (Walker 2022). Type I error is high. Short sellers and the
  SEC already do this. The payoff is accusing named firms of fraud, so the defamation risk is high. `CROWDED`, low verifier.
- **CMS Open Payments.** Already heavily mined (journalism and academia). Payoff centers on named individual physicians,
  which edges toward targeting individuals. Drop.
- **Folk-tune variant families (Roud/Child).** Computational melody-family work exists (Utrecht, 360 melodies / 26 families).
  The verifier is expert taste. A deep dive, not a discovery.
- **NEISS (CPSC injury data).** A good dataset, but the search found no hobbyist-discovery precedent, and its narratives are
  coded for product category, not model, so a "signal" can't be tied to a product to recall.

---

## Pilot in a day

**OEIS range-limited conjectures, triage plus extension.** Chosen because the verifier is mechanical, the data is reachable
from this container (GitHub; oeis.org itself was 403), the A173419 precedent is exactly this shape, and it is `PARTLY`
crowded rather than `CROWDED` like Erdős.

1. Get the data (works here; ~2 GB, ~10 min):
   ```
   git clone --depth 1 --filter=blob:none --sparse https://github.com/oeis/oeisdata.git
   cd oeisdata && git sparse-checkout set seq
   cat time.txt   # record the export timestamp
   ```
   b-files for selected entries: `git sparse-checkout add files/A173` (per-prefix), or raw URL
   `https://raw.githubusercontent.com/oeis/oeisdata/main/files/A173/b173419.txt` (path layout unverified; check the README).
2. Reproduce the survey counts as a script in `puzzles/<slug>/analysis/` with the output checked in (Rule 6). The ad hoc
   version used here was `grep -rh '^%[CF]' seq | grep -i conjecture` (26,687 lines), then
   `grep -iE 'verified|checked|true for|holds for|tested'` (1,264), then excluding `disprov|counterexample|false` (412 lines overall).
3. Drop entries with keyword `dead`, entries whose later comments already settle the conjecture, and the 492 formalized in the
   OEIS Open benchmark (list at tadamcz.com/oeis-open; unverified URL).
4. An LLM classifies each remaining line: {finite-checkable with stated N, asymptotic, vague}. Keep the finite-checkable ones with
   a runnable `%o` program (PARI/Python/Mathematica; prefer PARI/Python).
5. For the top ~50 by cheapness, write two independent checkers (the `%o` program and a fresh one), confirm they agree on the
   b-file, then extend to 10·N under a CPU budget per item.
6. Output: a table of {A-number, conjecture, old N, new N, result}. Any counterexample gets a third check before an OEIS
   comment is drafted. Extending a verified range is a legitimate, modest result. Expect mostly that.

Wall to name if it stalls: conjectures whose checker cost grows super-exponentially (like A173419's BFS), where 10·N is
infeasible on a laptop.

## Unverified claims

- AO3 added a Cloudflare AI-scraper tool after the 2025 Hugging Face scrape (Reddit report via search; date unclear).
- Current openFDA bulk manifest URL `https://api.fda.gov/download.json` and partition layout: from openFDA docs via
  search summary; not fetched (proxy 403).
- MAUDE data moving to FDA AEMS in 2026: FDA page per search summary; status not confirmed.
- Current `FLAT_CMPL.zip` host: data.gov lists www-odi.nhtsa.dot.gov; static.nhtsa.gov path inferred from CMPL.txt.
- NHTSA defect petition channel (49 CFR Part 552): from memory, not fetched.
- OEIS Open interactive list at tadamcz.com/oeis-open: from the seqfan post via search summary.
- The A173419 counterexample computations were "scripted with help from Claude" (search summary of the arXiv/HAL listing;
  not fetched).
- Problem #281 as "the most unambiguous instance" of AI solving an open problem (Tao, via one secondary outlet). The
  reduction-to-Davenport–Erdős dispute is from Reddit.
- Wikidata dump size (100+ GB uncompressed): from memory.
- OEIS conjecture counts above come from an unsaved ad hoc grep (2026-10-15 export), not from a checked-in script. Treat them as
  approximate until step 2 of the pilot reruns them. The regexes surely miss phrasings ("we conjecture", "it appears that").
- ProPublica "Dollars for Docs" as prior Open Payments mining: from memory, not searched.
- Deliberate trap errors in printed tables to detect copying: folklore, not sourced.
- Lichess database CC0 license: confirmed only on third-party mirrors.
