# Locator adjudication — 2026-09-26

The first comparison is already exposed and remains unchanged. It pairs
different grids where readers traversed page columns differently. This is a
post hoc collation repair, not a new frozen prediction experiment.

1. A fresh Sol agent sees only the same three source images and acquisition
   manifest. It reads chapter headings and item numbers, and records column
   and within-column positions. It sees no previous transcription or model.
2. The main thread creates an explicit mapping from each of the two original
   reader keys to those physical source locators. Match by printed number,
   source region and heading continuity. Record every changed identifier.
   Do not match on grid letters, hidden truth, model performance or Mathers.
3. Require a one-to-one, exhaustive mapping of the original 22 items in each
   reader. Ambiguity excludes a join; never search letter similarity for it.
   Commit the locator audit and map before producing corrected model scores.
4. Keep every raw letter unchanged. Apply the same shape, J/I, uncertainty,
   source-ID and Mathers visible-agreement rules used in `score.py`. Publish
   separate post hoc outputs, including coverage and all rejected joins.
5. Add physical locators to both raw readings in the corrected collation, so
   even shape conflicts can be inspected. Agreed letters are a transcription
   consensus, not an adjudicated edition. Per-cell records must preserve both
   reader values and uncertainty.

The main thread has seen raw readings and prediction files; the locator
reader has not. Even if enough interior cells become available, the repaired
cohort will not be presented as a confirmatory A/B verdict. It is a usable
source packet and a diagnostic for the next, still-unseen manuscript packet.
