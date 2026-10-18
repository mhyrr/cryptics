# PLANS — things we should do

A running list of what to work on next, across the catalog, the dives and the
untouched-data survey. Pinned items go first; reorder freely. When an item
starts, it gets a home (a dive, a pilot folder) and this line points there.
`NEXT-SESSION.md` stays the handoff for what is in flight; this file is the
queue.

## The test (Greg, 2026-10-18): true secrets the world does not know

Novelty comes before readability. A text counts only if we can show:
(a) nobody has published a reading of it;
(b) no plaintext can exist by construction: no clear copy kept by the sender
    and no decipherment by the recipient. Private ciphers and intercepts that
    were never broken pass. Chancery letters usually fail;
(c) we can reach the images.

Only then ask whether code can read it. Survey under this test:
`sources/novel-secrets-2026-10-18.md`.

## Pinned: discoveries about the world (2026-10-18)

Picked because a find here is new knowledge, not bookkeeping, and the check
is mechanical or physical.

1. **Logan: search the whole public sequencing archive for a class of element
   nobody has swept.**
   - Logan is NCBI's Sequence Read Archive assembled into contigs (Institut
     Pasteur): about 38 M runs.
   - Precedent: obelisks were found in already-public data (Zheludev et al.,
     *Cell* 2024), and Serratus found about 132 k new RNA viruses (*Nature*
     2022).
   - `logan-pub` S3 answers from this container (200, 2026-10-18).
   - Blocked: NCBI and EBI hosts, which the sample metadata and raw-read
     confirmation need.
   - Pilot:
     1. Calibrate by rediscovering known obelisks in a few hundred runs.
     2. Run one search for an element class nobody has swept.
   - Home when started: `ideas/untouched-data/pilots/03-logan/`.
   - Candidate notes: `sources/untouched-data/03-biology.md` §1.
2. **Unrecovered meteorite falls: NEXRAD Level II radar × GOES-GLM bolides.**
   - A find is a radar debris signature under a recorded fireball, with no
     recovery on record. That gives a strewn field someone can walk.
   - Precedent: a 2024 review counts 33 unrecovered radar falls.
   - First check: whether NASA already cross-checks every GLM bolide.
   - Then test which data hosts this container can reach. NEXRAD and GOES
     are on public S3.
   - Candidate notes: `sources/untouched-data/07-new-domains-instruments.md`
     §2.
3. **OEIS conjectures checked only to the edge of their own b-file.**
   - The pilot ran on branch `untouched-data-survey`: 3 conjectures disproved,
     5 entry errors, drafts written and not posted.
   - Next:
     - Greg reviews and posts the drafts.
     - Merge the pilot to `main`.
     - Run the remaining ~580 candidates the first batch skipped.
   - Pilot: `ideas/untouched-data/pilots/01-oeis-conjectures/` (on that
     branch).

## Known key + hard-to-reach pages (Greg screenshots, we read)

The es. 132 pattern. The key was published, the pages were "free online", and
nobody had put them together because the viewer blocks scripts. Greg's browser
is the scarce resource.
- Ranked survey (15 rows, click-by-click shopping list for the top 3):
  `sources/screenshot-opportunities-2026-10-18.md`. Top: es. 132 remaining folios
  plus f. 129 as a held-out check; BnF fr. 3641 Mendoza letters (Cp.30 + Nevers
  key 54; novelty doubtful: nos. 3/4, 28/29, 43/44 are already deciphered and
  serve only as calibration, and the four targets may have clear minutes in
  Simancas, AGS Estado K, so check that first); Saint-Goard fr. 16106 with Mousset. Try the Gallica IIIF full-size URL
  in a browser before screenshotting.
- Already known:
  - es. 132 ff. 39, 50, 79, 150, 177.
  - Saint-Goard, BnF fr. 16106–16108, with Mousset's 1912 key.
  - Philip IV to Velada (Morgan Library).
  - Ungnad to Maximilian II (HHStA; a scan order of about €100–160).

## Ciphers with a small key search
- **Armstrong to Madison, 20 Feb 1808.** The key was "concerted with another
  correspondent", which leaves about five legation codes. Two are tested. The
  test runs here in 1–4 CPU-hours.
  - Source: `sources/untouched-data/10-decryptable-resweep-2026-10-18.md`.
  - First re-check Bourdeau's notes, which are the basis for calling it open.
- **Blume:** a key list built from the dossier for K2 (item 3 in
  `puzzles/blume-salamanca-1937/NEXT.md`). Also an AlphaEvolve-style loop
  that evolves the solver against the planted w2 18–20 controls.

## Housekeeping
- **Papal ciphers (Barb.lat.6960).** Bourdeau's notes report the 1628 key
  reads all 28 letters, apart from about 1,750 code groups. Verify, then close
  the dive as a calibration case.
- **Seismic attribution: no-go from here.** The event lists are unreachable.
  See `ideas/untouched-data/pilots/02-seismic-attribution/FEASIBILITY.md`.
  Revisit if Poli's table turns up.
