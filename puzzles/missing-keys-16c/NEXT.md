# Next session — missing keys, 1500–1620

**Last session:** 2026-11-19. Two jobs: stage 1 of the cross-section (`line/PROMPT-cross-section.md`), then
Greg's "finish the outstanding items". `/session-close` was run. Commits are local, not pushed.

## Where it stopped
- **Cross-section: no five.** 28 candidates gated; none passes all four gates (`line/cross-section.md`). The
  outside repository works 6 of the 10 seeds; access walls hold most of the rest. Greg has not chosen; stage 2
  of that prompt is not started.
- **No. 1336: key stays at 28 values.** Seventh stage failed as registered (178 of 200, bar 190). Guide revision
  2 (`SIGN-GUIDE-r2.md`) and two fresh readers on c. 652r lines 6–7 weakened the old reading: the n in
  `barlamento`, `pontific` and two other words came from `qx`, and the new readers see `qxl` (long bar), which
  has no value. `READING.md` section 4 says so. Outside check: `outside-check.md` (consistent; case not found).
- **No. 2351: `key-v1.tsv`** adds `bbar` = i and `zm` = non (probable). Letter B reads at 1,396 of 1,922 columns,
  above 200 of 200 shuffles. Letter B is not in Desjardins vol. 2. Record: `items/2351/README.md`, `READING.md`.

## STARTED 2026-11-19 (Greg accepted the 11 px exception). State in `items/2946/`:
- Done and committed: `gate.md` (go), fetch, strips (bands with a y ruler; per-line cutting failed, `lines.py`),
  `PLAIN-GUIDE.md`, `SIGN-GUIDE.md` (frozen), briefs as sent in `briefs/`.
- Plain readers PA–PD (all five pages): line counts agree (691: 51, 692: 49, 693: 46, 694: 17, c215: 19);
  clear 0.63–0.88, gloss 0.47–0.64 (`results/plain-agree.tsv`). Gloss is 5–6 px: build from words both read alike.
- c. 215 (the target): four cipher readers CA–CD, agreement 0.96–0.97, merge 458 kept / 2 unread
  (`results/c215-merged.txt`, `rename-c215.tsv`). Done.
- Page 691: readers KA–KC (L01–L26) and KD–KF (L27–L51) were running when the session hit its limit; KB done.
  Check which `readers/K*/` have `691a.txt` / `691b.txt`; a reader with only `pass1.txt` is usable as one pass.
- Next: guide revision 1 from readers' notes (Z-shaped L with a top bar: n-zl/n-z/n-zed; c with a bar, rc+c joins;
  dots under `tp`; loop-on-stem variants qbar/qbase; `#19 rc bc` groups that may be figures), committed before
  readers on 692–694 (3 per half-page), then merge, METHOD 0b (hold the four 1428–30 Mantua keys in
  `sources/raw-outside/`), 0c design counts, **stop for Greg before the build**.

## First action (original plan): no. 2946 + 2947 (H10)
Gianfrancesco Gonzaga to Cosimo de' Medici, 1439. ASF MAP XI: 2947 = images 691–694, glossed between the
lines (about 4,000 signs, the pair); 2946 = c. 215, bare (about 400 signs, the target). Images at the server's
maximum (1272 px) measure 11 px, the no. 1336 level. Scout notes: `line/cross-section/scout-A.md`; images in
`sources/cache/cross/2946/`, `2947/`. It is also H6's clean test: a pair neither builder was shaped on.
Order: `items/2946/gate.md` and design counts (METHOD 0–0c, including the Gonzaga/Mantua keys of the 1430s
in the outside profiles: `cattanei1430`, `malatesta1428`, `mutiliana1428` name Gianfrancesco); strips; guide;
clear-word readers first; four or more cipher readers; build; registered test; reading. Key work on Fable.

## Second
1. **No. 2351, next registered stage** for the leads from Dudout's shapes: unmarked `2` = t, marked `2` = b,
   `flong` = et, `L4` = ll (`items/2351/results/dudout-shapes.md`). They need held-out text in letter A's pair,
   because letter B has been scored.
2. **No. 1336, `qxl`:** is it `qx` drawn long? Only unscored text can test it. None is online at a usable size.

## Walls named this session
- **No. 1336, text:** all held-out cipher is spent; the other Ambrosiana groups (`more-letters.md`) are name codes
  of about 10 signs at 750 px (about 8 px). Breach: the Ambrosiana's own images, or more letters in the 1573–76
  volumes beyond the scout's 146 images.
- **No. 1336, the case:** Sala, *Documenti* III, pp. 448–536 (Borromeo to Speciano, 1573), no scan found.
- **DECODE images need a login, and Greg's does not work.** Do not plan on it or ask again. Blocked: Sforza
  family G (R5436 "da cifra"), AAV Spagna 22 (R5624), Sforza 1446.
- **2854 (Ferdinand to John II, 1478):** Tomokiyo 2018 returns 403. **1270 (Juan Manuel):** BNE refuses scripts.
- **No. 2911:** a library copy of Bertelli 1964 or the Edizione Nazionale vol. VI (unchanged).

## Open on method
- H6: clean test still owed; 2946/2947 is the candidate pair.
- H7: an answer-free stage 4 bar.
- `line/sign_height.py` over-reads joined runs (2554); rule by eye on a native crop when components look few.
- Guide revisions change what readers write (`qx` → `qxl`): a revision can weaken a passed reading. Revise the
  guide before the registered test, not after.

## Housekeeping
- Untracked on purpose: bench run keys and logs, `items/*/work/`, readers' crops, outside raw files
  (`items/2351/sources/raw-bourdeau*`). Stale crops in `items/1336/readers/{J,K,L,M}/crops/` are safe to remove.
