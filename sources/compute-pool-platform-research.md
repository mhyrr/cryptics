# Compute-pool platform research: bring-your-own-key volunteer workers

**Date:** 2026-09-21
**Scope:** Facts needed to judge whether a "volunteer runs a worker on their own
machine with their own API key, pulls work units from a coordinator, submits
results" design is workable. Does **not** cover credit/subscription transfer —
that is settled in `sources/pooled-compute-research.md` (transfer is not
possible on OpenAI, Anthropic, or OpenRouter).

## Method note — read this before trusting a quote

**Every `WebFetch` and `curl` in this session was refused by the network egress
proxy** (`EGRESS_BLOCKED` for `openrouter.ai`, `r.jina.ai`, `docs.anthropic.com`,
`arxiv.org`, `openrouter.zendesk.com`, `conductatlas.com`; `curl` returned
`CONNECT tunnel failed, response 403`). Only `WebSearch` was reachable.

Consequence: **no quotation below was read off the live page.** Quoted strings
come from search-engine summaries of those pages. They are marked
`(snippet-derived)`. URLs and tiers are given so a later session with working
egress can verify in one pass. Under repo rule 1 and rule 2, treat every
`(snippet-derived)` quote as *reported wording, not verified wording*. The
open verification tasks are listed under `## Could not verify`.

---

## 1. OpenRouter per-key controls (spend limit, expiry, model restriction)

**Finding — spend limit: yes.** OpenRouter API keys carry a credit limit field.
The `GET /api/v1/key` response exposes `limit`, `limit_remaining`, and
`limit_reset`; `limit_reset` accepts `daily`, `weekly`, `monthly`, or `null`
(no reset), and resets run at midnight UTC (weeks Monday–Sunday).
(snippet-derived)

**Finding — enforcement point matters.** Once a key reaches its limit, further
requests on that key are rejected *before* being forwarded to the upstream
provider, so they incur no upstream cost. (snippet-derived) This is the
property that makes a donor-capped key safe: the cap is enforced by OpenRouter,
not by the worker program.

**Finding — programmatic per-user keys: yes, and endorsed.** OpenRouter's
Management API (Provisioning keys) exposes `/api/v1/keys` with create / list /
get / update / delete. OpenRouter's own help center documents the pattern "one
API key per user with its own spending limit," describing a SaaS app that
creates a unique key per customer and sets a credit limit on it.
(snippet-derived)

**Finding — expiry: reported, not established.** Search summaries state key
creation supports "expiration (set when the key expires)" alongside credit
limit and reset limit. (snippet-derived) Separately, OpenRouter reserves the
right to expire *unused credits* after one year of purchase — a different
thing, do not conflate. The per-key expiry field name was not confirmed.

**Finding — model restriction per key: NOT CONFIRMED.** Nothing in the
retrieved material shows an allowed-models / model-allowlist field on an
OpenRouter key. Treat "restrict which models this key may call" as unverified;
see `## Could not verify`.

- https://openrouter.ai/docs/api_reference/limits — *PRIMARY* (vendor docs; not fetched)
- https://openrouter.ai/docs/api-reference/api-keys — *PRIMARY* (vendor docs; not fetched)
- https://openrouter.zendesk.com/hc/en-us/articles/51680687417499-Can-I-create-one-API-key-per-user-with-its-own-spending-limit-Management-API-keys — *PRIMARY* (vendor help center; not fetched)

### 1b. `/api/v1/generation/{id}` as a third-party receipt

**Finding: yes, it returns a cost and full token accounting.** The endpoint
`GET https://openrouter.ai/api/v1/generation` takes an `id` parameter (string,
min length 1) and returns, among other fields: `id`, `model`, `streamed`,
`generation_time`, `created_at`, `tokens_prompt`, `tokens_completion`,
`native_tokens_prompt`, `native_tokens_completion`, `num_media_prompt`,
`num_media_completion`, `origin`, and `total_cost`. (snippet-derived)

**Caveat that matters for the design:** whether a *third party* (the
coordinator, holding only the generation id and its own unrelated key) can read
another account's generation record is **not established**. The endpoint is
documented as authenticated; the retrieved material does not say whose key
authorizes the lookup. The safe reading is that the *donor* can pull the
receipt and forward it, not that the coordinator can pull it independently. See
`## Could not verify`.

- https://openrouter.ai/docs/api/api-reference/generations/get-generation — *PRIMARY* (vendor docs; not fetched)
- https://openrouter.ai/docs/cookbook/administration/usage-accounting — *PRIMARY* (vendor docs; not fetched)

---

## 2. OpenRouter terms: is a BYO-key volunteer workload permitted?

Three clauses are relevant. All wording below is (snippet-derived) from
https://openrouter.ai/terms.

1. **Multiple accounts / bypassing limits.** Users may not create false
   identities, misrepresent identity, or create multiple accounts as a single
   user *"for purposes of bypassing or circumventing use limits on the Site or
   Service."*
2. **Resale / competing service.** Users may not access the Site or Service
   *"for purposes of reselling API access to Models or otherwise developing a
   competing service."*
3. **Credential responsibility.** Users are responsible for the confidentiality
   and security of all API keys, tokens, passwords and other credentials, and
   for all activity and charges under their account or API Credentials, whether
   or not authorized.
4. **Restricted Models / circumvention.** Users must not use VPNs or proxies to
   reach Restricted Models, nor *"circumvent safeguards or measures implemented
   by OpenRouter or Model Providers designed to restrict access to Restricted
   Models."*

**Plain answer: unaddressed, and it does not trip any of the named
prohibitions — with one condition.**

- Clause 1 bites on *one person holding several accounts*. A pool of many
  distinct people, each with one account and one key, is not that. It becomes
  clause-1 conduct only if the pool recruits sockpuppets, or if the coordinator
  farms free-tier allowances across accounts to dodge a per-account cap.
- Clause 2 bites on *reselling access*. Nobody is paid and no API access is
  resold in this design, so it does not apply. Note the widely-repeated reading
  of this clause in community discussion: you may not expose OpenRouter access
  as an API of your own.
- Clause 3 is the design constraint, and it cuts in the design's favour: the
  key never leaving the donor's machine is exactly what clause 3 asks for. A
  variant where donors paste keys into a coordinator would be the risky one.
- Clause 4 is not implicated as long as the worker does not route around
  geographic or model-access restrictions.

Rate limits specifically: search summaries note that additional accounts or keys
*do not* raise rate limits because OpenRouter governs capacity globally
(snippet-derived) — so a pool cannot be construed as a rate-limit dodge, since
there is no limit to dodge by aggregating.

- https://openrouter.ai/terms — *PRIMARY* (vendor terms; not fetched)
- https://openrouter.ai/terms/stealth — *PRIMARY* (Stealth Program EULA separately forbids exceeding or bypassing rate limits, API call restrictions, or safety measures; applies only to stealth-program models)
- https://news.ycombinator.com/item?id=47703636 — *POPULAR* (community reading of the resale clause)

---

## 3. Anthropic API: per-workspace spend limits and per-key scoping

**Finding: yes for spend limits, in the Console; no for the Admin API.**
Anthropic Workspaces support monthly spend limits set per workspace, with alert
thresholds, configured on a "Spend limits" tab in the Console. API keys are
scoped to a workspace. (snippet-derived)

**Limitation:** the Admin API supports workspace CRUD and member management but
exposes **no endpoint to configure per-workspace rate or spend limits
programmatically** — that is Console-UI only. Admin API calls require an Admin
API key, an `org:admin` OAuth token, or an unscoped personal/service-account
key; **workspace-scoped keys do not work against the Admin API.**
(snippet-derived)

Implication for the design: an Anthropic-key donor can cap their exposure, but
only by hand in the Console, and a coordinator cannot provision capped keys for
donors the way it could on OpenRouter.

- https://platform.claude.com/docs/en/manage-claude/workspaces — *PRIMARY* (vendor docs; not fetched)
- https://platform.claude.com/docs/en/api/rate-limits — *PRIMARY* (vendor docs; not fetched)
- https://claude.com/blog/workspaces — *PRIMARY* (vendor announcement; not fetched)
- https://github.com/anthropics/claude-quickstarts/issues/371 — *SECONDARY* (feature request: Admin API endpoint for workspace rate/spend limits)

---

## 4. Navier–Stokes, 2026: who published what

The user's belief was "OpenAI and probably also Anthropic." **Half right.**

**OpenAI: yes, institutionally, on 2026-09-08.** OpenAI announced that an
internal model described as significantly more capable than GPT-6 Astra
produced a proof that the 3D Navier–Stokes equations can develop a singularity
in finite time. The run is reported as roughly **10,000 agents, ~130B tokens,
88 hours**. The reported method is the one directly relevant here: agents first
attacked a simpler cousin — the unforced Euler equations — solving it with
~1,000 agents over ~50 hours, then scaled to ~10,000 agents for Navier–Stokes.
(snippet-derived)

**Anthropic: no institutional publication found.** What exists is an
individual-authorship result: **Levent Alpöge (an Anthropic employee)** with
**Tristan Buckmaster (Courant, NYU)** posted, on 2026-09-07 — about 12 hours
before OpenAI's announcement — three preprints establishing finite-time blowup
with smooth forcing for (a) the incompressible porous medium equation, (b) the
2D Boussinesq system, and (c) the 3D incompressible Euler equations, **with Lean
formalizations of the proofs**. They describe heavy LLM use across the project
(Claude to identify elements of prior proofs and reproduce arguments; Claude and
OpenAI's Codex to write the main body), and say they hold an **unverified**
proof of blowup for an easier version of Navier–Stokes. This is not an
Anthropic "many agents on one open problem" program result.

A priority dispute followed; Buckmaster reports contacts in which OpenAI told
him an internal model had produced a ~100-page proof of finite-time blowup for
the *forced* Navier–Stokes equations. The status of OpenAI's claim as of the
reporting is **announced and contested, not independently confirmed**.

Two facts worth carrying into a design doc: the Alpöge–Buckmaster side attached
**machine-checkable Lean formalizations**, and the OpenAI side is the existence
proof that a large agent fan-out on a single open problem is a real method with
published resource numbers.

- https://openai.com/index/navier-stokes-solution/ — *PRIMARY* (claimant's own announcement; also *CLAIMANT* in the repo's sense)
- https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/ — *POPULAR*
- https://www.science.org/content/article/how-ai-math-breakthrough-ignited-controversy — *POPULAR* (Science news section, not peer-reviewed)
- https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy — *SECONDARY*
- https://www.unite.ai/buckmaster-and-alpoge-post-ai-fluid-blowup-proofs-dispute-openai-contact/ — *POPULAR*
- https://quomodocumque.wordpress.com/2026/09/07/finite-time-blowup/ — *POPULAR* (Jordan Ellenberg's blog, contemporaneous)

---

## 5. BOINC mechanics worth borrowing

**(a) The credit unit.** The Cobblestone (named after Jeff Cobb of SETI@home)
is **1/200 day of CPU time on a reference computer that does 1 GFLOPS on the
Whetstone benchmark.** (snippet-derived)

**Normalization across heterogeneous hardware.** CPU credit derives from the
Whetstone benchmark score; GPU credit from a manufacturer-supplied formula.
Under CreditNew, *host normalization* is the anti-cheat: *"An exaggerated claim
will increase `host_app_version.pfc_avg`, causing subsequent credit to be scaled
down proportionately."* (snippet-derived) I.e. credit is not taken at the
host's word; a host that over-claims is silently deflated on later work.

**(b) Redundancy / quorum validation.** Each app that uses replication has a
**validator**: it examines the instances of a job, compares their output files,
decides whether a quorum of equivalent results exists, and if so designates one
instance as **canonical**. When enough successful results return (the quorum),
the server compares them for consensus. Both the comparison method (which may
have to tolerate platform-varying floating-point arithmetic) and the consensus
policy (e.g. best two of three) are **supplied by the application**, not by the
framework. (snippet-derived)

**(c) Deadlines and reissue.** If an instance of job J is dispatched to a host
at time T, its deadline is **T + `delay_bound(J)`**. If results are not returned
by the deadline, the instance is assumed lost or excessively late and **a new
instance of J is created.** (snippet-derived)

- https://boinc.berkeley.edu/wiki/Computation_credit — *PRIMARY* (project docs; not fetched)
- https://boinc.berkeley.edu/trac/wiki/CreditNew — *PRIMARY* (project docs; not fetched)
- https://github.com/BOINC/boinc/wiki/JobReplication — *PRIMARY*
- https://github.com/BOINC/boinc/wiki/Validators — *PRIMARY*
- https://arxiv.org/pdf/1903.01699 — *SCHOLARLY* (Anderson, "BOINC: A Platform for Volunteer Computing")
- https://en.wikipedia.org/wiki/BOINC_Credit_System — *SECONDARY*

---

## 6. TOPLOC (Prime Intellect): needs activations, so not applicable to API calls

**Finding: TOPLOC verifies by hashing intermediate activations, which a
black-box API does not expose. It cannot verify a donor's OpenRouter or
Anthropic API call.**

TOPLOC is *"a compact locality sensitive hashing mechanism for intermediate
activations"* that detects unauthorized modification of models, prompts, or
compute precision, reported at 100% accuracy with no false positives or
negatives in the paper's evaluation. It is robust across GPU types, tensor
parallel dimensions and attention kernels, validates up to 100x faster than the
original generation, and a polynomial encoding scheme cuts proof memory ~1000x
to **258 bytes per 32 new tokens**. The reference implementation is integrated
with vLLM. (snippet-derived)

The verifier must be able to recompute/inspect activations for the claimed
tokens, i.e. hold the weights and run the model. A donor calling a hosted API
receives text and usage counts only. **Verification of BYO-key API work must
therefore rest on something else** — provider-side receipts (see 1b),
replication/quorum (see 5b), or machine-checkable artifacts (see the Lean point
in 4).

- https://arxiv.org/abs/2501.16007 — *SCHOLARLY* (ICML 2025; not fetched)
- https://www.primeintellect.ai/blog/toploc — *PRIMARY* (authors' own writeup; not fetched)
- https://github.com/PrimeIntellect-ai/toploc — *PRIMARY* (reference implementation)

---

## 7. ARC Prize compute cap (efficiency-normalized scoring precedent)

**ARC Prize 2026, ARC-AGI-2 track.** Objective: **85% accuracy on the private
evaluation set *within the Kaggle efficiency limits*.** The submission runs in a
Kaggle sandbox with a **12-hour runtime budget** (combined CPU/GPU), and
**no internet access during evaluation — so no API-hosted systems (GPT, Claude,
etc.) can be called at runtime.** Solutions must be open-sourced before official
private-evaluation scores are issued. (snippet-derived)

**The compute cap in money terms.** The 2025 competition's Kaggle efficiency
limit worked out to roughly **$50 of compute per submission across 120 tasks —
about $0.42 per task.** Separately, the public ARC Prize **leaderboard only
lists systems that cost under $10,000 to run**, which is the efficiency-
normalized reporting rule rather than the competition cap. (snippet-derived)

Note for anyone borrowing this: the Kaggle cap is enforced as *sandbox wall-clock
on fixed hardware*, and the dollar figure is a derived equivalent, not the rule
itself. The no-internet rule means ARC's cap is not directly transplantable to a
BYO-API-key design; what transplants is the idea of scoring accuracy *per unit
of spend*.

- https://arcprize.org/competitions/2026/arc-agi-2 — *PRIMARY* (not fetched)
- https://arcprize.org/competitions/2026 — *PRIMARY* (not fetched)
- https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/rules — *PRIMARY* (rules text; not fetched)
- https://arcprize.org/leaderboard — *PRIMARY* ($10,000 listing threshold)

---

## 8. Prediction market attached to a research bounty or prize

**Finding: a partial precedent exists (Manifund impact certificates), and the
operators' own retrospective says it did not work well. No clean example of a
prediction market wired to a research bounty was found.**

Manifund's **impact certificates** are the nearest mechanism: *"venture funding
for charitable endeavors"* where investors buy shares ("certs") in a project
that pay out **if the project later receives a retroactive prize.** Manifund ran
three such programs: **ACX Grants, the Manifold Community Fund, and a ChinaTalk
essay competition** (the last giving away $6,000 in prize money for essays
making predictions about the future of China, explicitly intended to make use of
Manifold's prediction markets). (snippet-derived)

**The operators' verdict is negative.** Manifund's own Q1 retrospective reports
it *"had been hard to get investor interest in impact certificates,"* and that
they *"still hadn't found a use case where certs led to better funding
decisions."* (snippet-derived) Anyone proposing this mechanism should read that
retro first.

No documented case was found of a Manifold or Metaculus market on "will X be
solved by date" being *formally attached* to a bounty — i.e. where market price
determines payout, bounty size, or resource allocation. Markets of that question
form certainly exist; the *attachment* is what is missing. See
`## Could not verify`.

- https://manifund.org/about/impact-certificates — *PRIMARY* (not fetched)
- https://www.lesswrong.com/posts/AzoopyYgzNimBJDdY/manifund-q1-retro-learnings-from-impact-certs — *PRIMARY* (operators' own retrospective)
- https://manifund.substack.com/p/manifund-2023-in-review — *PRIMARY*

---

## Could not verify

Everything here failed for one of two reasons: the egress proxy blocked all
page fetches, or the fact is genuinely absent from what search returned. The
first group is a tooling wall, not a research wall — a session with working
egress clears it in a handful of fetches.

**Blocked by the egress proxy (verify verbatim when egress works):**

1. **Every quotation in this brief.** All are snippet-derived. Highest priority
   to re-verify against the live page: the OpenRouter terms clauses in §2, the
   Cobblestone definition in §5, and the ARC efficiency-limit wording in §7.
2. `https://openrouter.ai/terms` — the full acceptable-use section, its
   effective date, and whether any clause addresses coordinated multi-user
   workloads at all. Section numbering could not be recovered.
3. `https://openrouter.ai/docs/api-reference/api-keys` — exact request schema
   for key creation: the precise field names for limit, expiry, and any model
   restriction.
4. `https://docs.anthropic.com` / `https://platform.claude.com` — the workspace
   spend-limit and key-scoping pages, read directly.
5. `https://arxiv.org/abs/2501.16007` — the TOPLOC paper's own statement of its
   threat model and what the verifier must possess.
6. `https://openai.com/index/navier-stokes-solution/` — OpenAI's own numbers
   (10,000 agents / 130B tokens / 88 hours) read off the announcement rather
   than off reporting about it.

**Genuinely open questions:**

7. **Per-key model restriction on OpenRouter.** No evidence found that a key can
   be limited to a named set of models. If the design needs "this donated key
   may only call model X," treat it as unsupported until shown otherwise.
8. **Per-key expiry field on OpenRouter.** Reported in summaries; field name
   unconfirmed. Distinct from the one-year unused-credit expiry.
9. **Third-party readability of `/api/v1/generation/{id}`.** Whether a
   coordinator holding only a generation id — and not the donor's key — can
   fetch that receipt. Assume no until tested. This is load-bearing: if the
   coordinator cannot independently pull the receipt, the receipt is
   donor-supplied and therefore forgeable, and verification falls back to
   replication.
10. **Independent confirmation of OpenAI's Navier–Stokes proof.** As of the
    retrieved reporting the claim is announced and disputed. Whether the ~100-page
    proof has been checked (by referees or by formalization) is unresolved.
11. **Whether Anthropic published any institutional "many agents on one open
    problem" result in 2026.** Two searches found none — only the individual
    Alpöge/Buckmaster preprints. Recorded as *not found*, not as *does not
    exist*.
12. **A prediction market formally attached to a research bounty.** No clean
    precedent found where market price sets payout or allocation. Metaculus was
    not searched separately for lack of budget.
