# 05 — Documentary onset

**Question.** What do dated documents of 1452–1454 say about unusual sky or
weather? Can they bound when the aerosol arrived, and, weakly, where?
Criteria 2 and 6.

**Sources reached.**
- Joseon Wangjo Sillok, the Korean court annals: full-text search of the classical Chinese at sillok.history.go.kr, all reigns.
- Ming Shilu, the Ming court annals, up to 1627, on the same site.
- Mingshi treatises (Wuxing and Tianwen), via Wikisource.
- Therrell et al. 2004 (Mexico).
- Oliński 2016 (Polish and Silesian chronicles).

**Walls.**
- Euro-Climhist needs a registered account.
- Japanese Kyōtoku 1–3 chronicles: no open searchable source found. Fujiki 2007, 日本中世災害史年表稿 ("Draft chronology of disasters in medieval Japan"), is a book only.

All provenance is in `PROVENANCE.md` and `data/manifest.tsv`.

## Method
1. `fetch.py` saves raw pages to `data/raw/`, gzip-compressed, with a sha256 per file. It fetches:
   - every search-result page for 29 Sillok terms and 16 Ming terms;
   - the month lists of every reign;
   - per-month article lists for these lunar years: 1440–1465, 1595–1606, 1636–1646, 1779–1788 and 1810–1820.

   Sillok terms: 日色 日無光 日赤 無光 赤氣 日光 白虹 霾 雨土 黃霧 昏霧 霧 隕霜 降霜 霜 雨雪 大雪 雪 雨雹 雹 凍 雨灰 夏雪 晦冥 陰霾 霧塞 日色赤 日色如血 日暈.
   English: sun colour; sun without light; red sun; lightless; red vapour; sunlight; white rainbow; dust haze; dust rain; yellow fog; dark fog; fog; frost falls; frost descends; frost; snow falls; heavy snow; snow; hail falls; hail; freeze; ash rain; summer snow; darkness; gloomy haze; fog-choked; sun red; sun red as blood; sun halo.
2. `parse.py` dates every hit. It converts the lunar date to a Julian date in four steps:
   - It computes new moons and the winter solstice astronomically (Meeus) at UTC+8.
   - Month 11 contains the solstice.
   - It takes leap months from the Sillok month lists.
   - It fixes the exact day with the sexagenary day name the record gives.

   On the 16,349 Sillok rows that carry a day name, the estimate matches it exactly 98.0% of the time and is within ±1 day 99.7% of the time (`results/calendar_check.txt`). Independent check: the Mingshi puts the start of the 1453/54 snow on 十一月戊辰 ("the wuchen day of the 11th month"). The Shilu memorial says 十一月十六日 ("the 16th day of the 11th month"). The script makes 戊辰 the 16th, 15 Dec 1453 (Julian).
3. `tabulate.py` counts Sillok "notices", in three steps:
   - A notice is an article whose Korean translators' title AND whose original text both match a category pattern. The categories are snow, frost, hail, dust, fog, sun dim/red, red vapour, cold, halo and white rainbow.
   - It divides the count by the year's total article count.
   - It tests each target year against baseline years with a Poisson test and a z-score.

   It runs the same counts on four calibration eruptions. For the Ming Shilu it counts cold/snow reports per year by keyword, minus metaphors (雪冤 "clear an injustice", 饑寒 "hunger and cold" as a stock phrase for poverty, …). These are raw counts.
4. `mingshi.py` lists the dated clauses in the Mingshi sections 恆寒 (persistent cold), 恆陰 (persistent overcast), 雨雪隕霜 (snow and frost), 日变月变 (changes of sun and moon), 晕适 (halos), 云气 (cloud vapours) and 天变 (sky changes).
5. I (the LLM) read the hits for 1452–1455 and wrote `entries.csv`. It has 23 entries, each with citation, original date, Julian date, original text, an English translation, a reading and a confidence that the entry is aerosol-related. That confidence is my judgement. The counts are not.

**Run.**
```
python3 -I fetch.py data months kaa kba kca kda kea kfa kga kha kia kja kka kla kma kna knb koa kob kpa kqa kra krb ksa ksb kta ktb kua kva kwa kxa kya kza kzb
python3 -I fetch.py data search w 日色 日無光 日赤 無光 赤氣 日光 白虹 霾 雨土 黃霧 昏霧 霧 隕霜 降霜 霜 雨雪 大雪 雪 雨雹 雹 凍 雨灰 夏雪 晦冥 陰霾 霧塞 日色赤 日色如血 日暈
python3 -I fetch.py data search m 雪 霜 凍 寒 冰 雹 霾 日色 無光 赤氣 晦冥 黃霧 雨土 隕霜 日赤 霧
python3 -I fetch.py data days kda 22 32   # then: kea 0 2, kfa 0 3, kga 1 11, kna 28 39, kpa 14 24, kva 3 12, kwa 10 20
python3 -I parse.py data out
python3 -I tabulate.py out > results/tabulate.txt
python3 -I mingshi.py data/raw/papers/mingshi_28.wiki data/raw/papers/mingshi_27.wiki > results/mingshi.txt
```
`fetch.py` reads its cache first, so a rerun is offline. `out/` is gitignored.
`data/raw/` is 45 MB and should not be committed. Keep `data/manifest.tsv`.

## Result

**Earliest dated anomalies, by region (Julian dates).**
- **China, spring 1453.**
  - 9 Mar 1453, a memorial: 邇者新春風雨連月寒沍倍冬 ("lately, in the new spring, wind and rain for a month, frost-cold twice that of winter").
  - Fengyang (33° N) reported 二月三月雨雪不止麥苗浥爛 ("in the 2nd and 3rd months snow fell without stopping; the wheat seedlings rotted"). That is about 10 Mar–8 May 1453.
  - Spring 1452 has similar reports. On 9 Mar 1453 a memorial recalls 去年正月大雪異常 ("last year in the first month, extraordinary heavy snow"), and Taihe reported 今春雨雪連綿二麥無收 ("this spring continuous rain and snow; no wheat harvest"). So spring cold alone does not mark onset.
- **Korea, summer 1453.**
  - 2 Aug 1453: 雨雪于咸吉道咸興府 ("rain and snow fell at Hamheung", 39.9° N).
  - 17 Aug 1453: 甲山郡隕霜三日, 寒氣如十月 ("at Gapsan frost fell three days; the cold was like the tenth month").
  - 21 Nov 1453: Gangwon crops failed 因雨水、早霜 ("because of rain and early frost").
- **China, winter 1453/54.** From 15 Dec 1453: 大雪…淮河東海冰結四十餘里人民頭畜凍死不下萬計 ("heavy snow … the Huai and the eastern sea froze over 40 li; people and livestock frozen to death, no fewer than ten thousand"). Cold deaths were reported as far south as Hengzhou (27° N), Suzhou, Hangzhou and Fujian. Shandong ice had not melted by April 1454.
- **Europe.** Silesian sources: the first phase of winter 1453/54 was "exceptionally frosty, 23 Nov – 15 Dec" (Oliński 2016, secondhand). Winter 1454/55 was severe (Długosz).
- **Mexico.** The famine of 1454 followed a drought that had begun by 1450–52. The "1453 autumn frost" is one reading of a pictograph (Therrell 2004).

**No dimmed, red or hazy sun is recorded anywhere in 1452–1454.** Searched: Sillok, Ming Shilu and Mingshi; Oliński says the Polish sources are silent on it too. The one Ming hit, 日或昏蝕 ("the sun is at times dim or eclipsed", Nov 1454), sits in a rhetorical list of portents.

**Baseline comparison, computed (`results/tabulate.txt`).**
- **Ming Shilu, cold/snow reports.** Lunar years 1453–54 give 22 reports against 3.5 expected from 1436–51 and 1455–64 (Poisson p = 4 × 10⁻¹¹). 19 of the 22 are in lunar 1454, which is winter 1453/54. Lunar 1453 alone has 3, below 1452's 5.
- **Sillok.** Counts are small. 1453–54 snow: 3 notices against 0.5 expected (p = 0.012). Frost, fog and cold are not significant. Sun-dimming notices are 0 in every year 1440–1465.
- **Halos.** Halo notices jump in 1454 (35 vs 12.3 expected). Halo counts also run high in 1456–57 and 1462 with no eruption, so I read this as recording effort, not aerosol.

**Calibration: does the Sillok see known eruptions?** Sometimes.
- **Komagatake (GVP 31 Jul 1640) and Parker/Melebingoy (GVP 26 Dec 1640).** Strong signal in 1641: 10 frost notices against 1.6 expected (p = 8 × 10⁻⁶). They include June–July 1641 frosts in four provinces. Fog notices: 7 against 0.2 expected.
- **Huaynaputina (GVP 17 Feb 1600).** Nothing in 1600 or 1601, in either the Sillok or the Ming Shilu.
- **Kuwae (1458).** No Sillok signal in 1459.
- **Laki (1783) and Tambora (1815).** Untestable. The late Sillok records no weather notices at all.

The Sillok has no dimmed-sun record in any of these windows. The Mingshi does record 日无光，旋赤如赭 ("the sun had no light, then turned red like ochre") on 25 Mar 1458. It records red or lightless suns again in 1459 and 1462–64, after Kuwae, and none in 1452–55.

**What this bounds.**
- Documents put cold effects in East Asia by early August 1453 and an extreme cold outbreak from mid-December 1453. Both fit the tree-ring cold summer of 1453.
- The spring-1453 cold reports cannot be told from spring 1452, so they do not move the onset earlier.
- No document fixes an eruption date or a visible veil. Criterion 2 is not met by documents.
- Criterion 6 gains a fact: the record is silent on the sky, not just on the eruption.

**Limits.**
- Sillok sensitivity is about one in three on the calibrations that can be tested.
- Sillok notice counts in the 1450s are single digits.
- The Sillok's sky-colour reporting is near zero after about 1410.
- Ming counts are not normalised for article totals.
- Regex categories miss weather buried in long memorials.
- Japanese and Euro-Climhist sources were not searched.
- Pang's Constantinople claims (fog on 26 May 1453, "flames" on Hagia Sophia) were not chased to Barbaro or Sphrantzes. They stay unverified.
