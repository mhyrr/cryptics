+++
title = "Sun Yat-sen's Wen Mi code telegrams, 1916–17"
slug = "sun-yat-sen-era-chinese-telegrams"
kind = "cipher"
era = "1916–1917"
origin = "China and Japan (Sun Yat-sen's circle, intercepted by the Japanese Ministry of Communications)"
language = "Chinese (classical telegraphic style)"
status = "partial"
confidence = "medium"
digitized = "https://www.jacar.archives.go.jp/das/meta/B03050090000"
tags = ["telegram", "codebook", "Chinese-telegraph-code", "code-condenser", "superencipherment", "20th-century", "JACAR", "Sun-Yat-sen", "Cryptiana"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 5
crowding = 4
+++

# Sun Yat-sen's Wen Mi code telegrams, 1916–17

## What it is
Coded telegrams of Sun Yat-sen's circle, listed in Satoshi Tomokiyo's Cryptiana as "Telegrams related to Sun Yat-sen in Wen Mi 文密 (1916)". They rest on the Chinese telegraph code, in which each character is a four-digit number in a codebook. The Japanese Ministry of Communications copied telegrams of Sun Yat-sen's circle and passed them to the Foreign Ministry, which could not read them and filed them. They survive in the Foreign Ministry records (外務省記録 1.6.1.4-2-1-2, vols 2–4) and are online at the Japan Center for Asian Historical Records (JACAR), refs B03050088300, B03050088400, B03050089100, B03050090000, B03050090100 and B03050090200. They run from March 1916 to June 1917. Most were sent as ten-letter "words" made by a *code condenser*, which turns each pair of digits into a consonant–vowel syllable. In September 2026 Daniel Bourdeau read about fifty-six of them. The residue is the traffic from July 1916 onward that is marked with the prefix 文密 *wen mi* (encoded 2429 1378), together with a few other telegrams.

Solved siblings, named for completeness and not catalogued here: the **telegram from "Tanaka" to Sun Yat-sen, 3 April 1916** (JACAR B03050738800, the "Swatow telegram"), whose condenser table Bourdeau recovered from the ciphertext alone in September 2026. It reports Mo Qingyu's rising at Chaozhou. Also solved is the **telegram from Huang Xing to Lin Hu and Li Genyuan, 25 May 1916** (JACAR B03050731500). It was filed with a contemporary decode; Bourdeau identified the system as a three-kana code, and Tomokiyo then found the mapping formula (23 September 2026). Sun Yat-sen's own telegrams with an additive of 111 had been decoded earlier by Tomokiyo.

## What is unsolved
How the 文密 telegrams of July 1916 to June 1917 were condensed. Tomokiyo, reporting Bourdeau, says they use a different code condenser with an extra vowel (y) and consonant (w). A search of about 200,000 tables in the extended family found nothing. Bourdeau thinks the condenser is a table rather than a rule. Also unread: three of the five late-May 1916 Tokyo–Shanghai telegrams that lack the usual key indicator; the June 1917 exchange with Dai Jitao, which contains groups that are not consonant–vowel pairs (e.g. "myzoasdoke", "liriopen"); and a kana-stream message of 126 ten-letter groups (B03050089100, frames 0076–0078).

## What survives
- The telegram copies, scanned and openly viewable on JACAR (B03050090000 frame 0416 has a 文密 example, July 1916). Bourdeau's transcriptions are on GitHub. The standard Chinese telegraph code (*Dian bao xin bian*) is published and machine-readable.

Excluded sibling: Cryptiana's "Telegrams found in a sunken ship Zhongshan (ca. 1938)" is not catalogued, because no corpus is available (see EXCLUDED.md).

## Prior attempts and current consensus
Tomokiyo (Cryptiana, 2021 onward) reconstructed Yamada Junzaburo's two known condensers and the +111 additive system, but could not read the Swatow telegram with them. Bourdeau (September 2026) assumed a family of condenser tables: 5 vowels in permuted order × 20 consonants in cyclic shift, ×2 fill directions, ×2 positions for 00, with optional additive, about 57,600 keys. He scored each key against a traditional-Chinese character-frequency model, and one key stood out. Seven keys of that family then read most of the March–May 1916 traffic. One telegram reports the assassination of Chen Qimei on 18 May 1916. The six-vowel extension did not read the 文密 traffic.

## What a solution would have to do
Give one condenser table (or a small stated set, tied to indicators such as 文密) that maps every two-letter syllable in the 文密 telegrams to two digits. The resulting four-digit groups must decode in the standard Chinese telegraph code to continuous, grammatical telegraphic Chinese. The decodes should name people, places and dates that fit Sun Yat-sen's documented movements in 1916–17, and wherever a reply or a plaintext copy survives, the decode should match it. The same table must work across telegrams, not be refitted to each.

## Why the scores
- mystery 2: intercepted political traffic of Sun Yat-sen's circle in the anti-Yuan period. Historians of the early Republic would use it, but no known historical question hangs on it.
- material 4: the telegrams are complete and openly scanned on JACAR, and Bourdeau has transcribed much of the traffic. It falls short of 5 because no checked, complete transcription of the 文密 telegrams is published, and their count is not stated.
- solvable 5: a state-standard codebook under a condenser, used by real correspondents.
- compute 4: for Wen Mi, the hard part is a 100-entry digit-pair-to-syllable table over a known codebook with a strong character-frequency model. That is a substitution search, and hill-climbing should handle it once enough text is pooled, whether or not the table belongs to a neat family. This is why it scores higher than a bespoke codebook would. Not 5: the 文密 table lies outside the family already enumerated, and the amount of 文密 text available to pool is unknown.
- verifiable 5: decodes come out as standard-code Chinese characters, so a reading of continuous, sensible telegraphic Chinese is a mechanical check.
- crowding 4: two serious workers (Tomokiyo, Bourdeau), both within the last five years.
- compute mode: ENUMERATE / HILL-CLIMB (condenser table over the standard code, scored by Chinese character n-grams) · verifier MECHANICAL · space SAMPLABLE · signal YES · fit HIGH.

## Sources
- PRIMARY — JACAR, 外務省記録 1.6.1.4-2-1-2, telegram copies (e.g. B03050090000, frame 0416, 文密 prefix, July 1916). https://www.jacar.archives.go.jp/das/meta/B03050090000
- PRIMARY — JACAR B03050738800 (the Swatow telegram, solved sibling). https://www.jacar.archives.go.jp/das/meta/B03050738800
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," sections "Telegrams Related to Sun Yat-Sen in Wen Mi (文密) (1916)", "Telegram to Sun Yat-sen (1916)", "Telegram from Huang Xing…". https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Solution of Two Chinese Cipher Telegrams Archived in Japan (1916)" (Bourdeau's method, the 57,600-key family, the 200,000-table Wen Mi search, the JACAR file refs, the unread residue). https://cryptiana.web.fc2.com/code/chinesecrypto_e2.htm
- CLAIMANT — Daniel Bourdeau, "Sun Yat-sen's intercepted telegrams, 1916–17" (about 56 telegrams decoded; 文密 not decoded). https://dbourdeau.github.io/cyphersolver/sunintercepts.html
- CLAIMANT — Daniel Bourdeau, the Swatow telegram writeup. https://dbourdeau.github.io/cyphersolver/sunyatsen.html

## Unverified claims
- The exact count of unread 文密 telegrams. Neither Tomokiyo nor Bourdeau states one in what was read here.
- Whether Bourdeau's "about fifty-six telegrams" includes the Swatow telegram.
- The September 2026 Bourdeau and Tomokiyo decodes have not been independently reviewed or published in a scholarly venue.
