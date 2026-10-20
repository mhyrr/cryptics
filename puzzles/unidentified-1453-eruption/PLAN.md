# Research and evaluation path

Written 2026-10-20 from the four surveys in `sources/survey-2026-10-20/`.
Criteria numbers refer to `README.md`.

## The shape of the problem

The literature gives three facts and one gap.

- The plume went mostly north (asymmetry 0.83).
- The sulfur isotopes look extratropical (Burke 2023).
- The cooling was strongest at high northern latitudes (Esper 2017).
- **The survey found no published tephra search of the 1453 Greenland
  layer.** Abbott 2021 sampled TUNU2013 only at 1477 and 1479 and lists both
  1450s events as future work. Cole-Dai et al. 2013 report no tephra at
  1452/53, but which core they searched is unchecked (probably Antarctic).
  "No tephra found" in the popular account may mean "not looked for in
  Greenland", which is a different fact. Checking this is the first job of 02.

The first three point the same way: a Northern Hemisphere extratropical
eruption. The fourth suggests the decisive test may not have failed. It may
not have been run.

## Success tiers

A result at any tier is a finished result (AGENTS.md rule 8).

| Tier | Result | Open data enough? |
|---|---|---|
| T1 | Latitude band and season, with a calibrated interval | Yes |
| T2 | Shortlist of ≤ 5 named candidates with scores from a pipeline that has been tested blind on solved eruptions | Yes, if the 14C lab ages are published |
| T3 | Named volcano with a glass match | No. Needs 1453 ice shards or a distal cryptotephra |

"An unidentified North Pacific eruption" is a legitimate T1/T2 outcome. The
1477 Veiðivötn layer and the Greenland layer once tied to Vesuvius 79 CE
(now unidentified Aleutian) show region-level answers are real answers.

## Calibration set (rule 7)

Every method runs first on eruptions whose source is known, blind to the
answer, and is scored on how highly it ranks the truth. Candidates, to be
confirmed against eVolv2k v4's "attributed volcano" column:

- extratropical NH: Katmai/Novarupta 1912, Laki 1783, Veiðivötn 1477, Shiveluch 1854;
- tropical: Tambora 1815, Krakatau 1883, Pinatubo 1991, Samalas 1257;
- former mystery, now solved: 1831 Zavaritskii (Hutchison 2025).

**Leakage trap.** GVP dates many of these from the ice itself
(`StartEvidenceMethod = "Sidereal: Ice Core"`). The candidate scorer must drop
those dates, or it will match the ice to itself. The same rule holds for
UE 1453: GVP's Grímsvötn 1450 ± 10 and Katla 1450 ± 50 are dated by ice core,
so they need checking at source before they count.

## Experiments

Numbered in run order. Each lands in `analysis/NN-name/` with a README and a
checked-in result. LLMs extract; code computes.

**01-gvp-window (done).** The GVP eruption table, 1400–1500. 58 eruptions in
1420–1490 have VEI ≥ 4 or unknown VEI. 59 have a year ± uncertainty that
covers 1452. The only VEI-5 rows covering 1452 are Pinatubo 1450 ± 50 and
El Chichón unit B 1360 ± 100, both radiocarbon-dated and tropical.

**02-ice-onset (done 2026-10-20).** Pull NEEM-2011-S1 at 2 cm (PANGAEA.940553), Burke 2023
dataset S01 and the Abbott 2021 supplement. Measure the onset month of the
1453 rise against seasonal markers (Na, Ca). Test whether the Antarctic
5 kg km⁻² is above background in the cores that report it. Moves H4. Gives the
season, which the emulator in 03 needs. Criterion 1.

**03-latitude-posterior (done 2026-10-20).** First calibrate: for every eVolv2k v4 event with
an attributed volcano, how well do asymmetry and the isotope class predict
latitude? Then run the Marshall et al. 2021 emulator (CEMAC; data on CEDA)
over a grid of latitude × season × height. Combine it with Burke's isotope
class to get a posterior on latitude for 1453. Moves H2, H3. Criteria 1, 4.

**04-cooling-fingerprint (done 2026-10-20).** Compute the latitude gradient of summer cooling
in the tree-ring density network (Esper 2017 sites, N-TREND) for each
calibration eruption. Test whether extratropical and tropical eruptions
separate. If they do, classify 1453. Criterion 5. Independent of 03, so
agreement between them means something.

**05-documentary-onset (done 2026-10-20).** Sweep the Joseon Sillok for 1452–1454 (Danjong's
reign; searchable at sillok.history.go.kr), the Ming Shilu, Japanese
chronicles and Euro-Climhist. An LLM extracts dated mentions of a dimmed sun,
red sky, ashfall, untimely frost or snow. Code tabulates the earliest dates.
Also chase the primary sources behind Pang 1993 and Therrell 2004 (Mexican
frost). Bounds the season from outside the ice. Criteria 2, 6. Korean and
Chinese quotations get English beside them.

**06-candidate-ranking (done 2026-10-20; region-level result, named shortlist weak).** For each GVP and LaMEVE row in the window, plus
regional catalogs (TephraKam, AVO, AIST Japan):
1. pull the original 14C lab ages from the primary paper (LLM extracts, with page cite);
2. recalibrate them with IntCal20 in a stdlib script;
3. score P(date covers 1452–53) × P(latitude | 03, 04) × P(size ≥ ~10 Tg S | deposit volume).

Run the scorer blind on the calibration set first, with the leakage rule on.
Report the rank of the true source for each calibration case before ranking
1453. Criteria 2, 3, 4. Gives T2.

**07-glass-reference.** For the top candidates, assemble published glass
major- and trace-element data (GEOROC, EarthChem, TephraKam, AVO). Write a
similarity scorer, tested on 1477 Veiðivötn shards (Abbott 2021 supplement),
so a future 1453 shard is scored in minutes. In parallel, search published NH
peat, lake and Arctic ice records for an unsourced cryptotephra bracketed in
1440–1470. Criterion 7, prepared, not met.

**08-summer-1452 (done, added 2026-10-20).** Was summer 1452 already cold?
No; it excludes little. Window 1452.9–1453.5 if NHET. Frost rings in 1453.

**09-ice-tracers (done, added 2026-10-20).** Lithic, halogen and
volatile-metal tracers in NEEM and TUNU2013. They do not separate Icelandic
eruptions. A TUNU2013 Al pulse at the onset is a post-hoc lead.

Results of each are in `analysis/README.md`; the state is in `NEXT.md`.

## Consequence tests (added 2026-10-20, Greg's direction)

A weak shortlist (06) becomes a strong one when candidates die from their
own evidence. For each named candidate, assume it is the source and write
down what must then be true, before looking. Then run the tests one at a
time, cheapest and most decisive first. Each test can kill the candidate.
None can identify it; only glass does that (criterion 7).

Standard list for candidate X:
1. **Own date.** X's deposits date to ~1452/53 from brackets in lake, peat
   and archaeological sections, modelled as a Bayesian sequence. No polar ice.
2. **Near-field signal.** Tree rings or other proxies close to X show a
   local 1453 shock beyond the hemispheric cooling. Calibrate on a known
   eruption in the same region.
3. **Isotope match.** If X has another eruption with measured Δ33S in
   Greenland, its pattern should resemble 1453's.
4. **Sulfur budget.** Petrologic S yield of X's magma can reach ~10 Tg S.
5. **Distal glass.** X's glass appears in an NH distal record bracketed
   1440–1470.
6. **Ash timing.** X's region predicts particle arrival relative to sulfate
   (Plunkett 2023), testable on the sub-annual TUNU2013 particle record.

Order of candidates: Aniakchak Half Cone (H10; 11-aniakchak-date is test 1),
then Karymsky and Katla, then the rest of 06's top rows.

## The wall

Criterion 7 needs 1453 glass. Two routes past it:

1. **Ice.** TUNU2013 archive ice at DRI (McConnell, Sigl) and Queen's
   University Belfast (Plunkett, Abbott). The question for them is whether
   the 1452.5–1453.5 interval has been sampled for shards. Contacting them is
   an external action and Greg's decision. A T2 shortlist makes the request
   much stronger: it says which glass to compare against.
2. **Distal deposit.** A cryptotephra in a well-dated NH peat or lake record
   (07's second half). Open literature, no permission needed. Probability low.

## Order and cost

02, 03 and 04 are cheap and independent, so they can run in parallel, one
agent per experiment. 05 is mostly reading. 06 is the large one: it needs
per-candidate primary papers. 07 waits on 06's shortlist.
