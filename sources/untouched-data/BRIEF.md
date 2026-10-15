# Untouched-data survey — shared brief for research agents

*2026-10-15. Prompt: a Substack post ("I went looking for lost cities with Claude",
Nate, 11 Oct 2026) reports ~30 unrecorded earthen mounds on Mexico's Gulf coast in
NASA G-LiHT lidar collected in 2013 to measure forests, and nine unmapped stone
ruins in Arizona, for "a few hundred dollars of tokens". Precedent it cites:
Valeriana, a Maya city found in 2024 by a Tulane PhD student in public lidar
collected for carbon measurement. Question: where else is public data,
collected for some other purpose, a little compute away from a real discovery?*

Read `AGENTS.md` (rules 1, 2, 3, 6, 7 apply in full) and `ideas/pooled-compute.md`
(its lesson: compute is the cheap part; a **verifier** is what's scarce).

## What counts as a candidate

A **dataset × question** pair where all of these hold or nearly hold:

1. **Data is public and machine-readable now** (URL, format, size, license).
2. **It was collected for a different purpose**, or at a scale nobody has
   exhaustively looked at, so a gap plausibly exists. Give evidence of the gap
   (e.g. "the 2024 paper searched only tiles X"), not vibes.
3. **A hit can be checked**: ground truth, a registry to compare against, a
   follow-up observation, an expert who can confirm, a mechanical test. Name it.
4. **Precedent**: a real discovery made this way (sourced, tiered), or a
   reason to think one is possible.
5. **Cost** to a hobbyist with an LLM and a laptop/cloud VM: hours? $? GPUs?

## Every candidate must also record

- **Traps**: the known false-positive modes and the crank history of the
  field (Rule 7: calibrate against cases that went wrong; e.g. Google-Earth
  "pyramids", Planet Nine claims, SETI signals that were microwaves).
- **"Already done?"**: search whether someone has already swept it. An idea
  that is already a funded project or citizen-science effort is still worth
  listing, marked `CROWDED`.
- **Ethics/legal**: looting risk from publishing site coordinates, privacy,
  deanonymization, terms of service, export control, harm to living people.
  Rule: no candidates whose payoff is identifying private individuals, intercepting
  private communications, or defeating security. Say so and drop it if that
  is where an idea leads.

## Output format (write to your assigned file only)

Top: a 5-line summary of the domain's best bets.
Then one `###` section per candidate (aim for 6–10), with fields:

- **Data** (who collected it, why, size, URL, license)
- **Question / what a find looks like**
- **Gap evidence**
- **Verifier**
- **Precedent** (sourced)
- **Recipe** (concrete pipeline; what an LLM does vs what code does)
- **Cost**
- **Traps**
- **Crowding** (`OPEN` / `PARTLY` / `CROWDED`, with who)
- **Ethics**
- **Scores 1–5**: `data_ready`, `gap`, `verifier`, `cheapness`, `payoff`, `ethics_clear`
- **Sources** (URL + tier: PRIMARY/SCHOLARLY/SECONDARY/CLAIMANT/POPULAR)

End with `## Pilot in a day`: the single candidate you'd run first from a
Linux container with internet, Python, no GPU, ~1 day; give the exact
download URLs and steps. Then `## Unverified claims`.

## Budget and conduct

- Use WebSearch/WebFetch. Verify the claims that drive the scores; two or
  three fetches per candidate. Your training memory is not a source.
- Do NOT spawn agents of your own.
- Do not attempt the discovery itself; this is a survey (Rule 9).
- Write only your assigned file. Do not commit.

## Domains already assigned (files 01–06)

01 remote-sensing archaeology (lidar, CORONA, Sentinel, bathymetry wrecks) ·
02 astronomy (TESS, Gaia, DASCH, NEOWISE, SETI, HiRISE/LRO) ·
03 biology (SRA, museum specimens, bioacoustics, camera traps, aDNA, AlphaFold) ·
04 signals/geophysics/OSINT (seismic, infrasound, hydrophones, AIS, SAR, methane, ADS-B, WSPR, TLEs) ·
05 documents/archives (HTR on manuscripts, cipher letters, Genizah, papyri, palimpsests, newspapers, declassified, lost media) ·
06 wild cards (fan fiction, FAERS/NHTSA/consumer data, software archaeology, Erdős/OEIS, endangered-language audio, chess, Wikidata).
Files 07–08 are **new domains** only: do not re-survey the above.
