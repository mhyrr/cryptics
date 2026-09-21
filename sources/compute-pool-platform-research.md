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

**Second pass, 2026-09-21.** A later session had egress to exactly three hosts:
`platform.claude.com`, `github.com`, `raw.githubusercontent.com`. Everything
on those hosts was read off the live page and is marked `(verified
2026-09-21)` below: all of §3 (Anthropic), all of §5 (BOINC, via the GitHub
wiki), the README half of §6 (TOPLOC), the generation-receipt call shape in
§1b (from OpenRouter's own examples repo), and issue 371. `openrouter.ai`,
`boinc.berkeley.edu`, `arxiv.org`, `arcprize.org`, `openai.com`,
`manifund.org`, `lesswrong.com`, `wikipedia.org` and the news sites were still
policy-blocked (`403` on `CONNECT`), so §1, §2, §4, §7 and §8 remain
`(snippet-derived)` in full.

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

**Call shape, from OpenRouter's own examples repository (verified 2026-09-21).**
The only working receipt lookup found in public OpenRouter code is
`claude-code/statusline.ts` in `OpenRouterTeam/openrouter-examples`. It calls
`GET https://openrouter.ai/api/v1/generation?id=<id>` with
`Authorization: Bearer <apiKey>`, where the file header says the key is *"your
OpenRouter API key"*, i.e. the key that made the generation. It reads the
record from `json.data` and types it as `{ total_cost, cache_discount,
provider_name, model }`, so the response is nested under `data` and carries
`cache_discount` and `provider_name`, which the field list above omits. This is
evidence for the safe reading (owner pulls the receipt and forwards it), not
evidence that a third party is refused. Nothing in that repository (91 files)
touches `/api/v1/keys`, `limit_reset`, or a key expiry field, so the key
schema in §1 stays unverified.

- https://openrouter.ai/docs/api/api-reference/generations/get-generation — *PRIMARY* (vendor docs; not fetched)
- https://openrouter.ai/docs/cookbook/administration/usage-accounting — *PRIMARY* (vendor docs; not fetched)
- https://raw.githubusercontent.com/OpenRouterTeam/openrouter-examples/main/claude-code/statusline.ts — *PRIMARY* (vendor's own example code; fetched 2026-09-21)

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

All quotations in this section were read off the live pages on 2026-09-21.

**Finding: yes for spend limits, in the Console; no for the Admin API.**
(verified 2026-09-21) The workspaces page: *"You can set workspace limits
lower than (but not higher than) your organization's limits"*, with
*"**Spend limits:** Cap monthly spending for a workspace. Set these on the
workspace's **Spend limits** settings tab in the Claude Console"* and, on the
same tab, alerts *"when spending reaches certain thresholds."* Key scoping:
*"**API keys** can be scoped to a single workspace. In this case, they can only
access resources within that workspace."*

**Three conditions the first pass missed** (verified 2026-09-21):

- *"You cannot set limits on the Default Workspace."* A donor whose
  organization has only the Default Workspace cannot cap anything until they
  create a second workspace and scope a key to it.
- *"Organization-wide limits always apply, even if workspace limits add up to
  more."* Tier caps on the rate-limits page: Start $500/month, Build
  $1,000/month, Scale $200,000/month, Custom uncapped.
- Per-user monthly spend limits exist only in the auto-created Claude Code
  workspace (*"It is the only workspace that supports per-user monthly spend
  limits"*), not in an ordinary API workspace.

**How a capped key fails** (verified 2026-09-21; the rate-limits page). A
donor's cap fails closed and distinguishably: *"When usage reaches a spend
limit you set, requests return HTTP 400 with error type
`invalid_request_error`. The message begins `You have reached your specified
API usage limits`, or `You have reached your specified workspace API usage
limits` for a workspace limit, and states when access resumes."* Hitting the
organization's *tier* cap instead returns HTTP 429 with
`"error_code": "enforced_spend_limit_reached"` and no `retry-after` header. A
worker can therefore tell "this donor's cap is spent" from "this donor's whole
organization is capped" and stop cleanly on either.

**Limitation, sharpened** (verified 2026-09-21; the Admin API page). The Admin
API accepts *"an Admin API key … an OAuth bearer token with the `org:admin`
scope … a personal key or service account key that isn't scoped to a specific
workspace"*; *"Workspace keys don't work there."* Its workspace endpoints are
create, get, list, update, archive, and member add/update/remove. The only
limits entry is a read-only Rate Limits API (*"Read the rate limits configured
for your organization and its workspaces"*). There is **no endpoint to set a
workspace spend or rate limit**. Harder than that, from the page's FAQ:
*"**Can I create new API keys through the Admin API?** No. You create API keys
in the Claude Console. The Admin API can only read, rename, and change the
status of existing keys."* A coordinator cannot provision Anthropic keys for
donors at all, capped or otherwise.

**A Spend Limits API does exist, and does not help.** (verified 2026-09-21)
*"The Spend Limits API lets you set a spend limit on each Claude Enterprise
member"* and *"is available to Claude Enterprise organizations only. It is not
available to Claude Platform (Claude Console) organizations."* It is per user
seat, not per workspace or per key. Recorded so a later reader does not think
it was missed.

**Per-key controls** (verified 2026-09-21; the authentication page). The only
per-key settings documented are workspace scope and expiry: *"you choose an
expiration: a preset (3 hours, 1 day, 7 days, or 30 days), a custom duration,
or Never … expiration is set at creation time and cannot be changed
afterward."* An expired key returns `401 authentication_error`, and the Admin
API reports `expires_at` (null for keys that never expire). **No per-key spend
cap and no per-key model restriction appear anywhere on the page.**

Implication for the design: an Anthropic-key donor caps exposure with three
by-hand steps (a dedicated workspace with a monthly Spend-limits cap, a key
scoped to that workspace, a key expiry chosen at creation). Model choice cannot
be constrained at the credential; the worker program has to honour the model
floor, which is trust-based. A coordinator cannot mint capped keys the way it
could on OpenRouter, because it cannot mint keys.

- https://platform.claude.com/docs/en/manage-claude/workspaces — *PRIMARY* (fetched 2026-09-21)
- https://platform.claude.com/docs/en/api/rate-limits — *PRIMARY* (fetched 2026-09-21)
- https://platform.claude.com/docs/en/manage-claude/admin-api — *PRIMARY* (fetched 2026-09-21)
- https://platform.claude.com/docs/en/manage-claude/spend-limits-api — *PRIMARY* (fetched 2026-09-21)
- https://platform.claude.com/docs/en/manage-claude/authentication — *PRIMARY* (fetched 2026-09-21)
- https://claude.com/blog/workspaces — *PRIMARY* (vendor announcement; not fetched, host blocked)
- https://github.com/anthropics/claude-quickstarts/issues/371 — *POPULAR* (a third-party feature request, open since 2026-03-11, titled "Feature Request: Admin API endpoint for Workspace Rate/Spend Limits"; corroborative only, the Admin API page above is the primary evidence; fetched 2026-09-21)

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

All quotations in this section were read off the BOINC GitHub wiki on
2026-09-21 (`raw.githubusercontent.com/wiki/BOINC/boinc/<Page>.md`). The
`boinc.berkeley.edu` host was still blocked; the wiki is the same project
documentation.

**(a) The credit unit.** (verified 2026-09-21) *"BOINC's unit of credit, the
**Cobblestone** (named after Jeff Cobb of SETI@home), is 1/200 day of CPU time
on a reference computer that does 1 GFLOPS based on the Whetstone benchmark."*
And: *"Credit has no monetary or other value; it's just a measure of how much
work your computers have done."* The definition lives on the wiki page
`Computation credit` (the URL has a `%20`), not on `CreditNew`, which only
carries the constant `cobblestone_scale is 200/86400e9`.

**Normalization across heterogeneous hardware.** (verified 2026-09-21)
CreditNew: *"BOINC estimates the **peak FLOPS** of each processor. For CPUs,
this is the Whetstone benchmark score. For GPUs, it's given by a
manufacturer-supplied formula."* Host normalization is the anti-cheat, under
the heading *Cheat prevention*: *"Host normalization mostly eliminates the
incentive to cheat by claiming excessive credit (i.e., by falsifying benchmark
scores or elapsed time). An exaggerated claim will increase
`host_app_version.pfc_avg`, causing subsequent credit to be scaled down
proportionately. This means that no special cheat-prevention scheme is needed
for single replications; in this case, granted credit = claimed credit."*

**What host normalization does not stop** (verified 2026-09-21; same page, a
fact the first pass missed). CreditNew names two residual attacks: *"One-time
cheats (for example, claiming a PFC of 1e304)"*, handled by a sanity check that
*"grants a default amount of credit and treats the host with suspicion for a
while"*, and *"Cherry picking"* when jobs vary in size. Note also the direction
of the mechanism: *"The host normalization mechanism reduces the claimed credit
of hosts that are less efficient than average, and increases the claimed credit
of hosts that are more efficient than average."* A pool that borrows the
deflation rule still needs a per-unit credit cap and a defence against
selective abandonment of hard units.

**(b) Redundancy / quorum validation.** (verified 2026-09-21) JobReplication:
*"BOINC provides a form of redundant computing in which each computation is
performed on multiple clients, the results are compared, and are accepted only
when a 'consensus' is reached."* Then: *"when a sufficient number (a 'quorum')
of successful results have been returned, it compares them and sees if there is
a 'consensus'. The method of comparing results (which may need to take into
account platform-varying floating point arithmetic) and the policy for
determining consensus (e.g., best two out of three) are supplied by the
application. If a consensus is reached, a particular result is designated as
the 'canonical' result."* The worked examples use `min_quorum = 2` and
`target_nresults = 3`.

The Validators page adds the default rule: *"**Replication check**: if the job
is replicated, compare its replicas. If a strict majority are found to be
'equivalent', those replicas are considered valid and the rest are marked as
invalid."* Equivalence is application-defined (*"regarding floating-point
numbers as equivalent if they agree within some tolerance"*). Three validator
switches are directly reusable by a pool: `--max_granted_credit X` (*"Grant no
more than this amount of credit to a job"*), `--update_credited_job` (records
which user contributed to each work unit), and `--check_punitive` (*"run the
validator for failed tasks (Compute error) so the validator can check for known
host issues and set the max number of jobs per day to one to avoid that host
getting more tasks"*): throttle a misbehaving worker rather than ban it.

**(c) Deadlines and reissue.** (verified 2026-09-21; the first pass cited
`JobReplication` for this, which does not contain it. The rule lives in the
work-unit parameters.) `JobIn`, under `delay_bound`: *"An upper bound on the
time (in seconds) between sending a result to a client and receiving a reply.
The scheduler won't issue a result if the estimated completion time exceeds
this. If the client doesn't respond within this interval, the server 'gives up'
on the result and generates a new result, to be assigned to another client. Set
this to several times the average execution time of a workunit on a typical
PC."* The verbatim formula, from `BackendLogic`:
`result.report_deadline = now + wu.delay_bound`. Two neighbouring parameters
the first pass omitted and a pool needs: `min_quorum` (*"The validator is run
when there are this many successful results. If a strict majority agree, they
are considered correct."*) and `max_total_results` (*"If the total number of
results for this workunit would exceed this, the workunit is declared to be in
error"*), which is the reissue cap that stops a poisoned unit from being
re-issued forever.

- https://raw.githubusercontent.com/wiki/BOINC/boinc/Computation%20credit.md — *PRIMARY* (project wiki; fetched 2026-09-21)
- https://raw.githubusercontent.com/wiki/BOINC/boinc/CreditNew.md — *PRIMARY* (fetched 2026-09-21)
- https://raw.githubusercontent.com/wiki/BOINC/boinc/JobReplication.md — *PRIMARY* (fetched 2026-09-21)
- https://raw.githubusercontent.com/wiki/BOINC/boinc/Validators.md — *PRIMARY* (fetched 2026-09-21)
- https://raw.githubusercontent.com/wiki/BOINC/boinc/JobIn.md — *PRIMARY* (fetched 2026-09-21)
- https://raw.githubusercontent.com/wiki/BOINC/boinc/BackendLogic.md — *PRIMARY* (fetched 2026-09-21)
- https://boinc.berkeley.edu/wiki/Computation_credit — *PRIMARY* (same text on the project site; host blocked, not fetched)
- https://boinc.berkeley.edu/trac/wiki/CreditNew — *PRIMARY* (same; not fetched)
- https://arxiv.org/pdf/1903.01699 — *SCHOLARLY* (Anderson, "BOINC: A Platform for Volunteer Computing"; not fetched)
- https://en.wikipedia.org/wiki/BOINC_Credit_System — *SECONDARY* (not fetched)

---

## 6. TOPLOC (Prime Intellect): needs activations, so not applicable to API calls

**Finding: TOPLOC verifies by hashing intermediate activations, which a
black-box API does not expose. It cannot verify a donor's OpenRouter or
Anthropic API call.**

**From the reference implementation's README** (verified 2026-09-21): TOPLOC
*"leverages locality sensitive hashing of intermediate activations to verify
that LLM providers are using authorized model configurations and settings."*
Its stated feature set, in full: *"Detect unauthorized modifications to models,
prompts, and precision settings; 1000x reduction in storage requirements
compared to full activation storage; Validation speeds up to 100x faster than
original inference; Robust across different hardware configurations and
implementations."*

**From the paper and blog only** (snippet-derived; `arxiv.org` and
`primeintellect.ai` still blocked): the *258 bytes per 32 new tokens* proof
size, the polynomial encoding scheme, the *100% accuracy with no false
positives or negatives* evaluation result, and the vLLM integration. None of
these four appears in the README; the first pass attributed them to it too
loosely.

**Why the verifier must hold the model** (verified 2026-09-21). The README never
says so in prose; the API does. Every verification entry point takes
activations as its first argument:
`verify_proofs_base64(activations, proofs, decode_batching_size=3, topk=4,
skip_prefill=False)`, returning `VerificationResult(exp_intersections=…,
mant_err_mean=…, mant_err_median=…)`. The verifier must produce the
intermediate activations for the claimed tokens, which means running the
weights. A donor calling a hosted API receives text and usage counts only.
**Verification of BYO-key API work must therefore rest on something else**:
provider-side receipts (see 1b), replication/quorum (see 5b), or
machine-checkable artifacts (see the Lean point in 4).

- https://arxiv.org/abs/2501.16007 — *SCHOLARLY* (ICML 2025; not fetched, host blocked)
- https://www.primeintellect.ai/blog/toploc — *PRIMARY* (authors' own writeup; not fetched, host blocked)
- https://raw.githubusercontent.com/PrimeIntellect-ai/toploc/main/README.md — *PRIMARY* (reference implementation; fetched 2026-09-21)

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

Everything here failed for one of two reasons: the egress proxy blocked the
page fetch, or the fact is genuinely absent from what search returned. The
first group is a tooling wall, not a research wall.

**Cleared on 2026-09-21** (hosts `platform.claude.com`, `github.com`,
`raw.githubusercontent.com` became reachable): item 4 below (Anthropic pages,
now read directly), the BOINC quotations in §5 (read from the GitHub wiki), the
README half of §6, and the receipt call shape in §1b. Struck items are kept
for the record.

**Still blocked by the egress proxy (verify verbatim when egress works):**

1. **Every quotation in §1, §2, §4, §7 and §8.** Still snippet-derived. Highest
   priority: the OpenRouter terms clauses in §2 and the ARC efficiency-limit
   wording in §7. (The Cobblestone definition in §5 is now verified.)
2. `https://openrouter.ai/terms` — the full acceptable-use section, its
   effective date, and whether any clause addresses coordinated multi-user
   workloads at all. Section numbering could not be recovered.
3. `https://openrouter.ai/docs/api-reference/api-keys` — exact request schema
   for key creation: the precise field names for limit, expiry, and any model
   restriction.
4. ~~`https://platform.claude.com` — the workspace spend-limit and key-scoping
   pages, read directly.~~ **Done 2026-09-21**; see §3. Net new facts: the
   Default Workspace cannot be capped; the Admin API cannot create keys at all;
   caps fail with a distinguishable HTTP 400; per-key expiry exists; no per-key
   spend cap or model restriction exists.
5. `https://arxiv.org/abs/2501.16007` — the TOPLOC paper's own statement of its
   threat model, and the 258-byte, 100%-accuracy and vLLM specifics. (The
   README's activation-taking API already settles what the verifier must
   possess; see §6.)
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
   replication. Partial evidence 2026-09-21: OpenRouter's own example code
   authorizes the lookup with the generation owner's key (§1b), which supports
   "assume no" without proving it.
13. **Anthropic per-key model restriction.** Now read directly: absent from the
    authentication page (§3). Recorded as *not offered*, not as *forbidden*.
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
