# Pooled LLM compute for unsolved-text brute force — research brief

Compiled 2026-09-15. Tier key: **[P]** primary (actor's own publication/terms), **[S]** scholarly (arXiv), **[2]** secondary (journalism, Wikipedia), **[POP]** popular/blog.

**Method note / limits.** The `WebSearch` budget for this session was already exhausted, so retrieval was done by direct `WebFetch`, the Hacker News Algolia API as a search proxy, and the `r.jina.ai` text proxy for sites that 403 on direct fetch (openai.com, ams.org, docs pages). I never saw raw openai.com HTML myself — see "Could not verify" at the end.

---

## Part 1 — The "generate massively, verify cheaply" wins

### 1.1 OpenAI, Navier–Stokes, September 2026

**What was claimed.** On 2026-09-08 OpenAI published *On the Navier–Stokes Millennium Prize Problem*, claiming an internal model produced a proof that "an initially smooth fluid at rest can develop a singularity in a finite time," resolving alternatives **(C) and (D)** of Fefferman's official Clay statement — i.e. *blow-up*, not global regularity, and with a **smooth forcing term**. [P] https://openai.com/index/navier-stokes-solution/

The accompanying Lean 4 repo states the formalized theorems precisely: for any positive viscosity on ℝ³ there exist smooth initial data with no global smooth finite-energy solution; likewise on the torus ℝ³/ℤ³. A companion Euler result gives finite-time singularity for smooth, compactly supported, divergence-free data under **unforced** 3D Euler (C¹ norm unbounded, ∫‖ω‖_∞ divergent). [P] https://github.com/openai/NavierStokesAndEuler

**Scale — the "130 billion output tokens" figure is CORRECT.** OpenAI's own text: *"Across all attempted problems, the agents sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens."* [P] https://openai.com/index/navier-stokes-solution/ (via r.jina.ai); quoted verbatim and independently by [2] https://simonwillison.net/2026/Sep/8/on-navier-stokes/

**Method.** Not enumeration. Roughly **10,000 concurrent agents** driven by "an internal model that is significantly more capable than GPT-6 Astra," launched 2026-09-01, solution in hand 2026-09-05 (~88 h), Lean formalization a further ~17 h; model training reportedly began 2026-08-28. **Cost:** OpenAI estimated ~**$15,000,000** at public API rates. [P] ibid.; headline confirmation [2] https://www.newscientist.com/article/2588063-openai-has-solved-the-navier-stokes-millennium-problem-using-15m-of-ai-effort/

**Verification.** Lean 4 (4.34.0-rc2) + Mathlib, published as a buildable repo with a `Comparator` challenge harness. This is the load-bearing part: the verifier is mechanical and free *relative to the search*. [P] https://github.com/openai/NavierStokesAndEuler

**Reception — contested, and the "pure brute force" framing is wrong.**
- Clay Mathematics Institute, 2026-09-11: the problem "has apparently been settled"; "The process is deliberately unhurried, but we will provide updates." No prize awarded. [P] https://www.claymath.org/news/navier-stokes-announcement/
- AMS leadership (Vakil, Meier), 2026-09-08: "a milestone advance in human knowledge," explicitly crediting the chain Navier/Stokes → Córdoba, Martínez-Zoroa → Alpöge, Buckmaster → OpenAI. [P] https://www.ams.org/news?news_id=7686
- **Tristan Buckmaster (NYU), public statement 2026-09-08.** He and Levent Alpöge had already released finite-time blowup with smooth forcing for incompressible porous medium, Boussinesq and 3D Euler, and believed they had hypo-dissipative Navier–Stokes. The program came from Diego Córdoba and Luis Martínez-Zoroa ("I believe Luis Martínez-Zoroa deserves a Fields Medal"). They used Claude, Codex, GPT-5.6 Sol and Astra; blow-up results 2026-08-15, Lean-verified 2026-08-22. He says he was told OpenAI's first prompt was sent "after information about our work had reached OpenAI," that the claim of "very little human input" "turned out not to be true," that an entire OpenAI team had worked on it, and that "an insane amount of compute had been used." He calls the Euler writeup "AI slop" and the episode "a Deep Blue–Kasparov moment." [P] https://cims.nyu.edu/~tristanb/statement.pdf
- Terence Tao on the Alpöge–Buckmaster results: "the actual solving of these problems is only a proxy goal for the primary goal of developing mathematical understanding and insight"; notes autoformalization agents now routinely Lean-check such work. [P] https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/
- Credit dispute covered by [2] NYT, Wired, Axios, WSJ (headlines indexed via HN; not individually fetched).

**Takeaway for the repo:** the 130B tokens *finished* a ten-year human research program with a known attack route and a formal verifier. They did not search a raw hypothesis space.

### 1.2 Contrast — DeepMind + Brown/NYU/Stanford, unstable singularities (2025, PINNs)

*Discovery of Unstable Singularities*, arXiv:2509.14185, submitted 2025-09-17; 22 authors incl. Yongji Wang, Javier Gómez-Serrano, Tristan Buckmaster, Ching-Yao Lai, Pushmeet Kohli. First systematic discovery of families of **unstable** self-similar singularities for the incompressible porous media equation and 3D Euler, via "curated machine learning architectures and training schemes with a high-precision Gauss-Newton optimizer," reaching near double-float machine precision — precise enough to feed computer-assisted proofs. [S] https://arxiv.org/abs/2509.14185 · DeepMind blog 2025-09-18 names Brown, NYU and Stanford, describes the method as Physics-Informed Neural Networks trained against the equations rather than data, and reports a linear pattern in λ across instability orders implying more solutions exist. [P] https://deepmind.google/discover/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/ · Follow-up: gradient-normalized residual re-weighting, arXiv:2511.22819 (2025-11-28), Wang/Léger/Lai/Buckmaster. [S]

Opposite cost profile: a small, structured optimization with a precise numerical residual as objective. Cheap, targeted, no token firehose.

### 1.3 Other instances of the same pattern

| Case | Date | What made it brute-forceable |
|---|---|---|
| **AlphaProof + AlphaGeometry 2** at IMO 2024: 4/6 problems, 28/42, silver level. AlphaProof = pretrained LM + AlphaZero RL operating *in Lean*; a Gemini autoformalizer converted ~1 million natural-language problems to formal statements. Geometry solved in 19 s; other problems took **up to three days**. [P] https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/ | 2024-07-25 | Lean = free, total, mechanical verifier. You can search for days because a wrong proof costs nothing to reject. |
| **FunSearch**: LLM proposes *programs*, an automated evaluator scores them, best programs feed back. Largest cap sets found in 20 years; beat SOTA online bin-packing heuristics. [P] https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/ | 2023-12-14 | Candidate = short program; verifier = run it and measure. Partial-credit *score*, not pass/fail — that is what lets evolution steer. |
| **AlphaEvolve**: Gemini Flash (breadth) + Pro (depth) in an evolutionary loop with automated evaluators. 4×4 complex matmul in 48 scalar multiplications (beats Strassen 1969); kissing number lower bound 593 in 11 dimensions; improved SOTA on ~20% of 50+ open problems; recovered 0.7% of Google's global compute via scheduling; 23% matmul kernel speedup. [P] https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ | 2025-05-14 | Same as FunSearch plus: the objective is a *number*, so you always know which of two candidates is better. |
| **AlphaEvolve at scale on math**: Georgiev, Gómez-Serrano, Tao, Wagner — 67 problems across analysis, combinatorics, geometry, number theory; rediscovered known solutions in most, improved several, generalized finite computations into formulas; combined with Deep Think and AlphaProof for proofs. [S] https://arxiv.org/abs/2511.02864 | 2025-11-03 | Explicitly search-with-evaluator. Tao is a co-author, which is why the framing is careful. |
| **Erdős problems, 2025–26.** Tao's wiki taxonomy: 1(a) autonomous / 1(b) alongside literature / 1(c) building on literature / 1(d) collaborative, plus secondary 2(a) literature search, 2(b) formalization, 2(c) rewriting, 2(d) computation; statuses 🟢 full / 🟡 partial / 🔴 incorrect / ⚪ unverified. Credits GPT-5.2–5.5 Pro, Claude Opus/Fable/Mythos, Gemini 3 Pro, Aristotle, AlphaProof, AlphaEvolve, OpenAI internal models. [P] https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems | 2025-11 → | Small self-contained statements; a competent human or Lean can check a candidate proof in hours. |
| Milestones: #124 solved with Harmonic's **Aristotle** (2025-11-30); #728 "solved more or less autonomously by AI" (GPT-5.2 Pro; hobbyists Barreto & Price, 2026-01-04); OpenAI's unit-distance (1946 Erdős conjecture) result 2026-05-20; "Astra" announced 10 more advances 2026-08-01. A DeepMind team of 21 "autonomously resolved **9 of 353** open Erdős problems at the per-problem cost of **a few hundred dollars**." Bloom's database: 565 solved / 652 open. [2] https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/ | 2026-08-03 | **Cautionary half:** #333 was "solved," then found in Erdős's own 1977 paper. Bloom: "AI is being used a lot by people who aren't mathematicians ... not capable of verifying the output." 100–200 page AI papers circulate that "no human has read." |

### 1.4 Current retail output-token prices, and what 130B tokens costs

| Model | Output $/M | Source |
|---|---|---|
| OpenAI GPT-6 Astra | **50** (long-ctx 75) | [P] https://platform.openai.com/docs/pricing |
| OpenAI GPT-5.6 Sol / Terra / Luna | 20 (promo to 2026-11-21) / 12 / 1.20 | ibid. |
| Anthropic Claude Fable 5.1, Mythos 5.1 | **50** | [P] https://docs.claude.com/en/docs/about-claude/pricing |
| Anthropic Claude Opus 5 (and 4.5–4.8) | 25 | ibid. |
| Anthropic Claude Sonnet 5 / Haiku 4.5 | 10 / 5 | ibid. |
| Google Gemini 3.8 Flash / 3.5 Flash / 2.5 Pro | 3.75 (→7.50 on 2027-01-01) / 6.75 / 10–15 | [P] https://ai.google.dev/gemini-api/docs/pricing |
| OpenRouter deepseek-v4-flash-0731 | **0.11** | [P] https://openrouter.ai/api/v1/models |
| OpenRouter z-ai/glm-5.3-flash / minimax-m3 | 0.333 / 1.20 | ibid. |
| OpenRouter deepseek-v4-pro / glm-5.3 / kimi-k3 | 3.20 / 4.40 / 13.28 | ibid. |

**Batch discounts are 50% on all three majors** — OpenAI ("Batch" tier 50% off; Flex matches it), Anthropic ("a 50% discount on both input and output tokens"), Google (50% batch). Anthropic prompt caching: 5-min write 1.25× input, 1-h write 2× input, cache reads 0.1× input (0.025× on Fable/Mythos 5.1). [P] the three pricing pages above.

**130,000,000,000 output tokens, output-only, at list:** GPT-6 Astra $50/M → **$6.50M** (batch $3.25M) · Claude Opus 5 $25/M → **$3.25M** (batch $1.63M) · Gemini 3.8 Flash $3.75/M → **$488K** · deepseek-v4-pro $3.20/M → **$416K** · minimax-m3 $1.20/M → **$156K** · glm-5.3-flash $0.333/M → **$43.3K** · deepseek-v4-flash $0.11/M → **$14.3K**.

OpenAI's ~$15M figure is consistent with $6.5M of output plus input/reasoning across 2.7M messages. The spread that matters for a volunteer project: **the same token count is ~450× cheaper on the cheapest credible open-weight model than on a frontier model.** Whether a cheap model can *find* anything is the whole question — but cheap model + strict verifier + large sample budget is at least the right shape.

---

## Part 2 — Precedents for pooling on one hard problem

### 2.1 Volunteer compute (closest analog: distributed.net)

- **RC5-56** — launched Feb 1997, key `0x532B744CC20999` found **1997-10-19**, 250 days, 47% of keyspace; plaintext "It's time to move to a longer key length." $10,000 RSA prize. [P] https://www.distributed.net/RC5 · [2] https://en.wikipedia.org/wiki/Distributed.net
- **RC5-64** — completed **2002-07-14**, **1,757 days**, 82.77% of keyspace, key `0x63DE7DC154F4D039`, plaintext "Some things are better left unread." Project stats: **327,856 participants**, 56,878,907,073 blocks ≈ 15.27 quintillion keys, ~102 billion keys/sec. [P] https://stats.distributed.net/projects.php?project_id=5
- **DES challenges** — DES-II-1 in 39 days (1998-02-23); DES-II-2 lost to EFF's hardware cracker in 2.5 days; DES-III cracked in **22.5 hours** (1999-01-19) with EFF Deep Crack. [2] Wikipedia, above.
- **RC5-72** — started 2002-12-03; **15.691% complete as of March 2026**, ~36–43 years to exhaust. [2] https://en.wikipedia.org/wiki/RC5 · *The cautionary datum: pooled volunteer compute scales linearly; exponential keyspaces do not care.*
- **SETI@home** — launched 1999-05-17, hibernated 2020-03-31. Peak >5.2M participants, 1,803,163 lifetime users, 668 TFLOPS (2013), >2M years aggregate CPU time, Guinness-recognized "largest computation in history" (10²¹ FLOP by Sept 2001). **Found nothing.** Spawned BOINC. [2] https://en.wikipedia.org/wiki/SETI@home
- **Folding@home** — launched 2000-10-01. First exaflop system **2020-03-25** (768 PFLOPS native / 1.5 x86 exaFLOPS); **2.43 exaflops by 2020-04-12**, from ~30,000 pre-pandemic users surging massively. [2] https://en.wikipedia.org/wiki/Folding@home
- **GIMPS** — founded Jan 1996 by George Woltman. ~280,000 users / 2.9M hosts, ~4.71 PFLOPS (2022). EFF $150K for a 100M-digit prime; GIMPS pays $3,000 per discovery. Latest: **M136,279,841** (41,024,320 digits), found **2024-10-21 by Luke Durant** — not on a home PC but on **rented cloud A100s**. [2] https://en.wikipedia.org/wiki/Great_Internet_Mersenne_Prime_Search · *Durant is the best precedent for "one person rents a lot of compute and wins."*

### 2.2 Prize / data / labor pooling

- **Vesuvius Challenge** — launched March 2023 by Nat Friedman and Daniel Gross, Brent Seales principal advisor. Open prize pool **$2,140,000**, **$1,868,000 already awarded**; funders include Friedman ($2.25M), Musk Foundation ($2.084M), Alex Gerko ($450K), Joseph Jacks ($250K), Gross ($225K). The 2023 **$500,000 Grand Prize** was won within a year for four passages / 140 characters from a Herculaneum scroll. By 2026 **PHerc. 1667 became the first scroll virtually unwrapped and read end to end.** Open now: $1M Grand Prize (2027) for fully unrolling a sealed scroll, $500K First Letters, $590K/yr monthly Progress Prizes at $20K. Winners must open-source. [P] https://scrollprize.org/ · **The model this repo should study hardest:** pooled *money* and pooled *open data*, with competing individual runs — no need to pool anyone's API account.
- **Zooniverse** — launched 2009-12-12 out of Galaxy Zoo (Adler, Oxford, Minnesota). >2.7M registered volunteers by March 2025, >450 peer-reviewed papers. [2] https://en.wikipedia.org/wiki/Zooniverse
- **Polymath Project** — Timothy Gowers, January 2009, "Is massively collaborative mathematics possible?" Polymath1: ~40 contributors, ~3 months, density Hales–Jewett, two papers as "D. H. J. Polymath." Polymath8a took prime gaps to H = 4,680; Polymath8b to **H = 246**. [2] https://en.wikipedia.org/wiki/Polymath_Project
- **Kaggle** — not independently verified this session; treat as unsourced here.

### 2.3 Attempts to pool LLM / GPU compute specifically

- **Prime Intellect INTELLECT-1** (2024-11-29): first 10B-parameter LM "collaboratively trained across the globe," 1T tokens, **5 countries / 3 continents, up to 112 H100s, 42 days**, 400× communication-bandwidth reduction via PRIME (DiLoCo + FSDP2, ElasticDeviceMesh); 96% compute utilization US-only, 83% globally. [P] https://www.primeintellect.ai/blog/intellect-1-release
- **Prime Intellect INTELLECT-2** (2025-04-15): 32B RL run on QwQ-32B. "Anyone can permissionlessly contribute their heterogeneous compute resources" — 4×RTX 3090 suffices. Stack: prime-rl (async distributed RL), Shardcast (tree-topology weight distribution), **TOPLOC** (locality-sensitive hashing for *verifiable inference*, detecting malicious workers), SYNTHETIC-1/GENESYS (task + verifier environments). [P] https://www.primeintellect.ai/blog/intellect-2 · **TOPLOC is the key transferable idea:** untrusted volunteers are only usable if their output is cheaply checkable — the same constraint as distributed.net's block re-issue.
- **Nous Research Psyche** (announced 2025-05-14): decentralized training over underutilized hardware using DisTrO compression; coordinator lives **on-chain in a Solana smart contract**; first run is **Consilience-40B** (MLA architecture) on 20T tokens from FineWeb / FineWeb-2 / Stack V2. [P] https://nousresearch.com/nous-psyche/
- **Petals** (BigScience) — "Run large language models at home, BitTorrent-style": load a slice of the model, connect to peers hosting the rest. ~6 tok/s single-batch for Llama 2 70B; supports Llama 3.1 405B, Mixtral 8×22B, Falcon, BLOOM 176B; README shows no shutdown notice. [P] https://raw.githubusercontent.com/bigscience-workshop/petals/main/README.md · Caveat: 6 tok/s is ~4 orders of magnitude short of a 130B-token campaign.
- **Bittensor, Hivemind, Together / Akash / io.net, Hugging Face Inference** — not verified this session; see "Could not verify."

### 2.4 Funding mechanisms

- **Quadratic funding** — formalized by Buterin, Hitzig and Weyl, *Liberal Radicalism* (2018). Gitcoin Grants is the main implementation (Owocki, Moore, Singh): **>$60,000,000 to 3,000+ open-source projects as of 2022**, though Wikipedia notes it "differs in several ways from the original QF scheme." Known weaknesses: collusion and sybil resistance. [2] https://en.wikipedia.org/wiki/Quadratic_funding
- **Manifund** — 501(c)(3) run by Austin Chen. Three mechanisms: open fundraising ("a Kickstarter for nonprofits"), **regranting** (delegated budgets to expert regrantors), and **impact markets** (funders invest in projects competing for charitable prizes). Turnaround "in days instead of weeks." [P] https://manifund.org/about
- **VitaDAO** — longevity DAO: **$4.7M deployed across 31 projects** (3 target discovery, 18 drug discovery, 3 preclinical, 3 clinical), 8 IP tokens, 3 companies founded; funds via equity and IP-NFTs, governed by the VITA token. [P] https://www.vitadao.com/
- **Experiment.com, Kickstarter science** — not verified this session.

### 2.5 The specific obstacle: LLM credits and subscriptions are legally non-poolable

Every provider checked forbids exactly the mechanism a "token SETI@home" would need.

- **OpenAI Service Credit Terms** — decisive. Credits "expire one year after the date of purchase or issuance if not used"; "are not refundable except where required by law"; **"We prohibit and do not recognize any purported transfers, sales, gifts, or trades of Service Credits"**; they are "non-transferable and may be used only in connection with the applicable Service for which they were issued"; "not legal tender or currency ... not redeemable, refundable, or exchangeable for any sum of money." [P] https://openai.com/policies/service-credit-terms/
- **OpenAI Business Terms** — §3.3 prohibits "buy, sell, or transfer API keys from, to, or with a third party"; "Customer will not share Account access credentials or individual login credentials between multiple users"; "Customer may not resell or lease access to its Account"; "End User Accounts may only be provisioned to, registered for, and used by, a single End User." [P] https://openai.com/policies/business-terms/
- **OpenAI consumer Terms of Use (ChatGPT Plus/Pro)** — "You may not share your account credentials or make your account available to anyone else"; no programmatic extraction of Output; no lease/sell/distribute. **ChatGPT subscription allowances cannot be pooled or redirected. Confirmed.** [P] https://openai.com/policies/terms-of-use/
- **Anthropic Consumer Terms (Claude Pro/Max)** — "You may not share your Account login information, Anthropic API key, or Account credentials with anyone else. You also may not make your Account available to anyone else." Automated/non-human access prohibited except via an API key. **Claude Max allowances cannot be pooled. Confirmed.** [P] https://www.anthropic.com/legal/consumer-terms
- **Anthropic Commercial Terms** — D.4: customer "may not ... resell the Services except as expressly approved by Anthropic"; M.4: no assignment without written consent; H.1 defers prepaid credits to separate Supplemental Credits Terms (page 404'd — see below). [P] https://www.anthropic.com/legal/commercial-terms
- **OpenRouter** — credits are **"non-transferable, including between accounts"**, have "no equivalent value in fiat currency," are refundable only within 24 h (crypto never), and "may expire three hundred sixty-five (365) days after purchase." The ToS bans "sell or otherwise transfer the access granted under these Terms," and bans multiple accounts to bypass use limits. BYOK costs 5% of normal model price above $25,000/month on pay-as-you-go. [P] https://openrouter.ai/terms · [P] https://openrouter.ai/docs/faq · **But:** OpenRouter supports **organization accounts** with an admin who invites Authorized Users and controls logging/retention. That is the one sanctioned pooling shape: *one org account, funded by donated money, running the job* — not donated credits.

**Clean legal conclusion.** You cannot pool tokens. You can pool *dollars* into a single organizational account and spend them centrally — the Vesuvius Challenge model, entirely permitted. Batch APIs then halve the bill at all three majors, and open-weight rates cut it by another one to two orders of magnitude.

---

## Part 3 — Analysis: what makes a problem brute-forceable, and what pooling can supply

The Navier–Stokes run worked because four conditions held simultaneously, and only one of them is about compute. First, a **cheap, total, mechanical verifier**: Lean either accepts the proof term or it does not, at negligible cost relative to generating it, which is what made it rational to burn 130 billion output tokens on candidates that were almost all wrong — the asymmetry between generation cost and verification cost *is* the trick, and it is the same asymmetry that let distributed.net hand untrusted volunteers a keyspace block and that TOPLOC re-creates for untrusted GPU workers. Second, a **samplable hypothesis space with structure**, supplied here not by enumeration but by a decade of the Córdoba–Martínez-Zoroa program plus Alpöge and Buckmaster's smooth-forcing route; OpenAI's agents sampled from a space someone else had already narrowed to a few plausible attacks. Third, a **partial-credit signal**: FunSearch and AlphaEvolve are explicit that their objective is a *number*, so search can hill-climb; a pass/fail verifier alone gives no gradient and degenerates to blind sampling. Fourth, **fully digitized inputs**, trivially true for equations. Score the Voynich manuscript against these and the picture is uncomfortable: inputs are digitized (good), the space of ciphers and languages is samplable (good), but there is **no cheap total verifier** — "is this a correct decipherment?" is a human judgment call, not a Lean kernel — and consequently **no honest partial-credit signal** either, since every plausible scoring function (n-gram plausibility, dictionary coverage, morphological fit) is precisely what generates the field's endless stream of confident false positives. That is the binding constraint, not money. So pooled tokens can supply only the third of the four inputs: throughput over a samplable space. A **coordinator** must supply everything else — the verifier (a pre-registered, adversarially tested, mechanically computable acceptance test written *before* the search, with a null-model false-positive rate measured on synthetic gibberish), the scoring function and its calibration, deduplication so a thousand donors do not re-sample the same region, the open corpus and its provenance, and the trust model for accepting untrusted contributors' claims. Since credits are legally non-transferable anyway, the coordinator is unavoidable: the only sanctioned architecture is pooled *dollars* in one org account (OpenRouter org, batch API, open-weight models at $0.11–$3.20 per million output tokens, i.e. $14K–$416K for a 130B-token campaign), with Vesuvius's prize-plus-open-data structure as the governance template. Build the verifier first; if you cannot write one a skeptic would pre-commit to, no amount of pooled compute will help — and the correct reading of RC5-72, 15.7% done after 23 years, is that pooled volunteers buy a constant factor, never an exponent.

---

## Could not verify

- **Raw openai.com HTML.** openai.com 403s direct fetch; the 130B / 300B / 4.9M / 2.7M figures, the $15M, and the 10,000-concurrent-agents claim come from the `r.jina.ai` rendering of that page, corroborated independently by Simon Willison's verbatim quotes. Two independent renderings agree, but I did not read the source page directly. An HN item claims OpenAI later edited the press release and the Lean code — **unverified**.
- **Anthropic Supplemental Credits Terms** — both `anthropic.com/legal/credits` and `.../supplemental-credits-terms` returned 404. Anthropic's position on prepaid credit *transferability* is **unconfirmed**; only the resale ban and the account-sharing ban are confirmed.
- **DeepMind "9 of 353 Erdős problems at a few hundred dollars per problem"** — Quanta only; I could not locate the primary arXiv paper through the arXiv API.
- **INTELLECT-1 contributor count** (commonly cited as ~30 independent contributors) — the release blog gives node/GPU counts but not a contributor count, and does not say whether contributors were volunteers or paid.
- **Bittensor** — Wikipedia page 404'd; not verified from any source. **Hivemind, Together, Akash, io.net, Hugging Face Inference, Kaggle, Experiment.com, Kickstarter science** — not fetched this session; do not cite them from this document.
- **Gemini 3 Pro output pricing** — the pricing page render returned 3.8/3.5 Flash and 2.5 Pro but no current Pro-tier frontier price.
- **Petals' live swarm health** — README shows no shutdown notice, but I did not check the swarm monitor, so "usable today" is unconfirmed.
