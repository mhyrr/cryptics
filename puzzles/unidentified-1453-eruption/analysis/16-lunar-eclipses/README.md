# 16 — Lunar eclipses 1450–1458

**Question.** Do descriptions of total lunar eclipses in 1450–1457 constrain
when stratospheric aerosol from UE 1453 arrived and how long it stayed?

## Pre-registration (written 2026-10-21, after the eclipse list was computed, before any description was read)

The eclipse list comes from `eclipses.py`. Each eclipse below is assigned the
expected Danjon class (L) under the working window (Greenland sulfate onset
1453.0–1453.1; eruption 1452.9–1453.5 if NH extratropical, from 08).

| Eclipse (Julian) | Visible in | Months after 1453.0 | Prediction if UE 1453 was stratospheric and large |
|---|---|---|---|
| 1450 Jan 28 T | Europe | −35 | normal (L 2–4) |
| 1450 Jul 24 T | Europe (rising), East Asia (setting) | −29 | normal |
| 1451 Jan 17 T | East Asia (rising) | −23 | normal |
| 1451 Jul 14 P (0.66) | Europe | −18 | normal |
| 1453 May 22 P (0.74) | East Asia; Constantinople at moonrise | +5 | weakly dark if the aerosol was already in place; a partial eclipse is a poor test |
| 1453 Nov 16 T | East Asia, high in the evening | +10.5 | **dark (L 0–1)**. This is the decisive eclipse |
| 1454 May 12 T | Americas only | +16 | no Old World record expected |
| 1454 Nov 5 T | East Asia | +22 | L 1–2 if the veil persisted (Pinatubo-like); normal if it decayed with a NHET e-folding of under ~1 yr |
| 1457 Mar 11 T, 1457 Sep 3 T | East Asia; Europe | +50, +56 | normal (before the 1458 sulfate) |
| 1458 Feb 28 T, 1458 Aug 24 T | East Asia | +62, +68 | calibration: dark expected for Aug 1458 if Kuwae/UE 1458 was erupting by early 1458 |

**Scoring rule.**
- A described-as-normal (red/coppery, visible) total eclipse on 16 Nov 1453
  weakens a large stratospheric veil at NH latitudes 10 months after onset.
  It does not refute one, because a single description is weak.
- A dark or "invisible" moon on 16 Nov 1453, with normal descriptions
  before 1452, supports a veil in place by late 1453.
- Silence (no description) is uninformative. Most records say only that an
  eclipse happened.
- Nothing here can date the eruption more finely than the eclipse spacing
  (~6 months).

## Method precedent (read 2026-10-21)

Guillet, S. et al. 2023, "Lunar eclipses illuminate timing and climate impact
of medieval volcanism", *Nature* 616: 90–95, doi:10.1038/s41586-023-05751-z
(`SCHOLARLY`; open text at https://pmc.ncbi.nlm.nih.gov/articles/PMC10076221/).
What matters here:
- Period 1100–1300 CE. Nothing after 1300; the 1450s are not covered. No
  later extension was found (searches 2026-10-21).
- Danjon L is assigned only from explicit wording. L0 needs the Moon
  "invisible or extremely dark". L1 is dark, grey or brownish; L2 deep red;
  L3 brick red (Latin *rubeus*, *sanguineus*). Partial eclipses are excluded.
- Almost all colour descriptions are European. East Asian sources "rarely
  describe colour": one East Asian eclipse (2 Dec 1229) was usable.
- Dark eclipses are expected 3–20 months after a large eruption, when SAOD
  is ≥ ~0.1. Tambora's June 1816 eclipse is their L0 test case.

## Method

1. `eclipses.py` parses the NASA catalog (Espenak & Meeus, *Five Millennium
   Catalog of Lunar Eclipses*, https://eclipse.gsfc.nasa.gov/LEcat5/LE1401-1500.html,
   `PRIMARY` for computed geometry; sha256 52f21977…). It lists every umbral
   eclipse 1440–1465. For 12 sites it gives the Moon's altitude at U1, at
   greatest eclipse and at U4. Catalog dates before 1582 are Julian.
2. `court_records.py` searches the Joseon Sillok and the Ming Shilu for
   月食 / 月蝕 ("lunar eclipse") through 05's `fetch.py`. It dates each hit
   with 05's calendar code and matches it to the catalog. It also scans
   every eclipse notice in every year for words of colour, brightness or
   visibility (`results/colour_terms.txt`).
3. `calibration.py` is the known-case test of the court channel. It asks
   how the same annals record total and deep-partial eclipses 3–24 months
   after Huaynaputina 1600, Parker 1640, Tambora 1815, Krakatau 1883 and
   UE 1458. Eruption months: Guillet 2023 for Tambora (April 1815); 05's
   README for Huaynaputina and Parker; Krakatau August 1883 is from memory
   and unverified, but the result does not depend on it.
4. `constantinople.py` computes the 22 May 1453 eclipse as seen from
   Constantinople, to compare with Barbaro.
5. The LLM read Barbaro's diary (Cornet 1856 edition, archive.org OCR,
   sha256 0655d071…) and the court entries. Its Danjon readings are below.

**Run** (from this folder; downloads go to `data/`, which is gitignored):
```
python3 -I -c "import urllib.request as u; [open('data/LE%s.html'%s,'wb').write(u.urlopen(u.Request('https://eclipse.gsfc.nasa.gov/LEcat5/LE%s.html'%s,headers={'User-Agent':'Mozilla/5.0'})).read()) for s in ('1401-1500','1601-1700','1801-1900')]"
python3 -I eclipses.py data/LE1401-1500.html > results/eclipses.tsv
python3 -I ../05-documentary-onset/fetch.py data/sillok search w 月食 月蝕
python3 -I ../05-documentary-onset/fetch.py data/sillok search m 月食 月蝕
python3 -I court_records.py data/sillok ../05-documentary-onset/data results/eclipses.tsv > results/court_records.tsv
python3 -I court_records.py data/sillok ../05-documentary-onset/data results/eclipses.tsv colour > results/colour_terms.txt
python3 -I calibration.py data > results/calibration.txt
python3 -I constantinople.py data/LE1401-1500.html > results/constantinople_1453.txt
```
- `court_records.py` needs 05's cached Sillok month lists in
  `../05-documentary-onset/data/raw/months/`.
- Barbaro: `Barbaro, Nicoló _ 1856 _ Giornale dell' assedio di Costantinopoli 1453_djvu.txt`
  from https://archive.org/details/giornale-dell-assedio-di-costantinopoli-1453-1856.
- Fetch provenance: `results/sillok_manifest.tsv`.
- Each court entry is at `https://sillok.history.go.kr/id/<id>`, with the id in
  `results/court_records.tsv` (e.g. `wfa_10110016_001` for the Sillok entry of
  16 Nov 1453).

## Eclipse list, 1450–1458 (computed, `results/eclipses.tsv`)

Times are UT at greatest eclipse. Altitudes are the Moon's, in degrees, at
U1/greatest/U4.

| Date (Julian) | Type, umbral mag | Totality | UT | Europe (Venice) | Constantinople | East Asia (Beijing / Seoul / Kyoto) |
|---|---|---|---|---|---|---|
| 1450 Jan 28 | T 1.215 | 69 min | 00:41 | 60/57/43 | 64/51/32 | setting at dawn, Beijing 5/−13/−27 |
| 1450 Jul 24 | T 1.574 | 98 min | 18:56 | rising −14/4/18 | −1/16/28 | setting 31/21/5 |
| 1451 Jan 17 | T 1.169 | 60 min | 10:15 | below horizon | below horizon | rising −8/10/28 |
| 1451 Jul 14 | P 0.661 | — | 00:03 | 24/24/18 | 29/23/13 | below horizon |
| 1453 May 22 | P 0.745 | — | 17:16 | below horizon | rises at maximum, −17/−2/11 | 27/25/18 |
| **1453 Nov 16** | **T 1.153** | 60 min | 12:25 | below horizon | below horizon | **21/40/59, 28/49/67, 35/56/74 (evening)** |
| 1454 May 12 | T 1.572 | 94 min | 06:51 | below horizon (Americas only) | below horizon | below horizon |
| 1454 Nov 5 | T 1.202 | 70 min | 13:32 | below horizon | ends at moonrise, −25/−11/6 | 32/52/67, 40/60/70, 48/67/71 |
| 1455 May 1 | P 0.252 | — | 23:47 | 28/27/24 | 31/27/21 | below horizon |
| 1457 Mar 11 | T 1.282 | 79 min | 10:54 | below horizon | below horizon | rising |
| 1457 Sep 3 | T 1.253 | 70 min | 22:04 | 29/39/40 | 40/45/40 | setting |
| 1458 Feb 28 | T 1.036 | 31 min | 11:01 | below horizon | below horizon | rising |
| 1458 Aug 24 | T 1.191 | 62 min | 14:40 | below horizon | below horizon | 25/37/42, 33/43/43, 39/47/43 |

The geometric result:
- **No total lunar eclipse was visible from Europe or the Mediterranean
  between 24 Jul 1450 and 3 Sep 1457.** Europe is the region that supplies
  nearly all of Guillet's colour descriptions.
- Both eclipses in UE 1453's dark window (16 Nov 1453 at +10.5 months, and
  5 Nov 1454 at +22 months) were visible only in East Asia and the Pacific.
- The 22 May 1453 eclipse was partial (0.745), and at Constantinople it rose
  near maximum.

## Descriptions found

| Eclipse | Source (tier) | Text | English | Danjon estimate and reasoning |
|---|---|---|---|---|
| 1450 Jan 28 | Ming Shilu, Jingtai 1/1/15 (`PRIMARY`) | 是日早月食當在卯正三刻欽天監官以為辰初初刻致失救護 | "This day at dawn the moon was eclipsed, properly at the third quarter of mao; the Directorate of Astronomy said the first quarter of chen, so the rescue rite was missed" | None. Timing dispute only; it shows the eclipse was observed. |
| 1450 Jul 24 | Sillok, Munjong accession yr 6/16; Ming Shilu (`PRIMARY`) | 月食旣 / 夜月食 | "the moon was eclipsed, totally" / "at night the moon was eclipsed" | None |
| 1451 Jan 17 | Sillok, Munjong accession yr 12/15; Ming Shilu (`PRIMARY`) | 月食旣 / 夜月食 | as above | None |
| 1453 May 22 | Barbaro, *Giornale*, ed. Cornet 1856, p. 49 (`PRIMARY`, eyewitness diary) | "a un hora de notte levò la luna et havea hozi el suo tondo … questa luna si levò come quela avesse abudo tre zorni, la qual puoco parea, e iera l'aiere sereno come uno cristalo neto e mundo; questa luna si durò a questo muodo zerca hore quatro, e poi a puoco a puoco quela si se andé fazando el suo tondo, e a ore sie de note, tuta si fo compida" | "at one hour of night the moon rose, and today it was full … this moon rose as if it were three days old, and showed little, and the air was clear as a clean, pure crystal; the moon stayed this way about four hours, then little by little it made its round, and at six hours of night it was fully complete" | **Not assignable.** It is a partial eclipse, which Guillet excludes. A 0.74 eclipse rising near maximum, in twilight, looks like a crescent at any Danjon value; "showed little" is normal for the eclipsed part against a twilight sky. "Clear air" rules out local fog that evening. The four-hour duration is physically wrong: the umbral phase ends 1.3 h after moonrise and the penumbral 2.4 h after (`results/constantinople_1453.txt`). Aerosol cannot lengthen the penumbral phase, so this is narrative inflation, not a measurement. |
| 1453 May 22 | Barbaro p. 40, entry for 12 May (`PRIMARY`) | "mai Costantinopoli non se perderia … per in fina che la luna non levasse scura, siando el suo tondo, zoè che la se vedesse, salvo la mitade de quela" | "Constantinople would never be lost … until the moon rose dark while full, that is, so that only half of it could be seen" | This is the prophecy, not an observation. The "dark" in Pang's "rose in dark eclipse" (JPL release, 6 Dec 1993, `CLAIMANT`/`POPULAR`, https://www.jpl.nasa.gov/news/jpl-confirms-15th-century-volcanic-eruption/; repeated on Wikipedia) comes from this wording. The eyewitness says crescent. |
| 1453 May 22 | Ming Shilu, Jingtai 4/4/13 (`PRIMARY`) | 月食 (variant edition 廣本: 日食) | "lunar eclipse" (variant reading: "solar eclipse") | None. The date is one day off the catalog, and one edition reads "solar eclipse". |
| **1453 Nov 16** | Sillok, Danjong 1/10/16 (`PRIMARY`) | 己亥/月食旣 | "jihai day: the moon was eclipsed, totally" | **None.** 旣 ("total") is also written for partial eclipses after known eruptions (1601 Dec 9, mag 0.91; 1641 Apr 25, mag 0.80; `results/calibration.txt`), so it may come from prediction. |
| **1453 Nov 16** | Ming Shilu, Jingtai 4/10/16 (`PRIMARY`) | 夜月蝕犯六諸王西第一星 | "at night the moon was eclipsed and encroached on the westernmost star of the Six Princes" | **None.** The conjunction suggests the eclipsed Moon was watched, but there is no word on brightness or colour. |
| 1454 Nov 5 | Ming Shilu, Jingtai 5/10/15 (`PRIMARY`) | 夜月食 | "at night the moon was eclipsed" | None. No Sillok entry. |
| 1457 Sep 3 | Ming Shilu (`PRIMARY`) | 夜月食 | as above | None. Peuerbach and Regiomontanus timed this eclipse in Austria (MacTutor, `SECONDARY`, https://mathshistory.st-andrews.ac.uk/Biographies/Peurbach/); no colour found. |
| 1458 Feb 28, Aug 24 | Ming Shilu (`PRIMARY`) | 昏刻月食於翼宿遂犯右執法星 / 辛丑夜月食於室宿 | "at dusk the moon was eclipsed in the Wings lodge, then encroached on the Right Executor of Law star" / "xinchou night, the moon was eclipsed in the House lodge" | None |

Court-annal colour channel, all years (`results/colour_terms.txt`):
- 259 short Sillok and 206 short Ming eclipse notices span 1393–1900.
- One describes the Moon's colour: Ming 1587, 其體赤黃色 ("its body was
  red-yellow").
- Thirteen record "not seen" (不見): 6 Sillok, 7 Ming. Most give cloud or rain as the reason.
  Ming 1569 and 1579 give no reason.
- No notice uses a word for dark (黑, 暗, 無光).

## Calibration (known cases)

The court channel fails its known-case test (`results/calibration.txt`):
- Tambora: the Sillok records the 16 Dec 1815 total eclipse (8 months
  after) with the same bare 月食旣 as any other eclipse, plus computed
  magnitudes. It has no entry at all for Guillet's L0 eclipse of 10 Jun
  1816.
- Huaynaputina: the 9 Dec 1601 eclipse (22 months after) is the same bare
  formula in both annals.
- Krakatau: no entry for 1884.

An L0 eclipse is therefore indistinguishable from a normal one in these
annals. A European-chronicle calibration (Guillet's channel) is not needed
here, because no European total eclipse falls in the window.

## Result against the pre-registration

**The test could not be run.** Not one eclipse in 1450–1458 has a
description that carries Danjon information. Under the scoring rule,
silence is uninformative. UE 1453's arrival and persistence are not
constrained by lunar eclipses.

The wall is the combination of three things:
1. Geometry (computed). Europe and the Mediterranean, where almost all
   medieval colour descriptions come from, saw no total eclipse from
   Jul 1450 to Sep 1457.
2. Genre (computed, calibrated). Korean and Chinese court annals record
   eclipses with a fixed formula that is blind to darkness, even after
   Tambora.
3. Sources. Barbaro's 22 May 1453 account is real and matches the computed
   partial eclipse at moonrise. But it is a partial eclipse, and his
   duration is not physical. The popular "dark eclipse" is the prophecy's
   wording, not his observation.

**What would breach it.** Japanese diaries for the full moon of the 10th
month of Kyōtoku 2 (16 Nov 1453) and Kyōtoku 3 (5 Nov 1454). Guillet's
one usable East Asian case came from a Japanese courtier diary
(*Meigetsuki*).
- Candidates: *Yasutomi-ki* 康富記 (a volume covering Kyōtoku 2/8 – 3/12 is
  at the University of Tokyo digital archive, as manuscript images only,
  https://da.dl.itc.u-tokyo.ac.jp/portal/en/assets/5a34e884-2529-2c44-608a-e4f17f9d6225,
  `PRIMARY`, unread); *Morosato-ki* 師郷記; *Daijōin jisha zōjiki* 大乗院寺社雑事記
  (begins 1450).
- Kanda Shigeru's *Nihon tenmon shiryō* (1935) compiles Japanese eclipse
  records to 1600; via Hasegawa 1995,
  https://otemae.repo.nii.ac.jp/record/1937/files/1995_jc_h290-297_hasegawa.pdf,
  `SCHOLARLY`. It is a book and was not reached.
- A dark reading on 16 Nov 1453 in Kyoto would be the first positive
  datum. A "red" one would weaken a large NH veil at +10 months.

## Caveats
- The descriptions are sparse and literary. The siege accounts are framed
  by prophecy; "blood moon" and darkness are topoi.
- A Danjon value from one observer at one site is weather-dependent.
- The 1453 May 22 Ming date is one day off the catalog, and one edition
  reads "solar eclipse".
- `results/court_records.tsv` still contains non-eclipse hits for 月食
  ("monthly rice ration"). Matching to the catalog separates them.
- Visibility ignores refraction and parallax (< 1°).

## Unverified claims
- Krakatau's eruption month (August 1883) is from memory. Only the
  calibration list depends on it, and the result does not.
- The identity of the 六諸王 asterism and the Moon's position in it were
  not checked.
- Other siege witnesses (Sphrantzes, Kritoboulos, Leonard of Chios) on
  22 May 1453 were not read. Pang's fog of 26 May and "flames" on Hagia
  Sophia were not chased here, as 05 also noted.
- Whether Peuerbach recorded the colour of the 3 Sep 1457 eclipse is
  unknown; only his timing is reported (Schöner 1544, via MacTutor).
