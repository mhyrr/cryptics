# Untouched data — biology, genomics, natural history

*Survey written 2026-10-15 against `sources/untouched-data/BRIEF.md`. Rules 1, 2, 3,
6, 7 of `AGENTS.md` apply: every load-bearing claim below carries a URL and a tier,
claims I could not verify are in `## Unverified claims`, and nothing here is an
attempt at the discovery itself (Rule 9).*

**Best bets in this domain, in order:**

1. **Logan** — the entire SRA assembled into contigs, free and anonymous on S3. It is
   the single most under-searched public corpus in biology right now, and the papillomavirus
   sweep shows a 10-hour search can expand a viral family by a third.
2. **Bioacoustic archives with an open classifier attached** (NOAA's
   `noaa-passive-bioacoustic` + Google's 2024 multi-species whale model): hundreds of
   TB of audio, an off-the-shelf detector, and a precedent (the biotwang) where the
   find was in the archive all along.
3. **Specimen-label error in digitized collections** (GBIF/iDigBio/herbarium images):
   a measured base rate of ~50% wrong names in tropical material means the "find" is
   plentiful; the bottleneck is a taxonomist willing to sign the redetermination.
4. **Structural dark matter** (AlphaFold DB + TED/Foldseek clusters): data ready,
   verifier mechanical-ish, but heavily crowded and GPU-adjacent.
5. Weakest of the lot: camera-trap and iNaturalist sweeps — cheap, but the payoff is
   usually a range extension rather than a discovery, and the experts are swamped.

The pattern across all of these: the verifier is a human specialist in a small field,
except for sequence work, where independent re-assembly plus phylogenetic placement is
a genuine mechanical test. That asymmetry should drive candidate choice.

---

### 1. Logan (whole-SRA assemblies) searched for an unswept class of element

- **Data** — Logan: the full NCBI Sequence Read Archive assembled into unitigs and
  contigs by Chikhi and colleagues at Institut Pasteur. v1 was a December 2023 freeze
  of ~27.3M accessions (4.59 Pbp unitigs, 0.90 Pbp contigs); the project page now
  states v1.2 is built from an **end-of-2025 freeze of the entire SRA, 87 petabases
  across 38 million accessions**. Public S3, no AWS account needed:
  `s3://logan-pub/c/<ACC>/<ACC>.contigs.fa.zst` (zstd-compressed FASTA), also over
  plain HTTPS at `https://s3.amazonaws.com/logan-pub/c/...`. Listed in the AWS
  Registry of Open Data (no egress charge, anonymous access). A k-mer search index
  over unitigs from 23.4M accessions is at logan-search.org. License is not stated on
  the project page — see Unverified claims.
- **Question / what a find looks like** — SRA is sequenced for one organism at a time
  and almost nothing else in the run is ever looked at. Pick a class of element that
  nobody has swept Logan for and sweep it: candidates include novel self-cleaving
  ribozyme families, further obelisk-like RNA lineages outside the described
  phylogeny, CRISPR-associated gene modules in eukaryote-project bycatch,
  giant-virus marker genes, or complete genomes of unculturable endosymbionts riding
  along in host sequencing runs. A find is: a contig set from ≥3 independent
  accessions, with a coherent predicted structure or protein family, absent from
  current reference databases.
- **Gap evidence** — The Logan preprint itself reports the corpus expanding known
  diversity of plasmids 22-fold over PLSDB and obelisks 3.7-fold over the original
  description, i.e. the authors demonstrated the gap exists for the handful of classes
  they happened to test, and did not test the rest. The papillomavirus follow-on
  (Shen, Korobeynikov, Chikhi, Babaian) searched Logan for *one* DNA virus family in a
  ~10-hour alignment run and expanded PV diversity by 34% with 383 novel types across
  105 host species — one family, one search, in one working day. Serratus searched 5.7M
  runs for **one gene** (RdRP) and got ~132k novel RNA viruses; every other marker gene
  in biology is a separate unswept axis.
- **Verifier** — Strong and largely mechanical, which is what makes this the best
  candidate in the domain: (a) re-assemble the candidate from the *raw reads* of the
  source accessions independently of Logan's assembler; (b) place it phylogenetically
  — a real element has relatives and a tree position, an artefact does not; (c) check
  for the signature of index hopping/cross-contamination by looking at what else was
  on the same sequencing run and the same submitting project; (d) for structured RNA,
  covariation support for the predicted secondary structure across independent
  variants. Then a specialist in the relevant element class, and a submission to the
  appropriate taxonomy committee (ICTV for viruses).
- **Precedent** — Salzberg et al. 2005 pulled three new *Wolbachia* genomes out of the
  public Trace Archive by using a known strain as a probe, one assembled to >95%
  coverage; the paper's framing is exactly this candidate's thesis ("an unexpected
  benefit of depositing raw data in a central repository"). Edgar et al., *Nature*
  2022 (Serratus). Zheludev et al., *Cell* 2024 (obelisks — a wholly new class of RNA
  element found in already-public metatranscriptomes). Altae-Tran et al., *Science*
  2023 (188 previously unreported CRISPR-linked gene modules from 8.8 Tbp of public
  metagenomes).
- **Recipe** — Code does essentially all of it. (1) Build or borrow a query: an HMM or
  a set of 31-mers for your marker. (2) Narrow the accession set — use logan-search.org
  for k-mer hits, or filter SRA metadata by library strategy/organism to a few 10⁵
  accessions. (3) Stream per-accession contigs from S3, `zstdcat | ` your matcher
  (`rcgrep` for single k-mers, `back_to_sequences` for many queries, `hmmsearch` after
  6-frame translation for protein markers), discard, keep hits. (4) Cluster hits,
  dereplicate, align, build a tree. The LLM's job is strictly the parts that are
  reading and judgement: choosing an unswept marker by reading what the Logan and
  Serratus papers *did not* search, writing and debugging the pipeline, reading
  submitter metadata to spot contamination stories, and drafting the writeup. The LLM
  must not be allowed to opine on whether a hit is real — that is (c)/(d) above.
- **Cost** — Hours to days of wall clock; no GPU. Egress is free from `logan-pub`, but
  the whole contig set is ~0.9 Pbp, so the cost is entirely in how well you narrow the
  accession list. A focused sweep of 10⁴–10⁵ accessions is a laptop-plus-fast-internet
  job; a tens-of-dollars cloud VM in `us-east-1` (same region as the bucket) makes it
  comfortable. The published precedent runs are 10 hours of compute, not thousands.
- **Traps** — (i) Index hopping and library cross-contamination are *the* false-positive
  mode in this field: reanalyses of pangolin and Wuhan agricultural datasets found
  bat-, mouse- and human-matching reads at 0.1–1% across unrelated samples, and the
  authors attributed them to index hopping and handling contamination, not biology.
  Any "novel X in an unexpected host" claim is a contamination claim until the run
  structure is examined. (ii) Assembly chimeras: two organisms' reads can be glued into
  one contig. (iii) Database-novelty is not biological novelty — "no BLAST hit" often
  means "fast-evolving region of a known thing". (iv) The crank history here is
  specifically the host-attribution literature around SARS-CoV-2 relatives, where
  contamination was repeatedly read as discovery.
- **Crowding** — `PARTLY`. The Logan group and Babaian's lab (Serratus) are actively
  sweeping it and will take the obvious marker genes; big labs (Zhang's for CRISPR)
  take the high-value ones. But the corpus is 87 Pbp and the number of markers is
  large, so a specific unglamorous class is plausibly `OPEN`. Check the Logan GitHub
  and logan-search publications before committing to a marker.
- **Ethics** — Human-derived runs are a large fraction of SRA. Rule: stay in the
  non-human and microbial fraction, and never attempt to genotype or re-identify a
  human sample — that is out of bounds under the brief and is dropped, not mitigated.
  Nagoya/CBD: sequence data from public archives is "digital sequence information",
  which COP16 Decision 16/2 brought into a benefit-sharing mechanism (the Cali Fund,
  launched February 2025, with an indicative contribution rate for commercial users).
  A non-commercial survey is not a contributor, but anything with a commercial tail
  needs to look at this, and descriptions of organisms from a specific country should
  credit and ideally involve researchers there.
- **Scores** — `data_ready` 5, `gap` 5, `verifier` 4, `cheapness` 4, `payoff` 5,
  `ethics_clear` 4.
- **Sources**
  - https://github.com/IndexThePlanet/Logan — PRIMARY (project page; v1.2, Dec-2025 freeze, 87 Pbp/38M accessions, S3 paths)
  - https://github.com/IndexThePlanet/Logan/blob/main/Contigs.md — PRIMARY (exact `s3://logan-pub/c/...` paths, zstd, `--no-sign-request`)
  - https://github.com/IndexThePlanet/Logan/blob/main/Sequence_Search.md — PRIMARY (search recipes, `rcgrep`, `back_to_sequences`)
  - https://www.biorxiv.org/content/10.1101/2024.07.30.605881.full.pdf and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12424806/ — SCHOLARLY (Logan paper; 4.59 Pbp unitigs, 22× plasmids, 3.7× obelisks)
  - https://registry.opendata.aws/pasteur-logan — PRIMARY (open-data registration, anonymous access)
  - https://elifesciences.org/reviewed-preprints/111778 — SCHOLARLY (papillomavirus sweep of Logan; ~10 h, +34% diversity, 383 novel types)
  - Edgar et al., *Nature* 602:142–147 (2022), https://www.pasteur.fr/en/whats-new/latest-news/news/innovative-genomic-data-analysis-method-leads-discovery-novel-coronavirus-families — SCHOLARLY/SECONDARY (Serratus; 5.7M runs, 10.2 Pbp, ~$0.01/sample, 131,957 novel RdRPs)
  - Zheludev et al., *Cell* (2024), preprint https://www.biorxiv.org/content/10.1101/2024.01.20.576352.full.pdf — SCHOLARLY (obelisks; 29,959 distinct, hammerhead ribozyme variant)
  - Altae-Tran et al., *Science* 382:eadi1910 (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10910872/ — SCHOLARLY (FLSHclust; 8.8 Tbp, 188 new CRISPR-linked modules)
  - Salzberg et al., *Genome Biology* 6:R23 (2005), https://cbcb.umd.edu/node/38496 — SCHOLARLY (Wolbachia from the Trace Archive)
  - https://arxiv.org/pdf/2108.08163 and https://arxiv.org/pdf/2104.01533 — SCHOLARLY (preprints; contamination/index-hopping in public datasets)
  - https://www.cbd.int/califund/guides/guide%20to%20parties.pdf — PRIMARY (Cali Fund / DSI benefit sharing)

---

### 2. Cobiont and symbiont genomes in reference-genome projects' raw reads

- **Data** — Raw long reads (PacBio HiFi, ONT) from the large reference-genome
  consortia, deposited in ENA/SRA: Darwin Tree of Life (target 70,000 eukaryotic
  genomes), plus the other Earth BioGenome affiliates. Each read set is the target
  organism *plus* everything living in or on it.
- **Question / what a find looks like** — A complete, reference-quality genome of an
  organism nobody sequenced on purpose: an endosymbiont, a gut microbe, a parasite, a
  fungal associate — including unculturable ones that cannot be obtained any other way.
  A find is a closed or near-closed genome binned out of a read set, with a credible
  taxonomic placement and a plausible biological relationship to the host.
- **Gap evidence** — The cobiont material is a byproduct the consortia deliberately
  *remove*: their pipelines (BlobToolKit and friends) exist to detect and discard
  non-target sequence before assembly submission. A 2024 preprint on disentangling
  cobionts states the case directly — that reference-quality genomes can be built for
  cobionts including unculturable endosymbionts given suitable tools — and a companion
  study using a variational autoencoder over tetranucleotide composition on DToL HiFi
  insect read sets recovers a large fraction of cobionts found by reference-based
  screening. In other words the tooling now exists and the backlog of read sets grows
  monthly.
- **Verifier** — Mechanical and good: completeness/contamination statistics on the bin
  (BUSCO/CheckM), coverage and GC coherence, a phylogenomic tree from conserved
  marker genes, and independent recovery of the same bin from a *different* individual
  or a different sequencing run of the same host species. Then a microbial systematist;
  a new species name needs a formal description under the relevant code.
- **Precedent** — Salzberg 2005 (above) is the prototype. The 2024/2025 cobiont work is
  the modern form; a 2025 paper found a bacteriophage sequence in a mite genome
  assembly, which both revealed bacterial contamination and opened a route to studying
  arthropod symbionts from existing data.
- **Recipe** — Code does all the heavy lifting: pull HiFi read sets for a host clade
  from ENA, assemble, bin by composition/coverage, classify bins, drop the host, keep
  the rest; or start from the published assemblies' discarded "contamination" scaffolds
  where those were deposited. LLM does: choosing a host clade whose symbionts are
  poorly known, reading the consortium's QC reports to find which read sets had large
  non-target fractions, and writing the pipeline.
- **Cost** — Higher than candidate 1. HiFi read sets are tens of GB each; assembly of a
  single insect-scale read set wants ~64–128 GB RAM for hours. A hobbyist can do a
  handful of read sets on a rented VM for tens of dollars; a systematic sweep is a real
  compute project. No GPU needed.
- **Traps** — Distinguishing a genuine cobiont from laboratory contamination and from
  index hopping is the whole game, and it is the same trap as candidate 1 — with the
  added wrinkle that a "symbiont" recovered from one individual of one species is not
  yet a symbiosis. Barcode/16S-only claims are not genomes.
- **Crowding** — `PARTLY`. The DToL/Sanger group built the tools and is interested; but
  they are optimizing for publishing host genomes, and the cobiont bins are a side
  product nobody has time to describe. The gap between "recovered" and "described" is
  where a careful outsider fits.
- **Ethics** — Nagoya/CBD applies with force here: these are organisms from specific
  countries, sampled under specific permits, and a symbiont described from them has
  the same provenance obligations as the host. Check the host record's permit and
  country-of-origin metadata and involve local researchers. Human-associated read sets
  are out of scope.
- **Scores** — `data_ready` 4, `gap` 4, `verifier` 4, `cheapness` 2, `payoff` 4,
  `ethics_clear` 3.
- **Sources**
  - https://www.biorxiv.org/content/10.1101/2024.05.30.596622.full.pdf — SCHOLARLY (disentangling cobionts and contamination in long-read data; DToL 70,000-genome target)
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11540323/ — SCHOLARLY (composition-based VAE recovers cobionts from DToL HiFi insect read sets)
  - https://sanger.ac.uk/tool/blobtoolkit and https://blobtoolkit.genomehubs.org/2017/06/28/introducing-blobtoolkit — PRIMARY (the tool whose purpose is removing this material)
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12507336/ — SCHOLARLY (phage found in a mite genome assembly)
  - Salzberg et al. 2005, https://cbcb.umd.edu/node/38496 — SCHOLARLY

---

### 3. NOAA's passive-acoustic archive, swept with the open 2024 whale model

- **Data** — `gs://noaa-passive-bioacoustic`, NOAA NCEI's passive acoustic archive on
  Google Cloud under the NOAA Big Data Program. I listed the bucket: 32 top-level
  collections, including `sanctsound/`, `pifsc/`, `nefsc/`, `sefsc/`, `swfsc/`,
  `afsc/`, `nrs/` (Ocean Noise Reference Stations), `adeon/`, `mbari/`, `cornell/`,
  `dclde/`, plus `big_query_metadata/`. The PIFSC collection alone holds
  `pifsc/audio/pipan_10/` across 16 stations (hawaii, wake, saipan, tinian, pagan,
  howland, kingman, palmyra, PHR, equator, cross-seamount, Kauai, Ladd Seamount…),
  as FLAC-compressed XWAV with a documented 75-second-subchunk header format and an
  `annotations.csv` of human-audited intervals. SanctSound is reported at ~300 TB and
  NOAA's North Pacific recorder network at >500 TB / ~200,000 hours since 2005.
  Access is anonymous HTTPS/GCS; there is a bucket-root `README.pdf`.
- **Question / what a find looks like** — Recordings made to measure *noise* and to
  count a handful of target species contain every other sound in the ocean. A find is:
  a recurring, structured, un-attributed sound type with a coherent seasonal and
  geographic footprint — which is how new populations and new call types get
  recognized — or a known species' call appearing at a station far outside its
  documented range and season.
- **Gap evidence** — The biotwang is the clean demonstration: a call first logged in
  2014, sitting in NOAA's archive, only attributed to Bryde's whales in a 2024
  *Frontiers in Marine Science* paper, and only then traced across the archive (the
  team used a mix of manual and machine-learning annotation over "extensive historical
  passive acoustic monitoring datasets" to map it to the Marianas, Wake, the NW
  Hawaiian Islands and Howland). The archive was annotated for humpback song (the 2021
  PIFSC CNN paper); everything the annotators were not looking for is unlabeled. The
  Google model's own release notes that it labeled "more than 200,000 hours" of
  recordings, i.e. one pass by one group over one set of targets.
- **Verifier** — This is the candidate's weak joint and must be named honestly. There
  is no mechanical test that a sound is a new species. What exists: (a) co-occurrence
  with visual sightings — exactly how the biotwang was pinned, during a 2018 survey
  that saw ten groups of Bryde's whales while recording; (b) consistency across
  independent instruments and years; (c) a marine-bioacoustician who knows the local
  soundscape. A hobbyist can produce a defensible *detection and distribution* claim;
  the species attribution requires someone with a ship. Name that wall up front.
- **Precedent** — Biotwang → Bryde's whale, 2024 (ML search of the historical archive).
  Cerchio et al. 2020, *Endangered Species Research*: a previously unrecognized blue
  whale population in the western Indian Ocean, recognized from song recorded off Oman
  and compared against archived recordings — including a CTBTO Diego Garcia hydrophone
  record used for the comparison song type. Both are "the data already existed".
- **Recipe** — Code: stream FLAC/XWAV from GCS, decode (honoring
  `--keep-foreign-metadata` for the XWAV header), window, run Google's multi-species
  whale model (8 species, including the biotwang class, on Kaggle Models via the
  TensorFlow SavedModel API) to get a baseline label track, then look at the
  *residual* — high-energy, repeating, structured events the classifier scores low on
  every class — and cluster those by spectrogram embedding. LLM: reads the station
  metadata and the species' known ranges to decide which detections are anomalous and
  worth a human's attention, drafts the writeup, and finds the right specialist. The
  LLM must not judge whether a spectrogram is a whale.
- **Cost** — Dominated by audio volume: a single station-year is hundreds of GB. One
  station, one year, one model pass is a day on a CPU VM with patience (the Google
  model will run on CPU but slowly); a GPU makes it comfortable and is the one place in
  this survey where a GPU genuinely helps. Egress from GCS is the real bill if you pull
  outside Google Cloud — run it inside `us-central`-ish GCP to avoid that, or budget
  for tens of dollars of transfer per station-year.
- **Traps** — The false-positive modes are richly documented and mostly non-biological:
  ships, seismic airguns, ice, fish choruses, instrument self-noise, mooring strum,
  electrical interference, and file-boundary artifacts, all of which make tonal or
  pulsed patterns. The field's crank analogue is the "unexplained ocean sound"
  genre — most famous unidentified sounds (Bloop, etc.) resolved to ice or geology,
  not animals. Also: the archive's own documented erratum (PIFSC annotations.csv had
  UTC endpoints 8 hours off until 2022-07-27) is a reminder that metadata time bases
  are a real source of spurious "co-occurrence".
- **Crowding** — `PARTLY` to `CROWDED` on the target species (NOAA + Google are
  actively sweeping for the eight modeled species); `OPEN` on the residual — the
  sounds nobody has a class for — and on stations outside the North Pacific focus.
- **Ethics** — Clean. Public-domain US government data, no privacy issue, no living
  humans involved. One real concern: do not publish precise locations of identified
  individuals or aggregations of endangered species in a way that could direct
  harassment or vessel traffic; follow NOAA's own practice of station-level rather
  than fine-grained reporting.
- **Scores** — `data_ready` 5, `gap` 4, `verifier` 2, `cheapness` 3, `payoff` 4,
  `ethics_clear` 5.
- **Sources**
  - `gs://noaa-passive-bioacoustic` listing and `pifsc/README.md`, retrieved 2026-10-15 via `https://storage.googleapis.com/storage/v1/b/noaa-passive-bioacoustic/o` — PRIMARY (32 collections; XWAV/FLAC format; annotations.csv schema and erratum)
  - https://www.ncei.noaa.gov/products/passive-acoustic-data — PRIMARY (archive landing page; `pad.info@noaa.gov`)
  - https://catalog.data.gov/dataset/sanctsound-raw-passive-acoustic-data — PRIMARY (SanctSound raw audio, GCS location)
  - https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2024.1394695/pdf — SCHOLARLY (biotwang = Bryde's whale; ML + manual search of historical PAM data; seasonal/geographic footprint)
  - https://research.google/blog/whistles-songs-boings-and-biotwangs-recognizing-whale-vocalizations-with-ai/ — POPULAR/PRIMARY (Google, 2024-09-18: 8-species model, biotwang class, Kaggle Models release, >200,000 hours labeled)
  - https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2021.607321 — SCHOLARLY (PIFSC humpback CNN; what the archive was annotated *for*)
  - Cerchio et al., *Endangered Species Research* (2020), copy at https://repository.library.noaa.gov/view/noaa/52786/noaa_52786_DS1.pdf — SCHOLARLY (new WIO blue whale population; CTBTO H08N1 comparison recording)
  - https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2021.703682/pdf — SCHOLARLY (NCEI archive described as >100 TB in 2021; NOAA Big Data Program/GCP route)

---

### 4. Wrong names in digitized natural-history collections

- **Data** — GBIF and iDigBio aggregate hundreds of millions of specimen records, a
  large and growing fraction with high-resolution images (herbarium sheets especially,
  which are flat, standardized, and label-bearing). CC-BY/CC0 metadata; image licenses
  vary by institution. Machine-readable via GBIF's occurrence download API and
  iDigBio's API.
- **Question / what a find looks like** — Two different finds. (a) **Redetermination**:
  a specimen whose label name is wrong, flagged by image, and corrected. (b) **The
  Bebber find**: a specimen that belongs to no described species at all, sitting in a
  drawer. A find in form (b) is a specimen (or a set of them) that a monographer agrees
  is undescribed, leading to a formal description with that sheet as the type.
- **Gap evidence** — This is the best-quantified gap in the survey. Bebber et al., PNAS
  2010: only 16% of flowering-plant species described 1970–2010 were named within five
  years of first collection, nearly a quarter were described from specimens over 50
  years old, and extrapolation gives **more than half of the ~70,000 still-undescribed
  species already collected and sitting in herbaria**. Goodwin et al., *Current
  Biology* 2015: of ~4,500 African ginger specimens across 40 herbaria in 21 countries,
  **at least 58% carried the wrong name** before a modern revision; the authors
  estimate >50% of tropical specimens are incorrectly named and explicitly recommend
  remotely accessed digitized specimens as one of two essential tools for fixing it.
- **Verifier** — Named precisely, because it is the binding constraint: a monographer
  of the group, looking at the sheet (or at a high-resolution image plus, where
  needed, the physical specimen), and a published redetermination or description. There
  is no mechanical substitute; the ICN requires a type specimen, and the "describe from
  photographs" practice is contested — one high-profile photo-only description was
  called "taxonomic malpractice" in the ensuing exchange, and a 2022 *Madhuca* study
  found that key microscopic characters often cannot be resolved even in
  high-resolution images.
- **Precedent** — Bebber et al. is both the evidence and the precedent: Oxford's
  coverage of it cites a researcher describing 60 new *Strobilanthes* species from
  long-unexamined herbarium material. The iNaturalist cases (candidate 6) are the
  photo-first version of the same workflow.
- **Recipe** — Code: bulk-download GBIF occurrence records plus image URLs for a
  target family; compute, per determined name, the distribution of a vision model's
  embeddings; flag sheets that are embedding-outliers within their label name, or whose
  nearest neighbors are consistently a different name; cross-check against label text
  via OCR (collector, date, locality) and against the accepted-name backbone. LLM:
  reads the labels (handwritten collector data, where OCR fails and a VLM is genuinely
  good), reconciles synonymy, reads the group's revisions to see whether a flagged
  cluster corresponds to a known taxonomic problem, and writes the dossier that gets a
  monographer's attention. Code computes the anomaly; the LLM must not pronounce a
  species new (Rule 6 and Rule 4 both bite here).
- **Cost** — Very cheap. Metadata downloads are GB-scale; a few tens of thousands of
  images is a laptop-day. CPU-only embedding models are adequate for outlier flagging.
- **Traps** — (i) Specimen images are a hard domain for off-the-shelf vision models:
  the 2021 herbarium challenge found classical CNNs trained on field photos essentially
  fail on herbarium sheets (MRR 0.011; domain adaptation got to 0.180). Model
  disagreement with a label is weak evidence. (ii) The label may be "wrong" only in the
  sense of being an outdated synonym — Goodwin's 58% explicitly includes outdated
  names, redundant names and genus-only determinations, so an unexamined pipeline will
  mostly rediscover nomenclature, not biology. (iii) Intraspecific variation (the
  *Equisetum* case) generates outliers that are not misidentifications. (iv) The social
  trap: unsolicited "your specimen is misidentified" reports from strangers are a known
  nuisance to curators; a dossier that respects their time is the whole craft.
- **Crowding** — `PARTLY`. Digitization and ML-assisted curation are funded programs
  (iDigBio, institutional projects, the herbarium-challenge community), but they are
  working family-by-family and institution-by-institution, and the backlog is
  tens of thousands of species by the field's own estimate. A specific neglected group
  is `OPEN`.
- **Ethics** — No privacy issue. Two real ones: (a) Nagoya and country-of-origin — a
  new species described from a colonial-era collection taken from a country whose
  botanists were not involved is a live grievance in this field; involve them, as a
  matter of both ethics and getting the name accepted. (b) Locality data for rare taxa
  is already redacted by many publishers to deter collectors; respect the redaction and
  do not reconstruct coordinates for poaching-sensitive groups (orchids, cycads,
  succulents).
- **Scores** — `data_ready` 5, `gap` 5, `verifier` 2, `cheapness` 5, `payoff` 4,
  `ethics_clear` 4.
- **Sources**
  - Bebber et al., *PNAS* 107:22169–22171 (2010), doi 10.1073/pnas.1011841108; summary https://www.botany.one/herbaria-are-a-major-frontier-for-species-discovery/ — SCHOLARLY (16%/5 yr; >half of 70,000 undescribed already collected)
  - Goodwin et al., *Current Biology* 25:R1066–R1067 (2015), https://ora.ox.ac.uk/objects/uuid:f1e0fc2f-05f6-4c4e-958e-fab71939ed8c — SCHOLARLY (≥58% wrong names in African gingers; >50% tropical estimate)
  - https://hal.inrae.fr/hal-03338823/document — SCHOLARLY (herbarium-identification challenge; CNN MRR 0.011 vs 0.180 with domain adaptation)
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5680669/ — SCHOLARLY (CNNs on digitized collections; 90%/96% accuracies on easier tasks)
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4607853/ — SCHOLARLY (the photo-only description debate, "taxonomic malpractice")
  - https://research-scotland.ac.uk/handle/20.500.12594/23122 — SCHOLARLY (limits of digital images for taxonomy; *Madhuca*)

---

### 5. Structural dark matter in AlphaFold DB

- **Data** — AlphaFold Protein Structure Database (~214M predicted structures,
  CC-BY 4.0, bulk download from EBI), plus two derived public products: the Foldseek
  clustering of the whole database (Barrio-Hernandez et al., *Nature* 622:637–645,
  2023; browser and downloads at cluster.foldseek.com) and TED, The Encyclopedia of
  Domains (Lau et al., *Science* 2024; ~365M domains, Zenodo releases including a set
  of candidate novel-fold PDB files).
- **Question / what a find looks like** — A structural cluster or domain family with no
  relative in the PDB, no Pfam annotation, and a coherent, non-trivial fold — ideally
  one whose members' genomic context suggests a function. A find is a new fold or
  superfamily that survives expert scrutiny, better still one with a functional
  hypothesis a wet lab would test.
- **Gap evidence** — The gap is stated numerically by the people who made the
  resources: Barrio-Hernandez et al. report 2.30M non-singleton structural clusters of
  which **31% lack annotations**, "representing probable previously undescribed
  structures". TED reports ~20% of domains with no PDB-based relative and **>7,000
  candidate novel folds** released as a file set, plus >10,000 new structural
  interactions between superfamilies. These are explicitly piles of unexamined
  candidates, not finished results — Durairaj et al. (*Nature* 622:646–653, 2024's
  companion) shows what finishing one looks like: the β-flower fold, new Pfam families,
  and an experimentally demonstrated new toxin–antitoxin superfamily (TumE–TumA).
- **Verifier** — Partly mechanical, which is unusual and good: structure-structure
  search against PDB and against the clusters themselves (Foldseek), AlphaFold's own
  pLDDT/PAE confidence, whether the fold is reproduced by an independent predictor,
  whether the family shows covariation consistent with the fold, and whether genomic
  neighborhood is conserved across distant taxa. Final arbitration is a structural
  bioinformatician plus, for a function claim, a wet-lab experiment — which a hobbyist
  does not have.
- **Precedent** — Durairaj et al. 2023/2024 (β-flower; TumE–TumA) is a real discovery
  made exactly this way, from predicted structures already in the public database.
- **Recipe** — Code: download the TED candidate-novel-fold set and the unannotated
  Foldseek clusters; filter hard on prediction confidence (low pLDDT regions are the
  dominant artifact); Foldseek them against PDB and against each other; keep families
  with ≥N members across ≥M phyla; pull the source organisms and gene neighborhoods
  from UniProt/ENA. LLM: reads the literature for each surviving family to check it is
  not a known thing under another name, reads genomic context into a function
  hypothesis, and writes it up — this is the part where an LLM is actually strong,
  because the bottleneck is reading, not computing.
- **Cost** — The derived products are the cheap entry point: the TED novel-fold release
  is thousands of PDB files, not 214M structures. Foldseek is CPU-capable and fast. A
  laptop-to-small-VM job, days not weeks, no GPU. Downloading all of AlphaFold DB is
  terabyte-scale and unnecessary.
- **Traps** — (i) **Low-confidence predictions that look like folds.** This is the
  field's dominant false positive; disordered and low-pLDDT regions produce
  plausible-looking novel topologies that are artifacts. (ii) Coiled coils, repeats and
  low-symmetry structures get called "novel" by automated pipelines — the follow-up
  literature on TED's candidates is specifically about separating these. (iii)
  "Unannotated" ≠ "unknown": many clusters lack a Pfam hit because annotation lags, not
  because the protein is new. (iv) Novel fold ≠ novel function; a fold claim with a
  speculative function attached is where this field's hype lives.
- **Crowding** — `CROWDED`. Beltrao, Steinegger, Orengo and their groups are working
  this corpus directly, the resources were built by them for this purpose, and the
  obvious candidates are being picked. A hobbyist's realistic play is a narrow
  taxonomic or functional slice nobody has prioritized, and the honest expectation is
  a contribution to someone else's pipeline rather than a solo find.
- **Ethics** — Clean. Public structures, CC-BY, no human-subject dimension. The only
  flag: a function claim with biosecurity implications should not be published
  casually; stay away from toxin and virulence-factor families, which is also where the
  interesting findings cluster — note it and choose a different slice.
- **Scores** — `data_ready` 5, `gap` 3, `verifier` 4, `cheapness` 4, `payoff` 3,
  `ethics_clear` 4.
- **Sources**
  - Barrio-Hernandez et al., *Nature* 622:637–645 (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10584675/ — SCHOLARLY (2.30M non-singleton clusters, 31% unannotated; cluster.foldseek.com)
  - Durairaj et al., *Nature* 622:646–653 (2023/2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC10584680/ — SCHOLARLY (β-flower fold; TumE–TumA)
  - Lau et al., *Science* (2024) doi 10.1126/science.adq4946, https://research.unipd.it/retrieve/78efa495-e8c1-4501-800f-89382d5f4640/Accepted_version_TED.pdf — SCHOLARLY (TED; ~365M domains, thousands of new folds, >10,000 new superfamily interactions)
  - https://zenodo.org/records/10848710 and https://zenodo.org/record/13908086 — PRIMARY (TED releases; 7,427 candidate-novel-fold PDB files)
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12688089/ — SCHOLARLY (follow-up on >7,400 candidate novel folds; low-symmetry caveat)

---

### 6. iNaturalist's open dataset as a pre-screen for undescribed and out-of-range taxa

- **Data** — `s3://inaturalist-open-data` (AWS Registry of Open Data, us-east-1,
  `--no-sign-request`, no account needed): four monthly-refreshed metadata files
  (observations, observers, photos, taxa) plus the image objects. Licenses are CC or
  CC0 and vary per photo, recorded in the metadata. A 2021-era community post gives
  ~42.3M observations / ~70.3M photos; the metadata files were then 1.6 GB and 2.9 GB
  compressed. Current totals are larger — I did not verify them (see Unverified
  claims).
- **Question / what a find looks like** — (a) An observation that is not any described
  species, spotted by a specialist from the photo. (b) A credible record far outside a
  species' documented range — the first record for a country, or evidence of an
  establishing introduced population. (b) is the realistic, frequent payoff.
- **Gap evidence** — Weaker than the other candidates, and worth saying so. The
  platform's community already triages observations hard, so "nobody has looked" is
  less true here than in a museum drawer. What is plausibly unlooked-at: the
  "needs ID"/coarse-identification tail in under-birded and under-recorded taxa
  (invertebrates, fungi) and in regions with few local identifiers.
- **Verifier** — A taxonomist in the group, and in most cases a *specimen*: the
  published cases that ended in a formal name did so after someone went and collected
  the animal or plant. Describing from photographs alone is possible but contested —
  the 2021 *Journal of Orthoptera Research* pygmy grasshopper was described from
  iNaturalist photographs *without a formal name* precisely because of this norm.
- **Precedent** — Real and multiple: *Linaria alfercensis*, a toadflax photographed by a
  tourist in Monchique, Portugal and flagged from the iNaturalist upload by botanist
  João Farminhão; *Inimia nat*, a new mantis **genus** from a Queensland photo, named
  for the iNaturalist community; *Gasteruption mamburrumurl*, a wasp confirmed new from
  an NT photograph and named with the Jawoyn Association; the unnamed Peruvian
  *Scaria* grasshopper known only from photographs. The pattern in every case: photo
  first, specialist second, specimen third.
- **Recipe** — Code: pull the metadata files, join observations to taxa and photos,
  select records whose identification is coarse (genus or above) or whose location is
  far outside the GBIF-documented range for the identified taxon; rank by image quality
  and by how few identifiers work on that group. LLM: reads the images and the
  observation comments to filter the obvious (captives, cultivated plants, misIDs of
  common things), drafts a per-record dossier, and identifies which specialist to
  contact. The LLM's identification is a *triage signal only* and must never appear in
  the dossier as a determination.
- **Cost** — Trivial: a few GB of metadata, a laptop, hours. Images are pulled
  selectively.
- **Traps** — Captive, cultivated and planted organisms generating fake range records;
  geotag errors and obscured coordinates (iNaturalist deliberately obscures locations
  for sensitive taxa, so apparent range outliers can be artifacts of obscuring); photos
  of dead/transported specimens; the long tail of "new to me" that is well known to the
  relevant specialist. And the social trap again: specialists in small groups are
  flooded with low-quality tips, so volume is the enemy of credibility.
- **Crowding** — `CROWDED`. This is a citizen-science platform whose entire design is
  people looking at these observations, with an active identifier community and
  automated computer-vision suggestions built in. Listed because the precedent is
  strong and the cost is near zero, not because the field is empty.
- **Ethics** — Observer photos are licensed but authorship matters: credit the observer,
  and in the published cases the observer is a co-author or acknowledged. Respect
  obscured coordinates for sensitive species and never attempt to de-obscure them.
  Honor per-photo licenses. No human-privacy payoff is involved; photos incidentally
  containing people are not the target and should not be analyzed.
- **Scores** — `data_ready` 5, `gap` 2, `verifier` 2, `cheapness` 5, `payoff` 2,
  `ethics_clear` 4.
- **Sources**
  - https://registry.opendata.aws/inaturalist-open-data — PRIMARY (bucket, `--no-sign-request`, four metadata files, CC/CC0 per-photo licensing, monthly refresh)
  - https://forum.inaturalist.org/t/getting-the-inaturalist-aws-open-data-metadata-files-and-working-with-them-in-a-database/22135 — POPULAR (schema walkthrough; the ~42.3M/~70.3M figures, 2021-era)
  - https://doaj.org/article/f2b235df124d45ef9fb2ad84d3e764c8 — SCHOLARLY (*J. Orthoptera Research* 2021; Peruvian pygmy grasshopper described from iNaturalist photos, left unnamed)
  - https://petapixel.com/2026/09/25/tourists-photo-accidentally-leads-to-discovery-of-new-flower-species/ — POPULAR (*Linaria alfercensis*, Monchique; Farminhão)
  - https://wildlife.org.au/extraordinary_discoveries/ — POPULAR (*Inimia nat*; *Gasteruption mamburrumurl*)
  - https://nhmu.utah.edu/articles/five-surprising-discoveries-made-inaturalist — POPULAR

---

### 7. Archived wildlife-sound collections, mined for vocal species limits

- **Data** — xeno-canto (community bird/insect/bat sound archive; per-recording
  licenses, each recording's license linked in its metadata; an HTTP API with v2
  endpoints wrapped by several Python/JS clients, and a newer "more full-featured API"
  per their own documentation, which also notes the old simple web service "is not
  recommended for new projects") and the Macaulay Library (Cornell; browse and
  download via eBird/Macaulay interfaces, terms more restrictive than xeno-canto).
  Regional archives (WikiAves for Brazil) add coverage. I could not verify current
  recording totals or the archive-wide license — see Unverified claims.
- **Question / what a find looks like** — A taxon whose archived recordings fall into
  discrete, geographically coherent vocal types that do not grade into each other,
  indicating unrecognized species limits. Birds are the target because vocal diagnosis
  carries real weight in avian taxonomy.
- **Gap evidence** — The archives were built by recordists documenting birds, not by
  taxonomists testing limits, and most species have never had their archived
  recordings analyzed as a dataset. The demonstrated workflow exists but has been
  applied to a tiny number of taxa.
- **Verifier** — An avian systematist, and in practice a taxonomic committee (SACC,
  AOS, IOC) — plus, for a strong case, concordance with specimens and with genetic
  data. The mechanical part is real though: discreteness of vocal clusters and their
  geographic coherence are computable and falsifiable, and the field accepts
  spectrographic evidence as a line of argument.
- **Precedent** — The *Chamaeza campanisona* (Atlantic Forest) study: 183 recordings
  from Macaulay Library, WikiAves and xeno-canto combined with museum specimens,
  spectrographic analysis plus a deep neural network, yielding three discrete loudsong
  types with discrete geographic distributions and support for recognizing two
  diagnosable species under the Phylogenetic Species Concept. Also the West African
  cases in the *Bulletin of the BOC* and a published vocal comparison of *Corvus enca*
  subspecies using xeno-canto and Macaulay recordings.
- **Recipe** — Code: pull all recordings for a target genus with coordinates; segment
  and measure standard call parameters (note count, frequency bounds, pace, note
  shapes) and/or embed with a bioacoustic model; cluster; test discreteness and map.
  LLM: reads the taxonomic literature for the genus to find which limits are already
  contested (candidate selection is the whole art), reads recordists' notes for
  context, drafts the paper. Code computes; the LLM must not declare a split.
- **Cost** — Very cheap: hundreds of recordings per genus, laptop, hours. No GPU.
- **Traps** — Recording quality and equipment vary wildly and confound frequency
  measurements; geographic sampling is driven by where recordists go, so apparent
  discreteness can be a sampling gap (this is the central trap and the main reason
  such papers get rejected); individual, seasonal and dialect variation; mislabeled
  recordings; playback-elicited vocalizations differing from spontaneous ones.
  Taxonomic inflation from vocal characters alone is a live controversy, not a settled
  method.
- **Crowding** — `PARTLY`. Neotropical ornithology does this actively and well; the
  `OPEN` space is under-studied regions and non-passerine or non-bird groups (bats,
  Orthoptera) where fewer people combine the archives.
- **Ethics** — Honor per-recording licenses and credit recordists (the convention in
  this literature is to list them). Macaulay's terms are more restrictive than
  xeno-canto's — check before bulk download. Do not publish precise localities for
  taxa at risk from trapping, which is a real problem for Asian songbirds.
- **Scores** — `data_ready` 4, `gap` 3, `verifier` 3, `cheapness` 5, `payoff` 3,
  `ethics_clear` 4.
- **Sources**
  - https://xeno-canto.org/article/153/preview — PRIMARY (API documentation; old service deprecated, per-response totals)
  - https://www.scielo.br/j/zool/a/qbw4QyRkb8jWncVfBtgsPSP/?lang=en — SCHOLARLY (*Chamaeza campanisona*; 183 archive recordings + specimens + DNN; two diagnosable species)
  - https://bioone.org/journals/Bulletin-of-the-British-Ornithologists-Club/volume-139/issue-2/bboc.v139i2.2019.a7/Two-undescribed-species-of-bird-from-West-Africa/10.25226/bboc.v139i2.2019.a7.pdf — SCHOLARLY (two undescribed West African birds)
  - https://www.hbw.com/node/1271489 — SCHOLARLY/SECONDARY (xeno-canto + Macaulay vocal comparison, *Corvus enca*)

---

### 8. "Dark taxa" in DNA barcode reference libraries

- **Data** — BOLD Systems (Barcode of Life Data System), University of Guelph: the
  Public Data Portal needs no account, and BOLD now offers data packages in Parquet,
  with an official R client (`BOLDconnectR`, first CRAN release 2025-09-17) that
  retrieves records by BIN, project code or geography. BOLD assigns Barcode Index
  Numbers (BINs) monthly, only to COI sequences >500 bp with <1% ambiguous bases. v3
  listed 1,422,394 animal BINs and is scheduled for retirement 2026-06-30; current v5
  totals I could not verify (see Unverified claims).
- **Question / what a find looks like** — BINs are operational species proxies, and a
  large share have no Linnaean name — the "dark taxa". A find is not a new BIN (the
  pipeline makes those automatically); it is a *linked* find: a nameless BIN tied to
  specimens, morphology and a geography well enough that a taxonomist can describe it,
  or a BIN that reveals a cryptic complex inside a named species.
- **Gap evidence** — BOLD's own documentation frames dark taxa as "the millions of
  species lacking a scientific name" and says BINs were developed partly to handle
  them. A 2016 analysis attributes a visible drop in the named fraction of GenBank
  around 2010 to BOLD barcodes without formal names, and states that fewer than half
  of newly sequenced invertebrate taxa entering GenBank are identified to species.
- **Verifier** — A taxonomist plus the physical voucher, which BOLD records point to.
  The mechanical part — that a BIN is distinct, monophyletic and stable — is already
  computed by BOLD; what is not computed is whether it corresponds to a species, and
  that is exactly where the field's live argument sits.
- **Precedent** — Negative as much as positive, and that is the useful part. Sharkey et
  al. (2021) converted >99% of 390 BINs into named species (387 of 390) in a
  "minimalist revision"; a published re-analysis argued in response that "BINs do not
  deserve names" and that BOLD needs a stronger commitment to open science. The
  original authors' reply was that BINs and species concepts match for well over 90% of
  species but that "this matching does not equate to equality." Anyone entering this
  space should read that exchange before writing a line of code: it is the clearest
  statement of the verifier problem in the whole survey.
- **Recipe** — Code: pull a clade's public records (Parquet or `BOLDconnectR`), build
  per-BIN summaries — geography, host/habitat fields, voucher institution, sequence
  divergence to the nearest named BIN — and rank nameless BINs by how well-documented
  and how deeply divergent they are. LLM: reads the group's revisions to find which
  nameless BINs fall in genera with an active monographer, reads voucher metadata, and
  writes the dossier. The LLM does not assign species status.
- **Crowding** — `CROWDED` and contested. BOLD's own consortium, iBOL's BIOSCAN, and
  the dark-taxa literature are all on this, and the methodological dispute is
  unresolved. Listing it mainly because the data access is genuinely easy and because
  the dispute itself is a useful calibration case (Rule 7).
- **Traps** — NUMTs, heteroplasmy and *Wolbachia*-driven mitochondrial sweeps make COI
  divergence a poor species proxy in some groups; contamination and misassociated
  vouchers; the single-locus problem generally; and the strong incentive toward
  taxonomic inflation that the Sharkey exchange documents. Also, much of BOLD's richest
  data is private to projects, so a public-portal sweep sees a biased subset.
- **Ethics** — Nagoya again, sharply: barcode records carry country of origin and
  collecting permits, and describing species from another country's material without
  its researchers is the central grievance in this literature. No privacy dimension.
- **Scores** — `data_ready` 4, `gap` 3, `verifier` 2, `cheapness` 5, `payoff` 2,
  `ethics_clear` 3.
- **Sources**
  - https://arxiv.org/pdf/2404.05696 — SCHOLARLY (BOLD v4 platform paper; dark taxa framing, BIN system)
  - https://v3.boldsystems.org/?taxid=30 — PRIMARY (1,422,394 animal BINs; v3 retirement 2026-06-30; public portal needs no account)
  - https://sameerpadhye.r-universe.dev/api/packages/BOLDconnectR — PRIMARY (official R client, 2025)
  - https://www.biorxiv.org/content/10.1101/2021.04.28.441626.full.pdf — SCHOLARLY (re-analysis: "BINs do not deserve names"; the 387/390 figure)
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC4971186/figure/RSTB20150334F4 — SCHOLARLY (named fraction of GenBank; <half of new invertebrate taxa named)

---

### 9. Historical pathogen records in already-published ancient-DNA read sets

*Listed with a deliberate narrowing: the find here is a historical/archaeological
claim about disease in the past, from sequence data already published by its
authors. Anything touching the characterization or reconstruction of hazardous
agents is out of scope and not pursued; see Ethics.*

- **Data** — Shotgun sequencing data from ancient human and animal remains, deposited
  in ENA/SRA by the groups that generated it. Population-scale aDNA datasets of
  thousands of individuals are now public.
- **Question / what a find looks like** — Microbial sequence present in a dated
  archaeological individual, establishing the presence of a disease in a time and
  place where it was not previously documented. The payoff is historical: when a
  disease reached a region, how it tracked migration or animal domestication.
- **Gap evidence** — The practice is to analyze the *human* genome and leave the rest
  of the reads unexamined; the pathogen screens that have been run were run years after
  the data were published, on data generated for population genetics. Sikora et al.,
  *Nature* 643:1011–1019 (2025) screened 1,313 ancient Eurasian individuals spanning
  37,000 years and got 5,486 hits against 492 species in 136 genera, 3,384 of them
  known human pathogens, "many of which had not previously been identified in ancient
  human remains". That is one screen over one curated set; aDNA deposition continues.
- **Verifier** — Good and well-codified by the field, which is why this candidate is
  listed at all. (a) Authenticity: aDNA damage patterns (C→T deamination at read ends)
  distinguish ancient molecules from modern contamination — the HOPS tool evaluates
  each read for both pathogen specificity and ancient origin. (b) Even read
  distribution across the reference genome, not pileups on conserved or repetitive
  regions. (c) Negative controls and the laboratory's own blanks. (d) Replication from
  an independent extract or individual. (e) A paleogenomicist. The field's own base
  rate is sobering and useful: a screen of nearly 3,000 archaeological samples yielded
  only eight ancient *Salmonella* infections.
- **Precedent** — Rasmussen et al. (*Cell*, 2015) screened ~89 billion raw reads
  previously generated from the teeth of 101 Bronze Age individuals (Allentoft et al.
  2015) and found seven individuals carrying *Yersinia pestis*-like sequence — the
  textbook case of a major result obtained entirely by re-reading someone else's
  published reads. Sikora et al. 2025 is the industrial-scale version.
- **Recipe** — Code: fetch read sets, run an established authenticated screening
  pipeline (HOPS/MALT-style, which exists precisely for this and already encodes the
  damage and evenness checks), and report hits with their authenticity statistics.
  LLM: reads the archaeological context — dating, site, burial, the excavation
  literature — which is where the historical claim actually lives and where an LLM
  that reads a lot is useful. All statistics come from the pipeline, never from the
  model (Rule 6).
- **Cost** — Moderate: read sets are GB-to-tens-of-GB each, the screening pipelines
  want tens of GB of RAM and a large reference database on disk. A handful of
  individuals is a laptop-plus-patience job; a hundred is a cloud VM for a few days.
  No GPU.
- **Traps** — Modern laboratory and environmental contamination is the dominant
  false-positive mode and the reason the authenticity criteria above are
  non-negotiable; reference-database bias makes reads map to the best available
  relative rather than the true organism; environmental relatives of pathogens in soil
  produce spurious hits; low-coverage hits cannot distinguish species within a genus.
  The field has a real history of early claims later attributed to contamination,
  which is why its own screens report such low positive rates.
- **Crowding** — `CROWDED`. This is a well-funded specialty (Jena/MPI, Copenhagen,
  Oxford) with purpose-built tools, and the obvious datasets have been screened. A
  realistic `PARTLY` opening is newly deposited read sets not yet included in a screen,
  and non-human (livestock, commensal) aDNA, which gets less attention.
- **Ethics** — The heaviest in this survey, and it is what bounds the candidate.
  (a) Ancient human remains are ancestral remains: descendant and Indigenous
  communities have standing over how data about them is used, and NAGPRA-style
  consultation and community consent are the norm in the field, not a formality.
  (b) No reidentification: these are human genomes, and nothing here touches living
  individuals' genetic privacy — any question whose payoff involves identifying people
  is dropped under the brief. (c) Scope limit: the find is "this disease was present
  here, then". Work aimed at characterizing what makes an agent dangerous, or at
  reconstructing one, is not a data-survey question and is excluded. (d) Framing: claims
  about disease in a named ancient population are claims about the ancestors of living
  people and should be written with that in mind.
- **Scores** — `data_ready` 4, `gap` 3, `verifier` 4, `cheapness` 3, `payoff` 3,
  `ethics_clear` 2.
- **Sources**
  - Sikora et al., *Nature* 643:1011–1019 (2025), https://ideas.repec.org/a/nat/nature/v643y2025i8073d10.1038_s41586-025-09192-8.html — SCHOLARLY (1,313 individuals, 37,000 years, 5,486 hits / 492 species / 136 genera)
  - Rasmussen et al., *Cell* (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4644222/ — SCHOLARLY (~89 billion previously published reads rescreened; 7 of 101 individuals)
  - https://sites.duke.edu/clubevmed/2024/05/02/pathogens-through-space-and-time-lessons-from-high-throughput-screening-for-ancient-pathogen-dna-2/ — SECONDARY (HOPS read-level authenticity criteria; 8 positives from ~3,000 samples)
  - Mühlemann et al., *Nature* 557:418–423 (2018), https://www.cam.ac.uk/research/news/oldest-genetic-evidence-of-hepatitis-b-virus-found-in-ancient-dna-from-4500-year-old-skeletons — SCHOLARLY/SECONDARY (shotgun data from ancient remains; 25 of the skeletons positive, 12 analyzable)

---

### 10. Camera-trap and museum-CT archives — listed and down-scored

Two candidates from the brief's list that I checked and am recording as weak, with the
reason, rather than padding them into full entries.

- **Camera-trap archives (LILA BC).** Data are genuinely ready: LILA hosts dozens of
  labeled sets — Snapshot Serengeti at ~7.1M images in 2.65M sequences, a 3.7M-image
  North American set, Wellington at 270,450 images — mirrored on Source Cooperative,
  with permissive licenses and an active ML community. But I could not find a single
  case of a new species or a documented range extension produced by *reanalysis of an
  archived* camera-trap corpus; the literature on these datasets is about recognition
  benchmarks. The images are also already labeled by the projects that collected them,
  so the "nobody looked" premise largely fails. Scores: `data_ready` 5, `gap` 2,
  `verifier` 3, `cheapness` 4, `payoff` 2, `ethics_clear` 4 — with the ethics caveat
  that camera traps incidentally photograph people, so any sweep must discard human
  images without analyzing them, and that precise locations of poaching-sensitive
  species should not be published.
  Sources: https://source.coop/agentmorris/lila-wildlife (PRIMARY),
  https://lila.science/datasets/ (PRIMARY),
  https://arxiv.org/pdf/2005.00116 and https://arxiv.org/pdf/2206.12458 (SCHOLARLY, dataset sizes).
- **MorphoSource CT archives.** The repository is real and large (e.g. a deposited
  collection of 489 non-human-primate scans from 431 specimens across 59 species), and
  3D "cybertypes" are an established practice — the centipede *Eupolybothrus
  cavernicolus* was described with micro-CT deposited in MorphoSource, and myriapod
  type specimens have been published as full 3D datasets. But in every case I found,
  the scan was *made for* the description. I found no case of a new taxon recognized
  inside pre-existing scans of a differently-motivated study, which is the premise
  this candidate needs. Add that scan access on MorphoSource is frequently
  permission-gated per specimen by the owning institution, so "public and
  machine-readable now" only partly holds. Scores: `data_ready` 2, `gap` 3,
  `verifier` 3, `cheapness` 3, `payoff` 3, `ethics_clear` 4 — ethics caveat: human and
  hominin specimens in the repository carry descendant-community and
  repatriation sensitivities, so stay in non-human material.
  Sources: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4736502/ (SCHOLARLY, primate CT collection),
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6029791/ (SCHOLARLY, myriapod 3D cybertypes),
  https://publikationen.ub.uni-frankfurt.de/files/43892/BDJ_article_1013.pdf (SCHOLARLY, *E. cavernicolus*).

---

## Pilot in a day

**Candidate 1, narrowed: sweep Logan contigs for obelisk-like RNA elements outside the
described phylogeny, in a non-human metatranscriptome slice.**

Chosen because it is the only candidate in this domain with a verifier that does not
require another person's ship, drawer or microscope on day one: a hit can be
independently re-assembled from raw reads and placed on a tree by the same person who
found it. The Logan paper already reports a 3.7× expansion of obelisks as a
*byproduct*, which both proves the signal is there and tells you the authors did not
treat it as their main result.

Steps, from a Linux container with internet, Python, no GPU:

1. **Get the query set.** Download the obelisk sequences and Oblin protein alignments
   from the paper's deposited files: `https://purl.stanford.edu/wb363nt3637` (Zheludev
   et al. data and analysis). Build (a) a nucleotide k-mer set (k=31) from
   representative obelisk genomes and (b) an HMM from the Oblin-1 protein alignment
   (`hmmbuild`). The HMM is the sensitive query; the k-mers are the fast filter.
2. **Install tooling.**
   `pip install rcgrep`; install `zstd`, `hmmer`, `seqkit`, and the AWS CLI
   (`aws` works anonymously with `--no-sign-request`). Optionally build
   `back_to_sequences` (Rust) for many-query searches.
3. **Pick the accession slice.** Do *not* try to sweep 38M accessions. Either
   (a) query `https://logan-search.org/` with a few obelisk k-mers and take the
   returned accession list, or (b) pull SRA metadata for `library_strategy=RNA-Seq`
   with a metatranscriptomic/environmental organism field, restricted to non-human
   sources, and take 10,000–50,000 accessions. Record the list to a file; it is the
   experiment's definition.
4. **Stream and search.** For each accession:
   ```
   aws s3 cp s3://logan-pub/c/<ACC>/<ACC>.contigs.fa.zst - --no-sign-request \
     | zstdcat | <filter>
   ```
   First pass: `rcgrep` (it searches reverse complements, which matters) or
   `back_to_sequences --in-kmers query.fa`. Second pass on survivors only: 6-frame
   translate and `hmmsearch` the Oblin HMM. Keep hits, discard the stream. Verify the
   path pattern first on the documented example,
   `https://s3.amazonaws.com/logan-pub/c/SRR11905265/SRR11905265.contigs.fa.zst`.
   Run inside `us-east-1` if renting a VM — the bucket is there, and egress is free.
5. **Triage.** Cluster hit contigs at 90% identity (matching the paper's clustering so
   the comparison is like-for-like), drop anything ≥90% identical to a published
   obelisk, and keep candidates ~1 kb with a predicted rod-like fold (RNAfold) and an
   ORF that hits the Oblin HMM weakly but significantly.
6. **Verify — the part that makes it a result rather than a BLAST hit.** For each
   surviving candidate: (a) fetch the raw reads for its source accession from SRA and
   re-assemble independently (`megahit` or `spades`), confirming the contig is not an
   artifact of Logan's assembler; (b) require ≥3 independent accessions, ideally from
   different submitting projects, before the candidate is called anything; (c) check
   what else was on the same run and the same BioProject for a contamination story;
   (d) build an Oblin phylogeny placing the candidates relative to the published
   families. Everything in this step is code, and its outputs get checked in, per
   Rule 6.
7. **Write it down honestly.** The expected outcome of one day is *not* a new element
   class. It is: a defined accession slice, a reproducible pipeline with its output,
   and either a shortlist of candidates with their verification status or a clean
   negative — "this slice contains no obelisk-like element outside the described
   families, at this sensitivity." Both are results. A named wall — e.g. "the
   sensitive search is HMM-bound and the slice beyond 50k accessions needs
   in-region compute" — is a finished result under Rule 8.

Ethics for the pilot, concretely: restrict the accession list to non-human sources at
step 3 and drop any human-derived run that slips through; make no attempt to genotype
or re-identify any sample; note country of origin for any organism-associated find,
per the DSI/Cali Fund discussion in candidate 1.

---

## Unverified claims

- **Logan's data license.** The project page states the data are public, hosted on
  `logan-pub` with anonymous access and no AWS account needed, and the AWS Registry of
  Open Data lists the dataset — but neither the GitHub page nor the material I fetched
  states an explicit license for the assemblies. Treat the license as unverified; check
  the registry entry's license field and the Logan paper before any redistribution or
  commercial use.
- **Current size of the NOAA NCEI passive-acoustic archive.** I verified the bucket's
  structure and collection list directly, but the only size figures I found are
  "over 100 TB" from a 2021 *Frontiers in Marine Science* paper, "close to 300
  terabytes" for SanctSound alone from an undated trade article, and ">500 TB /
  ~200,000 hours" for NOAA's North Pacific recorder network from NOAA-linked coverage.
  The archive-wide current total is not established here. NCEI directs enquiries to
  `pad.info@noaa.gov`.
- **Google whale model license.** The model is distributed via Kaggle Models and
  Google's blog describes it as available for download, but I did not verify the
  license terms. "Open" in the sense of a permissive license is unconfirmed; check the
  Kaggle model card.
- **xeno-canto totals, license, and API version.** I could not verify the current
  number of recordings, any archive-wide license (their own metadata links a license
  per recording, which implies there is no single one), or the existence of a "v3" API.
  The documentation I did reach describes an older simple web service as deprecated and
  a newer fuller API, without a version number I could confirm.
- **Current BOLD v5 record and BIN totals, and the share of BINs lacking species
  names.** The 1,422,394 animal-BIN figure is from the v3 interface, which is slated for
  retirement in June 2026. I found no current v5 figure, and no published current
  percentage of nameless BINs; the closest is a 2016 statement that fewer than half of
  newly sequenced invertebrate taxa entering GenBank are named to species. The widely
  repeated framing of "millions of dark taxa" is BOLD's own documentation language, not
  a measured count.
- **Current iNaturalist open-dataset totals.** The ~42.3M observations / ~70.3M photos
  figures are from a community forum post of roughly 2021 and are certainly now low.
  The registry entry confirms monthly metadata refreshes but I did not read current
  counts out of the metadata files.
- **LILA BC aggregate size.** Individual dataset sizes are sourced above; I found no
  figure for the collection's combined image count, and one benchmark page explicitly
  says it "varies by dataset."
- **"New species found by image models in digitized collections."** The brief listed
  "misidentified specimens found by image models" as a precedent. I could not find a
  study that uses a vision model to flag misidentified herbarium specimens in
  GBIF/iDigBio and reports an error rate. What exists is adjacent: CNNs detecting
  mercury staining (~90%) and discriminating two plant families (~96%), and the 2021
  challenge showing models trained on field photos transfer badly to herbarium sheets.
  Candidate 4's premise therefore rests on Goodwin's measured misidentification rate,
  not on a demonstrated ML pipeline. Recorded as reported, not established.
- **Fontaine et al. 2012 "shelf life" figure.** I looked for the commonly cited
  ~21-year average lag between collection and description and could not retrieve the
  paper. The Bebber et al. figures above (16% within five years; a quarter from
  specimens >50 years old) are verified and carry the same point; I have not used the
  Fontaine number.
- **Whether a new taxon has ever been recognized inside pre-existing MorphoSource
  scans.** I searched and found only scans made for the description at hand. Absence of
  evidence here, not evidence of absence — but the candidate's premise is unsupported
  as of this survey, which is why it is down-scored in candidate 10.
- **No reanalysis-driven camera-trap discovery found.** Same status: searched, not
  found, recorded rather than assumed either way.
- **Cali Fund contribution rate.** The 0.1%-of-revenue / 1%-of-profit indicative rate
  comes from the CBD's own guidance documents and secondary reporting of COP16 Decision
  16/2; I did not read the decision text itself.
