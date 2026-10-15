# Untouched data: astronomy and planetary science public archives

*2026-10-15. Domain survey for `BRIEF.md`. No discoveries attempted (Rule 9).*

**Verification note.** In this session WebFetch failed on DNS for every host and
direct `curl` was refused by the egress proxy, so no page was opened. Every claim
below was checked only through WebSearch result summaries, and I ran out of
search budget before finishing. Scores rest on those summaries, and the tier
given is the tier of the underlying page. Anything I could not confirm that way
is listed under `## Unverified claims`. A later session with working fetch
should re-open the top sources for the three highest-scored candidates before
acting on them.

## Summary: best bets

1. **Precovery of known near-Earth asteroids in archival survey images (ZTF,
   DECam, old plates).** This has the best verifier in the domain: an orbit fit
   either accepts the new positions or it does not, and the Minor Planet Center
   (MPC) is the registry. Precedent goes from a citizen project that improved 551
   NEA orbits up to the 2016 precoveries of 2024 YR4. Partly crowded by B612's
   ADAM::Precovery. **This is the pilot.**
2. **TESS full-frame images: long-period and shallow transits that the SPOC and
   QLP pipelines missed.** This is the Rabtsevich/Claude precedent from October
   2026, with Planet Hunters TESS before it. The verifier exists (ExoFOP CTOI,
   then TFOP and a predicted transit) but is slow. Crowding is growing quickly.
3. **Gaia DR4, due 2 December 2026.** The first epoch astrometry and photometry
   for about 1.8 billion sources. For a few weeks there will be a real
   first-look gap. The verifier is radial-velocity or catalog follow-up, so it
   is weak for hobbyists.
4. **Century-baseline plate archives (DASCH DR7, APPLAUSE DR4).** The data are
   large and finished, and few people have looked at them. The traps are
   severe: emulsion systematics produced the disputed Boyajian's Star "dimming"
   and the VASCO "vanishing stars."
5. **Spacecraft image archives (LRO NAC, HiRISE/CTX, Voyager/Cassini).** Real
   amateur precedents exist (Vikram debris, Despina's shadow), and a re-imaging
   request is the verifier. The payoff is small and specific. SETI
   reanalysis and CNEOS/IM1 are recorded here mainly as **traps**.

## The prompt's precedent: "I think I found a planet nobody knew existed" (Oct 2026)

- **Who/what.** Pavel Rabtsevich, described as a product manager in Spain with no
  astronomy training, used Claude Code and OpenAI Codex on public TESS data.
  He posted on X on about 7 October 2026 and in r/ClaudeAI. Coverage ran
  8–11 Oct (Gizmodo, Journal du Geek, Cybernews, The420, egamers, explainx).
- **Claim.** A transit-like dip on **TIC 4206066**, a star slightly smaller than
  the Sun about 116 ly away. The dip is about 0.05% deep, lasts about 2 hours,
  and repeats every **3.18 d**. If it is a planet, its radius is about 1.4 R⊕.
  The signal is in TESS sectors from 2018, 2020 and 2025. A weaker second
  signal has an 11.13 d period. He reports about two weeks of work, "74
  analyses" and more than 1,000 scripts.
- **Conduct.** The good part: he calls them candidates, not validated planets.
  He published dated, preregistered predictions (9 transits expected for signal
  A, 3 for B, with expected depths and outcome categories recovered /
  inconsistent / excluded / insufficient data). He asked the TESS team for
  2-minute-cadence observations, and coverage reports that the request was
  approved as a Director's Discretionary program, observing **31 Oct – 26 Nov
  2026**.
- **Did it hold up?** **Not yet determined.** As of 2026-10-15 the test has not
  run. I found **no ExoFOP TOI or CTOI entry** and no preprint. One explainer
  (explainx) found no NASA or TESS page mentioning the star. A third-party GitHub
  project (`eumemic/exoplanets`, a sweep of about 9,979 nearby K/M dwarfs)
  reportedly recovered both signals blindly, at 3.18278 d and 11.13274 d. That is
  a claimant-grade replication, not vetting. One search summary attributed to
  Scientific American a "solid" verdict from Greg Laughlin and a warning that
  the 2018 dips line up with TESS thruster firings (momentum dumps), a classic
  false-positive source. I could not surface that article directly. See
  Unverified claims.
- **Lesson for the survey.** The work was cheap and the verifier was slow but
  real. The scarce resource was a telescope-time decision, which he obtained by
  writing preregistered predictions. Status: **reported, not established.**

---

### 1. Precovery of known NEAs and comets in archival survey images

- **Data.** These are archives of surveys built for other purposes, mostly
  transients, cosmology and supernovae. ZTF (public DR23, January 2025, about 5
  billion light curves; images are at IRSA). DECam archive (NOIRLab). SDSS.
  Pan-STARRS. Digitized plates (DASCH, APPLAUSE; see #4). Search engines that
  answer "which images could contain object X": CADC **SSOIS** (it covers
  Gemini, Subaru, WISE, HST, SDSS and others) and IRSA's moving-object search
  for ZTF/WISE. The data are public, but each archive has its own licence terms.
- **Question / a find.** A known NEA with a short arc and a poor orbit has
  faint, unreported detections in an image taken years before its discovery.
  You measure them, refit, and the arc grows by years.
- **Gap evidence.** A 2025 preprint on an automated prediscovery pipeline says
  archival precoveries "can extend observational arcs, often by years," which
  implies that most have not been harvested. 2024 YR4 was discovered in
  December 2024. Its 2016 iPTF detections were reported in 2026, more than a
  year after the object became the most-watched impactor candidate (Deen & Lam
  preprint; B612 ADAM::Precovery). So even high-priority objects are not
  exhaustively mined. Detections below the survey's own detection threshold,
  which need forced photometry at the predicted position, are the main gap.
- **Verifier.** Mechanical and strong. Refit the orbit with the new astrometry:
  real precoveries give small residuals (sub-arcsecond) consistent with the rest
  of the arc, and false ones do not. Then submit to the MPC, which publishes
  accepted observations in the MPECs and MPC Circulars. Independent check: JPL
  SBDB orbit update.
- **Precedent.** A Spanish Virtual Observatory citizen project used SDSS images:
  3,226 users, more than 167,000 measurements, 551 NEA orbits improved in 15
  months (SCHOLARLY). EURONEAR / Mega-Archive improved more than 400 NEA orbits
  from 800,000 images (SCHOLARLY). 2024 YR4 precoveries in 2016 iPTF images
  (Deen & Lam, arXiv 2602.06890; B612 submitted 5 observations to the MPC). A
  NAROO/Gaia DR3 study found potentially hazardous asteroid precoveries in plate
  databases that improved orbits and Yarkovsky estimates (SCHOLARLY).
- **Recipe.** Code: pull the poorly constrained NEAs from JPL SBDB; compute
  ephemerides and uncertainty regions for archive epochs; query
  SSOIS/IRSA for covering frames; download cutouts; run forced photometry or
  shift-and-stack at the predicted track; measure centroids against Gaia;
  refit. LLM: write and debug the pipeline, read archive docs, triage cutouts
  flagged by code, draft the ADES submission. The LLM never judges whether a
  blob is the asteroid; the orbit residuals do.
- **Cost.** Laptop. Cutouts are small (MB per object). A day for the pipeline,
  then tens of dollars in tokens. No GPU.
- **Traps.** (a) Detections that are too bright: B612 found some 2016 YR4 hits
  were spurious because magnitudes were too bright. (b) Image artifacts or a
  different asteroid on the predicted track; check against all known objects
  in the frame. (c) Most bright ZTF/Pan-STARRS detections are already reported
  to the MPC by the surveys themselves, so check the object's MPC observation
  list first. (d) Planetary-defense sensitivity: never publicize an impact
  probability yourself; that is CNEOS/ESA NEOCC's job.
- **Crowding.** `PARTLY`. B612 Asteroid Institute (ADAM::Precovery), an
  end-to-end precovery pipeline (Balaji et al. 2026, validated on YR4), EURONEAR,
  and NEO teams at the MPC/JPL. The long tail of ordinary short-arc NEAs and
  main-belt objects in sub-threshold detections remains.
- **Ethics.** Clear. The only caution is the impact-risk publicity noted above.
- **Scores.** data_ready 4, gap 3, verifier 5, cheapness 5, payoff 3,
  ethics_clear 5.
- **Sources.**
  - https://arxiv.org/pdf/1302.5375 (SCHOLARLY: SVO citizen precovery)
  - https://arxiv.org/pdf/2303.03164 and https://arxiv.org/pdf/1905.08847.pdf (SCHOLARLY: EURONEAR archive mining)
  - https://arxiv.org/html/2510.07588v1 (SCHOLARLY preprint: automated prediscovery pipeline)
  - https://arxiv.org/pdf/2602.06890 (SCHOLARLY preprint: YR4 in 2016 iPTF)
  - https://b612foundation.org/?p=30633 (POPULAR/institutional: ADAM::Precovery on YR4)
  - https://tamz.umd.edu/publication/balaji-2026-acm/ (SCHOLARLY: precovery pipeline)
  - https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/8C6CC8AA254675C1EF9A41B084DD5BF9/S1743921315008704a.pdf/solar-system-object-image-search-a-precovery-search-engine.pdf (SCHOLARLY: SSOIS)
  - https://www.aanda.org/10.1051/0004-6361/202348793 (SCHOLARLY: plate precovery of PHAs, via search summary)
  - https://irsa.ipac.caltech.edu/Missions/ztf.html (PRIMARY: ZTF DR23)

### 2. TESS full-frame images: missed long-period and shallow transits

- **Data.** TESS (NASA/MIT) full-frame images at 30, 10 or 3.3 min cadence on
  MAST as FITS. The total is many TB, but per-star cutouts are small (TESScut).
  Light-curve products already exist: QLP high-level science products (for
  example 9.1 million stars for sectors 27–39), TESS-SPOC, and eleanor
  (open-source FFI photometry). Public, NASA data policy.
- **Question / a find.** A periodic or single transit on a star where neither SPOC
  nor QLP produced a TOI. Long periods show only one or two transits per sector;
  shallow signals need several sectors stacked across years.
- **Gap evidence.** Planet Hunters TESS reported about 5 high-quality candidates
  per sector that SPOC and QLP had not found, about two thirds of them
  long-period single transits, because "pipelines typically require two or more
  transit events" (SCHOLARLY). QLP detrended light curves cover stars brighter
  than T = 13.5, so fainter stars get fewer pipeline looks. A 2025 Oxford
  network trained on PHT volunteer votes recovers candidates "missed by current
  automated pipelines" (SCHOLARLY). The October 2026 TIC 4206066 case is itself
  a multi-year, shallow-signal stack.
- **Verifier.** Submit a **CTOI** to ExoFOP. TFOP (seeing-limited photometry,
  high-resolution imaging, radial velocities) vets it, and a predicted transit
  is observed. TESS Director's Discretionary time is possible, as in the
  Rabtsevich case. Statistical validation tools (TRICERATOPS, vespa-type
  false-positive probabilities) are a partial mechanical check. This takes
  months.
- **Precedent.** Planet Hunters TESS I: TOI 813, a Saturn-sized planet on an
  84-day orbit, found by volunteers (SCHOLARLY). PHT II: two-year findings
  (SCHOLARLY). ExoMiner validated 301 Kepler candidates, which shows archived
  candidate lists hold more (SCHOLARLY). TIC 4206066 (Oct 2026, unconfirmed;
  see above).
- **Recipe.** Code: choose a stellar sample (for example nearby M/K dwarfs from
  the TIC); pull TESScut or QLP/SPOC light curves; detrend; run BLS/TLS for
  periodic signals plus a single-dip search; run automatic vetting (odd/even
  depths, secondary eclipse, centroid shift, momentum-dump mask, comparison
  with nearby stars); cross-match against ExoFOP TOIs/CTOIs and known eclipsing
  binaries. LLM: build the pipeline and write the vetting report. A human reads
  the diagnostic plots before any CTOI is submitted.
- **Cost.** Laptop for a few thousand stars. A cloud VM (about $20–100) for
  around 10^5 stars. No GPU needed.
- **Traps.** Momentum dumps and scattered light (reportedly a concern for the
  2018 TIC 4206066 dips). Blended eclipsing binaries from TESS's 21″ pixels, the
  dominant false positive. Stellar variability and flares. Contamination from a
  neighbour, which shows up as a centroid shift. Already-known TOIs and CTOIs
  (check first). Calibrating against cases that went wrong: many PHT and
  community CTOIs end up as eclipsing binaries in TFOP. A single transit gives
  no period, so a confirming re-observation is hard to schedule.
- **Crowding.** `CROWDED` and getting more so: SPOC, QLP, PHT (Zooniverse), many
  ML groups, and after October 2026 a wave of LLM-assisted amateurs, including
  at least one (`eumemic/exoplanets`) sweeping about 10^4 K/M dwarfs. The open
  niche is single transits on fainter stars, beyond QLP's T = 13.5 cutoff.
- **Ethics.** Clear. The main risk is press inflation ("found a planet") ahead
  of vetting, so use preregistered predictions as Rabtsevich did.
- **Scores.** data_ready 5, gap 3, verifier 4, cheapness 4, payoff 3,
  ethics_clear 5.
- **Sources.**
  - https://arxiv.org/pdf/1909.09094 (SCHOLARLY: PHT I, TOI 813, pipeline-miss rate)
  - https://arxiv.org/pdf/2011.13944 (SCHOLARLY: PHT II)
  - https://oatml.cs.ox.ac.uk/publications/202506_Malik_Accelerating_Exoplanets.html (SCHOLARLY)
  - https://ar5iv.labs.arxiv.org/html/2110.05542 (SCHOLARLY: QLP 9.1M stars, T<13.5)
  - https://ar5iv.arxiv.org/html/1903.09152 (SCHOLARLY: eleanor)
  - https://ar5iv.arxiv.org/html/2111.10009 (SCHOLARLY: ExoMiner 301)
  - https://gizmodo.com/did-claude-help-an-amateur-astronomer-discover-a-new-planet-2000824393 (POPULAR)
  - https://www.journaldugeek.com/2026/10/11/claude-code-internaute-affirme-avoir-trouve-planete-dont-personne-soupconnait-lexistence-lenquete-archives-nasa-secoue-reddit/ (POPULAR)
  - https://cybernews.com/tech/claude-code-possible-exoplanet-found-in-nasa-data/ (POPULAR)
  - https://egamers.io/amateur-uses-claude-code-codex-and-nasa-data-to-flag-a-possible-exoplanet-and-tess-will-test-it-in-november/ (POPULAR)
  - https://explainx.ai/blog/claude-code-planet-candidate-tic-4206066-tess-rabtsevich-2026 (POPULAR: "a claim, not a result")
  - https://gist.github.com/MrBoostie/b7a34b9ec96fbfb37e8fd250ba6debba (CLAIMANT: candidate write-up)
  - https://tic4206066.pages.dev/ (CLAIMANT: predictions page)
  - https://github.com/eumemic/exoplanets (CLAIMANT: blind recovery; not opened, repository outside session access)
  - https://x.com/VaibhavSisinty/status/2110347443653185961 (POPULAR: viral summary)

### 3. Gaia DR4 epoch data (release window: 2 Dec 2026)

- **Data.** ESA Gaia, built for astrometry. **DR4 is scheduled for Wednesday
  2 December 2026**, covering the first 66 months. It is the first release
  with **epoch astrometry, photometry and RVS spectra** for the whole catalog.
  DR5 (the legacy release) is no earlier than the end of 2030. Very large,
  public, ESA terms.
- **Question / a find.** The first-look window: astrometric wobble from
  companions (the NASA Exoplanet Archive expects DR4 to be the first large set
  of astrometric exoplanet candidates), dark companions, unusual dippers in
  epoch photometry, and micro-lensing events. Before then, DR3 epoch photometry
  (about 10 million variables) is already public.
- **Gap evidence.** This gap is about timing. Nobody outside the DPAC
  consortium has looked at the DR4 epoch data before release day. The
  consortium's own papers will cover the headline science, and the long tail
  of odd individual objects is usually not covered. A "2026 NYC Gaia DR4
  Sprint" mailing-list post shows professionals preparing to mine it fast.
- **Verifier.** Moderate. Cross-match with published RV surveys and
  Hipparcos–Gaia proper-motion anomaly catalogs; check DR3 versus DR4
  consistency. For companions, the real confirmation is RV follow-up, which a
  hobbyist cannot do. For variables, AAVSO VSX submission or ZTF/ATLAS light
  curves give an independent check.
- **Precedent.** DR2 and DR3 produced a stream of community papers within weeks
  (Gaia BH1/BH2 were found in DR3 astrometric orbits by professionals). I did
  not verify a specific amateur Gaia discovery this session.
- **Recipe.** Before release, prepare queries against the Gaia archive (ADQL)
  and pipelines for epoch astrometry residuals. On release day, run them,
  rank outliers, and cross-match. LLM: ADQL, pipeline, literature cross-check.
  Code: every statistic.
- **Cost.** Moderate. Archive queries are free and bulk epoch data may be large.
  A cloud VM for a few days.
- **Traps.** Known DR4 processing artifacts, which the release documentation
  will list, such as scanning-law patterns and crowding in dense fields.
  Unresolved binaries mimicking planets. Professionals publish within days, so
  a hobbyist "first" is probably already in preparation by DPAC.
- **Crowding.** `CROWDED` after release (DPAC, sprints). `OPEN` only for odd
  individual objects.
- **Ethics.** Clear.
- **Scores.** data_ready 2 (until 2 Dec; then 5), gap 4, verifier 2,
  cheapness 3, payoff 4, ethics_clear 5.
- **Sources.**
  - https://www.cosmos.esa.int/web/gaia/news-2026 (PRIMARY: DR4 date 2 Dec 2026)
  - https://exoplanetarchive.ipac.caltech.edu/docs/GaiaMission.html (SECONDARY: astrometric exoplanet expectation)
  - https://conference.astro.dur.ac.uk/event/7/contributions/327/attachments/351/628/gaia-status-nam25-jul25.pdf (PRIMARY: epoch data in DR4)
  - https://mailman.sydney.edu.au/pipermail/asa/Week-of-Mon-20260504/007525.html (POPULAR: DR4 sprint)

### 4. Century-baseline photographic plates (DASCH DR7, APPLAUSE DR4)

- **Data.** **DASCH DR7** (Harvard; plates from about 1880–1990 originally taken
  for all-purpose sky monitoring). It is the final release, 29 Dec 2024: 23.57
  billion measurements of 252 million sources, mosaics of 429,274 plates
  (about 750 MB each). Access is through the `daschlab` Python package and web
  APIs. The full products are about 7.9 TiB (bulk on request) and the whole
  archive is about 678 TiB. **APPLAUSE DR4** (AIP Potsdam / Hamburg / Bamberg /
  Tartu): about 94,000 images from 1893–1998, more than 2 billion calibrated
  measurements from about 70,000 direct plates, calibrated against Gaia EDR3 with
  PyPlate.
- **Question / a find.** (a) Century-scale variability: slow dimmers, novae
  before the modern era, rare outbursts, eclipses of long-period binaries. (b)
  Precovery of comets and asteroids decades before discovery (see #1). (c)
  Historical counterparts of modern transients.
- **Gap evidence.** DR7 was completed only in December 2024 and is described
  as final. 252 million light curves is far beyond anything inspected one by
  one. APPLAUSE DR4 added the Bamberg survey (17,600 plates, 1912–1968).
- **Verifier.** Weak to moderate. Requirements: agreement across two plate
  archives (DASCH plus APPLAUSE plus Sonneberg); comparison stars of matching
  colour and magnitude that do *not* show the trend; consistency with
  Gaia/ZTF/ASAS-SN in the modern part; AAVSO VSX for new variables. For
  precoveries the orbit fit is a strong verifier.
- **Precedent.** Schaefer's DASCH claim that Boyajian's Star faded about 0.16
  mag/century (SCHOLARLY) is contested, but it is the canonical example that
  this archive can raise real questions. Montet & Simon's independent Kepler
  fading made it more plausible. Plate-database precovery of PHAs (#1).
- **Recipe.** Code: pull DASCH light curves for a defined sample (for example
  all Gaia stars in a field with G < 14); robust trend and outburst statistics;
  hold the comparison-star population fixed as the null distribution;
  cross-check hits in APPLAUSE. LLM: pipeline, documentation reading, writing up
  the systematics checklist.
- **Cost.** Laptop for field-sized samples. Bulk access needs contact with the
  DASCH team.
- **Traps.** **Severe; this is the domain's best-documented false-positive
  machine.** (a) DASCH emulsion and plate-technology changes, including the
  1960s "Menzel gap," produce false long-term trends. Hippke et al. found many
  comparison stars "dim" too, and Lund et al. say the systematics do not allow
  Schaefer's precision. The DR7 ATLAS-refcat2 light curves carry an explicit
  warning about false long-term trends. (b) **VASCO "vanishing stars"/POSS-I
  transients**: nine simultaneous transients on a 1950 plate, a catalog of 5,399
  candidates, and a claimed correlation with nuclear tests (Bruehl & Villarroel
  2025). Hambly & Blair (2024) argue the profiles are emulsion defects. This
  is `contested` and is where crankery and UFO claims gather. (c) Plate flaws,
  ghost images, satellite-free but airplane-rich fields, and plate edges.
- **Crowding.** `PARTLY`. DASCH team, Hippke and Schaefer on specific stars,
  VASCO on POSS-I. Systematic DR7-wide anomaly searches look open, but I did
  not verify this.
- **Ethics.** Clear.
- **Scores.** data_ready 4, gap 4, verifier 2, cheapness 4, payoff 3,
  ethics_clear 5.
- **Sources.**
  - https://dasch.cfa.harvard.edu/dr7 and https://dasch.cfa.harvard.edu/dr7/data-products (PRIMARY)
  - https://arxiv.org/pdf/2501.12977 (SCHOLARLY: DASCH final paper)
  - https://www.aip.de/en/news/digitization-project-photographic-plates-completed/ (PRIMARY/institutional: APPLAUSE)
  - https://arxiv.org/html/2404.17355v1 (SCHOLARLY: APPLAUSE DR4)
  - https://arxiv.org/pdf/1609.03505 (SCHOLARLY: Boyajian DASCH debate summary)
  - https://ar5iv.arxiv.org/html/1605.02760 (SCHOLARLY: Hippke et al., F-star century stability)
  - https://arxiv.org/pdf/2507.15896 (SCHOLARLY/CLAIMANT: VASCO transient profiles)
  - https://arxiv.org/pdf/2604.04810 (SCHOLARLY preprint: independent recovery of vanishing sources)
  - https://www.metabunk.org/goto/post?id=349522 (POPULAR: skeptic forum)

### 5. Activity on known asteroids in archival images (active asteroids, main-belt comets)

- **Data.** DECam archive (NOIRLab, about 10^5–10^6 images), also OmegaCAM and
  others. The images were taken for cosmology and supernova surveys.
- **Question / a find.** A tail or coma on an object catalogued as an inert
  asteroid. The project estimates activity occurs in about 1 in 10,000
  asteroids.
- **Gap evidence.** The Active Asteroids Zooniverse project has covered about
  430,000 images with about 8,300 volunteers. Rubin will add many more.
- **Verifier.** Multiple independent images showing the tail with correct
  anti-solar geometry. Follow-up imaging at the next perihelion. Publication in
  RNAAS or CBET.
- **Precedent.** 2015 VA108, 2015 VP51, (588045) 2007 FZ18, 2018 CZ16 and 2016
  UU121 (the last with the TailNet neural network) were all found by volunteers
  or ML in archival DECam images (SCHOLARLY).
- **Recipe.** Code: SSOIS or ephemerides to find cutouts of every numbered
  asteroid in DECam frames; a CNN or radial-profile test against PSF stars. An
  LLM can triage. A human confirms against the anti-solar vector.
- **Cost.** VM plus storage for cutouts. Moderate.
- **Traps.** Background galaxies, star trails, and diffraction spikes that look
  like tails. Seeing variation.
- **Crowding.** `CROWDED` (Chandler et al., Active Asteroids, TailNet).
- **Ethics.** Clear.
- **Scores.** data_ready 4, gap 2, verifier 4, cheapness 3, payoff 2,
  ethics_clear 5.
- **Sources.**
  - https://www.zooniverse.org/projects/orionnau/active-asteroids/about (PRIMARY: project)
  - https://par.nsf.gov/biblio/10610718 (SCHOLARLY)
  - https://par.nsf.gov/biblio/10400634 (SCHOLARLY)

### 6. WISE/NEOWISE movers: brown dwarfs and nearby cold objects

- **Data.** WISE/NEOWISE (NASA). NEOWISE was an asteroid hunter. Its
  multi-epoch all-sky infrared data are at IRSA, and the 11th year has about
  10.9 billion single-exposure detections. Also unWISE coadds and CatWISE.
- **Question / a find.** A faint high-proper-motion infrared source, such as a
  Y dwarf or nearby T dwarf.
- **Gap evidence.** Thin. Backyard Worlds has run since 2017 and in April 2026
  published about 3,000 motion-confirmed L/T candidates (arXiv 2604.01323).
- **Verifier.** Proper motion confirmed across epochs plus spectroscopy (JWST,
  Keck, IRTF), which needs a professional collaborator. Backyard Worlds
  provides that route.
- **Precedent.** A Tasmanian volunteer found a T5.5 dwarf 6 days after the 2017
  launch (SCHOLARLY). 95 brown dwarfs announced by NASA in 2020 (POPULAR).
- **Recipe.** Join Backyard Worlds rather than duplicating it. A solo pipeline
  would difference unWISE epochs and cross-match against CatWISE and Gaia.
- **Cost.** Low.
- **Traps.** Image artifacts, ghosts, and latents; blended sources; asteroids in
  single epochs.
- **Crowding.** `CROWDED` (Backyard Worlds; CatWISE team).
- **Ethics.** Clear.
- **Scores.** data_ready 5, gap 1, verifier 3, cheapness 4, payoff 2,
  ethics_clear 5.
- **Sources.**
  - https://arxiv.org/abs/1705.02919 (SCHOLARLY: first Backyard Worlds discovery)
  - https://arxiv.org/pdf/2604.01323 (SCHOLARLY: 3,000 L/T candidates)
  - https://irsa.ipac.caltech.edu/data/WISE/docs/release/NEOWISE/expsup/sec1_5.html (PRIMARY: NEOWISE archive)
  - https://earthsky.org/space/brown-dwarfs-cosmic-neighborhood-backyard-worlds-citizen-scientists/ (POPULAR)

### 7. Rubin LSST alert stream via public brokers (live since Feb 2026)

- **Data.** Vera C. Rubin Observatory alerts. First alerts went out **24 Feb
  2026**: about 800,000 that night, with up to 7 million per night planned and
  about 2-minute latency. Seven public brokers (ALeRCE, AMPEL, ANTARES, Babamul,
  Fink, Lasair, Pitt-Google) are open to "the public and citizen scientists."
  Data Preview 1 (ComCam) was delivered 30 June 2025.
- **Question / a find.** Rare transients (fast blue optical transients, tidal
  disruptions), new comets and NEOs, and odd variables. Also the cross-domain
  case in "What ZTF Saw Where Rubin Looked" (arXiv 2507.06217): ZTF archival
  anomaly hunting in Rubin fields.
- **Gap evidence.** The volume exceeds human vetting. But brokers and
  professional teams are built to filter it, so the gap is in idiosyncratic
  filters, not in volume.
- **Verifier.** TNS report plus spectroscopic classification by someone with a
  telescope. MPC for movers. The verifier exists but is not in a hobbyist's
  hands.
- **Precedent.** Amateur and citizen TNS reports exist from ZTF-era projects (not
  verified this session).
- **Recipe.** A broker filter (Fink and Lasair accept user filters), with
  cross-match of light curves against ZTF DR23 history. An LLM can write the
  filters; code computes the scores.
- **Cost.** Low.
- **Traps.** Bogus subtractions, satellite streaks (Starlink), and solar-system
  objects misread as transients.
- **Crowding.** `CROWDED` by design.
- **Ethics.** Clear.
- **Scores.** data_ready 5, gap 2, verifier 3, cheapness 5, payoff 3,
  ethics_clear 5.
- **Sources.**
  - https://skyandtelescope.org/astronomy-news/rubin-observatory-sends-800000-alerts-to-astronomers-per-night/ (POPULAR)
  - https://earthsky.org/space/rubin-observatory-launches-real-time-alert-system/ (POPULAR)
  - https://usdf-rsp.slac.stanford.edu/docs (PRIMARY: DP1)
  - https://arxiv.org/pdf/2507.06217 (SCHOLARLY)

### 8. Archival radio pulsar-survey data: missed fast radio bursts

- **Data.** Parkes (Murriyang) pulsar-survey archives (CSIRO Data Access Portal)
  and others. Filterbank files run to many TB.
- **Question / a find.** A dispersed single pulse with extragalactic dispersion
  measure that earlier pulsar searches did not flag.
- **Gap evidence.** The first FRB (Lorimer burst, 2001 data) was found in 2007,
  more than five years later. **FRB 010312** was found in 2019 in the *same*
  2001 Magellanic Clouds dataset, and its authors argued more bursts "are likely
  still waiting to be found" in the Parkes archive (SCHOLARLY).
- **Verifier.** Moderate and mechanical. The dispersion sweep follows ν⁻² and is
  seen in one or a few beams, not all 13 (RFI test). Peryton-like RFI is the
  calibrated failure. Then expert review and publication. A one-off
  burst cannot be re-observed unless it repeats.
- **Precedent.** Lorimer burst (2007) and FRB 010312 (2019), both archival
  (SCHOLARLY).
- **Recipe.** Code: download filterbanks, dedisperse with GPU tools (heimdall)
  or CPU (PRESTO single-pulse), cluster candidates, apply a multibeam RFI
  veto, use an ML classifier (FETCH). LLM: tool installation, triage of
  diagnostic plots.
- **Cost.** High for a hobbyist. TB-scale downloads and many CPU-days, or a GPU.
- **Traps.** **Perytons** (Parkes microwave-oven bursts, the canonical RFI
  impostor), the Lorimer burst's own early skepticism, and the narrow-band RFI
  zoo.
- **Crowding.** `PARTLY`. Professional reprocessing has happened (HTRU, FRB
  010312). The extent of remaining unsearched archives was not verified.
- **Ethics.** Clear.
- **Scores.** data_ready 3, gap 3, verifier 3, cheapness 2, payoff 4,
  ethics_clear 5.
- **Sources.**
  - https://en.wikipedia.org/wiki/Fast_radio_burst (SECONDARY)
  - https://arxiv.org/pdf/1902.06009 (SCHOLARLY: FRB 010312 in Lorimer data)
  - https://arxiv.org/pdf/2405.19106 (SCHOLARLY: FRB discovery history)

### 9. Spacecraft image archives: lost hardware, fresh impacts, small moons

- **Data.** LRO NAC (Moon, about 0.5 m/pixel), MRO HiRISE (about 0.3 m) and CTX
  (about 6 m) for Mars, and Voyager and Cassini archives (PDS). All NASA PDS,
  public.
- **Question / a find.** (a) Lost landers and impact debris (Soviet Luna and
  Mars probes, failed commercial landers). (b) Fresh Mars impacts in
  before-and-after CTX pairs. (c) Small moons or ring features in outer-planet
  frames.
- **Gap evidence.** Fresh impacts: a JPL/Brown classifier run over more than
  112,000 CTX images produced 69 new impacts confirmed with HiRISE, and the
  authors note that manual searches were slow and biased toward low thermal
  inertia terrain. Moons: Perdita sat unrecognized in 1986 Voyager images until
  1999.
- **Verifier.** Strong where re-imaging exists. **HiWISH** lets anyone request
  HiRISE targets; the LROC team re-images and compares before-and-after.
  For moons: recovery in other frames on a consistent orbit, then telescope or
  later-mission confirmation (Perdita was confirmed by Hubble in 2003).
- **Precedent.** **Vikram lander debris** (2019): Shanmuga Subramanian spotted a
  roughly one-pixel debris item in public LRO images, and NASA credited him and
  found the main crash 750 m away (POPULAR). **Beagle 2** (2015): Michael Croon
  noticed a gap in HiRISE coverage and requested imaging via HiWISH, and the
  lander was found partly deployed. Note that Croon was a former Mars Express
  operations engineer, not a pure outsider (POPULAR). **Lunokhod 1** (2010):
  LROC located it, and APOLLO laser ranging got returns on the first try
  (SCHOLARLY). **Perdita** (Karkoschka, 1999, Voyager 2 archive) (SECONDARY).
  **Despina's shadow** in 1989 Voyager frames (Ted Stryk, amateur, 2009)
  (POPULAR).
- **Recipe.** Code: download before-and-after NAC or CTX pairs for a target
  ellipse; co-register; difference; rank blobs. LLM: read landing-ellipse
  literature, plan the search, draft a HiWISH or LROC note. The human
  and the re-image decide.
- **Cost.** Low to moderate. NAC frames are hundreds of MB each, and a target
  ellipse is tens of frames.
- **Traps.** Boulders and fresh small craters that look like hardware; changes
  in illumination (Vikram was first missed because of shadows); pareidolia (the
  "face on Mars" genre). For moons: hot pixels, cosmic rays, and known small
  moons.
- **Crowding.** `PARTLY`. LROC and HiRISE teams search high-profile targets,
  and the Mars impact work is a JPL program. Targets like Luna 9, Mars 2/3/6 and
  recent commercial lunar landers may be open; not verified this session.
- **Ethics.** Clear. Crash sites hold no human remains. Be respectful in tone
  about recent national missions.
- **Scores.** data_ready 4, gap 3, verifier 4, cheapness 4, payoff 2,
  ethics_clear 5.
- **Sources.**
  - https://motherboard.vice.com/en/article/mbm8n8/an-amateur-astronomer-helped-nasa-find-a-wrecked-lander-on-the-moon (POPULAR)
  - https://www.nasa.gov/image-feature/goddard/2019/obscured-in-the-lunar-highlands (PRIMARY: Vikram LRO)
  - https://theconversation.com/how-we-found-our-lost-mars-lander-after-a-decade-of-searching-and-whats-next-85374 (POPULAR: Beagle 2, by team members)
  - https://www.arxiv-vanity.com/papers/1009.5720/ (SCHOLARLY: Lunokhod 1 laser ranging)
  - https://www.space.com/8295-lost-soviet-reflecting-device-rediscovered-moon.html (POPULAR)
  - https://ar5iv.labs.arxiv.org/html/2207.05679 (SCHOLARLY: ML fresh Mars impacts, 69 confirmed)
  - https://www.freethink.com/articles/craters-on-mars (POPULAR: 112,000 CTX images)
  - https://science.nasa.gov/uranus/moons/perdita/ (PRIMARY/SECONDARY: Perdita)
  - https://www.planetary.org/articles/2035 (POPULAR: Stryk, Despina shadow)

### 10. SETI open data and CNEOS fireballs: recorded as traps

These score low. They are kept here because Rule 7 asks for the cases that
went wrong.

- **Breakthrough Listen open data** (GBT, Parkes; petabytes; public). **BLC1**
  (Proxima, 2019) looked like a technosignature and turned out to be a
  drifting intermodulation product of local interferers. About 60 look-alikes
  appeared at off-target pointings, and 39 hours of re-observation found
  nothing (SCHOLARLY). **Ma et al. 2023** (ML on 820 stars, 480 h) flagged 8
  "signals of interest", and **none re-detected** (SCHOLARLY). Verifier: the
  ON-OFF cadence and re-observation, which already rule out nearly everything.
  Gap: low. Payoff if real: maximal. Expected value for a hobbyist: about 0,
  and high crank risk. **Scores:** data_ready 4, gap 1, verifier 3, cheapness 2,
  payoff 5, ethics_clear 5. `CROWDED`.
- **CNEOS fireball database and IM1 (CNEOS 2014-01-08)**. The interstellar
  claim (Siraj & Loeb) rests on US-government sensor velocities with **no
  published uncertainties**. Critiques say the errors may be large enough to
  allow a bound orbit. A 2024 A&A reassessment gives 94.1%, below a 3σ
  discovery threshold. The seismic signal used to locate the ocean expedition
  was **likely a truck** (Fernando et al., LPSC 2024), and infrasound puts the
  fireball more than 100 miles from the search area. Status: `contested`, best
  read as reported, not established. Lesson: a dataset whose error model is
  classified has **no verifier**. **Scores:** data_ready 4, gap 2, verifier 1,
  cheapness 5, payoff 3, ethics_clear 5.
- **Planet Nine archival claims.** The 2025 IRAS–AKARI candidate (Phan et al.,
  PASA) was narrowed from 2 million sources to 13 pairs to 1. Two detections
  cannot fix an orbit, and Mike Brown says the inclined orbit could not explain
  the clustering. An earlier 2021 signal was not confirmed. This is the
  standard pattern of an archival-mover claim before follow-up.
- **Sources.**
  - https://seti.berkeley.edu/blc1/ (PRIMARY: BLC1)
  - https://iopscience.iop.org/article/10.3847/2515-5172/ac33b2 (SCHOLARLY)
  - https://www.universetoday.com/153097/the-radio-signal-from-proxima-centauri-came-from-earth-after-all (POPULAR)
  - https://astrobiology.com/2023/01/31/a-deep-learning-search-for-technosignatures-of-820-nearby-stars/ (POPULAR: Ma et al. summary)
  - https://ar5iv.arxiv.org/html/1904.07224 (CLAIMANT: Siraj & Loeb)
  - https://arxiv.org/pdf/2311.07699 (SCHOLARLY: critique of Loeb et al.)
  - https://arxiv.org/html/2405.17219v1 (SCHOLARLY: 94.1% reassessment)
  - https://hub.jhu.edu/2024/03/07/alien-meteor-truck (POPULAR/institutional: truck)
  - https://arxiv.org/abs/2504.17288v1 (CLAIMANT: Planet Nine IRAS/AKARI)
  - https://www.astronomy.com/science/have-astronomers-found-planet-nine/ (POPULAR: Brown's objection)

### Not given full sections

- **SOHO/LASCO sungrazing comets.** 5,000th comet on 25 Mar 2024 (Hanjie Tan,
  Sungrazer). More than half of all known comets come from SOHO. This is the
  strongest amateur-discovery pipeline in astronomy, but it runs in near real
  time and is `CROWDED`. I found no evidence about leftover archival gaps.
  Sources: https://www.esa.int/ESA_Multimedia/Images/2024/03/SOHO_reaches_5000_comets
  (PRIMARY), https://svs.gsfc.nasa.gov/14552/ (PRIMARY).
- **Kepler/K2 residuals.** ExoMiner (301 validated) and UCLA (366 candidates)
  show Kepler has been reprocessed repeatedly. `CROWDED`, gap 1.
- **ZTF DR23 light curves** (about 5 billion, Parquet on AWS S3) are excellent
  infrastructure for #1, #4 and #7, and the SNAD anomaly-detection group already
  mines them (arXiv 2507.06217, 2603.09762).

## Pilot in a day

**Candidate #1: sub-threshold precovery of short-arc NEAs in ZTF archival images.**
I chose it because its verifier is an orbit fit you can run yourself before
anyone else is involved.

*URLs are as I know them. The endpoints were not fetched this session (no
egress), so confirm each one first.*

1. **Target list.** Query the JPL SBDB Query API for NEAs with a poor orbit
   (`condition_code` ≥ 5) and an arc under one opposition:
   `https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,pdes,condition_code,data_arc,n_obs_used,first_obs,last_obs&sb-group=neo&sb-cdata=...`
   (build the constraint with `sb-cdata` per the API docs at
   `https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html`). Keep about 50 objects
   discovered after 2019 whose sky tracks crossed ZTF's footprint earlier.
2. **Already reported?** For each object, fetch its MPC observation list
   (`https://www.minorplanetcenter.net/db_search/show_object?object_id=<desig>`
   or the MPC Explorer API) and drop epochs already covered by ZTF (obs code
   I41).
3. **Which images.** Query IRSA's Moving Object Search Tool
   (`https://irsa.ipac.caltech.edu/applications/MOST/`, which has a program
   interface) with catalog "ZTF" and the object designation. It returns the ZTF
   science frames whose footprint contains the predicted position. CADC SSOIS
   (`https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/ssois/`) does the same for
   DECam, CFHT and SDSS.
4. **Cutouts.** Fetch about 60″ cutouts from the IRSA ZTF image service
   (`https://irsa.ipac.caltech.edu/ibe/data/ztf/products/sci/...` with
   `?center=ra,dec&size=60arcsec`), together with JPL Horizons predicted
   position and 3σ uncertainty ellipse at each epoch
   (`https://ssd.jpl.nasa.gov/api/horizons.api`).
5. **Detect.** Standard-library-plus-numpy/astropy script: forced PSF
   photometry on the Horizons track. Where the ellipse is large, shift-and-stack
   along a grid of trial tracks within the ellipse across same-night exposures.
   Require at least 2 independent detections on the same night at a rate
   consistent with the prediction.
6. **Verify (the actual test).** Measure centroids against Gaia DR3 and refit
   the orbit with Find_Orb (`https://www.projectpluto.com/find_orb.htm`,
   command-line `fo`). A precovery is accepted only if residuals are
   ≲ 0.5–1″ and the refit predicts the *other* archival epochs. The script
   output (residual table) gets checked in, per Rule 6.
7. **Submit only after review.** Prepare ADES-format astrometry and ask an
   experienced MPC submitter (an observatory or B612) how archival third-party
   measurements should be credited before anything is sent.

Success after one day: a pipeline that recovers known ZTF-reported detections
for 5 control objects (calibration, Rule 7), plus a ranked list of candidate
sub-threshold precoveries with refit residuals. Failure modes to record: none
survive the refit, or every hit is already in the MPC.

## Unverified claims

- **Rabtsevich / TIC 4206066.** I did not open the Reddit post itself. The X
  post date (about 7 Oct 2026), "74 analyses / 1,000+ scripts," the 0.05% depth
  and 2 h duration, and the 116 ly distance come only from search summaries of
  press and X. Also unconfirmed: that TESS DDT "Program 100" with Rabtsevich as
  PI exists; the Scientific American article; Greg Laughlin's "solid" quote
  (a second search could not surface it); and the claim that the 2018 dips
  align with thruster firings. The "independent blind recovery" by
  `eumemic/exoplanets` is reported in a search summary. The repository is
  outside this session's GitHub access and was not read. A Threads post's
  claim that "researchers confirmed the signal could be real" was not traced to
  any primary source. Absence of an ExoFOP CTOI is based on search, not on
  checking ExoFOP directly.
- **Gaia DR4 contents** beyond the date (for example which epoch products are
  complete) are from conference slides seen through search summaries.
- **Rubin LSST official survey start date.** Sources disagree, and I did not
  confirm it.
- **NEOWISE end and final release dates.** Not confirmed this session. (My
  recollection is that the survey ended in August 2024; per Rule 2, unverified.)
- **APPLAUSE astrometry submitted to the MPC.** Not found.
- **Luna 9 identified in LRO imagery (by anyone).** Not found.
- **An amateur discovering a genuinely new moon in Voyager or Cassini
  archives.** Not found. Archival moon finds (Perdita, Cassini moonlets) were
  professional, and the amateur case (Stryk) was the shadow of a known moon.
- **CHIME/FRB Catalog 2 status, and the volume of still-unsearched Parkes
  archives.** Not verified; search budget was exhausted.
- **A specific amateur Gaia discovery** (for the #3 precedent). Not verified.
- **MPC policy on third-party measurements of archival images** (credit, obs
  code). Not verified. Pilot step 7 says to ask first.
- **Pilot URLs and API parameter names** come from memory and were not
  fetched.
- **Breakthrough Listen open-data portal URL and current volume.** Not
  verified.
