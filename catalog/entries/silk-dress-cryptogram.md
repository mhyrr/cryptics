+++
title = "Silk dress cryptogram (solved 2023) — calibration case"
slug = "silk-dress-cryptogram"
kind = "cipher"
era = "27 May 1888 (observations); found 2013"
origin = "United States (US Army Signal Service weather network); dress found in Maine"
language = "English telegraphic code (Signal Service weather code)"
status = "solved"
confidence = "high"
digitized = "https://www.noaa.gov/heritage/stories/cryptogram-in-silk-dress-tells-weather-story"
tags = ["calibration", "solved", "codebook", "telegraph-code", "weather", "Victorian", "document-search"]

[scores]
mystery = 1
material = 4
solvable = 5
compute = 3
verifiable = 5
crowding = 3
+++

# Silk dress cryptogram (solved 2023) — calibration case

## What it is
Two sheets of crumpled paper, 23 handwritten lines of apparently random English words ("Bismark, omit, leafage, buck, bank"; "Calgary, Cuba, unguard, confute, duck, fagan"). Sara Rivers-Cofield, an archaeologist and dress collector, found them in December 2013 in a hidden pocket under the bustle of a Victorian silk dress she bought at an antique mall in Maine. It spent a decade on "top unsolved" lists (Schmeh's top 50, #32). Wayne Chan (University of Manitoba) solved it. It is a US Army Signal Service telegraphic weather code: each word stands for a station and its observations (temperature, pressure, dew point, wind, precipitation, cloud). The decoded observations belong to a single time, 27 May 1888 at 10 p.m.

## What is unsolved
Nothing in the text. What remains is historical: who owned the dress (a "Bennett" label is not firmly linked), why weather reports were in a dress pocket, and whether the wearer was a Signal Service employee or volunteer observer.

## What survives
The two sheets and the dress, in Rivers-Cofield's possession; photographs published widely. The key: Signal Service and Weather Bureau telegraphic codes, including the 1892 Weather Bureau code supplied by NOAA's Central Library. And the control that verified the solution: the Signal Service daily weather maps for 27 May 1888.

## Prior attempts and current consensus
Nine years of amateur attempts treated it as cryptanalysis and got nowhere. Chan approached it as document identification, working through about 170 telegraphic codebooks. He found a reference to Army weather codes in *Telegraphic Tales and Telegraphic History*, obtained the Weather Bureau code from NOAA, and decoded the sheets. The decoded values match the published weather maps for that night. Published as "Breaking the Silk Dress cryptogram," *Cryptologia* (online 2023; vol. 48 no. 5). Consensus: solved.

## What a solution would have to do
Met: a codebook, independently documented, that turns every group into station-plus-observation values; and decoded values that agree with an independent record (the Signal Service maps) that the solver did not use to fit the key. This is the strongest class of confirmation a code solution can get.

## Why the scores
Scored as of 2013–2022, before the break.
- mystery 1 today (it would have been 2: a charming curiosity, little at stake).
- material 4: complete, two legible sheets, photographed; short.
- solvable 5: a structured list of dictionary words in regular groups, plainly a telegraph code.
- compute 3: the lesson. Cryptanalysis could not break it, because a one-part code on dictionary words has no letter statistics to attack and the text is far too short to reconstruct a codebook. What worked was a search over a closed set of documents: period telegraphic codebooks, many digitized. A calibrated rubric should have said compute 3, SWEEP, not 5, ENUMERATE: computation helps by searching codebooks, not by fitting keys.
- verifiable 5: the decoded weather either matches the 1888 maps or it does not.
- crowding 3: a decade on top-unsolved lists with many amateur attempts; nobody had systematically searched codebooks.
- compute mode (retrospective): SWEEP over digitized commercial and government telegraph codebooks · verifier MECHANICAL · space ENUMERABLE · signal YES (partial codebook hits) · fit HIGH.
- Calibration point: for short word-lists in a known language, `compute` should ask "is there a closed corpus of codebooks to search?", not "can a key be fitted?" The same pattern (fell to a document, not to analysis) is recorded in NEXT-SESSION for Chaocipher and Kryptos.

## Sources
- SCHOLARLY — Wayne Chan, "Breaking the Silk Dress cryptogram," *Cryptologia* 48 (5) (published online 2023). https://www.tandfonline.com/doi/full/10.1080/01611194.2023.2223562
- SECONDARY — NOAA Heritage, "'Cryptogram' in a silk dress tells a weather story" (discovery, 170 codebooks, NOAA Central Library's 1892 code, the 27 May 1888 10 p.m. date, verification against daily weather maps, open questions). https://www.noaa.gov/heritage/stories/cryptogram-in-silk-dress-tells-weather-story
- POPULAR — Klaus Schmeh, "The Top 50 unsolved encrypted messages: 32. The silk dress cryptogram," Cipherbrain, 13 May 2017. https://scienceblogs.de/klausis-krypto-kolumne/2017/05/13/the-top-50-unsolved-encrypted-messages-32-the-silk-dress-cryptogram/
- POPULAR — CBC News, "Dress code: How a Winnipeg codebreaker cracked one of the 'world's top unsolved messages'" (2023). https://www.cbc.ca/news/canada/manitoba/code-silk-dress-cryptogram-1.7056758

## Unverified claims
- The year of the break: NOAA implies about 2022 and news coverage is from 2023; the Cryptologia paper was published online in 2023. EXCLUDED.md previously said "solved 2022"; the paper's received date was not checked.
- Whether every line decoded or a residue remained; the CBC article (403 on fetch) was not read.
- The "23 lines" count comes from search-result summaries of news reports, not from the paper.
